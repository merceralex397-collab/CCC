# Runbook: EVA Rejected Payload

Status: future P3 runbook placeholder.

## Trigger

EVA/Sentry rejects a submitted payload or returns an unexpected response.

## Immediate Action

- Stop retrying automatically.
- Preserve exported EVA JSON and submission response.
- Keep the work item in review or export-failed state.
- Notify an operator/reviewer.

## Checks

- token expiry;
- field names and order;
- date format `DD/MM/YYYY`;
- required principal/case/claim fields;
- image package ordering;
- duplicate submission risk.

## Recovery

Correct the reviewed canonical data or adapter mapping, regenerate export, and resubmit only with explicit approval.

