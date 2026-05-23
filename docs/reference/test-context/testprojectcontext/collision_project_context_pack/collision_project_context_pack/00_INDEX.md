# Collision Project Context Pack

Generated: 2026-05-22  
Project: Collision Engineers automation centre  
Purpose: provide a structured handoff pack for the project so future chats, agents, developers, and stakeholders can quickly understand what is being built, why it matters, and what remains unresolved.

## Important scope note

This pack is based on the project context available in this chat/project environment. The accessible context states that Collision Engineers wants to automate a workflow involving Outlook, Box, a niche system called EVA, PDFs, images, spreadsheets, JSON imports, and possibly APIs. If there were discussions outside this visible context, those details were not available here and should be imported into a later revision.

## Project summary

Collision Engineers receives PDF files by email. Images may arrive with the same email or in a separate email. The files are stored in Box. A human currently reads the PDF, copies data into a spreadsheet, uploads/stores the file in Box, and then manually adds the data to EVA. The objective is to automate as much of that intake, extraction, validation, storage, spreadsheet update, and EVA import process as possible.

## Recommended reading order

1. [01_PROJECT_BRIEF.md](01_PROJECT_BRIEF.md) — business objective, scope, and success criteria.
2. [02_CURRENT_STATE_AND_MANUAL_PROCESS.md](02_CURRENT_STATE_AND_MANUAL_PROCESS.md) — current workflow and pain points.
3. [03_TARGET_OPERATING_MODEL.md](03_TARGET_OPERATING_MODEL.md) — desired future workflow.
4. [04_SYSTEMS_AND_INTEGRATION_CONTEXT.md](04_SYSTEMS_AND_INTEGRATION_CONTEXT.md) — Outlook, Box, EVA, spreadsheet, and automation layer.
5. [08_DATA_EXTRACTION_AND_AI_STRATEGY.md](08_DATA_EXTRACTION_AND_AI_STRATEGY.md) — PDF/image extraction approach.
6. [09_DATA_MODEL_AND_JSON_CONTRACTS.md](09_DATA_MODEL_AND_JSON_CONTRACTS.md) — canonical data model and sample JSON.
7. [14_IMPLEMENTATION_ROADMAP.md](14_IMPLEMENTATION_ROADMAP.md) — practical phased delivery.
8. [19_AGENT_HANDOFF_CONTEXT.md](19_AGENT_HANDOFF_CONTEXT.md) — concise context to paste into a future AI/agent session.
9. [20_SELF_REVIEW_AND_COVERAGE_CHECK.md](20_SELF_REVIEW_AND_COVERAGE_CHECK.md) — coverage check against the project brief.

## File inventory

| File | Role |
|---|---|
| 00_INDEX.md | Master index and scope note. |
| 01_PROJECT_BRIEF.md | Project definition, goals, non-goals, success criteria. |
| 02_CURRENT_STATE_AND_MANUAL_PROCESS.md | Current process, known manual steps, operational pain. |
| 03_TARGET_OPERATING_MODEL.md | End-to-end desired future workflow. |
| 04_SYSTEMS_AND_INTEGRATION_CONTEXT.md | System roles, integration assumptions, source references. |
| 05_OUTLOOK_INTAKE.md | Email intake, attachments, separate image emails, correlation logic. |
| 06_BOX_STORAGE_AND_METADATA.md | Box storage design, folder structure, metadata, naming. |
| 07_EVA_INTEGRATION.md | EVA import/API integration strategy, assumptions, error handling. |
| 08_DATA_EXTRACTION_AND_AI_STRATEGY.md | PDF parsing, OCR, AI extraction, validation, confidence. |
| 09_DATA_MODEL_AND_JSON_CONTRACTS.md | Canonical fields, JSON examples, spreadsheet mapping. |
| 10_WORKFLOW_STATES_AND_ORCHESTRATION.md | State machine, idempotency, orchestration model. |
| 11_EXCEPTION_HANDLING_AND_HUMAN_REVIEW.md | Human review queue, exception taxonomy, escalation. |
| 12_SECURITY_PRIVACY_AND_GOVERNANCE.md | Permissions, audit, data protection, retention. |
| 13_TESTING_QA_ACCEPTANCE_CRITERIA.md | Test plan, acceptance criteria, evaluation harness. |
| 14_IMPLEMENTATION_ROADMAP.md | Delivery phases, milestones, dependencies. |
| 15_AUTOMATION_CENTRE_OPERATING_MODEL.md | Wider automation-centre architecture and operating model. |
| 16_MONITORING_OBSERVABILITY_AND_RUNBOOKS.md | Monitoring, dashboards, alerts, operational runbooks. |
| 17_OPEN_QUESTIONS_AND_DECISION_LOG.md | Known unknowns and decision register. |
| 18_GLOSSARY.md | Plain-English definitions of technical and AI terms. |
| 19_AGENT_HANDOFF_CONTEXT.md | Compact future-agent/project handoff prompt. |
| 20_SELF_REVIEW_AND_COVERAGE_CHECK.md | Coverage matrix and work-check. |

## Context categories used throughout

- **Confirmed context** means it came from the visible project instructions or this chat.
- **Recommended design** means a proposed architecture or process that fits the known requirements.
- **Assumption** means it should be verified before build or procurement.
- **Open question** means a missing detail that affects implementation.


## Source references checked on 2026-05-22

The documents below use these official/public sources where vendor-specific behaviour matters:

- Microsoft Graph Outlook Mail API overview: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview?view=graph-rest-1.0
- Microsoft Graph create subscription/change notification API: https://learn.microsoft.com/en-us/graph/api/subscription-post-subscriptions?view=graph-rest-1.0
- Microsoft Graph Outlook change notifications overview: https://learn.microsoft.com/en-us/graph/outlook-change-notifications-overview
- Box Webhooks overview: https://developer.box.com/guides/webhooks
- Box V2 Webhooks: https://developer.box.com/guides/webhooks/v2
- Box metadata instances: https://developer.box.com/guides/metadata/instances/create
- Box AI Extract Structured API: https://developer.box.com/reference/post-ai-extract-structured
- ICO UK GDPR data protection principles: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/
- ICO personal data guidance: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/personal-information-what-is-it/what-is-personal-data/what-is-personal-data/
- ICO personal data breach guide: https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/
