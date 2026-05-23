# Parser Result Contract v1

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
- Inspection address handling must support up to six lines without silently dropping lines.
- Mileage must distinguish missing, estimated, extracted, and manually corrected values.
- VAT status and mileage unit must be explicit where required.
- Missing work provider/principal is a critical export blocker.

## Rule

EVA field shape is an export adapter. Do not let EVA-specific JSON become the only internal representation.
