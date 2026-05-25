from __future__ import annotations

import re
from datetime import datetime

from .constants import DATE_FIELDS, FIELD_KEYS
from .models import ExtractedField, ParserWarning, Provenance
from .normalization import (
    clean_value,
    extract_uk_postcode,
    normalize_field,
    normalize_search_text,
)
from .providers import ProviderPreset
from .readers import DocumentModel


PRESENCE_CHECK_FIELDS = {
    "vat_status": ("Yes", "No"),
    "mileage_unit": ("Miles", "Km"),
}

EVA_DATE_RE = re.compile(r"^\d{2}/\d{2}/\d{4}$")


def _raw_lines(text: str) -> list[str]:
    return [line.replace("\r", "").replace("\t", " ").strip() for line in text.splitlines()]


def _lines(text: str) -> list[str]:
    return [clean_value(line) for line in text.splitlines()]


def _line_looks_like_new_label(line: str) -> bool:
    if not line:
        return False
    if re.match(r"^[A-Za-z][A-Za-z /&()'’\-]{1,60}:$", line):
        return True
    if len(line) < 60 and line.count(":") == 1:
        left, _ = line.split(":", 1)
        return 0 < len(left.strip()) < 35
    return False


def _looks_like_section_heading(line: str) -> bool:
    stripped = line.strip()
    if not stripped or len(stripped) > 80:
        return False
    return bool(re.match(r"^[A-Z][A-Z0-9 '&()\-/]{6,}$", stripped))


def _config_tokens(config_value: str) -> list[str]:
    return [clean_value(part) for part in (config_value or "").split(",") if clean_value(part)]


def _parse_two_label_config(config_value: str) -> tuple[str, str]:
    raw = (config_value or "").strip()
    if "||" in raw:
        start, end = raw.split("||", 1)
        return start.strip(), end.strip()
    parts = [part.strip() for part in raw.splitlines() if part.strip()]
    if len(parts) >= 2:
        return parts[0], parts[1]
    return "", ""


def _extract_multiline_after_labels(text: str, labels: list[str], max_lines: int = 6) -> str:
    labels_clean = [clean_value(label) for label in labels if clean_value(label)]
    if not labels_clean:
        return ""
    lines = _raw_lines(text)
    for index, line in enumerate(lines):
        norm_line = clean_value(line).lower()
        matched = False
        for label in labels_clean:
            norm_label = label.lower()
            if norm_line == norm_label or norm_line.rstrip(":") == norm_label:
                matched = True
            elif norm_line.startswith(norm_label + ":"):
                remainder = clean_value(line.split(":", 1)[1])
                if remainder:
                    return remainder
                matched = True
            elif norm_line.startswith(norm_label) and len(norm_line) <= len(norm_label) + 2:
                matched = True
            if matched:
                break
        if not matched:
            continue
        collected: list[str] = []
        blank_run = 0
        for next_line in lines[index + 1 :]:
            cleaned = clean_value(next_line)
            if not cleaned:
                blank_run += 1
                if collected and blank_run >= 2:
                    break
                continue
            blank_run = 0
            if collected and (_line_looks_like_new_label(cleaned) or _looks_like_section_heading(cleaned)):
                break
            if collected and re.search(
                r"^(Dear Sirs|Yours faithfully|Please arrange|I act on behalf|Finally having regard)",
                cleaned,
                re.I,
            ):
                break
            collected.append(cleaned)
            if extract_uk_postcode(cleaned):
                break
            if len(collected) >= max_lines:
                break
        if collected:
            return "\n".join(collected)
    return ""


