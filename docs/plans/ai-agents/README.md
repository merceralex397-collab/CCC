# AI Agents Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_ai_agents.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`, `docs/architecture/governance_security.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: mcp-and-tooling, agent-skills, automation-centre, governance-security, ai-platform-tools
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/ai-agents/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/ai-agents/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Bounded workflow agents that orchestrate approved tools and portable skills under permission and approval gates.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- inbox triage, missing-information, valuation/uplift, engineer support, and continuous-learning agent plans
- agent permission levels, escalation, and approval boundaries
- agent-vs-automation decision framework

## Does Not Own

- deterministic automation engine
- MCP tool implementation
- portable skill prompt specs
- model hosting and evaluation substrate

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_ai_agents.md` | Original AI agents phase source. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md` | Reviewed correction that most features are automation, tools, dashboards, or drafts rather than free-running agents. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md` | Agent-vs-automation decision framework. |
| `docs/architecture/governance_security.md` | Human approval and governance guardrails. |

## Cross-Workspace Dependencies

- mcp-and-tooling
- agent-skills
- automation-centre
- governance-security
- ai-platform-tools

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
