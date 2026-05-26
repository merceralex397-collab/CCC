# Data Model and JSON Contracts

## Purpose

Define a canonical data model that sits between source documents and EVA. This model should be stable even if the PDF templates, spreadsheet columns, or EVA import details change.

## Why a canonical model matters

Without a canonical model, every parser and automation step becomes directly tied to EVA. That creates brittle code. A canonical model creates a clean boundary:

```text
PDF/email/images -> extraction -> canonical JSON -> validation/review -> EVA-specific JSON
```

## Canonical work item model

```json
{
  "work_item_id": "WI-20260522-000123",
  "schema_version": "1.0.0",
  "status": "extracted",
  "source": {
    "email": {
      "mailbox": "intake@example.com",
      "graph_message_id": "...",
      "internet_message_id": "...",
      "conversation_id": "...",
      "subject": "...",
      "sender_email": "sender@example.com",
      "received_at": "2026-05-22T10:15:00Z"
    },
    "box": {
      "folder_id": "123456789",
      "folder_url": "https://box.example/..."
    }
  },
  "documents": [
    {
      "document_id": "DOC-001",
      "role": "source_pdf",
      "original_filename": "report.pdf",
      "box_file_id": "987654321",
      "checksum_sha256": "...",
      "content_type": "application/pdf"
    }
  ],
  "case": {
    "case_reference": null,
    "claim_reference": null,
    "instruction_reference": null,
    "received_date": "2026-05-22",
    "document_type": null
  },
  "parties": {
    "client": {
      "name": null,
      "email": null,
      "phone": null
    },
    "insurer": {
      "name": null,
      "reference": null
    },
    "solicitor": {
      "name": null,
      "reference": null
    }
  },
  "vehicle": {
    "registration": null,
    "make": null,
    "model": null,
    "vin": null,
    "mileage": null
  },
  "incident": {
    "date": null,
    "location": null,
    "description": null
  },
  "inspection": {
    "date": null,
    "engineer": null,
    "location": null
  },
  "extraction": {
    "method": "pdf_text_ocr_ai",
    "overall_confidence": 0.0,
    "fields": {}
  },
  "review": {
    "required": true,
    "status": "not_started",
    "reviewer": null,
    "reviewed_at": null
  },
  "eva": {
    "status": "not_submitted",
    "payload_version": null,
    "eva_record_id": null,
    "last_error": null
  }
}
```

## Field-level extraction object

Every extracted field should carry value, confidence, source, and validation state.

```json
{
  "value": "AB12CDE",
  "confidence": 0.94,
  "status": "accepted",
  "source": {
    "document_id": "DOC-001",
    "page": 1,
    "method": "regex_after_pdf_text",
    "evidence": "Vehicle Reg: AB12CDE"
  },
  "normalized_value": "AB12 CDE",
  "validation": {
    "rules_passed": ["uk_vehicle_registration_format"],
    "rules_failed": []
  }
}
```

## Spreadsheet mapping

The exact spreadsheet columns must be confirmed. Until then, use a mapping file rather than hard-coded column positions.

Example mapping:

```json
{
  "spreadsheet_version": "current-manual-v1",
  "columns": {
    "A": "work_item_id",
    "B": "received_at",
    "C": "sender_email",
    "D": "case.case_reference",
    "E": "vehicle.registration",
    "F": "box.folder_url",
    "G": "review.status",
    "H": "eva.status",
    "I": "eva.last_error"
  }
}
```

## EVA payload boundary

The EVA payload should be generated from approved canonical data only.

Example EVA-shaped payload placeholder:

```json
{
  "externalReference": "WI-20260522-000123",
  "caseReference": "TBC",
  "receivedDate": "2026-05-22",
  "vehicle": {
    "registration": "AB12 CDE",
    "make": "TBC",
    "model": "TBC"
  },
  "documents": [
    {
      "role": "source_pdf",
      "boxFileId": "987654321",
      "fileName": "report.pdf"
    }
  ]
}
```

This is not the final EVA schema. It is a placeholder until EVA documentation is confirmed.

## Validation rules

Validation should be defined as data/configuration where practical.

Example:

```json
{
  "ruleset_version": "2026-05-22",
  "required_fields_for_eva": [
    "work_item_id",
    "source.email.received_at",
    "documents[role=source_pdf].box_file_id",
    "vehicle.registration"
  ],
  "format_rules": {
    "vehicle.registration": "uk_vehicle_registration_or_manual_review",
    "incident.date": "date_iso_8601"
  }
}
```

## Schema versioning

Use semantic versioning for the canonical schema:

- Patch: non-breaking clarification or optional field.
- Minor: additive field that does not break consumers.
- Major: breaking field rename/removal/meaning change.

Example versions:

```text
canonical-work-item/1.0.0
eva-mapping/1.0.0
spreadsheet-mapping/1.0.0
validation-rules/1.0.0
```

## Database tables or collections

A simple relational design:

| Table | Purpose |
|---|---|
| `work_items` | One row per intake/case. |
| `source_emails` | Email metadata. |
| `documents` | Box/file metadata for PDFs/images. |
| `extracted_fields` | Field-level extraction values and confidence. |
| `reviews` | Human corrections and approvals. |
| `eva_submissions` | Payloads, attempts, and responses. |
| `events` | Immutable audit log. |

## Event log object

```json
{
  "event_id": "EVT-000001",
  "work_item_id": "WI-20260522-000123",
  "event_type": "files_stored",
  "created_at": "2026-05-22T10:20:00Z",
  "actor": "automation-service",
  "details": {
    "box_folder_id": "123456789",
    "file_count": 3
  }
}
```

## Data model open questions

- Exact spreadsheet columns.
- Exact EVA field requirements.
- Whether images need structured metadata or only storage links.
- Whether there are multiple case/document types requiring different required fields.
- Whether customer/client/vehicle fields include sensitive categories that need additional controls.
- Whether there is an existing unique reference number in every PDF.
