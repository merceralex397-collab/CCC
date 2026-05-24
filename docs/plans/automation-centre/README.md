# Automation Centre Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md`, `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`, `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, operations-quality, governance-security, mcp-and-tooling
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/automation-centre/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/automation-centre/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Deterministic automation architecture, operating cadence, and reusable workflow patterns.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- automation-vs-agent decision framework
- workflow triggers, queues, retries, idempotency, and exception routing
- automation operating model and KPIs
- shared automation service boundaries

## Does Not Own

- domain adapters such as Outlook, Box, EVA, finance, or portal implementations
- AI agent orchestration
- MCP tool schemas and gateway controls

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md` | Initial automation phase source. |
| `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md` | Reusable automation-centre operating model. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md` | Boundary between automation, draft-only skills, and agents. |
| `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md` | Workflow states, retries, and orchestration evidence. |

## Cross-Workspace Dependencies

- case-workflow-state
- operations-quality
- governance-security
- mcp-and-tooling

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
