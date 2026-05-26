# Governance Security Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/architecture/governance_security.md`, `docs/security/dpia_vendor_governance.md`, `docs/security/vendor_register.md`, `docs/security/api_security_standard.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/12_compliance_governance_and_risk.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: all workspaces
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/governance-security/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/governance-security/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/governance-security/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/architecture/governance_security.md` | Canonical governance and security architecture. |
| `docs/security/dpia_vendor_governance.md` | DPIA and vendor governance checklist. |
| `docs/security/vendor_register.md` | Current vendor register. |
| `docs/security/api_security_standard.md` | API security standard. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/12_compliance_governance_and_risk.md` | Expert evidence and AI governance risk source. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] DPIA/vendor governance tickets and risk acceptance | `docs/architecture/governance_security.md`<br>`docs/security/dpia_vendor_governance.md`<br>`docs/security/vendor_register.md`<br>`docs/security/api_security_standard.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/12_compliance_governance_and_risk.md` | `all workspaces` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] data map, retention, redaction, access review, and audit policy backlog | `docs/architecture/governance_security.md`<br>`docs/security/dpia_vendor_governance.md`<br>`docs/security/vendor_register.md`<br>`docs/security/api_security_standard.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/12_compliance_governance_and_risk.md` | `all workspaces` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] expert-evidence boundary and risk-language policy | `docs/architecture/governance_security.md`<br>`docs/security/dpia_vendor_governance.md`<br>`docs/security/vendor_register.md`<br>`docs/security/api_security_standard.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/12_compliance_governance_and_risk.md` | `all workspaces` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] public/commercial data licensing controls and API security standards | `docs/architecture/governance_security.md`<br>`docs/security/dpia_vendor_governance.md`<br>`docs/security/vendor_register.md`<br>`docs/security/api_security_standard.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/12_compliance_governance_and_risk.md` | `all workspaces` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S0-S1

- [ ] Gate core architecture, data map, roles, audit, and no personal injury or KADOE scope.

### S2-S4

- [ ] Review cloud OCR, AI, Box/Graph/EVA, valuation, and redaction controls before activation.

### S5-S6

- [ ] Gate partner APIs, portals, analytics, warehouse, risk indicators, payment automation, and commercial data use.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `all workspaces` | Governance/security owns cross-programme risk, data, vendor, licensing, audit, and expert-boundary gates for every workspace. |

## Non-Overlap Rules

The workspace explicitly does not own:

- all domain implementation of controls
- operations runbooks except governance incident requirements
- MCP gateway implementation details

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
