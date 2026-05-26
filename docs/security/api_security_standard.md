# API Security Standard

Date: 2026-05-23

## Applies To

Future CCC APIs and adapters, including Box, Outlook/Graph, EVA/Sentry, DVLA/DVSA, valuation services, and cloud OCR/document intelligence.

## Minimum Rules

- Store credentials outside the repository.
- Use named CCC app accounts for audit; do not rely on shared mailbox identity.
- Use least-privilege tokens/scopes.
- Never log secrets, access tokens, refresh tokens, or full credential payloads.
- Record integration attempts and failures as audit events.
- Add dry-run or sandbox mode before live writes.
- Add retry limits and idempotency/duplicate protection for live write APIs.
- Keep parser output canonical; adapters translate from reviewed CCC contracts.
- Require manual approval before live EVA/Sentry submission unless a future ADR explicitly changes this.

## Required Tests For Live Write Adapters

- invalid credential failure;
- expired token failure;
- duplicate payload prevention;
- partial failure recovery;
- operator-visible error;
- audit event creation;
- rollback or retry path.

