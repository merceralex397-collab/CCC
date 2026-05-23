# Backlog Index

Date: 2026-05-23
Status: active backlog index
Owner: unassigned
Created: 2026-05-23
Last reviewed: 2026-05-23
Source links: `docs/plans/operational-core/source_synthesis.md`, `docs/reference/originalplanning/`, `docs/research/`, `docs/reference/test-context/`
Roadmap milestone: Operational Core MVP
Dependencies: source synthesis and canonical promotion rules
Expected outputs: phased ticket index and active ticket files
Acceptance criteria: every promoted idea is represented in a phase ticket, merged into canonical docs/contracts, parked, or superseded
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/operational-core/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

This is the canonical phased backlog for CCC planning. Every generated-pack idea is promoted into a ticket, merged into canonical docs/contracts, explicitly parked in `docs/plans/operational-core/source_synthesis.md`, or superseded by ADRs.

## Phase Files

| Phase | File | Outcome |
| --- | --- | --- |
| P0 | `docs/plans/operational-core/tickets/p0-foundation.md` | Planning, contracts, provider corpus, governance, and parser-ready foundation. |
| P1 | `docs/plans/operational-core/tickets/p1-operational-core-mvp.md` | Parser, provider admin, work item/review queue, EVA export, and Box-ready package MVP. |
| P2 | `docs/plans/operational-core/tickets/p2-parser-hardening-provider-parity.md` | Provider parity, corpus regression, extraction hardening, and UI/CLI parity hardening. |
| P3 | `docs/plans/operational-core/tickets/p3-integrations-storage-eva-intake.md` | Outlook intake, live storage, EVA/Sentry adapter, and operational integration. |
| P4 | `docs/plans/operational-core/tickets/p4-intelligence-engineer-communications.md` | Valuation support, image intelligence, engineer pack, communication drafting. |
| P5 | `docs/plans/operational-core/tickets/p5-platform-expansion.md` | Analytics, portal/API, data warehouse, partner integrations, continuous improvement. |

## Ticket Requirements

Each ticket must include:

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
- archive target when implemented or superseded.
- supersedes/superseded-by fields.

## Parking Rule

Ideas not represented in these phase files are parked in `docs/plans/operational-core/source_synthesis.md` until a future planning pass promotes them.
