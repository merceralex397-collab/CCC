# Docs Plans Workspace Expansion Plan

Date: 2026-05-23
Status: active planning record
Owner: unassigned
Created: 2026-05-23
Last reviewed: 2026-05-23
Source links: `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md`, `docs/reference/originalplanning/`, `docs/reference/originalplanning/originalplans_output/phase_new_system.md`, `docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/00_README_PLAN_INDEX.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md`, `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md`
Roadmap milestone: Pre-code planning structure
Dependencies: all-ideas ledger, source synthesis, original planning packs, source manifest
Expected outputs: formal `docs/plans/` workspace taxonomy for every reference-derived planning family
Acceptance criteria: every original planning pack and all-ideas ledger domain has an owning planning workspace; the mature end-to-end platform has a first-class planning home
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/initial-repo-setup/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Expand `docs/plans/` from a small set of active implementation folders into a complete planning workspace structure for the whole CCC programme.

The all-ideas ledger currently captures 177 planned items across S0-S6. This plan assigns those ideas to durable folders so future work can be promoted into scoped plans, tickets, option papers, and archives without losing long-horizon work.

## Original Planning Coverage Checked

`docs/reference/originalplanning/` contains 143 files:

| Pack | Files | Planning signal |
| --- | ---: | --- |
| `ce_phase4_agents_reviewed_plan` | 16 | Agent/automation boundaries, intake, missing info, valuation, image matching, engineer support, operations intelligence, governance. |
| `ce_system_plans_enhanced` | 14 | Enhanced MVP and mature platform plan, data model, mapper extraction, Outlook, Box, dashboard, EVA/Sentry, engineer pack, provider migration, rollout. |
| `cedocumentmapper_rebuild_plan_pack_all_zips` | 6 | Parser rebuild, automation enhancement, EVA API enhancement, delivery roadmap, risks. |
| `collision_engineers_ai_tools_plans_markdown` | 35 | Individual AI/tool/MCP/skill plans for EVA, Outlook, Box, vehicle intelligence, valuation, extraction, evidence, estimates, communications, governance, tooling, ANDIE. |
| `collision_engineers_bulk_data_research_pack` | 27 | MOT/DVSA, mileage, vehicle identity, valuation, salvage, duplicate evidence, weather, road/traffic context, data quality, analytics, schema contracts. |
| `originalplans_output` | 9 | Earlier phase plans, including new case-intake system and bespoke end-to-end system. |
| `phase7_expanded_markdown_plan` | 36 | Expanded backlog, dependencies, governance, external integrations, portal/API, warehouse, scheduling, estimates, RAG, invoice/payment, historical search. |

The "new system that combines everything" is real and should not be hidden inside domain folders. Its main source files are:

- `docs/reference/originalplanning/originalplans_output/phase_new_system.md`: near-term integrated case-intake and management platform.
- `docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md`: Phase 6 bespoke end-to-end system.
- `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/00_README_PLAN_INDEX.md`: explains that those two plans describe the same target platform at different maturity levels.
- `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md`: detailed mature single-platform plan.
- `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md`: broader reusable automation-centre model.
- `docs/architecture/future_system_convergence.md`: current active canonical summary of how later modules attach to the shared spine.

## Further Category Audit

A second pass over the original planning headings, Phase 7 matrices, AI-agent phase plan, and context-pack coverage audit found these categories were too implicit in the first taxonomy and should be first-class planning homes:

| Missing or under-specified category | Why it needs a folder |
| --- | --- |
| Parser/extraction service | The CE Document Mapper rebuild, central extraction service, OCR fallback, field extraction, file triage, and regression corpus are a large workstream, not just a sub-note under Operational Core. |
| Case workflow and state | Work item state store, holding pen, review queue, audit trail, missing-info state, duplicate/historical search, and job-sheet replacement appear repeatedly as the operational spine. |
| Provider/principal/garage configuration | Provider settings, principal and garage migration, mapping assistant, routing metadata, and provider coverage are large enough to outgrow parser tickets. |
| Automation centre | The context pack has a reusable automation-centre model with intake connectors, document services, workflow engine, integration adapters, governance, observability, and operating cadence. That is broader than the first Operational Core slice. |
| AI agents | The original Phase 4 plan separates agents from tools: inbox triage, missing-info, valuation/uplift, engineer support, and continuous learning agents. These need their own plan home so they are not hidden inside generic AI tooling. |
| MCP and tool surface | The AI tools pack has named MCP plans for EVA/Sentry, Outlook Graph, Box, DVLA/DVSA, job-sheet bridge, observability, and the MCP security gateway. These are platform/tool contracts, not ordinary product tickets. |
| Agent skills | Case summary, missing-info drafting, CE style, valuation explanation, report-clause RAG, AI literacy, and training modules are reusable skills. They should be planned as a skills catalogue with prompts, evaluations, policies, and release controls. |
| User experience and interfaces | Dashboard/UI, case detail, review screens, internal portal/Teams front door, engineer PWA/mobile, and admin UI recur across plans and need coordinated design. |
| Finance and billing | Invoice, fee-note, payment status, payment chaser, and portal/payment automation are distinct from evidence review and partner APIs. |