def _extract_after_label(text: str, labels: list[str], multiline: bool = False) -> str:
    if multiline:
        value = _extract_multiline_after_labels(text, labels)
        if value:
            return value
    labels_clean = [clean_value(label) for label in labels if clean_value(label)]
    if not labels_clean:
        return ""
    label_union = "|".join(re.escape(label) for label in labels_clean)
    lower_labels = {label.lower() for label in labels_clean}
    same_line_patterns = [
        re.compile(rf"(?im)^\s*(?:{label_union})\s*[:#\-|]?\s*(.+?)\s*$"),
        re.compile(rf"(?im)\b(?:{label_union})\b\s*[:#\-|]?\s*(.+)"),
    ]
    for regex in same_line_patterns:
        for match in regex.finditer(text):
            value = clean_value(match.group(1))
            if value and value.lower() not in lower_labels:
                return value
    lines = _lines(text)
    for index, line in enumerate(lines):
        if not line:
            continue
        matched = False
        for label in labels_clean:
            norm_label = label.lower()
            norm_line = line.lower()
            if norm_line == norm_label or norm_line.rstrip(":") == norm_label:
                matched = True
            elif norm_line.startswith(norm_label + ":") or norm_line.startswith(norm_label + " -"):
                remainder = clean_value(line[len(label) :])
                if remainder:
                    return remainder
                matched = True
            elif norm_line.startswith(norm_label) and len(line) <= len(label) + 2:
                matched = True
            if matched:
                break
        if matched:
            collected: list[str] = []
            for next_line in lines[index + 1 :]:
                if not next_line:
                    if collected:
                        break
                    continue
                if _line_looks_like_new_label(next_line) and collected:
                    break
                collected.append(next_line)
                if not multiline:
                    break
                if len(" ".join(collected)) > 250:
                    break
            if collected:
                return clean_value("\n".join(collected) if multiline else collected[0])
    return ""


def _extract_between_labels(text: str, start_label: str, end_label: str) -> str:
    if not start_label or not end_label:
        return ""
    pattern = re.compile(rf"(?is){re.escape(start_label)}\s*:?\s*(.*?)\s*(?={re.escape(end_label)})")
    match = pattern.search(text)
    if match:
        return clean_value(match.group(1))
    capture = False
    collected: list[str] = []
    for raw_line in text.splitlines():
        cleaned = clean_value(raw_line.rstrip())
        lower = cleaned.lower()
        if not capture:
            if lower.startswith(start_label.lower()):
                capture = True
                remainder = clean_value(re.sub(rf"(?i)^{re.escape(start_label)}\s*:?", "", cleaned))
                if remainder:
                    collected.append(remainder)
        else:
            if lower.startswith(end_label.lower()):
                break
            collected.append(cleaned)
    return clean_value("\n".join(part for part in collected if part))


def _extract_fixed_position(text: str, config_value: str) -> str:
    raw = (config_value or "").strip()
    match = re.match(r"^(\d+)\s*(?:-|:)\s*(\d+)$", raw) or re.match(r"^(\d+)$", raw)
    if not match:
        return ""
    start = int(match.group(1))
    end = int(match.group(2)) if match.lastindex and match.lastindex >= 2 and match.group(2) else start
    if start <= 0 or end < start:
        return ""
    lines = text.splitlines()
    if start > len(lines):
        return ""
    selected = [clean_value(line) for line in lines[start - 1 : end]]
    return clean_value("\n".join(line for line in selected if line))


def _extract_fixed_position_label(text: str, config_value: str) -> str:
    line_part, label = _parse_two_label_config(config_value)
    if not line_part or not label:
        return ""
    try:
        line_no = int(line_part)
    except ValueError:
        return ""
    lines = text.splitlines()
    if line_no <= 0 or line_no > len(lines):
        return ""
    target = lines[line_no - 1]
    index = target.lower().find(label.lower())
    if index < 0:
        return ""
    return clean_value(target[index + len(label) :])


def _extract_single_label_offset(text: str, config_value: str) -> str:
    label, offset_part = _parse_two_label_config(config_value)
    match = re.fullmatch(r"\s*([+\-])\s*(\d+)\s*", offset_part or "")
    if not label or not match:
        return ""
    offset = int(match.group(2)) if match.group(1) == "+" else -int(match.group(2))
    lines = text.splitlines()
    anchor = next((index for index, line in enumerate(lines) if label.lower() in line.lower()), None)
    if anchor is None:
        return ""
    if offset == 0:
        return clean_value(lines[anchor])
    step = 1 if offset > 0 else -1
    remaining = abs(offset)
    index = anchor + step
    last_seen = anchor
    while 0 <= index < len(lines) and remaining > 0:
        if lines[index].strip():
            last_seen = index
            remaining -= 1
        index += step
    return clean_value(lines[last_seen])


def _extract_email_date(text: str, config_value: str) -> str:
    label = (config_value or "").strip()
    if not label:
        return ""
    for line in text.splitlines():
        index = line.lower().find(label.lower())
        if index < 0:
            continue
        tail = line[index + len(label) :]
        match = re.search(r"\b(\d{4}-\d{1,2}-\d{1,2})\b", tail)
        if match:
            return match.group(1)
    return ""


def _first_regex_match(text: str, patterns: list[str]) -> str:
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            return clean_value(match.group(1))
    return ""


