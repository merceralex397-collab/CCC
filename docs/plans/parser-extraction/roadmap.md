# Parser Extraction Roadmap

Date: 2026-05-24
Status: active workspace roadmap
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`, `docs/decisions/0004-ground-up-compatible-parser-rebuild.md`, `docs/decisions/0007-deterministic-first-parser.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`, `docs/contracts/extraction_adapter_contract_v1.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: provider-principal-config, operations-quality, governance-security, user-experience-interfaces
Expected outputs: phased promotion sequence for `docs/plans/parser-extraction/`
Acceptance criteria: roadmap stages cite source-backed workspace scope and do not duplicate another workspace's primary ownership
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## S1

- Maintain active parser MVP planning here, then deliver deterministic parser core and shared UI/CLI service behavior.

## S2

- Harden extraction adapters, provider corpus coverage, export blockers, and UI/CLI parity.

## S3-S4

- Evaluate OCR/cloud fallback and AI extraction only behind governance and measurable regression evidence.

## Promotion Gate

Any item promoted from this roadmap must cite `source_map.md`, name dependencies, define acceptance criteria, and state whether governance/security or operations-quality approval is required.
