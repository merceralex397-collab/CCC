# AI Platform Plan (group home)

Date: 2026-05-29
Status: active workspace plan
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: ai-platform
Wave: G4
Layer: ai-tooling
Source links: `docs/plans/ai-platform/context.md`, `docs/superpowers/specs/2026-05-29-ai-platform-design.md`, `docs/plans/ai-agents/plan.md`, `docs/plans/ai-platform-tools/plan.md`, `docs/architecture/governance_security.md`
Roadmap milestone: G4 ai-platform
Dependencies: governance-security, operations-quality, agent-skills, mcp-and-tooling, case-workflow-state, parser-extraction
Expected outputs: substrate + bounded-agent designs, model/hosting option papers, and a sequenced build plan for `docs/plans/ai-platform/`
Acceptance criteria: each promoted item cites source evidence, names dependencies, defaults away from free-running agents, and carries governance gates
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/ai-platform/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

This is the **ai-platform** broad-workspace group home. Sub-areas (current folders pending the deferred move): `agents` ← `ai-agents/`, `platform-tools` ← `ai-platform-tools/`. See `docs/plans/_groups.md`.

## This Iteration — Design + Option-Papers (build deferred)

Approved design: `docs/superpowers/specs/2026-05-29-ai-platform-design.md`. Decisions (2026-05-29): design both sub-areas in parallel; build deferred; model strategy is two-track (multi-provider front ends now + self-hosting evaluation); agents are bounded, human-gated, read-only/draft-only.

| Sub-area | This iteration |
| --- | --- |
| `platform-tools` | Substrate design: prompt/version governance + run logging; eval datasets/gold-standards/corrections/regression; redaction/training-data/AI-policy. The substrate `agent-skills` lifecycle depends on. |
| `agents` | Bounded-agent permission/escalation/approval model + the agent-vs-automation framework; candidate agents are later draft/read-only pilots. |

Option-papers (group home `option-papers/`): model/provider + hosting; prompt/version/eval/redaction substrate; bounded-agent permission model.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `governance-security` | Model/vendor/privacy/redaction/AI-policy + autonomous-action gates. |
| `operations-quality` | Release/regression for AI-assisted modules. |
| `agent-skills` | Consumes the lifecycle substrate; agents call skills. |
| `mcp-tooling` | Agents call only gateway-approved tools. |
| `casework/automation` | Deterministic engine vs agents — the agent-vs-automation framework decides; keep one canonical version. |
| `parser` | Deterministic-first; AI assists, never replaces deterministic extraction. |

## Non-Overlap Rules

Does not own: deterministic automation engine (`casework/automation`); MCP gateway (`mcp-tooling`); portable skill content (`agent-skills`). Personal injury and KADOE remain out of scope.

## Promotion Gates

- `option-papers/` for model/hosting, the substrate, and the agent permission model before any build.
- Prompt/version governance + eval + redaction before any AI-assisted module expands.
- Agents are bounded, audited, human-approval-gated; no autonomous external actions; continuous-learning is recommendation-only.
