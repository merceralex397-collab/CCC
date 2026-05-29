# Ticket: Work-Item SQLite Store + Service + Audit (Casework Foundation)

Status: planned (foundation; unblocks bridge intake)
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Source links: `docs/superpowers/specs/2026-05-29-casework-design.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/review_audit_event_contract_v1.md`, `docs/plans/case-workflow-state/decisions/0001-casework-ui-winui3-and-sqlite-store.md`, `docs/plans/case-workflow-state/option-papers/work-item-store-access-boundary.md`
Roadmap milestone: G2-G3 casework
Dependencies: parser-extraction (canonical result), intake-storage-integrations (bridge intake is the first consumer), governance-security (role model + audit)
Expected outputs: a SQLite work-item store + service implementing the work-item and review/audit contracts, with the create API + entry states the bridge needs
Acceptance criteria: see deliverables; lifecycle gates enforced; audit append-only
Verification required: `python tools/verify_scaffold.py`, store/service unit tests, lifecycle-gate tests
Archive target: `docs/plans/case-workflow-state/archived_plans/implemented/`
Supersedes: complements `tickets/p1-work-item-review-queue.md`
Superseded-by: none

## Scope

The work-item store + service foundation. No live integrations, no MCP exposure. Personal injury and KADOE remain out of scope.

## Deliverables

1. **SQLite store** implementing `work_item_contract_v1` (identity, lifecycle `status`, source metadata, relationships) + an **append-only audit table** per `review_audit_event_contract_v1`; WAL mode.
2. **Work-item service/API**: create/read/update/transition, query the review queue, record audit events. Resolve the access boundary per the option-paper before building (shared SQLite vs Python service the WinUI app calls).
3. **Lifecycle gates**: enforce the contract's validation gates on transitions (e.g. no `ready_for_export` without reviewed principal/dates/inspection-or-image-marker/VRM/critical-warnings resolved).
4. **Bridge target**: `create_work_item(...)` accepting source metadata (`source_channel`, `source_labels`, etc.) and emitting `work_item_created` / `file_added` / `integration_attempted` events.
5. **Missing-info state machine**: derive `needs_evidence` / `needs_instruction` / `blocked` from what's present.

## Acceptance Criteria

- Transitions enforce the contract gates; invalid transitions are rejected with a reason.
- Audit is append-only; critical-warning overrides require reviewer role + reason.
- The bridge can create a work item with source metadata and the required audit events.
- Concurrent edits are safe (SQLite WAL).

## Follow-on (sequenced, separate tickets)

Duplicate/merge/link/split; historical search; minimal automation rules; the WinUI 3 casework app (via the winui-dev agent).
