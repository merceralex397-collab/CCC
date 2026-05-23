# 17 — Source Map and Assumptions

Generated: 2026-05-22

## Purpose

This file separates verified sources, uploaded project material, current web spot-checks, inferences and open questions.

## Uploaded project sources used

| Source file | Used for |
|---|---|
| `Proposal Workflow Clarification.txt` | Core workflow interpretation: intake → evidence matching → engineer booking → report production; human-in-the-loop framing. |
| `Collision Engineers report.pdf` | Company research, services, AI opportunity areas, compliance considerations. |
| `Audatex Overview and Use.txt` | Audatex ecosystem, Qapter, AudaConnect, estimate parser opportunity and integration cautions. |
| `ABP 2025 Industry Guide.txt` | ABP retail/non-contract charge context and ABP charge-review assistant concept. |
| `deep-research-report (4).md` | Due diligence, public market signals, AI options, compliance/ROI roadmap. |
| `About Us _ Collision Engineers.md` | Contact/intake details, email/WhatsApp/API references. |
| `Repairer Portal _ Collision Engineers.md` | Repairer portal, Audatex estimate request, fixed estimate fee, image upload flow. |
| `Collision Engineers _ Independent Automotive Engineering Experts.md` | Website positioning, service categories, independence, CPR/expert witness language. |
| `Services _ Collision Engineers.md` | Detailed service lines and use cases. |
| `Follow-up Email Brainstorm.txt` | Proposal angles, discovery questions, module ideas and wording. |
| `Initial Demo Proposal.txt` | MVP demo scope, build order, data model and demo narrative. |
| `Collision Engineers Overview.txt` | Plain-English company/business explanation. |
| `removed_items_report.md` | Cleanup/noise-awareness for website extracts. |
| `abp.jpg` | ABP screenshot context indicating real dispute/review relevance. |

## Current web spot-checks performed on 2026-05-22

| Source | What was checked | URL |
|---|---|---|
| Companies House overview | Collision Engineers Ltd active, company number, registered office, incorporation date. | https://find-and-update.company-information.service.gov.uk/company/09671917 |
| Companies House PSC | Andrew John Patterson listed with 75%+ ownership/voting control. | https://find-and-update.company-information.service.gov.uk/company/09671917/persons-with-significant-control |
| Collision Engineers website | Public positioning as independent automotive engineering experts. | https://collisionengineers.co.uk/ |
| ABP publications | ABP 2026 and 2025 guide listings. | https://www.abpclub.co.uk/publications |
| ABP 2026 guide news | 2026 guide available online from 8 December 2025. | https://www.abpclub.co.uk/news/abp-2026-guide-to-retail-and-non-contract-charges-now-available-online-link-below-with-print-copies-posted-on-monday-15-december |
| Audatex AudaConnect | AudaConnect described as secure/GDPR-compliant API-style integration route. | https://audatex.co.uk/solutions/audaconnect/ |
| Audatex Qapter Intelligent Triage | AI/API-based photo triage context. | https://audatex.co.uk/solutions/qapter-intelligent-triage/ |
| Audatex Qapter Guided Image Capture | Guided photo capture/API context. | https://audatex.co.uk/solutions/qapter-guided-image-capture/ |
| CPR Part 35 | Expert evidence restricted to what is reasonably required. | https://www.justice.gov.uk/courts/procedure-rules/civil/rules/part35 |
| Practice Direction 35 | Expert objectivity/unbiased opinion requirements. | https://www.justice.gov.uk/courts/procedure-rules/civil/rules/part35/pd_part35 |
| ICO AI/data protection guidance | AI processing of personal data and guidance-under-review context. | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/ |
| GOV.UK DUAA changes | Automated decision-making framework changes and safeguards. | https://www.gov.uk/guidance/data-use-and-access-act-2025-data-protection-and-privacy-changes |

## Important verified facts

- Collision Engineers Ltd is listed by Companies House as active.
- The registered office is currently listed as 238a Telegraph Road, Heswall, Wirral, England, CH60 0AL.
- The company was incorporated on 6 July 2015.
- The public website positions the business as independent automotive engineering experts.
- Uploaded website extracts show service lines including accident damage reports, forensic engineering, diminution, valuation, roadworthy/unroadworthy and criminal reports.
- The repairer portal extract says users can submit vehicle details/images for a professional Audatex estimate.
- ABP lists the 2026 Guide to Retail and Non-Contract Charges as current in its publications area.
- Audatex positions AudaConnect as the approved API-style integration layer.

## Core inferences

These are strong inferences from the project notes, not independently verified operational facts:

1. The “holding pen” is spreadsheet-like or at least manually maintained.
2. Instruction PDFs and images often arrive separately.
3. Admin staff currently reconcile instruction, estimate, images and references manually.
4. Vehicle registration is likely a primary matching key.
5. Audatex estimate PDFs are likely common enough to justify a parser.
6. ABP charge disputes are relevant enough to justify a later assistant module.
7. The first prototype should focus on pack generation rather than final report automation.

## Unknowns requiring direct confirmation

1. Current case-management tool.
2. Exact holding-pen format.
3. Weekly case volume.
4. Average admin time per intake.
5. Current report templates.
6. Whether Audatex is used directly, received externally, or both.
7. Whether AudaConnect access exists.
8. Whether client contracts restrict AI processing.
9. Whether data must stay in a particular region.
10. Whether previous cases can be used for internal model improvement/search.
11. Engineer allocation process.
12. Actual ABP dispute frequency.
13. Whether WhatsApp is personal, business, or API-managed.
14. Who has final authority to approve AI-generated wording.

## Confidence levels

| Item | Confidence | Reason |
|---|---:|---|
| Core project should be intake/evidence matching | High | Repeated across call notes and demo planning. |
| Final engineering judgement must remain human | High | Legal/expert context and project notes. |
| Audatex parser is relevant | High | Repairer portal and Audatex research. |
| ABP assistant is relevant | Medium-high | Screenshot/research indicates real dispute use, but frequency unknown. |
| Holding pen is Excel | Medium | Notes suggest spreadsheet, but not directly confirmed. |
| Weekly ROI | Low until discovery | Internal volume/time data unknown. |

## Source-quality notes

- Companies House and government/justice/ICO sources should be treated as authoritative for company/legal/public-regulatory facts.
- Collision Engineers’ website is authoritative for their public positioning and service claims, but not internal workflow details.
- Uploaded call notes and brainstorm documents are the strongest source for internal workflow interpretation, but need confirmation from the company.
- ABP full guide content may be member-gated; use current guide references carefully and avoid quoting inaccessible charge values unless provided/licensed.
- Audatex materials are proprietary/commercial; use official APIs/exports and avoid unauthorised extraction methods.

## Working assumption for all other docs

The recommended project is scoped around **case preparation**, not automated expert decisioning.
