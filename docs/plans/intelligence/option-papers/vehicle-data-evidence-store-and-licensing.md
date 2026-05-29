# Option Paper: Vehicle-Data Evidence Store + Licensing

Status: open (design — not approved for build)
Owner: unassigned
Created: 2026-05-29
Group: intelligence / vehicle (G3-G4)
Source links: `docs/superpowers/specs/2026-05-29-intelligence-design.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/08_dvla_vrm_attribute_cache.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md`

## Context

Vehicle data is fetched live today (DVSA-MOT MCP, Autotrader via Codex) per case. The decision (2026-05-29) is to also **accumulate a CCC-owned valuation/MOT/DVLA evidence store** over time, with source confidence and provenance, while keeping live-fetch. This paper covers what to store, licensing, and retention.

## Options

1. **Live-fetch only + per-case snapshots** retained inside the work item/package (no separate store). Simplest; no central data asset.
2. **Evidence store accumulating reviewed fetches** (DVLA VRM cache, MOT history, market comps) with provenance/confidence + retention rules. Builds a reusable asset; licensing + retention governance.
3. **Bulk/delta ingestion** (e.g. MOT bulk + delta) into the store ahead of need. Most capable; heaviest licensing/storage/governance, overlaps `analytics-data-platform`.

## Decision Criteria

DVLA/DVSA/MOT and market-data **licensing terms** for storage/reuse (vs per-case fetch); retention limits + PII; provenance/confidence + live-vs-stored reconciliation; storage cost; boundary with `analytics-data-platform` (reviewed canonical data only, not an ungoverned warehouse); value of a reusable evidence asset for valuation defensibility.

## Governance Gates

Data licensing + retention + privacy review (governance-security) before any persistent store. The store holds reviewed evidence with provenance; it is not a free-form data lake.

## Open Questions

Licensing for storing vs fetching MOT/DVLA/market data; retention window; how stored evidence is versioned when live data later differs; the analytics boundary.
