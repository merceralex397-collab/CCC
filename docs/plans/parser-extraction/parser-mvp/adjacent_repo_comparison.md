# Adjacent Repository Comparison

Date: 2026-05-24
Status: implemented comparison note
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/adjacent_repositories.md`, `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`, `../cedocumentmapper/app.py`, `../collisionpdf/`, `../cedocumentmapper_v2.0/`
Roadmap milestone: Section 2 - Parser, Provider, And Corpus Core
Dependencies: parser MVP implementation, provider coverage baseline, operations-quality regression gates
Expected outputs: adopted/rejected pattern record for the parser rebuild
Acceptance criteria: implementation choices cite adjacent evidence without copying unsupported architecture wholesale
Verification required: `python -m pytest`, `python tools/run_parser_corpus.py`
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Adopted Patterns

| Source | Adopted |
| --- | --- |
| `../cedocumentmapper/app.py` | Extraction cascade order, all-phrases provider detection, legacy rule method names, six-line inspection address export, date/VRM/mileage normalization, and Work Provider export gate. |
| `../collisionpdf/` | Reader/output separation, native extraction before OCR, confidence/warning concepts, schema-style validation before export, and regression-report thinking. |
| `../cedocumentmapper_v2.0/` | Module boundary pattern: readers -> detection -> rules -> normalization/validation -> exporters -> UI/CLI. |

## Rejected Patterns

| Source | Rejected |
| --- | --- |
| `../cedocumentmapper/app.py` | Monolithic Tk/provider/parser/export implementation, UI-owned parsing behavior, and implicit export behavior without canonical validation. |
| `../collisionpdf/` | Synthetic fixture accuracy claims as parity evidence. CCC uses the private real instruction corpus as the regression baseline. |
| `../cedocumentmapper_v2.0/` | Treating contract scaffold as implemented production behavior. CCC imported the boundary ideas, not the incomplete implementation. |

## Resulting Rebuild Approach

The parser MVP now has a shared Python core used by CLI and staff UI. Readers return source-linked document models; provider detection explains match strength; rules emit canonical fields with provenance; validation gates EVA export; and package manifests carry image order data. This is deliberately superior to the legacy tool because parser behavior is testable without the UI, corpus regression is repeatable, and review-required cases are explicit.

