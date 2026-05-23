# Collision Engineers AI Automation Context Pack

Generated: 2026-05-22

This folder is a working knowledge pack for the Collision Engineers AI automation project. It consolidates the call notes, uploaded research, website extracts, Audatex/ABP context, demo planning, and implementation thinking into separate markdown files so the project can be handed to a developer, used for another client call, or turned into a proposal.

## Core conclusion

The recommended project is **not** “AI writes final engineering reports.” The recommended project is:

> **An AI-assisted case intake, evidence matching, and engineer-pack generation system for Collision Engineers.**

In plain terms: the system should take messy incoming work — instruction PDFs, vehicle images, Audatex/repair estimates, emails, notes and references — and turn it into a complete, checked, engineer-ready case file. The engineer still owns the technical judgement and final report.

## How to use this pack

Read these files in order for a complete understanding:

| Order | File | Purpose |
|---:|---|---|
| 1 | `01_project_brief.md` | One-page project framing and recommended positioning. |
| 2 | `02_company_business_context.md` | What Collision Engineers does and why the workflow matters. |
| 3 | `03_domain_glossary.md` | Plain-English explanations of AI, legal, vehicle and claims terminology. |
| 4 | `04_current_workflow_and_pain_points.md` | The inferred current workflow and operational pain points. |
| 5 | `05_target_workflow.md` | The proposed future workflow from intake to engineer review. |
| 6 | `06_mvp_demo_case_intake_engineer_pack.md` | Narrow first demo scope and acceptance criteria. |
| 7 | `07_ui_dashboard_spec.md` | Dashboard screens, buttons, states and user flows. |
| 8 | `08_technical_architecture.md` | Prototype and production architecture options. |
| 9 | `09_data_model_and_schemas.md` | Case, document, evidence, estimate, pack and audit data structures. |
| 10 | `10_ai_modules_and_prompts.md` | AI module breakdown and prompt/guardrail patterns. |
| 11 | `11_audatex_abp_industry_context.md` | Audatex, Qapter, AudaConnect and ABP charge-review relevance. |
| 12 | `12_compliance_governance_and_risk.md` | CPR, GDPR/DUAA, audit, data security and expert-signoff guardrails. |
| 13 | `13_implementation_roadmap_and_roi.md` | Phased delivery plan, KPIs and value model. |
| 14 | `14_discovery_questions_and_call_prep.md` | Questions and call script for the next conversation. |
| 15 | `15_demo_dataset_and_test_plan.md` | Synthetic demo data, test cases and acceptance tests. |
| 16 | `16_client_pitch_and_positioning.md` | Proposal language, follow-up copy and what not to claim. |
| 17 | `17_source_map_and_assumptions.md` | Source map, assumptions, verification notes and unknowns. |
| 18 | `18_work_check_coverage_audit.md` | Coverage audit confirming the generated pack includes the required areas. |

## Recommended first deliverable

Build a **local web demo** called **AI Case Intake + Engineer Pack Generator**.

The demo should accept:

- one instruction PDF;
- one Audatex or repair estimate PDF;
- several vehicle images;
- optional pasted email/WhatsApp/admin text.

It should output:

- a structured case record;
- matched documents/images;
- missing-information flags;
- confidence scores;
- an engineer-ready assessment pack;
- a draft chaser/client message.

## Non-goals for phase one

Do not lead with these in the first demo:

- autonomous final expert reports;
- autonomous fraud decisions;
- full Audatex replacement;
- repair-cost calculation from images;
- live WhatsApp/email sending;
- full calendar dispatch optimisation;
- production-grade legal evidence system.

Those can be later-phase discussions once the intake/reconciliation workflow is proven.

## Verification status

This pack is based on uploaded project sources plus a current web spot-check on 2026-05-22. The live-check items are summarised in `17_source_map_and_assumptions.md`.
