# Roadmap

Date: 2026-05-24
Status: active programme roadmap
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-25
Source links: `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md`, `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`, `docs/plans/operational-core/source_synthesis.md`, `docs/architecture/future_system_convergence.md`, `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/14_IMPLEMENTATION_ROADMAP.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/02_prioritised_roadmap.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: source manifest, workspace source maps, governance/security gates, operations-quality gates
Expected outputs: sequential implementation and planning order for all reference-derived workspaces
Acceptance criteria: every roadmap section points to an owning workspace and source-backed evidence; high-risk work is gated before implementation
Verification required: `python tools/verify_scaffold.py`
Archive target: owning workspace `archived_plans/implemented/`
Supersedes: previous P0-P5-only roadmap structure
Superseded-by: none

CCC starts with vehicle-damage instruction parsing and evidence preparation, then expands through controlled workflow, integrations, intelligence, AI/tooling, external ecosystem, analytics, and mature platform convergence. Collision Engineers do not do personal injury or KADOE work; those workflows remain out of scope.

## Current Status

Current position: Section 2 parser MVP execution is in progress on branch `codex/parser-mvp-full`. The first executable parser core, CLI, staff UI review surface, EVA export adapter, evidence package manifest, provider fixtures, corpus regression ledger, deterministic fallback extraction, and Tk drag/drop intake are implemented under `src/ccc_parser/`, `tools/`, and `docs/reference/data/`.

Current milestone: harden parser MVP implementation against review findings, provider field gaps, and release packaging after corpus regression reports zero reader-level blockers across the private `Instructions/` corpus.

Parser implementation status: executable MVP present. The active parser MVP plan is `docs/plans/parser-extraction/parser-mvp/plan.md`; the operational-core parser path is only a compatibility stub. Current verification commands are `python -m pytest`, `python tools/run_parser_corpus.py`, and `python tools/verify_scaffold.py`.

Current known parser review items: local OCR now recovers the short MP image-only PDFs when a Tesseract binary is available, folder parsing can merge one instruction with one engineer report without losing the instruction provider, and PR review fixes covered per-parse attachment workspaces, partial batch reporting, triaged source-hash reuse, and DOC converter timeouts. Three corpus items remain `UNKNOWN`/review-required because the source evidence is an image pack or lacks a configured inspection address; many provider presets still require staff review for mileage, mileage unit, VAT, or inspection address because those values are absent from current provider rules or source documents. The CNX parsertests gap has been resolved by deterministic fallback extraction and is pinned in `tests/parsertests/output1.json`. Current blockers are captured in `docs/reference/data/parser_corpus_regression_report.json` and `docs/reference/data/parser_corpus_fixture_ledger.json`.

Local repo skill status: installed at `C:/Users/PC/.codex/skills/ccc-repo-task-start` and planned/evaluated in `docs/plans/initial-repo-setup/local-repo-task-start-skill-plan.md`. This local development skill is separate from `docs/plans/agent-skills/`, which is reserved for production Collision Engineers skills.

## Source Basis

| Source | Why it is used |
| --- | --- |
| `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md` | Exhaustive ledger of reference-derived ideas and phases. |
| `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md` | Approved workspace taxonomy and split-out plan. |
| `docs/plans/operational-core/source_synthesis.md` | Current source-promotion map and generated-pack disposition. |
| `docs/architecture/future_system_convergence.md` | Convergence spine and scope guardrails for future modules. |
| `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/14_IMPLEMENTATION_ROADMAP.md` | Incremental delivery strategy from discovery through expansion. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/02_prioritised_roadmap.md` | Longer-horizon platform, portal, analytics, partner, and governance sequencing. |

## Workspace Plan Entry Points

