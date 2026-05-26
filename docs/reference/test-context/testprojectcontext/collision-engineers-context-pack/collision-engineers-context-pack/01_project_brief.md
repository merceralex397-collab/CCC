# 01 — Project Brief

Generated: 2026-05-22

## Working title

**Collision Engineers AI Case Intake and Engineer Pack System**

## One-sentence project definition

Build an AI-assisted workflow layer that receives instruction PDFs, repair estimates, vehicle images and notes; matches them into the correct matter; flags missing or inconsistent evidence; and prepares an engineer-ready assessment pack for human review.

## The business problem

The project notes point to a consistent operational problem:

1. A work provider sends an instruction PDF.
2. Images, estimates or supporting documents may arrive separately.
3. Incomplete or unmatched items sit in a “holding pen”.
4. Admin staff manually reconcile the instruction, images, estimates, references and booking requirement.
5. An engineer receives the case only after the evidence is organised.
6. The final report remains technical, evidential and human-signed.

The main inefficiency is therefore **case reconciliation**, not final expert judgement.

## Best proposal angle

Use this positioning:

> “We will build an AI-assisted case intake, evidence matching and report-preparation workflow. The system prepares the case file, highlights missing information and drafts structured text. Qualified engineers remain responsible for technical opinions, conclusions and final report approval.”

Avoid this positioning:

> “We will build an AI that writes engineering reports.”

The second phrase sounds risky because the firm works in legal, insurance, expert-witness and potentially criminal-evidence contexts.

## Plain-English explanation

An **AI workflow layer** means software that sits between their incoming communications and the engineer. It does not replace existing industry tools like Audatex. It reads and organises files, checks whether the right evidence is present, suggests matches, drafts safe admin text, and gives the engineer a cleaner starting point.

## Why this is commercially relevant

Collision Engineers sells speed, clarity and defensible independent technical evidence. Admin friction directly undermines that value proposition. A better intake layer should improve:

- case turnaround;
- fewer missing-document chasers;
- fewer wrongly matched photos or estimates;
- faster engineer allocation;
- more consistent report preparation;
- better audit trails;
- management visibility over work in progress.

## Primary users

| User | Need |
|---|---|
| Admin / new business staff | Triage incoming work, match files, chase missing evidence, update status. |
| Vehicle engineer / VDA | Receive a clean pack with key facts, estimate summary, photos and questions. |
| Manager / director | Track throughput, bottlenecks, case status and workload. |
| Client/work provider | Receive faster acknowledgement, clearer chasers and more consistent turnaround. |

## Phase-one product name

**AI Case Intake + Engineer Pack Generator**

## Phase-one output

A demo web application that takes a small batch of uploaded files and produces:

- structured case record;
- document classifications;
- extracted identifiers;
- evidence-matching suggestions;
- holding-pen status;
- missing-information checklist;
- engineer assessment pack;
- draft chaser/admin response.

## Decision boundary

The AI may:

- classify documents;
- extract fields;
- summarise instructions;
- match documents by identifier and context;
- flag missing evidence;
- draft non-final report sections;
- draft admin/chaser messages;
- prepare an engineer pack.

The AI should not:

- issue final expert opinions;
- decide fraud;
- decide liability;
- certify roadworthiness;
- override Audatex calculations;
- bypass Audatex licensing or APIs;
- send external communications without user approval.

## Success criteria

The phase-one demo succeeds if it proves this statement:

> “A messy inbound batch can be turned into a structured, reviewable, engineer-ready case pack faster and more consistently than manual handling.”

Suggested measurable targets for a later live pilot:

- 50%+ reduction in admin time spent reading PDFs to populate a case row.
- 50%+ reduction in unmatched/misfiled evidence.
- A clear status for every open case.
- Pack generation within minutes of complete evidence arrival.
- Every AI decision traceable to source files and human approval status.
