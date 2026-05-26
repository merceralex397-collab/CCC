# External Platform Partners Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md`, `docs/architecture/future_system_convergence.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: governance-security, case-workflow-state, intake-storage-integrations, product-business
Expected outputs: source-to-plan traceability for `docs/plans/external-platform-partners/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/external-platform-partners/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md` | Customer self-service portal plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md` | External partner API plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md` | Insurance platform integration plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md` | Audatex/estimating-system partnership plan. |
| `docs/architecture/future_system_convergence.md` | Portal/API guardrails and convergence rule. |

## Ownership Boundary

Primary ownership:

- customer self-service portal option papers
- external partner API option papers
- insurer platform and structured-feed integrations
- Audatex/estimating-system partnership discovery
- partner access controls and security gates

Explicit exclusions:

- internal intake metadata capture
- finance billing logic
- estimate parsing of supplied PDFs

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
