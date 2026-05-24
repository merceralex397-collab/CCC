# Cross-Workspace Backlog Index

Date: 2026-05-24
Status: active cross-workspace coordination index
Owner: unassigned
Created: 2026-05-23
Last reviewed: 2026-05-24
Source links: `docs/plans/operational-core/source_synthesis.md`, `docs/reference/originalplanning/`, `docs/research/`, `docs/reference/test-context/`
Roadmap milestone: Operational Core MVP
Dependencies: source synthesis and canonical promotion rules
Expected outputs: cross-workspace phase index; active tickets in owning workspaces
Acceptance criteria: every promoted idea is represented in a workspace ticket, merged into canonical docs/contracts, captured in the all-ideas ledger, or superseded
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/operational-core/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

This is the cross-workspace coordination index for the CCC programme backlog. As of 2026-05-24, tickets have been relocated from `docs/plans/operational-core/tickets/` into their owning domain workspaces. The old ticket files in this folder are tombstones (preserved for scaffold verification) pointing to the new locations.

## Phase Ticket Locations

| Phase | Coordination File | Owning Workspace Tickets |
| --- | --- | --- |
| P0 | `docs/plans/operational-core/tickets/p0-foundation.md` (tombstone) | `parser-extraction/tickets/`, `governance-security/`, cross-workspace ADRs |
| P1 | `docs/plans/operational-core/tickets/p1-operational-core-mvp.md` (tombstone) | `parser-extraction/`, `user-experience-interfaces/`, `provider-principal-config/`, `case-workflow-state/`, `intake-storage-integrations/` |
| P2 | `docs/plans/operational-core/tickets/p2-parser-hardening-provider-parity.md` (tombstone) | `parser-extraction/tickets/`, `provider-principal-config/tickets/` |
| P3 | `docs/plans/operational-core/tickets/p3-integrations-storage-eva-intake.md` (tombstone) | `intake-storage-integrations/tickets/` |
| P4 | `docs/plans/operational-core/tickets/p4-intelligence-engineer-communications.md` (tombstone) | `vehicle-valuation-data/`, `evidence-estimate-review/`, `engineer-communications/` |
| P5 | `docs/plans/operational-core/tickets/p5-platform-expansion.md` (tombstone) | `analytics-data-platform/`, `external-platform-partners/` |

## Active Parser MVP Plan

The parser MVP implementation plan has moved to:
`docs/plans/parser-extraction/parser-mvp/plan.md`

The old path `docs/plans/operational-core/parser-mvp/plan.md` is preserved as a stub for scaffold verification.

## All-Ideas Planning Rule

Ideas not represented in workspace tickets are captured in `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md` until a future planning pass promotes them into an owning workspace ticket or canonical document.

## Ticket Requirements

Each workspace ticket must include:

- status;
- owner placeholder;
- created date;
- last reviewed date;
- source links;
- roadmap milestone;
- dependencies;
- expected outputs;
- acceptance criteria;
- verification required;
- archive target when implemented or superseded;
- supersedes/superseded-by fields.
