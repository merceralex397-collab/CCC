# Vehicle Valuation Data Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/04_mileage_estimation_engine.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/08_dvla_vrm_attribute_cache.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: mcp-and-tooling, governance-security, analytics-data-platform, engineer-communications
Expected outputs: source-to-plan traceability for `docs/plans/vehicle-valuation-data/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/vehicle-valuation-data/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md` | MOT bulk/delta ingestion plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/04_mileage_estimation_engine.md` | Mileage estimation engine plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/08_dvla_vrm_attribute_cache.md` | DVLA VRM attribute cache plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md` | Market valuation evidence store plan. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md` | Vehicle data and uplift review guardrails. |

## Ownership Boundary

Primary ownership:

- DVLA/DVSA and MOT evidence planning
- mileage estimation, anomaly review, and source confidence
- vehicle identity normalization and conflict resolution
- valuation evidence store, salvage benchmarking, and prior vehicle/case context

Explicit exclusions:

- final valuation or uplift decisions
- market/commercial-provider activation without governance
- broad analytics warehouse

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
