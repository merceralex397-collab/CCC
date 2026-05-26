# Unified Platform Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_new_system.md`, `docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md`, `docs/architecture/future_system_convergence.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: operational-core, case-workflow-state, automation-centre, user-experience-interfaces, governance-security
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/unified-platform/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/unified-platform/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/unified-platform/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_new_system.md` | Near-term integrated case-intake system scope. |
| `docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md` | Mature bespoke system direction. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md` | Detailed mature single-platform plan. |
| `docs/architecture/future_system_convergence.md` | Canonical convergence spine and guardrails for later modules. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] full case-management target platform | `docs/reference/originalplanning/originalplans_output/phase_new_system.md`<br>`docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md`<br>`docs/architecture/future_system_convergence.md` | `operational-core`, `case-workflow-state`, `automation-centre`, `user-experience-interfaces`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] system-wide convergence roadmap | `docs/reference/originalplanning/originalplans_output/phase_new_system.md`<br>`docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md`<br>`docs/architecture/future_system_convergence.md` | `operational-core`, `case-workflow-state`, `automation-centre`, `user-experience-interfaces`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] migration and legacy decommissioning strategy | `docs/reference/originalplanning/originalplans_output/phase_new_system.md`<br>`docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md`<br>`docs/architecture/future_system_convergence.md` | `operational-core`, `case-workflow-state`, `automation-centre`, `user-experience-interfaces`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] cross-workspace platform dependency map | `docs/reference/originalplanning/originalplans_output/phase_new_system.md`<br>`docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md`<br>`docs/architecture/future_system_convergence.md` | `operational-core`, `case-workflow-state`, `automation-centre`, `user-experience-interfaces`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S0-S1

- [ ] Track how foundational parser, work item, provider, UI, and export work align to the shared platform spine.

### S2-S3

- [ ] Coordinate storage, intake, EVA/Sentry, and automation-centre decisions so they use common contracts.

### S4-S6

- [ ] Sequence mature platform capabilities, adoption, and legacy decommissioning only after parity and rollback evidence.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `operational-core` | Operational Core coordinates the first executable slice and points specialist work to its owning workspace. |
| `case-workflow-state` | Work-item state, review status, blockers, audit events, and approvals are the operational source of truth. |
| `automation-centre` | Deterministic automation owns triggers, retries, idempotency, queues, and exception routing used by domain workflows. |
| `user-experience-interfaces` | Human-facing surfaces must use shared domain contracts and keep UI thin over parser/work-item services. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |

## Non-Overlap Rules

The workspace explicitly does not own:

- domain implementation tickets owned by specialist workspaces
- first parser-runtime implementation details
- vendor activation decisions without governance-security sign-off

If a proposed ticket touches one of those exclusions, link to the owning workspace and keep this workspace as a supporting dependency only.

## Source Ownership Rules

- Cite the source paths above in every promoted ticket, option paper, or roadmap change.
- Use `source_map.md` to explain how the evidence supports the workspace boundary.
- Keep generated and historical planning packs reference-only until a scoped ticket or option paper promotes them.
- Do not edit raw evidence under `docs/reference/raw/collisionrelateddocs/`; create derivatives only under documented derivative paths.

## Promotion Gates

- Use `tickets/` for implementation-ready work with acceptance criteria and verification.
- Use `option-papers/` before vendor, privacy, external access, autonomous send, payment automation, AI/RAG, cloud OCR/document intelligence, commercial data, or partner/API work.
- Link governance/security approval where privacy, vendor, retention, licensing, expert-boundary, API security, or autonomous-action risk exists.
- Link operations-quality approval where release, rollback, regression, monitoring, runbook, support, pilot, or decommissioning evidence is needed.
