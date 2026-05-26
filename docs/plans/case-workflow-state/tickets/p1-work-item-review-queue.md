# P1-005 Work Item And Review Queue

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/contracts/work_item_contract_v1.md`, `docs/contracts/review_audit_event_contract_v1.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_04_human_review_queue_and_exception_sla.md`, `docs/plans/operational-core/archived_plans/implemented/2026-05-23-implemented-figmaplan.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: state-store decision, P1-001 (Parser Core MVP).
- Expected outputs: work item lifecycle, missing-info states, review/correction workflow, audit event persistence, and optional metadata capture for source channel, Box/local folder references, and current payment/portal evidence.
- Acceptance criteria: staff can move cases through draft, missing evidence/instruction, parsed, in review, ready for export, exported, packaged, blocked, archived; work items can record `source_channel`, `source_category`, `source_labels`, `portal_submission_id`, `payment_status`, `payment_chaser_sent`, `box_folder_url`, `box_folder_stage`, `local_network_folder_url`, and `closed_file_reason` without making those fields parser-required or authorizing portal/payment/WhatsApp automation in P1.
- Verification required: lifecycle tests, correction/audit tests, blocked-state tests, and schema checks confirming the full optional metadata field set is accepted but not required.
- Archive target: `docs/plans/case-workflow-state/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p1-operational-core-mvp.md` § P1-005.
- Superseded-by: none.

## Context

The Excel job sheet currently manages case state via VBA helpers `CreateNewRow`, `FolderCreator`, and `RowMover` (see `handover.docx` normalized companion). This ticket must replicate those state transitions in the new system without inheriting their manual, spreadsheet-bound limitations.
