# Open Questions and Decision Log

## Purpose

Track unresolved questions and decisions that shape the build.

## High-priority open questions

### EVA

1. What is the exact EVA JSON import schema?
2. Does EVA expose an API, or only JSON file import?
3. How are JSON imports submitted?
4. Does EVA have a sandbox/test environment?
5. Does EVA support idempotency/external reference fields?
6. Can EVA store Box links or file references?
7. Are images/documents imported into EVA or only stored in Box?
8. What validation errors does EVA return?
9. Who is the EVA vendor/technical contact?

### Spreadsheet

1. What are the exact spreadsheet columns?
2. Which fields are manually typed vs formula-derived?
3. Is the spreadsheet currently the operational source of truth?
4. Are there macros or downstream dependencies?
5. Should the spreadsheet remain as the review surface during pilot?

### Outlook

1. Which mailbox/folder should be monitored?
2. Are emails sent to a shared mailbox or personal mailboxes?
3. What senders/subjects identify relevant emails?
4. How often do images arrive separately?
5. How are separate image emails currently matched manually?
6. Are there duplicates/forwards/replies that may trigger reprocessing?

### Box

1. What is the current folder structure?
2. Are naming conventions already defined?
3. Which staff/groups need access?
4. Is Box metadata available and acceptable for this use case?
5. Are Box retention policies already configured?
6. Is Box AI Extract licensed/allowed for this workflow?

### Extraction

1. What fields must be extracted?
2. Which fields are mandatory for EVA?
3. How many PDF templates exist?
4. How many PDFs are scanned vs text-based?
5. Are there handwritten fields?
6. What languages appear in documents?
7. What accuracy threshold is required before auto-approval?

### Security/privacy

1. What personal data categories appear in PDFs/images?
2. Is a DPIA or equivalent assessment required?
3. What retention period applies to source and extracted data?
4. Are third-party AI/OCR services permitted?
5. What audit/reporting is required?

## Decision log

| ID | Decision | Status | Rationale | Date |
|---|---|---|---|---|
| ADR-001 | Use a canonical JSON model before EVA mapping. | Recommended | Decouples extraction from EVA-specific schema. | 2026-05-22 |
| ADR-002 | Preserve original files in Box and never overwrite them. | Recommended | Supports audit and data integrity. | 2026-05-22 |
| ADR-003 | Use human review for low-confidence or incomplete records. | Recommended | Reduces risk of incorrect EVA entries. | 2026-05-22 |
| ADR-004 | Use a work item state machine. | Recommended | Improves reliability, retries, and monitoring. | 2026-05-22 |
| ADR-005 | Keep spreadsheet as a temporary control/review layer during MVP. | Recommended | Maintains business continuity while automation matures. | 2026-05-22 |
| ADR-006 | Use Microsoft Graph for Outlook integration. | Recommended pending tenant confirmation | Official Microsoft path for mailbox/API integration. | 2026-05-22 |
| ADR-007 | Use Box API/metadata for storage traceability. | Recommended pending Box account capability | Supports automated storage and metadata. | 2026-05-22 |

## Assumptions to validate

| Assumption | Risk if wrong | Validation method |
|---|---|---|
| EVA can accept automated JSON import. | EVA integration may require manual upload or UI automation. | Obtain EVA docs/test import. |
| Source emails can be monitored via Microsoft Graph. | Intake may require alternative connector or mailbox forwarding. | Tenant/admin spike. |
| Box API access is available. | File storage automation may need manual or alternative approach. | Box admin/API spike. |
| PDFs have extractable or OCR-readable text. | Extraction may need more human review. | Sample corpus analysis. |
| Related image emails contain enough correlation signals. | Manual image matching may remain significant. | Analyse historical email samples. |

## Decision-making rule

When in doubt, choose the design that preserves source evidence, prevents duplicate EVA entries, and makes exceptions visible.