## Planned `docs/plans/` Workspaces

| Folder | Purpose | Goes here |
| --- | --- | --- |
| `docs/plans/initial-repo-setup/` | Existing pre-code workspace. | Repo scaffold, documentation hierarchy, source manifest, raw evidence rules, reference audit, all-ideas ledger, plan lifecycle. |
| `docs/plans/operational-core/` | Existing first executable implementation workspace. | Parser MVP, provider config baseline, work item store, review queue, EVA JSON export, Box-ready package, P0-P3 execution tickets. This stays as the first delivery slice, not the only planning home for those domains. |
| `docs/plans/unified-platform/` | Mature end-to-end platform that combines the programme. | Full case management platform, automation centre spine, case database, workflow engine, role model, web/PWA/mobile surfaces, legacy decommissioning, system-wide convergence roadmap. |
| `docs/plans/automation-centre/` | Deterministic automation patterns and reusable operating model. | Workflow engine, trigger/event model, automation cadence, queue/retry/idempotency patterns, exception routing, automation KPIs, reusable service boundaries, automation-vs-agent promotion rules. |
| `docs/plans/parser-extraction/` | Parser, document extraction, and CE Document Mapper evolution. | Ground-up compatible mapper rebuild, central extraction service, PDF/DOCX/DOC/MSG/EML/image parsing, OCR/cloud fallback options, field extraction, schema mapping, provider-rule extraction behavior, regression corpus. |
| `docs/plans/case-workflow-state/` | Case/work-item state and operational workflow spine. | Work item state store, holding pen, review queue, audit event stream, missing-info checklist/state machine, duplicate case service, historical search, merge/link/split workflow, job-sheet replacement. |
| `docs/plans/provider-principal-config/` | Provider, principal, garage, and routing configuration. | Provider presets, principal/garage migration, mapped principals, provider coverage gaps, composite mappings, provider admin UI, provider mapping assistant, routing metadata, contacts and delivery rules. |
| `docs/plans/intake-storage-integrations/` | Intake channels and integration adapters. | Outlook Graph intake, mailbox polling, separate image-email correlation, Box metadata/upload, EVA/Sentry API adapter, website/WhatsApp intake metadata, spreadsheet bridge. |
| `docs/plans/evidence-estimate-review/` | Evidence, images, estimates, and review tools. | Evidence matching, duplicate/reused evidence, image quality, visible VRM matching, image ordering, Audatex estimate parsing, ABP charge review, ANDIE-style damage workbench. |
| `docs/plans/vehicle-valuation-data/` | Vehicle intelligence and valuation support. | DVLA/DVSA, MOT bulk/delta ingestion, mileage estimation, mileage anomalies, vehicle identity normalization, valuation evidence store, salvage benchmarking, prior total loss review. |
| `docs/plans/engineer-communications/` | Engineer pack and communication workflows. | Engineer pack generator, template manager, report drafting assistant, engineer copilot, missing-info chasers, CE style communication, status summaries, report-clause/RAG support. |
| `docs/plans/ai-agents/` | Bounded workflow agents that orchestrate tools under human approval. | Inbox triage agent, missing-information agent, valuation/uplift agent, engineer support agent, continuous learning agent, agent-vs-automation decision framework, permission levels, escalation and approval boundaries. |
| `docs/plans/mcp-and-tooling/` | MCP servers, internal tool adapters, and tool security gateway. | EVA/Sentry MCP, Outlook Graph MCP, Box storage MCP, DVLA/DVSA MCP, job-sheet/spreadsheet bridge MCP, observability MCP, tool registry, MCP security gateway, schemas, audit, rate limits, safe tool discovery. |
| `docs/plans/agent-skills/` | Reusable staff/engineer-facing agent skills. | Case summary skill, missing-info chaser drafter, CE style communication skill, valuation explanation skill, report-clause/RAG skill, AI literacy/training skill, skill prompt/version/evaluation lifecycle. |
| `docs/plans/ai-platform-tools/` | Governed AI platform layer behind tools, skills, and agents. | Model hosting, evaluation datasets, prompt/version governance, document mapper learning loop, model feedback loop, redaction/training-data controls, AI policy implementation. |
| `docs/plans/user-experience-interfaces/` | Human-facing screens and interaction design across staff, engineer, and admin workflows. | Dashboard, holding pen UI, case detail page, review screens, parser UI, admin UI, internal portal/Teams front door, engineer PWA/mobile, accessibility and adoption checks. |
| `docs/plans/finance-billing/` | Finance, invoice, fee-note, and payment workflow. | Invoice/fee note generation, payment status tracking, payment chaser metadata, repairer portal payment evidence, finance approvals, payment automation option papers. |
| `docs/plans/governance-security/` | Cross-programme controls. | DPIA, vendor governance, privacy, PII redaction, public/commercial data licensing, expert-evidence boundary, risk-language policy, API security. |
| `docs/plans/operations-quality/` | Delivery, QA, rollout, and operational reliability. | Test corpus, regression harness, release/rollback, monitoring, runbooks, pilot rollout, decommissioning, integration sandbox testing. |
| `docs/plans/analytics-data-platform/` | Data, analytics, historical mining, and BI. | Operations analytics, client/principal intelligence, data quality metrics, data warehouse, EVA report mining, risk indicators, predictive scheduling, continuous improvement, bulk data architecture. |
| `docs/plans/external-platform-partners/` | External-facing and partner systems. | Customer portal, external partner API, insurer platform integrations, Audatex/estimating partnerships, payment workflow automation, partner access controls. |
| `docs/plans/product-business/` | Business framing and non-code product planning. | Discovery, ROI/KPI tracking, client pitch, conservative positioning, objection handling, independence/defensibility. |

