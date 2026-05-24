# Vehicle Valuation Data Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/04_mileage_estimation_engine.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/08_dvla_vrm_attribute_cache.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: mcp-and-tooling, governance-security, analytics-data-platform, engineer-communications
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/vehicle-valuation-data/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/vehicle-valuation-data/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/vehicle-valuation-data/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md` | MOT bulk/delta ingestion plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/04_mileage_estimation_engine.md` | Mileage estimation engine plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/08_dvla_vrm_attribute_cache.md` | DVLA VRM attribute cache plan. |
| `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md` | Market valuation evidence store plan. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md` | Vehicle data and uplift review guardrails. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] DVLA/DVSA and MOT evidence planning | `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/04_mileage_estimation_engine.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/08_dvla_vrm_attribute_cache.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md` | `mcp-and-tooling`, `governance-security`, `analytics-data-platform`, `engineer-communications` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] mileage estimation, anomaly review, and source confidence | `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/04_mileage_estimation_engine.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/08_dvla_vrm_attribute_cache.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md` | `mcp-and-tooling`, `governance-security`, `analytics-data-platform`, `engineer-communications` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] vehicle identity normalization and conflict resolution | `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/04_mileage_estimation_engine.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/08_dvla_vrm_attribute_cache.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md` | `mcp-and-tooling`, `governance-security`, `analytics-data-platform`, `engineer-communications` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] valuation evidence store, salvage benchmarking, and prior vehicle/case context | `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/04_mileage_estimation_engine.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/08_dvla_vrm_attribute_cache.md`<br>`docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md` | `mcp-and-tooling`, `governance-security`, `analytics-data-platform`, `engineer-communications` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S4

- [ ] Plan factual DVLA/DVSA, MOT, mileage, and valuation evidence with source confidence and review boundaries.

### S5

- [ ] Add salvage benchmarking and prior same-VRM context once retention/licensing controls are approved.

### S6

- [ ] Keep weather, road, and traffic context as option papers unless directly needed for review.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `mcp-and-tooling` | MCP/tool exposure must wrap approved adapters with schemas, auth, audit, rate limits, and gateway controls. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `analytics-data-platform` | Analytics must consume reviewed canonical events and approved data products, not raw operational side effects. |
| `engineer-communications` | Coordinate source ownership, sequencing, acceptance criteria, and verification before ticket promotion. |

## Non-Overlap Rules

The workspace explicitly does not own:

- final valuation or uplift decisions
- market/commercial-provider activation without governance
- broad analytics warehouse

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
