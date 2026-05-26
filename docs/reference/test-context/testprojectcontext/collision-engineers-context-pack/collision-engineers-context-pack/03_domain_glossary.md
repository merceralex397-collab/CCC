# 03 — Domain Glossary

Generated: 2026-05-22

This file explains the key terms used across the project in plain English.

## Business and claims terms

| Term | Meaning |
|---|---|
| **Instruction** | The formal request from a client/work provider asking Collision Engineers to assess a vehicle matter. Usually includes vehicle details, claim references, questions to answer and supporting documents. |
| **Instruction pack** | The PDF/email bundle containing the instruction plus supporting files. |
| **Work provider** | The organisation sending the work: solicitor, insurer, accident management company, repairer, fleet operator, government body or private client. |
| **Holding pen** | A temporary queue for cases that cannot yet progress because evidence is missing, unmatched or unclear. It may currently be a spreadsheet or manual list. |
| **Case reconciliation** | Matching all documents, images, estimates and references that belong to the same matter. This is the “marry up” stage in the notes. |
| **Desktop inspection** | Assessment based on photos, documents and estimates rather than physically inspecting the vehicle. |
| **Physical inspection** | Engineer physically examines the vehicle or relevant components. |
| **Engineer pack** | A structured pack prepared before engineer review: case summary, instruction summary, photos, estimate data, missing items and questions. |
| **Final report** | The formal expert/engineering output that must be reviewed, approved and signed off by a qualified human engineer. |
| **RTA** | Road traffic accident. |
| **Total loss** | The vehicle is uneconomical or inappropriate to repair, often because repair cost approaches or exceeds value. |
| **Salvage category** | UK write-off classification, such as Cat S or Cat N, describing structural/non-structural damage and repair status. |
| **Diminution in value** | Loss in market value after a vehicle has been damaged and repaired. Even a correctly repaired vehicle may be worth less because of accident history. |

## Vehicle and repair terms

| Term | Meaning |
|---|---|
| **VDA** | Vehicle Damage Assessor. A trained person who assesses accident repair damage and costs. |
| **VIN** | Vehicle Identification Number, the vehicle’s unique chassis identity. |
| **VRM / registration** | Vehicle registration mark, such as AB12 CDE. Often the most useful matching identifier. |
| **ADAS** | Advanced Driver Assistance Systems: cameras, radar and sensors for features like lane assist, emergency braking and adaptive cruise. Damage to ADAS-related areas can require calibration. |
| **OEM** | Original Equipment Manufacturer. The vehicle maker or official source of parts/repair methods. |
| **Supplementary estimate** | A later estimate created when hidden damage or additional work is identified after the original estimate. |
| **Wheel alignment** | Checking/adjusting wheel geometry; relevant when suspension/wheel damage is present. |
| **SRS / airbag** | Supplemental restraint system; safety-critical airbag and restraint components. |
| **Clamp and pull** | Bodyshop structural correction operation using pulling equipment. Often disputed if not evidenced properly. |
| **QC time** | Quality control time after repair; sometimes challenged in non-contract charge disputes. |

## Audatex and industry terms

| Term | Meaning |
|---|---|
| **Audatex** | Solera-owned vehicle claims and collision-repair estimating ecosystem used to create and review repair estimates. |
| **AudaEnterpriseGold / AEG** | Audatex’s main UK vehicle damage estimating platform. |
| **AudaConnect** | Audatex API/integration route. Use approved integration routes rather than scraping. |
| **Qapter** | Solera/Audatex AI/photo-based claims tools for guided image capture, triage and intelligent estimating. |
| **cap hpi** | Vehicle valuation and automotive data provider often relevant to total-loss and valuation decisions. |
| **ABP Guide** | Auto Body Professionals guide to retail and non-contract charges; used as a benchmark/reference in some charge disputes. |
| **BS 10125** | UK vehicle damage repair specification relevant to safe and compliant accident repair. |

## AI and software terms

| Term | Meaning |
|---|---|
| **AI** | Software that performs tasks usually requiring human-like pattern recognition, such as reading documents, classifying images or drafting text. |
| **LLM** | Large language model, such as ChatGPT or Claude. It can read, summarise, classify, extract fields and draft text. It does not “know” the case unless provided with source material. |
| **OCR** | Optical Character Recognition: converting scanned PDFs or images into readable text. Plain English: making a scan searchable/readable by software. |
| **Structured extraction** | Taking messy text and converting it into clean fields, such as vehicle registration, claim reference, date of loss and report type. |
| **Confidence score** | A numeric indication of how sure the system is. It should guide review, not replace it. |
| **Human-in-the-loop** | The AI prepares or suggests, but a person reviews and approves important actions. |
| **RAG** | Retrieval-Augmented Generation. Plain English: the AI answers using a searchable library of approved documents rather than relying only on its general training. |
| **Embedding** | A numerical representation of text/image content used for search and similarity matching. Plain English: a way to find “things like this”. |
| **Metadata** | Information about a file, such as filename, upload time, sender, EXIF camera data or email subject. |
| **Audit trail** | A record of what was uploaded, extracted, matched, approved, edited and generated. Essential for legal/insurance confidence. |
| **API** | A controlled software connection that lets systems exchange data without manual copying and pasting. |
| **Webhook** | A notification from one system to another when something happens, such as a new file upload. |

## Legal/governance terms

| Term | Meaning |
|---|---|
| **CPR Part 35** | Civil Procedure Rules section governing expert evidence in civil proceedings in England and Wales. |
| **Practice Direction 35** | Detailed requirements supplementing CPR Part 35, including objectivity and report content expectations. |
| **Expert duty to court** | An expert must help the court objectively within their expertise. This duty overrides the duty to the paying party. |
| **GDPR / UK GDPR** | UK data protection framework governing personal data. Vehicle claims files can contain personal data. |
| **DUAA 2025** | Data (Use and Access) Act 2025, which changed parts of the UK data protection framework including automated decision-making rules. |
| **DPIA** | Data Protection Impact Assessment. A structured review of privacy risks, likely needed before high-impact AI processing. |

## Project-specific shorthand

| Term | Meaning |
|---|---|
| **The demo** | The phase-one local web app for upload → extraction → matching → engineer pack. |
| **The pack** | The engineer-ready assessment pack, not a final expert report. |
| **Low confidence** | Any match/extraction below the chosen threshold, e.g. 85%, requiring admin review. |
| **Evidence card** | UI element representing a PDF, image, email note or estimate, showing extracted identifiers and match reasons. |
| **Review flag** | A prompt for human attention, not an automatic finding. |
