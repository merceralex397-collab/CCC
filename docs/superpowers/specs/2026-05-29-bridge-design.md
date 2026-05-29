# Bridge: Outlook Intake, Box Storage, and EVA Submission — Design

Date: 2026-05-29
Status: approved design (brainstorming output)
Owner: unassigned
Workspace: `docs/plans/intake-storage-integrations/` (group: bridge, G2, spine)
Source links: `docs/plans/intake-storage-integrations/context.md`, `docs/contracts/evidence_package_contract_v1.md`, `docs/contracts/storage_adapter_contract_v1.md`, `docs/contracts/eva_export_contract_v1.md`, `docs/plans/intake-storage-integrations/tickets/p3-integrations.md`, `docs/reference/raw/collisionrelateddocs/collision_releated/Sentry_API_Complete_Guide.md`, `docs/operations/runbooks/outlook-intake-stopped.md`, `src/ccc_parser/readers.py`, `src/ccc_parser/exporters/eva.py`, `src/ccc_parser/packaging.py`
Microsoft Graph grounding (Microsoft Learn, 2026-05-29): `https://learn.microsoft.com/graph/outlook-share-messages-folders`, `https://learn.microsoft.com/graph/auth-limit-mailbox-access`, `https://learn.microsoft.com/graph/delta-query-messages`, `https://learn.microsoft.com/graph/change-notifications-overview`

## Context

The bridge connects CCC's reviewed parser output to the outside systems: **intake** (Outlook/Graph), **storage** (Box), **eva** (EVA/Sentry). The EVA export and Box-ready package already exist inside the parser (`exporters/eva.py`, `packaging.py`); the bridge owns the *adapter boundaries* around them and the live-system edges. Binding constraints are the three v1 contracts (see `context.md`).

## Decisions captured (user, 2026-05-29)

- **Staged shape:** build read-only **Outlook intake → work items**; keep **Box at `package_only`** and **EVA export-only** (human submits). No autonomous external writes this iteration.
- **Outlook mechanism:** scheduled **delta-query polling** with app-only `Mail.Read` scoped via **Role Based Access Control for Applications** to a security group of the four mailboxes.
- **Governed option-papers (design only, not built):** live Box upload adapter; EVA/Sentry submission adapter; spreadsheet/job-sheet transition bridge.

## Goals / Non-goals

**Goals:** capture relevant shared-mailbox email + attachments into reviewable work items; preserve originals; de-duplicate; reuse the parser's existing triage/readers; keep every external write gated behind review + approval; produce the three option-papers.

**Non-goals (this iteration):** live Box upload, live EVA/Sentry submission, payment automation, WhatsApp sends, the customer portal product, work-item state/review internals (owned by `casework`), and MCP tool exposure (owned by `mcp-tooling`). Personal injury and KADOE remain out of scope.

## Design

### intake — build (read-only Outlook adapter)

- **Sync:** scheduled delta-query polling per mailbox folder (`GET /users/{mailbox}/mailFolders('Inbox')/messages/delta`); persist the delta token; incremental and throttle-friendly; no hosted endpoint. Change-notification webhooks are a later enhancement (need a hosted HTTPS endpoint + lifecycle/`missed` recovery).
- **Auth / least privilege:** app-only `Mail.Read` (or `Mail.ReadBasic` where attachments aren't required), scoped by **App RBAC for Applications** to a mail-enabled security group of `desk@`, `engineers@`, `info@`, `digital@` only. (`New-ApplicationAccessPolicy` is the legacy mechanism; use App RBAC.)
- **Per-message processing:** create a work item + source manifest; **preserve the original `.eml`/`.msg`**; route attachments through the existing `src/ccc_parser/readers.py` triage path (already materialises MSG/EML attachments and computes hashes). De-duplicate on `internetMessageId` + content checksums. Mark processed via category/move — **never delete** source mail. Idempotent re-runs (re-seeing a message is a no-op).
- **Boundary:** intake *stages* work items for parser review; it does not bypass review or auto-export. Source labels/categories distinguish instruction vs image-only vs query flows.
- **Dependencies:** `casework` (a minimal work-item/review target — hard dependency), `governance-security` (Graph vendor/privacy/API-security sign-off — this is a live read of PII email), `operations-quality` (sandbox tests; runbook `outlook-intake-stopped.md` exists), `mcp-tooling` (later tool exposure).

### storage — gated (`package_only` only)

Keep the deterministic local Box-ready folder + manifest from `packaging.py` per `evidence_package_contract_v1.md`. No live upload. Live upload is option-paper #1.

### eva — gated (export-only)

Keep validated EVA JSON from `exporters/eva.py` per `eva_export_contract_v1.md`; a human submits it. Live submission is option-paper #2.

### Option-papers (design only)

1. **Live Box upload adapter** — `storage_adapter_contract` `mode` progression `package_only → dry_run → live_upload`; same package shape; duplicate handling; upload-status tracking; runbook `box-upload-failure.md`.
2. **EVA/Sentry submission adapter** — manual-approval-gated; exact-identifier writes only (`POST /Claim/LocationUpdate`, `POST /Instruction/Inspection`); no general search/auto-fill; client-side throttled batching; duplicate prevention; failure recovery; runbook `eva-rejected-payload.md`; JWT/token handling per the Sentry guide.
3. **Spreadsheet/job-sheet transition bridge** — migrate the legacy CE Job Sheet workbook semantics (Jobs/Principals/Garages) into work-item state without macro side effects.

## Sequencing

1. Coordinate a minimal work-item/review target with `casework`.
2. Build the delta-query polling intake adapter (scoped via App RBAC), with dedup + idempotency.
3. Sandbox/mocked-Graph tests + the intake runbook.
4. Write the three option-papers (parallel).

## Testing

- Mocked Graph responses (no live tenant in tests); delta-token persistence and incremental re-poll.
- Idempotency/dedup: same `internetMessageId` re-seen → no duplicate work item.
- Attachments routed through existing triage/readers; original `.eml`/`.msg` preserved with checksums.
- "Never delete source mail" assertion; processed-marking via category/move.
- `python tools/verify_scaffold.py` green.

## Risks & Open Questions

- Ownership of the Entra app registration, admin consent, and the RBAC security-group setup (CE IT / governance).
- Whether intake auto-creates work items or stages them into a review queue (depends on the `casework` work-item contract).
- Folder scoping: whole Inbox vs a controlled subfolder per mailbox.
- Graph throttling during initial backfill (bounded batch + delta).
- `casework` work-item contract is a hard dependency for intake to attach to.

## Acceptance Criteria

- A new email in a scoped mailbox produces a work item + source manifest with the original `.eml`/`.msg` preserved and attachments routed through triage; re-runs are idempotent; source mail is never deleted.
- The adapter uses delta-query polling with app-only `Mail.Read` scoped to the four mailboxes via App RBAC.
- Box remains `package_only` and EVA remains export-only; no autonomous external writes exist.
- Three option-papers (live Box upload, EVA/Sentry submission, spreadsheet bridge) exist with options, decision criteria, and governance gates.
- `verify_scaffold.py` passes; governance-security and casework dependencies are linked.
