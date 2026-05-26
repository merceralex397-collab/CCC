# Automation Centre Roadmap

Date: 2026-05-24
Status: active workspace roadmap
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_initial_automation.md`, `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`, `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, operations-quality, governance-security, mcp-and-tooling
Expected outputs: phased promotion sequence for `docs/plans/automation-centre/`
Acceptance criteria: roadmap stages cite source-backed workspace scope and do not duplicate another workspace's primary ownership
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/automation-centre/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## S1-S2

- Define event taxonomy and deterministic automation boundaries alongside work-item state.

## S3

- Plan intake/storage/EVA retry and exception patterns with runbook hooks.

## S4-S6

- Promote only measured, low-risk workflows from assisted mode toward controlled automation.

## Promotion Gate

Any item promoted from this roadmap must cite `source_map.md`, name dependencies, define acceptance criteria, and state whether governance/security or operations-quality approval is required.
