# Evidence Estimate Review Workspace

## Purpose

This workspace owns all planning for evidence quality checks, image quality review, estimate parsing, ABP (Agreed Body Parts) review, duplicate/reused evidence detection, image ordering, damage workbench, and preview-image recommendations.

## Scope Rules

- Image intelligence produces review flags only — it must not automatically decide cases.
- Personal injury and KADOE are out of scope.
- Visible VRM hints and image quality checks are reviewer aids, not automatic case decisions.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/07_image_review_evidence_quality_and_matching.md` | Image review, evidence quality, and matching design. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md` | Image evidence quality and schedule checker. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md` | Visible VRM and image-to-case matcher. |
| `docs/reference/raw/collisionrelateddocs/claudechat.md` | Image ordering rule: two preview images followed by all images including previews. |

## Workspace Layout

- `README.md` — this file
- `tickets/` — active tickets
- `option-papers/` — unresolved decisions
- `archived_plans/` — implemented and superseded plans
