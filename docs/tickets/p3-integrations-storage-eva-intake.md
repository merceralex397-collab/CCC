# P3 Integrations, Storage, EVA, And Intake Tickets

## P3-001 Outlook Intake Adapter

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md`, test-context `05_OUTLOOK_INTAKE.md`.
- Dependencies: P1 work item queue, governance review.
- Expected outputs: mailbox ingestion plan, email/source manifest creation, attachment capture, duplicate detection.
- Acceptance criteria: intake creates work items and source files without bypassing parser review.
- Verification: mocked mailbox tests and manual import fallback.
- Archive target: `archive/plans/implemented/`.

## P3-002 Live Box Upload Adapter

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/contracts/storage_adapter_contract_v1.md`, `ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`, `collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md`.
- Dependencies: P1-007, vendor/security review.
- Expected outputs: Box adapter, dry-run mode, duplicate handling, upload status tracking.
- Acceptance criteria: live upload uses the P1 package shape and records storage references/audit events.
- Verification: Box sandbox tests, dry-run package comparison, failure-retry tests.
- Archive target: `archive/plans/implemented/`.

## P3-003 EVA/Sentry Adapter And Import Control

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/research/gptevadeepresearch.md`, `ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md`, `phase7_expanded_markdown_plan/additional_items/08_05_eva_sentry_api_adapter_and_import_control.md`.
- Dependencies: P1-006, API access approval, security review.
- Expected outputs: Sentry/EVA API adapter design, token handling, manual approval gate, duplicate prevention, failure recovery.
- Acceptance criteria: direct submission is never automatic; reviewed exports can be submitted only with explicit operator/reviewer action.
- Verification: sandbox/mock API tests, token-expiry tests, duplicate-payload tests, rejection runbook.
- Archive target: `archive/plans/implemented/`.

## P3-004 CCC-Owned Storage Decision

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/decisions/options/state_store_options.md`, `docs/decisions/options/cloud_document_intelligence_options.md`, `docs/contracts/storage_adapter_contract_v1.md`.
- Dependencies: P1 package generation metrics and governance review.
- Expected outputs: ADR for long-term storage provider and migration plan from Box-only workflow.
- Acceptance criteria: Google Cloud, AWS, and Azure are compared against security, cost, document intelligence, operational fit, and migration risk.
- Verification: ADR accepted with vendor/governance sign-off.
- Archive target: `archive/plans/implemented/`.

