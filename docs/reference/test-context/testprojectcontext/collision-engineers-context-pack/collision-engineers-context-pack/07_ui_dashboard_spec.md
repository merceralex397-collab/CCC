# 07 — UI Dashboard Specification

Generated: 2026-05-22

## Product framing

The UI should feel like a **case-operation dashboard**, not a generic admin dashboard. Its job is to move a matter from messy intake to engineer-ready pack.

## Core workflow

```text
Incoming files
→ classify documents
→ extract case details
→ match evidence
→ flag missing information
→ admin approves uncertain items
→ generate engineer pack
```

## Main navigation

1. Dashboard / Holding Pen
2. Upload / New Intake
3. Processing Results
4. Case Detail
5. Evidence Matching
6. Estimate / Audatex Review
7. Missing Information / Chaser
8. Engineer Pack Preview
9. Activity Log / Audit
10. Settings / Templates

## 1. Dashboard / Holding Pen

### Purpose

Show all live cases and their current status.

### Top buttons

| Button | Function |
|---|---|
| **Upload Files** | Opens the upload/new intake screen. |
| **Process New Files** | Runs classification/extraction on unprocessed uploads. |
| **Review Low Confidence** | Filters cases below the confidence threshold. |
| **Ready for Engineer** | Shows cases that can have packs generated. |
| **Export Holding Pen** | Downloads the current queue as CSV/Excel-compatible data. |
| **Refresh** | Refreshes statuses and processing results. |

### Status filter chips

- New Instruction
- Awaiting Images
- Awaiting Estimate
- Awaiting Instruction
- Possible Duplicate
- Needs Admin Review
- Ready for Engineer
- Engineer Booked
- Pack Generated
- Report Issued
- Archived

### Case row/card fields

| Field | Example |
|---|---|
| Status | Needs Admin Review |
| Vehicle Reg | AB12 CDE |
| Claim Ref | CLM-12345 |
| Report Type | Desktop damage assessment |
| Missing | Rear image, estimate |
| Confidence | 82% |
| Assigned Engineer | Unassigned |
| Last Activity | Estimate uploaded 10:14 |
| Next Action | Review match |

### Case row buttons

| Button | Function |
|---|---|
| **Open Case** | Opens full case workspace. |
| **Review Match** | Opens evidence matching. |
| **Generate Pack** | Creates engineer pack if complete. |
| **Request Missing Info** | Opens chaser view. |
| **Mark Ready** | Manually marks ready for engineer. |
| **Assign Engineer** | Optional in demo; assigns/recommends engineer. |
| **More** | Merge, split, archive, delete test case, download data. |

## 2. Upload / New Intake View

### Purpose

Allow admin to manually upload files for the prototype.

### Buttons

| Button | Function |
|---|---|
| **Add PDFs** | Upload instruction PDFs, estimates, invoices or repair documents. |
| **Add Images** | Upload vehicle photos. |
| **Add Notes** | Paste email, WhatsApp or admin text. |
| **Use Demo Data** | Loads synthetic demo cases. |
| **Clear Batch** | Removes current batch before processing. |
| **Start Processing** | Runs classification, extraction and matching. |
| **Save as New Case** | Creates a case from the batch. |
| **Link to Existing Case** | Attaches uploaded files to an existing case. |

### Accepted file types for demo

- PDF
- JPG
- PNG
- HEIC, if supported by local environment
- WEBP
- TXT/MD for pasted notes or sample email text

## 3. Intake Processing Results View

### Purpose

Show what the AI extracted before committing it to a case.

### Buttons

| Button | Function |
|---|---|
| **Accept Extracted Details** | Saves extracted data. |
| **Edit Fields** | Manual correction. |
| **Re-run Extraction** | Runs extraction again. |
| **View Source Text** | Shows source text/OCR. |
| **Flag as Unknown** | Marks file for manual review. |
| **Create Case** | Creates a structured case record. |

### Fields displayed

- Vehicle registration
- VIN, if found
- Claim reference
- Client/work provider
- Report type
- Inspection type
- Date of loss
- Vehicle make/model
- Location
- Urgency
- Special instructions
- Missing information
- AI confidence score

## 4. Case Detail View

### Tabs

- Overview
- Documents
- Images
- Estimate
- Evidence Matching
- Missing Information
- Engineer Pack
- Activity Log

### Header buttons

| Button | Function |
|---|---|
| **Edit Case** | Edit core fields. |
| **Change Status** | Manually move case state. |
| **Add Files** | Upload more evidence. |
| **Add Internal Note** | Add admin/engineer note. |
| **Assign Engineer** | Assign or mark unassigned. |
| **Generate Engineer Pack** | Generate pack from current evidence. |
| **Archive Case** | Remove from active queue while retaining record. |

### Overview cards

- Case summary
- Client/work provider
- Vehicle details
- Report type
- Inspection type
- Current status
- AI confidence
- Missing items
- Assigned engineer
- Documents received
- Images received
- Next recommended action

## 5. Evidence Matching View

### Purpose

Show how documents/images are grouped into a case. This is the core workflow screen.

### Buttons

| Button | Function |
|---|---|
| **Auto Match Evidence** | Runs matching across uploaded files. |
| **Approve Match** | Confirms selected files belong to case. |
| **Reject Match** | Removes suggested evidence from case. |
| **Link to Existing Case** | Moves selected evidence elsewhere. |
| **Create New Case from Selection** | Creates a separate case from selected files. |
| **Merge Cases** | Combines suspected duplicates. |
| **Split Case** | Separates incorrectly grouped evidence. |
| **View Match Reasons** | Shows why match was suggested. |
| **Flag for Admin Review** | Marks as requiring manual review. |

