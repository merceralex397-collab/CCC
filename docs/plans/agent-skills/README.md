# Agent Skills Workspace

## Purpose

This workspace owns all planning for reusable natural-language skills: drafting, summarisation, RAG retrieval, valuation support, communication, and training skills. Skills must be modular and portable across the CE platform, direct workflow agents, ChatGPT, Claude Desktop, or other approved front ends.

## Scope Rules

- Skills must be designed as modular prompts or configs — no skills may be tightly coupled to a single runtime.
- Skills must enforce CE style and expert-boundary rules — no skills may assert uplift, produce autonomous decisions, or bypass review.
- Personal injury and KADOE are out of scope.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md` | CE style communications skill design. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/15_missing_info_checker_and_chaser_drafter.md` | Missing info checker and chaser drafter skill. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/` | Full CE AI tools plans covering drafting, RAG, valuation, and comms skills. |

## Workspace Layout

- `README.md` — this file
- `tickets/` — active tickets
- `option-papers/` — skill portability and runtime proposals
- `archived_plans/` — implemented and superseded plans
