# P2 Parser Hardening Tickets

## P2-003 Extraction Adapter Hardening

- Status: implemented baseline; further hardening remains open for broader OCR policy and release packaging.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-25.
- Source links: `docs/contracts/extraction_adapter_contract_v1.md`, `docs/research/siderpdf.md`, `docs/research/gptdeepresearch.md`.
- Roadmap milestone: P2 Parser Hardening And Provider Parity.
- Dependencies: P1-001, P2-001 (Golden Corpus Regression Harness).
- Expected outputs: hardened PDF cascade, table extraction fallback, legacy DOC conversion path, MSG/EML attachment handling, image/OCR fallback rules. Current implementation includes PyMuPDF/pdfplumber/pypdf cascade, DOCX OOXML, DOC Word/LibreOffice/antiword/OLE/RTF fallbacks, MSG/EML parsing and attachment routing, deterministic field fallbacks for visible labelled values, invalid fixed-position noise suppression, optional local Tesseract OCR for short image-only instruction PDFs, isolated per-parse attachment workspaces, and image-only evidence PDF review warnings.
- Acceptance criteria: extraction failures produce structured warnings; OCR is not run by default on native PDFs; provenance is retained.
- Verification required: adapter-level tests and corpus cases for native, table-heavy, scanned, DOC, DOCX, MSG, EML, image pack, and batch folder inputs. Current command: `python tools/run_parser_corpus.py`.
- Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p2-parser-hardening-provider-parity.md` § P2-003.
- Superseded-by: none.

## P2-004 UI/CLI Parity Hardening

- Status: implemented baseline; drag/drop restored in Tk UI when `tkinterdnd2` is installed.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-25.
- Source links: `docs/architecture/parser_ui_cli.md`, `docs/plans/parser-extraction/parser-mvp/plan.md`.
- Roadmap milestone: P2 Parser Hardening And Provider Parity.
- Dependencies: P1-002 (Staff Parser UI), P1-003 (Parser CLI Parity).
- Expected outputs: shared service API, parity checklist, accessibility/usability fixes, batch progress/error reporting. Current implementation includes folder-level instruction plus engineer-report merge handling, explicit engineer-report override warnings, and batch reports that preserve successful parses while returning structured per-file failures.
- Acceptance criteria: every parser/export/package action exposed in UI has CLI equivalent and uses same core validation.
- Verification required: parity tests and staff workflow walkthrough.
- Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p2-parser-hardening-provider-parity.md` § P2-004.
- Superseded-by: none.
