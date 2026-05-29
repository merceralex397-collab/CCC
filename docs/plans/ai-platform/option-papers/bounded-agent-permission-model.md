# Option Paper: Bounded-Agent Permission Model + Agent-vs-Automation Framework

Status: open (design — not approved for build)
Owner: unassigned
Created: 2026-05-29
Group: ai-platform / agents (G4)
Source links: `docs/superpowers/specs/2026-05-29-ai-platform-design.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`, `docs/architecture/governance_security.md`

## Context

The reviewed source corrects the original plan: most "agents" are really automation, tools, dashboards, or drafts. So CCC agents are **bounded, read-only/draft-only, human-approval-gated**, call only approved tools (`mcp-tooling`) and skills (`agent-skills`), and are fully audited.

## Agent-vs-Automation Framework

A decision rule for each need: is it **deterministic automation** (`casework/automation`), a **tool** (`mcp-tooling`), a **skill/draft** (`agent-skills`), or a **bounded agent**? Default away from free-running agents; prefer the most deterministic option that meets the need. This framework is shared with `casework/automation` — keep one canonical version.

## Permission Model To Design

- Permission levels: what an agent may read vs draft vs (never) send/write externally.
- Escalation + human-approval gates for any consequential action.
- Tool/skill allow-lists per agent (enforced by the `mcp-tooling` gateway).
- Full audit of agent actions; continuous-learning agents are recommendation-only and cannot self-modify production behaviour.

## Candidate Agents (later, draft/read-only pilots)

Inbox triage, missing-info, valuation/uplift support, engineer support, continuous-learning — all bounded and gated; piloted only after tools + skills + audit + substrate exist (S4-S5).

## Decision Criteria

Safety/auditability; default-to-deterministic; clear permission levels mapped to the CE role model; enforceability via the gateway; human-approval boundaries.

## Governance Gates

No autonomous external action; human approval for consequential steps; audit of all agent runs; governance sign-off before any pilot.

## Open Questions

CE role model the permissions map to (depends on `casework`); which candidate agent pilots first; where the canonical agent-vs-automation framework lives.
