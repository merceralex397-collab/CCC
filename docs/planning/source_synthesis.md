# Source Synthesis And Promotion Map

Date: 2026-05-23

This document records how generated packs, research notes, test-context packs, and current operational evidence are promoted into canonical CCC planning outputs. Generated packs remain reference material unless this map or a ticket explicitly promotes an idea into the canonical plan.

## Scope Guardrails

- CCC covers vehicle damage instruction intake, parsing, review, packaging, and downstream collision-engineering workflows.
- Personal injury and KADOE are out of scope and must not be added to tickets, contracts, or architecture unless a future written decision explicitly changes scope.
- EVA JSON is an export adapter, not the internal data model.
- Box is the initial storage integration, starting with Box-ready package generation rather than live upload.
- Cloud OCR and document intelligence are future adapters behind governance and feature flags.

## Canonical Outputs

| Output | Purpose |
| --- | --- |
| `docs/architecture/programme_architecture.md` | Programme-level architecture for Operational Core and later convergence. |
| `docs/architecture/mvp_interlock.md` | Shows how parser, provider admin, work item queue, review, and evidence package work together. |
| `docs/architecture/governance_security.md` | Role, audit, privacy, storage, and vendor governance rules. |
| `docs/architecture/future_system_convergence.md` | How later intake, EVA/Sentry, storage, valuation, image, and analytics work plugs in. |
| `docs/contracts/` | Versioned contracts for parser, work item, provider config, audit, package, EVA, storage, and extraction adapters. |
| `docs/decisions/` | ADRs for locked decisions and option papers for unresolved choices. |
| `docs/tickets/` | Executable phased backlog with dependencies, acceptance criteria, and verification gates. |
| `docs/plans/parser_mvp_implementation_plan.md` | First executable MVP implementation plan for the parser and staff UI/CLI surfaces. |

## Generated Pack Disposition

| Source | Promoted Or Merged | Parked Or Superseded | Canonical Destination |
| --- | --- | --- | --- |
| `docs/reference/generated-packs/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/` | Deterministic case association, missing-information state handling, valuation evidence with approval, image/evidence matching, security/governance, acceptance tests. | Autonomous external emailing, autonomous EVA submission, and open-ended continuous learning are parked. | P3/P4 tickets, governance doc, future convergence doc. |
| `docs/reference/generated-packs/ce_system_plans_enhanced/ce_system_plans_enhanced/` | Data model and workflow, Document Mapper/extraction package, Box files, review/matching, EVA/Sentry integration, provider settings migration. | Phase 6 mobile/PWA and decommissioning work are parked until parser parity and Operational Core are live. | Programme architecture, contracts, P1-P3 tickets. |
| `docs/reference/generated-packs/cedocumentmapper_rebuild_plan_pack_all_zips/` | Ground-up compatible parser rebuild, legacy mapper behavioural oracle, parser adapters, EVA export boundary. | Zip files remain parked reference unless implementation evidence is missing from normalized docs. | ADR 0004, parser MVP plan, extraction adapter contract, P1/P2 tickets. |
| `docs/reference/generated-packs/collision_engineers_ai_tools_plans_markdown/` | CE extraction service, field/schema mapper, Box metadata adapter, review queue, provider mapping assistant, PII/audit controls, canonical case store. | ANDIE workbench, broad RAG/training, invoices, and front-door portal are parked until Operational Core is stable. | Contracts, P1/P4/P5 tickets, future convergence doc. |
| `docs/reference/generated-packs/collision_engineers_bulk_data_research_pack/` | MOT/DVLA cache ideas, mileage estimation and anomaly review, vehicle identity normalization, valuation evidence store, duplicate image review, data governance. | Weather, traffic, road-safety enrichment, broad analytics, and warehouse items are parked for P4/P5. | P4/P5 tickets, governance doc, future convergence doc. |
| `docs/reference/generated-packs/originalplans_output/` | Practical new-system MVP framing: holding pen, intake/upload, evidence matching, case detail page, chasers, engineer pack, provider management. | Earlier broad sequencing is superseded by the Operational Core roadmap. | Roadmap, MVP interlock, P0-P5 backlog. |
| `docs/reference/generated-packs/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/` | Work-item state store, provider/principal library, central extraction service, human review queue, EVA adapter/import control, engineer pack, monitoring, DPIA/vendor governance. | Predictive scheduling, external partner APIs, insurer/Audatex partnerships, and data warehouse are parked until core workflow data exists. | Programme architecture, governance doc, P1-P5 backlog. |

## Research Disposition

| Source | Promoted Or Merged | Canonical Destination |
| --- | --- | --- |
| `docs/research/gptdeepresearch.md` | Hybrid document extraction research, native-first/OCR fallback strategy, confidence and validation, avoiding EVA as internal model. | Parser MVP plan, parser result contract, extraction adapter contract, cloud document intelligence option paper. |
| `docs/research/gptevadeepresearch.md` | EVA/Sentry API findings, short-lived bearer token notes, lack of public schema/OpenAPI, future adapter caution, image order requirements. | EVA export contract, future convergence doc, P3 EVA/Sentry tickets, open business questions. |
| `docs/research/siderpdf.md` | PDF cascade: PyMuPDF geometry first, pdfplumber/table fallback, pypdf fallback, OCR only when justified, provenance and confidence requirements. | Parser MVP plan, extraction adapter contract, parser result contract, tooling architecture. |

## Test Context Disposition

| Source | Promoted Or Merged | Parked Or Superseded | Canonical Destination |
| --- | --- | --- | --- |
| `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/` | Outlook intake, Box storage, EVA integration, extraction/AI strategy, canonical data model, workflow states, review, governance. | Wider automation-centre material is parked behind Operational Core. | Architecture, contracts, P1-P4 backlog. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/` | Operational MVP framing, UI/dashboard expectations, schemas, AI module boundaries, compliance/governance, test plan. | Client pitch and speculative ecosystem material are parked. | MVP interlock, parser UI/CLI plan, tickets. |

## Provider Coverage Findings

`docs/data/provider_coverage_matrix.md` remains the current provider coverage source. The parser has 26 presets. The job-sheet evidence contains actual job principal rows that are not directly parser-covered: `ACSP`, `OAK/AX`, `PRINCIPAL`, and `WOODLANDS`.

For planning purposes:

- `ACSP` and `WOODLANDS` are concrete provider/principal gaps that need triage before parser parity can be claimed.
- `OAK/AX` appears to be a composite mapping case and must be modelled as provider-rule composition or manual review rather than silently treated as one provider.
- `PRINCIPAL` is likely a spreadsheet header or data-quality artifact and must be reviewed before it becomes a provider.

## Promotion Rules

Every promoted idea must appear in `docs/tickets/` with:

- phase;
- dependency list;
- source links;
- owner placeholder;
- status placeholder;
- acceptance criteria;
- verification requirement.

Ideas not in a ticket are either merged into architecture/contracts, explicitly parked in this synthesis, or superseded by a later canonical decision.

