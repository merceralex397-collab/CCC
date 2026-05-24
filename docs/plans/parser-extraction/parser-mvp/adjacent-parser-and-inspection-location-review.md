# Adjacent Parser And Inspection Location Review

Date: 2026-05-24
Status: active evidence and decision note
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/reference/adjacent_repositories.md`, `docs/reference/raw/collisionrelateddocs/Instructions/`, `docs/reference/normalized/`, `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json`, `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json`, `docs/reference/raw/collisionrelateddocs/collision_releated/Sentry_API_Complete_Guide.md`, `docs/reference/raw/collisionrelateddocs/collision_releated/Backup of CE Job Sheet 260309.xlsm`, `docs/operations/job_sheet_spreadsheet_companion.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`, `../cedocumentmapper/app.py`, `../collisionpdf/`, `../cedocumentmapper_v2.0/`
Roadmap milestone: Section 2 - Parser, Provider, And Corpus Core
Dependencies: provider-principal-config, intake-storage-integrations, governance-security, operations-quality, user-experience-interfaces
Expected outputs: source-backed parser design decisions, inspection-location policy, adjacent-repository comparison, atomic parser handoff tasks
Acceptance criteria: parser MVP implementation can cite exact evidence for parity requirements, deliberate divergences, and unresolved inspection-site lookup questions
Verification required: `python tools/verify_scaffold.py`, provider corpus regression plan review, EVA JSON field-order test review
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Question Answered

This note answers two open parser-design questions:

- How does the existing official parser handle inspection address/site data?
- Can the new parser obtain inspection-site data from EVA/Sentry by API call?

It also records how the parser MVP plan should use the adjacent parser repositories, current instruction corpus, job sheet workbook, spreadsheet companion, FigJam workflow export, final EVA JSON example, and Sentry API guide.

## Source Set Examined

| Source | Evidence used |
| --- | --- |
| `docs/reference/adjacent_repositories.md` | Defines `../cedocumentmapper` as the current official behavior reference, `../collisionpdf` as parser-first experiment, and `../cedocumentmapper_v2.0` as contract-first scaffold. |
| `../cedocumentmapper/app.py` | Official current behavior for text extraction cascade, provider detection, provider rules, field extraction, inspection-address normalization, and export gating. |
| `../collisionpdf/` | Useful parser-service patterns: native extraction IR, OCR fallback boundary, schema validation, warnings, and tests. Its tests are synthetic, so it is not proof of production parser parity. |
| `../cedocumentmapper_v2.0/docs/architecture/module-boundaries.md` and `docs/contracts/module-interfaces.md` | Useful module boundaries: readers produce document models, provider detection emits matches, rule engine emits field extractions, exporters serialize reviewed records. |
| `../cedocumentmapper_v2.0/docs/migration/v1-to-v2.md` and `docs/tickets/EPIC-08-regression-harness.md` | Useful migration and regression-harness shape. |
| `docs/reference/raw/collisionrelateddocs/Instructions/` and `docs/reference/normalized/` | Real instruction corpus, including PDF, DOCX, DOC, MSG, and image-pack examples. |
| `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json` | Current 26 provider presets and their inspection-address methods. |
| `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json` | Required final EVA JSON field order and six-line `Inspection Address` string shape. |
| `docs/reference/raw/collisionrelateddocs/collision_releated/Sentry_API_Complete_Guide.md` | Available EVA/Sentry write and report retrieval endpoints; no documented general location lookup endpoint. |
| `docs/reference/raw/collisionrelateddocs/collision_releated/Backup of CE Job Sheet 260309.xlsm` | Operational `Jobs`, `Principals`, and `Garages` data. `Principals` records image-based/address handling; `Garages` records garage address/contact lookup data. |
| `docs/operations/job_sheet_spreadsheet_companion.md` | Explains workbook role and confirms `Garages` is inspection-address/contact lookup evidence. |
| `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md` | Confirms real workflow: instruction/images/query splitting, Not Ready/Ready states, garage image/estimate chasing, EVA setup, Box backup, Outlook/WhatsApp reporting. |

## Existing Parser Handling

The current official parser in `../cedocumentmapper/app.py` treats inspection address as one configured output field. It does not model `inspection_mode`, `inspection_site_source`, or garage identity separately.

Observed behavior:

- Extraction uses provider preset rules from `Settings Backup/providers.json`.
- Inspection address can be `manual_input`, `single_label`, or `two_labels` depending on provider.
- Several providers manually output `Image-based Assessment` instead of an address.
- Address extraction can be forced to isolate a postcode for providers that set `force_postcode_for_inspection_address`.
- Export-time normalization converts the inspection-address value into exactly six lines for the EVA JSON payload.
- Empty inspection address exports as six blank lines.
- `Image-based Assessment` exports as line 1 followed by five blank lines.
- Real addresses are normalized into body lines plus postcode, with overflow folded into line 5.
- There is no live EVA/Sentry lookup for garage or inspection-site data inside the parser.
- `FW (Garage)` and `FW (Solicitor)` are separate presets; garage instructions extract an inspection-location block, while solicitor instructions use manual `Image-based Assessment`.

Provider config evidence from `Settings Backup/providers.json`:

| Inspection-address method | Count | Meaning |
| --- | ---: | --- |
| `single_label` | 10 | Extract from one label such as `Address:`, `Vehicle Location:`, `currently located at:`, or `Location`. |
| `two_labels` | 8 | Extract between start/end labels such as `Inspection Location` to `Should you have`, or `Address` to `Work`. |
| `manual_input` | 8 | Use fixed/manual values such as `Image-based Assessment`, or leave blank for review. |

Representative provider behaviors:

| Provider | Current inspection-address behavior |
| --- | --- |
| `ALISON` | `single_label` from `Address:`. |
| `ALS` | manual `Image-based Assessment`. |
| `AX` | manual `Image-based Assessment`. |
| `BC` | `single_label` from `Address:` with postcode forcing. |
| `DFD` | `single_label` from `Vehicle location`. |
| `FW (Garage)` | `two_labels` from `Inspection Location` to `Should you have`, with postcode forcing. |
| `FW (Solicitor)` | manual `Image-based Assessment`. |
| `HDUK` | `single_label` from `currently located at:`. |
| `KBS` | `single_label` from `The vehicle is currently located at:`. |
| `QDOS` | manual `Image-based Assessment`. |
| `RJS` | `two_labels` from `Address` to `Work`. |
| `TEN` | `single_label` from `currently stored at`. |

## EVA/Sentry Lookup Feasibility

Based on `Sentry_API_Complete_Guide.md`, the parser MVP should not depend on EVA/Sentry to obtain inspection sites.

Documented endpoints relevant to this question:

| Endpoint | What it supports | Parser MVP implication |
| --- | --- | --- |
| `POST /Instruction/Inspection` | Creates an inspection instruction and accepts `InspType` values such as vehicle damage inspection and desktop. The documented payload does not provide a general inspection-site lookup. | Useful future write path only; not a source of missing location data. |
| `POST /Claim/LocationUpdate` | Writes claim location data with `LocationName`, `Address`, `Postcode`, and `LocationType` values such as `REPAIRER`, `INSPECTION`, `INSURED`, `THIRDPARTY`. | Confirms EVA can receive location data, but this is an update endpoint, not a read/search endpoint. |
| `GET /Report/GetAvailableReports` | Lists released reports. | Not a live instruction-location lookup. |
| `GET /Report/GetReport?id={id}` | Retrieves a released report data structure. | May provide historical/released report metadata, but it is not a reliable pre-setup inspection-site source for new instructions. |

Decision: the parser should extract or review inspection-site data from the instruction corpus, provider config, job sheet, garage lookup, and staff correction. EVA/Sentry can be a later destination for reviewed location updates after governance/security and integration design, not an MVP dependency for filling missing inspection-site fields.

## Job Sheet, Companion, And FigJam Evidence

The workbook has three relevant sheets:

| Sheet | Parser-relevant evidence |
| --- | --- |
| `Jobs` | Current operational queue with VRM, principal, client, vehicle, missing-info status, due date, and folder path. Missing values include `Instructions`, `Images`, `Estimate/images`, and `Instructions/Images`. |
| `Principals` | Maps solicitor/work-provider names to EVA code, Box code, inbox, instruction receipt style, Drag in to EVA, images location, image-based/address instructions, and report routing. |
| `Garages` | Garage name, address, email, phone, and figures. This is inspection-address/contact lookup evidence, but belongs to provider/principal config rather than parser extraction rules. |

Useful `Principals` examples:

| Principal/provider evidence | Inspection-location implication |
| --- | --- |
| Alison | Image based if not residential address; ask sender to confirm in some cases. |
| ALS | Image-based. |
| AX | Images from garage; check inspection type, inspection location, case number, request date. |
| Baker Coleman | Sometimes physical; use client address if image quality is not enough; otherwise image based. |
| BlackStone | Confirm address with client/source; special storage/garage addresses appear for named sources. |
| DFD | Address can be in email; named image source can imply a known address. |
| Fairway | Garage/storage evidence differs between garage and solicitor paths. |
| GGP/KBS/RJS direct | Request images and inspection location from client/source. |
| QDOS | Always image-based assessment. |
| Oakwoods | Garage address if from garage, otherwise ask client to confirm. |
| QCL | Can be image based or client address depending on channel and case. |

FigJam evidence reinforces this split. Incoming work is separated into instruction, images, and queries; incomplete work remains Not Ready; staff may message garages for images/estimates; EVA setup happens after required evidence exists. Therefore inspection site is not purely a parser field. It is a reviewed work-item fact that may be extracted, inferred from controlled lookup, or requested from a sender.

## Decision Register

| Decision | Status | Reasoning and source evidence |
| --- | --- | --- |
| Preserve legacy six-line `Inspection Address` export. | accepted | `Final Format Example 02.json` and `../cedocumentmapper/app.py` require exactly this export shape. |
| Add richer canonical inspection fields internally. | accepted | Current parser loses meaning by putting both addresses and `Image-based Assessment` into one field. Job sheet and FigJam evidence show mode, source, and site may differ. |
| Do not use EVA/Sentry as an MVP inspection-site lookup source. | accepted | `Sentry_API_Complete_Guide.md` documents location update and released report retrieval, but no general live claim/location read/search endpoint. |
| Keep garage lookup outside parser extraction rules. | accepted | Workbook `Garages` and companion describe operational lookup/contact data; primary ownership belongs to `provider-principal-config`. Parser can suggest a controlled lookup match only after provider-config design. |
| Use `cedocumentmapper` as behavior oracle, not imported architecture. | accepted | `AGENTS.md` and ADR 0004 require a compatible rebuild without wholesale monolith import. |
| Adopt `collisionpdf` provenance/schema patterns but not its accuracy claims. | accepted | It is parser-first and useful, but its tests are synthetic and not production proof. |
| Adopt `cedocumentmapper_v2.0` module boundaries where useful. | accepted | Its contracts align with thin UI/CLI and shared parser core requirements. |

## Recommended Canonical Inspection Fields

The parser MVP should keep the final EVA payload unchanged while the internal parser result separates meaning:

| Field | Purpose |
| --- | --- |
| `inspection_mode` | `physical`, `image_based`, `unknown`, or `review_required`. |
| `inspection_site_source` | `instruction_text`, `provider_manual_rule`, `garage_lookup`, `principal_policy`, `staff_review`, `eva_history`, or `unknown`. |
| `inspection_address_lines` | Structured address lines before legacy six-line export formatting. |
| `inspection_site_name` | Garage/storage/site name when available separately from address. |
| `inspection_postcode` | Postcode as a structured value when detected or confirmed. |
| `inspection_location_confidence` | Confidence and review state. |
| `inspection_location_evidence` | Source file, page/email/body location, provider rule id, or lookup id. |

The EVA JSON adapter should convert those fields back into the legacy `Inspection Address` string only after validation/review.

## Parser MVP Atomic Tasks

1. Create a legacy behavior inventory for `../cedocumentmapper/app.py` covering PDF, DOCX, DOC, MSG, provider detection, rule methods, normalization, export gating, and JSON ordering.
2. Create an adjacent-repository comparison table covering `cedocumentmapper`, `collisionpdf`, and `cedocumentmapper_v2.0`, with adopted patterns and rejected patterns.
3. Build a fixture ledger for every raw instruction file under `docs/reference/raw/collisionrelateddocs/Instructions/`.
4. Link each fixture to its normalized companion under `docs/reference/normalized/`.
5. Record provider, file type, extraction method, expected fields, missing fields, and review blockers for each fixture.
6. Convert all 26 provider presets from `Settings Backup/providers.json` into versioned test fixtures before behavior changes.
7. Add field-order tests against `Final Format Example 02.json`.
8. Add six-line inspection-address export tests for real address, image-based assessment, blank value, postcode forcing, and overflow line handling.
9. Add inspection-mode tests for providers with manual image-based behavior and providers with extracted physical addresses.
10. Add review-required behavior for provider/principal workbook cases where job-sheet policy says staff must ask sender or garage.
11. Add a controlled design link to `provider-principal-config` for garage lookup and principal image/address policy.
12. Add a controlled design link to `intake-storage-integrations` for later EVA/Sentry `LocationUpdate` writes and released-report reads.
13. Keep cloud OCR and document intelligence behind an option paper and off by default.
14. Keep UI and CLI thin over the same parser services and validation/export contracts.

## Unknowns To Resolve Before Implementation Acceptance

| Unknown | Blocking level | Required resolution |
| --- | --- | --- |
| Whether any real EVA/Sentry tenant exposes a private location read/search endpoint not documented in `Sentry_API_Complete_Guide.md`. | non-blocking for MVP, blocking for live lookup design | Ask EVA/Sentry or inspect approved tenant docs; do not assume it exists. |
| Whether workbook `Garages` should become canonical provider-config seed data. | blocking for garage lookup automation | Provider-principal-config must define migration, validation, ownership, and correction workflow. |
| Whether every provider has at least one authoritative fixture with enough fields for full EVA JSON snapshot. | blocking for parity claim | Fixture ledger must label full, partial, and review-required cases. |
| Whether image-based assessment should still be represented in final EVA `Inspection Address` or mapped to a later Sentry `InspType`. | non-blocking for parser MVP export, blocking for live EVA submission | Preserve current export for MVP; revisit in EVA/Sentry adapter design. |
