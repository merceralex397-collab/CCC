# Agent Skills: Portable Catalogue + Lifecycle + collisionplugin Adoption — Design

Date: 2026-05-29
Status: approved design (brainstorming output)
Owner: unassigned
Workspace: `docs/plans/agent-skills/` (group: agent-skills, parallel track)
Source links: `docs/plans/agent-skills/context.md`, `docs/plans/agent-skills/skill-catalogue.md`, `../collisionplugin/skills/valuation/vehicle-valuation/SKILL.md`, `../collisionplugin/rebuttal/projecttext.md`, `../collisionplugin/roadworthy/`, `../collisionplugin/skills/valuation/totalloss/`, `../collisionplugin/assets/`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md`

## Context

agent-skills is a parallel track owning portable, reusable skill specs + their prompt/version/eval/release lifecycle, usable across approved AI front ends. `collisionplugin` already holds real skills (vehicle-valuation, rebuttal, roadworthy, total-loss, CE style); the job is to bring them under a governed, portable catalogue rather than build from scratch.

## Decisions captured (user, 2026-05-29)

- **Deliver:** the portable skill **catalogue + lifecycle**, and **adopt/formalise the collisionplugin skills** into it.
- **Contract format:** standardise on the **Claude Code `SKILL.md` format** as the portable contract; document how it maps to Claude Desktop and ChatGPT/Codex. No rewrite of existing skills.
- **First-wave skills:** vehicle-valuation; rebuttal; roadworthy; total-loss; CE style/tone; case-summary; missing-info; **plus a new CE branding skill (logo + design layout)** that the document-producing skills consume.
- **Firm guardrail:** expert/legal-output skills (valuation, rebuttal, roadworthy) require mandatory human sign-off, "AI-assisted draft" status until signed, no autonomous external send.

## Goals / Non-goals

**Goals:** a skill catalogue (`skill-catalogue.md`) with status/governance/dependencies; the `SKILL.md` portable-contract standard + front-end mapping; the prompt/version/eval/release lifecycle (coordinated with `ai-platform/platform-tools`); an adoption path for the collisionplugin skills; the new CE branding skill.

**Non-goals (this iteration):** workflow orchestration (`ai-platform/agents`); model hosting / run-logging substrate (`ai-platform/platform-tools` owns it; we consume it); MCP tool exposure (`mcp-tooling`); building every planned skill. Personal injury and KADOE remain out of scope.

## Design

### Portable skill contract (`SKILL.md`)

Adopt the Claude Code `SKILL.md` shape as the canonical portable contract: frontmatter (`name`, `description`/trigger), body (workflow), and `references/`, `scripts/`, `assets/`. Document the mapping to Claude Desktop and ChatGPT/Codex (where a skill becomes a system prompt + tool bindings). Skills declare their tool dependencies (e.g. valuation → Autotrader Codex connector + DVSA-MOT MCP via `mcp-tooling`) and their governance class.

### Skill lifecycle

Each catalogued skill carries: a version; golden input/output examples; an evaluation set (coordinated with `ai-platform/platform-tools`); a release state (`draft` / `in-review` / `released`); and source citations. RAG-type skills add source-citation + no-source-refusal rules.

### CE branding skill (new)

A shared `ce-branding` skill/asset module: CE logo (`svg`/`png`/`pdf`), the document layout templates (`report.html.j2`, `evidence_pack.html.j2`, `_base.html.j2`, `styles.css`), and `pdf-template-spec.md`/`brand.md`. The document-producing skills (valuation, rebuttal, roadworthy, total-loss, fee-note) reference it so house style/logo/layout are defined once. Source: `collisionplugin/assets/` + `…/vehicle-valuation/assets/templates/` + `…/references/brand.md`.

### Expert-boundary governance (firm)

Valuation reports, diminution rebuttals, and roadworthy certificates are expert/legal outputs. Each such skill: produces an **"AI-assisted draft"** until a named human signs off; **no autonomous external send**; preserves source evidence; uses the approved external-wording rules (the valuation skill already encodes these). Coordinate `governance-security` + `intelligence/comms`.

### Adoption path for collisionplugin skills

Catalogue each, record its governance class + tool/asset dependencies, repoint asset/script paths into the CCC layout, and bring it under the lifecycle. Do not change skill behaviour during adoption.

## Sequencing

1. Write the catalogue + the lifecycle/portable-contract option-paper (this iteration).
2. Define the CE branding skill and point the document skills at it.
3. Formalise the first-wave skills under the lifecycle (vehicle-valuation, rebuttal, roadworthy, total-loss, CE style, case-summary, missing-info) — coordinated with `ai-platform/platform-tools` (eval) and `mcp-tooling` (tools).

## Acceptance Criteria

- `skill-catalogue.md` lists each first-wave skill with source, output, governance class (human-signoff yes/no), tool/asset dependencies, and release state.
- The `SKILL.md` portable contract + front-end mapping is documented in the option-paper.
- The CE branding skill is defined with its asset/template sources and consuming skills.
- Every expert/legal-output skill records the mandatory human-sign-off gate and no-autonomous-send rule.

## Risks & Open Questions

- Lifecycle tooling (versioning, eval datasets, redaction, run logging) depends on `ai-platform/platform-tools`, which isn't built yet.
- `SKILL.md`→ChatGPT/Codex mapping fidelity (tool bindings differ per front end).
- Where skills physically live in CCC and how collisionplugin assets/scripts migrate (Phase-4 promotion).
- RAG report-clause skill needs an approved source corpus + licensing.
