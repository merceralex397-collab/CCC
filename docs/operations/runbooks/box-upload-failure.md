# Runbook: Box Upload Failure

Status: future P3 runbook placeholder.

## Trigger

Live Box upload fails, partially uploads, or returns unexpected folder/file ids.

## Immediate Action

- Keep the local Box-ready package unchanged.
- Do not delete partial remote files until reviewed.
- Record the storage attempt id and error.
- Provide staff with local package fallback.

## Checks

- Box credentials and permissions;
- folder naming conflicts;
- file size/path restrictions;
- network failure;
- checksum mismatch.

## Recovery

Retry from the package manifest after confirming duplicate handling.

