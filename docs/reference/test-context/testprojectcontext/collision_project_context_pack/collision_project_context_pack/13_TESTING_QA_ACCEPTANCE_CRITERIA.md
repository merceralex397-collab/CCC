# Testing, QA, and Acceptance Criteria

## Purpose

Define how to prove the automation works before trusting it with production records.

## Test levels

### Unit tests

Test individual functions:

- Filename sanitisation.
- Checksum generation.
- Email classification rules.
- Reference number regex.
- Date normalization.
- JSON schema validation.
- EVA payload mapping.

### Integration tests

Test external systems in sandbox/test mode:

- Microsoft Graph mailbox read/download.
- Box folder creation and upload.
- Box metadata apply/update.
- OCR/extraction service call.
- EVA JSON import/API submission.

### End-to-end tests

Test the full workflow using representative emails and documents:

```text
sample email -> intake -> Box storage -> extraction -> validation -> review -> EVA test import -> status update
```

### Regression tests

Whenever a parser, prompt, schema, or mapping changes, run all known sample documents again to ensure old cases still work.

## Sample corpus

Create a test corpus with expected outputs.

Minimum set:

- Standard text-based PDF.
- Scanned PDF.
- PDF with multiple pages.
- Email with one PDF and images.
- PDF email followed by separate image email.
- Email with multiple PDFs.
- Duplicate email.
- Unsupported attachment.
- Low-quality image/scan.
- Known EVA validation failure.

## Gold-standard outputs

For each sample document, manually prepare:

- Expected canonical JSON.
- Expected Box folder/file layout.
- Expected spreadsheet/control row.
- Expected EVA payload.
- Expected review requirement.

## Extraction evaluation

Measure by field:

```text
field_name, expected_value, extracted_value, match, confidence, method, notes
```

Key metrics:

- Critical field accuracy.
- Required field recall.
- False positives.
- False auto-approval rate.
- Review correction rate.

## Acceptance criteria by phase

### Phase 1: intake and Box storage

Accept when:

- Relevant emails are detected.
- PDFs and images are downloaded.
- Files are uploaded to the correct Box folder.
- File checksums are stored.
- Duplicate attachments do not create duplicate work items.
- Failures are visible in the control table.

### Phase 2: extraction and validation

Accept when:

- Extraction produces valid canonical JSON.
- Required fields are flagged when missing.
- Low-confidence fields require review.
- Evidence snippets/page references are captured where possible.
- Reviewers can see and correct extracted values.

### Phase 3: EVA import

Accept when:

- Approved canonical data maps to valid EVA JSON.
- Test/sandbox EVA imports succeed.
- EVA errors are captured and routed correctly.
- Duplicate submissions are prevented.
- Payload and response are stored for audit.

### Phase 4: operational rollout

Accept when:

- Monitoring dashboard is live.
- Runbooks exist for common failures.
- Access controls are reviewed.
- Staff know how to review exceptions.
- Manual fallback process is documented.

## Negative tests

Do not only test happy paths. Include:

- Corrupt PDF.
- Password-protected PDF.
- Missing attachment.
- Duplicate email.
- Same image sent twice.
- Conflicting reference numbers.
- Invalid date.
- EVA unavailable.
- Box metadata failure.
- Graph token failure.

## Performance tests

Measure:

- Time from email received to file stored.
- Time from file stored to extraction complete.
- Time from approval to EVA import.
- Throughput under expected peak volume.
- Cost per document if using paid OCR/AI.

## Manual fallback criteria

Manual processing must remain possible when:

- The automation is unavailable.
- EVA integration is down.
- A document type is unsupported.
- The business needs to process a case urgently.

Manual fallback should still record work item status so the automation does not later duplicate the record.

## Release gates

Do not release to production until:

- Test mailbox and Box sandbox pass end-to-end tests.
- EVA sandbox/test import is proven.
- Data protection/security review is complete enough for pilot.
- A named operations reviewer can handle exceptions.
- A named technical owner can respond to failures.
