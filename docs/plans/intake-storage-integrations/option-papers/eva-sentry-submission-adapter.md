# Option Paper: EVA/Sentry Submission Adapter

Status: open (design only — not approved for build)
Owner: unassigned
Created: 2026-05-29
Group: bridge / eva (G2)
Source links: `docs/contracts/eva_export_contract_v1.md`, `docs/reference/raw/collisionrelateddocs/collision_releated/Sentry_API_Complete_Guide.md`, `docs/superpowers/specs/2026-05-29-bridge-design.md`, `docs/operations/runbooks/eva-rejected-payload.md`

## Context

EVA is export-only today: `src/ccc_parser/exporters/eva.py` produces validated EVA JSON in `Final Format Example 02.json` field order; a human submits it. This paper evaluates a live Sentry submission adapter. The Sentry API supports **exact-identifier writes** (`POST /Claim/LocationUpdate`, `POST /Instruction/Inspection`) and released-report reads (`GET /Report/GetAvailableReports`, `GetReport`) — but **no general claim/location search and no native batch endpoint**, so no auto-fill of parser-missing data and only client-side throttled batching.

## Options To Evaluate

1. **Manual-approval-gated submission adapter** — operator/reviewer explicitly triggers each submit; no autonomous send.
2. **Export-only retained** — staff submit via the EVA UI; CCC only produces the JSON.
3. **Read-only first** — implement released-report reads (`GetAvailableReports`/`GetReport`) before any write, to build confidence with no write risk.

## Decision Criteria

JWT/token handling (the guide notes short token expiry) server-side only; manual-approval gate; duplicate-payload prevention; client-side throttled batching; failure recovery (runbook); sandbox/mock availability; audit of every request/response; no autonomous submission.

## Governance Gates

API-access approval + security review mandatory. Direct submission must never be automatic. Belongs after intake + review are proven.

## Open Questions

EVA sandbox availability; conditionally-required fields per submission type; duplicate-detection support on the EVA side; token-refresh strategy within the short expiry window.