## Standard Workspace Structure

Every new top-level workspace should use this structure:

```text
docs/plans/<workspace>/
  README.md
  source_map.md
  roadmap.md
  tickets/
    README.md
  option-papers/
    README.md
  archived_plans/
    implemented/.gitkeep
    superseded/.gitkeep
```

`README.md` defines purpose, ownership, planning rules, and source scope.

`source_map.md` maps originalplanning, test-context, raw evidence, normalized companions, and current canonical docs into the workspace.

`roadmap.md` groups the work into phases, dependencies, and promotion order.

`tickets/` holds executable implementation tickets once items are promoted.

`option-papers/` holds decision work before implementation, especially for integrations, vendors, AI, privacy, and partner/API choices.

`archived_plans/` mirrors the implemented/superseded lifecycle used by existing plan workspaces.

## Workspace Ownership Rules

Every originalplanning pack must be represented in at least one workspace `source_map.md`.

Every all-ideas ledger row must have exactly one primary planning workspace, even if it cross-links to supporting workspaces.

The `unified-platform/` workspace owns the system-wide target architecture and migration/decommissioning roadmap. It does not replace the specialist folders; it coordinates them.

The `operational-core/` workspace becomes the first-slice coordination workspace after the split. It should retain source synthesis, roadmap/backlog coordination, MVP interlock, cross-workspace dependency sequencing, and any truly cross-cutting P0 foundation items. It should not remain the physical home for parser, provider configuration, case-state, integration, UI, intelligence, analytics, or partner tickets once their owning workspaces exist.

The `automation-centre/` workspace owns deterministic automation architecture: triggers, workflows, retries, event logs, exception routing, observability hooks, and operating cadence. It coordinates with domain workspaces that own their specific adapters or screens.

The `ai-agents/`, `mcp-and-tooling/`, and `agent-skills/` workspaces are deliberately separate:

- `mcp-and-tooling/` owns callable business tools and MCP servers, including schemas, auth boundaries, audit, rate limits, and the tool registry/security gateway.
- `agent-skills/` owns reusable natural-language skills, prompt/version lifecycle, skill-specific evaluations, and staff-facing drafting/summarisation/training behaviours.
- `ai-agents/` owns orchestrators that choose among approved tools and skills to investigate or propose actions under permission levels.

