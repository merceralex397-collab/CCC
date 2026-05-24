# Parser Extraction Workspace

## Purpose

This workspace owns all planning for the CCC instruction parser, extraction adapters, provider detection engine, mapping rule engine, OCR fallback strategy, and corpus regression harness.

## Scope Rules

- Parser output must pass canonical schema validation before EVA-specific output is generated.
- The CE Document Mapper monolith (`cedocumentmapper`) must not be imported wholesale. Its behaviours are oracle evidence for the rebuild, migrated deliberately through this workspace.
- Provider coverage must be tracked in `docs/reference/data/provider_coverage_matrix.md` before adding or changing provider rules.
- Cloud OCR and document intelligence are future adapters behind governance and feature flags; they must not be the default runtime path.
- Personal injury and KADOE workflows are out of scope.

## Evidence Sources

| Source | Role |
| --- | --- |
| `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json` | 26 provider presets and extraction mapping methods |
| `docs/reference/raw/collisionrelateddocs/claudechat.md` | Legacy CE Document Mapper behaviours (field order, date format, inspection address, mileage/VAT constraints) |
| `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json` | Authoritative EVA JSON field order |
| `docs/reference/normalized/collisionrelateddocs__collision_releated__handover.docx.md` | Job sheet VBA helpers, network folder paths, OCR cutoff notes |
| `docs/research/siderpdf.md` | PDF cascade strategy: PyMuPDF → pdfplumber → pypdf → OCR |
| `docs/research/gptdeepresearch.md` | Hybrid document extraction research, native-first/OCR fallback |
| `docs/reference/originalplanning/cedocumentmapper_rebuild_plan_pack_all_zips/` | Ground-up compatible rebuild plan and mapper behavioural oracle |
| `docs/reference/data/provider_coverage_matrix.md` | Current provider preset list and gap tracking |

## Workspace Layout

- `parser-mvp/plan.md` — current executable parser MVP implementation plan
- `tickets/` — phased implementation tickets
- `option-papers/` — unresolved design choices (cloud OCR, state-store, adapter approach)
- `archived_plans/` — implemented or superseded plans

## AGENTS.md Cross-Reference

> Current parser MVP implementation work lives at `docs/plans/parser-extraction/parser-mvp/plan.md`.
> Parser rules: keep UI and CLI thin; both must call the same parser core and share validation/export contracts.
