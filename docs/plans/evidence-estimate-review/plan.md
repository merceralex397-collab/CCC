# Evidence Estimate Review Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, vehicle-valuation-data, engineer-communications, governance-security
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/evidence-estimate-review/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/evidence-estimate-review/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/evidence-estimate-review/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md` | Image evidence quality and schedule checker plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md` | Visible VRM and image case matcher plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md` | Audatex estimate parser and QA assistant plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md` | Estimate and ABP review pack plan. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md` | Audatex and ABP industry context and safe positioning. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] evidence matching and duplicate/reused evidence flags | `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md` | `case-workflow-state`, `vehicle-valuation-data`, `engineer-communications`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] image quality, visible VRM, and image ordering assistance | `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md` | `case-workflow-state`, `vehicle-valuation-data`, `engineer-communications`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] Audatex/repair estimate parsing and estimate QA flags | `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md` | `case-workflow-state`, `vehicle-valuation-data`, `engineer-communications`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] ABP charge review pack and ANDIE-style long-range damage workbench | `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md` | `case-workflow-state`, `vehicle-valuation-data`, `engineer-communications`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S2-S3

- [ ] Use case-state and review queues to surface evidence matching and image-order issues.

### S4

- [ ] Promote image intelligence, estimate parsing, ABP review, and evidence duplicate flags as review aids.

### S6

- [ ] Plan advanced damage workbench only after evidence, governance, and engineer-review controls are mature.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `case-workflow-state` | Work-item state, review status, blockers, audit events, and approvals are the operational source of truth. |
| `vehicle-valuation-data` | Vehicle facts and valuation evidence need licensing, confidence, provenance, and human review boundaries. |
| `engineer-communications` | Coordinate source ownership, sequencing, acceptance criteria, and verification before ticket promotion. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |

## Non-Overlap Rules

The workspace explicitly does not own:

- vehicle valuation source selection
- engineer final technical judgement
- Audatex commercial partnership discovery

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
