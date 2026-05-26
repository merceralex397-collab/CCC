# 09 — Data Model and Schemas

Generated: 2026-05-22

## Design goal

The data model should preserve three things:

1. **Case state** — what matter this is and where it sits in the workflow.
2. **Evidence traceability** — which source files support each field or conclusion.
3. **Human review** — who approved matches, edited packs and issued reports.

## Core entities

```text
Case
Document
ImageEvidence
Estimate
MatchSuggestion
MissingItem
ReviewFlag
EngineerPack
MessageDraft
AuditEvent
AIRun
User
Engineer
Template
```

## Case

```ts
interface Case {
  id: string
  status: CaseStatus
  vehicleReg?: string
  vin?: string
  vehicleMake?: string
  vehicleModel?: string
  claimRef?: string
  clientRef?: string
  audatexRef?: string
  clientName?: string
  workProvider?: string
  reportType?: ReportType
  inspectionType?: InspectionType
  dateOfLoss?: string
  location?: string
  urgency?: "normal" | "urgent" | "same_day" | "unknown"
  assignedEngineerId?: string
  confidence: number
  missingItemIds: string[]
  reviewFlagIds: string[]
  documentIds: string[]
  imageIds: string[]
  estimateIds: string[]
  createdAt: string
  updatedAt: string
  archivedAt?: string
}
```

## Enums

```ts
type CaseStatus =
  | "new_instruction"
  | "awaiting_images"
  | "awaiting_estimate"
  | "awaiting_instruction"
  | "possible_duplicate"
  | "needs_admin_review"
  | "ready_for_engineer"
  | "engineer_booked"
  | "pack_generated"
  | "report_issued"
  | "archived"

type ReportType =
  | "damage_assessment"
  | "valuation"
  | "diminution"
  | "roadworthy"
  | "forensic"
  | "criminal"
  | "audatex_estimate"
  | "unknown"

type InspectionType =
  | "desktop"
  | "physical"
  | "unknown"
```

## Document

```ts
interface Document {
  id: string
  caseId?: string
  type: DocumentType
  filename: string
  originalFilename: string
  mimeType: string
  fileSize: number
  checksum: string
  storagePath: string
  extractedTextPath?: string
  extractedFields?: Record<string, unknown>
  sourceChannel?: "upload" | "email" | "whatsapp" | "portal" | "api"
  sourceSender?: string
  sourceSubject?: string
  uploadBatchId?: string
  confidence: number
  createdAt: string
  processedAt?: string
}

type DocumentType =
  | "instruction_pdf"
  | "audatex_estimate"
  | "repair_estimate"
  | "repair_invoice"
  | "valuation_evidence"
  | "engineer_report"
  | "email_note"
  | "image"
  | "unknown"
```

## ImageEvidence

```ts
interface ImageEvidence {
  id: string
  caseId?: string
  documentId: string
  filename: string
  storagePath: string
  thumbnailPath?: string
  imageRole?: ImageRole
  qualityScore?: number
  exifDateTaken?: string
  detectedVehicleReg?: string
  detectedDamageZones?: string[]
  matchConfidence?: number
  notes?: string
}

type ImageRole =
  | "front_view"
  | "rear_view"
  | "nearside_view"
  | "offside_view"
  | "damage_closeup"
  | "odometer"
  | "vin_plate"
  | "interior"
  | "unknown"
```

## Estimate

```ts
interface Estimate {
  id: string
  caseId?: string
  documentId: string
  estimateType: "audatex" | "repairer_pdf" | "invoice" | "unknown"
  estimateRef?: string
  repairerName?: string
  insurerName?: string
  workProvider?: string
  vehicleReg?: string
  vin?: string
  estimateDate?: string
  partsTotal?: number
  labourTotal?: number
  paintTotal?: number
  specialistTotal?: number
  vatTotal?: number
  grandTotal?: number
  valuation?: number
  supplementaryDetected: boolean
  adasKeywordsDetected: string[]
  alignmentKeywordsDetected: string[]
  safetyKeywordsDetected: string[]
  operations: EstimateOperation[]
  flags: ReviewFlag[]
  confidence: number
}

interface EstimateOperation {
  section?: string
  description: string
  operationType?: "repair" | "replace" | "remove_refit" | "paint" | "blend" | "align" | "calibrate" | "diagnostic" | "misc" | "unknown"
  quantity?: number
  labourHours?: number
  partNumber?: string
  cost?: number
}
```

## MatchSuggestion

