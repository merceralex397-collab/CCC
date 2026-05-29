# Unified Platform Workspace — Context (Information Document)

Date: 2026-05-29
Status: active context document
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: unified-platform (G6, spine endpoint — later, layer: platform) — see `docs/plans/_groups.md`
Source links: `docs/architecture/future_system_convergence.md`, `docs/plans/_groups.md`, `docs/superpowers/specs/2026-05-29-casework-design.md`, `docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md`

This is the spine endpoint (G6). The user has explicitly said the unified platform **comes later in the dev cycle** and is built **from scratch** — so this workspace is convergence planning, not near-term build.

## What this workspace owns

The mature end-to-end CCC platform convergence: full case-management target platform; system-wide convergence roadmap; the **cross-workspace platform dependency map**; and the **migration + legacy decommissioning** strategy (retire `cedocumentmapper` + the CE Job Sheet spreadsheet).

It does **not** own: domain implementation (the specialist workspaces own their features); first parser-runtime details; vendor activation without governance sign-off.

## Why it is deliberately later

Everything the platform converges is being planned/built first: parser (G1), bridge (G2), casework (G2-G3, incl. the WinUI app + SQLite store), intelligence/ai-platform (G3-G4), business (G5), with mcp-tooling + agent-skills + foundation throughout. The platform is the convergence of these into one mature system — it cannot precede them. The canonical convergence spine + scope guardrails live in `docs/architecture/future_system_convergence.md`.

## Convergence seeds already visible

- The **casework WinUI 3 app** + work-item SQLite store is the operational hub the platform centres on (the casework UI-tech option-paper noted a local web UI as the eventual platform-UI direction).
- The contracts (parser result, work item, review/audit, EVA export, evidence package, storage adapter, provider/principal config) are the shared model the platform inherits.
- The tool gateway (`mcp-tooling`) + portable skills (`agent-skills`) + role model (`foundation`) are the cross-cutting substrate.

## Key theme — decommission only after parity

Retire legacy (the `cedocumentmapper` monolith, the spreadsheet) **only after** parity, audit, rollback, support ownership, and adoption evidence. Decommissioning is a controlled release milestone (operations-quality), not an MVP side effect.

## Dependencies

All specialist workspaces + `operations-quality` (parity/rollback/decommissioning gates) + `foundation` (role model, governance).

## Guardrails

Convergence coordinates sequencing + dependencies; it does not reach into specialist implementation. No legacy decommissioning without parity + rollback + adoption evidence. Personal injury and KADOE remain out of scope.

## Open design question for the interview

What to capture now, given it is explicitly later: the cross-workspace dependency map + the decommissioning gates as a design-only convergence plan (build deferred), or more?
