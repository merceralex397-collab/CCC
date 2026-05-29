# Parser Workspace — Context (Information Document)

Date: 2026-05-29
Status: active context document
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Source links: `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`, `docs/plans/parser-extraction/parser-mvp/legacy_behavior_inventory.md`, `docs/decisions/0004-ground-up-compatible-parser-rebuild.md`, `docs/decisions/0007-deterministic-first-parser.md`, `docs/contracts/parser_result_v1.md`, `docs/contracts/extraction_adapter_contract_v1.md`, `docs/contracts/eva_export_contract_v1.md`, `docs/reference/adjacent_repositories.md`, `../cedocumentmapper/app.py`
Group: parser (G1, spine, layer: ingest-parse) — see `docs/plans/_groups.md`
Roadmap milestone: P1 Operational Core MVP / G1 parser
Purpose of this document: consolidate what is already known about the parser so the brainstorming interview can focus on the *next improvement iteration*, not re-discovery.

## What this workspace owns

Deterministic-first instruction parsing and extraction: file triage/classification; PDF/DOCX/DOC/MSG/EML/image/ZIP/batch adapters; provider detection and the mapping-rule engine for all 26 presets; the canonical parser result (provenance/confidence/warnings); UI/CLI parity over a shared core; EVA JSON export gate + field order; image-package ordering; and the private-corpus regression. Sub-area `providers` (← `provider-principal-config`) owns provider/principal/garage/routing config and the provider-admin workflow.

It does **not** own: case-state transitions after parse, business UI design beyond parser needs, or live Outlook/Box/EVA adapters (those are the `bridge`).

## Current state — this is a hardening baseline, not greenfield

An executable, modular rebuild already exists in `src/ccc_parser/`:

| Module | Responsibility |
| --- | --- |
| `core.py` | Orchestrates triage → adapters → detection → rules → result; loads providers. |
| `triage.py` | File-type/role classification, batch manifest, MSG/EML attachment routing. |
| `readers.py` | Extraction adapters → layout-aware IR (PyMuPDF → pdfplumber → pypdf cascade; DOCX/DOC/MSG/EML/image; optional local Tesseract OCR). |
| `providers.py` | Loads the 26 presets; provider detection (all-phrases match + scoring). |
| `rules.py` | Mapping-rule engine (single/two label, fixed position, offsets, email date, transforms, engineer-report, blank rules) + deterministic fallback extraction. |
| `normalization.py` | Date → DD/MM/YYYY, VRM, mileage, six-line inspection address, control-char cleanup. |
| `models.py` | Canonical parser result + inspection-site fields (`inspection_mode`, `inspection_site_source`, structured address, confidence, evidence). |
| `validation.py` | Export gates (critical blockers) and warnings. |
| `review.py` | Reviewer overrides with audit identity. |
| `exporters/eva.py` | Canonical result → EVA JSON in `Final Format Example 02.json` field order. |
| `packaging.py` | Evidence-package manifest inputs + image preview ordering. |
| `cli.py` | `triage / parse / validate / export-eva / package / batch / providers` commands. |
| `ui/app.py` | Staff Tk UI (import, field review/correction, validation, EVA export, package), drag/drop via optional `tkinterdnd2`. |

Verification baseline (per the MVP plan): `pytest` and `python tools/run_parser_corpus.py` pass with **zero reader-level blockers across all 134 instruction files**; remaining blockers are review-required data gaps or non-instruction sources that intentionally must not export to EVA. (Note: `pytest` and parser runtime deps are not installed in the current shell interpreter `C:\Python314`; `verify_scaffold.py`, which imports `ParserCore` and asserts 26 presets, does pass.)

## How it already improves on the legacy `cedocumentmapper`

Legacy (`../cedocumentmapper/app.py`) is a ~1000+ line Tkinter monolith mixing UI, extraction, provider config, OCR, MSG handling, and export. The rebuild's deliberate improvements (per the MVP plan's divergence table):

- **Separation**: shared parser core with thin UI *and* CLI over the same services (legacy had no CLI).
- **Canonical result** with provenance/confidence/warnings (legacy exposed only EVA JSON).
- **Structured inspection-site model** (`mode`/`source`/structured address) collapsed to the legacy six-line string *only* at the EVA export adapter — so image-based vs physical vs garage-lookup vs unknown are no longer conflated.
- **Contract-first**: schema validation before any EVA-specific output; versioned provider fixtures instead of a baked `providers.json`.
- **Deterministic fallback** that extracts visible labelled values where a provider preset has blank rules (legacy left them blank).
- **Safety**: image/image-pack sources hard-blocked from EVA export; per-parse attachment workspaces; bounded DOC-converter timeouts; explicit failure on ambiguous duplicate provider codes (e.g. `FW`).

Compatibility held where it matters: 26 presets, EVA field order, six-line address, DD/MM/YYYY, mileage/VAT gates, image ordering.

## Known open gaps / hardening backlog (candidate interview inputs)

- **Provider coverage**: `ACSP`, `OAK/AX`, `PRINCIPAL`, `WOODLANDS` are uncovered/anomalous job-sheet principals needing triage before parity claims (`docs/reference/data/provider_coverage_matrix.md`).
- **Review-required-by-design cases**: e.g. TEN 01/02 (no address block), AMS 01 (client address ≠ vehicle location) — left as review-required under the inspection-site safety policy.
- **UI technology is an open decision** (`docs/architecture/parser_ui_cli.md`): modernized Tkinter vs Windows desktop vs local web. Bears on whether the staff UI is throwaway or converges with the future platform UI.
- **OCR / cloud document intelligence**: deterministic-first; cloud OCR is feature-flagged off and gated by governance.
- **EVA/Sentry**: no parser dependency on live location lookup (no suitable read endpoint); any live read/write belongs to the `bridge`.

## Hard constraints / guardrails

- Deterministic-first (ADR 0007); ground-up compatible rebuild, do not import the monolith wholesale (ADR 0004).
- Preserve all 26 presets, EVA field order, six-line address, DD/MM/YYYY, and private-real-corpus-only testing (ADR 0008).
- No personal injury / KADOE scope. Human review remains the gate before export.

## Open design questions for the interview

1. What is the *primary goal* of this next parser iteration — close review-required/coverage gaps to "release-ready", modernise the staff UI, or add a new capability?
2. UI direction: keep/modernise Tk, or move the staff UI toward the web stack the unified platform will use (avoid throwaway work)?
3. How far to push provider coverage now (the 4 uncovered principals) vs deferring to the `providers` sub-area?
4. Where exactly is the parser ↔ bridge boundary for EVA export and evidence packaging?
5. Cloud OCR / document-intelligence: keep off, or open a governed option-paper evaluation?

*(These are resolved during the interview and promoted into the expanded `plan.md`, `open-questions.md`, and a dated spec under `docs/superpowers/specs/`.)*
