# Finance Billing Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_14_invoice_and_payment_workflow_automation.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/evidence_package_contract_v1.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, provider-principal-config, intake-storage-integrations, governance-security
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/finance-billing/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/finance-billing/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Finance, invoice, fee-note, payment-status, payment evidence, and billing automation option planning.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- invoice and fee-note document generation
- fee rules and finance approval workflow
- payment status, payment chaser metadata, overdue visibility
- payment/accounting integration option papers

## Does Not Own

- repair estimate review
- external customer portal product scope
- early parser-owned payment automation

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md` | Invoice/fee-note generation tool plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_14_invoice_and_payment_workflow_automation.md` | Invoice and payment workflow automation plan. |
| `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md` | Website form, payment status, invoice, and chaser evidence. |
| `docs/contracts/work_item_contract_v1.md` | Payment status and chaser metadata fields. |
| `docs/contracts/evidence_package_contract_v1.md` | Invoice, summary, and payment metadata package rules. |

## Cross-Workspace Dependencies

- case-workflow-state
- provider-principal-config
- intake-storage-integrations
- governance-security

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
