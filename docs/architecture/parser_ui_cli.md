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

The scaffold keeps the UI implementation as a thin Python module. The detailed UI technology decision remains open between modernized Tkinter, a Windows desktop UI, and a local web UI. The default bias is the lowest-friction Windows office deployment that does not block a later dashboard.
