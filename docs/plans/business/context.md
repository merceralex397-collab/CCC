# Business Workspace — Context (Information Document)

Date: 2026-05-29
Status: active context document
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: business (G5, layer: business-external) — see `docs/plans/_groups.md`
Source links: `docs/plans/finance-billing/plan.md`, `docs/plans/external-platform-partners/plan.md`, `docs/plans/product-business/plan.md`, `docs/plans/analytics-data-platform/plan.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/evidence_package_contract_v1.md`, `../collisionplugin/assets/feenoteexample.pdf`

Group home for the business broad workspace. Sub-areas (current folders pending the deferred move): `finance` ← `finance-billing/`, `partners` ← `external-platform-partners/`, `product` ← `product-business/`, `analytics` ← `analytics-data-platform/`.

## What this workspace owns

- **finance**: invoice + fee-note generation; fee rules + finance approval workflow; payment status / chaser metadata / overdue visibility; payment/accounting integration option-papers.
- **partners**: customer self-service portal; external partner API; insurer platform + structured-feed integrations; Audatex/estimating partnership discovery; partner access controls.
- **product**: discovery + stakeholder decisions; ROI/KPI framing; client pitch + objection handling; conservative positioning + independence/defensibility wording.
- **analytics**: operations analytics + KPI dictionaries; client/principal intelligence + data-quality metrics; data warehouse / archival / EVA-mining / case-lake option-papers; risk indicators / predictive scheduling / continuous improvement.

## Timing and posture

This is the latest functional group (G5), almost entirely **option-paper + governance-gated**: external access, partner APIs, portals, payment automation, warehouses, and commercial data all start in option-papers, not implementation. `analytics` consumes **reviewed canonical data only** (no ungoverned warehouse). `finance` records payment/invoice evidence as **metadata first** (no early payment automation). `product` is framing/positioning, not implementation.

## Near-term connections

- **finance** has the most concrete near-term material: the work-item + evidence-package contracts already carry `payment_status`, `payment_chaser_sent`, `portal_submission_id`; `collisionplugin` has a fee-note example PDF and the valuation skill produces fee notes — so fee-note/invoice **document generation** could build on the `agent-skills` `ce-branding` skill + work-item metadata.
- **partners** overlaps the `bridge` (internal intake metadata is bridge; the external portal *product* is partners) and `intelligence/evidence` (estimate parsing is evidence; Audatex *partnership* is partners).
- **analytics** consumes `casework` canonical events + package metadata; no warehouse until retention/licensing/data-quality mature.
- **product** framing draws on the CE context pack (project brief, business context, ROI, discovery, pitch).

## Boundaries

Does not own: estimate parsing/review (`intelligence/evidence`); internal intake metadata capture (`bridge`); governance policy ownership (`governance-security`); operational monitoring/runbooks (`operations-quality`); AI eval substrate (`ai-platform`); vehicle evidence facts (`intelligence/vehicle`).

## Guardrails

External access, partner APIs, portals, payment automation, warehouse, and commercial data are governance-gated and start as option-papers. Conservative, defensible product positioning (CCC = vehicle-damage intake/evidence/admin support, not autonomous expert judgement). Personal injury and KADOE remain out of scope.

## Open design questions for the interview

1. Depth: design + option-papers across all four (build deferred), prioritise one sub-area, or build now?
2. Which sub-area(s) to flesh out most (finance has the most near-term material)?
3. Finance: build fee-note/invoice document generation soon (as a `ce-branding`-based skill over work-item metadata), or keep metadata-only + an accounting-integration option-paper?
