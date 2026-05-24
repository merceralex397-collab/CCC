# External Platform Partners Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md`, `docs/architecture/future_system_convergence.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: governance-security, case-workflow-state, intake-storage-integrations, product-business
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/external-platform-partners/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/external-platform-partners/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

External-facing systems, customer/partner portals, partner APIs, insurer integrations, Audatex partnerships, and partner access controls.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- customer self-service portal option papers
- external partner API option papers
- insurer platform and structured-feed integrations
- Audatex/estimating-system partnership discovery
- partner access controls and security gates

## Does Not Own

- internal intake metadata capture
- finance billing logic
- estimate parsing of supplied PDFs

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md` | Customer self-service portal plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md` | External partner API plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md` | Insurance platform integration plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md` | Audatex/estimating-system partnership plan. |
| `docs/architecture/future_system_convergence.md` | Portal/API guardrails and convergence rule. |

## Cross-Workspace Dependencies

- governance-security
- case-workflow-state
- intake-storage-integrations
- product-business

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
