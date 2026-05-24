# Finance Billing Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_14_invoice_and_payment_workflow_automation.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/evidence_package_contract_v1.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, provider-principal-config, intake-storage-integrations, governance-security
Expected outputs: source-to-plan traceability for `docs/plans/finance-billing/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/finance-billing/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md` | Invoice/fee-note generation tool plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_14_invoice_and_payment_workflow_automation.md` | Invoice and payment workflow automation plan. |
| `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md` | Website form, payment status, invoice, and chaser evidence. |
| `docs/contracts/work_item_contract_v1.md` | Payment status and chaser metadata fields. |
| `docs/contracts/evidence_package_contract_v1.md` | Invoice, summary, and payment metadata package rules. |

## Ownership Boundary

Primary ownership:

- invoice and fee-note document generation
- fee rules and finance approval workflow
- payment status, payment chaser metadata, overdue visibility
- payment/accounting integration option papers

Explicit exclusions:

- repair estimate review
- external customer portal product scope
- early parser-owned payment automation

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
