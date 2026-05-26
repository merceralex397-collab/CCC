# ADR 0001: Parser-First Repository Direction

- Status: accepted
- Date: 2026-05-23

## Decision

CCC starts with the parser foundation, office-staff UI, equivalent CLI, source manifest, provider coverage, and export/storage contracts before broader workflow automation.

## Rationale

The parser is already the strongest automation path because EVA can consume JSON imports. The new source documents clarify missing provider coverage and spreadsheet workflows. Rebuilding around a shared parser core reduces drift between office use and future automation.

## Consequences

- Workflow dashboard, Outlook ingestion, WhatsApp automation, valuation automation, and direct Sentry submission are later work.
- UI and CLI must share the parser core.
- Provider coverage and golden tests become gating work.
