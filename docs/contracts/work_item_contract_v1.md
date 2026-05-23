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

## Optional Source And Tracking Metadata

These fields capture current operational context from Outlook, website portal, WhatsApp, Box, and local folder workflows. They are future-capable metadata and must not be treated as parser-required fields for MVP:

| Field | Required | Notes |
| --- | --- | --- |
| `source_channel` | no | Intake or status source such as `outlook`, `website_portal`, `whatsapp`, or later adapters. |
| `source_category` | no | Coarse operational grouping such as instruction, image-only intake, query, or portal request. |
| `source_labels` | no | Labels/categories observed in the source system, for example Outlook categories or query markers. |
| `portal_submission_id` | no | Website repair-estimate submission identifier where present. |
| `payment_status` | no | Current portal/payment evidence such as `pending`, `paid`, or `unknown`. |
| `payment_chaser_sent` | no | Tracks whether the current payment chase evidence has already been recorded. |
| `box_folder_url` | no | Box folder link for the request or package when available. |
| `box_folder_stage` | no | Observed storage stage such as live request folder, packaged, or closed-file backup. |
| `local_network_folder_url` | no | Spreadsheet-created local network path/link where operationally relevant. |
| `closed_file_reason` | no | Reason a file was closed without normal completion, for example missing information after chase limit. |

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
- Recording `source_channel`, payment status, Box links, or local folder links must not create an MVP requirement to automate portal, payment, or WhatsApp actions.

## Sources

- `docs/reference/generated-packs/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_01_work_item_state_store_and_job_sheet_replacement.md`
- `docs/reference/generated-packs/ce_system_plans_enhanced/ce_system_plans_enhanced/05_WORK_PACKAGE_DATA_MODEL_AND_WORKFLOW.md`
