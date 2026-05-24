# Parser Extraction — Source Map

Date: 2026-05-24
Status: active
Owner: unassigned

This map tracks how raw evidence and original planning packs feed into active parser planning.

## Raw Evidence

| File | Key Facts |
| --- | --- |
| `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json` | 26 provider presets with extraction methods: `Single Label`, `Two Labels`, `Fixed Position`, `Regex`, `Manual Input`, `Address Block`. |
| `docs/reference/raw/collisionrelateddocs/claudechat.md` | Legacy CE Document Mapper field order, date format (`DD/MM/YYYY`), six-line inspection address handling, mileage/VAT/unit constraints, image ordering (2 previews + all), BEL/control-char cleanup, blank-line offset, engineer-report overwrite guard. |
| `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json` | Authoritative EVA JSON field order for export validation. |
| `docs/reference/normalized/collisionrelateddocs__collision_releated__handover.docx.md` | OCR only when justified; native-first extraction; network folder paths `\\192.168.0.106\...`. |
| `docs/reference/data/provider_coverage_matrix.md` | 26 covered presets; `ACSP`, `OAK/AX`, `PRINCIPAL`, `WOODLANDS` uncovered or anomalous. |

## Research Promotions

| Source | Promoted Finding | Destination |
| --- | --- | --- |
| `docs/research/siderpdf.md` | PDF cascade: PyMuPDF geometry first → pdfplumber table fallback → pypdf fallback → OCR only where justified. | `parser-mvp/plan.md` |
| `docs/research/gptdeepresearch.md` | Hybrid extraction: native-first, OCR fallback, confidence/validation, EVA not internal model. | `parser-mvp/plan.md`, extraction adapter contract. |

## Original Planning Promotions

| Pack | Promoted | Destination |
| --- | --- | --- |
| `cedocumentmapper_rebuild_plan_pack_all_zips/` | Ground-up compatible parser rebuild, legacy mapper behavioural oracle, EVA export boundary. | `parser-mvp/plan.md`, ADR 0004. |
| `ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md` | Extraction package design, provider rules migration. | P1-001 ticket. |

## Uncovered Principal Triage Required

- `ACSP` — real provider, no preset; triage needed before parity claim.
- `OAK/AX` — composite mapping case; model as provider-rule composition or manual review.
- `PRINCIPAL` — likely spreadsheet header or data-quality artefact; review before treating as provider.
- `WOODLANDS` — real provider, no preset; triage needed.
