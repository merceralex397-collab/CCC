# Option Paper: Prompt/Version + Evaluation + Redaction Substrate

Status: open (design — not approved for build)
Owner: unassigned
Created: 2026-05-29
Group: ai-platform / platform-tools (G4)
Source links: `docs/superpowers/specs/2026-05-29-ai-platform-design.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md`, `docs/plans/agent-skills/option-papers/skill-lifecycle-and-portable-contract.md`

## Context

This substrate is what the `agent-skills` lifecycle and any AI-assisted module depend on: versioned prompts, evaluation, redaction, and run logging. The agent-skills interview flagged that its lifecycle needs this.

## Components To Design

1. **Prompt/version governance + run logging:** versioned prompts/schemas per skill/module; AI runs logged (input/output/model/version/actor) for audit + regression.
2. **Evaluation:** evaluation datasets + gold standards + reviewer corrections feeding back; regression alerts on prompt/model change.
3. **Redaction / training-data controls / AI policy:** PII redaction before external calls per the governance data map; controls on training/eval data use.

## Options For Timing

1. **Design only now**; agent-skills runs a minimal in-repo lifecycle (version + golden examples) until this is built.
2. **Build a minimal substrate now** (prompt/version registry + eval gold-standards) so agent-skills can run its full lifecycle immediately.
3. **Full substrate** (eval harness + run-log store + redaction service) — heaviest.

## Decision Criteria

What the agent-skills lifecycle minimally needs; audit/regression value; redaction obligations (governance data map); build effort; overlap with `operations-quality` regression tooling.

## Governance Gates

Redaction-before-external-call per policy; run-log retention + access (governance + operations).

## Open Questions

Minimal viable substrate vs full; where run logs live + retention; how eval gold-standards are authored/owned for expert-class skills.
