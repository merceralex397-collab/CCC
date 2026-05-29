# Parser Iteration: Local OCR, Provider Coverage, and Extraction Hardening — Design

Date: 2026-05-29
Status: approved design (brainstorming output)
Owner: unassigned
Workspace: `docs/plans/parser-extraction/` (group: parser, G1, spine)
Source links: `docs/plans/parser-extraction/context.md`, `docs/plans/parser-extraction/parser-mvp/plan.md`, `src/ccc_parser/readers.py`, `src/ccc_parser/models.py`, `src/ccc_parser/validation.py`, `src/ccc_parser/cli.py`, `src/ccc_parser/ui/app.py`, `docs/reference/data/provider_coverage_matrix.md`, `tools/run_parser_corpus.py`, `tools/verify_scaffold.py`

## Context

The parser is not greenfield: `src/ccc_parser/` is a modular, contract-first rebuild at "implemented baseline, active hardening" (see `context.md`). This spec defines the **next iteration**: make the parser a production-usable, deterministic, **local-only** staff tool with stronger extraction and full provider parity, keeping the Tk staff UI. No cloud or AI extraction.

### Decisions captured (user, 2026-05-29)

- Primary goal: **provider-coverage parity + new extraction capability**.
- UI: **keep/modernise the Tk staff UI** (no web rebuild this iteration).
- Extraction: **deterministic-first**; add **ocrmypdf** as a stronger *local* OCR methodology; cloud/AI OCR stays off.
- Coverage: **add presets and rescue low-quality scans via OCR**; all four uncovered principals (`ACSP`, `OAK/AX`, `PRINCIPAL`, `WOODLANDS`) are **confirmed real providers**.
- Capability scope: ocrmypdf OCR robustness **+** table/layout hardening **+** confidence/provenance in the UI **+** batch/throughput.

## Goals / Non-goals

**Goals:** recover currently-blocked/low-quality scanned PDFs; reach parity for the four real principals; improve table/layout extraction; surface confidence/provenance/OCR-used in the Tk review screen; improve batch reliability and throughput. Preserve all existing parity guarantees (26 presets, EVA field order, six-line address, DD/MM/YYYY, mileage/VAT gates, image ordering) and the private-real-corpus regression.

**Non-goals (this iteration):** cloud document intelligence / AI extraction; web UI; live Outlook/Box/EVA integration (that is the `bridge`); valuation automation. Personal injury and KADOE remain out of scope.

## Design

### 1. Local OCR robustness via ocrmypdf (core)

Today's cascade in `readers.py:read_document` is PyMuPDF blocks (`_extract_pdf_pymupdf`) → pdfplumber (`_extract_pdf_pdfplumber`) → pypdf (`_extract_pdf_pypdf`). The only OCR path is the narrow `should_ocr` branch (`readers.py:210`): empty text **and** ≤ `OCR_PAGE_LIMIT` (2) pages **and** exactly one image per page. Multi-page or messy scans fall through to the `image_only_pdf_requires_review` warning and `pdf_image_metadata` (`readers.py:838`).

Add an **ocrmypdf stage** invoked when native extraction yields no/low text (or scan signature detected):

- Run `ocrmypdf` on the source PDF into a per-parse temp workspace (reuse the existing per-parse attachment-workspace pattern), with `--skip-text` (leave text pages untouched), `--deskew`, `--clean`, `--rotate-pages`, `--quiet`, bounded by `SUBPROCESS_TIMEOUT_SECONDS`.
- **Re-run the existing PyMuPDF→pdfplumber cascade on the OCR'd PDF**, so we get layout-aware text and tables rather than flat per-page `image_to_string`. Tag `reader_method="ocrmypdf_layer"`; keep emitting the `ocr_fallback_used` warning so reviewers see OCR was used.
- **Optional-runtime** like `tkinterdnd2`/`pytesseract` today (guarded import, graceful fallback to the current behaviour if unavailable). Wraps the already-bundled Tesseract; **requires Ghostscript** — packaging/availability of Ghostscript is a runtime-dependency item (see Risks).
- The narrow `OCR_PAGE_LIMIT==2` branch is superseded by this stage (kept only as a no-Ghostscript fallback).

