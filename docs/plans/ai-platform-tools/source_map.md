# AI Platform Tools Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/10_ai_modules_and_prompts.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: governance-security, operations-quality, agent-skills, parser-extraction
Expected outputs: source-to-plan traceability for `docs/plans/ai-platform-tools/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/ai-platform-tools/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md` | Model hosting, data collection, and evaluation/feedback-loop source. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md` | Model evaluation and feedback loop plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md` | PII redaction, audit, and governance tool plan. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/10_ai_modules_and_prompts.md` | AI modules and prompt-pattern evidence. |

## Ownership Boundary

Primary ownership:

- model/provider selection and hosting option papers
- prompt/version governance and AI run logging
- evaluation datasets, gold standards, reviewer corrections, and regression alerts
- redaction/training-data controls and AI policy implementation

Explicit exclusions:

- portable skill content
- workflow agents
- MCP tool gateway

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
