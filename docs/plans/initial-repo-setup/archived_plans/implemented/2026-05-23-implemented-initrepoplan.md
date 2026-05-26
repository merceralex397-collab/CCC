# Implemented State

- Status: implemented
- Implemented date: 2026-05-23
- Delivered summary: Repository hygiene docs, canonical documentation scaffold, source manifest, normalized companions/blockers, provider coverage matrix, parser UI/CLI scaffold, contracts, roadmap, and verification script were created.
- Verification performed: `tools/verify_scaffold.py` plus targeted file/content checks.
- Follow-up work moved elsewhere: Provider golden-rule implementation, production UI buildout, real EVA payload validation, live Box upload, cloud storage selection, and cloud OCR/document-intelligence vendor review.

---

# CCC Initial Repository Scaffold Plan

## Current Task Boundary

This file is the active plan for the initial CCC repository scaffold. This hardening pass only updates `initrepoplan.md`; it does not initialize git, move files, commit raw docs, scaffold parser code, install conversion tools, normalize documents, or implement parser behaviour.

While active, this file is the scaffold plan only. It must also establish the repository document hierarchy so the many generated plan packs do not remain as competing active instructions. When this plan is fully implemented, move it to `docs/plans/operational-core/archived_plans/implemented/`, rename it `YYYY-MM-DD-implemented-initrepoplan.md`, and add an implemented-state note at the top.

## Summary

Build `CCC` into the canonical private repository for Collision Command Centre, starting with a rebuilt parser foundation rather than the workflow dashboard. The first delivery target is an internal MVP: a Python parser core with a full office-staff UI and equivalent CLI automation interface. It must preserve CE Document Mapper behaviour for vehicle-damage instruction parsing, produce validated EVA-ready JSON/payload outputs, support initial Box evidence-storage integration, and keep raw evidence plus normalized Markdown companions traceable.

The scope is vehicle damage only. Collision Engineers do not do personal injury or KADOE work, so personal injury, KADOE keeper lookup, MIB/OIC workflows, bodily-injury medical evidence, fraud/liability conclusions, and non-vehicle property workflows must not be planned into CCC.

## Parser-First MVP Boundaries

- First product slice: local parser package, full parser UI, equivalent CLI, provider configuration, test corpus, and validated EVA-ready JSON/payload output.
- The parser UI is a first-class deliverable for non-technical office staff. It must support drag/drop import, batch navigation, source text preview, extracted field review/editing, provider preset selection/configuration, confidence/warning display, image extraction/export, EVA JSON/payload preview, validation feedback, and clear blocked/manual-review states.
- The CLI must call the same parser core and expose equivalent functionality for automation and AI-agent usage: import, extract, batch, validate, export JSON/payload, export images, and emit audit/metadata sidecars.
- EVA-ready means local schema/payload validation and manual review. It does not mean direct Sentry API submission.
- No live Outlook ingestion, case-management dashboard, MCP/tool gateway, WhatsApp automation, valuation automation, or workflow orchestration in this initial parser-first scaffold.
- Box is an initial integration track for evidence storage and case package handoff. The parser MVP may start with manual export/package output, but the repository scaffold must include Box integration contracts, metadata requirements, and adapter boundaries from the start.
- Do not import `cedocumentmapper` source into CCC initially. Reference the adjacent `cedocumentmapper` repo as the behaviour source and document any extracted requirements in CCC.
- Use local-first extraction/OCR. Cloud OCR or external document intelligence services require a later privacy and vendor review.

## Key Changes

- Initialize `C:\Users\PC\Documents\GitHub\CCC` as the canonical private git repo only after repo privacy, `.gitignore`, source manifest, hashes, and secret/PII scan are confirmed.
- Add root hygiene and project docs: `README.md`, `AGENTS.md`, `.gitignore`, `.gitattributes`, source manifest, roadmap, architecture docs, decision log, glossary, requirements, and contracts.
- Preserve raw documents unchanged and create normalized Markdown/metadata companions.
- Commit raw files into the private repo using normal git only after private-repo safety gates pass. If safety cannot be confirmed, record a blocker before committing.
- Build `src/ccc_parser/`, parser UI project structure, CLI entrypoints, and `tests/` around a shared parser core.
- Add initial Box integration planning docs and contracts, even if live Box upload is implemented after parser/UI parity.
- Define a storage abstraction so Box can be the first integration while future CCC-owned storage can move to Google Cloud, AWS, or Azure without rewriting parser/export logic.

## Source-Of-Truth Hierarchy

Use this hierarchy when consolidating the existing plan packs and source docs:

