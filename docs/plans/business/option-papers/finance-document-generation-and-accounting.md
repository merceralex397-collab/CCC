# Option Paper: Finance Document Generation + Accounting

Status: open (fee-note/invoice skill is near-term; accounting integration deferred)
Owner: unassigned
Created: 2026-05-29
Group: business / finance (G5)
Source links: `docs/superpowers/specs/2026-05-29-business-design.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/evidence_package_contract_v1.md`, `../collisionplugin/assets/feenoteexample.pdf`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md`

## Context

The work-item + evidence-package contracts already carry payment metadata (`payment_status`, `payment_chaser_sent`, `portal_submission_id`); `collisionplugin` has a fee-note example PDF. The decision (2026-05-29) is to plan fee-note/invoice **document generation as a near-term `ce-branding`-based skill**, and keep accounting/payment integration as a deferred option.

## Near-term: fee-note/invoice generation skill

- A skill in the `agent-skills` catalogue (content) using `ce-branding` (logo/layout) + work-item data → fee-note/invoice PDF in CE house style.
- `finance` owns the **fee rules + approval workflow**; the skill renders. Output is a review aid; a named human approves.
- Buildable once `agent-skills` ce-branding + `casework` work-item payment metadata exist.

## Deferred option: accounting/payment integration

Evaluate accounting-system integration + payment status sync + (possibly) automated chasers — all **governance-gated, no automation now**. Options: metadata-only (current), one-way export to accounting, two-way sync (highest risk).

## Decision Criteria

Fee-rule source of truth (per provider/principal — coordinate `parser/providers`); house-style fidelity (ce-branding); named-human approval; which accounting system; whether payment automation is ever in scope; audit.

## Governance Gates

No payment automation / autonomous chasers without explicit approval; finance docs are review aids; PII/financial-data handling review.

## Open Questions

Fee-rule structure + source; accounting system; automation appetite; how invoice/fee-note evidence is retained in the package.