```ts
interface MatchSuggestion {
  id: string
  caseId: string
  evidenceId: string
  evidenceType: "document" | "image" | "estimate" | "note"
  confidence: number
  reasons: MatchReason[]
  status: "suggested" | "approved" | "rejected" | "expired"
  reviewedBy?: string
  reviewedAt?: string
}

interface MatchReason {
  type:
    | "vehicle_reg_match"
    | "vin_match"
    | "claim_ref_match"
    | "client_ref_match"
    | "audatex_ref_match"
    | "filename_match"
    | "same_upload_batch"
    | "sender_match"
    | "timestamp_proximity"
    | "semantic_similarity"
    | "manual"
  value: string
  weight: number
}
```

## MissingItem

```ts
interface MissingItem {
  id: string
  caseId: string
  itemType:
    | "instruction_pdf"
    | "vehicle_images"
    | "front_image"
    | "rear_image"
    | "nearside_image"
    | "offside_image"
    | "damage_closeup"
    | "odometer_image"
    | "vin_image"
    | "estimate"
    | "claim_ref"
    | "date_of_loss"
    | "location"
    | "valuation_data"
    | "repair_invoice"
    | "other"
  description: string
  severity: "blocking" | "warning" | "optional"
  status: "open" | "requested" | "received" | "waived"
  createdAt: string
  resolvedAt?: string
  resolvedBy?: string
}
```

## ReviewFlag

```ts
interface ReviewFlag {
  id: string
  caseId: string
  sourceId?: string
  sourceType?: "document" | "estimate" | "image" | "system" | "manual"
  category:
    | "reg_mismatch"
    | "claim_ref_mismatch"
    | "possible_duplicate"
    | "supplementary_estimate"
    | "adas_calibration"
    | "alignment_issue"
    | "srs_airbag"
    | "manual_misc_charge"
    | "abp_charge_review"
    | "high_repair_cost"
    | "possible_total_loss"
    | "image_quality"
    | "metadata_issue"
    | "other"
  description: string
  severity: "low" | "medium" | "high"
  status: "open" | "resolved" | "dismissed"
  createdBy: "ai" | "user" | "system"
  createdAt: string
  resolvedAt?: string
  resolvedBy?: string
}
```

## EngineerPack

```ts
interface EngineerPack {
  id: string
  caseId: string
  version: number
  status: "draft" | "locked" | "exported"
  markdown: string
  htmlPath?: string
  pdfPath?: string
  generatedBy: "ai" | "user"
  generatedAt: string
  editedBy?: string
  editedAt?: string
  sourceDocumentIds: string[]
  sourceImageIds: string[]
  unresolvedMissingItemIds: string[]
  unresolvedReviewFlagIds: string[]
}
```

## MessageDraft

```ts
interface MessageDraft {
  id: string
  caseId: string
  type: "missing_info_chaser" | "acknowledgement" | "ready_for_engineer" | "report_cover" | "other"
  channel: "email" | "whatsapp" | "internal_note"
  subject?: string
  body: string
  status: "draft" | "copied" | "sent_externally" | "discarded"
  generatedAt: string
  approvedBy?: string
  approvedAt?: string
}
```

## AuditEvent

```ts
interface AuditEvent {
  id: string
  caseId?: string
  actorType: "user" | "ai" | "system"
  actorId?: string
  action: string
  targetType: string
  targetId?: string
  before?: Record<string, unknown>
  after?: Record<string, unknown>
  metadata?: Record<string, unknown>
  createdAt: string
}
```

## AIRun

```ts
interface AIRun {
  id: string
  caseId?: string
  documentId?: string
  module:
    | "document_classifier"
    | "instruction_extractor"
    | "estimate_parser"
    | "evidence_matcher"
    | "missing_info_checker"
    | "chaser_drafter"
    | "engineer_pack_generator"
  modelProvider: string
  modelName: string
  promptVersion: string
  inputSummary: string
  outputJson: Record<string, unknown>
  confidence?: number
  createdAt: string
}
```

## Example case JSON

```json
{
  "id": "case_001",
  "status": "needs_admin_review",
  "vehicleReg": "AB12 CDE",
  "claimRef": "CLM-12345",
  "workProvider": "Example Solicitors LLP",
  "reportType": "damage_assessment",
  "inspectionType": "desktop",
  "dateOfLoss": "2026-05-04",
  "confidence": 82,
  "missingItemIds": ["missing_rear_image"],
  "reviewFlagIds": ["flag_claim_ref_not_in_estimate"],
  "documentIds": ["doc_instruction", "doc_estimate"],
  "imageIds": ["img_front", "img_damage_closeup"],
  "estimateIds": ["est_001"],
  "createdAt": "2026-05-22T10:30:00Z",
  "updatedAt": "2026-05-22T10:42:00Z"
}
```

## Implementation note

The model should not treat extracted fields as unquestionable facts. Every extracted field should retain:

- source document ID;
- source page or text snippet where possible;
- confidence;
- last human correction;
- audit history.
