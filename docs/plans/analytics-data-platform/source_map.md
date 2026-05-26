# Analytics Data Platform Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/21_client_principal_management_intelligence.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_07_advanced_analytics.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, operations-quality, governance-security, vehicle-valuation-data
Expected outputs: source-to-plan traceability for `docs/plans/analytics-data-platform/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/analytics-data-platform/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md` | Job sheet and operations analytics plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/21_client_principal_management_intelligence.md` | Client/principal management intelligence plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md` | Data quality, confidence, and explainability plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_07_advanced_analytics.md` | Advanced analytics and BI plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md` | Data warehouse and archival plan. |

## Ownership Boundary

Primary ownership:

- operations analytics and KPI dictionaries
- client/principal intelligence and data quality metrics
- data warehouse, archival, EVA report mining, and historical case lake option papers
- risk indicators, predictive scheduling, and continuous improvement programme

Explicit exclusions:

- operational monitoring and incident runbooks
- vehicle evidence facts needed in active case review
- AI model evaluation substrate

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
