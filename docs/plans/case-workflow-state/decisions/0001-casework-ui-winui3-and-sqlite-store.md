# ADR 0001 (casework): WinUI 3 Casework UI + Local SQLite Work-Item Store

Date: 2026-05-29
Status: accepted (workspace-local)
Scope: `docs/plans/case-workflow-state/` (casework)
Source links: `docs/superpowers/specs/2026-05-29-casework-design.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/review_audit_event_contract_v1.md`

## Context

Casework needs a persistent work-item store and a staff UI for the queue/review/case-detail/search. The parser already has a Python Tk UI but operates per-file, not over a work-item queue. The bridge intake (Python) and parser (Python) both write work items; staff need a richer operational surface.

## Decision

1. **Work-item store = local SQLite**, first-party, implementing `work_item_contract_v1` + an append-only audit table per `review_audit_event_contract_v1`. WAL mode for concurrent staff edits.
2. **Casework UI = a separate WinUI 3 Windows app** (Windows App SDK, C#/XAML), distinct from the parser's Python Tk tool, built and tested with the **winui-dev agent** and the WinUI skills (`winui-design`, `winui-dev-workflow`, `winui-ui-testing`, `winui-packaging`).

## Consequences

- **Cross-language stack:** Python (parser, bridge intake, work-item service) + .NET (casework UI) share the SQLite work-item store. The shared truth is the schema/contract; the access boundary (shared file vs a Python service the WinUI app calls) is resolved in `option-papers/work-item-store-access-boundary.md`.
- **Deployment:** staff machines run a Python tool + a .NET WinUI app; packaging/update is an `operations-quality` concern (`winui-packaging` for the MSIX side).
- The casework UI is **not** the parser Tk UI extended; the two stay separate tools over shared work-item services.
- Keeps business rules in the work-item service; the WinUI app stays thin.

## Alternatives Considered

- Extend the parser Tk UI (rejected: user chose a separate UI; Tk is weaker for a richer operational dashboard).
- Local web UI as the platform seed (not chosen now; revisit at the unified-platform G6 stage).
- JSON/file store (rejected: weaker for queue queries, concurrency, and audit integrity).