Domain-specific active work must move to its owning workspace as part of this taxonomy implementation. Do not leave duplicate active tickets behind in `operational-core/`; update links and indexes to the new paths.

Governance-gated areas must start in `option-papers/`, not `tickets/`: cloud OCR, external APIs, portal/payment automation, WhatsApp send automation, valuation providers, DVLA/DVSA, Audatex partnerships, AI/RAG, and EVA/Sentry submit.

## Detailed Workspace Mapping and Reference Verification

To ensure planning plans for each workspace are detailed and verified with raw evidence, the workspaces will own and enforce the following fact-checked requirements derived from `docs/reference/raw/collisionrelateddocs/`:

1. **Unified Platform (`unified-platform/`)**
   - *Reference Evidence*: `handover.docx` (Section: "The Job Sheet").
   - *Key Constraints*: Retires the legacy Excel Job Sheet (`Backup of CE Job Sheet 260429.xlsm` / `Backup of CE Job Sheet 260309.xlsm`). Must translate VBA logic (`CreateNewRow`, `FolderCreator`, `RowMover`) into secure server-side database workflows. Addresses the Excel Desktop collaboration issues (which cause sync corruption online) by migrating to a concurrent Postgres case store.
   - *Infrastructure Facts*: Replaces local Z network drive sharing configurations (`\\PGUSER\Report Images` private Private private password-protected sharing, Windows account credentials e.g., `PGUSER3945 / password`) with cloud storage hooks.

2. **Automation Centre (`automation-centre/`)**
   - *Reference Evidence*: `10_WORKFLOW_STATES_AND_ORCHESTRATION.md`, `15_AUTOMATION_CENTRE_OPERATING_MODEL.md`.
   - *Key Constraints*: Implements deterministic triggers, idempotency checks, event logging, and retry queues. Exposes observability hooks and exceptions (e.g., stuck case routing, mismatched images alerts) for administrative triage.

3. **Parser Extraction (`parser-extraction/`)**
   - *Reference Evidence*: `handover.docx` (Section: "CE Document Mapper" / "Image Extraction" / "OCR"), `app_settings.json`, `providers.json`.
   - *Key Constraints*: Rebuilds Document Mapper functionality. PDF native extraction cascade using PyMuPDF first, then pdfplumber, and pypdf.
   - *OCR Fallback Rule*: Trigger OCR on PDF if and only if it has a single image on each page and is less than 3 pages long (1 or 2 pages only). Otherwise, preserve as images for extraction.
   - *Audit Mode Rule*: Overwrites fields in red outline when a document is imported as an "Engineer Report" (checked for CNX and EVA presets). Processes instruction and engineer reports in the correct order.
   - *Decoders & Cleanups*: Handles odd-glyph PDF decoding, `/uniXXXX` unicode cleanup, and BEL control-character removal.
   - *Extraction Methods*: Replicates Single Label (takes next non-empty line if same line is empty), Two Labels, Fixed Position, Fixed Position + Label, Single Label +/-, and Email Date (MSG date extraction).

4. **Case Workflow State (`case-workflow-state/`)**
   - *Reference Evidence*: `handover.docx` (Section: "The Job Sheet" / "Conditional Formatting").
   - *Key Constraints*: Replicates the Excel spreadsheet rules:AA Table Locators (`T1_START`, `T2_START`), row 6 icon templates (`AB6`), Row I "Add New Row" anchor. Rules for conditional formatting apply to columns `=C:C` (dates), `=I:I` (instruct status), and `=D:D` (names), matching the VBA logic.
   - *Workflow Gates*: Unresolved, ambiguous, or mismatch cases are routed to the holding pen.

5. **Provider Principal Config (`provider-principal-config/`)**
   - *Reference Evidence*: `Mapped Principals.xlsx`, `providers.json`.
   - *Key Constraints*: Preserves settings layout currently in `CE Document Mapper/providers.json`. Ensures coverage for the 26 presets (e.g., ALISON, TEN, KERR). Coordinates principal coverage gaps identified in `Mapped Principals.xlsx` (lost cause ACSP due to low OCR quality; ALISON format inconsistencies; composite provider rules e.g. `OAK/AX`).

