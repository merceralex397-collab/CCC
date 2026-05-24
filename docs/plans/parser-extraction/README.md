# Parser Extraction Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`, `docs/decisions/0004-ground-up-compatible-parser-rebuild.md`, `docs/decisions/0007-deterministic-first-parser.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`, `docs/contracts/extraction_adapter_contract_v1.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: provider-principal-config, operations-quality, governance-security, user-experience-interfaces
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/parser-extraction/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Parser, document extraction, CE Document Mapper evolution, and extraction-regression planning.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- PDF, DOCX, DOC, MSG, EML, image, ZIP, and batch extraction
- deterministic-first parser core and provider-rule execution behavior
- OCR/cloud document-intelligence option papers
- parser CLI parity and extraction regression corpus

## Does Not Own

- provider business routing metadata after extraction
- case-state transitions after parse
- human-facing UI design beyond parser-specific requirements

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/plans/parser-extraction/parser-mvp/plan.md` | Active parser MVP implementation plan. |
| `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md` | Adjacent parser comparison, inspection-location decision register, and EVA/Sentry lookup constraint. |
| `docs/decisions/0004-ground-up-compatible-parser-rebuild.md` | Accepted ground-up compatible parser rebuild decision. |
| `docs/decisions/0007-deterministic-first-parser.md` | Accepted deterministic-first parser decision. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md` | Document Mapper and extraction work package. |
| `docs/contracts/extraction_adapter_contract_v1.md` | Versioned extraction adapter contract. |

## Cross-Workspace Dependencies

- provider-principal-config
- operations-quality
- governance-security
- user-experience-interfaces

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
