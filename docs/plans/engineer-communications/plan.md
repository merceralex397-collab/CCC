# Engineer Communications Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/11_WORK_PACKAGE_ENGINEER_PACK_AND_REPORTING.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_06_engineer_pack_generator_and_template_manager.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_09_communications_chaser_and_status_drafting.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/17_engineer_pack_generator.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, agent-skills, user-experience-interfaces, governance-security
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/engineer-communications/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/engineer-communications/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/engineer-communications/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/11_WORK_PACKAGE_ENGINEER_PACK_AND_REPORTING.md` | Engineer pack and reporting work package. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_06_engineer_pack_generator_and_template_manager.md` | Engineer pack generator and template manager plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_09_communications_chaser_and_status_drafting.md` | Communications chaser and status drafting plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/17_engineer_pack_generator.md` | Engineer pack generator skill/tool plan. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] engineer pack generation workflow | `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/11_WORK_PACKAGE_ENGINEER_PACK_AND_REPORTING.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_06_engineer_pack_generator_and_template_manager.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_09_communications_chaser_and_status_drafting.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/17_engineer_pack_generator.md` | `case-workflow-state`, `agent-skills`, `user-experience-interfaces`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] template manager and report-support workflow | `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/11_WORK_PACKAGE_ENGINEER_PACK_AND_REPORTING.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_06_engineer_pack_generator_and_template_manager.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_09_communications_chaser_and_status_drafting.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/17_engineer_pack_generator.md` | `case-workflow-state`, `agent-skills`, `user-experience-interfaces`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] missing-info and status communication workflow | `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/11_WORK_PACKAGE_ENGINEER_PACK_AND_REPORTING.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_06_engineer_pack_generator_and_template_manager.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_09_communications_chaser_and_status_drafting.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/17_engineer_pack_generator.md` | `case-workflow-state`, `agent-skills`, `user-experience-interfaces`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] communications approval, audit, and handoff patterns | `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/11_WORK_PACKAGE_ENGINEER_PACK_AND_REPORTING.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_06_engineer_pack_generator_and_template_manager.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_09_communications_chaser_and_status_drafting.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/17_engineer_pack_generator.md` | `case-workflow-state`, `agent-skills`, `user-experience-interfaces`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S4

- [ ] Generate engineer packs and communication drafts only from reviewed work items and approved source evidence.

### S5

- [ ] Add engineer support/report drafting assistants with explicit engineer sign-off boundaries.

### S6

- [ ] Connect mature report/template support to unified-platform rollout and decommissioning gates.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `case-workflow-state` | Work-item state, review status, blockers, audit events, and approvals are the operational source of truth. |
| `agent-skills` | Portable skills must stay separate from runtime orchestration and cite approved skill prompts/evaluation examples. |
| `user-experience-interfaces` | Human-facing surfaces must use shared domain contracts and keep UI thin over parser/work-item services. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |

## Non-Overlap Rules

The workspace explicitly does not own:

- portable natural-language skill specs
- expert judgement or final report conclusions
- external channel automation without separate approval

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