### Evidence card fields

- Filename
- File type
- Upload time
- Extracted registration
- Extracted claim reference
- Matched case
- Confidence score
- Reason for match
- Approve/reject buttons

## 6. Estimate / Audatex Review View

### Purpose

Parse estimate documents and surface engineer review prompts.

### Buttons

| Button | Function |
|---|---|
| **Parse Estimate** | Extracts structured estimate data. |
| **Re-run Estimate Parsing** | Runs parser again. |
| **View Original Estimate** | Opens source PDF. |
| **Add Review Flag** | Adds manual concern. |
| **Resolve Flag** | Marks flag handled. |
| **Add Engineer Question** | Adds to engineer pack. |
| **Compare with Instruction** | Checks reg/ref/client consistency. |
| **Send to Evidence Matching** | Moves estimate into matching workflow. |

### Automatic flags

- Vehicle reg mismatch
- Claim ref mismatch
- Estimate present but no images
- Images present but no estimate
- Supplementary estimate detected
- ADAS/calibration keyword detected
- Wheel/suspension issue detected
- SRS/airbag keyword detected
- Manual/miscellaneous line detected
- High repair cost versus valuation
- Possible total-loss marker

## 7. Missing Information / Chaser View

### Purpose

Turn missing evidence into a draft message.

### Buttons

| Button | Function |
|---|---|
| **Generate Chaser Draft** | Drafts email/WhatsApp-style request. |
| **Copy Draft** | Copies text to clipboard. |
| **Mark Requested** | Logs that the item has been requested. |
| **Mark Received** | Marks item as received. |
| **Waive Requirement** | Records that item is not needed. |
| **Add Missing Item** | Manual addition. |
| **Regenerate Draft** | Rewrites after edits. |
| **Add to Engineer Pack** | Includes unresolved items in pack. |

### Missing item examples

- No estimate found
- No instruction PDF found
- No clear front image
- No clear rear image
- No nearside/offside image
- No odometer image
- No VIN/chassis image
- Claim reference missing
- Vehicle reg mismatch
- Date of loss missing
- Client reference missing
- Pre-accident value missing
- Repair authority missing

## 8. Engineer Pack Preview / Generator View

### Buttons

| Button | Function |
|---|---|
| **Generate Engineer Pack** | Builds pack. |
| **Regenerate Pack** | Rebuilds after edits/new evidence. |
| **Edit Pack** | Manual editing. |
| **Regenerate Section** | Rewrites one section. |
| **Add Engineer Question** | Adds review question. |
| **Preview PDF** | Shows export preview. |
| **Download PDF** | Exports pack. |
| **Download Markdown/HTML** | Useful for demo/debugging. |
| **Copy Summary** | Copies short case summary. |
| **Lock Pack** | Marks pack final for that stage. |
| **Send to Engineer** | Later phase; disabled in demo. |

### Pack sections

- Case summary
- Instruction summary
- Vehicle details
- Client/work provider
- Claim reference
- Date of loss
- Documents reviewed
- Image schedule
- Estimate summary
- Audatex/repair estimate notes
- Missing or uncertain information
- AI matching confidence
- Engineer questions
- Draft admin/client message
- Audit trail summary

## 9. Activity Log / Audit View

### Buttons

| Button | Function |
|---|---|
| **View Full Log** | Shows all actions. |
| **Download Audit Log** | CSV/PDF export. |
| **View AI Runs** | Shows extraction/matching/generation runs. |
| **View Prompt/Output** | Debugging and traceability. |
| **Re-run Step** | Re-run classification/extraction/matching/pack generation. |
| **Compare Versions** | Compare pack or extracted-record versions. |

### Log entries

- File uploaded
- Document classified
- PDF text extracted
- Vehicle reg detected
- Claim ref detected
- Estimate parsed
- Images matched
- Missing item flagged
- Admin approved match
- Chaser draft generated
- Engineer pack generated
- Pack downloaded
- Status changed
- Engineer assigned

## 10. Settings / Templates View

### Buttons

| Button | Function |
|---|---|
| **Manage Report Types** | Damage assessment, valuation, diminution, roadworthy, forensic, criminal. |
| **Manage Checklists** | Required fields/evidence per report type. |
| **Manage Chaser Templates** | Email/WhatsApp templates. |
| **Manage Pack Template** | Section order and fixed wording. |
| **Manage Confidence Thresholds** | Auto-match vs review thresholds. |
| **Manage Engineers** | Names, regions, specialisms, availability. |
| **Manage AI Provider** | Model/provider configuration. |
| **Export Settings** | Download config. |
| **Import Settings** | Load JSON/CSV config. |

## Exact MVP button list

Include these first:

```text
Upload Files
Use Demo Data
Start Processing
Accept Extracted Details
Edit Fields
Open Case
Review Match
Approve Match
Reject Match
Link to Existing Case
Create New Case
Merge Cases
Split Case
Request Missing Info
Generate Chaser Draft
Copy Draft
Mark Requested
Mark Received
Parse Estimate
Add Review Flag
Resolve Flag
Generate Engineer Pack
Regenerate Pack
Preview PDF
Download PDF
Add Internal Note
Change Status
Archive Case
View Activity Log
```

## Buttons deliberately excluded from first demo

```text
Send Email
Send WhatsApp
Submit to Audatex
Sync Calendar
Auto-Assign Engineer
Auto-Issue Report
Detect Fraud
Calculate Repair Cost
Approve Final Report
```

These imply production integrations, legal responsibility or engineering judgement. Keep the demo to **ingest, classify, match, flag, draft and package**.
