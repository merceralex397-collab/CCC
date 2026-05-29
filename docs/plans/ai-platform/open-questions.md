# AI Platform Workspace — Open Questions

Date: 2026-05-29
Status: active open-questions log
Owner: unassigned
Group: ai-platform (G4)
Source links: `docs/superpowers/specs/2026-05-29-ai-platform-design.md`, `docs/plans/ai-platform/plan.md`, `docs/plans/ai-platform/context.md`

## Resolved (this interview, 2026-05-29)

- **Depth?** — Design both sub-areas + option-papers; build deferred.
- **Priority?** — Design `platform-tools` and `agents` in parallel.
- **Model strategy?** — Two-track: multi-provider via approved front ends (Claude/Codex) now, no self-hosting, **and** a self-hosting evaluation option-paper.
- **Agents?** — Bounded, read-only/draft-only, human-approval-gated, audited; continuous-learning recommendation-only (firm).

## Open

1. **Minimal substrate for agent-skills** — what is the least platform-tools capability the agent-skills lifecycle needs before it can fully run (prompt/version registry? eval gold-standards?), and is design-only enough short-term?
2. **Self-hosting evaluation scope** — keep it an evaluation (data residency/cost/control), not a commitment; what would trigger building it.
3. **Redaction-before-external-call** — depends on the governance data map; which fields must be redacted before any external model call.
4. **One canonical agent-vs-automation framework** — shared with `casework/automation`; where it lives and who maintains it.
5. **AI run-logging store** — where AI run logs live and their retention (coordinate governance + operations).
