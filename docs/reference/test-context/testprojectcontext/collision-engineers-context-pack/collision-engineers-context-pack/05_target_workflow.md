# 05 — Target Workflow

Generated: 2026-05-22

## Target workflow in one line

**Incoming files → AI classification/extraction → evidence matching → missing-info flags → admin review → engineer pack → engineer sign-off.**

## Target workflow diagram

```text
Email / WhatsApp / Portal / API / Upload
        ↓
File intake queue
        ↓
Document and image classification
        ↓
PDF/OCR text extraction
        ↓
Structured case-field extraction
        ↓
Evidence matching and duplicate detection
        ↓
Missing-information checklist
        ↓
Low-confidence admin review
        ↓
Ready-for-engineer status
        ↓
Engineer pack generation
        ↓
Engineer review, judgement and final report approval
```

## Workflow states

| Status | Meaning | Typical next action |
|---|---|---|
| `new_instruction` | Instruction received but not fully processed. | Extract fields; classify files. |
| `awaiting_images` | Instruction/estimate present but required photos are missing. | Generate chaser draft. |
| `awaiting_estimate` | Instruction/photos present but estimate is missing. | Request estimate or continue if not required. |
| `awaiting_instruction` | Images or estimate present but no formal instruction. | Match to existing case or request instruction. |
| `possible_duplicate` | Similar reg/ref/images found elsewhere. | Merge, split or mark not duplicate. |
| `needs_admin_review` | Low confidence or mismatch detected. | Admin approves/rejects match. |
| `ready_for_engineer` | Required evidence is present. | Generate pack and assign engineer. |
| `engineer_booked` | Engineer assigned or inspection arranged. | Await engineer review. |
| `pack_generated` | Engineer pack created. | Engineer reviews/edits. |
| `report_issued` | Final report sent. | Archive with audit trail. |
| `archived` | Closed or test case. | Restore only if needed. |

## Evidence matching logic

The system should combine simple rules with AI-assisted matching.

### Strong identifiers

- vehicle registration;
- VIN;
- claim reference;
- client reference;
- Audatex assessment/estimate ID;
- repairer/work provider name.

### Contextual identifiers

- email sender;
- email subject;
- upload batch;
- timestamp proximity;
- filename clues;
- date of loss;
- vehicle make/model;
- visible registration plate, later phase only;
- image metadata, if available.

## Confidence handling

| Confidence | Suggested behaviour |
|---:|---|
| 95–100% | Auto-attach and mark as high confidence, but log reason. |
| 85–94% | Attach as suggested match; admin can approve quickly. |
| 60–84% | Needs admin review. |
| Below 60% | Do not attach automatically; suggest possible cases only. |

Confidence scores should be shown with match reasons, not hidden.

## Human-in-the-loop checkpoints

A human should approve:

- low-confidence evidence matches;
- case merges/splits;
- any outbound email/WhatsApp communication;
- final engineer pack lock;
- final report issue;
- any fraud, roadworthiness, causation, valuation or repair-method conclusion.

## Engineer pack generation

The pack should contain:

1. Case summary.
2. Instruction summary.
3. Vehicle details.
4. Client/work provider details.
5. Claim/reference details.
6. Date of loss and key dates.
7. Documents received.
8. Image schedule.
9. Estimate/Audatex summary.
10. Missing or uncertain information.
11. Evidence-matching confidence summary.
12. Review flags.
13. Questions for the engineer.
14. Audit trail summary.
15. Draft admin/client message, if needed.

## Activity log requirements

Every important action should generate an audit event:

- file uploaded;
- document classified;
- OCR/text extraction completed;
- field extracted;
- match suggested;
- match approved/rejected;
- missing item flagged;
- chaser draft generated;
- estimate parsed;
- review flag added/resolved;
- engineer pack generated;
- pack edited;
- pack downloaded;
- status changed;
- engineer assigned.

## Exceptions

The system must handle:

- image-only cases;
- scanned PDFs requiring OCR;
- multiple vehicles in one instruction;
- multiple estimates for one vehicle;
- duplicate files;
- supplementary estimates;
- missing registration;
- conflicting registration;
- handwritten or low-quality documents;
- files irrelevant to the case;
- test/demo cases.

## Outcome

The target workflow should make every incoming matter visible, attributable and reviewable. The engineer should not start by searching through emails or loose attachments. They should start from a structured pack and source-linked evidence.
