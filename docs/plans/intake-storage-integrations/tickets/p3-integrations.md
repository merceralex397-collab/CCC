# P3 Intake And Storage Integration Tickets

## P3-001 Outlook Intake Adapter

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/reference/originalplanning/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md`, `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/05_OUTLOOK_INTAKE.md`, `docs/plans/operational-core/archived_plans/implemented/2026-05-23-implemented-figmaplan.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`.
- Roadmap milestone: P3 Integrations Storage EVA Intake.
- Dependencies: P1 work item queue, governance review.
- Expected outputs: mailbox ingestion plan, email/source manifest creation, attachment capture, duplicate detection, and mapping into shared work-item source metadata.
- Acceptance criteria: intake creates work items and source files without bypassing parser review; source labels/categories distinguish instruction, image-only, and query flows; `digital@collisionengineers.co.uk` delegated access to `desk@`, `engineers@`, `info@` is the documented mailbox scope.
- Verification required: mocked mailbox tests, source-label mapping tests, and manual import fallback.
- Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p3-integrations-storage-eva-intake.md` § P3-001.
- Superseded-by: none.

## P3-002 Live Box Upload Adapter

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/contracts/storage_adapter_contract_v1.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md`, `docs/plans/operational-core/archived_plans/implemented/2026-05-23-implemented-figmaplan.md`.
- Roadmap milestone: P3 Integrations Storage EVA Intake.
- Dependencies: P1-007 (Box-Ready Evidence Package), vendor/security review.
- Expected outputs: Box adapter, dry-run mode, duplicate handling, upload status tracking, and metadata for Box folder URL/stage plus `Closed Files` backup references.
- Acceptance criteria: live upload uses the P1 package shape and records storage references/audit events without changing the Box-first package-only rule for P1.
- Verification required: Box sandbox tests, dry-run package comparison, failure-retry tests, and metadata assertions for folder/stage/archive references.
- Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p3-integrations-storage-eva-intake.md` § P3-002.
- Superseded-by: none.

## P3-003 Website/Payment Intake Boundary

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/plans/operational-core/archived_plans/implemented/2026-05-23-implemented-figmaplan.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/evidence_package_contract_v1.md`.
- Roadmap milestone: P3 Integrations Storage EVA Intake.
- Dependencies: P1-005, P1-007, governance review.
- Expected outputs: intake boundary definition for website submission metadata, payment status, explicit `payment_chaser_sent` metadata, and Box/package references.
- Acceptance criteria: current website/payment evidence can be recorded on work items and packages, including the `payment_chaser_sent` field, but portal/payment automation, checkout ownership, and autonomous chasers remain out of P3 implementation until separately approved.
- Verification required: contract review, fixture-based metadata tests including `payment_chaser_sent`, and explicit scope notes in integration docs.
- Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p3-integrations-storage-eva-intake.md` § P3-003.
- Superseded-by: none.

## P3-004 EVA/Sentry Adapter And Import Control

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/research/gptevadeepresearch.md`, `docs/reference/normalized/collisionrelateddocs__collision_releated__sentry_api_complete_guide.md.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_05_eva_sentry_api_adapter_and_import_control.md`.
- Roadmap milestone: P3 Integrations Storage EVA Intake.
- Dependencies: P1-006 (EVA JSON Export), API access approval, security review.
- Expected outputs: Sentry/EVA API adapter design, token handling, manual approval gate, duplicate prevention, failure recovery.
- Acceptance criteria: direct submission is never automatic; reviewed exports can be submitted only with explicit operator/reviewer action; JWT tokens are handled with 5-minute expiry; no public OpenAPI schema means field contract is from `Final Format Example 02.json`.
- Verification required: sandbox/mock API tests, token-expiry tests, duplicate-payload tests, rejection runbook.
- Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p3-integrations-storage-eva-intake.md` § P3-004.
- Superseded-by: none.

## P3-005 CCC-Owned Storage Decision

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/decisions/options/state_store_options.md`, `docs/decisions/options/cloud_document_intelligence_options.md`, `docs/contracts/storage_adapter_contract_v1.md`.
- Roadmap milestone: P3 Integrations Storage EVA Intake.
- Dependencies: P1 package generation metrics and governance review.
- Expected outputs: ADR for long-term storage provider and migration plan from Box-only workflow.
- Acceptance criteria: Google Cloud, AWS, and Azure are compared against security, cost, document intelligence, operational fit, and migration risk.
- Verification required: ADR accepted with vendor/governance sign-off.
- Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/` or `archived_plans/superseded/`.
- Supersedes: `docs/plans/operational-core/tickets/p3-integrations-storage-eva-intake.md` § P3-005.
- Superseded-by: none.
