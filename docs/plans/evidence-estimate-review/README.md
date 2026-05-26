# Evidence Estimate Review Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, vehicle-valuation-data, engineer-communications, governance-security
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/evidence-estimate-review/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/evidence-estimate-review/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Evidence matching, image review, estimate parsing, ABP review, and damage workbench planning.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- evidence matching and duplicate/reused evidence flags
- image quality, visible VRM, and image ordering assistance
- Audatex/repair estimate parsing and estimate QA flags
- ABP charge review pack and ANDIE-style long-range damage workbench

## Does Not Own

- vehicle valuation source selection
- engineer final technical judgement
- Audatex commercial partnership discovery

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md` | Image evidence quality and schedule checker plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md` | Visible VRM and image case matcher plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md` | Audatex estimate parser and QA assistant plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md` | Estimate and ABP review pack plan. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md` | Audatex and ABP industry context and safe positioning. |

## Cross-Workspace Dependencies

- case-workflow-state
- vehicle-valuation-data
- engineer-communications
- governance-security

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
