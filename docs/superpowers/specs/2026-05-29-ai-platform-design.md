# AI Platform: Substrate (platform-tools) + Bounded Agents — Design

Date: 2026-05-29
Status: approved design (brainstorming output) — design + option-papers this iteration, build deferred
Owner: unassigned
Workspace: `docs/plans/ai-platform/` (group home; sub-areas in ai-agents / ai-platform-tools)
Source links: `docs/plans/ai-platform/context.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md`, `docs/architecture/governance_security.md`

## Context

ai-platform is the AI substrate (`platform-tools`) plus bounded workflow agents (`agents`). The substrate underpins the `agent-skills` lifecycle and any AI-assisted module; agents are deliberately late and bounded. G4 timing → this iteration is design + option-papers.

## Decisions captured (user, 2026-05-29)

- **Depth:** design both sub-areas + option-papers; build deferred.
- **Priority:** design `platform-tools` and `agents` **in parallel**.
- **Model strategy (two-track):** use **multi-provider via approved front ends** (Claude / Codex) now, no self-hosting, **and** open an option-paper to **evaluate self-hosting** (data residency, cost, control).
- **Firm:** agents are bounded, read-only/draft-only, human-approval-gated, call only approved tools + skills, fully audited; continuous-learning is recommendation-only.

## Goals / Non-goals

**Goals:** a substrate design (prompt/version governance, evaluation datasets/gold-standards/corrections/regression, redaction/training-data/AI-policy, AI run logging); the bounded-agent permission/escalation/approval model + agent-vs-automation framework; the model/provider + self-hosting option-papers.

**Non-goals (this iteration):** building the substrate or any agent; the deterministic automation engine (`casework/automation`); MCP gateway (`mcp-tooling`); skill content (`agent-skills`). Personal injury and KADOE remain out of scope.

## Design

### platform-tools (substrate)

- **Prompt/version governance + AI run logging:** every AI-assisted module/skill has versioned prompts/schemas and logged runs (inputs/outputs/model/version) for audit + regression. This is the substrate the `agent-skills` lifecycle consumes.
- **Evaluation:** evaluation datasets, gold standards, reviewer corrections feeding back, and regression alerts when a prompt/model change degrades quality.
- **Redaction / training-data controls / AI policy:** PII redaction before any external model call where required; controls on what may be used as training/eval data; the implementation of the governance AI policy.
- **Model strategy (two-track):** (a) standardise prompt/version/eval across **approved multi-provider front ends** (Claude/Codex) with no self-hosting now; (b) a parallel **self-hosting evaluation** option-paper (open/data-residency/cost/control).

### agents (bounded)

- **Permission/escalation/approval model:** what an agent may read/draft, what requires human approval, how it escalates; agents call only `mcp-tooling`-gated tools and `agent-skills` skills; fully audited.
- **agent-vs-automation framework:** the decision rule for whether a need is deterministic automation (`casework/automation`), a tool, a skill/draft, or a bounded agent — defaulting away from free-running agents.
- **Candidate agents** (later pilots, draft/read-only): inbox triage, missing-info, valuation/uplift support, engineer support, continuous-learning (recommendation-only).

## Sequencing

Design both in parallel now. Build order later: substrate (prompt/version + eval + redaction + run-logging) before any agent; agents pilot only after tools + skills + audit + the substrate exist (S4-S5).

## Option-Papers (this iteration)

1. `option-papers/model-provider-and-hosting.md` (multi-provider front ends now + self-hosting evaluation).
2. `option-papers/prompt-version-eval-redaction-substrate.md` (the substrate design/approach).
3. `option-papers/bounded-agent-permission-model.md` (permission model + agent-vs-automation framework).

## Risks & Open Questions

- The `agent-skills` lifecycle needs at least a minimal substrate before it can fully run — what minimum is required, and is design-only enough short-term?
- Self-hosting evaluation pulls hosting/ops/cost forward; scope it as evaluation, not commitment.
- Redaction-before-external-call requirements depend on the governance data map.
- Agent-vs-automation framework is shared with `casework/automation`; keep one canonical version.

## Acceptance Criteria

- Substrate design covers prompt/version governance, evaluation, redaction/AI-policy, and run logging.
- Bounded-agent permission model + agent-vs-automation framework documented, defaulting away from free-running agents.
- Model/provider + self-hosting option-papers exist with options, criteria, and governance gates.
