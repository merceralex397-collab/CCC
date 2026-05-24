# AI Agents Workspace

## Purpose

This workspace owns all planning for controlled workflow agents, agent-vs-automation boundary decisions, and the governance framework for any agentic capability in the CCC platform.

## Scope Rules

- All AI agent implementations start as option papers in this workspace before promotion to tickets.
- Autonomous external actions (email, WhatsApp, EVA submission) require separate governance approval — they are never automatic.
- Personal injury and KADOE are out of scope.
- Agent decisions must be reviewable and auditable.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_ai_agents.md` | AI agents phase plan. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/` | Phase 4 controlled workflow agents and agent boundary. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/` | CE extraction service and AI tool plans — identifies agent vs. deterministic boundaries. |

## Workspace Layout

- `README.md` — this file
- `tickets/` — active tickets (only after option-paper approval)
- `option-papers/` — agent boundary proposals and governance reviews
- `archived_plans/` — implemented and superseded plans
