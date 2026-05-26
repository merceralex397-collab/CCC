# Local Tooling Requirements

## Current Availability

Available in the bundled Python runtime:

- `pypdf`
- `python-docx`
- `openpyxl`
- `pandas`
- PIL

Not currently available on PATH or in the bundled Python runtime:

- LibreOffice/`soffice`
- Pandoc
- Tesseract
- PyMuPDF
- pdfplumber
- `extract-msg`
- OCRmyPDF
- MarkItDown
- Outlook/Word COM libraries

## Recommended Local-First Stack

- PDF native text: PyMuPDF primary, `pypdf` fallback.
- PDF tables/layout: `pdfplumber` targeted fallback.
- DOCX: `python-docx` plus direct OOXML inspection.
- Legacy `.DOC`: Microsoft Word automation where Office is installed, with LibreOffice headless conversion as a service/CI fallback.
- MSG: `extract-msg` or equivalent pure-Python parser.
- XLSM/XLSX: `openpyxl`/`pandas` for structure and values. Do not execute macros.
- OCR: Tesseract/pytesseract as local fallback; OCRmyPDF only as optional batch normalization.
- Markdown normalization: MarkItDown can help bulk companions, but CCC parser extraction must remain provenance-aware and rule-backed.

LibreOffice is important only for local headless conversion of legacy Office files. It is not part of Collision Engineers' business workflow.
