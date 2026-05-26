# Exception Handling and Human Review

## Purpose

Design the human-in-the-loop part of the automation so uncertain records are reviewed safely instead of being forced through to EVA.

## Plain-English explanation

A **human-in-the-loop** process means automation handles the repetitive work, but a person reviews items when the system is unsure, data is missing, or the consequences of being wrong are too high.

## Exception categories

| Category | Examples | Default handling |
|---|---|---|
| Intake exception | No PDF, unsupported attachment, duplicate email. | Route to intake review. |
| Correlation exception | Images cannot be matched to a PDF/case. | Route to unmatched files queue. |
| File storage exception | Box upload or metadata failure. | Retry, then technical alert. |
| Extraction exception | OCR unreadable, unknown template, AI invalid JSON. | Route to extraction review. |
| Validation exception | Required field missing or invalid. | Route to business review. |
| Duplicate exception | Same reference already exists. | Route to duplicate resolution. |
| EVA exception | Import rejected or unknown response. | Route to EVA review/technical support. |

## Review queue design

A review queue should show:

- Work item ID.
- Received timestamp.
- Sender.
- Subject.
- Box source folder/file links.
- Extracted fields.
- Field-level confidence.
- Evidence snippets/page references.
- Validation errors.
- Required reviewer action.
- Submit/approve/reject buttons or equivalent workflow.

## Review actions

| Action | Meaning |
|---|---|
| Approve | Data is correct and can proceed to EVA. |
| Correct and approve | Reviewer changes fields, then approves. |
| Request more info | Case cannot proceed; missing source data. |
| Link related image/email | Reviewer associates unmatched files. |
| Mark duplicate | Work item should be linked to existing item. |
| Reject/ignore | Email is not relevant or should not be processed. |
| Escalate technical | Automation/system error needs developer/admin. |

## Reviewer audit trail

Record every reviewer change:

```json
{
  "work_item_id": "WI-20260522-000123",
  "review_event": "field_corrected",
  "field": "vehicle.registration",
  "old_value": "AB12C0E",
  "new_value": "AB12CDE",
  "reviewer": "user@example.com",
  "timestamp": "2026-05-22T11:30:00Z",
  "reason": "OCR misread D as 0"
}
```

## Prioritisation rules

Queue sorting should consider:

- Age of work item.
- SLA or urgency.
- Completeness.
- Whether only one field is missing.
- Whether EVA submission already failed.
- Whether related images are pending.

## Exception SLAs

Define practical service levels:

| Exception | Suggested SLA |
|---|---|
| Needs business review | Same working day or next working day. |
| Technical failure blocking all intake | Immediate alert. |
| Unmatched images | Review after correlation window expires. |
| EVA import rejection | Review within operational SLA. |

## Review UI options

### Spreadsheet-based review

Good for a fast first phase.

Pros:

- Familiar to staff.
- Low build cost.
- Easy to inspect.

Cons:

- Harder audit/control.
- Concurrent edits can be messy.
- Validation UX is limited.

### Lightweight web review app

Recommended medium-term.

Pros:

- Better field validation.
- Better audit trail.
- Better links to Box and EVA.
- Can enforce workflow transitions.

Cons:

- Requires development and hosting.

### EVA-native review

Only suitable if EVA can hold draft records and supports review status.

Pros:

- Keeps users in EVA.

Cons:

- May pollute EVA with incomplete records.
- Depends heavily on EVA capabilities.

## Recommended first review approach

Start with a controlled review surface that can be built quickly but still writes structured review events. A spreadsheet can be acceptable for pilot, but the authoritative state should live in the automation database/control table.

## Quality feedback loop

Reviewer corrections should feed back into extraction improvement:

- OCR misreads become normalization rules.
- Repeated missing fields become parser enhancements.
- New document templates become classification cases.
- Common EVA rejections become pre-validation rules.

## Do not automate these blindly

Avoid automatic EVA submission when:

- Critical fields are low confidence.
- The document type is unknown.
- A duplicate is suspected.
- Images are required but not matched.
- The extracted data conflicts with existing data.
- The source appears corrupted or incomplete.
