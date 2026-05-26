# Automation Centre Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md`, `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`, `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, operations-quality, governance-security, mcp-and-tooling
Expected outputs: source-to-plan traceability for `docs/plans/automation-centre/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/automation-centre/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md` | Initial automation phase source. |
| `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md` | Reusable automation-centre operating model. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md` | Boundary between automation, draft-only skills, and agents. |
| `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md` | Workflow states, retries, and orchestration evidence. |

## Ownership Boundary

Primary ownership:

- automation-vs-agent decision framework
- workflow triggers, queues, retries, idempotency, and exception routing
- automation operating model and KPIs
- shared automation service boundaries

Explicit exclusions:

- domain adapters such as Outlook, Box, EVA, finance, or portal implementations
- AI agent orchestration
- MCP tool schemas and gateway controls

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
