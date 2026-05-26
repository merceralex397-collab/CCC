from __future__ import annotations

import re

from .constants import DATE_FIELDS
from .models import ExtractedField, ParserWarning, ValidationIssue, ValidationResult


DATE_RE = re.compile(r"^\d{2}/\d{2}/\d{4}$")


def _value(fields: dict[str, ExtractedField], name: str) -> str:
    field = fields.get(name)
    value = ((field.normalized_value if field else "") or "")
    return value if name == "inspection_address" else value.strip()


def validate_fields(
    fields: dict[str, ExtractedField],
    *,
    detected_provider: str | None,
    parser_warnings: list[ParserWarning],
    has_images: bool = False,
    export_required: bool = True,
) -> ValidationResult:
    blockers: list[ValidationIssue] = []
    warnings: list[ValidationIssue] = []

    if not export_required:
        blockers.append(
            ValidationIssue(
                code="not_instruction_export_candidate",
                message="This item is not an instruction export candidate and should be routed as evidence/review material.",
            )
        )
    if export_required and not detected_provider:
        blockers.append(
            ValidationIssue(
                code="provider_not_detected",
                message="No provider preset matched the available source text.",
                field="work_provider",
            )
        )
    if export_required and not _value(fields, "work_provider"):
        blockers.append(
            ValidationIssue(
                code="missing_work_provider",
                message="Work Provider is required before EVA export.",
                field="work_provider",
            )
        )
    if export_required and not _value(fields, "vrm"):
        blockers.append(ValidationIssue(code="missing_vrm", message="VRM is required before EVA export.", field="vrm"))

    inspection_address = _value(fields, "inspection_address")
    if export_required and (not inspection_address or not any(line.strip() for line in inspection_address.split("\n"))):
        blockers.append(
            ValidationIssue(
                code="missing_inspection_address",
                message="Inspection Address or Image-based Assessment marker is required before EVA export.",
                field="inspection_address",
            )
        )
    elif export_required and len(inspection_address.split("\n")) != 6:
        blockers.append(
            ValidationIssue(
                code="invalid_inspection_address_shape",
                message="Inspection Address must be six-line compatible for EVA export.",
                field="inspection_address",
            )
        )

    for field_name in sorted(DATE_FIELDS):
        value = _value(fields, field_name)
        if export_required and value and not DATE_RE.match(value):
            blockers.append(
                ValidationIssue(
                    code=f"invalid_{field_name}",
                    message=f"{field_name} must be formatted as DD/MM/YYYY for EVA export.",
                    field=field_name,
                )
            )

    if export_required and not _value(fields, "mileage"):
        blockers.append(ValidationIssue(code="missing_mileage", message="Mileage requires review.", field="mileage"))
    if export_required and not _value(fields, "vat_status"):
        blockers.append(ValidationIssue(code="missing_vat_status", message="VAT Status requires review.", field="vat_status"))
    if export_required and not _value(fields, "mileage_unit"):
        blockers.append(
            ValidationIssue(code="missing_mileage_unit", message="Mileage Unit requires review.", field="mileage_unit")
        )
    if has_images:
        warnings.append(
            ValidationIssue(
                code="image_order_requires_review",
                message="Image package ordering must be reviewed before package export.",
                severity="warning",
                field="images",
            )
        )
    for warning in parser_warnings:
        if warning.severity == "blocker":
            blockers.append(ValidationIssue(code=warning.code, message=warning.message, field=None))
        elif warning.severity == "warning":
            warnings.append(
                ValidationIssue(code=warning.code, message=warning.message, severity="warning", field=None)
            )
    return ValidationResult(blockers=blockers, warnings=warnings)
