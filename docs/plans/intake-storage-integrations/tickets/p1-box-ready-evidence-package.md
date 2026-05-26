# P1-007 Box-Ready Evidence Package Generation

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/contracts/evidence_package_contract_v1.md`, `docs/contracts/storage_adapter_contract_v1.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`, `docs/plans/operational-core/archived_plans/implemented/2026-05-23-implemented-figmaplan.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P1-005 (Work Item And Review Queue), P1-006 (EVA JSON Export).
- Expected outputs: local package folder and manifest, with support for current website repair-estimate evidence such as uploaded images, `Invoice.pdf`, `Summary.txt`, source form data, and Box references when that intake channel is the source.
- Acceptance criteria: package includes originals, original email when available, images, EVA JSON when generated, companion report when available, notes, checksums, image preview ordering decision, and optional website/Box metadata where relevant; P1 does not add autonomous external sends or payment processing.
- Verification required: package manifest tests, image order tests, checksum tests, and fixture coverage for portal-originated package metadata.
- Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p1-operational-core-mvp.md` § P1-007.
- Superseded-by: none.

## Context

Image ordering rule from `claudechat.md`: two preview images followed by all images including the previews again. Legacy network-share storage is documented in `handover.docx`; treat that as source evidence rather than an active path dependency. P1 generates local packages only — live Box upload is P3.
