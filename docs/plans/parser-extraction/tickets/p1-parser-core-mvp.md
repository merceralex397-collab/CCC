# P1-001 Parser Core MVP

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/research/siderpdf.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P0-002, P0-003, P0-004.
- Expected outputs: parser core, extraction adapters, provider detection, mapping rule engine, canonical parser result output.
- Acceptance criteria: deterministic parser handles PDF, DOCX, DOC, MSG/EML, images, and batch folders; output includes provenance/confidence/warnings; legacy behaviours are captured by golden tests.
- Verification required: private corpus golden tests for all 26 provider presets; parser result schema validation; failure cases produce reviewable warnings.
- Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p1-operational-core-mvp.md` § P1-001.
- Superseded-by: none.
