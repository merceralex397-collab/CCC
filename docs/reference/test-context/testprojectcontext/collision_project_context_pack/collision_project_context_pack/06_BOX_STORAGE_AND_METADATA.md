# Box Storage and Metadata

## Purpose

Box should act as the controlled document store for original PDFs, related images, extracted artifacts, review outputs, and audit-supporting files.

## Storage principles

1. Preserve original source files.
2. Use predictable folder structures.
3. Avoid overwriting source documents.
4. Store machine-generated outputs separately from human/source evidence.
5. Apply metadata so files can be searched and linked to work items.
6. Design for audit and retention from the start.

## Recommended folder structure

A practical first structure:

```text
Collision Automation/
  Intake/
    YYYY/
      MM/
        workitem_<work_item_id>/
          source/
            original_email_metadata.json
            pdf/
            images/
            other_attachments/
          extracted/
            extraction_raw.json
            extraction_normalized.json
            extraction_confidence.json
          review/
            reviewer_changes.json
            review_notes.md
          eva/
            eva_payload.json
            eva_response.json
          logs/
            processing_log.jsonl
```

Alternative if the business has stable case/reference numbers:

```text
Collision Automation/
  Cases/
    <case_reference>/
      source/
      extracted/
      review/
      eva/
      logs/
```

Use date-based folders first if case/reference extraction is not reliable at initial intake time. The folder can later be renamed or linked after extraction.

## Naming convention

Recommended file naming pattern:

```text
<work_item_id>__<document_role>__<original_filename_sanitized>
```

Examples:

```text
WI-20260522-000123__source_pdf__engineer_report.pdf
WI-20260522-000123__image__vehicle_front_left.jpg
WI-20260522-000123__eva_payload__v1.json
```

## Metadata template recommendation

Create a Box metadata template for work items or files.

Suggested fields:

| Field | Type | Purpose |
|---|---|---|
| `work_item_id` | string | Stable automation ID. |
| `case_reference` | string | Extracted or assigned business reference. |
| `document_role` | enum | `source_pdf`, `supporting_image`, `email_metadata`, `extraction_output`, `eva_payload`, etc. |
| `source_email_id` | string | Link back to Outlook. |
| `sender_email` | string | Originator. |
| `received_at` | date/string | Intake timestamp. |
| `extraction_status` | enum | Current extraction state. |
| `review_status` | enum | Human review state. |
| `eva_status` | enum | EVA import state. |
| `checksum_sha256` | string | Duplicate/evidence control. |
| `retention_class` | enum/string | Retention policy marker. |

## Applying metadata

Box metadata can be applied to files or folders using a metadata template. Use metadata on both the work-item folder and key files where possible.

Folder metadata gives broad searchability. File metadata gives precise traceability.

## Box IDs vs URLs

Store both:

- Box folder/file IDs for API operations.
- Shared/internal URLs for human navigation.

IDs are better for automation. URLs are better for people.

## Checksums

Generate a SHA-256 checksum for each downloaded attachment before or after upload. Store the checksum in the work-item state and Box metadata.

Benefits:

- Detect duplicate attachments.
- Verify file integrity.
- Support audit.

## Versioning and source preservation

Do not edit original files in place. If annotation/redaction is required, create a derivative file in a separate folder such as `review/` or `derived/`.

## Box webhooks

Box webhooks are useful if the process needs to react when files are added, changed, moved, or reviewed inside Box. For the first build, Outlook can be the primary trigger, with Box used as the storage destination. Box webhooks become more useful when staff manually add files to Box and the automation needs to detect them.

## Permission design

Recommended pattern:

- Automation service account: write access to intake folders and metadata.
- Operations staff: read/review access to relevant work-item folders.
- Admins: manage folder templates, permissions, and retention.
- Developers: limited sandbox/test access, not broad production document access unless necessary.

## Retention and archiving

Define retention classes early. Case documents and images may contain personal data or sensitive business data. Retention rules should be reviewed with business/legal/privacy stakeholders.

## Failure handling

| Failure | Handling |
|---|---|
| Folder creation failure | Retry; if persistent, alert and stop downstream processing. |
| Upload failure | Retry with backoff. |
| Metadata apply failure | Do not lose file; flag work item for metadata repair. |
| Duplicate filename | Use work item ID and checksum to avoid collision. |
| Permission failure | Alert; this usually indicates service account or policy drift. |
