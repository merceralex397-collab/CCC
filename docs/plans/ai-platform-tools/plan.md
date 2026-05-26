# AI Platform Tools Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/10_ai_modules_and_prompts.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: governance-security, operations-quality, agent-skills, parser-extraction
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/ai-platform-tools/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/ai-platform-tools/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/ai-platform-tools/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md` | Model hosting, data collection, and evaluation/feedback-loop source. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md` | Model evaluation and feedback loop plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md` | PII redaction, audit, and governance tool plan. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/10_ai_modules_and_prompts.md` | AI modules and prompt-pattern evidence. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] model/provider selection and hosting option papers | `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/10_ai_modules_and_prompts.md` | `governance-security`, `operations-quality`, `agent-skills`, `parser-extraction` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] prompt/version governance and AI run logging | `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/10_ai_modules_and_prompts.md` | `governance-security`, `operations-quality`, `agent-skills`, `parser-extraction` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] evaluation datasets, gold standards, reviewer corrections, and regression alerts | `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/10_ai_modules_and_prompts.md` | `governance-security`, `operations-quality`, `agent-skills`, `parser-extraction` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] redaction/training-data controls and AI policy implementation | `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/10_ai_modules_and_prompts.md` | `governance-security`, `operations-quality`, `agent-skills`, `parser-extraction` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S2

- [ ] Version prompts and schemas for any AI-assisted module before release.

### S4

- [ ] Build evaluation datasets, correction feedback loops, and redaction controls.

### S5-S6

- [ ] Support model hosting and training/evaluation only after governance approval and source minimisation.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `operations-quality` | Release, rollback, regression, monitoring, runbooks, pilot, support, and decommissioning gates must be explicit. |
| `agent-skills` | Portable skills must stay separate from runtime orchestration and cite approved skill prompts/evaluation examples. |
| `parser-extraction` | Extraction work must preserve CE Document Mapper behavior, deterministic rules, canonical schema, and regression coverage. |

## Non-Overlap Rules

The workspace explicitly does not own:

- portable skill content
- workflow agents
- MCP tool gateway

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
