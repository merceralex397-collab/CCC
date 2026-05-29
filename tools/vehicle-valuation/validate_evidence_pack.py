"""Validate vehicle valuation payloads before PDF rendering."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_SUBJECT = [
    "registration",
    "make",
    "model",
    "body_type",
    "fuel",
    "transmission",
    "engine",
    "first_registered",
    "mileage",
]

REQUIRED_ADVERT = [
    "source",
    "url",
    "price",
    "make",
    "model",
    "derivative_or_engine",
    "registration_year",
    "mileage",
    "fuel",
    "transmission",
    "body_style",
    "seller_type",
    "location",
    "date_accessed",
    "comparability_note",
    "differences_note",
    "supports_assessed_value",
    "evidence_role",
    "is_materially_comparable",
]

OPTIONAL_WARN = ["advert_id", "screenshot_path"]
COMMERCIAL_WARN = ["vat_status", "admin_fee", "delivery_fee"]
REQUIRED_NARRATIVE = ["market_research", "conclusion"]
VALID_EVIDENCE_ROLES = {"supportive", "limiting", "contextual", "excluded"}
VALID_VALUATION_MODES = {"guide_supported", "market_only"}
FORBIDDEN_EXTERNAL_PATTERNS = [
    ("EVA", re.compile(r"\bEVA\b", re.IGNORECASE)),
    ("uplift", re.compile(r"\buplift(?:s|ed|ing)?\b", re.IGNORECASE)),
    ("guide value", re.compile(r"\bguide\s+value\b", re.IGNORECASE)),
    ("guide valuation", re.compile(r"\bguide\s+valuation\b", re.IGNORECASE)),
    ("guide price", re.compile(r"\bguide\s+price\b", re.IGNORECASE)),
    ("Engineer Value", re.compile(r"\bEngineer\s+Value\b", re.IGNORECASE)),
    ("Original Eng Value", re.compile(r"\bOriginal\s+Eng(?:ineer)?\s+Value\b", re.IGNORECASE)),
]
MISSING_STRINGS = {
    "n/a",
    "na",
    "none",
    "not applicable",
    "not provided",
    "not supplied",
    "not stated",
    "not visible",
    "not known",
    "tbc",
    "to be confirmed",
    "unknown",
}
MISSING_PREFIXES = {
    "not applicable",
    "not provided",
    "not supplied",
    "not stated",
    "not visible",
    "not known",
    "to be confirmed",
}


def load_payload(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _is_missing(value: Any) -> bool:
    if value is None or value == "":
        return True
    if isinstance(value, str):
        cleaned = " ".join(value.strip().lower().split())
        if not cleaned:
            return True
        return cleaned in MISSING_STRINGS or any(cleaned.startswith(token + " ") for token in MISSING_PREFIXES)
    return False


def _missing(mapping: dict[str, Any], fields: list[str]) -> list[str]:
    missing = []
    for field in fields:
        if _is_missing(mapping.get(field)):
            missing.append(field)
    return missing


def _append_pdf_text(fields: list[tuple[str, str]], path: str, value: Any) -> None:
    if _is_missing(value):
        return
    fields.append((path, str(value)))


def _pdf_bound_text_fields(payload: dict[str, Any]) -> list[tuple[str, str]]:
    fields: list[tuple[str, str]] = []
    subject = payload.get("subject_vehicle")
    if isinstance(subject, dict):
        for key in [
            "registration",
            "vehicle_description",
            "make",
            "model",
            "derivative",
            "body_type",
            "fuel",
            "transmission",
            "engine",
            "first_registered",
            "mileage",
            "colour",
            "vehicle_history",
            "vin",
        ]:
            _append_pdf_text(fields, f"subject_vehicle.{key}", subject.get(key))

    for key in ["intro", "market_research", "conclusion", "vat_note", "search_summary"]:
        _append_pdf_text(fields, key, payload.get(key))

    commentary = payload.get("valuation_commentary")
    if isinstance(commentary, list):
        for index, paragraph in enumerate(commentary, start=1):
            _append_pdf_text(fields, f"valuation_commentary[{index}]", paragraph)

    adverts = payload.get("adverts")
    if isinstance(adverts, list):
        for index, advert in enumerate(adverts, start=1):
            if not isinstance(advert, dict):
                continue
            for key in [
                "source",
                "price",
                "make",
                "model",
                "derivative_or_engine",
                "registration_year",
                "mileage",
                "fuel",
                "transmission",
                "body_style",
                "seller_type",
                "location",
                "report_comment",
            ]:
                _append_pdf_text(fields, f"adverts[{index}].{key}", advert.get(key))
    return fields


def _external_wording_errors(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for path, value in _pdf_bound_text_fields(payload):
        for label, pattern in FORBIDDEN_EXTERNAL_PATTERNS:
            if pattern.search(value):
                errors.append(f"External PDF wording contains forbidden term '{label}' in {path}")
    return errors


def _validate_evidence_assessment(payload: dict[str, Any], adverts: list[Any]) -> list[str]:
    errors: list[str] = []
    assessment = payload.get("evidence_assessment")
    if not isinstance(assessment, dict):
        return ["Missing object: evidence_assessment"]
    if assessment.get("sufficient_for_pdf") is not True:
        errors.append("evidence_assessment.sufficient_for_pdf must be true before rendering PDFs")
    if _is_missing(assessment.get("basis")):
        errors.append("evidence_assessment.basis missing or placeholder")

    suitable_adverts = [
        advert
        for advert in adverts
        if isinstance(advert, dict) and advert.get("evidence_role") != "excluded"
    ]
    supportive_comparable = [
        advert
        for advert in suitable_adverts
        if advert.get("supports_assessed_value") is True
        and advert.get("is_materially_comparable") is True
        and advert.get("evidence_role") == "supportive"
    ]
    if len(suitable_adverts) < 3:
        errors.append("At least three suitable live adverts are required before rendering PDFs")
    if len(supportive_comparable) < 2:
        errors.append("At least two materially comparable adverts must support the assessed retail value before rendering PDFs")
    return errors


def _validate_valuation_mode(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    mode = payload.get("valuation_mode", "guide_supported")
    if mode not in VALID_VALUATION_MODES:
        errors.append(
            "valuation_mode must be one of: " + ", ".join(sorted(VALID_VALUATION_MODES))
        )
        return errors

    if mode == "guide_supported":
        if _is_missing(payload.get("guide_value")):
            errors.append("Missing or placeholder field: guide_value")
    else:
        if _is_missing(payload.get("guide_value_unavailable_reason")):
            errors.append(
                "guide_value_unavailable_reason missing or placeholder for market_only valuation_mode"
            )
    return errors


def validate_payload(payload: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    subject = payload.get("subject_vehicle")
    if not isinstance(subject, dict):
        errors.append("Missing object: subject_vehicle")
    else:
        missing_subject = _missing(subject, REQUIRED_SUBJECT)
        if missing_subject:
            errors.append("subject_vehicle missing or placeholder: " + ", ".join(missing_subject))
        if "vehicle_description" in subject and _is_missing(subject.get("vehicle_description")):
            errors.append("subject_vehicle.vehicle_description is placeholder: remove it or provide the exact visible Vehicle text")

    meta = payload.get("meta")
    if not isinstance(meta, dict):
        errors.append("Missing object: meta")
    elif _is_missing(meta.get("your_ref")):
        errors.append("meta.your_ref missing or placeholder: ask for the claim or matter reference before rendering")

    errors.extend(_validate_valuation_mode(payload))

    for field in ["assessed_retail_value", "adverts"]:
        if _is_missing(payload.get(field)):
            errors.append(f"Missing or placeholder field: {field}")

    for field in REQUIRED_NARRATIVE:
        if _is_missing(payload.get(field)):
            errors.append(f"Missing or placeholder field: {field}")

    commentary = payload.get("valuation_commentary")
    if not isinstance(commentary, list) or not commentary:
        errors.append("valuation_commentary must be a non-empty list")
    else:
        missing_commentary = [str(index) for index, paragraph in enumerate(commentary, start=1) if _is_missing(paragraph)]
        if missing_commentary:
            errors.append("valuation_commentary contains placeholder/empty paragraphs: " + ", ".join(missing_commentary))

    adverts = payload.get("adverts")
    if not isinstance(adverts, list) or not adverts:
        errors.append("adverts must be a non-empty list")
        return errors, warnings

    errors.extend(_validate_evidence_assessment(payload, adverts))

    is_commercial = bool(payload.get("is_commercial_vehicle")) or str(subject.get("body_type", "") if isinstance(subject, dict) else "").lower() in {
        "van",
        "pickup",
        "commercial",
    }

    for index, advert in enumerate(adverts, start=1):
        if not isinstance(advert, dict):
            errors.append(f"advert {index} must be an object")
            continue
        missing_advert = _missing(advert, REQUIRED_ADVERT)
        if missing_advert:
            errors.append(f"advert {index} missing or placeholder: " + ", ".join(missing_advert))
        if "supports_uplift" in advert:
            errors.append(f"advert {index} uses deprecated supports_uplift; use supports_assessed_value and evidence_role")
        if not isinstance(advert.get("supports_assessed_value"), bool):
            errors.append(f"advert {index} supports_assessed_value must be boolean")
        if not isinstance(advert.get("is_materially_comparable"), bool):
            errors.append(f"advert {index} is_materially_comparable must be boolean")
        if advert.get("evidence_role") not in VALID_EVIDENCE_ROLES:
            errors.append(
                f"advert {index} evidence_role must be one of: " + ", ".join(sorted(VALID_EVIDENCE_ROLES))
            )
        missing_optional = _missing(advert, OPTIONAL_WARN)
        if missing_optional:
            warnings.append(f"advert {index} optional fields missing: " + ", ".join(missing_optional))
        if is_commercial:
            missing_commercial = _missing(advert, COMMERCIAL_WARN)
            if missing_commercial:
                warnings.append(f"advert {index} commercial fields missing: " + ", ".join(missing_commercial))

    errors.extend(_external_wording_errors(payload))
    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if len(argv) != 1:
        print("Usage: validate_evidence_pack.py <payload.json>", file=sys.stderr)
        return 2

    payload = load_payload(argv[0])
    errors, warnings = validate_payload(payload)
    for warning in warnings:
        print("WARNING: " + warning, file=sys.stderr)
    if errors:
        print("Payload validation failed:", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1
    print("Payload validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
