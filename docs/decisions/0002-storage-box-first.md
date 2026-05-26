# ADR 0002: Box First, Storage Adapter Always

- Status: accepted
- Date: 2026-05-23

## Decision

Plan Box as the first evidence-storage integration, but put all storage behavior behind an adapter contract.

## Rationale

Collision Engineers currently categorize case evidence in Box by case/PO number. Future CCC-owned storage may move to Google Cloud, AWS, or Azure, so parser/export logic must not depend on Box SDK details.

## Consequences

- Box metadata and folder conventions are documented early.
- Future storage selection remains an architecture decision.
- Cloud OCR/document intelligence requires privacy and vendor review.
