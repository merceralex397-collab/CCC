# 14 — Discovery Questions and Call Prep

Generated: 2026-05-22

## Call objective

Confirm the current workflow and choose the smallest prototype that proves value.

## Opening framing

Use this framing:

> “From what I understand, the main opportunity is not to replace the engineer. It is to reduce the admin between receiving an instruction and giving the engineer a clean, complete case file. I want to confirm how files arrive, how the holding pen works, and what a useful engineer pack needs to contain.”

## Workflow questions

1. Can you walk me through what happens from the moment an instruction arrives to the point an engineer starts the assessment?
2. Where do instructions arrive now — email, WhatsApp, repairer portal, shared drive, API, insurer portal or all of these?
3. What exactly is the “holding pen”? Excel, shared folder, CRM, case-management system or something else?
4. What fields are currently captured in the holding pen?
5. Which files usually arrive separately: instruction PDFs, Audatex estimates, photos, invoices, repairer notes or client emails?
6. What are the most common reasons a case cannot move straight to assessment?
7. How often do images arrive separately from the instruction PDF?
8. Who currently decides when a case is ready for engineer review?
9. What does “assessment” mean in your internal language: engineer pack, Audatex estimate, final report, roadworthy decision or internal summary?

## Matching questions

1. What is the most reliable matching field: vehicle registration, VIN, claim reference, client reference, Audatex ID, email sender or something else?
2. How often do references conflict or go missing?
3. Do multiple cases from the same client arrive in one email/thread?
4. Do images ever arrive with weak filenames and no obvious reference?
5. Are duplicate files common?
6. How often does the wrong material get attached to a case?
7. Who should review low-confidence matches?

## Audatex/estimate questions

1. Do you use Audatex directly, receive Audatex PDFs from others, or both?
2. Do your engineers create estimates in Audatex, review estimates created by others, or both?
3. Which Audatex product is involved: AudaEnterpriseGold, Qapter, PlanManager, AudaConnect or only emailed/networked estimates?
4. Are estimates received as PDFs, screenshots, exports, networked assessments or portal records?
5. Do you have AudaConnect/API access?
6. Which estimate sections are most time-consuming to review?
7. How often do supplementary estimates cause admin/reporting delays?
8. What estimate flags would be genuinely useful: ADAS, alignment, SRS, total loss, supplementary, mismatched reg, manual lines?

## ABP/charge-dispute questions

1. How often are ABP-style retail/non-contract charges discussed or disputed?
2. Which charge categories are most often challenged?
3. Do you need internal review notes or client-facing rebuttal drafts?
4. Should the system compare to fixed internal thresholds or simply flag charge categories for evidence review?
5. Who approves any ABP-related wording before issue?

## Engineer-pack questions

1. What does a good engineer-ready pack need to contain?
2. Which report types are most repetitive and safest for a prototype?
3. Which parts of a report are repetitive enough for AI to draft safely?
4. Which parts must remain entirely engineer-authored?
5. Do you already have standard report templates by service type?
6. Do you want the pack in PDF, Word, HTML, markdown or inside a dashboard?
7. What image schedule format would be most useful?
8. Do engineers need direct links to original source files?

## Technology questions

1. What systems do you use now for email, storage, calendar and case tracking?
2. Are you on Microsoft 365/SharePoint/Outlook?
3. Is there already a CRM or case-management system?
4. Where are images stored?
5. Do you need the first prototype to run locally, in the cloud or inside your existing systems?
6. Are there any insurer/solicitor restrictions on using AI tools?
7. Are previous reports/files allowed to be used for internal AI search or model improvement?
8. What is your preferred AI provider, if any? Are you already using Claude, ChatGPT or Gemini?

## Compliance and approval questions

1. Who signs off final reports?
2. What audit trail would you need for legal/insurance confidence?
3. Should AI outputs be stored permanently or only as drafts?
4. Do you need to disclose AI assistance in any internal or external context?
5. What data retention/deletion rules apply?
6. Do clients require data to stay in the UK/EU?
7. Who should approve outbound chasers/messages?
8. Are there specific CPR/expert-report clauses that must never be altered by AI?

## Success metric questions

1. What would count as a successful prototype?
2. Is the priority fewer admin minutes, faster turnaround, fewer unmatched files, fewer missed photos, better report consistency or more engineer capacity?
3. How many cases per week would the prototype need to handle to be useful?
4. How long does manual intake/matching currently take per case?
5. What is the cost of a delayed or incomplete case?
6. What would make you confident enough to pilot it internally?

## Suggested prototype-scope question

Ask this directly:

> “Would phase one be more useful as a PDF/image matching tool, an Audatex parser, or an engineer-pack generator? My recommendation is a narrow upload-based demo that combines all three lightly: classify the files, extract the key fields, match evidence and produce a pack.”

## Call close

End with:

> “I’ll keep the first version narrow: no automatic expert conclusions, no live sending, no Audatex scraping. The first proof will be whether the system can create a reliable case record and engineer pack from messy input files.”

## Follow-up email skeleton

```text
Subject: AI case intake and engineer-pack prototype

Hi [Name],

Thanks for the call. My understanding is that the main operational opportunity is the stage between receiving instructions and getting a clean file in front of an engineer.

The prototype I would suggest is an AI-assisted case intake and engineer-pack generator. It would accept instruction PDFs, repair/Audatex estimate PDFs, images and notes; extract key case details; suggest which evidence belongs together; flag missing or inconsistent information; and generate an engineer-ready assessment pack for review.

I would keep the first version deliberately narrow. It would not issue final expert reports, make fraud decisions or replace Audatex. It would focus on the admin and preparation layer, with human approval for uncertain matches and engineer sign-off for technical conclusions.

The next useful step would be to confirm:
- the fields currently tracked in the holding pen;
- a few example instruction/estimate formats;
- the required evidence checklist for one report type;
- what a good engineer pack should contain;
- the success metric for a two-to-four-week prototype.

Kind regards,
Alex
```
