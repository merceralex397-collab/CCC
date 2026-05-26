# 04 — Current Workflow and Pain Points

Generated: 2026-05-22

## High-level current workflow inferred from the project notes

```text
Client/work provider sends instruction
        ↓
Instruction PDF, estimate, photos and notes arrive through mixed channels
        ↓
Items may arrive at different times
        ↓
Unmatched or incomplete cases go into a holding pen
        ↓
Admin manually matches instruction + images + estimate + references
        ↓
Admin flags missing information
        ↓
Admin books or allocates engineer
        ↓
Engineer reviews evidence and prepares/finalises report
        ↓
Final PDF/report issued after human approval
```

## Intake channels likely involved

The uploaded materials and live checks indicate the business uses or references:

- email for professional enquiries;
- WhatsApp for quick messaging;
- website enquiry/contact form;
- repairer portal submission;
- API-based instruction once terms are agreed;
- manually received PDFs and vehicle images.

The key issue is that a single case can be split across these channels.

## What “written instruction with work in PDF” likely means

A client sends an instruction pack containing some or all of:

- vehicle registration;
- VIN, if available;
- claimant/client name;
- accident/loss date;
- claim reference;
- solicitor/insurer/accident management details;
- report type;
- repair estimate or invoice;
- special questions for the engineer;
- photos or links to photos.

The phrase should be normalised in proposals as **instruction document** or **case instruction pack**.

## Main pain point: asynchronous evidence

Cases can arrive in fragments:

- instruction first, photos later;
- photos first, instruction later;
- estimate later than both;
- multiple PDFs for one case;
- multiple matters from the same sender;
- weak filenames such as `IMG_3021.jpg`;
- duplicate or re-sent images;
- case references appearing in one document but not another.

This creates a matching problem.

## “Holding pen” problem

A holding pen is a useful manual control, but it has limitations:

- no automatic extraction from PDFs;
- no confidence score for matches;
- hard to see why a case is blocked;
- manual chasing creates delay;
- weak audit trail over who approved a match;
- potential for misfiled evidence;
- difficult management visibility across live work.

The proposed system should either replace it or sit beside it at first.

## Manual reconciliation tasks

Admin staff likely perform these repetitive tasks:

- open PDF instruction;
- read key details;
- copy fields into spreadsheet/case system;
- check images are present;
- compare vehicle registration across documents;
- compare claim/client references;
- decide whether an estimate belongs to the matter;
- chase missing photos or documents;
- decide readiness for engineer;
- book or notify an engineer;
- produce or initiate a report pack.

These are good automation targets because they are repeatable, structured and document-heavy.

## Likely failure modes

| Failure mode | Impact |
|---|---|
| Images attached to wrong matter | Engineer wastes time or report risk increases. |
| Instruction missing but images received | Case stalls without clear ownership. |
| Estimate present but no images | Desktop assessment cannot progress. |
| Vehicle reg mismatch | Possible wrong file or copied reference error. |
| Claim ref mismatch | Evidence may belong to another case. |
| Duplicate case opened | Work duplicated; status becomes unreliable. |
| Low-quality photos | Engineer must request more information. |
| Missing ADAS/alignment evidence | Safety or repair-method issue may be missed. |
| No audit trail | Hard to prove who approved what and when. |

## Why this is a strong automation opportunity

The target workflow is not speculative. The notes repeatedly point to the same bottleneck: **turning messy inbound evidence into a clean case file**.

An AI-assisted system can read, sort, extract, match and flag. A person then approves uncertain cases and the engineer makes the technical decision.

## Current-state assumptions to validate

These are not confirmed and should be tested in the next call:

1. The holding pen is Excel or spreadsheet-like.
2. Vehicle registration is usually the strongest match key.
3. Claim/client references are inconsistent across senders.
4. Images often arrive separately from the instruction.
5. Audatex PDFs or repair estimates are common evidence items.
6. Admin staff, not engineers, do the first evidence matching.
7. The term “assessment” may mean either an engineer pack, an Audatex estimate, or a final report depending on context.
