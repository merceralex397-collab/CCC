# External Services And Vendor Review

## Box

Box is the initial storage integration. CCC needs an adapter that can create or locate a case folder, upload evidence files, apply metadata, and return stable storage references. Live upload is not part of this scaffold.

Official docs: https://developer.box.com/

## Azure Document Intelligence

Azure Document Intelligence is a future candidate if CCC storage/hosting moves to Azure. It can support OCR and document layout extraction, but any use must pass privacy, cost, data-residency, and vendor review.

Official docs:

- https://learn.microsoft.com/azure/ai-services/document-intelligence/
- https://learn.microsoft.com/azure/ai-services/document-intelligence/prebuilt/read

## AWS Textract

AWS Textract is a future candidate for OCR/form/table extraction if CCC chooses AWS.

Official docs: https://docs.aws.amazon.com/textract/

## Google Document AI

Google Document AI is a future candidate if CCC chooses Google Cloud storage/hosting.

Official docs: https://cloud.google.com/document-ai/docs

## Local-First Rule

The parser-first MVP uses local extraction/OCR by default. Cloud processing is an adapter decision, not an implicit fallback.
