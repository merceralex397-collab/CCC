# Automation Centre Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md`, `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`, `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, operations-quality, governance-security, mcp-and-tooling
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/automation-centre/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/automation-centre/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/automation-centre/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md` | Initial automation phase source. |
| `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md` | Reusable automation-centre operating model. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md` | Boundary between automation, draft-only skills, and agents. |
| `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md` | Workflow states, retries, and orchestration evidence. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] automation-vs-agent decision framework | `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md`<br>`docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`<br>`docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md` | `case-workflow-state`, `operations-quality`, `governance-security`, `mcp-and-tooling` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] workflow triggers, queues, retries, idempotency, and exception routing | `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md`<br>`docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`<br>`docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md` | `case-workflow-state`, `operations-quality`, `governance-security`, `mcp-and-tooling` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] automation operating model and KPIs | `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md`<br>`docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`<br>`docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md` | `case-workflow-state`, `operations-quality`, `governance-security`, `mcp-and-tooling` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] shared automation service boundaries | `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md`<br>`docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`<br>`docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md` | `case-workflow-state`, `operations-quality`, `governance-security`, `mcp-and-tooling` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S1-S2

- [ ] Define event taxonomy and deterministic automation boundaries alongside work-item state.

### S3

- [ ] Plan intake/storage/EVA retry and exception patterns with runbook hooks.

### S4-S6

- [ ] Promote only measured, low-risk workflows from assisted mode toward controlled automation.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `case-workflow-state` | Work-item state, review status, blockers, audit events, and approvals are the operational source of truth. |
| `operations-quality` | Release, rollback, regression, monitoring, runbooks, pilot, support, and decommissioning gates must be explicit. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `mcp-and-tooling` | MCP/tool exposure must wrap approved adapters with schemas, auth, audit, rate limits, and gateway controls. |

## Non-Overlap Rules

The workspace explicitly does not own:

- domain adapters such as Outlook, Box, EVA, finance, or portal implementations
- AI agent orchestration
- MCP tool schemas and gateway controls

If a proposed ticket touches one of those exclusions, link to the owning workspace and keep this workspace as a supporting dependency only.

## Source Ownership Rules

- Cite the source paths above in every promoted ticket, option paper, or roadmap change.
- Use `source_map.md` to explain how the evidence supports the workspace boundary.
- Keep generated and historical planning packs reference-only until a scoped ticket or option paper promotes them.
- Do not edit raw evidence under `docs/reference/raw/collisionrelateddocs/`; create derivatives only under documented derivative paths.

## Promotion Gates

- Use `tickets/` for implementation-ready work with acceptance criteria and verification.
- Use `option-papers/` before vendor, privacy, external access, autonomous send, payment automation, AI/RAG, cloud OCR/document intelligence, commercial data, or partner/API work.
- Link governance/security approval where privacy, vendor, retention, licensing, expert-boundary, API security, or autonomous-action risk exists.
- Link operations-quality approval where release, rollback, regression, monitoring, runbook, support, pilot, or decommissioning evidence is needed.
