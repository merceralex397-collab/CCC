# 12 — Compliance, Governance and Risk

Generated: 2026-05-22

## Core governance principle

AI may assist with administration, extraction, matching, drafting and review prompts. It must not replace the named expert’s independent professional judgement.

## Expert evidence context

Collision Engineers’ work is legal/insurance-facing and may support civil or criminal proceedings. For civil proceedings in England and Wales, CPR Part 35 and Practice Direction 35 are central references.

A current source check confirms that CPR Part 35 restricts expert evidence to what is reasonably required to resolve proceedings, and Practice Direction 35 states experts should provide objective, unbiased opinions and should not act as advocates.

Implication:

- The AI can prepare materials.
- The engineer must own the opinion.
- The final report must not conceal AI assistance in a way that undermines accountability.
- The system must retain source material and review history.

## Human sign-off policy

The following must require human approval:

| Action | Required reviewer |
|---|---|
| Low-confidence evidence match | Admin or case handler |
| Case merge/split | Admin or supervisor |
| Missing-info chaser sent externally | Admin/user |
| Engineer pack locked | Admin/engineer |
| Technical opinion included | Qualified engineer |
| Roadworthiness conclusion | Qualified engineer |
| Fraud/counter-fraud conclusion | Qualified engineer / appropriate reviewer |
| Valuation conclusion | Qualified engineer/valuer |
| Final report issue | Named signing engineer |

## Data protection context

Vehicle claim files can contain personal data:

- names;
- addresses;
- contact details;
- vehicle registration;
- claim references;
- accident circumstances;
- images that may include people, homes, locations or plates;
- insurer/solicitor correspondence.

AI processing of personal data must be governed under UK data protection law. Current ICO guidance on AI/data protection is under review following the Data (Use and Access) Act 2025, but AI systems processing personal data remain inside data protection principles.

## Automated decision-making caution

Even where UK law has become more permissive on solely automated significant decisions, safeguards remain important.

Collision Engineers should avoid solely automated decisions that materially affect a person’s claim, legal position, settlement, vehicle safety status or fraud suspicion.

Use AI outputs as internal prompts:

- “review required”;
- “possible mismatch”;
- “missing evidence”;
- “estimate contains ADAS keyword”;
- “possible duplicate image”.

Avoid AI outputs like:

- “fraud confirmed”;
- “vehicle unroadworthy”;
- “claim invalid”;
- “repair cost unreasonable”;
- “liability established”.

## DPIA triggers

A Data Protection Impact Assessment is likely advisable if the production system includes:

- large-scale claim processing;
- AI processing of personal data;
- profiling or risk scoring;
- fraud indicators;
- image metadata analysis;
- duplicate-image search across historical claims;
- automated recommendations affecting claim handling.

## Audit trail requirements

For defensibility, the system should store:

- original files unchanged;
- file checksums/hashes;
- upload time and source channel;
- extracted text/OCR output;
- extracted fields and confidence scores;
- match reasons;
- AI prompt version and model name;
- user approvals/rejections;
- edits made to generated packs;
- final pack/report version;
- outbound message approval, if any.

## Source attribution

AI-generated summaries should be source-linked where possible. At minimum, each generated section should record:

- source document IDs;
- source pages or excerpts where possible;
- AI run ID;
- generation timestamp;
- human editor/approver.

## Audatex/proprietary system risk

Audatex is proprietary. Do not:

- scrape live Audatex screens;
- bypass login/licensing;
- reverse-engineer repair databases;
- recreate proprietary repair-time calculations;
- represent extracted estimates as official Audatex data unless sourced from a supplied Audatex output.

Safe route:

- parse customer-provided PDFs/exports;
- integrate via approved AudaConnect/API route if licensed;
- retain source documents;
- treat extracted values as parsed evidence, not recreated Audatex calculations.

## Image-forensics risk

Image analysis can produce false positives. Later-phase image-integrity tools should use careful language:

- “possible duplicate”;
- “metadata anomaly”;
- “image quality issue”;
- “requires human review”.

Do not use:

- “fake image”;
- “fraudulent image”;
- “manipulated image confirmed”;
- “claim invalid”.

## Prompt and output risk

LLMs can hallucinate. Guardrails:

- return JSON where possible;
- require null for unknown fields;
- provide confidence;
- include source snippets;
- forbid unsupported technical opinions;
- maintain prompt versions;
- test against synthetic edge cases;
- compare output with source documents during QA.

## Client confidentiality

Production needs:

- NDA/confidentiality review;
- approved AI vendor terms;
- data processing agreements;
- region/data residency preference;
- retention/deletion policy;
- incident-response plan;
- staff access controls;
- separation between demo and production data.

## Recommended governance wording for proposals

> “The system will assist with document processing, evidence organisation, consistency checks, draft communications and engineer-pack preparation. Qualified engineers remain responsible for technical opinions, conclusions and final report approval. All AI actions will be logged, source-linked and subject to human review where confidence is low or legal/technical judgement is required.”

## Red-line claims to avoid

Do not claim:

- “fully automated expert reports”;
- “AI fraud detection”;
- “AI determines roadworthiness”;
- “AI replaces Audatex”;
- “AI guarantees court compliance”;
- “AI eliminates the need for engineer review”.

## Safer claims

Use:

- “AI-assisted case preparation”;
- “evidence matching support”;
- “draft report sections for review”;
- “review flags”;
- “human-approved workflow”;
- “audit trail”;
- “source-linked summaries”;
- “engineer-ready pack generation”.
