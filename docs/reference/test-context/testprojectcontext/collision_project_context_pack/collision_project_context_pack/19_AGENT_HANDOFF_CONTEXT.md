# Agent Handoff Context

Use this file to quickly brief a future AI assistant, developer, or automation agent.

## Compact project context

Collision Engineers is building an automation centre. The first major workflow is to automate document intake from Outlook into Box, extract data from PDFs/images, update a control spreadsheet or state store, and import structured data into EVA.

Current manual process:

1. PDFs arrive by email.
2. Images may arrive in the same email or a separate email.
3. A human reads the PDF.
4. A human adds data to a spreadsheet.
5. A human uploads/stores the file in Box.
6. A human manually adds/imports data into EVA.

Goal:

Automate as much as possible while preserving auditability and human review for uncertain cases.

## Core systems

- Outlook: email intake.
- Box: file/document storage.
- EVA: destination business system, accepts JSON imports and may have an API.
- Spreadsheet: current tracking/data-entry surface; likely should become temporary control/review layer.

## Recommended architecture

Use a stateful workflow:

```text
Outlook intake -> work item -> Box storage -> extraction -> validation -> human review if needed -> EVA JSON/import -> audit/status update
```

Key design decisions:

- Use a canonical internal JSON model before mapping to EVA.
- Preserve original PDFs/images in Box.
- Use work item IDs across systems.
- Use field-level confidence and evidence for extraction.
- Use human review for low-confidence, missing, conflicting, duplicate, or unmatched cases.
- Avoid duplicate EVA records with idempotency controls.

## Critical unknowns

- Exact EVA JSON/API/import contract.
- Exact spreadsheet columns.
- Required EVA fields.
- Current Box folder structure and permission model.
- Outlook mailbox/folder to monitor.
- PDF templates and document variation.
- Frequency/pattern of separate image emails.
- Data retention/privacy requirements.

## Suggested next action for a future assistant

Do not start with code. First ask for or inspect:

1. Example PDF(s).
2. Example email(s), including separate image emails.
3. Current spreadsheet template.
4. EVA JSON import documentation or sample accepted JSON.
5. Box folder structure expectations.

Then produce:

- Field inventory.
- Canonical schema v1.
- EVA mapping v1.
- MVP implementation plan.
- Test corpus and acceptance criteria.

## Safe defaults

- Review-required by default for extracted records until measured accuracy is high.
- No deletion of source emails or files.
- No automatic EVA submission without approval until EVA sandbox tests and duplicate prevention are proven.
- Log and surface all failures.
- Treat source files as audit evidence.

## Example future prompt

```text
You are helping with the Collision Engineers automation centre. We need to automate Outlook PDF/image intake, Box storage, data extraction, spreadsheet/control-table updates, and EVA JSON/API import. Use a canonical JSON model, preserve audit trail, include human review for low-confidence records, and avoid duplicate EVA submissions. First inspect the sample files/spreadsheet/EVA schema, then propose the minimal implementation and tests.
```
