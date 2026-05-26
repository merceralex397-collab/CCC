# Outlook Intake

## Purpose

The Outlook intake stage detects relevant incoming emails, captures attachments, and creates a work item for downstream processing.

## Recommended trigger models

### Preferred: Microsoft Graph change notifications

Use Microsoft Graph subscriptions for Outlook messages where feasible. This allows the automation to receive notifications when relevant mail resources change.

### Alternative: scheduled polling

Use scheduled polling if webhooks/change notifications are not available or operationally convenient. Polling is simpler but less efficient and must be designed to avoid missing or duplicating emails.

### Hybrid model

Use change notifications for near-real-time intake and a scheduled reconciliation job as a safety net.

## Mailbox design options

### Dedicated intake mailbox

Example: `intake@collisionengineers.example`

Advantages:

- Cleaner permissions.
- Easier filtering.
- Easier operational monitoring.
- Lower risk of unrelated emails being processed.

Disadvantages:

- Requires suppliers/customers/staff to send documents to the correct mailbox.

### Shared mailbox

Useful if staff already use a team mailbox.

Advantages:

- Fits existing operational behaviour.
- Good for team visibility.

Disadvantages:

- Requires careful permission and folder design.
- Higher chance of mixed email types.

### Personal mailbox monitoring

Not recommended for production unless there is no alternative. It is harder to govern, audit, and support.

## Email classification rules

The intake service should classify emails using configurable rules such as:

- Sender allowlist or domain.
- Subject keyword.
- Recipient mailbox/folder.
- Attachment type: `.pdf`, image formats, `.zip` if used.
- Attachment count.
- Conversation/thread ID.
- Reference number pattern in subject/body.

## Attachment handling rules

### PDF attachments

- Treat PDFs as primary source documents unless business rules say otherwise.
- Store original binary file unmodified.
- Record attachment filename, size, content type, checksum, and email metadata.
- If multiple PDFs exist, either process each separately or classify one as primary and others as supporting documents.

### Image attachments

- Store images in Box with the work item where correlation is clear.
- If an image arrives without a matching PDF, place it into an `awaiting_related_files` status or unmatched queue.
- Capture EXIF metadata only if required and privacy-reviewed.

### ZIP attachments

If ZIP files are possible, define whether they are allowed. If allowed, scan and extract in a controlled environment. Avoid automatically processing nested archives without size, type, and malware controls.

## Separate image email correlation

Images may arrive in a separate email. Correlation should use multiple signals rather than a single brittle rule.

Possible signals:

- Same sender.
- Same email thread/conversation ID.
- Same subject or reference number.
- Same customer/claim/reference number extracted from body or filename.
- Time proximity, for example within a configurable window after the PDF email.
- Staff-forwarded notes.

## Correlation confidence

Use correlation confidence levels:

| Level | Meaning | Action |
|---|---|---|
| High | Reference/thread/sender strongly match. | Attach image to work item automatically. |
| Medium | Some signals match, but not definitive. | Human review or staged pending association. |
| Low | Weak or no clear relationship. | Keep in unmatched queue. |

## Duplicate detection

Deduplicate at multiple levels:

- Email-level: internet message ID and mailbox/folder identity.
- Attachment-level: checksum of file content.
- Work-item-level: extracted case/reference number plus sender/date.
- EVA-level: EVA reference or idempotency key if supported.

## Recommended email metadata to store

```json
{
  "email": {
    "mailbox": "intake@example.com",
    "graph_message_id": "...",
    "internet_message_id": "...",
    "conversation_id": "...",
    "subject": "...",
    "sender_email": "...",
    "sender_name": "...",
    "received_at": "2026-05-22T10:15:00Z",
    "body_preview": "...",
    "has_attachments": true
  }
}
```

## Post-processing mailbox actions

After a message has been captured, apply visible mailbox actions:

- Add category/tag: `Automation - Received`.
- Move to folder: `Processed`, `Needs Review`, or `Rejected` depending on design.
- Do not delete source emails automatically during early phases.

## Failure cases

| Failure | Handling |
|---|---|
| No attachment | Mark `needs_review` or ignore depending on rule. |
| Unsupported file type | Store if required, but flag unsupported. |
| Email too large | Log and alert. |
| Attachment download failure | Retry with backoff. |
| Duplicate email | Link to existing work item, do not create duplicate EVA record. |
| Unmatched images | Place in unmatched queue with search/correlation tools. |

## Implementation notes

- Store the raw email metadata before downstream processing begins.
- Never assume attachments were fully processed just because an email was detected.
- Use a reconciliation job to compare mailbox messages against the work-item store.
- Keep a manual override path so staff can associate unmatched images with a work item.
