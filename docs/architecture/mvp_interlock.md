# MVP Interlock

The parser is the first executable MVP, but it must be planned as one part of the Operational Core MVP. A parser that only emits JSON is not enough for non-technical office staff; staff need to upload files, review extracted fields, correct errors, order images, and produce an EVA-ready package.

## Interlocking Capabilities

| Capability | First MVP Role | Depends On | Feeds |
| --- | --- | --- | --- |
| Parser core | Extract fields from PDF, DOCX, DOC, MSG/EML, images, and batches. | Extraction adapters, provider config. | Parser result, review queue, EVA export. |
| Staff UI | Non-technical upload, preview, review, correction, and export. | Parser core, work-item state, provider admin. | Reviewed result, package build. |
| CLI | Same operations as UI for automation and AI-agent usage. | Parser core and same service methods as UI. | Golden tests, batch processing, future automation. |
| Provider admin | Manage principals, aliases, mapping rules, activation, rollback. | Provider config contract, audit events. | Parser detection, EVA principal/case rules. |
| Work-item queue | Replace spreadsheet working states for ready/missing/review/export/package. | Work item contract, auth/audit identity. | Review queue and operations metrics. |
| Review/audit | Record manual corrections, missing fields, approvals, rejection reasons. | Parser result contract, role model. | EVA export gate, quality loop. |
| Evidence package | Build Box-ready folder and manifest with originals, images, instruction, companion report, notes. | Reviewed result, storage adapter contract. | Box upload later, CCC-owned storage later. |

## First Success Definition

An office user can:

1. Create or open a work item.
2. Upload instruction files and evidence images.
3. Run parser triage and provider detection.
4. Review extracted data with source evidence and warnings.
5. Correct fields without losing extraction provenance.
6. Validate required fields and image ordering.
7. Export EVA-ready JSON in the required field order.
8. Generate a Box-ready evidence package with a manifest.

## Non-Goals For Parser MVP

- No live Box upload unless separately approved.
- No direct Sentry/EVA API submission.
- No autonomous Outlook monitoring.
- No WhatsApp automation.
- No valuation automation as a blocking parser dependency.
- No personal injury or KADOE workflow.

## Why Contracts Come First

Parser runtime work can start only after its contracts are stable enough for UI, CLI, review, and exports to share one model. The contracts in `docs/contracts/` are therefore part of the MVP implementation boundary, not optional paperwork.

