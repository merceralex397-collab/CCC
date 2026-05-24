# Intake Storage Integrations Workspace

## Purpose

This workspace owns all planning for Outlook email intake, Box live upload, EVA/Sentry API adapter, website/WhatsApp intake boundary, and spreadsheet bridge adapters.

## Scope Rules

- Intake creates work items and source files without bypassing parser review.
- Sentry/EVA submission is never automatic — reviewed exports require explicit operator/reviewer action.
- Portal/payment automation and autonomous WhatsApp/email send are long-range planned and require separate governance approval before implementation.
- Cloud OCR/document intelligence in the intake path requires the same privacy, cost, data-residency, and vendor review as in the parser path.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/normalized/collisionrelateddocs__collision_releated__sentry_api_complete_guide.md.md` | Sentry/EVA API v1.2: JWT bearer tokens with 5-minute expiry, `/api/v1/jobs` and `/api/v1/submit` endpoints, manual approval gate requirement. |
| `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json` | Authoritative EVA JSON field order for export validation. |
| `docs/reference/normalized/collisionrelateddocs__collision_releated__handover.docx.md` | Mailbox access: `digital@collisionengineers.co.uk` has delegated access to `desk@`, `engineers@`, `info@`. Network storage: `\\192.168.0.106\Collision Engineers\`. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md` | Outlook intake design. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md` | Box storage and file management. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md` | EVA/Sentry integration requirements. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_05_eva_sentry_api_adapter_and_import_control.md` | Sentry API adapter and import control design. |

## Workspace Layout

- `README.md` — this file
- `source_map.md` — reference-to-plan traceability
- `roadmap.md` — sequencing
- `tickets/` — active tickets
- `option-papers/` — unresolved decisions (storage provider, cloud intake)
- `archived_plans/` — implemented and superseded plans
