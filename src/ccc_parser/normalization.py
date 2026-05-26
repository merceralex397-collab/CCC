from __future__ import annotations

import re
from datetime import datetime


def clean_value(value: str | None) -> str:
    value = (value or "").replace("\r", " ").replace("\t", " ")
    value = re.sub(r"[ ]{2,}", " ", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip(" :\n")


def normalize_search_text(value: str | None) -> str:
    value = (value or "").lower().replace("\r", "\n").replace("\t", " ")
    value = re.sub(r"[^\w\n ]+", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def split_preserving_nonempty_lines(text: str | None) -> list[str]:
    return [part.strip() for part in (text or "").splitlines() if part.strip()]


def extract_uk_postcode(value: str | None) -> str:
    if not value:
        return ""
    match = re.search(r"\b([A-Z]{1,2}\d[A-Z\d]?\s*\d[ABD-HJLNP-UW-Z]{2})\b", value, re.IGNORECASE)
    if not match:
        return ""
    compact = re.sub(r"\s+", "", match.group(1).upper())
    if len(compact) < 5:
        return ""
    return f"{compact[:-3]} {compact[-3:]}"


def normalize_vrm(value: str | None) -> str:
    return re.sub(r"\s+", "", (value or "").strip()).upper()


def normalize_mileage(value: str | None) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    digits: list[str] = []
    started = False
    for char in raw:
        if char.isdigit():
            digits.append(char)
            started = True
            continue
        if started:
            if char == ",":
                continue
            break
    return "".join(digits)


def normalize_yes_no(value: str | None) -> str:
    lowered = (value or "").strip().lower()
    if not lowered:
        return ""
    if any(token in lowered for token in ("not vat", "non vat", "no vat", "not registered")):
        return "No"
    if lowered in {"yes", "y", "true", "1", "vat registered", "registered"}:
        return "Yes"
    if lowered in {"no", "n", "false", "0"}:
        return "No"
    return (value or "").strip()


def normalize_date(value: str | None) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""

    iso_match = re.search(r"\b(\d{4}-\d{1,2}-\d{1,2})\b", raw)
    if iso_match:
        raw = iso_match.group(1)

    cleaned = re.sub(r"(\d+)\s*(st|nd|rd|th)\b", r"\1", raw, flags=re.IGNORECASE)
    cleaned = cleaned.replace(",", " ")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    formats = [
        "%d/%m/%Y",
        "%d/%m/%y",
        "%d-%m-%Y",
        "%d-%m-%y",
        "%d %B %Y",
        "%d %b %Y",
        "%d-%B-%Y",
        "%d-%b-%Y",
        "%B %d %Y",
        "%b %d %Y",
        "%Y-%m-%d",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(cleaned, fmt).strftime("%d/%m/%Y")
        except ValueError:
            continue
    return raw


def normalize_inspection_address(value: str | None, force_postcode: bool = False) -> str:
    text = (value or "").strip()
    if not text:
        return ""
    if text.lower() == "image-based assessment":
        return "\n".join(["Image-based Assessment", "", "", "", "", ""])

    def canonical_postcode(postcode_text: str) -> str:
        compact = re.sub(r"\s+", "", (postcode_text or "").upper())
        if len(compact) < 5:
            return ""
        return f"{compact[:-3]} {compact[-3:]}"

    postcode_anywhere = re.compile(r"\b([A-Z]{1,2}\d[A-Z\d]?\s*\d[ABD-HJLNP-UW-Z]{2})\b", re.IGNORECASE)
    postcode_at_end = re.compile(r"\b([A-Z]{1,2}\d[A-Z\d]?\s*\d[ABD-HJLNP-UW-Z]{2})\b\s*$", re.IGNORECASE)

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\s*,\s*", "\n", text)
    raw_lines = split_preserving_nonempty_lines(text)
    if not raw_lines:
        return ""

    postcode_line = ""
    body_lines: list[str] = []
    if len(raw_lines) == 1:
        single_line = raw_lines[0]
        if force_postcode:
            end_match = postcode_at_end.search(single_line)
            anywhere_match = postcode_anywhere.search(single_line)
            match = end_match or anywhere_match
            if match:
                postcode_line = canonical_postcode(match.group(1))
                pre = single_line[: match.start()].strip(" ,")
                body_lines = [pre] if pre else []
            else:
                body_lines = raw_lines[:]
        else:
            end_match = postcode_at_end.search(single_line)
            if end_match:
                postcode_line = canonical_postcode(end_match.group(1))
                pre = single_line[: end_match.start()].strip(" ,")
                body_lines = [pre] if pre else []
            else:
                body_lines = raw_lines[:]
    else:
        last_line = raw_lines[-1]
        match = postcode_anywhere.search(last_line)
        if match:
            postcode_line = canonical_postcode(match.group(1))
            trailing = last_line[match.end() :].strip()
            body_lines = raw_lines[:-1]
            pre = last_line[: match.start()].strip(" ,")
            if pre:
                body_lines.append(pre)
            if trailing and not re.fullmatch(r"[\d\s+()/-]+", trailing):
                body_lines.append(trailing)
        else:
            body_lines = raw_lines[:-1]
            postcode_line = last_line

    if len(body_lines) >= 5:
        normalized = body_lines[:4] + [" ".join(part for part in body_lines[4:] if part), postcode_line]
    else:
        normalized = body_lines[:5] + [""] * (5 - len(body_lines[:5])) + [postcode_line]
    return "\n".join(part.strip() for part in normalized[:6])


def normalize_field(field_name: str, value: str | None, *, force_postcode: bool = False) -> str:
    if field_name == "vrm":
        return normalize_vrm(value)
    if field_name == "inspection_address":
        return normalize_inspection_address(value, force_postcode=force_postcode)
    if field_name == "mileage":
        return normalize_mileage(value)
    if field_name in {"incident_date", "instruction_date", "inspection_date"}:
        return normalize_date(value)
    if field_name == "vat_status":
        return normalize_yes_no(value)
    if field_name == "mileage_unit":
        lowered = (value or "").lower()
        if "mile" in lowered:
            return "Miles"
        if "km" in lowered or "kilomet" in lowered:
            return "Km"
    return (value or "").strip()
