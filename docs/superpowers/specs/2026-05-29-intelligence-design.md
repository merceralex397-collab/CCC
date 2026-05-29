# Intelligence: Evidence, Vehicle Data, and Engineer Comms — Design

Date: 2026-05-29
Status: approved design (brainstorming output) — design + option-papers this iteration, build deferred
Owner: unassigned
Workspace: `docs/plans/intelligence/` (group home; sub-areas in evidence-estimate-review / vehicle-valuation-data / engineer-communications)
Source links: `docs/plans/intelligence/context.md`, `../collisionplugin/skills/valuation/vehicle-valuation/SKILL.md`, `../collisionplugin/skills/valuation/vehicle-valuation/references/valuation-methodology.md`, `../collisionplugin/skills/valuation/totalloss/`, `../collisionplugin/rebuttal/projecttext.md`, `docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md`

## Context

Intelligence provides domain review-aids and engineer outputs over reviewed cases: `evidence`, `vehicle`, `comms`. It depends on parser + casework + the DVSA tool, which are being planned now, so this iteration is **design + governance option-papers**, not build.

## Decisions captured (user, 2026-05-29)

- **Depth:** design the three sub-areas + the boundary vs `agent-skills` + governance option-papers; build deferred.
- **Lead sub-area:** `vehicle`.
- **Vehicle data (three-pronged):** keep the valuation skill's **live-fetch** (DVSA-MOT + Autotrader per-case) **and** build up a **CCC valuation/MOT evidence store** over time **and** **research & develop the CCC valuation methodology**.
- **Firm:** all outputs are review aids; named humans retain expert judgement + final conclusions; outputs source-linked; no autonomous send.

## Goals / Non-goals

**Goals:** clear sub-area designs + the agent-skills boundary; the vehicle three-pronged data approach; option-papers for vehicle-data evidence-store + licensing/retention, the valuation methodology R&D, and Audatex/ABP estimate-review positioning.

**Non-goals (this iteration):** building the stores/aids (blocked on parser/casework/DVSA); final valuation/uplift decisions; commercial Audatex partnership; broad analytics warehouse. Personal injury and KADOE remain out of scope.

## Design

### Boundary vs agent-skills (firm)

`agent-skills` owns the reusable skill content (vehicle-valuation, total-loss, rebuttal, roadworthy); intelligence owns the **domain data + workflow** those skills consume/produce. Same registry of skills, different ownership of the data and the business workflow.

### vehicle (lead) — three-pronged data approach

1. **Live-fetch (now):** per-case MOT via the DVSA-MOT tool (`mcp-tooling`) and market comps via Autotrader (Codex), as the valuation skill does today. Lowest licensing/retention burden.
2. **Evidence store (build up over time):** a CCC-owned valuation/MOT/DVLA evidence store that accumulates fetched + reviewed evidence with source confidence and provenance — option-paper covers MOT bulk/delta ingestion, DVLA VRM cache, market valuation evidence store, licensing + retention. Overlaps `analytics-data-platform` (which only consumes reviewed canonical data) and is governance-gated.
3. **Valuation methodology R&D:** research and develop the CCC valuation methodology (comparability rules, ABI/benchmark basis, forensic validation, defensible assessed-value derivation, VAT/commercial handling) — consolidating and evolving `collisionplugin/.../references/valuation-methodology.md`, `external-wording.md`, `vat-and-commercial-vehicles.md`. This methodology is the expert content the valuation skill encodes; evolving it improves every valuation output. Expert sign-off applies.

### evidence

Image quality / visible-VRM / image-ordering assistance (coordinate with parser packaging); evidence matching + duplicate/reused flags (over the work-item store); Audatex/repair-estimate parsing + QA flags (skill = total-loss; workflow here); ABP charge review pack — kept to **factual, defensible positioning** (option-paper). ANDIE-style long-range damage workbench is later (S6).

### comms

Engineer pack assembly + template manager + report-support + missing-info/status communication, all routing the valuation/rebuttal/roadworthy skill outputs to **named-human sign-off**; communications approval/audit/handoff. No autonomous external send.

## Sequencing

vehicle (lead) → evidence → comms. This iteration produces designs + the three option-papers; build follows once parser/casework/DVSA land and governance approves the data/licensing items.

## Governance Option-Papers (this iteration)

1. `option-papers/vehicle-data-evidence-store-and-licensing.md`
2. `option-papers/valuation-methodology.md`
3. `option-papers/audatex-abp-estimate-review-positioning.md`

## Risks & Open Questions

- Vehicle-data licensing/retention (DVLA/DVSA/MOT + market) and overlap with analytics ownership.
- Valuation methodology is expert IP — who owns/signs off the methodology and its evolution.
- Audatex/ABP positioning must avoid commercial-partnership scope and stay defensible.
- Evidence store vs live-fetch consistency (the same case fetched twice may differ over time).

## Acceptance Criteria

- The three sub-area designs + the agent-skills boundary are documented.
- The vehicle three-pronged approach (live-fetch + evidence store + methodology R&D) is specified.
- The three governance option-papers exist with options, decision criteria, and gates.
