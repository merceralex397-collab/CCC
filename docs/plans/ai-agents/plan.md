# AI Agents Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_ai_agents.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`, `docs/architecture/governance_security.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: mcp-and-tooling, agent-skills, automation-centre, governance-security, ai-platform-tools
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/ai-agents/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/ai-agents/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/ai-agents/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_ai_agents.md` | Original AI agents phase source. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md` | Reviewed correction that most features are automation, tools, dashboards, or drafts rather than free-running agents. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md` | Agent-vs-automation decision framework. |
| `docs/architecture/governance_security.md` | Human approval and governance guardrails. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] inbox triage, missing-information, valuation/uplift, engineer support, and continuous-learning agent plans | `docs/reference/originalplanning/originalplans_output/phase_ai_agents.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`<br>`docs/architecture/governance_security.md` | `mcp-and-tooling`, `agent-skills`, `automation-centre`, `governance-security`, `ai-platform-tools` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] agent permission levels, escalation, and approval boundaries | `docs/reference/originalplanning/originalplans_output/phase_ai_agents.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`<br>`docs/architecture/governance_security.md` | `mcp-and-tooling`, `agent-skills`, `automation-centre`, `governance-security`, `ai-platform-tools` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] agent-vs-automation decision framework | `docs/reference/originalplanning/originalplans_output/phase_ai_agents.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md`<br>`docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`<br>`docs/architecture/governance_security.md` | `mcp-and-tooling`, `agent-skills`, `automation-centre`, `governance-security`, `ai-platform-tools` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S3

- [ ] Define agent permission model only after tools, skills, and audit contracts exist.

### S4-S5

- [ ] Pilot read-only or draft-only agents for triage, missing-info, valuation support, and engineer support.

### S6

- [ ] Continuous-learning agents remain recommendation-only and cannot self-modify production behavior.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `mcp-and-tooling` | MCP/tool exposure must wrap approved adapters with schemas, auth, audit, rate limits, and gateway controls. |
| `agent-skills` | Portable skills must stay separate from runtime orchestration and cite approved skill prompts/evaluation examples. |
| `automation-centre` | Deterministic automation owns triggers, retries, idempotency, queues, and exception routing used by domain workflows. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `ai-platform-tools` | AI-assisted behavior needs model/prompt governance, evaluation data, redaction, and run logging before expansion. |

## Non-Overlap Rules

The workspace explicitly does not own:

- deterministic automation engine
- MCP tool implementation
- portable skill prompt specs
- model hosting and evaluation substrate

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
