# Agent Skills Workspace — Context (Information Document)

Date: 2026-05-29
Status: active context document
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: agent-skills (parallel track, layer: ai-tooling) — see `docs/plans/_groups.md`
Source links: `docs/plans/agent-skills/plan.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/22_knowledge_base_report_clause_rag_skill.md`, `../collisionplugin/skills/valuation/vehicle-valuation/SKILL.md`, `../collisionplugin/rebuttal/projecttext.md`, `../collisionplugin/roadworthy/`, `../collisionplugin/skills/valuation/totalloss/`
Purpose: consolidate what is known about CCC's skill layer so the interview can focus on the portable skill catalogue + lifecycle and how to adopt the skills that already exist in `collisionplugin`.

## What this workspace owns

Portable, reusable staff/engineer **skill specs** (case summary, missing-info, CE style, valuation explanation, report-clause RAG, AI literacy, provider mapping); the skill **prompt/version/evaluation/release lifecycle**; and **portable skill contracts** usable across the CE platform, approved agents, ChatGPT, Claude Desktop, or other approved AI front ends.

It does **not** own: workflow orchestration (`ai-platform/agents`); model hosting / global AI run logging (`ai-platform/platform-tools`); the business workflow where a skill is used (e.g. `intelligence/comms`); MCP tool exposure (`mcp-tooling`). Skills are **content**, not infrastructure.

## Current state — skills migrated into src/skills/ (2026-05-29)

Migrated from `../collisionplugin` into `src/skills/` (see `collisionplugin-migration.md`). The production / near-production skills:

| Skill | What it is | Output | Maturity | Notes |
| --- | --- | --- | --- | --- |
| **vehicle-valuation** | Full Claude `SKILL.md`: extract vehicle (incl. EVA screenshot vision), Autotrader live-advert search, evidence selection, Jinja2/Python PDF render | Valuation report PDF + evidence pack PDF | Production-ready | Depends on the Autotrader Codex connector + DVSA-MOT MCP (`mcp-tooling`); strict external-wording rules; `guide_supported` vs `market_only` modes |
| **rebuttal** | Diminution-in-value expert rebuttal (CPR Part 35), 13-argument framework, CE house style | `.docx` rebuttal report | Near-production | Goes to instructing solicitors → expert/legal output; needs human sign-off |
| **roadworthy** | HS roadworthy certificate from an engineer's report, 14-field docx fill | `.docx` certificate | Near-production | "Do not ask clarifying questions; use fallbacks" |
| **total-loss** | Audatex/EVA damage-assessment PDF generator with EVA routing rules | EVA-compatible PDF | Code-complete | Relates to `intelligence/evidence` + `bridge/eva` |
| **CE style/tone** | Communication style & tone profile | Reference profile | Reference | Underpins all drafting skills |

Planned (from reference plans, not built): case-summary/status, missing-info, valuation-explanation, report-clause RAG, AI literacy, provider-mapping.

## Portability theme

`collisionplugin` skills use the **Claude Code `SKILL.md` format** (frontmatter `name`/`description` + body + `references/`/`scripts/`/`assets/`). The workspace goal is **portable skill contracts** reusable across approved AI front ends — so the catalogue needs one skill-contract format that maps to Claude / Claude Desktop / ChatGPT-Codex, plus the prompt/version/eval/release lifecycle (coordinated with `ai-platform/platform-tools`).

## Expert-boundary governance (firm)

Several skills produce **expert or legal documents** (valuation reports, diminution rebuttals, roadworthy certificates). CCC's expert-boundary policy is that AI **assists drafting**; named humans retain expert judgement and final approval. So every expert-output skill needs: a mandatory human-review/sign-off gate, an "AI-assisted draft" status until signed, no autonomous external send, and source-cited / no-source-refusal behaviour for RAG. Coordinate `governance-security` and `intelligence/comms`.

## Dependencies

`ai-platform/platform-tools` (prompt/version governance, eval datasets, redaction, run logging); `governance-security` (expert-boundary, privacy/redaction, autonomous-action gates); `intelligence/comms` (engineer pack / communications where skills are used); `mcp-tooling` (skills call approved tools — Autotrader, DVSA).

## Guardrails

Skills are portable content, separate from orchestration and hosting. No autonomous external send. Expert/legal outputs require human sign-off. Personal injury and KADOE remain out of scope.

## Open design questions for the interview

1. Focus this iteration: define the catalogue + lifecycle and adopt the collisionplugin skills, build new skills, or inventory-only?
2. Skill-contract format: standardise on `SKILL.md` as the portable contract, define a vendor-neutral spec, or defer?
3. Which skills to formalise first (collisionplugin production skills vs reference operational skills)?
