# Parser UI And CLI Architecture

## Implementation Status

The parser MVP now has a shared Python core in `src/ccc_parser/`:

- `core.py` orchestrates triage, reading, provider detection, rule extraction, validation, and result envelopes.
- `readers.py` implements deterministic extraction for PDF, DOCX, DOC, MSG, EML, images, image-only PDFs, email attachments, and normalized-companion fallback where the source is review-only.
- `rules.py`, `normalization.py`, and `validation.py` implement provider rule execution, canonical field normalization, inspection-mode derivation, and export gates.
- `rules.py` first applies provider presets, then uses deterministic fallbacks for clearly labelled values when a preset is blank or when a legacy fixed-position rule returns document-control noise.
- `exporters/eva.py` preserves the `Final Format Example 02.json` key order.
- `packaging.py` emits the evidence package image order rule.
- `cli.py` and `ui/app.py` both call these shared services.

Current verification:

- `python -m pytest`
- `python tools/run_parser_corpus.py`
- `python tools/verify_scaffold.py`

## UI Requirement

The initial parser is not fully automated. Non-technical office staff must be able to import files, inspect extraction results, correct fields, view warnings, export EVA-ready JSON/payloads, and package images/evidence without using a terminal.

Required UI capabilities:

- drag/drop and file-picker import for PDFs, DOCX, DOC, MSG/EML, images, and batches;
- batch navigation and blocked/manual-review queues;
- source text preview;
- extracted field review and correction;
- provider preset selection and provider mismatch warning;
- image extraction/export area;
- EVA JSON/payload preview;
- validation warnings for missing VRM, provider, images, mileage, or inspection address;
- audit metadata and blocker report export.

Current staff UI implementation:

- imports supported source files through the shared parser core;
- accepts drag/drop when `tkinterdnd2` is installed, with file-picker import as the desktop fallback;
- displays provider, validation status, blockers, warnings, extracted fields, and full parser-result JSON;
- supports manual field correction and revalidation;
- saves parser results, EVA JSON review/export payloads, and evidence package manifests.

## CLI Requirement

The CLI must expose the same parser core behavior for automation and AI-agent usage:

- import/extract;
- batch parse;
- validate;
- export JSON/payload;
- export images;
- emit audit metadata and blocker sidecars.

Current CLI commands:

- `ccc-parser triage <path>`
- `ccc-parser parse <path> [--provider <unique-code-or-full-name>] [--output result.json]`
- `ccc-parser validate <result.json>`
- `ccc-parser export-eva <result.json> [--allow-blockers] [--output eva.json]`
- `ccc-parser package <result.json> [--output package.json]`
- `ccc-parser batch <folder> [--output batch.json]`
- `ccc-parser providers list`
- `ccc-parser providers validate <config>`

Provider overrides accept a full provider name or a unique code. Shared codes such as `FW`, `MP`, and `PCH` must use the full preset name so the parser cannot silently select the wrong provider variant.

## Technology Decision

The detailed UI technology decision remains open. The comparison matrix is in `docs/decisions/options/ui_platform_options.md`.

Regardless of platform, the UI must use the same parser, validation, export, and package services as the CLI. A local web UI is the strongest current candidate for the first staff workflow spike, with WinUI/Tauri/desktop options still available if deployment constraints require a native app.
