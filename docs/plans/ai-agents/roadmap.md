# AI Agents Roadmap

Date: 2026-05-24
Status: active workspace roadmap
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_ai_agents.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`, `docs/architecture/governance_security.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: mcp-and-tooling, agent-skills, automation-centre, governance-security, ai-platform-tools
Expected outputs: phased promotion sequence for `docs/plans/ai-agents/`
Acceptance criteria: roadmap stages cite source-backed workspace scope and do not duplicate another workspace's primary ownership
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/ai-agents/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## S3

- Define agent permission model only after tools, skills, and audit contracts exist.

## S4-S5

- Pilot read-only or draft-only agents for triage, missing-info, valuation support, and engineer support.

## S6

- Continuous-learning agents remain recommendation-only and cannot self-modify production behavior.

## Promotion Gate

Any item promoted from this roadmap must cite `source_map.md`, name dependencies, define acceptance criteria, and state whether governance/security or operations-quality approval is required.