def _extract_vrm_fallback(text: str) -> str:
    table_value = _extract_client_vehicle_table_value(text, "reg")
    if table_value:
        return table_value
    lines = _lines(text)
    for line in lines:
        if re.search(r"\b(vrm|reg(?:istration)?(?: no)?|vehicle reg)\b", line, re.I):
            match = re.search(r"\b[A-Z]{2}\d{2}\s?[A-Z]{3}\b|\b[A-Z]\d{1,3}\s?[A-Z]{3}\b", line, re.I)
            if match:
                return match.group(0)
    return _first_regex_match(text, [r"\b([A-Z]{2}\d{2}\s?[A-Z]{3})\b", r"\b([A-Z]\d{1,3}\s?[A-Z]{3})\b"])


def _extract_reference_fallback(text: str) -> str:
    value = _extract_after_label(
        text,
        [
            "Our Ref",
            "Our Ref:",
            "Our Reference",
            "Reference",
            "Reference No",
            "Ref",
            "Claim No",
            "Claim Number",
        ],
    )
    if value:
        return value
    return _first_regex_match(
        text,
        [
            r"(?im)^\s*(?:our\s+reference|our\s+ref|reference|ref(?:erence)?|claim\s+no)\s*[:#\-]?\s*([A-Z0-9./_-]{4,})",
            r"(?im)^\s*((?=[^\n]*\d)[A-Z]{2,5}\d[A-Z0-9./_ -]{4,})\s*$",
            r"(?im)^\s*((?=[^\n]*\d)[A-Z]{1,5}[:./-][A-Z0-9][^\n]{3,})\s*$",
        ],
    )


def _extract_claimant_name_fallback(text: str) -> str:
    value = _extract_after_label(text, ["Client/Insured", "Client", "Claimant", "Insured", "Our Client"])
    if value:
        return value
    titled_name = re.compile(r"^(Mr|Mrs|Miss|Ms|Dr|Mx|Prof)\.?\s+[A-Z][A-Za-z'’\-]+(?:\s+[A-Z][A-Za-z'’\-]+){0,4}$")
    for line in _lines(text)[:80]:
        if titled_name.match(line):
            return line
    return ""


def _extract_vehicle_model_fallback(text: str) -> str:
    table_value = _extract_client_vehicle_table_value(text, "model")
    if table_value:
        return table_value
    vehicle_line = re.compile(
        r"(?im)^\s*(?:vehicle|vehicle\s+model|client'?s\s+vehicle|make\s*/\s*model|make\s+and\s+model)\s*[:#\-]\s*(.+?)\s*$"
    )
    for match in vehicle_line.finditer(text):
        value = clean_value(match.group(1))
        value = re.split(
            r"\b(?:colour|color|speedo|mileage|reg(?:istration)?(?:\s+no)?|vin\s+no|registered|type|trans)\s*:",
            value,
            maxsplit=1,
            flags=re.IGNORECASE,
        )[0]
        value = re.sub(r"\b[A-Z]{2}\d{2}\s?[A-Z]{3}\b", "", value, flags=re.IGNORECASE)
        value = clean_value(value)
        if value:
            return value
    return ""


def _extract_client_vehicle_table_value(text: str, value_type: str) -> str:
    lines = _lines(text)
    client_header = next(
        (
            index
            for index, line in enumerate(lines)
            if re.search(r"\bclients?\s+vehicle\b", line, re.IGNORECASE)
            and index + 1 < len(lines)
            and re.search(r"\bthird\s+party\s+vehicle\b", lines[index + 1], re.IGNORECASE)
        ),
        None,
    )
    if client_header is None:
        return ""
    label_re = r"vehicle\s+model" if value_type == "model" else r"vehicle\s+reg"
    for index in range(client_header + 2, min(len(lines), client_header + 24)):
        if not re.search(label_re, lines[index], re.IGNORECASE):
            continue
        for candidate in lines[index + 1 : min(len(lines), index + 5)]:
            if not candidate or re.search(r"^(third party|vehicle|client|tp vehicle)", candidate, re.IGNORECASE):
                continue
            return clean_value(candidate)
    return ""


