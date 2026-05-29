# Case Workflow State Plan (Casework)

Date: 2026-05-29
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-29
Group: casework
Wave: G2-G3
Layer: operational
Source links: `docs/plans/case-workflow-state/context.md`, `docs/superpowers/specs/2026-05-29-casework-design.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/review_audit_event_contract_v1.md`, `docs/architecture/mvp_interlock.md`
Roadmap milestone: G2-G3 casework (operational spine)
Dependencies: parser-extraction, intake-storage-integrations (bridge), provider-principal-config, governance-security, operations-quality, user-experience-interfaces
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/case-workflow-state/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/case-workflow-state/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

This is the **casework** broad workspace (group `casework`, waves G2-G3 — the operational spine). Sub-areas: `state` (work-item store/lifecycle/review/missing-info/dedup/search), `ui` (the staff surfaces), `automation` (deterministic triggers). It absorbs `case-workflow-state`, `user-experience-interfaces`, and `automation-centre`. See `docs/plans/_groups.md`.

## This Iteration — Full State Model + SQLite + WinUI App + Minimal Automation

Approved design: `docs/superpowers/specs/2026-05-29-casework-design.md`. Workspace ADR: `decisions/0001-casework-ui-winui3-and-sqlite-store.md`. Decisions (2026-05-29):

| Area | Decision |
| --- | --- |
| State model | Full: lifecycle + missing-info machine + duplicate/merge/link/split + historical search. |
| Store | Local **SQLite** first-party store; append-only audit table. Access boundary: option-paper `option-papers/work-item-store-access-boundary.md`. |
| UI | Separate **WinUI 3 Windows app** (Windows App SDK, C#/XAML), built with the **winui-dev agent** + WinUI skills. |
| Automation | Minimal deterministic, audited auto-advances (e.g. → `ready_to_parse` when instruction + evidence present). |

Bridge dependency: this iteration delivers the work-item create API + entry states the bridge intake adapter needs. Foundation ticket: `tickets/p1-work-item-store-and-service.md`.

## Cross-Language Note

The parser + bridge intake are Python; the casework UI is .NET/WinUI 3. Both use the work-item store. The store schema/contract is the shared truth; the access boundary (shared SQLite vs a Python service the WinUI app calls) is decided in the option-paper.

## Sequential Plan

### S1 (now)
- [ ] SQLite work-item store + service interface + append-only audit (settle the access boundary).
- [ ] Full state machine + validation gates + missing-info machine.

### S2
- [ ] Duplicate/merge/link/split + historical search.
- [ ] Minimal automation rules (audited auto-advances).

### S2-S3 (parallel once the service interface is stable)
- [ ] WinUI 3 casework app screens (dashboard / holding pen / review / case detail / search) via the winui-dev agent.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `parser` | Feeds the review queue; shares the canonical parser-result contract; Python side of the store. |
| `bridge` | Outlook intake creates work items with source metadata; needs the create API + entry states. |
| `provider-principal-config` | Principal/routing on the work item. |
| `governance-security` | Role model for review/override, append-only audit, retention/privacy for historical search. |
| `operations-quality` | Queue-health metrics, rollout, and the Python+WinUI deployment/packaging story. |

## Non-Overlap Rules

Does not own: parser extraction internals (`parser`); live Outlook/Box/EVA adapters (`bridge`); MCP exposure (`mcp-tooling`). Personal injury and KADOE remain out of scope.

## Promotion Gates

- `tickets/` for implementation-ready work (the store/service foundation).
- `option-papers/` for the store access boundary (and any vendor/retention decision for historical search).
- Append-only audit + human-review gate are mandatory; reviewed data gates all downstream export/packaging.
- WinUI build/test/package via the winui-dev agent and `winui-packaging`; coordinate `operations-quality` for deployment.
