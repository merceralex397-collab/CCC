# Legacy CE Document Mapper Behavior Inventory

Date: 2026-05-24
Status: implemented reference inventory
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-25
Source links: `../cedocumentmapper/app.py`, `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json`, `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json`, `docs/plans/parser-extraction/parser-mvp/plan.md`
Roadmap milestone: Section 2 - Parser, Provider, And Corpus Core
Dependencies: provider coverage baseline, parser MVP implementation
Expected outputs: compatibility inventory for extraction, provider detection, rule methods, normalization, validation blockers, and EVA export order
Acceptance criteria: new parser keeps compatibility where required and records deliberate divergences
Verification required: `python -m pytest`, `python tools/run_parser_corpus.py`
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Inventory Summary

`../cedocumentmapper/app.py` is the behavior oracle, not an architecture source. It combines Tk UI, local app data, provider editing, extraction, rule execution, image export, DOC export, and JSON export in one module. The rebuild preserves its user-visible extraction concepts while separating readers, provider detection, rule execution, validation, review, package, and EVA export.

## Extraction Cascade

- PDF: PyMuPDF block extraction first, simple page text fallback second, pypdf fallback if PyMuPDF cannot return text.
- OCR: only attempted for short image-only PDFs with one image per page. It is not default for native PDFs.
- DOCX: python-docx plus OOXML header/footer/textbox inspection.
- DOC: Word COM, LibreOffice conversion, or antiword. The rebuild adds an OLE WordDocument/RTF fallback so legacy `.DOC` corpus files still parse when Word/LibreOffice/antiword are unavailable.
- MSG/EML: body, headers, date, and attachment names are extracted without Outlook automation. The rebuild goes further by materializing attachments to a local parser cache and routing attached instruction/evidence files back through the shared triage and reader pipeline.
- Images/image PDFs: treated as evidence/review material when no text is present.

## Provider Detection

Legacy behavior requires every configured detect phrase to match. More specific presets win by phrase count and phrase length. This is required for shared phrases such as `FW (Garage)` and `FW (Solicitor)`.

The rebuild keeps this rule and adds match diagnostics in audit metadata: matched phrases, score, provider count, reader method, and provider config version.

## Mapping Rule Methods

The active provider config uses:

- `manual_input`
- `single_label`
- `two_labels`
- `fixed_position`
- `fixed_position_label`
- `single_label_offset`
- `email_date`

The rebuild supports these methods in `src/ccc_parser/rules.py`. A review against `tests/parsertests/output1.json` showed that strict legacy blank-rule behavior leaves visibly present CNX engineer-report values blank. The parser now preserves provider rules as the primary source but deliberately improves on the monolith by applying deterministic fallbacks only when a preset is blank or when a legacy fixed-position rule returns document-control noise. Unsupported or image-only sources remain review-required, not silent successes.

## Normalization And Export Gates

Compatibility preserved:

- Work Provider is required before EVA export.
- Dates normalize to `DD/MM/YYYY`.
- VRMs are uppercased and stripped of whitespace.
- Mileage extracts the first numeric run.
- Inspection Address exports in the legacy six-line shape.
- `Image-based Assessment` remains a valid legacy inspection-address line 1.
- EVA JSON key order follows `Final Format Example 02.json`.

Deliberate improvements:

- Canonical parser results include provenance, confidence, warning, validation, source file, image, and audit objects.
- Deterministic fallbacks extract clearly labelled values such as CNX VRM, client, reference, dates, desktop-assessment mode, and accident circumstances where the legacy config had blank fields.
- Invalid fixed-position values from legacy `.DOC` binary/OLE noise are suppressed and replaced with visible letterhead/label dates where available.
- Inspection site is internally separated into mode, source, structured lines, postcode, confidence, and evidence.
- Validation runs before EVA export and can block export unless an explicit review copy is requested.
- Evidence package image order is represented as data: two preview slots followed by all images including previews again.
- Drag/drop is exposed through the rebuilt Tk UI using `tkinterdnd2` when available; the callback still calls the shared parser service rather than duplicating extraction logic.
