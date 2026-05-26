# 10 — AI Modules and Prompt Patterns

Generated: 2026-05-22

## AI design principle

Use AI for repeatable reading, sorting, extraction, drafting and summarisation. Do not use AI to make final expert conclusions.

## Module map

| Module | Phase | Purpose |
|---|---|---|
| Document classifier | MVP | Decide whether a file is an instruction, estimate, invoice, image, note or unknown. |
| Instruction extractor | MVP | Extract structured case details from instruction PDFs/emails. |
| Estimate parser | MVP | Extract Audatex/repair estimate values and review triggers. |
| Evidence matcher | MVP | Suggest which documents/images belong to the same case. |
| Missing-information checker | MVP | Identify what blocks the case from being engineer-ready. |
| Chaser drafter | MVP | Draft email/WhatsApp-style requests for missing evidence. |
| Engineer pack generator | MVP | Produce structured pack for engineer review. |
| Estimate QA assistant | Phase 2 | Flag ADAS/alignment/SRS/supplementary/total-loss review points. |
| ABP charge-review assistant | Phase 2 | Flag retail/non-contract charge categories for engineer review. |
| Image quality checker | Phase 3 | Identify missing standard angles, blur and poor evidence quality. |
| Duplicate-image search | Phase 3 | Compare new images against prior image library for reuse/overlap. |
| Knowledge-base assistant | Phase 3 | Search prior reports, standard clauses and internal guidance. |
| Management analytics | Phase 4 | Summarise throughput, blockers, case mix and SLA performance. |

## Module 1 — Document classifier

### Input

- filename;
- MIME type;
- extracted text;
- first page preview text;
- upload batch metadata.

### Output

```json
{
  "documentType": "instruction_pdf",
  "confidence": 0.92,
  "reasons": ["contains instruction wording", "contains vehicle registration", "contains claim reference"]
}
```

### Prompt pattern

```text
You are classifying documents for a UK automotive engineering case-intake workflow.
Classify the file into exactly one of:
- instruction_pdf
- audatex_estimate
- repair_estimate
- repair_invoice
- valuation_evidence
- engineer_report
- email_note
- vehicle_image
- unknown

Return JSON only.
Do not infer facts not visible in the text.
If uncertain, choose unknown and explain the uncertainty in reasons.
```

## Module 2 — Instruction extractor

### Fields to extract

- vehicle registration;
- VIN;
- claim reference;
- client/work provider;
- claimant/insured name, if present;
- report type;
- inspection type;
- date of loss;
- location;
- urgency;
- special instructions/questions;
- supporting documents referenced;
- missing fields.

### Prompt guardrails

- Return `null` for missing fields.
- Do not invent client names or dates.
- Include confidence per field.
- Provide source snippets/page references where possible.
- Flag contradictions.

### Output shape

```json
{
  "vehicleReg": {"value": "AB12 CDE", "confidence": 0.98, "source": "page 1"},
  "claimRef": {"value": "CLM-12345", "confidence": 0.94, "source": "page 1"},
  "reportType": {"value": "damage_assessment", "confidence": 0.82, "source": "instruction heading"},
  "missingFields": ["location", "inspectionType"],
  "contradictions": []
}
```

## Module 3 — Estimate parser

### Extracted fields

- estimate reference;
- repairer/bodyshop;
- insurer/work provider;
- vehicle registration;
- VIN;
- estimate date;
- parts total;
- labour total;
- paint total;
- specialist/misc total;
- VAT;
- grand total;
- supplementary marker;
- ADAS/calibration keywords;
- alignment/suspension keywords;
- airbag/SRS/safety keywords;
- total-loss/valuation marker.

### Flags

- registration mismatch;
- claim reference mismatch;
- supplementary detected;
- ADAS keyword but no calibration line;
- wheel/suspension keyword but no alignment line;
- SRS/airbag keyword;
- manual/misc line;
- high estimate value needing engineer review.

### Prompt pattern

```text
You are parsing a UK vehicle repair estimate for an engineering review workflow.
Extract factual estimate data only.
Do not decide whether the estimate is correct.
Flag items requiring engineer review, but label them as review prompts only.
Return JSON only.
```

## Module 4 — Evidence matcher

### Matching signals

