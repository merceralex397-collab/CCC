# Option Paper: Work-Item Store Access Boundary (Python + .NET)

Status: open (must be decided before the store is built)
Owner: unassigned
Created: 2026-05-29
Group: casework / state (G2-G3)
Source links: `docs/superpowers/specs/2026-05-29-casework-design.md`, `docs/plans/case-workflow-state/decisions/0001-casework-ui-winui3-and-sqlite-store.md`, `docs/contracts/work_item_contract_v1.md`

## Context

The work-item store is SQLite. Two languages need it: the **parser + bridge intake (Python)** and the **casework UI (.NET/WinUI 3)**. How both reach the store is the central casework architecture decision; it affects schema ownership, concurrency, and deployment.

## Options

1. **Shared SQLite file, shared versioned schema.** Both Python and .NET open the same DB (WAL). Simplest runtime; no service to host. Risk: schema drift across two languages; concurrency/locking discipline; business-rule duplication unless one library owns transitions.
2. **Python work-item service owns the DB; WinUI calls it** (local HTTP/IPC). Single owner of schema + transition rules + audit; the WinUI app is a thin client. Cleaner integrity; adds a local service to run/deploy.
3. **Shared SQLite for reads, service for writes.** WinUI reads the DB directly for fast queue/search rendering; all writes/transitions go through the Python service so gates + audit are enforced in one place. Hybrid; more moving parts.

## Decision Criteria

Single source of truth for transition rules + audit; schema-drift risk; concurrency safety; deployment complexity on staff Windows machines (one Python tool + one .NET app already); latency of queue/search rendering; testability; alignment with the future unified platform.

## Recommendation Lean

Option 2 or 3 keeps the contract's validation gates + append-only audit enforced in one place (Python), with the WinUI app thin — at the cost of running a local service. Confirm against deployment constraints with `operations-quality`.

## Governance Gates

Audit integrity (append-only) and role-based override rules must hold regardless of option. Retention/privacy for historical search applies to whichever component queries history.
