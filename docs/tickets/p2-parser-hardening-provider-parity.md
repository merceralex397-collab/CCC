# P2 Parser Hardening And Provider Parity Tickets

## P2-001 Golden Corpus Regression Harness

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md`, `docs/decisions/0008-private-real-corpus-only.md`.
- Dependencies: P1-001.
- Expected outputs: private corpus fixture registry, expected result snapshots, provider regression runner.
- Acceptance criteria: all 26 provider presets have golden examples and expected canonical outputs; diffs are reviewable.
- Verification: corpus regression command passes for current accepted baseline.
- Archive target: `archive/plans/implemented/`.

## P2-002 Provider Parity And Uncovered Principals

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/data/provider_coverage_matrix.md`, `docs/contracts/provider_principal_config_contract_v1.md`.
- Dependencies: P2-001.
- Expected outputs: triage decisions for `ACSP`, `OAK/AX`, `PRINCIPAL`, `WOODLANDS`, provider-priority list for all requested providers.
- Acceptance criteria: uncovered principals are either implemented, mapped to existing provider logic, marked data-quality issue, or parked with reason.
- Verification: provider matrix updated and regression harness covers implemented additions.
- Archive target: `archive/plans/implemented/`.

## P2-003 Extraction Adapter Hardening

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/contracts/extraction_adapter_contract_v1.md`, `docs/research/siderpdf.md`, `docs/research/gptdeepresearch.md`.
- Dependencies: P1-001, P2-001.
- Expected outputs: hardened PDF cascade, table extraction fallback, legacy DOC conversion path, MSG/EML attachment handling, image/OCR fallback rules.
- Acceptance criteria: extraction failures produce structured warnings; OCR is not run by default on native PDFs; provenance is retained.
- Verification: adapter-level tests and corpus cases for native, table-heavy, scanned, DOC, DOCX, MSG, EML, image pack, and batch folder inputs.
- Archive target: `archive/plans/implemented/`.

## P2-004 UI/CLI Parity Hardening

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/architecture/parser_ui_cli.md`, `docs/plans/parser_mvp_implementation_plan.md`.
- Dependencies: P1-002, P1-003.
- Expected outputs: shared service API, parity checklist, accessibility/usability fixes, batch progress/error reporting.
- Acceptance criteria: every parser/export/package action exposed in UI has CLI equivalent and uses same core validation.
- Verification: parity tests and staff workflow walkthrough.
- Archive target: `archive/plans/implemented/`.

