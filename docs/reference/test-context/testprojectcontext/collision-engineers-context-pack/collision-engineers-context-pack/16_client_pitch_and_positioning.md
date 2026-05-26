# 16 — Client Pitch and Positioning

Generated: 2026-05-22

## Recommended headline

**AI-assisted case intake and assessment preparation for Collision Engineers**

## Short pitch

Collision Engineers appears to receive instructions, vehicle images, estimates and supporting documents through several channels and often at different times. The proposed system would organise that intake automatically: reading PDFs, extracting key case fields, matching evidence to the correct matter, flagging missing information and preparing an engineer-ready assessment pack.

The system would not replace expert judgement. It would reduce the admin burden before the engineer reviews the case.

## One-paragraph proposal wording

> Collision Engineers’ workflow appears to involve receiving instruction PDFs, vehicle images, repair estimates and supporting evidence at different times, then manually matching those items before an engineer can review the matter. I propose an AI-assisted intake and assessment-preparation system that reads incoming documents, extracts key case information, identifies matching images and estimates, flags incomplete or ambiguous matters, and generates an engineer-ready assessment pack. The system can also draft routine chaser messages and non-final report sections for review, while qualified engineers remain responsible for technical opinions and final report sign-off.

## What to emphasise

- Operational efficiency.
- Faster instruction-to-engineer time.
- Reduced manual matching.
- Better missing-information control.
- Human review for uncertainty.
- Source-linked outputs.
- Audit trail.
- Compatibility with Audatex-related evidence.
- No replacement of engineer judgement.

## What not to emphasise first

- Autonomous report writing.
- AI damage estimating from photos.
- Fraud detection.
- Court compliance guarantees.
- Live WhatsApp sending.
- Full Audatex integration.
- Large-scale custom model training.

## Safer language

Use:

- “AI-assisted”;
- “draft for review”;
- “review flag”;
- “evidence matching”;
- “source-linked summary”;
- “engineer-ready pack”;
- “human sign-off”;
- “workflow layer”.

Avoid:

- “automatic expert report”;
- “AI decides”;
- “fraud detected”;
- “roadworthiness certified by AI”;
- “replace Audatex”;
- “fully automated claims decision”.

## Demo positioning

> “The demo is intentionally narrow. It shows the part of the workflow that is safest and most valuable to automate first: turning messy inbound files into a structured case record and engineer pack. It does not issue final technical opinions.”

## Objection handling

### “Can AI write the final report?”

Answer:

> “It can draft factual and repetitive sections for review, but the final technical opinion should remain with the qualified engineer. That is safer legally and commercially.”

### “Can it detect fraud?”

Answer:

> “It can flag indicators that require review, such as duplicate images or mismatched evidence. It should not label something fraudulent without human investigation.”

### “Can it integrate with Audatex?”

Answer:

> “Phase one can parse supplied Audatex PDFs or exports. Deeper integration should use approved routes such as AudaConnect, subject to licence and permission.”

### “Can it send WhatsApp messages?”

Answer:

> “Eventually, possibly through an approved WhatsApp Business workflow. The first demo should generate copyable drafts only, so the risk is controlled.”

### “Can this replace the holding pen?”

Answer:

> “It can initially sit beside the holding pen and export CSV/Excel-compatible data. Once trusted, it can become the primary queue.”

## Suggested project names

- AI Case Intake + Engineer Pack Generator
- Evidence Matching Assistant
- Engineer Pack Builder
- Collision Case Orchestrator
- Assessment Preparation Assistant

## Suggested first prototype scope

```text
Input:
- instruction PDF
- repair/Audatex estimate PDF
- vehicle images
- optional notes

Processing:
- classify files
- extract key fields
- match evidence
- flag missing items
- parse estimate summary

Output:
- holding-pen case row
- evidence matching view
- engineer pack
- chaser draft
- audit log
```

## Follow-up email

```text
Subject: Suggested AI prototype — intake and engineer pack generation

Hi [Name],

Thanks again for the discussion. My read is that the strongest first opportunity is the admin layer between receiving an instruction and getting a complete file in front of an engineer.

I would suggest starting with a narrow prototype: an AI-assisted case intake and engineer-pack generator. It would accept instruction PDFs, repair/Audatex estimate PDFs, vehicle images and notes; extract key case details; match evidence into the correct matter; flag missing or inconsistent information; and generate an engineer-ready assessment pack.

I would keep the first version deliberately controlled. It would not issue final expert reports, make fraud decisions or replace Audatex. It would prepare the case file and draft routine admin text, with human approval for uncertain matches and engineer sign-off for any technical conclusions.

The main questions to confirm are:
- what fields are currently tracked in the holding pen;
- which files arrive separately most often;
- whether Audatex estimates are created internally, received externally, or both;
- what a good engineer pack should contain;
- what would count as a successful two-to-four-week proof of value.

Kind regards,
Alex
```

## Proposal outline

1. Context and current workflow.
2. Main pain point: evidence arrives separately and must be manually matched.
3. Proposed solution: AI-assisted case intake and engineer pack generator.
4. What the system does.
5. What it deliberately does not do.
6. MVP scope.
7. Later phases.
8. Governance and human sign-off.
9. Discovery questions.
10. Next steps.