6. **Intake Storage Integrations (`intake-storage-integrations/`)**
   - *Reference Evidence*: `handover.docx` (Section: "Copilot - Query Response Drafter" / "EVA"), `Sentry_API_Complete_Guide.md`.
   - *Key Constraints*:
     - *Mailbox Integration*: Outlook Graph connection to delegated mailboxes `desk@collisionengineers.co.uk`, `engineers@collisionengineers.co.uk`, and `info@collisionengineers.co.uk` under the main `digital@collisionengineers.co.uk` account.
     - *Sentry/EVA API Integration*: Enforces the Sentry API v1.2 REST protocol. JWT authentication requires obtaining tokens via `POST /Connect/token` with urlencoded Client_Id and Client_Secret, handling 5-minute token expiration and 30-second pre-expiry refresh buffer in memory. Implements write endpoints: `POST /Instruction/Inspection` (with base64 file attachments), `POST /Claim/LocationUpdate` (validating conditional keys `ClmNo + VehReg` or `EVARef + VehReg`), `POST /Claim/AuthorityStatusUpdate`, `POST /Note/SubmitNote`, `POST /Claim/Update` (updating Excess and VAT), and `POST /Report/SubmitReport`.
     - *EVA Installer Configuration*: Quick code `22571` for setup, installs Minotaur PDF Printer, and triggers updates.
     - *Box Integration*: Implements local Box-ready package generation (`evidence_package_contract_v1.md`) before live folder upload.

7. **Evidence Estimate Review (`evidence-estimate-review/`)**
   - *Reference Evidence*: `Standard Audatex Invoice.docx`, handover section "base44" (A.N.D.I.E damage assessment platform WIP).
   - *Key Constraints*: Checks image quality (excluding low-quality images like ACSP), matches VRM in images to instruction metadata, and parses Audatex estimates to generate QA review summaries (ADAS, calibration, SRS flags).

8. **Vehicle Valuation Data (`vehicle-valuation-data/`)**
   - *Reference Evidence*: `04_mileage_estimation_engine.md`, `08_dvla_vrm_attribute_cache.md`.
   - *Key Constraints*: Normalizes VRM lookup cache from DVLA, estimates MOT-based mileage trends, and flags mileage anomalies (e.g., odometer decreases or sudden jumps).

9. **Engineer Communications (`engineer-communications/`)**
   - *Reference Evidence*: `CE Communication Style & Tone Profile.docx`.
   - *Key Constraints*: Generates the complete engineer briefing pack. All draft communications and chasers must strictly apply the Collision Engineers tone profile (concise, factual, objective, neutral, with zero speculative assumptions or added facts).

10. **AI Agents (`ai-agents/`)**
    - *Reference Evidence*: `handover.docx` ("Copilot - Query Response Drafter" delegated mail access sync issues).
    - *Key Constraints*: Governs the AI inbox triage and missing-info agents. Mandates delegated mailbox queries explicitly instruct search on the delegated shared folders (`desk@`, `engineers@`, `info@`). Prohibits autonomous external emailing or report sign-off without human-in-the-loop review.

11. **MCP and Tooling (`mcp-and-tooling/`)**
    - *Reference Evidence*: `collision_engineers_ai_tools_plans_markdown/`.
    - *Key Constraints*: Exposes tool interfaces for EVA, Outlook Graph, Box, DVLA, and spreadsheet bridge with schema contracts, rate limits, and audit logs.

12. **Agent Skills (`agent-skills/`)**
    - *Reference Evidence*: Claude team plan shared projects, Andy's bot.
    - *Key Constraints*: Specifies portable natural-language prompts. Prompts must be independent of hosting, enabling reuse in the CE platform, Claude Desktop, ChatGPT, or Teams.

13. **AI Platform Tools (`ai-platform-tools/`)**
    - *Reference Evidence*: `25_model_evaluation_feedback_loop.md`.
    - *Key Constraints*: Evaluates prompt versions, logs AI invocations, and captures reviewer corrections to update prompt templates.

14. **User Experience Interfaces (`user-experience-interfaces/`)**
    - *Reference Evidence*: `handover.docx` ("CE CMS Design" rough sketch), `07_ui_dashboard_spec.md`.
    - *Key Constraints*: Designs dashboard layouts, review queues, parser warning overrides, and the holding pen UI.