| Workspace | Detailed plan | Purpose |
| --- | --- | --- |
| `docs/plans/unified-platform/` | `docs/plans/unified-platform/plan.md` | Mature end-to-end CCC platform planning and convergence roadmap. |
| `docs/plans/automation-centre/` | `docs/plans/automation-centre/plan.md` | Deterministic automation architecture, operating cadence, and reusable workflow patterns. |
| `docs/plans/parser-extraction/` | `docs/plans/parser-extraction/plan.md` | Parser, document extraction, CE Document Mapper evolution, and extraction-regression planning. |
| `docs/plans/case-workflow-state/` | `docs/plans/case-workflow-state/plan.md` | Canonical work-item state, review queue, audit stream, missing-info state, and historical search planning. |
| `docs/plans/provider-principal-config/` | `docs/plans/provider-principal-config/plan.md` | Provider, principal, garage, routing, and provider-rule lifecycle planning. |
| `docs/plans/intake-storage-integrations/` | `docs/plans/intake-storage-integrations/plan.md` | Intake channels, source capture, storage adapters, EVA/Sentry adapters, and transitional spreadsheet bridge planning. |
| `docs/plans/evidence-estimate-review/` | `docs/plans/evidence-estimate-review/plan.md` | Evidence matching, image review, estimate parsing, ABP review, and damage workbench planning. |
| `docs/plans/vehicle-valuation-data/` | `docs/plans/vehicle-valuation-data/plan.md` | Vehicle identity, DVLA/DVSA, MOT, mileage, valuation evidence, salvage, and vehicle-history support. |
| `docs/plans/engineer-communications/` | `docs/plans/engineer-communications/plan.md` | Engineer pack, template, reporting, status, and communication workflow planning. |
| `docs/plans/ai-agents/` | `docs/plans/ai-agents/plan.md` | Bounded workflow agents that orchestrate approved tools and portable skills under permission and approval gates. |
| `docs/plans/mcp-and-tooling/` | `docs/plans/mcp-and-tooling/plan.md` | MCP servers, internal tool adapters, registry, schemas, gateway controls, and safe tool discovery planning. |
| `docs/plans/agent-skills/` | `docs/plans/agent-skills/plan.md` | Portable reusable staff/engineer skills with prompt/version/evaluation lifecycle and cross-AI portability. |
| `docs/plans/ai-platform-tools/` | `docs/plans/ai-platform-tools/plan.md` | Shared AI substrate behind tools, skills, and agents. |
| `docs/plans/user-experience-interfaces/` | `docs/plans/user-experience-interfaces/plan.md` | Human-facing screen, workflow, and interaction design across staff, engineer, admin, and front-door surfaces. |
| `docs/plans/finance-billing/` | `docs/plans/finance-billing/plan.md` | Finance, invoice, fee-note, payment-status, payment evidence, and billing automation option planning. |
| `docs/plans/governance-security/` | `docs/plans/governance-security/plan.md` | Cross-programme governance, security, privacy, vendor, licensing, audit, and expert-boundary planning. |
| `docs/plans/operations-quality/` | `docs/plans/operations-quality/plan.md` | Shared QA, release, rollout, monitoring, support, regression, and decommissioning planning. |
| `docs/plans/analytics-data-platform/` | `docs/plans/analytics-data-platform/plan.md` | Data, analytics, historical mining, BI, data quality, and continuous improvement planning. |
| `docs/plans/external-platform-partners/` | `docs/plans/external-platform-partners/plan.md` | External-facing systems, customer/partner portals, partner APIs, insurer integrations, Audatex partnerships, and partner access controls. |
| `docs/plans/product-business/` | `docs/plans/product-business/plan.md` | Business framing, discovery, ROI/KPI tracking, client positioning, objections, and defensibility planning. |

## Section 0 - Taxonomy And Planning Scaffold

Owning workspaces: `initial-repo-setup`, `operational-core`, all newly created planning workspaces.

- Create workspace folders, README files, source maps, roadmaps, tickets folders, option-paper folders, and archives.
- Update `docs/plans/_index.md`, `docs/docs_index.md`, `docs/repo_map.json`, `docs/source_manifest.*`, and scaffold verification.
- Add source-backed ownership matrix so each future item has one primary planning home.

## Section 1 - Foundation And Governance

Owning workspaces: `operational-core`, `governance-security`, `operations-quality`, `product-business`.

- Lock contracts, ADRs, option papers, data map, vendor register, release/rollback baseline, and scope guardrails.
- Keep raw evidence immutable and source-backed.
- Gate cloud OCR, AI processing, live APIs, partner access, payment automation, WhatsApp sends, and external writes before implementation.

## Section 2 - Parser, Provider, And Corpus Core

Owning workspaces: `parser-extraction`, `provider-principal-config`, `operations-quality`, `user-experience-interfaces`.

