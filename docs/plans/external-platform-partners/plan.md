# External Platform Partners Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md`, `docs/architecture/future_system_convergence.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: governance-security, case-workflow-state, intake-storage-integrations, product-business
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/external-platform-partners/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/external-platform-partners/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/external-platform-partners/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md` | Customer self-service portal plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md` | External partner API plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md` | Insurance platform integration plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md` | Audatex/estimating-system partnership plan. |
| `docs/architecture/future_system_convergence.md` | Portal/API guardrails and convergence rule. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] customer self-service portal option papers | `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md`<br>`docs/architecture/future_system_convergence.md` | `governance-security`, `case-workflow-state`, `intake-storage-integrations`, `product-business` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] external partner API option papers | `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md`<br>`docs/architecture/future_system_convergence.md` | `governance-security`, `case-workflow-state`, `intake-storage-integrations`, `product-business` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] insurer platform and structured-feed integrations | `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md`<br>`docs/architecture/future_system_convergence.md` | `governance-security`, `case-workflow-state`, `intake-storage-integrations`, `product-business` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] Audatex/estimating-system partnership discovery | `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md`<br>`docs/architecture/future_system_convergence.md` | `governance-security`, `case-workflow-state`, `intake-storage-integrations`, `product-business` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] partner access controls and security gates | `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md`<br>`docs/architecture/future_system_convergence.md` | `governance-security`, `case-workflow-state`, `intake-storage-integrations`, `product-business` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S3

- [ ] Consume source metadata from intake integrations without creating external access yet.

### S5

- [ ] Write option papers for customer portal, partner API, and high-value partner commitments.

### S6

- [ ] Pursue insurer/Audatex partnerships only through approved licensed routes and governance sign-off.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `case-workflow-state` | Work-item state, review status, blockers, audit events, and approvals are the operational source of truth. |
| `intake-storage-integrations` | Outlook, Box, EVA/Sentry, website/WhatsApp, and spreadsheet bridges own live system boundaries and source capture. |
| `product-business` | Commercial framing, discovery, objections, ROI, and independence wording shape priority without owning implementation. |

## Non-Overlap Rules

The workspace explicitly does not own:

- internal intake metadata capture
- finance billing logic
- estimate parsing of supplied PDFs

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