1. Raw operational sources are immutable evidence: original PDFs, DOC/DOCX/MSG/XLSM/JAM files, settings backups, `claudechat.md`, `Final Format Example 02.json`, EVA/Sentry docs, and current provider/job-sheet files.
2. Normalized companions are derivatives: extracted Markdown/text, metadata JSON, hashes, OCR output, and generated summaries. They must link back to raw sources and must not replace them.
3. Generated plan packs are reference inputs unless explicitly promoted. Their README/index files and numbered plans are not active instructions by default.
4. Canonical repo docs are the only active project guidance after consolidation: `README.md`, `docs/source_manifest.md`, `docs/roadmap.md`, `docs/architecture/`, `docs/contracts/`, `docs/decisions/`, `docs/glossary.md`, and active tickets.
5. Implementation tickets are the execution layer. A plan-pack idea becomes actionable only after it is triaged into a ticket with source links, acceptance criteria, dependencies, and roadmap placement.

## Plan Pack Triage

The implementation must organize the numerous existing plans and generated packs, not just create new docs around them. At minimum, classify these current top-level inputs:

- `originalplans_output`
- `ce_system_plans_enhanced`
- `ce_phase4_agents_reviewed_plan`
- `phase7_expanded_markdown_plan`
- `collision_engineers_ai_tools_plans_markdown`
- `collision_engineers_bulk_data_research_pack`
- `cedocumentmapper_rebuild_plan_pack_all_zips`
- `testprojectcontext`
- `docs/reference/raw/collisionrelateddocs`

Each pack or folder must be marked as `raw-source`, `normalized-derivative`, `generated-reference`, `active-plan`, `backlog-ticket`, `implemented`, `superseded`, or `parked`. Preserve generated pack provenance where possible: generated date, source files used, generator/chat context, and which items were promoted into tickets.

## Raw Source And Normalized Companion Contract

- Raw files are immutable. Do not edit, rename destructively, re-save, or overwrite them during normalization.
- Every raw source gets a manifest record with original path, canonical path, size, hash, file type, source pack/folder, normalized companion path, extraction method, extraction confidence, and blockers.
- Every normalized Markdown or metadata companion must link back to the raw source hash.
- Failed or low-confidence conversions produce a documented blocker companion rather than silently losing wording.
- Image-only PDFs, scanned PDFs, `.msg`, legacy `.DOC`, and image-heavy Office files must be explicitly marked as complete, partial, blocked, or requiring OCR/manual QA.

## Conversion Toolchain Relevance And Blockers

LibreOffice matters because it is the practical local tool for headless conversion and text extraction from legacy `.DOC` and some Office files. It is not important for the business workflow itself; it is important because without a reliable converter, wording in legacy Word files can be missed.

Recommended local-first extraction approach:

- PDF native text: use PyMuPDF as the primary extractor because the existing CE parser already moved in that direction for better text/table rendering; keep `pypdf` as a fallback and retain the `/uniXXXX` cleanup path.
- PDF tables/layout: add `pdfplumber` as a targeted table/layout extractor for documents where PyMuPDF/pypdf text order is insufficient.
- DOCX: use `python-docx` plus direct OOXML inspection for headers, footers, text boxes, tables, and embedded images.
- Legacy `.DOC`: prefer Microsoft Word automation on Windows where Office is installed, with LibreOffice headless conversion as the service/CI-friendly fallback. Treat `antiword` as a last-resort compatibility option, not the primary strategy.
- MSG: use `extract-msg` or an equivalent pure-Python Outlook message parser; avoid Outlook COM automation as the default path because it is brittle for staff machines and automation.
- XLSM/XLSX: use `openpyxl`/`pandas` for workbook structure and values, but separately document VBA/macro behaviours because `openpyxl` does not execute macros.
- OCR: use Tesseract/pytesseract as the local fallback for scanned/image-only PDFs. Consider OCRmyPDF only as an optional batch-normalization tool for searchable PDF generation, not as the parser's first runtime dependency.
- Markdown companions: consider Microsoft MarkItDown for bulk source-to-Markdown normalization, but not as the parser of record for field extraction because field provenance, provider rules, source spans, and confidence are CCC-specific.
- Cloud OCR/document intelligence: keep Azure Document Intelligence, AWS Textract, and Google Document AI as later adapter candidates. Azure is a strong future candidate if CCC chooses Azure storage/hosting because it can combine storage, OCR, and document layout services, but cloud processing must be gated by privacy, cost, data residency, and vendor review.
- The plan should record missing converter requirements and blockers first. It should not install or configure these tools until implementation is explicitly approved.

Current local tool availability observed during planning:

- Available in bundled Python: `pypdf`, `python-docx`, `openpyxl`, `pandas`, and PIL.
- Not currently available on PATH or in bundled Python: LibreOffice/`soffice`, Pandoc, Tesseract, PyMuPDF, pdfplumber, `extract-msg`, OCRmyPDF, MarkItDown, and Outlook/Word COM libraries.
- Adjacent repos already use or require several missing tools: `cedocumentmapper` depends on PyMuPDF, `pypdf`, `python-docx`, `extract-msg`, `pytesseract`, and optional Windows COM; `collisionpdf` uses PyMuPDF, pdfplumber, Pillow, pytesseract, OpenCV, and JSON schema validation.

