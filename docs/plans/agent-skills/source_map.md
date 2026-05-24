# Agent Skills Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/README.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/22_knowledge_base_report_clause_rag_skill.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: ai-platform-tools, governance-security, engineer-communications, mcp-and-tooling
Expected outputs: source-to-plan traceability for `docs/plans/agent-skills/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/agent-skills/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md` | Natural-language skills for staff and engineers. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/README.md` | AI tools, MCPs, and skills plan index. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md` | Case summary/status skill plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md` | CE communication style skill plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/22_knowledge_base_report_clause_rag_skill.md` | Knowledge-base/report-clause RAG skill plan. |

## Ownership Boundary

Primary ownership:

- case summary, missing-info, CE style, valuation explanation, report-clause RAG, AI literacy, and provider mapping skill specs
- skill prompt/version/evaluation/release lifecycle
- portable skill contracts for CE platform, agents, ChatGPT, Claude Desktop, or other approved AI front ends

Explicit exclusions:

- workflow orchestration
- model hosting or global AI run logging
- business workflow ownership where the skill is used

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
