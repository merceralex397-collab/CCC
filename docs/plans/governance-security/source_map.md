# Governance Security Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/architecture/governance_security.md`, `docs/security/dpia_vendor_governance.md`, `docs/security/vendor_register.md`, `docs/security/api_security_standard.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/12_compliance_governance_and_risk.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: all workspaces
Expected outputs: source-to-plan traceability for `docs/plans/governance-security/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/governance-security/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/architecture/governance_security.md` | Canonical governance and security architecture. |
| `docs/security/dpia_vendor_governance.md` | DPIA and vendor governance checklist. |
| `docs/security/vendor_register.md` | Current vendor register. |
| `docs/security/api_security_standard.md` | API security standard. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/12_compliance_governance_and_risk.md` | Expert evidence and AI governance risk source. |

## Ownership Boundary

Primary ownership:

- DPIA/vendor governance tickets and risk acceptance
- data map, retention, redaction, access review, and audit policy backlog
- expert-evidence boundary and risk-language policy
- public/commercial data licensing controls and API security standards

Explicit exclusions:

- all domain implementation of controls
- operations runbooks except governance incident requirements
- MCP gateway implementation details

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
