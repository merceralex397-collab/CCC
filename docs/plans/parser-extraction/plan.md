# Parser Extraction Plan

Date: 2026-05-29
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-29
Group: parser
Wave: G1 (spine)
Layer: ingest-parse
Source links: `docs/plans/parser-extraction/context.md`, `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`, `docs/superpowers/specs/2026-05-29-parser-iteration-design.md`, `docs/decisions/0004-ground-up-compatible-parser-rebuild.md`, `docs/decisions/0007-deterministic-first-parser.md`, `docs/contracts/extraction_adapter_contract_v1.md`, `docs/reference/data/provider_coverage_matrix.md`
Roadmap milestone: G1 parser (spine)
Dependencies: provider-principal-config (sub-area `providers`), operations-quality, governance-security, user-experience-interfaces
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/parser-extraction/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`, parser corpus regression, UI/CLI parity, EVA field-order tests
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/parser-extraction/` is the **parser** broad workspace (group `parser`, wave G1, the start of the development spine). It owns deterministic-first extraction and the canonical parser result; the `providers` sub-area (← provider-principal-config) owns provider/principal/garage config and the provider-admin workflow. See `docs/plans/_groups.md` for the grouped roadmap.

## Current Baseline

`src/ccc_parser/` is an implemented, modular rebuild (core, triage, readers, providers, rules, normalization, models, validation, review, packaging, exporters/eva, cli, ui/app) at "implemented baseline, active hardening". The MVP implementation plan is `parser-mvp/plan.md`; the firsthand current-state summary is `context.md`. This already realises the architectural improvement over the legacy `cedocumentmapper` monolith (shared core + thin UI/CLI, canonical provenance/confidence, structured inspection-site model, contract-first validation).

## This Iteration — Local OCR, Coverage Parity, Extraction Hardening

Approved design: `docs/superpowers/specs/2026-05-29-parser-iteration-design.md`. Implementation ticket: `tickets/p2-local-ocr-coverage-and-extraction-iteration.md`.

Deterministic-first and **local-only** (no cloud/AI). Five workstreams:

| # | Workstream | Primary touch points | Acceptance check |
| --- | --- | --- | --- |
| 1 | Local OCR via **ocrmypdf** (deskew/clean + text layer, then re-run the layout cascade) | `src/ccc_parser/readers.py` (PDF cascade, `should_ocr`, `OCR_PAGE_LIMIT`) | Multi-page scans previously blocked now extract; optional-runtime fallback when Ghostscript/Tesseract absent |
| 2 | Provider coverage parity for `ACSP`, `OAK/AX`, `PRINCIPAL`, `WOODLANDS` (all confirmed real) | `docs/reference/data/parser_provider_presets_v1.json`, `provider_coverage_matrix.{md,csv}`, `tools/verify_scaffold.py` preset pin | Presets in the versioned fixture; coverage matrix updated; corpus covers them |
| 3 | Table/layout extraction hardening | `src/ccc_parser/readers.py` (PyMuPDF blocks, pdfplumber tables) | Fixtures for table-heavy providers pass |
| 4 | Confidence/provenance/OCR-used surfacing in the Tk UI | `src/ccc_parser/ui/app.py` (review screen); `models.py` (already carries the data) | Review screen shows per-field confidence, source evidence, OCR-used marker |
| 5 | Batch/throughput (bounded parallelism, resumable, per-item failure reporting) | `src/ccc_parser/cli.py`, `core.py` | Batch resumable; per-item failures reported without discarding successes |

Sequence: ocrmypdf stage → corpus re-run to measure rescued cases → presets for now-readable principals (+ verifier preset-pin update) → table/layout tuning → UI surfacing → batch/throughput.

## Sub-Areas

- `extraction` (this workspace's core; ← parser-extraction): triage, adapters, rules, canonical result, validation, EVA export, packaging inputs, UI/CLI.
- `providers` (← provider-principal-config): provider/principal/garage/routing config, provider-admin workflow, coverage lifecycle. Coordinate preset authoring (workstream 2) here.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `providers` sub-area (provider-principal-config) | Preset authoring, coverage lifecycle, and provider-admin must stay coherent with extraction mechanics. |
| `operations-quality` | Corpus regression, release/rollback, and the Ghostscript runtime-dependency packaging decision. |
| `governance-security` | Confirms no new vendor/privacy surface (OCR stays local; no cloud) and that PI/KADOE remain out of scope. |
| `user-experience-interfaces` | Tk UI confidence/provenance surfacing should align with the eventual platform review surface. |
| `bridge` (intake-storage-integrations) | Consumes EVA JSON + evidence-package inputs; parser owns up to those contracts, not live integration. |

## Non-Overlap Rules

This workspace does not own: case-state transitions after parse; business UI design beyond parser needs; live Outlook/Box/EVA adapters; valuation automation. Cloud OCR/document intelligence remains out of scope for this iteration.

## Source Ownership Rules

- Cite the source paths above in every promoted ticket, option paper, or roadmap change.
- New provider presets extend the versioned fixture `parser_provider_presets_v1.json`; do not edit the immutable raw `Settings Backup/providers.json`.
- Keep generated and historical planning packs reference-only until a scoped ticket promotes them.

## Promotion Gates

- `tickets/` holds implementation-ready work with acceptance criteria and verification (see the iteration ticket).
- `option-papers/` is required before any cloud OCR / document-intelligence, vendor, or external-write decision.
- Link operations-quality for the Ghostscript packaging decision and corpus-regression gating; link governance-security only if a non-local extraction path is ever proposed.