### 2. Provider coverage parity (4 real principals)

- Triage `ACSP`, `OAK/AX`, `PRINCIPAL`, `WOODLANDS` against the live job sheet and `provider_coverage_matrix`; author detection + mapping presets for each.
- Retry the low-quality cases (notably `ACSP`, previously "lost cause" purely from poor OCR) through the new ocrmypdf stage and add corpus fixtures for any that become parseable.
- **Constraint:** the new presets extend the **versioned fixture** `docs/reference/data/parser_provider_presets_v1.json`, **not** the immutable raw `Settings Backup/providers.json`. `verify_scaffold.py` currently pins the raw file at exactly 26 named presets and loads `ParserCore` from it; making the versioned fixture the authoritative preset source (30 presets) requires updating the verifier's provider check accordingly. This is the one verifier change this iteration needs.
- Regenerate `docs/reference/data/provider_coverage_matrix.{md,csv}`; provider config/admin lifecycle is coordinated with the `providers` sub-area.

### 3. Table/layout extraction hardening

Improve table/geometry handling for layout-heavy instructions and estimate-style tables: tune the PyMuPDF block sort + the pdfplumber `extract_tables` path in `readers.py`, and add corpus fixtures for the table-heavy providers. No new dependency.

### 4. Confidence / provenance in the Tk UI

The canonical result (`models.py`) already carries provenance and confidence. Surface in `ui/app.py`'s review screen: per-field confidence, the source-evidence reference, and an explicit "OCR used / fallback" marker so staff can prioritise review of OCR'd cases. No change to the canonical model.

### 5. Batch / throughput

Bounded parallelism for batch folders, resumable runs (extend the existing source-hash reuse so already-parsed items are skipped), and clearer per-item failure reporting surfaced in both `cli.py` batch output and the UI. Preserve the "partial batch failure does not discard successes" behaviour.

## Sequencing

1. ocrmypdf stage in the cascade (optional-runtime, gated).
2. Re-run `python tools/run_parser_corpus.py` to measure which uncovered/blocked cases the OCR stage rescues.
3. Author provider presets for the now-readable principals in the versioned fixture; update the verifier's preset check; regenerate the coverage matrix.
4. Table/layout tuning + fixtures.
5. UI confidence/provenance/OCR-used surfacing.
6. Batch/throughput improvements.

## Testing

- Extend the private golden corpus + fixture ledger with the rescued OCR cases and the four new presets; keep `run_parser_corpus.py` green across all presets.
- New adapter tests: multi-page scanned PDF rescued by ocrmypdf; text-PDF unchanged by `--skip-text`; ocrmypdf-unavailable graceful fallback.
- UI/CLI parity, EVA field-order, and image-ordering tests unchanged and still green.
- `python tools/verify_scaffold.py` green (with the updated preset check).

## Risks & Open Questions

- **Ghostscript packaging** for ocrmypdf (Tesseract is already bundled; Ghostscript is not) — confirm install/bundle story for staff machines and CI.
- Whether `ACSP`/`WOODLANDS` scans are genuinely recoverable after OCR, or remain review-required even with deskew/clean.
- OCR runtime cost on large batches (mitigated by `--skip-text` and parallelism, but measure).
- Exact UI affordance for confidence/OCR markers (kept lightweight; detail during build).
- Moving the verifier's 26-preset pin to the versioned fixture without weakening the parity guarantee.

## Acceptance Criteria

- Multi-page scanned instruction PDFs that previously hit `image_only_pdf_requires_review` are extracted via the ocrmypdf stage when Ghostscript+Tesseract are available, with graceful fallback when not.
- Presets exist for all four principals in the versioned fixture; the coverage matrix shows their status; the corpus regression covers them.
- The Tk review screen shows per-field confidence, source evidence, and an OCR-used marker.
- Batch runs are resumable and report per-item failures without discarding successes.
- `verify_scaffold.py`, the corpus regression, UI/CLI parity, and EVA field-order checks all pass; deterministic-first and PI/KADOE-out-of-scope guardrails preserved.
