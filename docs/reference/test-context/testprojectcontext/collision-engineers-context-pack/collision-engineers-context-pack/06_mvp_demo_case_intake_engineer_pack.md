# 06 — MVP Demo: AI Case Intake + Engineer Pack Generator

Generated: 2026-05-22

## Demo title

**AI Case Intake + Engineer Pack Generator**

## Demo thesis

The demo should prove one business value:

> “I can turn messy inbound files into a clean engineer-ready case file.”

Do not try to prove full report automation, image-based repair costing or live external integrations in the first demo.

## Demo inputs

The first demo should accept manual uploads:

- instruction PDF;
- Audatex or repair estimate PDF;
- repair invoice or supporting PDF;
- vehicle images;
- pasted email/WhatsApp/admin text;
- optional existing holding-pen CSV.

Manual upload is enough for the demo because it proves the processing layer without requiring access to their real inbox, WhatsApp, portal or API.

## Demo outputs

| Output | What it proves |
|---|---|
| Structured case record | The AI can read messy instructions and populate fields. |
| Evidence matching view | The system can suggest which files belong together. |
| Holding-pen status | The dashboard can replace or augment the spreadsheet. |
| Missing-information flags | The system can identify why a case is blocked. |
| Engineer-ready pack | The system can produce useful work product. |
| Draft chaser message | The system can reduce routine admin writing. |
| Audit log | The system can support traceability. |

## Minimum feature set

Build only these first:

1. Upload files.
2. Classify PDFs/images/notes.
3. Extract key fields from instruction PDFs.
4. Parse key fields from estimate PDFs.
5. Match documents/images into a case.
6. Show holding-pen status.
7. Flag missing or inconsistent evidence.
8. Generate an engineer-ready pack.
9. Draft a missing-information email/message.
10. Record an activity log.

## Suggested demo stack

| Layer | Demo recommendation | Production alternative |
|---|---|---|
| Frontend | Next.js / React | Same, with auth and RBAC. |
| Backend | FastAPI or Node/Express | FastAPI/Node with queue workers. |
| Database | SQLite | Postgres/Supabase/Azure SQL. |
| File storage | Local `/uploads` | S3, Azure Blob, Supabase Storage or SharePoint. |
| PDF parsing | PyMuPDF/pdfplumber | Add OCR for scanned PDFs. |
| OCR | Optional in demo | Azure AI Document Intelligence, AWS Textract, Google Document AI, Tesseract depending budget/governance. |
| AI | OpenAI/Claude/Gemini API | Provider chosen after data governance review. |
| PDF export | HTML-to-PDF | Branded template/PDF renderer. |

## What the demo should show on-screen

### Screen 1 — Holding pen

A dashboard table/cards with:

- status;
- vehicle registration;
- claim reference;
- report type;
- missing items;
- confidence;
- assigned engineer;
- next recommended action.

### Screen 2 — Upload

Drag-and-drop area for PDFs/images and a text box for loose notes.

### Screen 3 — Processing results

Show what was extracted:

- vehicle registration;
- VIN;
- claim reference;
- client/work provider;
- report type;
- date of loss;
- location;
- inspection type;
- urgency;
- special instructions;
- confidence.

### Screen 4 — Evidence matching

Show each file with:

- filename;
- detected type;
- extracted registration/reference;
- match confidence;
- reason for match;
- approve/reject controls.

### Screen 5 — Engineer pack preview

Generate a markdown/HTML pack with editable sections.

## Example engineer pack skeleton

```markdown
# Engineer Assessment Pack

## Case Summary
Vehicle: AB12 CDE  
Report Type: Desktop damage assessment  
Claim Reference: CLM-12345  
Instruction Source: Solicitor / insurer / repairer  
Current Status: Ready for engineer

## Documents Received
- Instruction PDF
- Audatex estimate
- 8 vehicle images

## Instruction Summary
[AI-generated factual summary, source-linked]

## Estimate Summary
Parts: £...  
Labour: £...  
Paint: £...  
VAT: £...  
Total: £...

## Image Schedule
1. Front nearside damage
2. Rear quarter view
3. Odometer / interior

## Missing / Uncertain Items
- No clear rear offside image.
- Estimate reg matches instruction, but claim ref not found in estimate.

## Questions for Engineer
- Confirm whether visible damage is consistent with the instruction.
- Review estimate for ADAS/alignment requirements.
- Confirm whether desktop assessment is sufficient or physical inspection required.
```

## Demo data should be synthetic

Use fake but realistic documents:

1. **Good complete case** — instruction + estimate + matching photos.
2. **Missing-images case** — instruction + estimate but insufficient photos.
3. **Mismatched-reg case** — instruction reg does not match estimate reg.
4. **Duplicate case** — same registration/claim ref appears twice.
5. **Supplementary estimate case** — estimate marked as supplementary.
6. **Unknown document case** — unrelated attachment to show the classifier can refuse.

Do not use real claimant/client data in the first demo.

## Acceptance criteria

The first demo passes if:

- it accepts mixed uploads;
- it classifies at least instruction PDF, estimate PDF, image and unknown document;
- it extracts vehicle registration and at least five other useful fields;
- it creates or updates a case record;
- it shows missing evidence clearly;
- it gives match reasons, not only a confidence number;
- it allows admin approval/rejection;
- it generates an engineer pack;
- it logs every major step;
- it does not claim to produce a final expert opinion.

## Demo narrative

Use this line when presenting:

> “This does not automate the engineer’s opinion. It automates the admin and preparation layer: reading incoming documents, matching evidence, flagging missing information, and producing a clean pack for human review.”

## First milestone

A local web app that accepts one instruction PDF, one estimate PDF and a set of images, then produces a structured case record and an engineer pack.
