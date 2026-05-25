# Parser Extraction Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`, `docs/decisions/0004-ground-up-compatible-parser-rebuild.md`, `docs/decisions/0007-deterministic-first-parser.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`, `docs/contracts/extraction_adapter_contract_v1.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: provider-principal-config, operations-quality, governance-security, user-experience-interfaces
Expected outputs: source-to-plan traceability for `docs/plans/parser-extraction/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/plans/parser-extraction/parser-mvp/plan.md` | Active parser MVP implementation plan. |
| `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md` | Adjacent parser comparison, inspection-location decision register, and EVA/Sentry lookup constraint. |
| `docs/plans/parser-extraction/parser-mvp/legacy_behavior_inventory.md` | Implemented inventory of legacy extraction cascade, provider detection, rule methods, normalization, and EVA export compatibility. |
| `docs/plans/parser-extraction/parser-mvp/adjacent_repo_comparison.md` | Adopted/rejected pattern record for adjacent parser repositories. |
| `docs/reference/data/parser_provider_presets_v1.json` | Versioned fixture copy of the current 26 provider presets. |
| `docs/reference/data/parser_corpus_fixture_ledger.json` | Fixture ledger for every raw instruction corpus file with expected provider status, fields, blockers, and export snapshot status. |
| `docs/reference/data/parser_corpus_regression_report.json` | Latest executable parser corpus regression summary. |
| `docs/decisions/0004-ground-up-compatible-parser-rebuild.md` | Accepted ground-up compatible parser rebuild decision. |
| `docs/decisions/0007-deterministic-first-parser.md` | Accepted deterministic-first parser decision. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md` | Document Mapper and extraction work package. |
| `docs/contracts/extraction_adapter_contract_v1.md` | Versioned extraction adapter contract. |

## Ownership Boundary

Primary ownership:

- PDF, DOCX, DOC, MSG, EML, image, ZIP, and batch extraction
- deterministic-first parser core and provider-rule execution behavior
- OCR/cloud document-intelligence option papers
- parser CLI parity and extraction regression corpus

Explicit exclusions:

- provider business routing metadata after extraction
- case-state transitions after parse
- human-facing UI design beyond parser-specific requirements

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
