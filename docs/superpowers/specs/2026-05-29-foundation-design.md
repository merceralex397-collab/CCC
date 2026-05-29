# Foundation: Governance, Operations, Setup, Coordination — Design

Date: 2026-05-29
Status: approved design (brainstorming output)
Owner: unassigned
Workspace: `docs/plans/foundation/` (group home; sub-areas in governance-security / operations-quality / initial-repo-setup / operational-core)
Source links: `docs/plans/foundation/context.md`, `docs/architecture/governance_security.md`, `docs/security/`, `docs/operations/`, `docs/plans/_groups.md`

## Context

Foundation is the continuous, cross-cutting gating layer and the **most-built** group — governance/security/operations docs and the coordination/scaffold already exist. This iteration maps them into the group, defines the CE role model, updates the vendor register + retention, and captures the cross-cutting gaps the other interviews surfaced.

## Decisions captured (user, 2026-05-29)

- **Scope:** map existing governance/security/operations docs into the foundation group + capture the cross-cutting gaps as a tracked backlog.
- **Role model:** define the CE role model **now** → `docs/security/role_model.md` (draft for sign-off).
- **Vendor register + retention:** update **now** → `docs/security/vendor_register.md` (new vendors) + new `docs/security/data_retention_policy.md` (draft, placeholder periods).

## Goals / Non-goals

**Goals:** the group mapping of existing docs; the CE role model; the updated vendor register; the draft retention policy; the cross-cutting gaps backlog.

**Non-goals:** re-authoring binding governance policy without sign-off (new policy is marked draft); domain implementation of controls (owned by each workspace); operations runbooks beyond governance/ops needs already covered. Personal injury and KADOE remain out of scope (the verifier enforces this).

## Design

### Mapping (existing → foundation group)

- governance-security → `docs/architecture/governance_security.md`, `docs/security/{data_map, dpia_vendor_governance, vendor_register, api_security_standard, source_safety_review, role_model, data_retention_policy}.md`.
- operations-quality → `docs/operations/{release_and_rollback, monitoring_runbooks}.md`, runbooks.
- repo-setup → `initial-repo-setup/`, `tools/verify_scaffold.py`, documentation lifecycle.
- coordination → `operational-core/source_synthesis.md`, `docs/roadmap.md`, `docs/plans/_groups.md`.

### New artifacts this iteration

1. **`docs/security/role_model.md`** — human roles (operator/reviewer/provider-admin/engineer/finance-approver/system-admin) + non-human (bounded agent/skill/tool) permission ceilings; least privilege; maps to casework/ai-platform/finance/intelligence. Draft for sign-off.
2. **`docs/security/data_retention_policy.md`** — retention/deletion/legal-hold per data category; placeholder periods to confirm with business/DPO.
3. **`docs/security/vendor_register.md`** — added Autotrader (via Codex), DVSA-MOT MCP (rotate token), AI model providers (Claude/Codex); noted Graph App RBAC scoping.

### Cross-cutting gaps backlog

`option-papers/cross-cutting-gaps-backlog.md` tracks: role model (now done-draft), DVSA token rotation, redaction data map, retention (now done-draft), deployment/packaging (Python+WinUI), vendor register (now updated) — with owner + status.

## Sequencing

Continuous. The role model unblocks casework review/override, ai-platform agent permissions, and finance approval. Token rotation is immediate. Retention + vendor items gate the bridge/intelligence/business builds.

## Risks & Open Questions

- New governance docs are drafts; require governance/DPO sign-off before they bind.
- Retention periods are legal/business decisions (placeholders only).
- Deployment of Python parser (Tk) + .NET WinUI casework app + work-item service needs an operations packaging plan.

## Acceptance Criteria

- Existing governance/security/operations docs mapped into the foundation group.
- CE role model + draft retention policy authored; vendor register updated with the new vendors + token-rotation note.
- Cross-cutting gaps captured with owners + status.
