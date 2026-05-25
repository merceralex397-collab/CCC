# Sentry API Enhancement Mechanisms

Date: 2026-05-25
Status: active enhancement evidence note
Owner: unassigned
Created: 2026-05-25
Last reviewed: 2026-05-25
Source links: `docs/reference/raw/collisionrelateddocs/collision_releated/Sentry_API_Complete_Guide.md`, `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`, `docs/contracts/parser_result_v1.md`, `docs/contracts/eva_export_contract_v1.md`, `docs/security/api_security_standard.md`
Roadmap milestone: Section 4 - Intake And Live Integration Boundaries
Dependencies: `docs/plans/intake-storage-integrations/`, `docs/plans/governance-security/`, `docs/plans/operations-quality/`
Expected outputs: source-backed future Sentry/EVA enhancement ideas without making live API writes part of parser MVP
Acceptance criteria: ideas preserve reviewed canonical parser output, avoid undocumented lookup assumptions, and identify owning workspaces and gates
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source-Confirmed Boundary

The Sentry guide documents token, instruction, claim update, note, authority, and report endpoints, but it does not document a general claim/location search endpoint or native batch endpoint. Existing claims are targeted by exact identifier combinations such as claim number plus VRM, EVA reference plus VRM, or file reference plus VRM depending on the endpoint.

Parser MVP implication: keep parser output canonical, reviewed, and source-provenanced. Do not couple extraction to live Sentry reads, and do not submit live writes from parser core.

## Enhancement Ideas

| Idea | API mechanism | Owning workspace | Required gate |
| --- | --- | --- | --- |
| Reviewed instruction submission bridge | `POST /Instruction/Inspection` | `intake-storage-integrations` | manual approval, duplicate prevention, sandbox tests, token refresh, rejection runbook |
| Reviewed location sync | `POST /Claim/LocationUpdate` | `intake-storage-integrations` | reviewed inspection fields, exact claim identifiers, garage/principal lookup ownership, no lookup dependency |
| Released report import and reconciliation | `GET /Report/GetAvailableReports`, `GET /Report/GetReport?id={id}` | `intake-storage-integrations` | released-report-only limitation, retention/licensing review, import audit trail |
| Assessor note and attachment handoff | `POST /Note/SubmitNote` | `intake-storage-integrations` | no autonomous sends, named operator approval, duplicate-note handling, payload/response audit |
| Limited claim-state sync | `POST /Claim/Update`, `POST /Claim/AuthorityStatusUpdate` | `intake-storage-integrations` | field-level approval, rollback rules, exact identifiers, finance/governance review where relevant |
| Engineer report submission bridge | `POST /Report/SubmitReport` | `engineer-communications` | named engineer sign-off, valuation and evidence provenance, sandbox validation, attachment controls |
| Adapter substrate | token and response model across endpoints | `intake-storage-integrations` | token broker, throttling, structured retries, no token logging, dry-run mode |

## Parser Work To Preserve Now

- Keep `inspection_mode`, `inspection_site_source`, `inspection_address_lines`, `inspection_postcode`, confidence, and provenance in the canonical parser result.
- Keep garage and principal lookups outside parser extraction rules until `provider-principal-config` owns the data model and correction workflow.
- Preserve file names, extensions, hashes, source ids, and operator-selected image/package order so future Sentry attachments can be assembled from reviewed package metadata.
- Capture downstream identifiers when source documents provide them, but treat missing identifiers as integration blockers rather than parser failures.

## Explicit Non-Goals For Parser MVP

- No live Sentry/EVA submission from parser core.
- No hidden Sentry lookup to fill missing inspection addresses.
- No native batch assumptions; future bulk work must be client-side with throttling, token refresh, retry, and audit logging.
- No report submission before evidence review, valuation, and named human sign-off workflows exist.
