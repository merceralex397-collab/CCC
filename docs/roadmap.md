# Roadmap

The first programme milestone is the Operational Core MVP: parser, provider/principal admin, work-item/review queue, EVA-ready export, and Box-ready package generation. Parser is still the first executable MVP inside that wider milestone.

Detailed tickets live in `docs/tickets/backlog_index.md`.

## P0 - Planning, Contracts, And Foundation

1. Promote generated-pack and research knowledge into canonical docs.
2. Lock accepted decisions in ADRs and keep unresolved choices in option papers.
3. Create versioned contracts for work items, parser results, provider config, review/audit events, evidence packages, EVA export, storage adapters, and extraction adapters.
4. Maintain source manifest, provider coverage matrix, and private-corpus planning.
5. Establish governance, security, release, and runbook baselines.

## P1 - Operational Core MVP

1. Build deterministic-first parser core.
2. Deliver non-technical staff UI and equivalent CLI over the same parser core.
3. Deliver provider/principal admin with versioning, activation, rollback, and audit.
4. Deliver work-item lifecycle and review/correction queue.
5. Export validated EVA JSON and generate Box-ready evidence packages.

## P2 - Parser Hardening And Provider Parity

1. Build private corpus golden regression harness.
2. Cover all 26 current provider presets.
3. Triage uncovered/anomalous job-sheet principals: `ACSP`, `OAK/AX`, `PRINCIPAL`, and `WOODLANDS`.
4. Harden PDF, DOCX, DOC, MSG/EML, image, and batch extraction adapters.
5. Prove UI/CLI parity and export/package gates.

## P3 - Integrations, Storage, EVA, And Intake

1. Add Outlook intake adapter after work-item/review model is stable.
2. Add live Box upload using the P1 package shape.
3. Add Sentry/EVA API adapter with manual approval and duplicate protection.
4. Decide long-term CCC-owned storage on Google Cloud, AWS, Azure, or another approved platform.

## P4 - Intelligence, Engineer Pack, And Communications

1. Add valuation evidence support and companion report handling.
2. Add DVLA/DVSA and mileage evidence support.
3. Add image quality/order/duplicate review assistance.
4. Generate engineer packs from reviewed work items and evidence.
5. Draft missing-info and status communications for staff approval.

## P5 - Platform Expansion

1. Add operations analytics from canonical events.
2. Consider customer/partner portal and external APIs.
3. Consider data warehouse and historical mining.
4. Consider external ecosystem integrations only after security, contracts, and Operational Core maturity are proven.

## Scope Guardrail

CCC does not plan personal injury or KADOE workflows.
