# Parser MVP Plan Enhancement And Adjacent Evidence

Date: 2026-05-24
Status: implemented baseline
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`, `docs/reference/adjacent_repositories.md`, `docs/reference/raw/collisionrelateddocs/Instructions/`, `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json`, `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json`, `docs/reference/raw/collisionrelateddocs/collision_releated/Sentry_API_Complete_Guide.md`, `docs/reference/raw/collisionrelateddocs/collision_releated/Backup of CE Job Sheet 260309.xlsm`, `docs/operations/job_sheet_spreadsheet_companion.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`
Roadmap milestone: Section 2 - Parser, Provider, And Corpus Core
Dependencies: provider-principal-config, operations-quality, governance-security, intake-storage-integrations, user-experience-interfaces
Expected outputs: implementation-ready parser MVP plan, adjacent-repository decision register, inspection-location policy, atomic provider/corpus tasks, EVA/Sentry constraints
Acceptance criteria: following the parser MVP plan 100% would produce a parser at parity with, or deliberately superior to, the current `cedocumentmapper` behavior; every divergence is justified with source evidence; unknowns are explicit review blockers
Verification required: `python tools/verify_scaffold.py`, parser corpus regression plan review, provider coverage matrix review
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Todo Checklist

- [x] Inventory `../cedocumentmapper/app.py` extraction, provider detection, rule execution, field normalization, six-line inspection-address export, and export gating behavior.
- [x] Inventory `../collisionpdf` for parser-service patterns worth adopting: native extraction IR, OCR fallback boundary, schema validation, warning taxonomy, and synthetic-test limitations.
- [x] Inventory `../cedocumentmapper_v2.0` for module-boundary and regression-harness patterns worth adopting.
- [x] Build a fixture ledger for every file under `docs/reference/raw/collisionrelateddocs/Instructions/`, linking raw source, normalized companion, detected provider, expected canonical fields, expected EVA JSON fields, and review-required gaps.
- [x] Convert the 26 provider presets from `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json` into versioned config fixtures with tests before changing behavior.
- [x] Add explicit inspection-location policy: preserve legacy six-line `Inspection Address` export while adding canonical internal mode/source/address fields.
- [x] Document why the new parser diverges from `cedocumentmapper` where it does: source-linked provenance, schema validation, separate inspection mode, provider/principal/garage lookup separation, and UI/CLI shared core.
- [x] Add EVA/Sentry constraints from `Sentry_API_Complete_Guide.md`: no direct live submission in MVP, no dependency on undocumented location lookup, future `LocationUpdate` write path only after governance review.
- [x] Use the job sheet workbook, companion, and FigJam workflow as provider/principal/garage operational evidence; do not encode spreadsheet-only routing as parser extraction logic without a provider-config owner decision.
- [x] Add acceptance tests for final EVA JSON field order against `Final Format Example 02.json`.

Implemented evidence: `docs/plans/parser-extraction/parser-mvp/legacy_behavior_inventory.md`, `docs/plans/parser-extraction/parser-mvp/adjacent_repo_comparison.md`, `docs/reference/data/parser_provider_presets_v1.json`, `docs/reference/data/parser_corpus_fixture_ledger.*`, and parser tests under `tests/`.
