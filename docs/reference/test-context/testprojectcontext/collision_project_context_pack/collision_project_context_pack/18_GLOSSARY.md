# Glossary

## API

An API is a way for software systems to talk to each other. Instead of a person clicking buttons in EVA or Box, the automation sends structured requests to those systems.

## JSON

JSON is a text format for structured data. It is easy for software to read and write.

Example:

```json
{
  "case_reference": "ABC123",
  "vehicle_registration": "AB12 CDE"
}
```

## OCR

OCR means optical character recognition. It converts pictures of text into actual text that software can process. It is needed when PDFs are scanned images rather than text-based documents.

## LLM

LLM means large language model. It is an AI model trained to process language. In this project, an LLM could help read inconsistent PDF text and return structured fields. It should be validated because it can make mistakes.

## AI extraction

AI extraction means using AI to pull structured fields from unstructured documents. Example: reading a PDF and returning a JSON object with `vehicle_registration`, `inspection_date`, and `case_reference`.

## Prompt

A prompt is the instruction given to an AI model. For extraction, prompts should be strict and schema-driven so the model returns only the fields needed.

## Hallucination

A hallucination is when an AI model returns information that is not actually supported by the source document. In this project, prompts and validation should explicitly prevent guessing.

## Confidence score

A confidence score estimates how reliable an extracted field is. It should be based on evidence such as OCR confidence, validation rules, repeated matching, and whether the value appears clearly in the document.

## Human-in-the-loop

A process where automation handles routine work, but a person reviews cases when the automation is uncertain or the consequences of an error are significant.

## Webhook

A webhook is a way for one system to notify another system when something happens. For example, Outlook/Microsoft Graph can notify the automation when a new message arrives, and Box can notify a service when a file is uploaded.

## Idempotency

Idempotency means the same operation can run more than once without causing duplicate or harmful results. For example, retrying an EVA submission should not create two EVA records for the same work item.

## State machine

A state machine is a controlled workflow where each item has a status and only allowed transitions can happen. Example: `received -> files_stored -> extracted -> needs_review -> ready_for_eva -> eva_imported`.

## Canonical data model

A canonical data model is the project’s internal standard shape for data. It sits between PDFs and EVA, so the system can change PDF parsers or EVA mappings without rewriting everything.

## Adapter

An adapter is a small integration layer that converts from the internal model into a specific system’s format. An EVA adapter would turn canonical work item data into EVA’s required JSON.

## Schema

A schema defines the expected shape of data. For JSON, it says which fields exist, which are required, and what types they should have.

## Validation

Validation checks whether data is complete and correctly formatted. Example: checking whether a date is in ISO format or whether an EVA-required field is missing.

## Metadata

Metadata is data about a file or record. In Box, metadata could include work item ID, case reference, sender email, received date, extraction status, and EVA status.

## Checksum

A checksum is a fingerprint of a file’s content. If two files have the same checksum, they are very likely identical. It helps detect duplicates and verify integrity.

## Work item

A work item is the automation’s internal record for one intake/case. It links the email, source files, extracted fields, review decisions, and EVA import result.

## Review queue

A list of work items that need human attention because they are incomplete, low confidence, duplicated, unmatched, or failed.

## Sandbox

A safe test environment that behaves like a real system but does not affect production records. EVA sandbox access is important before automated imports go live.

## Audit trail

A record of what happened, when, and by whom. In this project, the audit trail should connect the source email to Box files, extraction output, review changes, and EVA submission.

## MCP

MCP usually refers to Model Context Protocol. It is a way to expose tools and data sources to AI agents in a controlled interface. For this project, MCP-style tools could eventually let an agent search work items, inspect failures, or generate EVA payload previews.

## Agent

An agent is software that can choose actions/tools to complete a goal. In this project, agents should assist with investigation and review, while deterministic workflows handle critical processing.