## Parser UI And CLI Requirements

The parser must be usable by non-technical office staff without automation:

- Provide a clear import surface for PDFs, DOCX, DOC, MSG/EML, images, and batches.
- Show source text, extracted fields, provider match, extraction warnings, and confidence indicators side by side.
- Allow staff to correct fields before export without modifying raw source files.
- Preserve existing CE Document Mapper concepts where still valid: minimal/day-to-day view, expanded/configuration view, provider presets, batch navigation, engineer-report merge rules, image export, and JSON export.
- Make validation failures plain: missing VRM, missing provider, missing images, low-confidence OCR, unsupported file type, duplicate/ambiguous provider, and manual field requirements.
- Produce the same exports as the CLI: CE JSON, EVA-ready payload preview, images, audit metadata, and blocker reports.
- Keep UI and CLI thin. Both must call the same parser core and share the same validation/export contracts so office workflows and automation/AI-agent workflows cannot drift.

The initial UI technology choice should be made during implementation planning after comparing the current Tkinter app, a modern Windows desktop UI, and a local web UI. The default bias should be the lowest-friction Windows office deployment that preserves staff usability and does not block a future web/dashboard system.

## Provider Source Of Truth And Coverage Gaps

Parser provider parity source of truth is `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json`, which currently contains 26 parser provider presets:

`ALISON`, `ALS`, `AMS`, `AX`, `BC`, `BLACK`, `CNX (Engineers)`, `DFD`, `EVA (Engineers)`, `FW (Garage)`, `FW (Solicitor)`, `HDUK`, `KBS`, `KERR`, `KMR`, `MP (Branded)`, `MP (Simple)`, `OAK`, `PCH (Lawshield)`, `PCH (Performance)`, `QCL`, `QDOS`, `RJS`, `SBL`, `SWAN`, `TEN`.

The current job-sheet backups each have 58 `Principals` rows. Across `Backup of CE Job Sheet 260429.xlsm` and `Backup of CE Job Sheet 260309.xlsm`, a read-only comparison found 51 unique principal name/code rows, with 21 covered by parser config and 30 raw uncovered rows. Actual `Jobs!E` usage is narrower: across both backups there are 19 unique nonblank actual job principal values, with 17 covered and 2 uncovered: `ACSP` and `WOODLANDS`.

High-confidence uncovered candidates present in the job-sheet `Principals` tables but not covered by parser config:

`ABRAHAMS` / Abrahams Solicitors, `ACSP` / Accident Specialists Direct jobs, `ASLS` / Affinity Seven Law Solicitors, `ALL` / Alliance &Cooper, `AS` / Aman Solicitors Advocates, `VRM ARIANNA` / Arianna Autos, `AVI` / Avisons Solicitors, `BAKER` / Baker Hardman, `CASTLE` / Castle, `CW` / Countrywide, `FRZ` or `FRAZ`, `GG` or `GGP` / Graham Coffey, `HTU` / HTU Assessors Ltd, `LEX` / LEX Solicitors, `LPS` / LPS Solicitors, `MATT` / Matt Rowland Solicitors, `MBH` / MBH Solicitors, `R1AM/MOTORX`, `RL` / Regent Law Ltd, `RELAY` / Relay Motor Group, `ROZZII` / ROZZII or Green Destinations, `SS` / Savas & Savage, `STALLION` / Stallion, `TP` / Taylor Price, `TA` / Turnams, `WIL` / Williams & Co, `WLS` or `WOODLANDS` / Woodlands, `ZEN` / Zenith Lawyers.

`Mapped Principals.xlsx` has 65 entries; 23 are covered and 42 are not covered by parser aliases. Mapped-only uncovered codes with no detailed `Principals` table row in the two backups include `SWADE`, `WHITELINE`, `HALO`, `RC`, `FOCUS`, `EMPIRE`, `VOGUE`, `MCADE`, `PRESTIGE`, `PEBBLE`, `SKY`, `HVL`, `BROADWAY`, `ARSHED`, `CLIFTON`, `PROACTIVE`, `SILVER 100`, `SUSSEX`, `PREMIER`, `OSMAN`, `MOORHEY`, `SLUG`, `WATERMANS`, and `CAN`. `ACSP` appears as a lost cause with OCR quality noted as too low. `Questgates or Brownsword` is treated as info-only/non-actionable for parser coverage because both EVA and Box codes are `N/A`.

The implementation must not assume the parser covers all operational principals. It must create a provider coverage matrix that separates:

