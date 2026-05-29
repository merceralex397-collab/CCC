# Option Paper: Skill Lifecycle + Portable Contract

Status: open (design — not approved for build)
Owner: unassigned
Created: 2026-05-29
Group: agent-skills (parallel track)
Source links: `docs/superpowers/specs/2026-05-29-agent-skills-design.md`, `docs/plans/agent-skills/skill-catalogue.md`, `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`

## Context

Skills need a consistent portable contract and a prompt/version/evaluation/release lifecycle so they can be governed and reused across AI front ends. The decision (2026-05-29) is to standardise on the Claude Code `SKILL.md` format; this paper evaluates how far to formalise the lifecycle now, given the evaluation substrate (`ai-platform/platform-tools`) is not yet built.

## Portable Contract — confirmed direction

`SKILL.md` (frontmatter `name`/`description`-trigger + body + `references/`/`scripts/`/`assets/`) is the canonical contract. Document the mapping: Claude / Claude Desktop (native), ChatGPT/Codex (system prompt + tool/connector bindings), CE platform (skill registry entry). Each skill declares tool dependencies and a governance class.

## Lifecycle Options

1. **Minimal-now lifecycle**: version field + golden examples + release state tracked *in the skill repo/catalogue* (no external eval tooling). Adopt collisionplugin skills immediately under this. Upgrade when `ai-platform/platform-tools` exists.
2. **Wait for the platform substrate**: defer formalisation until versioning/eval/redaction/run-logging infrastructure is built. Slower; risks the existing skills staying ungoverned.
3. **External eval harness now**: stand up evaluation datasets + regression now. Most rigorous; heavy, and overlaps `ai-platform/platform-tools` ownership.

## Decision Criteria

Time-to-govern the existing skills; overlap with `ai-platform/platform-tools` ownership; expert-boundary enforceability (sign-off gates); portability fidelity across front ends; effort.

## Governance Gates

Expert/legal-output skills require human sign-off + "AI-assisted draft" status + no autonomous send. RAG skills require source-citation + no-source refusal. Coordinate `governance-security` and `ai-platform/platform-tools`.

## Open Questions

Minimal viable lifecycle before the platform substrate exists; front-end mapping fidelity; eval ownership for expert-class skills.
