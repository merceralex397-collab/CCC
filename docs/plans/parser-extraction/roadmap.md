# Parser Extraction — Roadmap

Date: 2026-05-24
Status: active
Owner: unassigned

## Sequence

| Phase | Milestone | Key Deliverables |
| --- | --- | --- |
| P0 | Foundation | Contracts baseline, provider coverage matrix, parser MVP plan, private-corpus-only ADR. |
| P1 | Parser Core MVP | Deterministic parser core, all 26 provider presets, UI/CLI parity, EVA JSON export, image ordering, golden corpus tests. |
| P2 | Hardening And Provider Parity | Golden corpus regression harness, triage of `ACSP`/`OAK/AX`/`PRINCIPAL`/`WOODLANDS`, extraction adapter hardening (PDF/DOCX/DOC/MSG/EML/image), UI/CLI parity hardening. |
| P3+ | Long-Range | Cloud document intelligence (behind governance gate), automated batch ingestion at scale, corpus expansion. |

## Gating Rules

- No provider preset added without entry in `docs/reference/data/provider_coverage_matrix.md`.
- No cloud OCR/document intelligence in default runtime path until privacy, cost, data-residency, and vendor review complete.
- Parser output must pass canonical schema validation before EVA export is generated.
- UI and CLI must call the same parser core and share validation/export contracts.
