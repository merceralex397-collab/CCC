# Project Brief

## Confirmed context

Collision Engineers is building a full automation centre. The initial automation target is a document-intake and case-data-entry workflow involving:

- Outlook email intake.
- Box file storage.
- EVA, a niche business system that can accept JSON imports and may expose an API.
- PDF files received by email.
- Images that may arrive in the same email or in a separate email.
- A spreadsheet that currently acts as a human-maintained data capture/control layer.

A human currently reads the PDF, extracts the relevant data, adds the data to a spreadsheet, manually stores/uploads files to Box, and manually enters or imports data into EVA. The project objective is to automate as much of that process as possible.

## Working objective

Build a reliable intake-to-EVA automation pipeline that can:

1. Detect relevant incoming Outlook emails.
2. Retrieve PDFs and images from those emails.
3. Correlate PDFs and related image emails into a single work item where possible.
4. Store source files in Box using predictable folders, names, and metadata.
5. Extract structured data from PDFs and, where useful, images.
6. Validate the extracted data against business rules.
7. Preserve a human review path for low-confidence, incomplete, contradictory, or high-risk cases.
8. Update a spreadsheet or replacement control table with status and extracted values.
9. Import validated data into EVA using JSON and preferably an API if available.
10. Maintain an auditable trail from original email to Box files to extracted data to EVA import result.

## Business outcomes

The automation should reduce manual re-keying, reduce missed attachments, reduce inconsistent Box storage, improve visibility of case status, and create a repeatable data pipeline that can support future automations.

## Target users

- Operations staff who currently process incoming PDFs and images.
- Administrators who maintain the spreadsheet and/or EVA records.
- Managers who need visibility of intake volume, exceptions, and throughput.
- Developers/automation builders who will maintain the automation centre.

## Non-goals for the first build

These are not excluded forever, but they should not block the first production-grade workflow:

- Fully autonomous processing of every possible document variation.
- Replacing EVA as the system of record.
- Removing human review entirely.
- Building a large custom case-management UI before the workflow is proven.
- Training a custom machine-learning model before simpler extraction approaches are tested.
- Solving every historical/backlog document migration before the new intake workflow works.

## Recommended first success criteria

A first production milestone should be considered successful when:

- New relevant emails can be detected automatically.
- PDFs and related images are captured and stored in Box without manual upload.
- A canonical work item is created for each case/intake.
- Key fields are extracted from PDFs with recorded confidence and traceability.
- Human reviewers can correct low-confidence fields before EVA import.
- EVA receives a valid JSON import for reviewed/approved work items.
- Every work item has a clear status: received, stored, extracted, needs review, approved, imported, failed, or archived.
- Failures do not disappear; they enter a visible retry or review queue.

## Quality principles

The automation centre should prefer correctness and traceability over raw automation rate. For a business process involving case files, claim information, images, and operational records, the best design is not simply “AI reads everything and posts to EVA.” The safer design is a controlled pipeline where the original source files are preserved, extraction is explainable, validation is explicit, and humans review exceptions.

## Practical implementation bias

Use simple, composable components first:

- Microsoft Graph for Outlook mailbox access and change notifications.
- Box API for file storage and metadata where licensed/available.
- A structured extraction service for PDF/OCR/AI extraction.
- A canonical JSON schema between extraction and EVA.
- A queue/state table for orchestration and audit.
- A lightweight review UI or review spreadsheet before a heavier custom portal.

## Core project risk

The biggest project risk is not the AI extraction itself. The bigger risk is uncontrolled variation: many email formats, inconsistent PDF templates, images arriving separately, unknown EVA constraints, and manual exceptions that staff currently solve informally. The first build should expose those variations rather than hiding them.
