# Agent Skills Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/README.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/22_knowledge_base_report_clause_rag_skill.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: ai-platform-tools, governance-security, engineer-communications, mcp-and-tooling
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/agent-skills/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/agent-skills/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Portable reusable staff/engineer skills with prompt/version/evaluation lifecycle and cross-AI portability.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- case summary, missing-info, CE style, valuation explanation, report-clause RAG, AI literacy, and provider mapping skill specs
- skill prompt/version/evaluation/release lifecycle
- portable skill contracts for CE platform, agents, ChatGPT, Claude Desktop, or other approved AI front ends

## Does Not Own

- workflow orchestration
- model hosting or global AI run logging
- business workflow ownership where the skill is used

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md` | Natural-language skills for staff and engineers. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/README.md` | AI tools, MCPs, and skills plan index. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md` | Case summary/status skill plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md` | CE communication style skill plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/22_knowledge_base_report_clause_rag_skill.md` | Knowledge-base/report-clause RAG skill plan. |

## Cross-Workspace Dependencies

- ai-platform-tools
- governance-security
- engineer-communications
- mcp-and-tooling

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
