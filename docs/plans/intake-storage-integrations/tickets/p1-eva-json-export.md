# P1-006 EVA JSON Export

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/contracts/eva_export_contract_v1.md`, `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json`, `docs/research/gptevadeepresearch.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P1-001 (Parser Core MVP), P1-005 (Work Item And Review Queue).
- Expected outputs: EVA-ready JSON export adapter and validation gate.
- Acceptance criteria: field order matches `Final Format Example 02.json`; required provider, dates as `DD/MM/YYYY`, inspection address/image-based marker, mileage/VAT/unit constraints, and warning gates are enforced; export is never automatic.
- Verification required: golden export tests, field-order assertion, invalid-export tests.
- Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p1-operational-core-mvp.md` § P1-006.
- Superseded-by: none.

## Context

Sentry API v1.2 requires JWT bearer tokens with 5-minute expiry (see normalized Sentry API guide). There is no public OpenAPI schema; the EVA JSON field order from `Final Format Example 02.json` is the authoritative contract. Direct submission must never be automatic — only an explicit operator/reviewer action may trigger it.
