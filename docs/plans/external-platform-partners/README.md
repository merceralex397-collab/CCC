# External Platform Partners Workspace

## Purpose

This workspace owns all planning for customer portal, partner API, insurer integrations, Audatex partnerships, and partner access controls.

## Scope Rules

- All external access items start in `option-papers/` — no implementation ticket until auth, audit, retention, and data minimisation are approved.
- No external access until security model and governance sign-off are complete.
- Personal injury and KADOE are out of scope.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md` | Customer self-service portal design. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md` | API for external partners design. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md` | Insurance platform integration. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md` | Audatex and estimating system partnerships. |

## Workspace Layout

- `README.md` — this file
- `tickets/` — active tickets (only after option-paper approval)
- `option-papers/` — portal, API, insurer, Audatex proposals
- `archived_plans/` — implemented and superseded plans
