from __future__ import annotations

from dataclasses import replace

from .models import ExtractedField, ParserResult, Provenance
from .normalization import normalize_field
from .rules import detect_inspection_mode
from .validation import validate_fields


def apply_field_overrides(result: ParserResult, overrides: dict[str, str], reviewer: str = "staff_review") -> ParserResult:
    fields = dict(result.fields)
    source_file_id = result.source_file_ids[0] if result.source_file_ids else "manual"
    for field_name, raw_value in overrides.items():
        if field_name not in fields:
            continue
        previous = fields[field_name]
        force_postcode = field_name == "inspection_address"
        normalized = normalize_field(field_name, raw_value, force_postcode=force_postcode)
        fields[field_name] = ExtractedField(
            name=field_name,
            raw_value=raw_value,
            normalized_value=normalized,
            confidence=1.0,
            provenance=[
                Provenance(
                    source_file_id=source_file_id,
                    extraction_method=reviewer,
                    section="manual_correction",
                    snippet=raw_value[:240],
                )
            ],
            warnings=previous.warnings,
            review_state="reviewed",
        )
    inspection_mode, inspection_source, address_lines, postcode, inspection_confidence, evidence = detect_inspection_mode(
        fields
    )
    validation = validate_fields(
        fields,
        detected_provider=result.detected_provider,
        parser_warnings=result.warnings,
        has_images=bool(result.images),
        export_required=result.document_classification not in {"image", "image_pack"},
    )
    return replace(
        result,
        fields=fields,
        validation=validation,
        inspection_mode=inspection_mode,
        inspection_site_source=inspection_source,
        inspection_address_lines=address_lines,
        inspection_postcode=postcode,
        inspection_location_confidence=inspection_confidence,
        inspection_location_evidence=evidence,
    )
