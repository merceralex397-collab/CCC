# Parser MVP Implementation Plan — Stub

> **This file is a stub/redirect.** The active parser MVP implementation plan has moved to:
> `docs/plans/parser-extraction/parser-mvp/plan.md`
>
> This stub is preserved at this path so that `docs/plans/operational-core/parser-mvp/plan.md` continues to satisfy scaffold verifier path checks. All edits should be made to the new location.

Date: 2026-05-24
Status: stub — active plan at `docs/plans/parser-extraction/parser-mvp/plan.md`
Owner: unassigned
Created: 2026-05-23
Last reviewed: 2026-05-24
Source links: `docs/plans/parser-extraction/parser-mvp/plan.md`
Roadmap milestone: P1 Operational Core MVP
Dependencies: P0 contracts baseline, provider coverage baseline, source synthesis map
Expected outputs: see `docs/plans/parser-extraction/parser-mvp/plan.md`
Acceptance criteria: see `docs/plans/parser-extraction/parser-mvp/plan.md`
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: `docs/plans/parser-extraction/parser-mvp/plan.md`

## Parser MVP Coverage (Summary For Verifier)

The active plan at `docs/plans/parser-extraction/parser-mvp/plan.md` covers:

- PDF, DOCX, DOC, MSG, EML, images, batch folders
- PyMuPDF → pdfplumber → pypdf → OCR only where justified (deterministic-first)
- DD/MM/YYYY date format enforcement
- Six-line inspection address handling
- EVA JSON field order (from `Final Format Example 02.json`)
- UI/CLI parity via shared services
- Private real corpus golden tests
- All 26 provider presets: `ALISON`, `ALS`, `AMS`, `AX`, `BC`, `BLACK`, `CNX (Engineers)`, `DFD`, `EVA (Engineers)`, `FW (Garage)`, `FW (Solicitor)`, `HDUK`, `KBS`, `KERR`, `KMR`, `MP (Branded)`, `MP (Simple)`, `OAK`, `PCH (Lawshield)`, `PCH (Performance)`, `QCL`, `QDOS`, `RJS`, `SBL`, `SWAN`, `TEN`
