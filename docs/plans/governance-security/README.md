# Governance Security Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/architecture/governance_security.md`, `docs/security/dpia_vendor_governance.md`, `docs/security/vendor_register.md`, `docs/security/api_security_standard.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/12_compliance_governance_and_risk.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: all workspaces
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/governance-security/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/governance-security/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Cross-programme governance, security, privacy, vendor, licensing, audit, and expert-boundary planning.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- DPIA/vendor governance tickets and risk acceptance
- data map, retention, redaction, access review, and audit policy backlog
- expert-evidence boundary and risk-language policy
- public/commercial data licensing controls and API security standards

## Does Not Own

- all domain implementation of controls
- operations runbooks except governance incident requirements
- MCP gateway implementation details

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/architecture/governance_security.md` | Canonical governance and security architecture. |
| `docs/security/dpia_vendor_governance.md` | DPIA and vendor governance checklist. |
| `docs/security/vendor_register.md` | Current vendor register. |
| `docs/security/api_security_standard.md` | API security standard. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/12_compliance_governance_and_risk.md` | Expert evidence and AI governance risk source. |

## Cross-Workspace Dependencies

- all workspaces

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
