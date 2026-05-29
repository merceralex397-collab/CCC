# Intelligence Workspace — Context (Information Document)

Date: 2026-05-29
Status: active context document
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: intelligence (G3-G4, layer: intelligence) — see `docs/plans/_groups.md`
Source links: `docs/plans/evidence-estimate-review/plan.md`, `docs/plans/vehicle-valuation-data/plan.md`, `docs/plans/engineer-communications/plan.md`, `../collisionplugin/skills/valuation/vehicle-valuation/SKILL.md`, `../collisionplugin/skills/valuation/totalloss/`, `../collisionplugin/rebuttal/projecttext.md`, `../collisionplugin/roadworthy/`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md`

This is the **group home** for the intelligence broad workspace. Its three sub-areas currently live in separate folders pending the deferred physical consolidation:
- `evidence` ← `docs/plans/evidence-estimate-review/`
- `vehicle` ← `docs/plans/vehicle-valuation-data/`
- `comms` ← `docs/plans/engineer-communications/`

## What this workspace owns

Domain intelligence and the engineer-facing outputs, as **review aids** with human sign-off:
- **evidence**: evidence matching + duplicate/reused flags; image quality / visible-VRM / image-ordering assistance; Audatex/repair-estimate parsing + QA flags; ABP charge review pack; ANDIE-style long-range damage workbench.
- **vehicle**: DVLA/DVSA + MOT evidence; mileage estimation / anomaly / source confidence; vehicle identity normalisation; valuation evidence store; salvage benchmarking; prior same-VRM/case context.
- **comms**: engineer pack generation; template manager + report-support; missing-info/status communication; communications approval/audit/handoff.

## Boundary vs agent-skills (important)

`agent-skills` owns the reusable **skill content**; intelligence owns the **domain workflow + data** where a skill is used. Concretely:
- vehicle-valuation **SKILL** → `agent-skills`; the vehicle **valuation evidence / DVLA-DVSA-MOT data** → `vehicle`.
- rebuttal / roadworthy **SKILLs** → `agent-skills`; the engineer **report/communication workflow** (pack assembly, approval, handoff) → `comms`.
- total-loss Audatex **SKILL** → `agent-skills`; the **estimate-review workflow + QA flags** → `evidence`.

Expert judgement and final report conclusions stay with named humans (not owned here).

## Current state and key connections

Nothing is built in these sub-areas. Strong dependencies and connections:
- **parser** feeds parsed evidence/cases; **casework** provides the work-item/review the aids attach to (both being planned now).
- **vehicle** depends on `mcp-tooling` (the DVSA-MOT connector being rebuilt first-party; valuation skill also uses Autotrader via Codex).
- `collisionplugin` already has the production skills that produce intelligence outputs (valuation report/evidence pack, total-loss Audatex PDF, diminution rebuttal, roadworthy cert) — intelligence owns the workflows that consume/route them.

## Governance / expert-boundary themes (firm)

- DVLA/DVSA/MOT and market data: **licensing, retention, and source-confidence** controls (governance-security); a valuation evidence store has retention/privacy implications.
- Audatex/ABP: there is an explicit "safe positioning" context source — estimate review + ABP charge commentary must stay factual/defensible, not commercial-partnership scope.
- All engineer-facing outputs are **review aids**: human sign-off, no autonomous external send, source-linked.

## Dependencies

`parser` (parsed evidence), `casework` (work-item/review), `mcp-tooling` (DVSA/vehicle tools), `agent-skills` (the skills that produce outputs), `governance-security` (data licensing/retention, expert boundary), `analytics-data-platform` (only consumes reviewed canonical data — no warehouse yet).

## Guardrails

Review aids only; human judgement and final report conclusions remain with named humans; outputs are source-linked and reviewable; vehicle/market data is licensing- and retention-gated. Personal injury and KADOE remain out of scope.

## Open design questions for the interview

1. Depth this iteration: design the three sub-areas' boundaries + governance option-papers (build deferred until parser/casework/DVSA ready), build one sub-area now, or full build?
2. Which sub-area leads (evidence / vehicle / comms)?
3. Vehicle data: keep the valuation skill's live-fetch (DVSA-MOT + Autotrader via tools) for now, or build a CCC valuation/MOT evidence store now (governed)?
