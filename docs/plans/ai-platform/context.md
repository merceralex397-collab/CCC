# AI Platform Workspace — Context (Information Document)

Date: 2026-05-29
Status: active context document
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: ai-platform (G4, layer: ai-tooling) — see `docs/plans/_groups.md`
Source links: `docs/plans/ai-agents/plan.md`, `docs/plans/ai-platform-tools/plan.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md`, `docs/architecture/governance_security.md`

Group home for the ai-platform broad workspace. Sub-areas (current folders pending the deferred move): `agents` ← `docs/plans/ai-agents/`, `platform-tools` ← `docs/plans/ai-platform-tools/`.

## What this workspace owns

- **platform-tools** (the AI substrate): model/provider selection + hosting option-papers; prompt/version governance + AI run logging; evaluation datasets, gold standards, reviewer corrections, regression alerts; redaction/training-data controls + AI policy implementation.
- **agents**: bounded workflow agents (inbox triage, missing-info, valuation/uplift support, engineer support, continuous-learning) under a permission/escalation/approval model; the agent-vs-automation decision framework.

It does **not** own: the deterministic automation engine (`casework/automation`); MCP tool implementation/gateway (`mcp-tooling`); portable skill content (`agent-skills`).

## Key stance — conservative agents (firm)

The reviewed source material corrects the original plan: **most "agents" are really automation, tools, dashboards, or drafts**, not free-running agents. So agents here are **bounded, read-only or draft-only, human-approval-gated**, may only call **approved tools (`mcp-tooling`) and skills (`agent-skills`)**, and are fully audited. Continuous-learning agents remain recommendation-only and cannot self-modify production behaviour.

## platform-tools is the substrate others depend on

`agent-skills`' lifecycle (prompt/version/eval/release) and any AI-assisted module depend on platform-tools for prompt/version governance, evaluation datasets, redaction, and run logging. The agent-skills interview already flagged that its lifecycle needs this substrate. So platform-tools is the more foundational sub-area; agents come only after tools + skills + audit exist (S4-S5).

## Boundaries / dependencies

`governance-security` (model/vendor/privacy/redaction/AI-policy, autonomous-action gates); `operations-quality` (release/regression for AI modules); `agent-skills` (consumes the lifecycle substrate; agents call skills); `mcp-tooling` (agents call gated tools); `casework/automation` (deterministic engine vs agents — the framework decides which); `parser` (deterministic-first; AI assists, never replaces deterministic extraction).

## Current state

Nothing built; G4. The substrate underpins all AI-assisted behaviour; agents are deliberately late and bounded. Models in use today are accessed via approved front ends (Claude / Codex); no CCC self-hosting exists.

## Guardrails

AI assists reading/drafting/summarising/review; named humans keep expert judgement + final approvals. Prompt/version governance + eval + redaction before any AI-assisted module expands. No autonomous external actions. Personal injury and KADOE remain out of scope.

## Open design questions for the interview

1. Depth this iteration: design + option-papers (build deferred), or build a minimal substrate (prompt-versioning + eval gold-standards) now?
2. Priority: platform-tools (the substrate skills/agents need) or agents first?
3. Model/provider direction: multi-provider via approved front ends (Claude/Codex) with no self-hosting now, or evaluate self-hosting now?
