# Casework Workspace — Open Questions

Date: 2026-05-29
Status: active open-questions log
Owner: unassigned
Group: casework (G2-G3)
Source links: `docs/superpowers/specs/2026-05-29-casework-design.md`, `docs/plans/case-workflow-state/plan.md`, `docs/plans/case-workflow-state/decisions/0001-casework-ui-winui3-and-sqlite-store.md`

## Resolved (this interview, 2026-05-29)

- **Build scope?** — Full state model now (lifecycle + missing-info + duplicate/merge/link/split + historical search).
- **Store?** — Local SQLite, first-party.
- **UI?** — Separate WinUI 3 Windows app, built with the winui-dev agent.
- **Automation?** — Include minimal deterministic, audited auto-advances.

## Open

1. **Store access boundary** (the central fork): both Python and .NET access the shared SQLite file against a versioned schema, or a Python work-item service owns the DB and the WinUI app calls it? See `option-papers/work-item-store-access-boundary.md`.
2. **Schema-drift control** across Python and .NET if they share the DB directly (migrations, versioning, a single source-of-truth schema definition).
3. **Deployment/packaging** of a Python parser (Tk) + a .NET WinUI app together on staff Windows machines (coordinate `operations-quality`; `winui-packaging`).
4. **Historical search** retention/privacy: how much case history is searchable, retention limits, and access control (governance-security).
5. **Sequencing**: keep the bridge's minimal work-item target (create API + entry states) landing early, before the larger dedup/merge/search scope.
6. **Role model**: reviewer/provider-admin roles the audit rules require (overrides need reviewer role + reason) — depends on the CE role model.
