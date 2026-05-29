# Data Map

Date: 2026-05-23

## Purpose

This is the initial CCC data map for planning and governance. It must be updated before any live integration, cloud OCR/document intelligence, live Box upload, or direct EVA/Sentry submission.

## Data Categories

| Category | Examples | Source | First Use |
| --- | --- | --- | --- |
| Instruction files | PDF, DOCX, DOC, email body instructions | Emails, uploads, historical corpus | Parser and review. |
| Email records | MSG/EML, sender, recipient, subject, body, attachments | Outlook/shared mailboxes or manual upload | Source preservation and future intake. |
| Vehicle details | VRM, make/model, mileage, damage circumstances | Instructions, DVLA/DVSA future adapters, staff review | Parser result and EVA export. |
| Evidence images | vehicle full view, damage close-up, all supporting photos | Email attachments, PDFs, Audatex/manual sources | Package generation and EVA image ordering. |
| Provider/principal data | principal code, aliases, mapping rules, reference sequence | providers.json, job sheets, staff admin | Provider detection and EVA export. |
| Review data | corrections, warnings, approvals, override reasons | CCC app users | Audit and export gates. |
| Package metadata | files, checksums, case/PO, storage status | CCC package builder | Box-ready package and storage adapters. |
| Integration credentials | Box, EVA/Sentry, DVLA/DVSA, cloud services | Admin configuration | Future integrations only. |

## Retention And Storage Notes

- Raw source files are immutable evidence and must not be edited in place.
- Package manifests must include checksums and source references.
- Secrets and credentials must not be committed to the repo.
- Retention periods, deletion process, and legal hold handling are defined as a draft (pending business/DPO sign-off) in `docs/security/data_retention_policy.md`.

## Out Of Scope

CCC does not plan personal injury or KADOE processing.