15. **Finance and Billing (`finance-billing/`)**
    - *Reference Evidence*: `Website Invoice Template.docx`, `Standard Audatex Invoice.docx`.
    - *Key Constraints*: Generates draft customer invoices and tracks payment status metadata.

16. **Governance and Security (`governance-security/`)**
    - *Reference Evidence*: `governance_security.md`, `dpia_vendor_governance.md`.
    - *Key Constraints*: Enforces PII redaction, vendor register DPIA, data protection, and the expert-evidence boundary.

17. **Operations and Quality (`operations-quality/`)**
    - *Reference Evidence*: `release_and_rollback.md`, `monitoring_runbooks.md`.
    - *Key Constraints*: Manages gold-standard regression corpus, release/rollback checks, and runbooks.

18. **Analytics and Data Platform (`analytics-data-platform/`)**
    - *Reference Evidence*: `20_job_sheet_and_operations_analytics.md`.
    - *Key Constraints*: Gathers BI metrics, turnaround queues, and error tracking.

19. **External Platform Partners (`external-platform-partners/`)**
    - *Reference Evidence*: Handover "base44" (WIP CarClaims landing page Ads figma design).
    - *Key Constraints*: Manages external APIs and client portals.

20. **Product and Business (`product-business/`)**
    - *Reference Evidence*: `16_client_pitch_and_positioning.md`.
    - *Key Constraints*: Measures ROI, savings, and handles client objections.


## Automation, AI Agent, MCP, And Skill Coverage

Yes, the reference material includes all four areas, but the taxonomy must make them explicit:

| Area | Existing source coverage | Owning workspace after this expansion |
| --- | --- | --- |
| Deterministic automation | `phase_initial_automation.md`, `15_AUTOMATION_CENTRE_OPERATING_MODEL.md`, Phase 7 workflow automation items, and P3/P5 integration tickets cover fixed workflows, intake connectors, adapter orchestration, retries, exceptions, monitoring, and automation KPIs. | `docs/plans/automation-centre/` for reusable automation architecture, with domain implementation tickets in intake/storage, case workflow, operations, finance, and external-platform workspaces. |
| AI agents | `phase_ai_agents.md` and `ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md` cover inbox triage, missing-information, valuation/uplift, engineer support, continuous learning, permission levels, and agent safety boundaries. | `docs/plans/ai-agents/`. |
| MCP plans | `collision_engineers_ai_tools_plans_markdown/01`, `02`, `03`, `04`, `20`, `26`, and `29` define EVA/Sentry, Outlook Graph, Box, DVLA/DVSA, job-sheet bridge, observability, and MCP security gateway plans. | `docs/plans/mcp-and-tooling/`, cross-linked from the affected domain workspaces. |
| Agent skills | `phase_ai_tools.md` and the AI tools pack define valuation, case summary, missing-info chaser, CE style, valuation explanation, report-clause/RAG, AI literacy, provider mapping, and engineer support skills. | `docs/plans/agent-skills/`, with domain cross-links to communications, valuation, provider config, engineer communications, governance, and AI platform. |

Boundary rule: automation executes known workflow steps; MCP/tools expose narrow callable capabilities; agent skills draft, summarise, explain, retrieve, or train; AI agents orchestrate approved tools and skills and must stop at human approval boundaries.

## Parser Extraction Vs Operational Core

`parser-extraction/` owns the subsystem that turns source files into reviewed structured data candidates. Its inputs are source files, provider/principal configuration, parser rules, and corpus fixtures. Its outputs are canonical parser results, extraction provenance, confidence/warnings, validation blockers, field evidence maps, and parser-specific UI/CLI behavior.

`operational-core/` owns the first end-to-end operating slice and its dependency coordination. It consumes parser outputs and coordinates work item state, review gates, package/export readiness, implementation sequencing, and cross-workspace acceptance. It should not own parser internals once `parser-extraction/` exists.

Boundary rule: if the question is "how do we read/classify/extract/map this document?", it belongs in `parser-extraction/`. If the question is "how does a reviewed case move through the business workflow?", it belongs in `operational-core/` coordination or the more specific owning workspace such as `case-workflow-state/`, `intake-storage-integrations/`, or `engineer-communications/`.

## Operational Core Split-Out Plan

Creating `parser-extraction/`, `case-workflow-state/`, and `provider-principal-config/` requires a real refactor of `docs/plans/operational-core/`, not just cross-links.

