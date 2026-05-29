# Casework: Work-Item State, Review, WinUI App, and Automation — Design

Date: 2026-05-29
Status: approved design (brainstorming output)
Owner: unassigned
Workspace: `docs/plans/case-workflow-state/` (group: casework, G2–G3)
Source links: `docs/plans/case-workflow-state/context.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/review_audit_event_contract_v1.md`, `docs/architecture/mvp_interlock.md`, `src/ccc_parser/ui/app.py`, `docs/superpowers/specs/2026-05-29-bridge-design.md`

## Context

Casework is the operational spine between parser output and export/packaging. The work-item lifecycle and the review/audit event stream are already fixed by `work_item_contract_v1.md` and `review_audit_event_contract_v1.md` (see `context.md`). This iteration builds the store + state machine + review + UI + minimal automation. The bridge Outlook intake adapter hard-depends on the work-item create API + entry states this iteration delivers.

## Decisions captured (user, 2026-05-29)

- **Full state model now:** lifecycle + missing-info state machine + duplicate/merge/link/split + historical search (not just the minimal bridge target).
- **Store:** local **SQLite** first-party store.
- **UI:** a **separate WinUI 3 Windows app** (Windows App SDK, C#/XAML), built with the **winui-dev agent** — distinct from the parser's Python Tk tool.
- **Automation:** include **minimal deterministic automation** (e.g. auto-advance to `ready_to_parse` when both instruction and evidence are present), audited.

## Goals / Non-goals

**Goals:** a SQLite work-item store implementing the contract; the full state machine + missing-info + dedup/merge/link/split + historical search; an append-only audit stream; a WinUI 3 staff app (dashboard/holding-pen/review/case-detail/search) thin over the work-item service; minimal audited automation; the bridge's minimal work-item target.

**Non-goals (this iteration):** parser extraction internals (`parser`); live Outlook/Box/EVA adapters (`bridge`); MCP exposure (`mcp-tooling`); the broad automation engine beyond the minimal auto-advance rules. Personal injury and KADOE remain out of scope.

## Design

### Work-item store (SQLite)

- A first-party store implementing `work_item_contract_v1` (identity, lifecycle `status`, source metadata, relationships, validation gates) and an **append-only** audit table per `review_audit_event_contract_v1`. SQLite chosen for transactional status transitions, queryable queues, and concurrent staff edits on a single office machine (WAL mode).
- **Cross-language access is the key architecture question.** The parser and bridge intake are **Python**; the casework UI is **.NET/WinUI 3**. Both need the work-item store. Options (see `option-papers/work-item-store-access-boundary.md`): (a) both access the shared SQLite file against a shared, versioned schema; (b) a Python work-item **service/API** owns the DB and the WinUI app calls it; (c) a thin local service either side. The schema/contract is the shared truth regardless.

### State machine

Implement the full contract lifecycle (`draft → needs_evidence/needs_instruction → ready_to_parse → parsed → in_review → ready_for_export → exported → packaged`, `blocked`, `archived`) with the validation gates, plus: the **missing-info** checklist/state machine (what blocks `needs_evidence`/`needs_instruction`/`blocked`), **duplicate/merge/link/split** (case association), and **historical search** over case history. Dedup/search carry retention/privacy considerations (coordinate `governance-security`).

### Casework WinUI 3 app

Screens (thin over the work-item service): dashboard, holding pen, review queue, case detail (source preview + extracted fields + warnings, reusing the parser's canonical result), missing-info panel, activity/audit log, and historical search. Built with the **winui-dev agent** and the WinUI skills (`winui-design` for XAML/layout, `winui-dev-workflow` for build/run, `winui-ui-testing` for tests, `winui-packaging` for MSIX). Keep business rules in the work-item service, not the UI.

### Minimal automation

Deterministic, audited auto-advances only: e.g. set `needs_evidence`/`needs_instruction` from what's present, and advance to `ready_to_parse` when both an instruction and evidence exist. Every auto-transition writes a `status_changed` audit event. No autonomous external actions.

## Sequencing

1. SQLite work-item store + service interface + audit table (the bridge/parser dependency) — settle the access boundary first.
2. Full state machine + validation gates + missing-info machine.
3. Duplicate/merge/link/split + historical search.
4. Minimal automation rules.
5. WinUI 3 app screens (can start once the service interface is stable, in parallel with 2–4) — via the winui-dev agent.

## Testing / Acceptance

- Store: lifecycle transitions enforce the contract's validation gates; audit is append-only; SQLite concurrency (WAL) holds under concurrent edits.
- Bridge target: a work item can be created with source metadata and the `work_item_created`/`file_added`/`integration_attempted` events.
- Dedup/merge/link/split + search behave per spec on a fixture case set.
- Automation: auto-advances are deterministic and audited.
- WinUI app: `winui-ui-testing` pass over the queue/review/search screens; thin-over-service (no business rules in UI).
- `python tools/verify_scaffold.py` green.

## Risks & Open Questions

- **Store access boundary** (shared SQLite vs Python service the WinUI app calls) — the central architecture fork; schema-drift risk across Python/.NET.
- **Deployment**: shipping a Python parser (Tk) + a .NET WinUI app together on staff machines — packaging/update story (coordinate `operations-quality`; `winui-packaging` for the .NET side).
- Historical search retention/privacy + how much case history is searchable (governance).
- Full-model scope is large; sequence carefully so the bridge's minimal target lands early.
