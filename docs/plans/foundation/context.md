# Foundation Workspace — Context (Information Document)

Date: 2026-05-29
Status: active context document
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: foundation (G0 / continuous, layer: cross-cutting) — see `docs/plans/_groups.md`
Source links: `docs/architecture/governance_security.md`, `docs/security/data_map.md`, `docs/security/dpia_vendor_governance.md`, `docs/security/vendor_register.md`, `docs/security/api_security_standard.md`, `docs/security/source_safety_review.md`, `docs/operations/release_and_rollback.md`, `docs/operations/monitoring_runbooks.md`, `docs/plans/operational-core/source_synthesis.md`, `docs/plans/_groups.md`

Group home for the foundation broad workspace. Sub-areas (current folders pending the deferred move): `governance-security`, `operations-quality`, `repo-setup` ← `initial-repo-setup/`, `coordination` ← `operational-core/`. (The legacy infra folders' physical move is deferred — see task #1.)

## What this workspace owns (continuous, gates every wave)

- **governance-security**: DPIA/vendor governance + risk acceptance; data map, retention, redaction, access review, audit policy; expert-evidence boundary + risk-language; public/commercial data licensing + API security standards.
- **operations-quality**: test corpus + regression harness; release/rollback; monitoring/runbooks/alerts/incident playbooks; pilot/shadow/rollout/support ownership/decommissioning gates.
- **repo-setup**: repository scaffold, documentation lifecycle, scaffold verification tooling.
- **coordination**: roadmap, source-synthesis, the groups overlay, cross-workspace sequencing.

## Current state — this is the most-built group

Real foundation content already exists:
- Governance/security: `docs/architecture/governance_security.md`; `docs/security/{data_map, dpia_vendor_governance, vendor_register, api_security_standard, source_safety_review}.md`.
- Operations: `docs/operations/{release_and_rollback, monitoring_runbooks}.md`; runbooks `outlook-intake-stopped`, `box-upload-failure`, `eva-rejected-payload`.
- Coordination/setup: `operational-core/source_synthesis.md`, `docs/roadmap.md`, `docs/plans/_groups.md` (new), `initial-repo-setup/` scaffold + `tools/verify_scaffold.py`.

So foundation is less about new build and more about **mapping what exists + closing the cross-cutting gaps** the other interviews surfaced.

## Cross-cutting gaps surfaced by the interviews (the valuable backlog)

1. **CE role model** — `casework` (reviewer / provider-admin / override roles), `ai-platform` (agent permission levels), `finance` (approval) all depend on a defined role model. Not yet defined.
2. **DVSA-MOT token rotation** — outstanding security action (token in plaintext in `collisionplugin`); rotate + secret-store.
3. **Redaction data map** — `ai-platform` redaction-before-external-call needs the PII field mapping on top of `data_map.md`.
4. **Retention policy** — `intelligence/vehicle` evidence store, `casework` historical search, `business/analytics` all need retention limits.
5. **Deployment/packaging** — Python parser (Tk) + .NET WinUI casework app + work-item service on staff Windows machines; release/rollback + MSIX packaging.
6. **Vendor register updates** — new vendors to register: Microsoft Graph (Outlook), Box, DVSA-MOT, Autotrader/Codex, model providers (Claude/Codex).

## Dependencies

**All workspaces** — foundation gates every wave (privacy/vendor/retention/licensing/expert-boundary/API-security + release/regression/rollout/support/decommissioning).

## Guardrails

Governance-gated work starts in option-papers, not implementation tickets; raw evidence immutable; no autonomous external action without approval; named humans retain expert judgement. Personal injury and KADOE remain out of scope (the verifier enforces this).

## Open design questions for the interview

1. Scope: map the existing governance/security/operations docs into the foundation group + capture the cross-cutting gaps as a backlog (vs build new artifacts now)?
2. Is defining the **CE role model** a foundation priority now (several groups depend on it)?
3. Update the **vendor register + retention policy** now for the new vendors (Graph/Box/DVSA/Codex/models) and data stores (evidence/search/analytics)?
