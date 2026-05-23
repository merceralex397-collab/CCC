# Automation Centre Operating Model

## Purpose

Frame the Collision Engineers workflow as the first capability in a broader automation centre.

## Automation centre concept

The automation centre is a set of reusable services, patterns, and governance practices that allow Collision Engineers to automate operational workflows safely.

Instead of building one-off scripts, the centre should create reusable capabilities:

- Email intake.
- File capture and storage.
- Document extraction.
- Human review.
- System integration.
- Audit logging.
- Monitoring.
- Exception handling.

## Reusable platform capabilities

### Intake connectors

- Outlook email monitoring.
- Attachment extraction.
- Future connectors for web forms, portals, SFTP, or Box drop folders.

### Document services

- File type detection.
- PDF text extraction.
- OCR.
- Structured extraction.
- Document classification.
- Evidence mapping.

### Workflow engine

- Work item state machine.
- Retry policies.
- Exception routing.
- SLA tracking.

### Integration adapters

- EVA adapter.
- Box adapter.
- Spreadsheet/control-table adapter.
- Future system adapters.

### Governance and audit

- Role-based access.
- Immutable event log.
- Retention policy hooks.
- Review history.

### Observability

- Dashboard.
- Alerts.
- Daily/weekly reporting.
- Volume and failure metrics.

## Suggested repository structure

```text
collision-automation-centre/
  apps/
    intake-service/
    extraction-service/
    review-ui/
    eva-adapter/
  packages/
    canonical-schema/
    validation-rules/
    box-client/
    graph-client/
    eva-client/
    audit-log/
  infra/
    dev/
    test/
    prod/
  docs/
    architecture/
    runbooks/
    data-models/
    decisions/
  tests/
    sample-corpus/
    integration/
    e2e/
```

## Agent/MCP direction

Given the broader interest in AI agents, plugins, MCPs, and automation, the project can eventually expose internal tools to agents. However, agentic automation should be layered on top of deterministic workflow controls.

Plain-English explanation: an **agent** is software that can decide which tool/action to use to complete a task. A **workflow** is a fixed process. For business-critical document intake, use workflows for reliability and agents for assistance, investigation, and operator support.

Potential future agent tools:

- `search_work_item(work_item_id)`
- `find_unmatched_images(reference_or_sender)`
- `summarize_case_documents(work_item_id)`
- `explain_validation_failure(work_item_id)`
- `generate_eva_payload_preview(work_item_id)`
- `create_box_folder_for_work_item(work_item_id)`
- `rerun_extraction(work_item_id, extraction_version)`

## Agent safety boundaries

Agents should not automatically:

- Delete source emails/files.
- Modify original PDFs/images.
- Submit to EVA without approval unless the case meets proven auto-approval rules.
- Override reviewer decisions without audit.
- Access more personal data than necessary.

## Decision records

Use Architecture Decision Records (ADRs) for durable design choices.

Example ADRs:

- Use Microsoft Graph for Outlook integration.
- Use Box as source document store.
- Use canonical JSON model before EVA mapping.
- Require human review for low-confidence extraction.
- Use work item state machine.
- Keep spreadsheet as temporary control view only.

## Operating cadence

### Daily during pilot

- Check failed work items.
- Check unmatched images.
- Check EVA import failures.
- Review extraction corrections.

### Weekly during pilot

- Review automation rate.
- Review top failure reasons.
- Update validation rules.
- Prioritise document templates for improvement.

### Monthly after stabilisation

- Access review.
- Cost review.
- Extraction quality review.
- Data retention and audit check.
- Roadmap planning for next automation.

## Automation centre KPIs

| KPI | Purpose |
|---|---|
| Intake volume | Number of emails/work items processed. |
| Straight-through processing rate | Percentage requiring no human review. |
| Review rate | Percentage requiring human review. |
| Review correction rate | Quality signal for extraction. |
| EVA import success rate | Integration reliability. |
| Average time to Box storage | File capture performance. |
| Average time to EVA import | End-to-end throughput. |
| Top exception reasons | Improvement focus. |
| Duplicate prevention count | Risk reduction. |

## Long-term target

A mature automation centre should make routine intake highly automated while giving staff better control over exceptions, audit, and system health than the current manual process provides.
