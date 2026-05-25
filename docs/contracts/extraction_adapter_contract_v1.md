# Extraction Adapter Contract v1

## Purpose

Extraction adapters normalize file-specific parsing into a shared intermediate representation used by provider detection, mapping rules, validation, UI review, and golden tests.

## Supported File Types For MVP Planning

- PDF;
- DOCX;
- legacy DOC;
- MSG;
- EML;
- image files;
- batch folders containing mixed evidence.

## Adapter Output

| Field | Required | Notes |
| --- | --- | --- |
| `adapter_name` | yes | For example `pymupdf_pdf`, `pdfplumber_table`, `docx_ooxml`, `msg_email`. |
| `adapter_version` | yes | Semantic or build version. |
| `source_file_id` | yes | Source file/hash reference. |
| `document_type_guess` | yes | Instruction, email, image pack, report, unknown, etc. |
| `pages` | no | Page-level text, blocks, images, dimensions. |
| `tables` | no | Structured table output where found. |
| `email` | no | Sender, recipients, subject, body, attachments for MSG/EML. |
| `images` | no | Extracted or referenced image metadata. |
| `warnings` | yes | Adapter-level issues. |
| `provenance` | yes | Method, page, bbox/span, parser confidence where available. |

## Required Behaviour

- Do not reduce layout-rich documents to plain text before the geometry/table passes have had a chance to run.
- Preserve page numbers, text spans, bounding boxes, block order, and extraction method when available.
- OCR is a fallback for image-only or failed native extraction, not a default for every PDF.
- Short image-only instruction PDFs may use a locally configured or bundled Tesseract binary; image-only evidence packs remain review material and must not be OCRed into EVA-exportable instructions by default.
- Adapter failures must be recoverable and visible to the review queue.
- External converter helpers must use bounded timeouts and fall through to the next extraction fallback where possible.
- Email attachment extraction must use per-parse workspaces so concurrent parses of the same source cannot delete each other's attachments.

## PDF Cascade Baseline

1. PyMuPDF geometry/text blocks first.
2. pdfplumber for table/layout fallback.
3. pypdf for text fallback.
4. OCR only where justified by scan detection, missing native text, or staff/operator choice.

## Sources

- `docs/research/siderpdf.md`
- `docs/research/gptdeepresearch.md`
