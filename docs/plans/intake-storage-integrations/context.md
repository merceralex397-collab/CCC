# Bridge Workspace — Context (Information Document)

Date: 2026-05-29
Status: active context document
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: bridge (G2, spine, layer: integrations) — see `docs/plans/_groups.md`
Source links: `docs/contracts/evidence_package_contract_v1.md`, `docs/contracts/storage_adapter_contract_v1.md`, `docs/contracts/eva_export_contract_v1.md`, `docs/plans/intake-storage-integrations/plan.md`, `docs/plans/intake-storage-integrations/tickets/p3-integrations.md`, `docs/reference/raw/collisionrelateddocs/collision_releated/Sentry_API_Complete_Guide.md`, `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md`
Purpose: consolidate what is known about the Outlook + Box + EVA bridge so the interview can focus on scope, sequencing, and the live-integration governance forks.

## What this workspace owns

The bridge between CCC's reviewed parser output and the outside systems: **intake** (Outlook/Graph email + attachments → work items), **storage** (Box-ready package → live Box upload), and **eva** (EVA JSON export → EVA/Sentry submission). Plus website/WhatsApp/payment/local-folder *metadata boundaries* and the job-sheet/spreadsheet transition bridge.

It does **not** own: the external customer portal product; payment automation itself; MCP tool *exposure* (that wraps these adapters — owned by `mcp-tooling`); work-item state/review (owned by `casework`); parser extraction (owned by `parser`).

Target broad-workspace split (after the deferred physical move): `bridge/intake`, `bridge/storage`, `bridge/eva`.

## Hard constraints from the contracts (already drafted)

- **EVA export** (`eva_export_contract_v1.md`): field order must match `Final Format Example 02.json` (golden-tested); export gates block missing provider/dates/inspection-address/mileage/VAT/image-order/critical-warnings; non-instruction evidence (images) must not export. Implemented in `src/ccc_parser/exporters/eva.py` + `packaging.py`. **Direct Sentry submission is future, manual-approval-gated**; the Sentry API supports exact-identifier writes (`POST /Claim/LocationUpdate`, `POST /Instruction/Inspection`) and released-report reads (`GET /Report/GetAvailableReports`, `GetReport`), but **no general claim/location search and no native batch endpoint** — so no auto-fill of parser-missing data and client-side throttled batching only.
- **Evidence package** (`evidence_package_contract_v1.md`): deterministic local folder named by reviewed `case_po` (fallback `work_item_id`+VRM, never invented); required contents (originals, original email, images, EVA JSON when generated, companion report, manifest); image order = full-vehicle preview, close-up-damage preview, then all images; manifest carries `source_channel`, `portal_submission_id`, `payment_status`, `payment_chaser_sent`, `box_folder_url`.
- **Storage adapter** (`storage_adapter_contract_v1.md`): **Box-first** — first deliverable is `package_only` (local Box-ready folder + manifest); live Box upload is a *separate later adapter* using the same package shape; adapter output carries `mode` (package_only/dry_run/live_upload), `status`, `remote_references`, `checksums`, `warnings`, `audit_event_id`, Box folder URL/stage. Future GCS/S3/Azure tied to a governed storage decision.

## Outlook/Graph intake — grounded in Microsoft Learn (2026-05-29)

Mailboxes: `digital@collisionengineers.co.uk` has delegated access to `desk@`, `engineers@`, `info@` (per the MCP reference plan).

- **Permissions**: delegated `Mail.Read.Shared`/`Mail.ReadWrite.Shared` can read shared folders **but cannot subscribe to change notifications** ([Get Outlook messages in a shared or delegated folder](https://learn.microsoft.com/graph/outlook-share-messages-folders)). App-only `Mail.Read` supports notifications **but defaults to all mailboxes** and must be scoped. Use `Mail.ReadBasic` (no body/attachments) where attachments aren't needed; `Mail.Read` where they are.
- **Least-privilege scoping**: restrict the app to only the four mailboxes via **Role Based Access Control for Applications** (modern; `New-ApplicationAccessPolicy` is legacy and slated for deprecation) targeting a mail-enabled security group of those mailboxes ([auth-limit-mailbox-access](https://learn.microsoft.com/graph/auth-limit-mailbox-access)).
- **Sync mechanism**: **delta query** is the efficient *pull* model (`GET /users/{id}/mailFolders('Inbox')/messages/delta`) — incremental, throttle-friendly, **no hosted endpoint required**. **Change notifications (webhooks)** are *push* but need a public HTTPS endpoint, subscription renewal, and `missed`/lifecycle handling with delta recovery; Outlook caps 1000 subscriptions/mailbox. Recommended: **delta-query polling for MVP, webhooks later**.
- Read messages: `GET /users/{mailbox}/mailFolders('Inbox')/messages`; download attachments via the message attachments endpoint; preserve the original `.eml`/`.msg` and `internetMessageId` + checksums for de-duplication (the parser's `readers.py` already materialises MSG/EML attachments through triage).

## Current planning state

- **P1 (foundational, mostly in the parser already):** EVA JSON export (`exporters/eva.py`) and Box-ready package manifest (`packaging.py`) exist. The bridge's P1 job is the *adapter boundary* around them.
- **P3 (planned, not built):** `tickets/p3-integrations.md` — Outlook intake adapter, live Box upload adapter, website/payment intake boundary, EVA/Sentry submission control, CCC-owned storage decision. All require governance/security review; none are built.
- Dependencies: `casework` (work-item/review to attach intake to), `mcp-tooling` (tool exposure), `governance-security` (vendor/privacy/API security, autonomous-action gates), `operations-quality` (sandbox tests, runbooks — runbooks already exist for outlook-intake-stopped, box-upload-failure, eva-rejected-payload).

## Guardrails

No autonomous EVA/Sentry submit, live Box write, payment chasing, or WhatsApp send without explicit approval gates. Adapter behaviour stays separate from MCP exposure. Personal injury and KADOE remain out of scope. Reviewed work-item data is the gate before any export/package/upload.

## Open design questions for the interview

1. Which bridge sub-area(s) and how far this iteration: design-only adapter boundaries, or build a live path?
2. Outlook intake: confirm delta-query polling + app-only `Mail.Read` scoped via App RBAC (vs delegated, vs webhooks) and which mailboxes/folders.
3. EVA/Sentry: stay export-only (human submits the JSON) or plan the live submission adapter (manual-approval-gated) now?
4. Box: keep `package_only` (local Box-ready folder) or plan the live Box upload adapter now?
5. Spreadsheet/job-sheet transition bridge: in scope this iteration or later?
