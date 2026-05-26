# Implementation Roadmap

## Delivery strategy

Build the automation centre incrementally. Each phase should produce operational value and reduce manual effort without depending on the entire final architecture being complete.

## Phase 0: discovery and baselining

### Goals

- Confirm the current process in detail.
- Collect representative sample documents/emails.
- Confirm spreadsheet columns.
- Confirm EVA JSON/API capabilities.
- Confirm Box folder/permission requirements.

### Outputs

- Process map.
- Sample corpus.
- Field inventory.
- EVA schema/import notes.
- Security/privacy initial assessment.
- Prioritised MVP scope.

### Exit criteria

- At least 20–50 representative documents/emails reviewed, or enough to cover known templates.
- Existing spreadsheet mapped.
- EVA import path confirmed.
- Pilot mailbox/folder identified.

## Phase 1: email intake and Box storage MVP

### Goals

- Detect relevant emails.
- Download PDF/image attachments.
- Create work items.
- Store files in Box.
- Update status/control table.

### Outputs

- Outlook intake worker.
- Box folder/file upload worker.
- Work item state store.
- Control spreadsheet/status export.
- Duplicate detection by email and attachment checksum.

### Value

This phase removes or reduces manual file capture and storage effort before solving full extraction.

## Phase 2: extraction and validation MVP

### Goals

- Extract structured fields from PDFs.
- Add OCR for scanned documents.
- Produce canonical JSON.
- Validate required fields.
- Flag exceptions for human review.

### Outputs

- Extraction pipeline.
- Canonical schema v1.
- Validation rules v1.
- Field-level confidence and evidence.
- Review queue/export.

### Value

This phase reduces manual reading and re-keying but preserves human control.

## Phase 3: human review workflow

### Goals

- Let staff correct/approve extracted fields.
- Capture review events and corrections.
- Prepare approved records for EVA.

### Outputs

- Review UI or controlled review spreadsheet.
- Review audit trail.
- Correction feedback loop.
- Approval gate.

### Value

This phase creates a safe bridge between AI extraction and system-of-record updates.

## Phase 4: EVA integration

### Goals

- Map approved canonical data to EVA JSON.
- Submit/import into EVA.
- Capture EVA responses/errors.
- Prevent duplicate EVA records.

### Outputs

- EVA adapter.
- EVA payload schema/mapping version.
- EVA submission log.
- Error handling and retry rules.

### Value

This phase reduces manual EVA data entry and closes the main automation loop.

## Phase 5: production hardening

### Goals

- Improve reliability, monitoring, and supportability.
- Formalise security and data controls.
- Train operations staff.

### Outputs

- Dashboards.
- Alerts.
- Runbooks.
- Access review.
- Retention rules.
- Backup/recovery plan.

## Phase 6: expansion

### Goals

- Increase auto-approval where evidence supports it.
- Add more document types/suppliers.
- Build broader automation-centre capabilities.
- Replace spreadsheet dependency if appropriate.

### Outputs

- Additional parsers/templates.
- Automation metrics.
- Better review UI.
- Additional EVA update operations.
- Cross-system dashboards.

## Suggested MVP scope

The strongest MVP is:

1. Dedicated intake mailbox/folder.
2. Automatic attachment capture.
3. Box storage with metadata.
4. Basic extraction for a known PDF template.
5. Review-required by default.
6. EVA JSON generation but not fully autonomous submission until mapping and review are proven.

## Implementation dependencies

| Dependency | Owner to confirm |
|---|---|
| Microsoft 365 app registration and mailbox access | M365 admin/technical owner |
| Box API credentials and root folder | Box admin |
| EVA JSON/API documentation | EVA owner/vendor |
| Current spreadsheet field definitions | Operations/business owner |
| Sample documents | Operations |
| Data handling/privacy requirements | Data/privacy owner |

## Build vs buy considerations

### Build custom pipeline

Best when:

- EVA integration is custom.
- Data model and audit requirements are specific.
- Long-term automation centre capabilities matter.

### Use low-code tools

Useful for early pilots or simple routing:

- Power Automate for Outlook/Box-like workflows if connectors fit.
- Box automation features if licensing supports them.

Risks:

- Harder custom extraction and complex state handling.
- Harder testability/versioning for mission-critical pipelines.

## First technical spike list

1. Read an email and attachment through Microsoft Graph.
2. Upload a PDF and image to Box via API.
3. Apply Box metadata to a file/folder.
4. Extract text from a representative PDF.
5. OCR a scanned representative PDF.
6. Produce canonical JSON for one sample.
7. Generate an EVA JSON payload for one sample.
8. Submit/import to EVA sandbox or test route.

## Rollout strategy

- Start with a narrow document class and controlled mailbox.
- Run in shadow mode: automation extracts and proposes, human still processes manually.
- Compare automation output against human output.
- Move to assisted mode: human reviews automation output and approves EVA import.
- Move to auto-submit only for cases with proven reliability and low risk.
