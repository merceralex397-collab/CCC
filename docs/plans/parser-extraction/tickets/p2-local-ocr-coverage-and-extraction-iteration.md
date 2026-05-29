# Ticket: Parser Local-OCR, Coverage Parity, and Extraction Hardening Iteration

Status: planned
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Source links: `docs/superpowers/specs/2026-05-29-parser-iteration-design.md`, `docs/plans/parser-extraction/plan.md`, `docs/plans/parser-extraction/context.md`, `src/ccc_parser/readers.py`, `src/ccc_parser/ui/app.py`, `src/ccc_parser/cli.py`, `docs/reference/data/provider_coverage_matrix.md`, `tools/run_parser_corpus.py`, `tools/verify_scaffold.py`
Roadmap milestone: G1 parser (spine)
Dependencies: provider-principal-config (`providers` sub-area), operations-quality (Ghostscript packaging, corpus gating), governance-security (confirm no new vendor/privacy surface)
Expected outputs: ocrmypdf local-OCR stage, 4 new provider presets in the versioned fixture, table/layout hardening, Tk confidence/provenance surfacing, batch/throughput improvements, updated corpus + coverage matrix
Acceptance criteria: see deliverables below; all verification gates green
Verification required: `python tools/verify_scaffold.py`, `python tools/run_parser_corpus.py`, `python -m pytest` (UI/CLI parity + EVA field-order + adapter tests)
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Scope

Deterministic-first, local-only parser iteration. No cloud/AI extraction; no web UI; no live integration. Personal injury and KADOE remain out of scope.

## Deliverables

1. **ocrmypdf local-OCR stage** in `src/ccc_parser/readers.py`: invoked when native extraction yields no/low text; `--skip-text --deskew --clean --rotate-pages`, bounded timeout, per-parse temp workspace; re-runs the PyMuPDF→pdfplumber cascade on the OCR'd PDF; `reader_method="ocrmypdf_layer"` + `ocr_fallback_used` warning; optional-runtime with graceful fallback when ocrmypdf/Ghostscript absent.
   - Acceptance: a multi-page scanned instruction PDF that previously hit `image_only_pdf_requires_review` extracts text when the OCR toolchain is present; text PDFs are unchanged (`--skip-text`); absence of ocrmypdf/Ghostscript falls back cleanly.
2. **Provider presets** for `ACSP`, `OAK/AX`, `PRINCIPAL`, `WOODLANDS` in the **versioned fixture** `docs/reference/data/parser_provider_presets_v1.json` (not the raw `providers.json`); update `verify_scaffold.py` to validate against the versioned fixture; regenerate `provider_coverage_matrix.{md,csv}`.
   - Acceptance: presets present; coverage matrix reflects new status; corpus covers the four; verifier green.
3. **Table/layout hardening** in `readers.py` (PyMuPDF blocks + pdfplumber tables) with fixtures for table-heavy providers.
4. **Tk UI confidence/provenance** in `src/ccc_parser/ui/app.py`: per-field confidence, source-evidence reference, and an OCR-used marker on the review screen.
5. **Batch/throughput** in `cli.py`/`core.py`: bounded parallelism, resumable runs (source-hash skip), per-item failure reporting without discarding successes.

## Verification Gates

- `python tools/verify_scaffold.py` passes (with updated preset check).
- `python tools/run_parser_corpus.py` green across all presets, including the four new principals and the OCR-rescued fixtures.
- UI/CLI parity, EVA JSON field-order, and image-ordering tests pass.
- ocrmypdf path is optional-runtime: suite passes with and without the OCR toolchain present.

## Open Questions

See `docs/plans/parser-extraction/open-questions.md` (Ghostscript packaging, scan recoverability, verifier preset pin, OCR cost, UI affordance).
