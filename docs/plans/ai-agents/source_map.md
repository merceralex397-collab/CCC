# AI Agents Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_ai_agents.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`, `docs/architecture/governance_security.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: mcp-and-tooling, agent-skills, automation-centre, governance-security, ai-platform-tools
Expected outputs: source-to-plan traceability for `docs/plans/ai-agents/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/ai-agents/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_ai_agents.md` | Original AI agents phase source. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md` | Reviewed correction that most features are automation, tools, dashboards, or drafts rather than free-running agents. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md` | Agent-vs-automation decision framework. |
| `docs/architecture/governance_security.md` | Human approval and governance guardrails. |

## Ownership Boundary

Primary ownership:

- inbox triage, missing-information, valuation/uplift, engineer support, and continuous-learning agent plans
- agent permission levels, escalation, and approval boundaries
- agent-vs-automation decision framework

Explicit exclusions:

- deterministic automation engine
- MCP tool implementation
- portable skill prompt specs
- model hosting and evaluation substrate

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
