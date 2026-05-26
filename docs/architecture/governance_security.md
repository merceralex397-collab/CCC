# Governance And Security

CCC handles private operational files and vehicle damage evidence. Governance must be built into the earliest parser and Operational Core work rather than added after automation is introduced.

## Scope And Data Handling

- CCC is for vehicle damage instruction processing and related evidence handling.
- Personal injury and KADOE are out of scope.
- Raw source files are immutable evidence. Do not rewrite, normalize in place, or delete originals.
- Normalized Markdown companions are for search and planning. They do not replace source files.
- Generated plan packs are not operational truth until promoted into canonical docs or tickets.
- Private real corpus tests are the source of truth for parser parity. Redacted public fixtures can be added later but must not weaken private-corpus coverage.

## Identity And Roles

The first auth model is named local app accounts with roles and audit identity. Shared Outlook mailbox identities must not be used as staff audit identities.

| Role | Allowed |
| --- | --- |
| Viewer | Read work items, parser results, package manifests, and audit history. |
| Operator | Upload files, run parser, correct fields, build packages, export EVA JSON. |
| Reviewer | Approve manual corrections, resolve warnings, release package/export gates. |
| Provider Admin | Edit provider/principal configuration, aliases, mapping rules, activation and rollback. |
| Admin | Manage users, roles, environment settings, and audit retention. |

## Audit Events

Audit events must record:

- actor account and role;
- timestamp;
- work item id;
- source file or config id where applicable;
- action name;
- before/after value for manual corrections or configuration changes;
- parser result id or provider config version;
- reason/comment when a warning is overridden.

## Vendor And Cloud Controls

Cloud OCR/document intelligence, Box AI/Extract, valuation services, DVLA/DVSA APIs, and future Sentry/EVA adapters must be introduced through explicit integration tickets and option/ADR updates. Before activation, each must have:

- data classification review;
- retention and deletion model;
- access control model;
- cost and rate-limit review;
- provenance mapping into CCC contracts;
- feature flag and fallback behaviour;
- test evidence using private corpus samples where legally permitted.

## Storage Controls

Box-ready package generation is the first storage deliverable. Live Box upload and CCC-owned storage on Google Cloud, AWS, or Azure are later adapters. Storage adapters must preserve:

- original files;
- generated EVA JSON;
- images in required order;
- companion report when present;
- package manifest;
- checksums;
- audit/export metadata.

## Documentation Hygiene

Plans and tickets are active only while implementation is pending. When implemented, move the plan or ticket to an archive folder and add a status block at the top confirming it has been implemented, the implementation date, and the canonical replacement docs or code paths.

