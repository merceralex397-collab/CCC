# Work Item Contract v1

## Purpose

A work item represents one Collision Engineers instruction/case candidate as it moves from uploaded evidence to reviewed EVA export and Box-ready package.

## Identity

| Field | Required | Notes |
| --- | --- | --- |
| `work_item_id` | yes | CCC-generated stable id. |
| `case_po` | no until reviewed | Collision Engineers internal reference. Generated/confirmed by staff. |
| `claim_reference` | no until reviewed | Client/work provider reference. |
| `principal_code` | no until reviewed | Internal provider/principal code used by CE/EVA. |
| `vrm` | no until parsed/reviewed | Vehicle registration mark. |
| `created_at` | yes | ISO timestamp. |
| `created_by` | yes | Named CCC local account. |
| `status` | yes | See lifecycle. |

## Lifecycle States

| State | Meaning |
| --- | --- |
| `draft` | Created but not ready for extraction. |
| `needs_evidence` | Instruction exists but images or other required evidence are missing. |
| `needs_instruction` | Images/evidence exist but instruction cannot be matched. |
| `ready_to_parse` | Files are available for parser run. |
| `parsed` | Parser result exists but has not been reviewed. |
| `in_review` | Staff are correcting or resolving warnings. |
| `ready_for_export` | Required validation gates passed. |
| `exported` | EVA-ready JSON has been generated. |
| `packaged` | Evidence package manifest has been generated. |
| `blocked` | Cannot progress without external input or decision. |
| `archived` | Closed historical record. |

## Required Relationships

- `source_file_ids`: uploaded instructions, emails, attachments, images, companion reports, notes.
- `parser_run_ids`: parser attempts against this work item.
- `review_event_ids`: manual corrections, warnings resolved, approvals.
- `package_ids`: generated evidence packages.
- `export_ids`: EVA JSON exports.

## Validation Gates

- A work item cannot move to `ready_for_export` without reviewed `principal_code`, required dates, inspection address or image-based marker, VRM where available, and resolved critical parser warnings.
- A work item cannot move to `packaged` without a package manifest and image-order decision.
- A work item cannot be archived while required missing-info blockers are unresolved unless an archive reason is recorded.

## Sources

- `docs/reference/generated-packs/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_01_work_item_state_store_and_job_sheet_replacement.md`
- `docs/reference/generated-packs/ce_system_plans_enhanced/ce_system_plans_enhanced/05_WORK_PACKAGE_DATA_MODEL_AND_WORKFLOW.md`

