# Unified Platform Plan

Date: 2026-05-29
Status: active workspace plan (design-only; build deferred to G6)
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-29
Group: unified-platform
Wave: G6 (spine endpoint — later)
Layer: platform
Source links: `docs/plans/unified-platform/context.md`, `docs/superpowers/specs/2026-05-29-unified-platform-design.md`, `docs/architecture/future_system_convergence.md`, `docs/plans/_groups.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md`
Roadmap milestone: G6 convergence
Dependencies: all specialist workspaces, operations-quality, foundation
Expected outputs: cross-workspace dependency map, decommissioning gates, and a deferred convergence plan
Acceptance criteria: convergence dependencies + decommissioning gates documented; build deferred until parity/rollback/adoption evidence exists
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/unified-platform/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

This is the **unified-platform** broad workspace — the G6 spine endpoint, explicitly built later/from-scratch. It coordinates convergence; it does not reach into specialist implementation. See `docs/plans/_groups.md`.

## This Iteration — Convergence Map + Decommissioning Gates (design-only)

Approved design: `docs/superpowers/specs/2026-05-29-unified-platform-design.md`. Decision (2026-05-29): capture the cross-workspace dependency map + decommissioning gates; build deferred; platform stack/UI not decided now.

- **Dependency map:** the platform converges parser → bridge → casework → intelligence/ai-platform → business, over the shared contracts + casework hub + tool gateway + skill catalogue + role model, with foundation continuous. (Diagram in the spec.)
- **Decommissioning gates:** retire `cedocumentmapper` after parser parity + adoption + rollback; retire the CE Job Sheet spreadsheet after casework parity + audit + rollback + support ownership; controlled operations-quality milestones only.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/architecture/future_system_convergence.md` | Canonical convergence spine and guardrails. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md` | Detailed mature single-platform plan. |
| `docs/superpowers/specs/2026-05-29-unified-platform-design.md` | Convergence map + decommissioning gates design. |

## Dependency Cross-Check

Depends on **all** specialist workspaces (it converges them), `operations-quality` (parity/rollback/decommissioning), and `foundation` (role model, governance, contracts). The `casework` work-item store + WinUI hub and the shared contracts are the convergence seeds.

## Non-Overlap Rules

Does not own: domain implementation tickets owned by specialist workspaces; first parser-runtime details; vendor activation without governance-security sign-off. Personal injury and KADOE remain out of scope.

## Promotion Gates

- Build is deferred to G6; nothing here promotes to implementation until earlier waves are delivered with parity/rollback/adoption evidence.
- Legacy decommissioning is a controlled release milestone with governance + operations sign-off.
