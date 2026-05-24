# P2 Parser Hardening And Provider Parity Tickets — Redirected

> **This file is a tombstone/redirect.** Tickets have been relocated to their owning workspaces as part of the docs/plans workspace expansion (2026-05-24). This file is preserved so that scaffold verifier path checks continue to pass.

- Status: redirected.
- Owner: unassigned.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`.
- Roadmap milestone: P2 Parser Hardening And Provider Parity.
- Dependencies: P1 Operational Core MVP.
- Expected outputs: see new workspace ticket files below.
- Acceptance criteria: all P2 tickets exist in their owning workspace.
- Verification required: scaffold verifier path checks pass.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: see new workspace paths below.

## Ticket Relocation Map

| Ticket | New Location |
| --- | --- |
| P2-001 Golden Corpus Regression Harness | `docs/plans/parser-extraction/tickets/p2-golden-corpus-regression.md` |
| P2-002 Provider Parity And Uncovered Principals | `docs/plans/provider-principal-config/tickets/p2-provider-parity.md` |
| P2-003 Extraction Adapter Hardening | `docs/plans/parser-extraction/tickets/p2-parser-hardening.md` |
| P2-004 UI/CLI Parity Hardening | `docs/plans/parser-extraction/tickets/p2-parser-hardening.md` |

## P2-001 Golden Corpus Regression Harness

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md`, `docs/decisions/0008-private-real-corpus-only.md`.
- Roadmap milestone: P2 Parser Hardening And Provider Parity.
- Dependencies: P1-001.
- Expected outputs: private corpus fixture registry, expected result snapshots, provider regression runner.
- Acceptance criteria: all 26 provider presets have golden examples and expected canonical outputs; diffs are reviewable.
- Verification required: corpus regression command passes for current accepted baseline.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.
## P2-002 Provider Parity And Uncovered Principals

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/reference/data/provider_coverage_matrix.md`, `docs/contracts/provider_principal_config_contract_v1.md`.
- Roadmap milestone: P2 Parser Hardening And Provider Parity.
- Dependencies: P2-001.
- Expected outputs: triage decisions for `ACSP`, `OAK/AX`, `PRINCIPAL`, `WOODLANDS`, provider-priority list for all requested providers.
- Acceptance criteria: uncovered principals are either implemented, mapped to existing provider logic, marked data-quality issue, or captured in the all-ideas ledger with reason.
- Verification required: provider matrix updated and regression harness covers implemented additions.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.

## P2-003 Extraction Adapter Hardening

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/contracts/extraction_adapter_contract_v1.md`, `docs/research/siderpdf.md`, `docs/research/gptdeepresearch.md`.
- Roadmap milestone: P2 Parser Hardening And Provider Parity.
- Dependencies: P1-001, P2-001.
- Expected outputs: hardened PDF cascade, table extraction fallback, legacy DOC conversion path, MSG/EML attachment handling, image/OCR fallback rules.
- Acceptance criteria: extraction failures produce structured warnings; OCR is not run by default on native PDFs; provenance is retained.
- Verification required: adapter-level tests and corpus cases for native, table-heavy, scanned, DOC, DOCX, MSG, EML, image pack, and batch folder inputs.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.

## P2-004 UI/CLI Parity Hardening

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/architecture/parser_ui_cli.md`, `docs/plans/operational-core/parser-mvp/plan.md`.
- Roadmap milestone: P2 Parser Hardening And Provider Parity.
- Dependencies: P1-002, P1-003.
- Expected outputs: shared service API, parity checklist, accessibility/usability fixes, batch progress/error reporting.
- Acceptance criteria: every parser/export/package action exposed in UI has CLI equivalent and uses same core validation.
- Verification required: parity tests and staff workflow walkthrough.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.
