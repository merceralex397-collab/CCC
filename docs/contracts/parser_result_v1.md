# Parser Result Contract v1

Implementation: `src/ccc_parser/models.py` now emits this contract shape through `ParserResult.to_dict()`. Field overrides preserve the same envelope through `src/ccc_parser/review.py`.

Parser output is canonical before it becomes EVA-specific.

## Result Envelope

| Field | Required | Notes |
| --- | --- | --- |
| `parser_result_id` | yes | Stable id for this parser result. |
| `work_item_id` | no | Required when parsed inside Operational Core. |
| `source_file_ids` | yes | One or more source files and hashes. |
| `parser_version` | yes | Parser core version. |
| `provider_config_version` | yes | Provider config used during extraction. |
| `detected_provider` | no | Provider preset or unknown. |
| `provider_confidence` | yes | Numeric or categorical confidence. |
| `document_classification` | yes | Instruction, email, image pack, report, unknown, batch. |
| `fields` | yes | Field objects with value, provenance, confidence, warnings. |
| `images` | yes | Extracted/referenced image metadata and ordering hints. |
| `validation` | yes | Required/optional warnings and export gates. |
| `audit_metadata` | yes | Tool versions, methods, timestamps. |

## Field Object

Each extracted field should include:

- canonical field name;
- raw value;
- normalized value;
- confidence;
- source file id;
- page number or email section where available;
- bounding box or text span where available;
- extraction method;
- warnings;
- manual correction link when reviewed.

## Core Fields

- work provider/principal;
- VRM;
- vehicle make/model;
- claimant/client name;
- client claim/reference number;
- incident date;
- instruction date;
- inspection date;
- inspection address or image-based assessment marker;
- accident circumstances;
- VAT status;
- mileage and mileage unit;
- evidence image list.

## Validation Requirements

- Dates intended for EVA export must normalize to `DD/MM/YYYY`.
- Inspection address handling must support up to six lines without silently dropping lines. Blank canonical values remain blank until the EVA export adapter renders the legacy six blank lines.
- Mileage must distinguish missing, estimated, extracted, and manually corrected values.
- VAT status and mileage unit must be explicit where required.
- Missing work provider/principal is a critical export blocker.
- Evidence images and image packs are not instruction export candidates and must not produce EVA JSON, even for review-copy export.

## Implemented Canonical Inspection Fields

The parser result also carries the inspection-site fields required by the parser MVP plan:

- `inspection_mode`: `physical`, `image_based`, `unknown`, or `review_required`.
- `inspection_site_source`: instruction text, provider manual rule, staff review, or unknown source marker.
- `inspection_address_lines`: six-line-compatible structured lines before EVA serialization.
- `inspection_postcode`: detected postcode where available.
- `inspection_location_confidence` and `inspection_location_evidence`.

## Rule

EVA field shape is an export adapter. Do not let EVA-specific JSON become the only internal representation.

## Deterministic Fallbacks

Provider presets remain the primary extraction source. When a preset has a blank config, or a fixed-position rule extracts visible document-control noise instead of a field value, the parser may apply deterministic labelled-value fallbacks for VRM, reference, claimant name, vehicle model, dates, inspection mode/address, accident circumstances, mileage, mileage unit, and provider code. These fallback fields still carry method, confidence, and provenance metadata and must remain reviewable before export.

## Engineer Report Merge Metadata

When a folder contains one instruction and one engineer-report source, parser core may merge non-provider engineer-report fields into the canonical result while preserving the instruction work provider. The result audit metadata records `engineer_report_provider`, `engineer_report_source_file_id`, and `engineer_report_field_overrides`; any replacement of a non-blank instruction value must create an `engineer_report_field_override` warning.
