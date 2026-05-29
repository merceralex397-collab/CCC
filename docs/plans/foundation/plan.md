# Foundation Plan (group home)

Date: 2026-05-29
Status: active workspace plan
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: foundation
Wave: G0 / continuous
Layer: cross-cutting
Source links: `docs/plans/foundation/context.md`, `docs/superpowers/specs/2026-05-29-foundation-design.md`, `docs/security/role_model.md`, `docs/security/data_retention_policy.md`, `docs/security/vendor_register.md`, `docs/architecture/governance_security.md`, `docs/plans/_groups.md`
Roadmap milestone: G0 / continuous
Dependencies: all workspaces (foundation gates every wave)
Expected outputs: group mapping, the CE role model, retention policy, updated vendor register, and the cross-cutting gaps backlog
Acceptance criteria: governance/operations docs mapped; new policy authored as drafts for sign-off; cross-cutting gaps tracked with owners
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/foundation/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

This is the **foundation** broad-workspace group home — the continuous, cross-cutting gating layer. Sub-areas (current folders): `governance-security`, `operations-quality`, `repo-setup` ← `initial-repo-setup/`, `coordination` ← `operational-core/` (legacy infra folders' physical move deferred — task #1). See `docs/plans/_groups.md`.

## This Iteration — Map Existing + Define Role Model + Update Vendor/Retention

Approved design: `docs/superpowers/specs/2026-05-29-foundation-design.md`. Decisions (2026-05-29): map existing docs + gap backlog; define the CE role model now; update vendor register + retention now.

| Deliverable | Where |
| --- | --- |
| CE role model (draft) | `docs/security/role_model.md` |
| Data retention policy (draft) | `docs/security/data_retention_policy.md` |
| Vendor register update | `docs/security/vendor_register.md` |
| Data map retention pointer | `docs/security/data_map.md` |
| Cross-cutting gaps backlog | `option-papers/cross-cutting-gaps-backlog.md` |

## Existing Content Mapped

governance-security → `docs/architecture/governance_security.md` + `docs/security/*`; operations-quality → `docs/operations/*` + runbooks; repo-setup → `initial-repo-setup/` + `tools/verify_scaffold.py`; coordination → `operational-core/source_synthesis.md` + `docs/roadmap.md` + `docs/plans/_groups.md`.

## Dependency Cross-Check

Foundation gates **every** workspace: privacy/vendor/retention/licensing/expert-boundary/API-security (governance-security) and release/rollback/regression/monitoring/runbooks/rollout/support/decommissioning (operations-quality).

## Non-Overlap Rules

Does not own domain implementation of controls (each workspace implements its own under foundation policy). Personal injury and KADOE remain out of scope.

## Promotion Gates

- New governance docs are **drafts requiring governance/DPO sign-off** before they bind.
- Governance-gated work starts in option-papers, not tickets.
- DVSA-MOT token rotation is an immediate action (see the gaps backlog).
