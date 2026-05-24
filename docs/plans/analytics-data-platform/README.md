# Analytics Data Platform Workspace

## Purpose

This workspace owns all planning for operations analytics, data warehouse, EVA report mining, data quality, risk indicators, scheduling, and business intelligence.

## Scope Rules

- Analytics consume canonical work item and audit events — not scraped mailbox state.
- Data warehouse items are long-range planned until canonical event data exists from the Operational Core.
- Personal injury and KADOE are out of scope.
- Retention policy and storage decision must precede warehouse implementation.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/08_operations_management_intelligence.md` | Operations management and intelligence design. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md` | Job sheet and operations analytics. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/17_eva_report_mining_and_sentry_bulk_sync.md` | EVA report mining and Sentry bulk sync. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md` | Data warehouse and archival design. |

## Workspace Layout

- `README.md` — this file
- `tickets/` — active tickets
- `option-papers/` — unresolved decisions
- `archived_plans/` — implemented and superseded plans
