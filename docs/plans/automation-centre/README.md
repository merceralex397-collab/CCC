# Automation Centre Workspace

## Purpose

This workspace owns all planning for deterministic automation models, workflow automation rules, retry logic, exception routing, automation KPIs, and the boundary between deterministic automation and AI agents.

## Scope Rules

- Automation here is deterministic and rule-based — AI agents are planned in `docs/plans/ai-agents/`.
- Autonomous email sending, WhatsApp sends, and EVA submission are out of scope until separately approved via governance option paper.
- Personal injury and KADOE are out of scope.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md` | Initial automation phase plan. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/` | Phase 4 agents reviewed plan — automation boundary and controlled workflow agents. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/` | Phase 7 automation and exception routing requirements. |

## Workspace Layout

- `README.md` — this file
- `tickets/` — active tickets
- `option-papers/` — automation boundary and governance proposals
- `archived_plans/` — implemented and superseded plans
