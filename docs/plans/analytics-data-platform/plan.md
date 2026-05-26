# Analytics Data Platform Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/21_client_principal_management_intelligence.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_07_advanced_analytics.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, operations-quality, governance-security, vehicle-valuation-data
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/analytics-data-platform/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/analytics-data-platform/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/analytics-data-platform/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md` | Job sheet and operations analytics plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/21_client_principal_management_intelligence.md` | Client/principal management intelligence plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md` | Data quality, confidence, and explainability plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_07_advanced_analytics.md` | Advanced analytics and BI plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md` | Data warehouse and archival plan. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] operations analytics and KPI dictionaries | `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/21_client_principal_management_intelligence.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_07_advanced_analytics.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md` | `case-workflow-state`, `operations-quality`, `governance-security`, `vehicle-valuation-data` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] client/principal intelligence and data quality metrics | `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/21_client_principal_management_intelligence.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_07_advanced_analytics.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md` | `case-workflow-state`, `operations-quality`, `governance-security`, `vehicle-valuation-data` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] data warehouse, archival, EVA report mining, and historical case lake option papers | `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/21_client_principal_management_intelligence.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_07_advanced_analytics.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md` | `case-workflow-state`, `operations-quality`, `governance-security`, `vehicle-valuation-data` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] risk indicators, predictive scheduling, and continuous improvement programme | `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/21_client_principal_management_intelligence.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_07_advanced_analytics.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md` | `case-workflow-state`, `operations-quality`, `governance-security`, `vehicle-valuation-data` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S4-S5

- [ ] Start from canonical event/work-item data for operations analytics, data quality, and ROI metrics.

### S5

- [ ] Add client/principal intelligence and continuous improvement workflows.

### S6

- [ ] Plan warehouse, EVA mining, risk indicators, scheduling, and BI only after governance and data quality mature.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `case-workflow-state` | Work-item state, review status, blockers, audit events, and approvals are the operational source of truth. |
| `operations-quality` | Release, rollback, regression, monitoring, runbooks, pilot, support, and decommissioning gates must be explicit. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `vehicle-valuation-data` | Vehicle facts and valuation evidence need licensing, confidence, provenance, and human review boundaries. |

## Non-Overlap Rules

The workspace explicitly does not own:

- operational monitoring and incident runbooks
- vehicle evidence facts needed in active case review
- AI model evaluation substrate

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
