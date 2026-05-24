# Unified Platform Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_new_system.md`, `docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md`, `docs/architecture/future_system_convergence.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: operational-core, case-workflow-state, automation-centre, user-experience-interfaces, governance-security
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/unified-platform/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/unified-platform/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Mature end-to-end CCC platform planning and convergence roadmap.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- full case-management target platform
- system-wide convergence roadmap
- migration and legacy decommissioning strategy
- cross-workspace platform dependency map

## Does Not Own

- domain implementation tickets owned by specialist workspaces
- first parser-runtime implementation details
- vendor activation decisions without governance-security sign-off

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_new_system.md` | Near-term integrated case-intake system scope. |
| `docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md` | Mature bespoke system direction. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md` | Detailed mature single-platform plan. |
| `docs/architecture/future_system_convergence.md` | Canonical convergence spine and guardrails for later modules. |

## Cross-Workspace Dependencies

- operational-core
- case-workflow-state
- automation-centre
- user-experience-interfaces
- governance-security

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
