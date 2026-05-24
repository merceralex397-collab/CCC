# Case Workflow State Workspace

## Purpose

This workspace owns all planning for work item state management, human review queues, audit event streams, missing-information state, duplicate detection, historical case search, and case lifecycle rules.

## Scope Rules

- Personal injury and KADOE workflows are out of scope.
- Autonomous external actions (email send, WhatsApp, EVA submission) must not be triggered from the work item lifecycle without separate governance approval.
- Work item schema supports optional portal/payment/Box metadata capture from P1, but automation of those channels is long-range planned.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/normalized/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md` | Whiteboard case flow, review queue, and state diagrams. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_01_work_item_state_store_and_job_sheet_replacement.md` | Work item state store design and job sheet replacement requirements. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_04_human_review_queue_and_exception_sla.md` | Human review queue, exception SLA, and missing-info handling. |
| `docs/reference/normalized/collisionrelateddocs__collision_releated__handover.docx.md` | Excel job sheet VBA helpers: `CreateNewRow`, `FolderCreator`, `RowMover`; states these must replace in the new system. |
| `docs/contracts/work_item_contract_v1.md` | Canonical work item contract. |
| `docs/contracts/review_audit_event_contract_v1.md` | Canonical review and audit event contract. |

## Workspace Layout

- `README.md` — this file
- `source_map.md` — reference-to-plan traceability
- `roadmap.md` — sequencing
- `tickets/` — active tickets
- `option-papers/` — unresolved decisions (state-store technology choice)
- `archived_plans/` — implemented and superseded plans
