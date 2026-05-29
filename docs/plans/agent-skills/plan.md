# Agent Skills Plan

Date: 2026-05-29
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-29
Group: agent-skills
Wave: parallel (alongside G1 parser / G2 bridge)
Layer: ai-tooling
Source links: `docs/plans/agent-skills/context.md`, `docs/plans/agent-skills/skill-catalogue.md`, `docs/superpowers/specs/2026-05-29-agent-skills-design.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md`, `../collisionplugin/skills/valuation/vehicle-valuation/SKILL.md`
Roadmap milestone: parallel track (ai-tooling)
Dependencies: ai-platform-tools, governance-security, engineer-communications, mcp-and-tooling
Expected outputs: source-backed catalogue, skill specs, option papers, roadmap updates, and archive records for `docs/plans/agent-skills/`
Acceptance criteria: each skill is catalogued with governance class, dependencies, and lifecycle state; expert/legal outputs carry human-sign-off gates
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/agent-skills/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

This is the **agent-skills** broad workspace (parallel track). It owns portable skill specs + the prompt/version/eval/release lifecycle + portable skill contracts across approved AI front ends. Skills are content, not orchestration or hosting. See `docs/plans/_groups.md`.

## This Iteration - Consolidated Skill Catalogue

Approved design: `docs/superpowers/specs/2026-05-29-agent-skills-design.md`. Decisions (2026-05-29): deliver the portable catalogue + lifecycle, consolidate the first-wave skills into coherent runnable units, standardise on the `SKILL.md` portable contract, and keep expert/legal outputs behind human sign-off.

Deliverables: this plan, `context.md`, `skill-catalogue.md`, `open-questions.md`, and `option-papers/skill-lifecycle-and-portable-contract.md`.

## First-Wave Skills

Current first wave: `vehicle-valuation`, `damage-estimating`, `salvage-categorisation`, `rebuttal`, `roadworthy`, `finance-document`, `ce-house-style`, plus reference skills `abp-rates`, `manufacturer-standards`, and `ce-domain-glossary`. Planned future `case-status` will cover `case-summary`, `missing-info`, and `chaser-draft` after canonical work-item data is available. Full table in `skill-catalogue.md`.

## Sequential Plan

### Now (parallel with parser/bridge)
- [x] Write the consolidated catalogue and lifecycle/portable-contract option paper.
- [x] Define `ce-house-style` with visual-layout and writing-tone modes and point document skills at it.
- [x] Consolidate damage estimating into one runnable skill with repair-estimate, eva-total-loss, paint-costing, and charge-review modes.
- [x] Consolidate fee note and invoice drafting into `finance-document`.

### Next
- [ ] Formalise the first-wave skills under the lifecycle, coordinated with `ai-platform-tools` (eval) and `mcp-and-tooling` (tools).

### Reference-data skills (2026-05-29 — done)
- [x] Drained the former infointake staging material into shared references (`abp-rates`, `manufacturer-standards`, `ce-domain-glossary`) and consolidated runnable skills (`damage-estimating`, `salvage-categorisation`, `finance-document`).
- [x] Committed the worked-case corpus to `docs/reference/case-corpus/` (governed; PII) and pointed each skill's `references/examples.md` at it.
- [ ] Source UK OEM equivalents (`option-papers/oem-standards-uk-applicability.md`); add render scripts for `damage-estimating`/`finance-document`; bring the new skills under the lifecycle.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `ai-platform-tools` | Prompt/version governance, eval datasets, redaction, run logging — the lifecycle substrate skills consume. |
| `governance-security` | Expert-boundary policy, privacy/redaction, autonomous-action gates. |
| `intelligence/comms` (engineer-communications) | Where the drafting/communication skills are used; source ownership. |
| `mcp-and-tooling` | Skills call approved tools (Autotrader Codex connector, DVSA-MOT MCP) via the gateway. |

## Non-Overlap Rules

Does not own: workflow orchestration (`ai-platform/agents`); model hosting / global AI run logging; the business workflow where a skill is used. Personal injury and KADOE remain out of scope.

## Promotion Gates

- Expert/legal-output skills (valuation, rebuttal, roadworthy) require mandatory human sign-off, "AI-assisted draft" status until signed, and no autonomous external send.
- `option-papers/` before any vendor/RAG-corpus/commercial-data decision.
- Coordinate `ai-platform/platform-tools` before relying on evaluation/versioning infrastructure that does not yet exist.
