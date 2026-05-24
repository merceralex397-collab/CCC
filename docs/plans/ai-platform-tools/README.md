# AI Platform Tools Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/10_ai_modules_and_prompts.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: governance-security, operations-quality, agent-skills, parser-extraction
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/ai-platform-tools/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/ai-platform-tools/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Shared AI substrate behind tools, skills, and agents.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- model/provider selection and hosting option papers
- prompt/version governance and AI run logging
- evaluation datasets, gold standards, reviewer corrections, and regression alerts
- redaction/training-data controls and AI policy implementation

## Does Not Own

- portable skill content
- workflow agents
- MCP tool gateway

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md` | Model hosting, data collection, and evaluation/feedback-loop source. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md` | Model evaluation and feedback loop plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md` | PII redaction, audit, and governance tool plan. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/10_ai_modules_and_prompts.md` | AI modules and prompt-pattern evidence. |

## Cross-Workspace Dependencies

- governance-security
- operations-quality
- agent-skills
- parser-extraction

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
