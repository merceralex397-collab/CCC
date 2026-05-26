# Evidence Estimate Review Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, vehicle-valuation-data, engineer-communications, governance-security
Expected outputs: source-to-plan traceability for `docs/plans/evidence-estimate-review/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/evidence-estimate-review/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md` | Image evidence quality and schedule checker plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md` | Visible VRM and image case matcher plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md` | Audatex estimate parser and QA assistant plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md` | Estimate and ABP review pack plan. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md` | Audatex and ABP industry context and safe positioning. |

## Ownership Boundary

Primary ownership:

- evidence matching and duplicate/reused evidence flags
- image quality, visible VRM, and image ordering assistance
- Audatex/repair estimate parsing and estimate QA flags
- ABP charge review pack and ANDIE-style long-range damage workbench

Explicit exclusions:

- vehicle valuation source selection
- engineer final technical judgement
- Audatex commercial partnership discovery

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