- Maintain active parser MVP planning in `parser-extraction`; the old operational-core parser path is only a compatibility stub.
- Preserve current CE Document Mapper behavior, all 26 provider presets, deterministic-first parsing, and private real corpus tests.
- Split provider/principal, garage, routing, provider-admin, and provider coverage work into `provider-principal-config`.
- Establish regression harness and release gates before broad automation.

## Section 3 - Operational Core First Slice

Owning workspaces: `case-workflow-state`, `user-experience-interfaces`, `intake-storage-integrations`, coordinated by `operational-core`.

- Build work item state, review queue, audit events, missing-info blockers, staff parser UI, CLI parity, EVA JSON export, and Box-ready package.
- Keep UI and CLI thin over shared parser and service contracts.
- Use reviewed data as the gate before export, packaging, or later live integration.

## Section 4 - Intake And Live Integration Boundaries

Owning workspaces: `intake-storage-integrations`, `mcp-and-tooling`, `automation-centre`, `operations-quality`, `governance-security`.

- Plan Outlook intake, live Box upload, EVA/Sentry adapter, website/WhatsApp metadata capture, and spreadsheet bridge.
- Add dry-run/sandbox tests, idempotency, duplicate prevention, runbooks, and manual approval gates.
- Keep adapter implementation separate from MCP exposure and agent orchestration.

## Section 5 - Evidence, Vehicle, Engineer Pack, Communications

Owning workspaces: `evidence-estimate-review`, `vehicle-valuation-data`, `engineer-communications`, `agent-skills`, `user-experience-interfaces`.

- Promote image quality/order/duplicate review, visible VRM hints, estimate/ABP review, DVLA/DVSA, MOT/mileage, valuation evidence, salvage context, engineer packs, and communication drafting.
- Keep all outputs source-linked and reviewable.
- Preserve engineer judgement and human sign-off for technical conclusions, valuation, roadworthiness, causation, and final reports.

## Section 6 - AI Platform, Tools, And Agents

Owning workspaces: `agent-skills`, `ai-platform-tools`, `mcp-and-tooling`, `ai-agents`, `automation-centre`, `governance-security`.

- Specify portable skills separately from workflow agents so they can be reused by the CE platform, approved agents, ChatGPT, Claude Desktop, or other approved AI front ends.
- Build model/prompt versioning, eval datasets, redaction, correction loops, and AI run logging before expanding AI-assisted behavior.
- Use bounded agents only with approved tools/skills, permissions, audit, and human approval boundaries.

## Section 7 - Finance And External Ecosystem

Owning workspaces: `finance-billing`, `external-platform-partners`, `provider-principal-config`, `governance-security`, `product-business`.

- Record current portal/payment/invoice evidence as metadata first.
- Plan invoice/fee-note generation, fee rules, finance approvals, payment status, and overdue visibility.
- Put portal, partner API, insurer integration, Audatex partnership, payment automation, and partner access into option papers before implementation.

## Section 8 - Analytics And Continuous Improvement

Owning workspaces: `analytics-data-platform`, `operations-quality`, `product-business`, `governance-security`.

- Build analytics only from canonical events, reviewed work items, package metadata, and approved data sources.
- Track operations analytics, provider/principal intelligence, data quality, ROI, queue health, and continuous improvement.
- Defer warehouse, EVA mining, risk indicators, scheduling models, and broad BI until retention, licensing, and data-quality controls are mature.

## Section 9 - Unified Platform And Decommissioning

Owning workspaces: `unified-platform`, `operations-quality`, all specialist workspaces.

- Coordinate mature end-to-end platform convergence across case management, workflow, automation, role model, UI/PWA/mobile, integrations, analytics, and governance.
- Retire spreadsheet or legacy mapper only after parity, audit, rollback, support ownership, and adoption evidence.
- Keep legacy decommissioning as a controlled release milestone, not a side effect of early MVP delivery.

## Cross-Workspace Guardrails

- Every all-ideas row has one primary workspace and may have supporting cross-links.
- Operational Core coordinates first-slice sequencing; it does not permanently own specialist domain work after relocation.
- Governance-gated work starts in option papers, not implementation tickets.
- No autonomous EVA/Sentry submit, payment chasing, WhatsApp sending, partner API, portal automation, cloud OCR, valuation provider, or broad AI/RAG work bypasses approval gates.
- AI outputs assist with reading, drafting, summarising, or review prompts; named humans retain expert judgement and final approvals.
