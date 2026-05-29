# Agent Skills Workspace — Open Questions

Date: 2026-05-29
Status: active open-questions log
Owner: unassigned
Group: agent-skills (parallel track)
Source links: `docs/superpowers/specs/2026-05-29-agent-skills-design.md`, `docs/plans/agent-skills/skill-catalogue.md`, `docs/plans/agent-skills/context.md`

## Resolved (this interview, 2026-05-29)

- **Focus?** — Define the portable catalogue + lifecycle and adopt the collisionplugin skills.
- **Contract format?** — Claude Code `SKILL.md` as the portable contract (map to Claude Desktop / ChatGPT-Codex).
- **First-wave skills?** — vehicle-valuation, rebuttal, roadworthy, total-loss, CE style, case-summary, missing-info, **plus a new `ce-branding` skill** (logo + document layout).
- **Expert-boundary?** — Firm: expert/legal outputs require human sign-off, "AI-assisted draft" until signed, no autonomous send.

## Open

1. Lifecycle substrate (`ai-platform/platform-tools`) — versioning, eval datasets, redaction, run logging — isn't built yet; what is the minimal viable lifecycle we can run before it exists?
2. `SKILL.md` → ChatGPT/Codex mapping fidelity (tool bindings + system-prompt translation per front end).
3. Where skills physically live in CCC and how collisionplugin assets/scripts migrate (Phase-4 promotion) — keep skills runnable during the move.
4. `ce-branding` scope: just logo + layout templates, or also tone (overlap with `ce-style`)? Confirm the boundary between `ce-branding` (visual) and `ce-style` (language).
5. Report-clause RAG: approved source corpus + licensing + no-source-refusal rules.
6. Evaluation/golden examples for expert-class skills — who reviews and signs off the eval criteria.
