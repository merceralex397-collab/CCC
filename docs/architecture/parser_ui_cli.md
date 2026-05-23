# Parser UI And CLI Architecture

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

## CLI Requirement

The CLI must expose the same parser core behavior for automation and AI-agent usage:

- import/extract;
- batch parse;
- validate;
- export JSON/payload;
- export images;
- emit audit metadata and blocker sidecars.

## Technology Decision

The detailed UI technology decision remains open. The comparison matrix is in `docs/decisions/options/ui_platform_options.md`.

Regardless of platform, the UI must use the same parser, validation, export, and package services as the CLI. A local web UI is the strongest current candidate for the first staff workflow spike, with WinUI/Tauri/desktop options still available if deployment constraints require a native app.
