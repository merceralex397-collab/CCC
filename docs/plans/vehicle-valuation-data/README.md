# Vehicle Valuation Data Workspace

## Purpose

This workspace owns all planning for vehicle intelligence, DVLA/DVSA data, MOT history, mileage estimation, mileage anomaly review, valuation evidence, salvage, vehicle identity normalisation, and data governance for vehicle data.

## Scope Rules

- Valuation evidence supports a case; it must not automatically decide uplift.
- Personal injury and KADOE are out of scope.
- DVLA/DVSA API access requires vendor/API governance review before implementation.
- Mileage data must record source and confidence — staff reviewers make the final determination.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md` | MOT bulk delta ingestion approach. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/04_mileage_estimation_engine.md` | Mileage estimation engine design. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/05_mileage_anomaly_review.md` | Mileage anomaly detection and review workflow. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/08_dvla_vrm_attribute_cache.md` | DVLA VRM attribute cache design. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md` | Valuation evidence store design. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md` | Valuation, vehicle data, and uplift review. |

## Workspace Layout

- `README.md` — this file
- `tickets/` — active tickets
- `option-papers/` — unresolved decisions
- `archived_plans/` — implemented and superseded plans
