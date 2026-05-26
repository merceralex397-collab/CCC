# Analytics Data Platform Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/21_client_principal_management_intelligence.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_07_advanced_analytics.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, operations-quality, governance-security, vehicle-valuation-data
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/analytics-data-platform/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/analytics-data-platform/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Data, analytics, historical mining, BI, data quality, and continuous improvement planning.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- operations analytics and KPI dictionaries
- client/principal intelligence and data quality metrics
- data warehouse, archival, EVA report mining, and historical case lake option papers
- risk indicators, predictive scheduling, and continuous improvement programme

## Does Not Own

- operational monitoring and incident runbooks
- vehicle evidence facts needed in active case review
- AI model evaluation substrate

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md` | Job sheet and operations analytics plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/21_client_principal_management_intelligence.md` | Client/principal management intelligence plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md` | Data quality, confidence, and explainability plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_07_advanced_analytics.md` | Advanced analytics and BI plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md` | Data warehouse and archival plan. |

## Cross-Workspace Dependencies

- case-workflow-state
- operations-quality
- governance-security
- vehicle-valuation-data

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
