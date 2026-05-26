# ADR 0003: Operational Core Is The First Programme MVP

Date: 2026-05-23

## Status

Accepted.

## Context

Earlier plans considered parser-only, intake-only, AI-agent, and wider platform paths. The current evidence shows that parser output is useful only when staff can review it, correct it, package evidence, and prepare an EVA-ready handoff.

## Decision

The first programme milestone is the Operational Core MVP:

- parser;
- provider/principal admin;
- work-item/review queue;
- Box-ready evidence package generation;
- EVA-ready export validation.

Parser remains the first executable MVP inside this wider milestone.

## Consequences

- Parser contracts must support work item, review, audit, package, and EVA export needs from the start.
- UI and CLI parity is required because staff use the UI and automation/AI agents need the CLI.
- Live Box upload, Outlook intake, direct EVA/Sentry submission, valuation automation, and cloud document intelligence remain future phases unless separately approved.

