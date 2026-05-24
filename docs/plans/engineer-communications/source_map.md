# Engineer Communications Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/11_WORK_PACKAGE_ENGINEER_PACK_AND_REPORTING.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_06_engineer_pack_generator_and_template_manager.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_09_communications_chaser_and_status_drafting.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/17_engineer_pack_generator.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, agent-skills, user-experience-interfaces, governance-security
Expected outputs: source-to-plan traceability for `docs/plans/engineer-communications/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/engineer-communications/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/11_WORK_PACKAGE_ENGINEER_PACK_AND_REPORTING.md` | Engineer pack and reporting work package. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_06_engineer_pack_generator_and_template_manager.md` | Engineer pack generator and template manager plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_09_communications_chaser_and_status_drafting.md` | Communications chaser and status drafting plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/17_engineer_pack_generator.md` | Engineer pack generator skill/tool plan. |

## Ownership Boundary

Primary ownership:

- engineer pack generation workflow
- template manager and report-support workflow
- missing-info and status communication workflow
- communications approval, audit, and handoff patterns

Explicit exclusions:

- portable natural-language skill specs
- expert judgement or final report conclusions
- external channel automation without separate approval

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