def _extract_date_fallback(text: str, field_name: str) -> str:
    date_pattern = r"(\d{1,2}(?:st|nd|rd|th)?\s+[A-Za-z]+\s+\d{4}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{1,2}-\d{1,2})"
    label_sets = {
        "incident_date": ["Incident", "Incident Date", "Accident Date", "Date of Accident", "Loss Date"],
        "instruction_date": ["Instruction Date", "Date Instructed", "Instructions Received", "Instructed"],
        "inspection_date": ["Inspection Date", "Date of Inspection", "Date Inspected", "Date"],
    }
    if field_name == "instruction_date":
        value = _first_regex_match(
            text,
            [rf"(?is)\binstructions\s+received\s+on\s+{date_pattern}"],
        )
        if value:
            return value
    for label in label_sets.get(field_name, []):
        value = _extract_after_label(text, [label])
        match = re.search(date_pattern, value, re.IGNORECASE)
        if match:
            return clean_value(match.group(1))
    keyword_union = "|".join(re.escape(label) for label in label_sets.get(field_name, []) if label)
    if keyword_union:
        value = _first_regex_match(text, [rf"(?im)(?:{keyword_union})\s*[:#\-]?\s*{date_pattern}"])
        if value:
            return value
    if field_name == "instruction_date":
        for line in _lines(text)[:80]:
            if re.search(r"\b(accident|incident|loss)\b", line, re.IGNORECASE):
                continue
            match = re.search(date_pattern, line, re.IGNORECASE)
            if match:
                return clean_value(match.group(1))
    return ""


def _extract_inspection_address_fallback(text: str) -> str:
    if re.search(r"\b(desktop\s+assessment|desktop\s+review|image[-\s]?based\s+assessment)\b", text, re.IGNORECASE):
        return "Image-based Assessment"
    return _extract_multiline_after_labels(
        text,
        [
            "Inspection Address",
            "Inspection Location",
            "Vehicle Location",
            "Vehicle location",
            "Vehicle is currently located at",
            "currently located at",
            "currently stored at",
            "Address",
        ],
        max_lines=7,
    )


def _extract_accident_circumstances_fallback(text: str) -> str:
    value = _first_regex_match(
        text,
        [
            r"(?is)\bNATURE\s+OF\s+INCIDENT\s*(.+?)(?=\n\s*(?:ENGINEER'?S\s+COMMENTS|VEHICLE\s+HISTORY|REPAIR\s+SCHEDULE|[A-Z][A-Z '&/\-]{8,})\s*\n)",
        ],
    )
    if value:
        return clean_value(value)
    value = _extract_after_label(text, ["Accident Circumstances", "Circumstances", "Incident Circumstances"], multiline=True)
    if value:
        return value
    return _extract_after_label(text, ["Damage"], multiline=True)


def _extract_mileage_fallback(text: str) -> str:
    value = _extract_after_label(text, ["Mileage", "Speedo", "Odometer"])
    if value:
        return value
    return _first_regex_match(text, [r"\b(\d{1,3}(?:,\d{3})+|\d{4,7})\s*(?:miles?|kms?|kilomet(?:er|re)s?)\b"])


def _extract_mileage_unit_fallback(text: str) -> str:
    if re.search(r"\b(\d{1,3}(?:,\d{3})+|\d{4,7})\s*(miles?)\b", text, re.IGNORECASE):
        return "Miles"
    if re.search(r"\b(\d{1,3}(?:,\d{3})+|\d{4,7})\s*(kms?|kilomet(?:er|re)s?)\b", text, re.IGNORECASE):
        return "Km"
    lines = _lines(text)
    for index, line in enumerate(lines):
        if re.search(r"\b(speedo|mileage|odometer)\b", line, re.IGNORECASE):
            window = " ".join(lines[index : index + 3])
            if re.search(r"\bmiles?\b", window, re.IGNORECASE):
                return "Miles"
            if re.search(r"\b(kms?|kilomet(?:er|re)s?)\b", window, re.IGNORECASE):
                return "Km"
    return ""


def _extract_vat_status_fallback(text: str) -> str:
    if re.search(r"\b(not\s+vat\s+registered|non[-\s]?vat|no\s+vat|vat\s+status\s*[:#\-]?\s*no)\b", text, re.IGNORECASE):
        return "No"
    if re.search(r"\b(vat\s+status\s*[:#\-]?\s*yes|vat\s+registered)\b", text, re.IGNORECASE):
        return "Yes"
    return ""


def _derive_provider_code(provider: ProviderPreset | None) -> str:
    if provider is None:
        return ""
    if provider.code:
        return provider.code
    prefix = provider.name.split("(", 1)[0].strip()
    return re.sub(r"[^A-Za-z0-9]+", "", prefix).upper()


