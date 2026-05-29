# Parser Workspace — Open Questions

Date: 2026-05-29
Status: active open-questions log
Owner: unassigned
Group: parser (G1, spine)
Source links: `docs/superpowers/specs/2026-05-29-parser-iteration-design.md`, `docs/plans/parser-extraction/plan.md`, `docs/plans/parser-extraction/context.md`

Tracked unknowns for the parser iteration. Resolve into the plan, a ticket, or an option paper as they close.

## Resolved (this interview, 2026-05-29)

- **Are the 4 uncovered principals real providers?** — Yes. `ACSP`, `OAK/AX`, `PRINCIPAL`, `WOODLANDS` are all confirmed real (user, 2026-05-29). Goal is full coverage parity, not exclusion.
- **UI direction?** — Keep/modernise the Tk staff UI this iteration; no web rebuild.
- **Cloud/AI extraction?** — No. Deterministic-first and local-only; add ocrmypdf as the stronger local OCR methodology.

## Open

1. **Ghostscript packaging.** ocrmypdf requires Ghostscript (Tesseract is already bundled via `cedocumentmapper/tesseract`). How is Ghostscript installed/bundled for staff Windows machines and for CI? (operations-quality)
2. **Scan recoverability.** Do `ACSP` and `WOODLANDS` scans become reliably parseable after `--deskew --clean` OCR, or do they stay review-required even after OCR? Measure on the real corpus before claiming parity.
3. **Verifier preset pin.** `verify_scaffold.py` pins the raw `providers.json` at exactly 26 named presets. When the versioned fixture (`parser_provider_presets_v1.json`) becomes the authoritative source at 30 presets, how do we update the verifier's check without weakening the parity guarantee?
4. **OCR runtime cost.** What is the per-document and per-batch OCR cost, and is `--skip-text` + bounded parallelism enough on large batch folders?
5. **UI confidence affordance.** Exact Tk presentation for per-field confidence, source-evidence link, and the OCR-used marker (kept lightweight; detail during build).
6. **OCR_PAGE_LIMIT branch.** Once ocrmypdf is in, is the legacy narrow `should_ocr` branch retired entirely or kept only as a no-Ghostscript fallback?
