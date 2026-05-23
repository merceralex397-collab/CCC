# 02 — Company and Business Context

Generated: 2026-05-22

## Plain-English summary

Collision Engineers is an independent vehicle engineering and expert-report business. The core product is not repairing cars; the core product is **technical evidence about vehicles**.

They inspect vehicles, photographs, repair estimates, valuation material and claim documents, then produce reports for parties such as solicitors, insurers, accident management companies, repairers, government bodies and private clients.

## Verified company facts

Current web spot-checks on 2026-05-22 found:

- Companies House lists **COLLISION ENGINEERS LTD**, company number **09671917**, as active.
- Companies House shows the registered office as **238a Telegraph Road, Heswall, Wirral, England, CH60 0AL**.
- The incorporation date is listed as **6 July 2015**.
- Companies House records Andrew John Patterson as a person with significant control with 75%+ share/voting control.

Source: Companies House overview and PSC pages listed in `17_source_map_and_assumptions.md`.

## What they do

Based on the uploaded website extracts and research notes, their service lines include:

1. **Vehicle damage assessment** — physical or desktop assessment of accident damage and repair reasonableness.
2. **Forensic engineering** — consistency of damage, low-velocity impact, counter-fraud and accident-circumstance analysis.
3. **Diminution in value** — quantifying post-repair loss in market value.
4. **Vehicle valuation** — assessing market value for total-loss, dispute, rare, modified or specialist vehicles.
5. **Roadworthy / unroadworthy reports** — assessing safety and suitability for road use.
6. **Criminal reports** — bespoke reports for serious vehicle-related criminal proceedings.
7. **Audatex/bodyshop estimate work** — repairers can submit vehicle details/images and receive a professional Audatex estimate.

## Why independence matters

A bodyshop may have a commercial interest in repair work. An insurer may have a commercial interest in cost control. A claimant may have a financial interest in recovery. Collision Engineers’ value proposition is that they provide an independent technical opinion that can be relied on in disputes.

That is why the AI system must preserve:

- human expert sign-off;
- source-document traceability;
- audit trails;
- clear distinction between facts, AI assistance and expert opinion;
- no hidden automation of conclusions.

## Typical client-side questions

Collision Engineers may be asked to answer questions like:

- Is the claimed damage consistent with the described accident?
- Is the repair estimate reasonable?
- Is the vehicle repairable or a total loss?
- Are there pre-existing damage issues?
- Is the vehicle safe to drive?
- Was the repair completed correctly?
- Has the vehicle lost value after repair?
- Are disputed retail/non-contract charges justified?
- Is the evidence suitable for legal or insurance use?

## Business model implications for AI

Because they sell expert judgement, AI should target the **pre-judgement administrative layer**:

- receiving and classifying files;
- extracting basic case facts;
- matching evidence;
- checking completeness;
- preparing packs;
- drafting standard admin text;
- surfacing review prompts;
- summarising estimates and instructions.

AI should not be framed as replacing the engineer. In this business, the engineer’s accountable judgement is the product.

## Operating model clues

The uploaded project materials suggest a mixed digital intake model:

- professional enquiries by email;
- WhatsApp as a quick messaging route;
- a website enquiry route;
- references to API-based instruction after terms of business;
- a repairer portal for estimate requests;
- case material arriving asynchronously from different sources.

This makes them a strong fit for an intake orchestration system.

## What “technical evidence” means here

Technical evidence means information and opinion that can influence money, liability, repair authorisation, settlement, fraud review, roadworthiness, prosecution or court proceedings.

That creates a high-value automation opportunity, but also a high-governance environment. The system must help the expert work faster without polluting, fabricating or obscuring the evidence chain.

## Immediate strategic takeaway

Collision Engineers appears to be a small, specialist, speed-sensitive expert business. The highest-value AI opportunity is to reduce the time between **instruction received** and **engineer ready to review**, while keeping legal defensibility intact.
