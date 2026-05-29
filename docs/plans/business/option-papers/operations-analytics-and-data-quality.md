# Option Paper: Operations Analytics + Data Quality

Status: open (canonical-events analytics near-term; warehouse deferred)
Owner: unassigned
Created: 2026-05-29
Group: business / analytics (G5)
Source links: `docs/superpowers/specs/2026-05-29-business-design.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md`, `docs/contracts/review_audit_event_contract_v1.md`

## Context

Analytics must build **only from reviewed canonical data**: `casework` work-item events, review/audit events, package/export metadata. No ungoverned warehouse. The decision (2026-05-29) is to flesh out operations analytics + data quality from canonical events; defer warehouse/EVA-mining/risk-indicators to option-papers.

## Near-term: canonical-events analytics

- **KPI dictionary** v1: queue health (ready/missing/review/export counts), throughput, blocker reasons, provider/principal volumes, time-in-state — all derived from `casework` events.
- **Data-quality/confidence metrics**: extraction confidence distribution, review-correction rates, missing-info frequency.
- Read-only over the work-item store/events; no new data source.

## Deferred options

Data warehouse / archival / EVA report mining / historical case lake / risk indicators / predictive scheduling — each an option-paper, gated on retention/licensing/data-quality maturity.

## Decision Criteria

Canonical-events-only discipline; boundary with `operations-quality` (operational health) vs business KPIs; retention/privacy for any persisted analytics; what v1 KPI set delivers value; explainability of metrics.

## Governance Gates

Reviewed-canonical-data only; warehouse/mining/commercial-data require governance + retention sign-off.

## Open Questions

v1 KPI set; analytics vs operations-quality boundary; warehouse trigger; where analytics outputs surface (casework dashboard vs separate).
