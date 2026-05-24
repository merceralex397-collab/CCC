# Case Workflow State Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/contracts/work_item_contract_v1.md`, `docs/contracts/review_audit_event_contract_v1.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_01_work_item_state_store_and_job_sheet_replacement.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: parser-extraction, provider-principal-config, governance-security, user-experience-interfaces
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/case-workflow-state/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/case-workflow-state/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Canonical work-item state, review queue, audit stream, missing-info state, and historical search planning.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- work item lifecycle and state transitions
- holding pen, review queue, and approval states
- missing-information checklist and state machine
- duplicate, merge, link, split, and historical search workflows

## Does Not Own

- parser extraction internals
- UI visual design
- live Outlook, Box, or EVA adapter implementation

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/contracts/work_item_contract_v1.md` | Canonical work item contract. |
| `docs/contracts/review_audit_event_contract_v1.md` | Review and audit event contract. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_01_work_item_state_store_and_job_sheet_replacement.md` | Work item state store and job-sheet replacement plan. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md` | Dashboard, review queue, evidence matching, and safeguards. |
| `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md` | Whiteboard-derived workflow and closure/payment metadata evidence. |

## Cross-Workspace Dependencies

- parser-extraction
- provider-principal-config
- governance-security
- user-experience-interfaces

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
