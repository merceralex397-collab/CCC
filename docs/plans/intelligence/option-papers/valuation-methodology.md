# Option Paper: CCC Valuation Methodology (Research & Development)

Status: open (research/development — expert content)
Owner: unassigned
Created: 2026-05-29
Group: intelligence / vehicle (G3-G4)
Source links: `docs/superpowers/specs/2026-05-29-intelligence-design.md`, `../collisionplugin/skills/valuation/vehicle-valuation/references/valuation-methodology.md`, `../collisionplugin/skills/valuation/vehicle-valuation/references/external-wording.md`, `../collisionplugin/skills/valuation/vehicle-valuation/references/vat-and-commercial-vehicles.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md`

## Context

The valuation methodology is the expert content that turns market + guide evidence into a **defensible assessed retail value**. It is currently encoded in the collisionplugin valuation skill's references (comparability rules, ABI/benchmark basis, forensic validation, VAT/commercial handling, external wording). The decision (2026-05-29) is to **research and develop a consolidated CCC valuation methodology** that the valuation skill (and any future tool) encodes — improving every valuation output.

## Scope Of The R&D

- Consolidate and evolve the existing methodology references into a canonical CCC methodology document.
- Comparability rules (mileage/age/trim/spec/provenance/seller-type/import) and evidence sufficiency thresholds.
- Benchmark basis (ABI and recognised guides) and how guide vs market-only modes are reconciled.
- Forensic validation / defensibility (how to withstand challenge), VAT + commercial-vehicle handling, salvage context.
- Approved external wording vs internal strategy language (already encoded — keep aligned).

## Decision Criteria / Questions

Who owns and signs off the methodology (it is expert IP); how it stays defensible and independent; how method changes are versioned and reflected in the valuation skill + evaluation set (coordinate `agent-skills` + `ai-platform/platform-tools`); how the evidence store + live-fetch feed it.

## Governance Gates

Expert sign-off on the methodology; outputs remain review aids with named-human approval; no autonomous valuation decisions; conservative, defensible positioning.

## Relationship To agent-skills

The **methodology** (this paper) is the expert content; the **vehicle-valuation skill** (`agent-skills`) is the runnable encoding of it. Keep them in lockstep: methodology changes → skill update + re-evaluation.