- vehicle registration;
- VIN;
- claim reference;
- client reference;
- Audatex estimate ID;
- filename;
- same upload batch;
- sender/channel;
- date/time proximity;
- semantic similarity between instruction and estimate text.

### Output

```json
{
  "suggestedCaseId": "case_001",
  "evidenceId": "doc_003",
  "confidence": 0.88,
  "reasons": [
    {"type": "vehicle_reg_match", "value": "AB12 CDE", "weight": 0.50},
    {"type": "same_upload_batch", "value": "batch_22", "weight": 0.20},
    {"type": "sender_match", "value": "same sender", "weight": 0.10}
  ],
  "requiresHumanReview": true
}
```

## Module 5 — Missing-information checker

### Checklist examples

#### Damage assessment

- instruction document;
- vehicle registration;
- claim reference;
- date of loss;
- estimate, if desktop repair-cost review;
- vehicle images;
- front/rear/nearside/offside/damage closeups;
- location, if physical inspection;
- specific questions to answer.

#### Diminution report

- repair history;
- pre-accident/post-repair valuation evidence;
- mileage;
- vehicle specification;
- repair invoice/estimate;
- post-repair photos;
- accident date.

#### Roadworthy report

- damage photos;
- safety-critical areas;
- inspection location;
- repair status;
- recovery/driveability question;
- urgency.

## Module 6 — Chaser drafter

### Safe draft example

```text
Subject: Further information required – {{vehicleReg}}

Hi,

Thank you for the instruction. We have received {{receivedItems}}, but the case is currently missing {{missingItems}}.

Please could you provide:
{{bulletList}}

Kind regards,
Collision Engineers
```

### Guardrails

- Do not make technical findings.
- Do not accuse fraud or non-compliance.
- Do not claim the case is accepted unless status says so.
- Keep language factual and concise.
- Require copy/approval before sending.

## Module 7 — Engineer pack generator

### Sections

- Case summary
- Instruction summary
- Documents received
- Image schedule
- Estimate summary
- Missing information
- Review flags
- Questions for engineer
- Draft admin/client message
- Audit trail summary

### Prompt pattern

```text
You are preparing an internal engineer assessment pack.
Use only the provided structured case data and source summaries.
Do not provide final technical opinions.
Do not decide causation, liability, fraud, roadworthiness, valuation or repair correctness.
Separate facts, missing information and questions for engineer review.
Return clean markdown.
```

## Module 8 — ABP charge-review assistant

### Purpose

Flag disputed charge categories in repair invoices/estimates. It should not decide whether a charge is recoverable or correct.

### Charge categories

- wheel alignment;
- ADAS reset/calibration;
- repair methods/research;
- clamp and pull;
- tyre replacement;
- QC time;
- energy/environmental charges;
- BS10125/manufacturer approval charges;
- mobility/storage/recovery;
- non-standard materials or miscellaneous items.

### Output

```json
{
  "chargeReviewFlags": [
    {
      "category": "adas_calibration",
      "lineReference": "Estimate page 3",
      "reason": "ADAS-related keyword found; calibration evidence should be checked",
      "requiredEvidence": ["repair method", "image reference", "sensor/ADAS involvement", "estimate line"]
    }
  ]
}
```

## Module 9 — Image quality and duplicate support

### Later-phase capability

The image layer can eventually:

- detect blurry images;
- check missing standard angles;
- identify visible damage zones;
- compare against previous images for reuse;
- check metadata inconsistencies;
- flag possible manipulation indicators.

### Guardrail

Never label the output as “fraud detected.” Use “requires review”, “possible duplicate”, “metadata anomaly” or “image integrity flag.”

## Global AI guardrails

All AI outputs should obey these rules:

1. Use source-provided facts only.
2. Return structured JSON where possible.
3. Use confidence scores.
4. Explain match reasons.
5. Flag uncertainty.
6. Preserve original files.
7. Require human approval for low-confidence cases.
8. Require engineer approval for technical conclusions.
9. Never auto-send external messages in phase one.
10. Never bypass proprietary systems or licensing.

## Prompt versioning

Every AI run should store:

- module name;
- prompt version;
- model name;
- input summary;
- output JSON;
- confidence;
- timestamp;
- human correction, if any.

This is essential for debugging and legal defensibility.
