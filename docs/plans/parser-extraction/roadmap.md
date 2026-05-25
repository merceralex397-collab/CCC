# Parser Extraction Roadmap

Date: 2026-05-24
Status: active workspace roadmap
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-25
Source links: `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`, `docs/plans/parser-extraction/parser-mvp/sentry-api-enhancement-mechanisms.md`, `docs/decisions/0004-ground-up-compatible-parser-rebuild.md`, `docs/decisions/0007-deterministic-first-parser.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`, `docs/contracts/extraction_adapter_contract_v1.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: provider-principal-config, operations-quality, governance-security, user-experience-interfaces
Expected outputs: phased promotion sequence for `docs/plans/parser-extraction/`
Acceptance criteria: roadmap stages cite source-backed workspace scope and do not duplicate another workspace's primary ownership
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## S1

- Parser MVP executable baseline implemented on branch `codex/parser-mvp-full`: deterministic parser core, shared CLI/UI service behavior, provider fixtures, EVA export adapter, evidence package manifest, corpus regression report, optional local OCR for short image-only instruction PDFs, and engineer-report folder merge handling.

## S2

- Harden provider field coverage, review-required cases, OCR/manual review workflow for image-only evidence packs, release packaging, and UI ergonomics using `docs/reference/data/parser_corpus_regression_report.json` as the regression baseline.

## S3-S4

- Evaluate OCR/cloud fallback and AI extraction only behind governance and measurable regression evidence.

## Promotion Gate

Any item promoted from this roadmap must cite `source_map.md`, name dependencies, define acceptance criteria, and state whether governance/security or operations-quality approval is required.
