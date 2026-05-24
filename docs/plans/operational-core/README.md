# Operational Core Planning

Date: 2026-05-24
Status: active coordination workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/plans/operational-core/source_synthesis.md`, `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md`, `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`
Roadmap milestone: Operational Core MVP coordination
Dependencies: parser-extraction, provider-principal-config, case-workflow-state, intake-storage-integrations, user-experience-interfaces, operations-quality, governance-security
Expected outputs: cross-workspace sequencing, dependency coordination, and first-slice acceptance gates
Acceptance criteria: Operational Core coordinates owning workspaces without duplicating their active domain tickets
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/operational-core/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

Operational Core is the first executable slice of CCC. After the planning workspace expansion, it coordinates sequencing across owning workspaces rather than permanently owning every parser, provider, workflow, integration, UI, intelligence, analytics, or partner ticket.

## Coordination Responsibilities

- Maintain `source_synthesis.md` as the source-promotion and canonical-destination map.
- Maintain a cross-workspace backlog index for the first-slice delivery sequence.
- Keep MVP interlock visible across parser, provider config, work item state, review, export, package, UI, governance, and operations gates.
- Link to the owning workspace when a ticket moves out of Operational Core.

## Current Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/plans/operational-core/source_synthesis.md` | Current source promotion map. |
| `docs/plans/operational-core/tickets/backlog_index.md` | Current phased backlog before full ticket relocation. |
| `docs/architecture/mvp_interlock.md` | Parser, UI, CLI, provider admin, work-item, review, and package interlock. |
| `docs/roadmap.md` | Whole-programme roadmap. |