The implementation should move and split active planning files as follows:

| Current Operational Core item | New owning path | Refactor action |
| --- | --- | --- |
| `docs/plans/operational-core/parser-mvp/plan.md` | `docs/plans/parser-extraction/parser-mvp/plan.md` | Move the active parser MVP plan. Update its roadmap milestone, source links, archive target, and all references. |
| `p0-foundation.md` / `P0-003 Provider Coverage And Migration Baseline` | `docs/plans/provider-principal-config/tickets/p0-provider-coverage-migration-baseline.md` | Extract this ticket into the provider workspace. Leave a short dependency reference in Operational Core P0 only if needed. |
| `p0-foundation.md` / `P0-004 Parser MVP Implementation Plan` | `docs/plans/parser-extraction/tickets/p0-parser-mvp-implementation-plan.md` | Extract this ticket into the parser workspace and point it at the moved parser MVP plan. |
| `p1-operational-core-mvp.md` / `P1-001 Parser Core MVP` | `docs/plans/parser-extraction/tickets/p1-parser-core-mvp.md` | Extract into parser workspace. |
| `p1-operational-core-mvp.md` / `P1-002 Staff Parser UI` | `docs/plans/user-experience-interfaces/tickets/p1-staff-parser-ui.md` | Extract into UX workspace, with parser-extraction dependency. |
| `p1-operational-core-mvp.md` / `P1-003 Parser CLI Parity` | `docs/plans/parser-extraction/tickets/p1-parser-cli-parity.md` | Extract into parser workspace. |
| `p1-operational-core-mvp.md` / `P1-004 Provider Principal Admin UI` | `docs/plans/provider-principal-config/tickets/p1-provider-principal-admin-ui.md` | Extract into provider workspace. |
| `p1-operational-core-mvp.md` / `P1-005 Work Item And Review Queue` | `docs/plans/case-workflow-state/tickets/p1-work-item-review-queue.md` | Extract into case workflow workspace. |
| `p1-operational-core-mvp.md` / `P1-006 EVA JSON Export` | `docs/plans/intake-storage-integrations/tickets/p1-eva-json-export.md` | Extract into integration workspace as the first EVA/export adapter ticket. |
| `p1-operational-core-mvp.md` / `P1-007 Box-Ready Evidence Package Generation` | `docs/plans/intake-storage-integrations/tickets/p1-box-ready-evidence-package.md` | Extract into integration/storage workspace. |
| `p2-parser-hardening-provider-parity.md` | `docs/plans/parser-extraction/tickets/p2-parser-hardening.md` and `docs/plans/provider-principal-config/tickets/p2-provider-parity-uncovered-principals.md` | Split parser hardening from provider/principal parity. |
| `p3-integrations-storage-eva-intake.md` | `docs/plans/intake-storage-integrations/tickets/p3-integrations-storage-eva-intake.md`, with MCP wrappers split to `docs/plans/mcp-and-tooling/tickets/` where applicable | Move deterministic intake/storage/EVA adapter work to integrations. Extract EVA/Sentry, Outlook Graph, Box, and job-sheet MCP wrapper planning into MCP/tooling tickets or option papers. |
| `p4-intelligence-engineer-communications.md` | `vehicle-valuation-data/`, `evidence-estimate-review/`, `engineer-communications/`, `agent-skills/`, and `ai-agents/` ticket files | Split by ticket: valuation and DVLA/DVSA to vehicle/valuation; image intelligence to evidence/estimate; engineer pack and communications workflow to engineer/communications; reusable drafting/summary/RAG skills to agent-skills; any orchestration agent to ai-agents. |
| `p5-platform-expansion.md` | `analytics-data-platform/`, `external-platform-partners/`, `finance-billing/`, `governance-security/`, `automation-centre/`, `mcp-and-tooling/`, and `ai-platform-tools/` ticket files | Split by ticket: analytics and warehouse to analytics; portal/API and partner integrations to external partners; payment/fee-note items to finance; governance controls to governance-security; automation-centre operating model to automation-centre; tool registry/MCP gateway to MCP/tooling; model evaluation/prompt governance to AI platform. |

After the move, `docs/plans/operational-core/tickets/backlog_index.md` should become a coordination index that links to the owning workspace ticket files. It must not duplicate moved ticket content.

