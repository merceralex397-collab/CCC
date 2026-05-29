# Option Paper: Audatex / ABP Estimate-Review Positioning

Status: open (design — not approved for build)
Owner: unassigned
Created: 2026-05-29
Group: intelligence / evidence (G3-G4)
Source links: `docs/superpowers/specs/2026-05-29-intelligence-design.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md`, `../collisionplugin/skills/valuation/totalloss/`

## Context

Evidence-side estimate review parses Audatex/repair estimates and produces QA flags + an ABP charge review pack. The reference material includes an explicit "safe positioning" context for Audatex/ABP, signalling the area is commercially and legally sensitive. The collisionplugin `total-loss` skill already generates EVA/Audatex-compatible PDFs. This paper sets how CCC positions estimate review.

## Options

1. **Factual QA flags only** — flag arithmetic/labour-time/parts/duplication issues against the estimate, no commercial judgement. Lowest risk; defensible.
2. **QA flags + ABP charge review pack** — structured review of ABP charges with factual commentary for the engineer to sign off.
3. **Comparative/benchmarking commentary** — broader market/benchmark commentary on charges. Higher value, higher sensitivity; risks straying toward commercial-partnership scope.

## Decision Criteria

Defensibility + independence; staying clear of Audatex **commercial partnership** scope (owned by `external-platform-partners`, not here); factual vs judgemental commentary; expert sign-off; alignment with the total-loss skill's EVA routing rules.

## Governance Gates

Expert sign-off on any charge commentary; factual/defensible positioning only; no commercial-partnership commitments; coordinate `governance-security` on expert-boundary + risk language.

## Open Questions

How far ABP commentary can go while staying factual; the boundary with `external-platform-partners` (Audatex partnership discovery); reuse of the total-loss skill's routing rules for QA flags.
