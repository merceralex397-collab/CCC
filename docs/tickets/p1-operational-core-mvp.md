# P1 Operational Core MVP Tickets

## P1-001 Parser Core MVP

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/plans/parser_mvp_implementation_plan.md`, `docs/research/siderpdf.md`, `ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`.
- Dependencies: P0-002, P0-003, P0-004.
- Expected outputs: parser core, extraction adapters, provider detection, mapping rule engine, canonical parser result output.
- Acceptance criteria: deterministic parser handles PDF, DOCX, DOC, MSG/EML, images, and batch folders; output includes provenance/confidence/warnings; legacy behaviours are captured by golden tests.
- Verification: private corpus golden tests for all 26 provider presets; parser result schema validation; failure cases produce reviewable warnings.
- Archive target: `archive/plans/implemented/`.

## P1-002 Staff Parser UI

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/architecture/parser_ui_cli.md`, `docs/decisions/options/ui_platform_options.md`, test-context UI/dashboard specs.
- Dependencies: P1-001, state-store decision or temporary local state.
- Expected outputs: upload/batch UI, source preview, field review/correction, warning review, image ordering, EVA preview/export, package generation trigger.
- Acceptance criteria: non-technical staff can complete the first success workflow in `docs/architecture/mvp_interlock.md` without terminal use.
- Verification: user walkthrough against private corpus sample set; UI/CLI parity checklist.
- Archive target: `archive/plans/implemented/`.

## P1-003 Parser CLI Parity

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/architecture/parser_ui_cli.md`, `docs/plans/parser_mvp_implementation_plan.md`.
- Dependencies: P1-001.
- Expected outputs: CLI commands for parse, validate, export EVA JSON, package evidence, batch runs, and machine-readable warnings.
- Acceptance criteria: CLI uses same parser core and validation/export services as UI.
- Verification: parity tests compare UI service calls and CLI output for the same fixture set.
- Archive target: `archive/plans/implemented/`.

## P1-004 Provider Principal Admin UI

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/contracts/provider_principal_config_contract_v1.md`, `ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`, `phase7_expanded_markdown_plan/additional_items/08_02_provider_principal_configuration_library.md`.
- Dependencies: P0-003, P0-006, state-store decision.
- Expected outputs: provider/principal admin screens, versioning, activation/rollback, alias management, detection phrase and rule editing.
- Acceptance criteria: provider-admin role can create draft config, validate against corpus examples, activate, and roll back with audit events.
- Verification: provider config regression checks and audit event assertions.
- Archive target: `archive/plans/implemented/`.

## P1-005 Work Item And Review Queue

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/contracts/work_item_contract_v1.md`, `docs/contracts/review_audit_event_contract_v1.md`, `phase7_expanded_markdown_plan/additional_items/08_04_human_review_queue_and_exception_sla.md`.
- Dependencies: state-store decision, P1-001.
- Expected outputs: work item lifecycle, missing-info states, review/correction workflow, audit event persistence.
- Acceptance criteria: staff can move cases through draft, missing evidence/instruction, parsed, in review, ready for export, exported, packaged, blocked, archived.
- Verification: lifecycle tests, correction/audit tests, blocked-state tests.
- Archive target: `archive/plans/implemented/`.

## P1-006 EVA JSON Export

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/contracts/eva_export_contract_v1.md`, `collisionrelateddocs/Final Format Example 02.json`, `docs/research/gptevadeepresearch.md`.
- Dependencies: P1-001, P1-005.
- Expected outputs: EVA-ready JSON export adapter and validation gate.
- Acceptance criteria: field order matches final-format example; required provider, dates as `DD/MM/YYYY`, inspection address/image-based marker, mileage/VAT/unit constraints, and warning gates are enforced.
- Verification: golden export tests, field-order assertion, invalid-export tests.
- Archive target: `archive/plans/implemented/`.

## P1-007 Box-Ready Evidence Package Generation

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `docs/contracts/evidence_package_contract_v1.md`, `docs/contracts/storage_adapter_contract_v1.md`, `ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`.
- Dependencies: P1-005, P1-006.
- Expected outputs: local package folder and manifest.
- Acceptance criteria: package includes originals, original email when available, images, EVA JSON when generated, companion report when available, notes, checksums, and image preview ordering decision.
- Verification: package manifest tests; image order tests; checksum tests.
- Archive target: `archive/plans/implemented/`.

