# CE Role Model

Date: 2026-05-29
Status: DRAFT — requires governance sign-off
Owner: unassigned
Source links: `docs/contracts/review_audit_event_contract_v1.md`, `docs/contracts/work_item_contract_v1.md`, `docs/architecture/governance_security.md`, `docs/superpowers/specs/2026-05-29-casework-design.md`, `docs/superpowers/specs/2026-05-29-ai-platform-design.md`

## Purpose

A single role model the whole programme references: `casework` review/override roles, `ai-platform` agent permissions, `finance` approval, and `agent-skills`/`intelligence` expert sign-off all depend on it. Least privilege by default; every consequential action is audited (per the review/audit contract).

## Human Roles

| Role | May do | Must not do (without escalation) |
| --- | --- | --- |
| **Office staff / operator** | Create/open work items, upload files, run parser triage, review and correct extracted fields, set image order, prepare packages. | Override critical warnings; activate provider config; approve fee notes; sign off expert conclusions. |
| **Reviewer** | All operator actions, plus resolve/override warnings (critical overrides require reviewer role + recorded reason) and approve a work item for export/package. | Provider activation/rollback; expert technical sign-off; finance approval. |
| **Provider admin** | Create/activate/roll back provider & principal config (requires provider-admin role + source-linked reason). | Expert sign-off; finance approval. |
| **Engineer (expert)** | Expert sign-off on technical conclusions, valuations, roadworthiness, causation, and final reports (the expert-boundary). | n/a — this is the human-judgement gate. |
| **Finance approver** | Approve fee notes / invoices; manage fee rules. | Expert sign-off; provider activation. |
| **System admin** | Manage local accounts, integration config, secrets (least privilege; secrets never exposed to agents/models). | Bypass audit; act as reviewer/engineer for sign-off. |

## Non-Human (Agent/Tool) Roles

| Principal | Permission ceiling |
| --- | --- |
| **Bounded agent** (`ai-platform/agents`) | Read-only or draft-only; calls only gateway-approved tools (`mcp-tooling`) and skills (`agent-skills`); every action audited; consequential actions require a named human's approval. No autonomous external send/write. |
| **Skill** (`agent-skills`) | Produces drafts/aids only; expert/legal-output skills produce an "AI-assisted draft" until a named human signs off. |
| **Tool/MCP** (`mcp-tooling`) | Scoped, schema-validated, rate-limited, audited; secrets injected server-side, never returned. |

## Mapping To Workspaces

- `casework`: operator, reviewer, provider-admin enforce the work-item lifecycle gates + append-only audit.
- `ai-platform`: bounded-agent permission levels derive from this model.
- `finance`: finance-approver gate on fee notes/invoices.
- `agent-skills` / `intelligence`: engineer (expert) sign-off on valuation/rebuttal/roadworthy/report outputs.

## Open Items For Sign-Off

Exact CE job titles → roles mapping; whether reviewer and engineer are distinct people; separation-of-duties rules (e.g. cannot approve own correction); how roles are enforced across the Python tools + the WinUI casework app + the tool gateway.