def _fallback_by_field(text: str, field_name: str, provider: ProviderPreset | None) -> str:
    if field_name == "work_provider":
        return _derive_provider_code(provider)
    if field_name == "vrm":
        return _extract_vrm_fallback(text)
    if field_name == "vehicle_model":
        return _extract_vehicle_model_fallback(text)
    if field_name == "claimant_name":
        return _extract_claimant_name_fallback(text)
    if field_name == "reference":
        return _extract_reference_fallback(text)
    if field_name in {"incident_date", "instruction_date", "inspection_date"}:
        return _extract_date_fallback(text, field_name)
    if field_name == "inspection_address":
        return _extract_inspection_address_fallback(text)
    if field_name == "accident_circumstances":
        return _extract_accident_circumstances_fallback(text)
    if field_name == "vat_status":
        return _extract_vat_status_fallback(text)
    if field_name == "mileage":
        return _extract_mileage_fallback(text)
    if field_name == "mileage_unit":
        return _extract_mileage_unit_fallback(text)
    return ""


def _is_eva_date(value: str) -> bool:
    return bool(EVA_DATE_RE.match((value or "").strip()))


def _looks_like_bad_reference(value: str) -> bool:
    candidate = clean_value(value)
    if not candidate:
        return False
    if any(char.isdigit() for char in candidate):
        return False
    if len(candidate) <= 4:
        return True
    return bool(re.search(r"[^\x20-\x7e]", candidate))


def _extract_by_rule(text: str, field_name: str, rule: dict) -> str:
    method = str((rule or {}).get("method") or "single_label")
    config = str((rule or {}).get("config", "") or "")
    tokens = _config_tokens(config)
    if method == "single_label":
        return _extract_after_label(text, tokens)
    if method == "two_labels":
        start, end = _parse_two_label_config(config)
        value = _extract_between_labels(text, start, end)
        if field_name.endswith("_date") and value:
            date_match = re.search(
                r"\b(\d{1,2}(?:st|nd|rd|th)?\s+[A-Za-z]+\s+\d{4}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b",
                value,
                re.IGNORECASE,
            )
            if date_match:
                return clean_value(date_match.group(1))
        return value
    if method == "fixed_position":
        return _extract_fixed_position(text, config)
    if method == "fixed_position_label":
        return _extract_fixed_position_label(text, config)
    if method == "single_label_offset":
        return _extract_single_label_offset(text, config)
    if method == "email_date":
        return _extract_email_date(text, config)
    if method == "manual_input":
        if config.strip().lower() == "{today}":
            return datetime.now().strftime("%d/%m/%Y")
        return config.strip()
    if method == "regex":
        return _first_regex_match(text, tokens)
    if method == "vrm_fallback":
        return _extract_vrm_fallback(text)
    if method == "reference_fallback":
        return _extract_reference_fallback(text)
    if method == "address_fallback":
        return _extract_inspection_address_fallback(text)
    if method in {"fixed_value", "current_date", "blank"}:
        return config.strip() if method == "fixed_value" else (datetime.now().strftime("%d/%m/%Y") if method == "current_date" else "")
    return _extract_after_label(text, tokens)


def _resolve_presence_check(text: str, field_name: str, rule: dict) -> str:
    config = str((rule or {}).get("config", "") or "").strip()
    if not config:
        return ""
    tokens = [clean_value(part) for part in config.splitlines() if clean_value(part)]
    if not tokens:
        tokens = _config_tokens(config)
    haystack = text.lower()
    if field_name == "vat_status" and re.search(r"\b(not\s+vat\s+registered|non[-\s]?vat|no\s+vat)\b", haystack):
        return "No"
    for token in tokens:
        needle = token.lower()
        if needle and needle in haystack:
            return PRESENCE_CHECK_FIELDS[field_name][0]
    return PRESENCE_CHECK_FIELDS[field_name][1]


def _provenance_for(document: DocumentModel, raw_value: str, method: str) -> list[Provenance]:
    if not raw_value:
        return []
    index = document.text.lower().find(raw_value.lower())
    span = (index, index + len(raw_value)) if index >= 0 else None
    snippet = raw_value if len(raw_value) <= 240 else raw_value[:237] + "..."
    return [
        Provenance(
            source_file_id=document.source_file.file_id,
            extraction_method=method,
            text_span=span,
            snippet=snippet,
        )
    ]


