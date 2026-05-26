# 11 — Audatex and ABP Industry Context

Generated: 2026-05-22

## Why this file matters

Collision Engineers operates in the UK vehicle damage assessment, repair-estimate and expert-reporting ecosystem. Audatex and ABP are both relevant, but they play different roles.

## Audatex in plain English

Audatex is an industry software ecosystem used to create, review, authorise and exchange vehicle damage repair estimates.

In plain terms: it is where vehicle repair estimates are often structured into vehicle details, damaged panels, repair/replace operations, parts, labour, paint, VAT and total-loss/valuation indicators.

## What Audatex is not

For this project, Audatex should not be treated as something to replace.

Do not pitch:

> “We will build our own Audatex.”

Pitch:

> “We will build an AI workflow layer around Audatex-related evidence, starting with PDFs/exports and only using approved integration routes if deeper integration is required.”

## Relevant Audatex components

| Component | Meaning for this project |
|---|---|
| **AudaEnterpriseGold / AEG** | Core estimating workflow. Estimate PDFs/exports may come from here. |
| **AudaConnect** | Approved API-style integration route, subject to licence/permission. |
| **Qapter** | Audatex/Solera AI photo capture, triage and estimating tools. Means the project should not try to compete directly with image-based estimating in phase one. |
| **cap hpi integration** | Relevant to valuation/total-loss decisions. |
| **PlanManager** | Bodyshop workflow environment; relevant only if clients/repairers use it. |

## Audatex estimate fields useful for automation

A parser should extract:

- vehicle registration;
- VIN;
- estimate reference;
- repairer/bodyshop;
- insurer/work provider;
- estimate date;
- parts total;
- labour total;
- paint total;
- specialist/misc total;
- VAT;
- grand total;
- valuation/total-loss indicators;
- repair/replace operations;
- ADAS/calibration references;
- alignment/suspension references;
- airbag/SRS/safety references;
- supplementary estimate marker.

## Audatex review flags

The system should flag, not conclude:

| Flag | Why it matters |
|---|---|
| Reg mismatch | Possible wrong estimate or instruction. |
| Claim ref mismatch | Evidence may belong to another matter. |
| Estimate but no images | Desktop assessment may be blocked. |
| Supplementary estimate | Engineer may need to compare original vs supplementary. |
| ADAS keyword without calibration line | Potential safety/review issue. |
| Wheel/suspension keyword without alignment line | Potential omission. |
| Airbag/SRS keyword | Safety-critical issue. |
| Manual/misc lines | May require justification. |
| High repair cost vs value | Possible total-loss review. |

## AudaConnect caution

AudaConnect is the safer route for deeper integration because it is an Audatex-approved integration channel. Production discovery must confirm:

- whether Collision Engineers has Audatex access;
- whether they use AudaEnterpriseGold directly;
- whether they only receive Audatex PDFs from others;
- whether AudaConnect access is licensed;
- what data they are allowed to read/write;
- whether client contracts permit integration.

Do not propose scraping Audatex or reverse-engineering its proprietary data.

## Qapter caution

Audatex/Solera already offers AI tools for guided image capture, triage and intelligent estimating. That matters because “AI estimates repair cost from photos” is not the strongest first pitch.

The stronger angle is:

> “We organise, validate and route the evidence around existing estimating workflows.”

## ABP in plain English

ABP refers to Auto Body Professionals Club. The ABP Guide to Retail and Non-Contract Charges is a reference/benchmark used in UK body repair charge discussions, especially where pricing is retail or non-contract rather than under a pre-agreed insurer/bodyshop contract.

It is not Audatex, not a repair platform, not law and not a mandatory tariff.

## Current ABP note

A web check on 2026-05-22 found ABP listing the **2026 Guide to Retail and Non-Contract Charges** and a news item saying it was available online from 8 December 2025. The 2025 guide remains relevant for 2025-dated repair disputes, but 2026 is current for new 2026 matters.

## ABP charge-review assistant

A useful module would read an estimate, invoice, insurer challenge or engineer note and flag charge categories that often need evidence:

- wheel alignment;
- ADAS reset/calibration;
- research/methods charges;
- clamp and pull;
- non-standard repair operations;
- quality control time;
- tyre replacement;
- energy/environmental charges;
- BS10125/manufacturer approval charges;
- mobility/storage/recovery charges.

## ABP output should be a review pack

Example output:

```text
This item has been challenged under ABP-style retail/non-contract guidance.
Evidence required:
- relevant repair method;
- image reference;
- damage location;
- ADAS/sensor involvement;
- justification for operation;
- estimate/invoice line reference.
```

The AI should not decide the legal recoverability or final reasonableness of the charge.

## Where Audatex and ABP meet in the workflow

```text
Instruction received
        ↓
Audatex / repair estimate parsed
        ↓
Estimate totals and operations extracted
        ↓
ABP-relevant charge categories flagged
        ↓
Images and repair evidence attached
        ↓
Engineer reviews reasonableness and technical support
        ↓
Draft rebuttal / report section prepared for sign-off
```

## Discovery questions specific to Audatex/ABP

1. Do they use Audatex directly or mainly receive Audatex PDFs from repairers/insurers?
2. Which products are involved: AudaEnterpriseGold, Qapter, PlanManager, AudaConnect or only PDF exports?
3. Are estimates received as PDFs, screenshots, networked assessments or exports?
4. Do they have AudaConnect/API access?
5. Do they create Audatex estimates, review third-party estimates, or both?
6. Which estimate sections consume the most engineer time?
7. How often are supplementaries involved?
8. Are ABP disputes frequent enough to justify a dedicated charge-review workflow?
9. Which charge categories are most frequently challenged?
10. Should the ABP assistant produce internal notes only, or draft client-facing rebuttal sections?
