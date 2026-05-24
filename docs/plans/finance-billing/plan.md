# Finance Billing Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_14_invoice_and_payment_workflow_automation.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/evidence_package_contract_v1.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, provider-principal-config, intake-storage-integrations, governance-security
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/finance-billing/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/finance-billing/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/finance-billing/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md` | Invoice/fee-note generation tool plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_14_invoice_and_payment_workflow_automation.md` | Invoice and payment workflow automation plan. |
| `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md` | Website form, payment status, invoice, and chaser evidence. |
| `docs/contracts/work_item_contract_v1.md` | Payment status and chaser metadata fields. |
| `docs/contracts/evidence_package_contract_v1.md` | Invoice, summary, and payment metadata package rules. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] invoice and fee-note document generation | `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_14_invoice_and_payment_workflow_automation.md`<br>`docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`<br>`docs/contracts/work_item_contract_v1.md`<br>`docs/contracts/evidence_package_contract_v1.md` | `case-workflow-state`, `provider-principal-config`, `intake-storage-integrations`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] fee rules and finance approval workflow | `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_14_invoice_and_payment_workflow_automation.md`<br>`docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`<br>`docs/contracts/work_item_contract_v1.md`<br>`docs/contracts/evidence_package_contract_v1.md` | `case-workflow-state`, `provider-principal-config`, `intake-storage-integrations`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] payment status, payment chaser metadata, overdue visibility | `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_14_invoice_and_payment_workflow_automation.md`<br>`docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`<br>`docs/contracts/work_item_contract_v1.md`<br>`docs/contracts/evidence_package_contract_v1.md` | `case-workflow-state`, `provider-principal-config`, `intake-storage-integrations`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] payment/accounting integration option papers | `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_14_invoice_and_payment_workflow_automation.md`<br>`docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`<br>`docs/contracts/work_item_contract_v1.md`<br>`docs/contracts/evidence_package_contract_v1.md` | `case-workflow-state`, `provider-principal-config`, `intake-storage-integrations`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S3

- [ ] Record payment and invoice evidence as metadata without authorising payment automation.

### S5

- [ ] Plan draft invoice/fee-note generation from approved case data and provider fee rules.

### S6

- [ ] Evaluate accounting/payment integrations and autonomous chasers only through option papers and governance approval.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `case-workflow-state` | Work-item state, review status, blockers, audit events, and approvals are the operational source of truth. |
| `provider-principal-config` | Provider/principal presets, routing, aliases, and admin workflows must stay separate from parser mechanics. |
| `intake-storage-integrations` | Outlook, Box, EVA/Sentry, website/WhatsApp, and spreadsheet bridges own live system boundaries and source capture. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |

## Non-Overlap Rules

The workspace explicitly does not own:

- repair estimate review
- external customer portal product scope
- early parser-owned payment automation

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