def extract_fields(document: DocumentModel, provider: ProviderPreset | None) -> dict[str, ExtractedField]:
    fields: dict[str, ExtractedField] = {}
    text = document.text or ""
    for field_name in FIELD_KEYS:
        raw = ""
        method = "unmapped"
        confidence = 0.0
        warnings: list[ParserWarning] = []
        if provider is not None:
            if field_name == "work_provider":
                rule = provider.field_rules.get("work_provider", {})
                raw = str(rule.get("config", "") or "").strip()
                method = "provider_manual_rule"
                confidence = 1.0 if raw else 0.0
            else:
                rule = provider.field_rules.get(field_name, {})
                config = str(rule.get("config", "") or "").strip()
                method = str(rule.get("method", "single_label") or "single_label")
                if config:
                    if field_name in PRESENCE_CHECK_FIELDS:
                        raw = _resolve_presence_check(text, field_name, rule)
                    else:
                        raw = _extract_by_rule(text, field_name, rule)
                    confidence = 0.92 if raw else 0.0
        if not raw:
            fallback = _fallback_by_field(text, field_name, provider)
            if fallback:
                raw = fallback
                method = "deterministic_fallback"
                confidence = 0.78 if field_name != "work_provider" else 0.72
        normalized = normalize_field(
            field_name,
            raw,
            force_postcode=bool(provider and provider.force_postcode_for_inspection_address),
        )
        if raw and field_name in DATE_FIELDS and not _is_eva_date(normalized):
            fallback = _fallback_by_field(text, field_name, provider)
            fallback_normalized = normalize_field(field_name, fallback)
            if fallback and _is_eva_date(fallback_normalized):
                raw = fallback
                normalized = fallback_normalized
                method = "deterministic_fallback"
                confidence = 0.78
            else:
                warnings.append(
                    ParserWarning(
                        code="invalid_primary_date_suppressed",
                        message=f"{field_name} primary extraction produced a non-date value and requires review.",
                        severity="warning",
                        source_file_id=document.source_file.file_id,
                    )
                )
                raw = ""
                normalized = ""
                method = "invalid_primary_suppressed"
                confidence = 0.0
        elif raw and field_name == "reference" and _looks_like_bad_reference(raw):
            fallback = _fallback_by_field(text, field_name, provider)
            if fallback and not _looks_like_bad_reference(fallback):
                raw = fallback
                normalized = normalize_field(field_name, fallback)
                method = "deterministic_fallback"
                confidence = 0.78
            else:
                warnings.append(
                    ParserWarning(
                        code="invalid_primary_reference_suppressed",
                        message="Reference primary extraction looked like document-control noise and requires review.",
                        severity="warning",
                        source_file_id=document.source_file.file_id,
                    )
                )
                raw = ""
                normalized = ""
                method = "invalid_primary_suppressed"
                confidence = 0.0
        elif raw and field_name == "vehicle_model":
            fallback = _fallback_by_field(text, field_name, provider)
            if fallback and len(fallback) > len(raw) + 3 and raw.lower() not in fallback.lower():
                raw = fallback
                normalized = normalize_field(field_name, fallback)
                method = "deterministic_fallback"
                confidence = 0.78
        if field_name == "inspection_date" and provider and provider.use_current_date_for_inspection_date:
            raw = datetime.now().strftime("%d/%m/%Y")
            normalized = raw
            method = "provider_current_date_policy"
            confidence = 0.8
        if raw and not normalized:
            warnings.append(
                ParserWarning(
                    code="normalization_empty",
                    message=f"{field_name} produced a raw value that normalized to blank.",
                    severity="warning",
                    source_file_id=document.source_file.file_id,
                )
            )
        fields[field_name] = ExtractedField(
            name=field_name,
            raw_value=raw,
            normalized_value=normalized,
            confidence=confidence,
            provenance=_provenance_for(document, raw, method),
            warnings=warnings,
            review_state="unreviewed" if normalized else "review_required",
        )
    return fields


def detect_inspection_mode(fields: dict[str, ExtractedField]) -> tuple[str, str, list[str], str | None, float, list[Provenance]]:
    field = fields.get("inspection_address")
    value = (field.normalized_value if field else "") or ""
    lines = value.split("\n") if value else []
    if value.strip().lower().startswith("image-based assessment"):
        return "image_based", "provider_manual_rule", lines, None, 0.95, list(field.provenance if field else [])
    if any(line.strip() for line in lines):
        postcode = lines[-1].strip() if len(lines) >= 6 and lines[-1].strip() else extract_uk_postcode(value)
        return "physical", "instruction_text", lines, postcode or None, 0.85, list(field.provenance if field else [])
    return "review_required", "unknown", [""] * 6, None, 0.0, []
