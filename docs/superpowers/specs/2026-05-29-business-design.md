# Business: Finance, Analytics, Partners, Product — Design

Date: 2026-05-29
Status: approved design (brainstorming output) — design + option-papers this iteration, build deferred
Owner: unassigned
Workspace: `docs/plans/business/` (group home; sub-areas in finance-billing / analytics-data-platform / external-platform-partners / product-business)
Source links: `docs/plans/business/context.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/evidence_package_contract_v1.md`, `../collisionplugin/assets/feenoteexample.pdf`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md`

## Context

Business is the latest functional group (G5), almost entirely option-paper + governance-gated. This iteration designs the four sub-areas and writes the governance option-papers; `analytics` and `finance` get the most concrete attention.

## Decisions captured (user, 2026-05-29)

- **Depth:** design + option-papers across all four; build deferred.
- **Flesh out most:** `analytics` and `finance`.
- **Finance fee-note/invoice:** plan as a **near-term `ce-branding`-based skill** over work-item payment metadata + the fee-note example — a concrete early finance win.

## Goals / Non-goals

**Goals:** designs for finance/analytics/partners/product + the agent-skills boundary for finance docs; the finance fee-note/invoice skill plan + accounting option-paper; the operations-analytics + data-quality design; the partner/portal/API option-papers; conservative product positioning.

**Non-goals (this iteration):** building portals/partner-APIs/payment-automation/warehouse; estimate review (`intelligence`); intake metadata (`bridge`); governance policy ownership (`governance-security`); AI eval substrate (`ai-platform`). Personal injury and KADOE remain out of scope.

## Design

### finance (flesh out)

- **Fee-note/invoice document generation = a new skill** in the `agent-skills` catalogue, using the `ce-branding` skill + the fee-note example + work-item payment metadata (`payment_status`, `payment_chaser_sent`, `portal_submission_id`). Boundary: `agent-skills` owns the skill content; `finance` owns the **fee rules + finance approval workflow + payment-status/chaser/overdue logic**.
- Payment/accounting integration stays an **option-paper** (no payment automation now).
- Outputs are review aids; a named human approves fee notes/invoices.

### analytics (flesh out)

- Operations analytics + **KPI dictionaries** built **only from `casework` canonical events + reviewed work items + package/export metadata** — not raw operational side effects.
- Client/principal intelligence + **data-quality/confidence metrics**.
- Warehouse / archival / EVA-mining / case-lake / risk-indicators / predictive-scheduling remain **option-papers** (deferred until retention/licensing/data-quality mature). Boundary: not operational monitoring (`operations-quality`), not vehicle evidence facts (`intelligence/vehicle`).

### partners

Customer self-service portal, external partner API, insurer/structured-feed integration, Audatex/estimating **partnership discovery**, and partner access controls — all **option-papers** with security/access gates. Boundary: the external portal *product* is here; internal intake metadata is `bridge`; estimate *parsing* is `intelligence/evidence`.

### product

Conservative positioning + ROI/KPI framing + discovery + objection handling: CCC is **vehicle-damage intake/evidence/admin support, not autonomous expert judgement**. Framing that shapes priority; not implementation.

## Sequencing

Design all four now. Finance fee-note skill is the first buildable item (after `agent-skills` ce-branding + `casework` work-item metadata exist). Analytics starts once `casework` emits canonical events. Partners/product remain option-papers/framing.

## Option-Papers (this iteration)

1. `option-papers/finance-document-generation-and-accounting.md`
2. `option-papers/operations-analytics-and-data-quality.md`
3. `option-papers/external-portal-and-partner-api.md`

## Risks & Open Questions

- Finance docs depend on `agent-skills` ce-branding + `casework` payment metadata existing first.
- Analytics must not become an ungoverned warehouse; canonical-events-only discipline.
- Partner/portal/insurer/Audatex are commercial + security-sensitive — option-papers only.
- Product positioning must stay conservative/defensible (independence).

## Acceptance Criteria

- Four sub-area designs + the finance↔agent-skills boundary documented.
- Finance fee-note/invoice planned as a ce-branding skill; accounting integration in an option-paper.
- Analytics design uses canonical events only; warehouse deferred to option-paper.
- Partner/portal/API option-papers exist with access/security gates; product positioning recorded.