- parser presets currently implemented;
- current job-sheet principals not parser-covered;
- code-only or historical entries from `Mapped Principals.xlsx`;
- lost-cause/unparseable providers;
- provider aliases and principal/EVA/Box code conflicts.

## Documentation And Archive Rules

- Create `docs/source_manifest.md` that inventories every raw source, normalized derivative, generated plan pack, archive, and active project doc.
- Add a status for each document or pack: `raw-source`, `normalized-derivative`, `generated-reference`, `active-plan`, `backlog-ticket`, `implemented`, `superseded`, or `parked`.
- Keep generated packs under a reference area such as `docs/reference/originalplanning/` or `archive/originalplanning/`; do not leave them looking like current implementation plans.
- Archive completed plans in `docs/plans/operational-core/archived_plans/implemented/`.
- Archive superseded or merged plans in `docs/plans/operational-core/archived_plans/superseded/` with a pointer to the replacement doc or ticket.
- Every active plan or ticket must have a status block with: status, owner, created date, last reviewed date, source links, roadmap milestone, acceptance criteria, verification required, and supersedes/superseded-by fields.
- When a plan or ticket is fully implemented, move it to the appropriate archive folder, rename it to indicate completion, and add a top-of-document status block confirming implementation completed, completion date, delivered summary, verification performed, and follow-up work moved elsewhere.
- Archived plans must not remain ambiguous active instructions.

## Roadmap

1. Repo safety, inventory, and secret hygiene.
2. Documentation consolidation: classify all existing plans/packs, create `docs/source_manifest.md`, and define the active doc hierarchy.
3. Source normalization: preserve raw sources unchanged, generate Markdown/metadata companions, and record hashes.
4. Plan/ticket promotion: triage plan-pack ideas into one backlog using the repeated priority pattern across packs: P0 foundations, P1 core adapters/workflow, P2 data/intelligence, P3 external integrations.
5. Parser-first scaffold: build shared parser core, full parser UI, equivalent CLI, and `tests/`.
6. Provider coverage matrix: distinguish current parser presets, uncovered job-sheet principals, historical/code-only principals, lost causes, and pilot priorities.
7. Provider parity for the 26 current parser presets.
8. Canonical data boundary: map parser output into a versioned canonical schema before EVA-specific payloads.
9. EVA-ready JSON/payload validation: preserve `Final Format Example 02.json` field order and add schema/golden tests.
10. Initial Box integration planning: define folder/package structure, metadata, upload boundaries, retention assumptions, and adapter contract.
11. Storage abstraction planning: support Box first, with a future path to CCC-owned storage on Google Cloud, AWS, or Azure.
12. Workflow expansion only after parser reliability, UI/CLI parity, canonical schema, source manifest, and plan/ticket lifecycle are proven.

## Test Plan

- Verify every source file appears in the manifest with path, size, hash, type, status, source pack, and canonical destination.
- Verify normalized Markdown companions exist or have a documented blocker.
- Verify every generated plan pack is classified in `docs/source_manifest.md` and marked reference-only unless promoted.
- Verify no root-level or pack-level document remains ambiguous as an active plan.
- Verify each promoted plan-pack item has a ticket with source links, dependencies, acceptance criteria, and roadmap placement.
- Verify archived or superseded plans include status blocks and replacement pointers.
- Run parser golden tests across all 26 parser provider presets.
- Verify parser UI and CLI call the same core extraction, validation, and export contracts.
- Verify the parser UI supports the non-technical staff workflow without requiring CLI usage.
- Assert CE JSON field order exactly matches `Final Format Example 02.json`.
- Create and verify a provider coverage matrix for parser presets, current job-sheet principals, mapped-principal codes, and lost causes.
- Verify Box integration requirements are captured in contracts before any live upload implementation.
- Validate no source files changed after organization by comparing pre/post hashes.
- Run secret scans before any commit or remote push.

## Assumptions And Open Business Details

- CCC MVP is vehicle-damage evidence focused only.
- The existing plan packs are mixed-quality generated/reference material. They should be preserved for traceability, but the repository must promote only selected items into the canonical roadmap and tickets.
- Box is an initial integration and should be planned from the repository scaffold onward, but live upload can follow parser/UI parity and adapter-contract approval.
- Microsoft 365/Outlook intake is not part of this parser-first scaffold unless a later active ticket promotes it.
- Future CCC-owned storage may use Google Cloud, AWS, or Azure. Azure should remain a serious option because Azure Document Intelligence could align storage and document extraction, but provider selection is a future architecture decision.
- Valuation provider choice is unresolved: Glass's, CAP HPI, Auto Trader, Experian/HPI, or another service must be selected before live valuation automation.
- Current local tooling lacks several recommended parser/normalization dependencies; the implementation must add them deliberately or record blockers for legacy `.DOC`, `.msg`, table-heavy PDFs, and OCR-heavy files.