`docs/plans/operational-core/source_synthesis.md` should remain in Operational Core because it records original promotion decisions, but its canonical destinations must be updated to the new owning workspaces.

All active references to moved paths must be updated in `README.md`, `AGENTS.md`, `docs/docs_index.md`, `docs/repo_map.json`, `docs/plans/_index.md`, `docs/plans/operational-core/source_synthesis.md`, `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md`, `tools/verify_scaffold.py`, and `tools/scaffold_initial_repo.py`.

## Implementation Steps For This Taxonomy

1. Create the new top-level workspace folders listed above, including explicit `automation-centre/`, `ai-agents/`, `mcp-and-tooling/`, and `agent-skills/` homes.
2. Add the standard folder structure to each workspace.
3. Add a concise `README.md`, `source_map.md`, and `roadmap.md` to each workspace.
4. Move `docs/plans/operational-core/parser-mvp/plan.md` to `docs/plans/parser-extraction/parser-mvp/plan.md`.
5. Split `p0-foundation.md`, `p1-operational-core-mvp.md`, `p2-parser-hardening-provider-parity.md`, `p3-integrations-storage-eva-intake.md`, `p4-intelligence-engineer-communications.md`, and `p5-platform-expansion.md` according to the split-out table above.
6. Rewrite `docs/plans/operational-core/tickets/backlog_index.md` as a cross-workspace coordination index pointing to the new ticket locations.
7. Update `docs/plans/operational-core/source_synthesis.md` so canonical destinations point to owning workspaces, especially `unified-platform/`, `automation-centre/`, `parser-extraction/`, `case-workflow-state/`, `provider-principal-config/`, `ai-agents/`, `mcp-and-tooling/`, `agent-skills/`, and the P4/P5 owning workspaces.
8. Add a workspace assignment section to `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md`.
9. Update `docs/plans/_index.md` with the full workspace table and moved parser/ticket paths.
10. Update `docs/docs_index.md` and `docs/repo_map.json` so humans and agents can route work by planning area.
11. Update active references in `README.md`, `AGENTS.md`, and relevant plan/ticket files so old Operational Core paths are not used for moved active documents.
12. Update `tools/verify_scaffold.py` so it checks required new planning folders, README files, archive folders, source-map files, and moved parser/ticket paths.
13. Update `tools/scaffold_initial_repo.py` so regenerated scaffold docs preserve the same folder taxonomy and moved paths.
14. Regenerate `docs/source_manifest.md`, `docs/source_manifest.csv`, and `docs/source_manifest.json`.
15. Run a final stale-path search for old `docs/plans/operational-core/parser-mvp/` and moved ticket paths; only historical archived references may remain.

## Verification Plan

Run:

```powershell
python tools\verify_scaffold.py
python -m pytest tests\test_scaffold_contracts.py
python -m json.tool docs\repo_map.json
rg --files docs\reference\originalplanning | Measure-Object
rg -n "docs/plans/(unified-platform|automation-centre|parser-extraction|case-workflow-state|provider-principal-config|intake-storage-integrations|evidence-estimate-review|vehicle-valuation-data|engineer-communications|ai-agents|mcp-and-tooling|agent-skills|ai-platform-tools|user-experience-interfaces|finance-billing|governance-security|operations-quality|analytics-data-platform|external-platform-partners|product-business)" docs
```

Expected results:

- Scaffold verification passes.
- Existing scaffold contract tests pass.
- `docs/repo_map.json` is valid JSON.
- Originalplanning still reports 143 files.
- New planning folders are referenced from indexes, source maps, all-ideas planning, and manifests.

## Assumptions

- Existing `initial-repo-setup/` and `operational-core/` remain the first two canonical workspaces.
- `unified-platform/` is the correct home for the "new system / bespoke platform" material, while `automation-centre/` owns reusable deterministic automation patterns that can serve that platform and the nearer-term workflow.
- Parser/extraction, case workflow/state, and provider/principal config get dedicated workspaces now. Active Operational Core files that physically contain those tickets should be moved or split as part of this taxonomy implementation.
- This plan is documentation/planning structure only; it should not change parser code, contracts, CLI behavior, or runtime APIs.
- Operational Core remains as a coordination and dependency workspace after the split, not the long-term folder for every implementation domain.
- AI agents, MCP/tooling, and agent skills are intentionally separate because they have different risk boundaries, verification methods, and implementation artefacts.
