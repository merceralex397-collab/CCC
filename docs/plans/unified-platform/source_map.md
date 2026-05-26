# Unified Platform Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_new_system.md`, `docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md`, `docs/architecture/future_system_convergence.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: operational-core, case-workflow-state, automation-centre, user-experience-interfaces, governance-security
Expected outputs: source-to-plan traceability for `docs/plans/unified-platform/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/unified-platform/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_new_system.md` | Near-term integrated case-intake system scope. |
| `docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md` | Mature bespoke system direction. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md` | Detailed mature single-platform plan. |
| `docs/architecture/future_system_convergence.md` | Canonical convergence spine and guardrails for later modules. |

## Ownership Boundary

Primary ownership:

- full case-management target platform
- system-wide convergence roadmap
- migration and legacy decommissioning strategy
- cross-workspace platform dependency map

Explicit exclusions:

- domain implementation tickets owned by specialist workspaces
- first parser-runtime implementation details
- vendor activation decisions without governance-security sign-off

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
