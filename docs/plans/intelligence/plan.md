# Intelligence Plan (group home)

Date: 2026-05-29
Status: active workspace plan
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: intelligence
Wave: G3-G4
Layer: intelligence
Source links: `docs/plans/intelligence/context.md`, `docs/superpowers/specs/2026-05-29-intelligence-design.md`, `docs/plans/evidence-estimate-review/plan.md`, `docs/plans/vehicle-valuation-data/plan.md`, `docs/plans/engineer-communications/plan.md`
Roadmap milestone: G3-G4 intelligence
Dependencies: parser-extraction, case-workflow-state (casework), mcp-and-tooling, agent-skills, governance-security, analytics-data-platform
Expected outputs: sub-area designs, governance option papers, and a sequenced build plan for `docs/plans/intelligence/`
Acceptance criteria: each promoted item cites source evidence, names dependencies, respects the agent-skills boundary, and carries governance gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/intelligence/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

This is the **intelligence** broad-workspace group home. Sub-areas (current folders pending the deferred physical move): `evidence` ← `evidence-estimate-review/`, `vehicle` ← `vehicle-valuation-data/`, `comms` ← `engineer-communications/`. See `docs/plans/_groups.md`.

## This Iteration — Design + Governance Option-Papers (build deferred)

Approved design: `docs/superpowers/specs/2026-05-29-intelligence-design.md`. Decisions (2026-05-29): design + boundaries + option-papers (build deferred); **vehicle leads**; vehicle data = live-fetch + evidence store + valuation-methodology R&D; outputs are review aids with human sign-off.

| Sub-area | This iteration |
| --- | --- |
| `vehicle` (lead) | Three-pronged data approach: keep live-fetch (DVSA-MOT + Autotrader); plan a CCC valuation/MOT evidence store; research & develop the CCC valuation methodology. |
| `evidence` | Design image quality/VRM/ordering aids, evidence matching/dup flags, Audatex estimate review + ABP positioning (factual/defensible). |
| `comms` | Design engineer pack + report-support + missing-info/status comms routing skill outputs to named-human sign-off. |

Option-papers (group home `option-papers/`): vehicle-data evidence store + licensing; valuation methodology; Audatex/ABP estimate-review positioning.

## Boundary vs agent-skills

`agent-skills` owns the skill content (vehicle-valuation, total-loss, rebuttal, roadworthy); intelligence owns the domain data + workflow consuming/producing them.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `parser` | Parsed evidence/cases feed evidence + vehicle aids. |
| `casework` | Work-item/review is where aids surface and reports attach. |
| `mcp-tooling` | DVSA-MOT tool (rebuilt first-party) + Autotrader connector for vehicle data. |
| `agent-skills` | The skills producing valuation/estimate/report outputs; keep content vs workflow separate. |
| `governance-security` | DVLA/DVSA/MOT + market data licensing/retention; expert boundary; Audatex/ABP positioning. |
| `analytics-data-platform` | Consumes reviewed canonical data only; evidence store must not become an ungoverned warehouse. |

## Non-Overlap Rules

Does not own: portable skill specs (`agent-skills`); final valuation/uplift or report conclusions (named humans); commercial Audatex partnership; broad analytics warehouse. Personal injury and KADOE remain out of scope.

## Promotion Gates

- `option-papers/` for vehicle-data licensing/retention, valuation methodology, and Audatex/ABP positioning before any build.
- All engineer-facing outputs are review aids with mandatory human sign-off and source links.
- Vehicle/market data activation is governance-gated.
