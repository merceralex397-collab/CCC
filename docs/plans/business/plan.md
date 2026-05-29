# Business Plan (group home)

Date: 2026-05-29
Status: active workspace plan
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: business
Wave: G5
Layer: business-external
Source links: `docs/plans/business/context.md`, `docs/superpowers/specs/2026-05-29-business-design.md`, `docs/plans/finance-billing/plan.md`, `docs/plans/analytics-data-platform/plan.md`, `docs/plans/external-platform-partners/plan.md`, `docs/plans/product-business/plan.md`
Roadmap milestone: G5 business-external
Dependencies: case-workflow-state (casework), agent-skills, intelligence, governance-security, operations-quality
Expected outputs: sub-area designs, governance option papers, and a sequenced plan for `docs/plans/business/`
Acceptance criteria: each promoted item cites source evidence, names dependencies, respects boundaries, and carries governance gates; external/financial work starts in option-papers
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/business/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

This is the **business** broad-workspace group home. Sub-areas (current folders pending the deferred move): `finance` ← `finance-billing/`, `analytics` ← `analytics-data-platform/`, `partners` ← `external-platform-partners/`, `product` ← `product-business/`. See `docs/plans/_groups.md`.

## This Iteration — Design + Option-Papers (analytics + finance fleshed out)

Approved design: `docs/superpowers/specs/2026-05-29-business-design.md`. Decisions (2026-05-29): design + option-papers across all four; flesh out analytics + finance; finance fee-note/invoice = a near-term ce-branding-based skill.

| Sub-area | This iteration |
| --- | --- |
| `finance` (flesh out) | Fee-note/invoice generation as a `ce-branding`-based skill over work-item payment metadata; fee rules + approval workflow; accounting integration = option-paper. |
| `analytics` (flesh out) | Operations analytics + KPI dictionaries from `casework` canonical events; data-quality metrics. Warehouse/EVA-mining/risk-indicators = option-papers. |
| `partners` | Portal / partner API / insurer / Audatex partnership + access controls = option-papers. |
| `product` | Conservative positioning, ROI/KPI framing, discovery, objection handling. |

Option-papers (group home `option-papers/`): finance document generation + accounting; operations analytics + data quality; external portal + partner API.

## Boundaries

`agent-skills` owns the fee-note skill *content*; `finance` owns fee rules + workflow. Estimate review = `intelligence/evidence`; intake metadata = `bridge`; operational monitoring = `operations-quality`; governance policy = `governance-security`; AI eval substrate = `ai-platform`.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `casework` | Canonical events + work-item payment metadata feed analytics + finance. |
| `agent-skills` | ce-branding + the fee-note/invoice skill content. |
| `intelligence` | Valuation/estimate outputs relate to fee notes + analytics; keep boundaries. |
| `governance-security` | External access, partner APIs, portals, payment automation, warehouse, commercial data gates. |
| `operations-quality` | Owns operational monitoring; analytics is business KPIs, not operational health. |

## Non-Overlap Rules

Does not own: estimate parsing/review (`intelligence`); intake metadata (`bridge`); governance policy (`governance-security`); operational monitoring (`operations-quality`); AI eval substrate (`ai-platform`); vehicle evidence facts (`intelligence/vehicle`). Personal injury and KADOE remain out of scope.

## Promotion Gates

- External access, partner APIs, portals, payment automation, warehouse, and commercial data start in `option-papers/`.
- Analytics consumes reviewed canonical data only — no ungoverned warehouse.
- Finance documents are review aids with named-human approval; no early payment automation.
- Conservative, defensible product positioning.
