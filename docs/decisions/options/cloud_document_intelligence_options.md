# Option Paper: Cloud OCR And Document Intelligence

Date: 2026-05-23

## Status

Open decision. Cloud OCR/document intelligence is not part of the default parser runtime.

## Decision Needed

Choose if and when CCC should add a cloud OCR/document-intelligence adapter for difficult scans, image-only documents, table-heavy inputs, or future metadata enrichment.

## Current Official Capability Notes

- Azure AI Document Intelligence layout model supports document structure extraction including text, tables, selection marks, and document structure. Microsoft documentation for Document Intelligence v4.0 notes support for PDF, image formats, and Office formats such as DOCX/XLS/PPTX for the layout model: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout
- Amazon Textract `AnalyzeDocument` supports feature types such as tables, forms, signatures, layout, and queries, with inputs including JPEG, PNG, PDF, and TIFF: https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeDocument.html
- Google Document AI provides processors for OCR, form parsing, layout parsing, classification, splitting, and extraction, with integration into Cloud Storage and BigQuery: https://cloud.google.com/document-ai/docs/overview
- Box AI structured extraction can extract metadata from supported document and image formats and applies OCR for image files and scanned documents. Box also announced Box Extract in January 2026 for configurable extraction agents: https://developer.box.com/guides/box-ai/ai-tutorials/extract-metadata-structured and https://support.box.com/hc/en-us/articles/48235161543955-Announcing-Box-Extract-Jan-2026

## Options

| Option | Strengths | Risks | Fit |
| --- | --- | --- | --- |
| Azure Document Intelligence | Strong layout/table/document structure story; Azure may fit future storage/app hosting. | Cloud data transfer and cost; service limits and model drift need governance. | Strong candidate for future adapter. |
| AWS Textract | Mature OCR/forms/tables APIs and AWS integration. | File type limits and AWS-specific storage/auth patterns. | Good if CCC chooses AWS storage. |
| Google Document AI | Strong processor model, OCR/layout/form parsing, and BigQuery/Cloud Storage integration. | Requires GCP setup and processor/version management. | Good if CCC chooses Google Cloud. |
| Box AI/Box Extract | Close to initial Box storage workflow; supports metadata extraction over stored files. | Ties extraction to Box and AI agent behaviour; may not provide deterministic parser parity. | Useful later after Box live upload and governance. |
| Local-only OCR | Keeps sensitive files local and deterministic where possible. | Lower accuracy on difficult scans, local dependency setup burden. | Baseline fallback for parser MVP. |

## Required Guardrails

- Do not OCR every PDF by default.
- Do not send private files to a cloud service without approval.
- Keep deterministic native extraction first.
- Require feature flags, provenance, confidence, cost logging, and manual review gates.
- Adapter output must map into `docs/contracts/extraction_adapter_contract_v1.md`.

## Required Follow-Up

- Select sample scanned/image-heavy cases from the private corpus.
- Compare local OCR, Azure, AWS, Google, and Box AI/Extract on accuracy, provenance, latency, cost, and operational fit.
- Decide provider only after storage/deployment direction is clearer.

