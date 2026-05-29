# Ticket: Outlook/Graph Read-Only Intake Adapter

Status: planned (ready to build once casework work-item target exists + governance sign-off)
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Source links: `docs/superpowers/specs/2026-05-29-bridge-design.md`, `docs/plans/intake-storage-integrations/context.md`, `docs/plans/intake-storage-integrations/plan.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md`, `src/ccc_parser/readers.py`, `docs/operations/runbooks/outlook-intake-stopped.md`
Roadmap milestone: G2 bridge (spine)
Dependencies: case-workflow-state (minimal work-item/review target), governance-security (Graph vendor/privacy/API-security sign-off), operations-quality (sandbox tests, runbook)
Expected outputs: a read-only Outlook intake adapter that turns scoped shared-mailbox email into reviewable work items with preserved sources
Acceptance criteria: see deliverables; no autonomous external writes; reviewed work-item gates all downstream
Verification required: `python tools/verify_scaffold.py`, mocked-Graph intake tests, dedup/idempotency tests
Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/`
Supersedes: refines the P3-001 Outlook Intake portion of `tickets/p3-integrations.md`
Superseded-by: none

## Scope

Read-only Outlook intake only. No EVA/Sentry submit, no live Box upload, no payment/WhatsApp automation. Personal injury and KADOE remain out of scope.

## Deliverables

1. **Delta-query polling client**: scheduled poll of `GET /users/{mailbox}/mailFolders('Inbox')/messages/delta` per scoped mailbox; persist + reuse the delta token; bounded batch on backfill.
2. **Auth/scoping**: app-only `Mail.Read` (attachments needed) scoped via **App RBAC for Applications** to a mail-enabled security group containing only `desk@`, `engineers@`, `info@`, `digital@`. Token/secret handled server-side; never committed.
3. **Work-item creation**: each new message → a work item + source manifest via the `casework` work-item contract; classify source flow (instruction / image-only / query).
4. **Source preservation**: keep the original `.eml`/`.msg`; route attachments through `src/ccc_parser/readers.py` triage (hashes computed there); store `internetMessageId`.
5. **De-duplication + idempotency**: skip messages already seen (by `internetMessageId` + content checksum); re-runs create no duplicates.
6. **Processed marking**: mark handled mail via category/move; **never delete** source mail.

## Acceptance Criteria

- A new email in a scoped mailbox yields one work item + manifest, original email preserved, attachments triaged; re-poll is idempotent; source mail never deleted.
- Access is provably limited to the four mailboxes (App RBAC), not the whole tenant.
- Intake stages for review; it does not auto-export or bypass parser review.
- Tests run against mocked Graph (no live tenant); dedup/idempotency covered; runbook `outlook-intake-stopped.md` referenced.

## Blocked-by

- `casework` minimal work-item/review target (hard dependency).
- governance-security sign-off for the live PII email read + Entra app registration/consent/RBAC group.
