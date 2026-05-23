# 08 — Technical Architecture

Generated: 2026-05-22

## Architecture principle

Start with a narrow, modular system that proves the workflow. Do not begin with a large enterprise platform.

The first build should be easy to demo, easy to reason about and easy to replace piece by piece later.

## Prototype architecture

```text
React / Next.js frontend
        ↓
API backend: FastAPI or Node/Express
        ↓
Local file storage: /uploads
        ↓
PDF parser: PyMuPDF / pdfplumber
        ↓
Optional OCR layer
        ↓
AI service for classification/extraction/drafting
        ↓
SQLite database
        ↓
Markdown/HTML engineer pack
        ↓
PDF export
```

## Production architecture

```text
Inbound channels
  - Outlook/shared mailbox
  - Website/repairer portal
  - WhatsApp Business API or approved integration
  - Client API
  - Manual upload
        ↓
Intake service
        ↓
Document processing queue
        ↓
Storage layer
  - encrypted object storage
  - immutable original files
  - derivative text/OCR files
        ↓
Structured database
        ↓
AI processing services
  - classifier
  - extractor
  - matcher
  - pack generator
  - chaser drafter
        ↓
Review UI
        ↓
Case pack/report workflow
        ↓
Audit/logging/analytics
```

## Recommended first stack

| Component | Recommended for demo | Notes |
|---|---|---|
| Frontend | Next.js / React | Fast, familiar, flexible. |
| Backend | FastAPI | Strong Python PDF/OCR/AI ecosystem. Node is also acceptable. |
| DB | SQLite | Sufficient for local demo; easy to inspect. |
| Storage | Local filesystem | Use clear folder structure for demo. |
| PDF extraction | PyMuPDF + pdfplumber | Use both if needed; templates vary. |
| OCR | Tesseract or cloud OCR later | Skip or minimal for demo unless scanned PDFs are required. |
| LLM | OpenAI/Claude/Gemini API | Choose after data-governance discussion. |
| Export | Markdown/HTML first | PDF export second. |
| Auth | None/local-only for demo | Add auth for production. |

## Why FastAPI is a good fit

FastAPI is a Python web framework. In plain terms, it lets the React dashboard talk to Python code that reads PDFs, calls AI models and stores results. It fits because Python has mature libraries for PDF parsing, OCR, data extraction and machine-learning workflows.

## File storage design

Use a case-oriented folder structure:

```text
/storage
  /originals
    /<document_id>_<filename>
  /case_files
    /<case_id>
      /documents
      /images
      /packs
      /exports
  /ocr_text
    /<document_id>.txt
  /ai_runs
    /<run_id>.json
```

Always preserve original files unchanged.

## Processing pipeline

### Step 1 — Upload

- Save original file.
- Create `Document` record.
- Generate checksum/hash.
- Record upload event.

### Step 2 — Classification

Classify each file as:

- instruction PDF;
- Audatex/repair estimate;
- repair invoice;
- vehicle image;
- loose note/email text;
- unknown.

Use rules first, AI second.

### Step 3 — Extraction

For PDFs:

- extract text layer;
- fall back to OCR if text is absent;
- run structured extraction;
- store source snippets or page references where possible.

### Step 4 — Matching

Match evidence using:

- extracted registration;
- extracted claim reference;
- filename;
- upload batch;
- source sender/channel when available;
- date/time proximity;
- document type;
- later, image metadata or visible registration.

### Step 5 — Review

- Auto-attach high-confidence evidence.
- Route low-confidence matches to admin review.
- Log match reasons.

### Step 6 — Pack generation

- Pull structured case fields.
- Pull evidence list.
- Pull estimate summary.
- Pull unresolved missing items.
- Pull review flags.
- Generate markdown/HTML.
- Store pack version.

## AI provider abstraction

Create a provider interface so the backend can swap models later.

```ts
interface AIProvider {
  classifyDocument(input): Promise<DocumentClassification>
  extractInstruction(input): Promise<InstructionFields>
  parseEstimate(input): Promise<EstimateFields>
  suggestMatches(input): Promise<MatchSuggestion[]>
  generateChaser(input): Promise<MessageDraft>
  generateEngineerPack(input): Promise<PackDraft>
}
```

Do not hard-code the app to one model provider.

## Retrieval / knowledge base later

A RAG system can come later. It would let staff search prior reports, standard clauses and repair/ABP/Audatex guidance. RAG means the model retrieves approved documents before answering, so answers can point back to sources.

Phase-one does not need a full RAG system. It needs robust intake and pack generation.

## Integration options

### Outlook/email

- Monitor shared mailbox.
- Ingest attachments and email text.
- Save sender/subject/date metadata.
- Do not auto-send externally in phase one.

### WhatsApp

- For production, use approved WhatsApp Business API/integration.
- For demo, use pasted WhatsApp text and uploaded images.

### Repairer portal

- The website already includes a repairer portal concept.
- A production system could connect portal submissions directly into the case queue.

### Audatex

- Start with PDFs/exports.
- Use AudaConnect only if licensed and approved.
- Do not scrape or reverse-engineer Audatex.

### Calendar/engineer booking

- Start with manual assignment.
- Add Outlook/Google Calendar integration after workflow proof.
- Route optimisation is later-phase unless physical inspection volume justifies it.

## Security baseline

Production must include:

- role-based access control;
- encrypted storage;
- audit logs;
- source file immutability;
- retention rules;
- secure API keys;
- environment separation;
- DPIA if personal data and AI processing are involved;
- data processing agreements with vendors;
- human approval for external communications and final reports.

## Prototype shortcuts allowed

The demo may:

- use local file storage;
- use SQLite;
- use synthetic data;
- skip authentication;
- skip live email/WhatsApp integrations;
- skip OCR unless needed;
- use markdown/HTML pack export first.

## Prototype shortcuts not allowed

Even the demo should not:

- use real personal claim data without approval;
- claim final expert decisioning;
- send messages automatically;
- hide the source of extracted information;
- overwrite original files;
- imply live Audatex integration without licence confirmation.
