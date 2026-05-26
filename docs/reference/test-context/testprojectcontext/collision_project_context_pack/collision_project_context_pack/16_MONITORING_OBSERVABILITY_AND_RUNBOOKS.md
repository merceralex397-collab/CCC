# Monitoring, Observability, and Runbooks

## Purpose

Define how the automation centre will be monitored and supported after launch.

## Monitoring objectives

The system should answer these questions quickly:

- Are emails being detected?
- Are attachments being captured?
- Are files reaching Box?
- Is extraction working?
- How many items need review?
- Are EVA imports succeeding?
- What is stuck and why?
- Are error rates increasing?

## Dashboard sections

### Intake

- Emails detected today.
- Emails ignored by rule.
- Emails with no attachments.
- Duplicate emails detected.
- Unmatched image emails.

### Storage

- Files uploaded to Box today.
- Box upload failures.
- Metadata failures.
- Average upload time.

### Extraction

- Documents extracted.
- Extraction failures.
- OCR-required percentage.
- Average extraction confidence.
- Unknown document templates.

### Review

- Items needing review.
- Oldest item needing review.
- Items reviewed today.
- Top validation failure reasons.

### EVA

- Payloads generated.
- EVA submissions attempted.
- EVA import successes.
- EVA import failures.
- Duplicate prevention events.

## Alerting recommendations

| Alert | Trigger |
|---|---|
| Intake stopped | No email processed in expected business window while mailbox has new relevant mail. |
| Box failures | Consecutive Box upload failures above threshold. |
| Extraction failures | Failure rate above threshold or extraction service unavailable. |
| Review backlog | Needs-review queue exceeds threshold or oldest item exceeds SLA. |
| EVA failures | Consecutive EVA import failures or auth failure. |
| Stuck work items | Work items in same processing state beyond threshold. |

## Log structure

Use structured logs, preferably JSON.

Example:

```json
{
  "timestamp": "2026-05-22T10:30:00Z",
  "level": "INFO",
  "service": "extraction-worker",
  "work_item_id": "WI-20260522-000123",
  "event": "extraction_completed",
  "duration_ms": 4200,
  "document_count": 1,
  "overall_confidence": 0.91
}
```

## Correlation IDs

Use the work item ID as the main correlation ID across all logs, state records, Box metadata, and EVA payloads.

## Runbook: Box upload failure

1. Check whether the Box API/service account is available.
2. Check whether the target root folder exists and permissions are intact.
3. Check whether file size/type is supported.
4. Retry if error is temporary.
5. If permission/configuration issue, escalate to Box admin.
6. Ensure the work item remains visible as `failed_retryable` or `failed_terminal`.

## Runbook: extraction failure

1. Open the source PDF/image from Box.
2. Check file corruption/password protection.
3. Check whether PDF has text or requires OCR.
4. Review extraction service logs.
5. Rerun extraction if temporary.
6. Mark as `needs_review` if the document is readable by a human but not by automation.
7. Add sample to test corpus if it represents a new template or failure mode.

## Runbook: unmatched image email

1. Check sender, subject, time window, and conversation/thread.
2. Search for candidate work items by sender/reference/date.
3. If confident, attach/link the image to the work item.
4. If not confident, leave in unmatched queue and request human decision.
5. Record the association decision for future rule improvement.

## Runbook: EVA import failure

1. Inspect EVA response/error code.
2. Determine category: auth, schema, business validation, duplicate, temporary outage.
3. If temporary, retry according to policy.
4. If schema/business validation, send to review or fix mapping.
5. If duplicate, link to existing EVA record or escalate.
6. Preserve payload and response in the work item folder.

## Runbook: suspected duplicate work item

1. Compare internet message ID.
2. Compare attachment checksums.
3. Compare extracted case/reference number.
4. Compare sender and received timestamp.
5. Check EVA for existing record if API/search exists.
6. Link/merge only according to business-approved rules.

## Operational report

A daily report could include:

```text
Date: 2026-05-22
Emails received: 42
Work items created: 38
Files stored in Box: 114
Extractions completed: 35
Needs review: 9
EVA imports successful: 24
EVA failures: 2
Unmatched images: 3
Top failure reason: missing vehicle registration
```

## Support ownership

Define owners before production:

- Primary technical support.
- Backup technical support.
- Operations review owner.
- Box admin contact.
- Microsoft 365 admin contact.
- EVA vendor/support contact.
