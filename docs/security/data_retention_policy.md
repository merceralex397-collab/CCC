# Data Retention Policy

Date: 2026-05-29
Status: DRAFT — placeholder periods; requires business/DPO sign-off
Owner: unassigned
Source links: `docs/security/data_map.md`, `docs/security/dpia_vendor_governance.md`, `docs/architecture/governance_security.md`

## Purpose

Define retention, deletion, and legal-hold handling for CCC data categories. UK GDPR principles apply: data minimisation and **storage limitation** (keep only as long as needed for the purpose), with legal-hold override. **Retention periods below are placeholders to confirm with the business/DPO** — collision-assessment + expert-evidence records can have long statutory/limitation-driven retention needs, which a legal decision must set.

## Principles

- Raw source files are immutable evidence; deletion is governed, never in-place edits.
- Keep reviewed canonical data + audit; minimise raw PII held beyond purpose.
- Secrets/credentials never committed; rotated on exposure.
- Legal hold overrides scheduled deletion.

## Retention By Category (placeholders — confirm)

| Category | Proposed retention | Notes |
| --- | --- | --- |
| Instruction files (raw) | [confirm — likely long, tied to case/limitation period] | Immutable evidence. |
| Email records (MSG/EML) | [confirm] | Source preservation; never delete source mail in intake. |
| Vehicle details / parser result | [confirm — case lifetime + limitation] | Canonical case data. |
| Evidence images | [confirm] | Package + EVA evidence. |
| Provider/principal config | retain while active + version history | Audit of activation/rollback. |
| Review/audit events | retain ≥ case retention (append-only) | Accountability; do not purge before the case. |
| Package/export metadata | [confirm — with case] | Checksums + storage status. |
| Integration credentials/secrets | not retained in repo; rotate on exposure | Secret store only. |
| AI run logs (`ai-platform`) | [confirm — short/medium] | For audit/regression; redact PII; storage-limited. |
| Vehicle/MOT/market evidence store (`intelligence/vehicle`) | [confirm — licensing-bound] | Licensing terms may cap storage/reuse. |
| Historical search index (`casework`) | [confirm] | Built from retained case data; respects category retention. |
| Analytics (`business/analytics`) | aggregate/derived; [confirm raw vs aggregate] | Reviewed-canonical-data only; no ungoverned warehouse. |

## Deletion + Legal Hold

- Scheduled deletion at end of retention, with audit of the deletion event.
- Legal hold flag suspends deletion for named cases.
- Deletion cascades to derivatives (normalized companions, packages, search index entries) per category.

## Open Items For Sign-Off

Confirm every period with the business/DPO (statutory + limitation periods for collision/expert-evidence work); confirm whether DVLA/DVSA/market licensing caps evidence-store retention; confirm AI-run-log retention; confirm deletion cascade scope.
