# P1 Operational Core MVP Tickets — Redirected

> **This file is a tombstone/redirect.** Tickets have been relocated to their owning workspaces as part of the docs/plans workspace expansion (2026-05-24). This file is preserved so that scaffold verifier path checks continue to pass.

- Status: redirected.
- Owner: unassigned.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P0 foundation.
- Expected outputs: see new workspace ticket files below.
- Acceptance criteria: all P1 tickets exist in their owning workspace.
- Verification required: scaffold verifier path checks pass.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: see new workspace paths below.

## Ticket Relocation Map

| Ticket | New Location |
| --- | --- |
| P1-001 Parser Core MVP | `docs/plans/parser-extraction/tickets/p1-parser-core-mvp.md` |
| P1-002 Staff Parser UI | `docs/plans/user-experience-interfaces/tickets/p1-staff-parser-ui.md` |
| P1-003 Parser CLI Parity | `docs/plans/parser-extraction/tickets/p1-parser-cli-parity.md` |
| P1-004 Provider Principal Admin UI | `docs/plans/provider-principal-config/tickets/p1-provider-principal-admin-ui.md` |
| P1-005 Work Item And Review Queue | `docs/plans/case-workflow-state/tickets/p1-work-item-review-queue.md` |
| P1-006 EVA JSON Export | `docs/plans/intake-storage-integrations/tickets/p1-eva-json-export.md` |
| P1-007 Box-Ready Evidence Package | `docs/plans/intake-storage-integrations/tickets/p1-box-ready-evidence-package.md` |

## P1-001 Parser Core MVP

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/plans/operational-core/parser-mvp/plan.md`, `docs/research/siderpdf.md`, `ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P0-002, P0-003, P0-004.
- Expected outputs: parser core, extraction adapters, provider detection, mapping rule engine, canonical parser result output.
- Acceptance criteria: deterministic parser handles PDF, DOCX, DOC, MSG/EML, images, and batch folders; output includes provenance/confidence/warnings; legacy behaviours are captured by golden tests.
- Verification required: private corpus golden tests for all 26 provider presets; parser result schema validation; failure cases produce reviewable warnings.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.

## P1-002 Staff Parser UI

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/architecture/parser_ui_cli.md`, `docs/decisions/options/ui_platform_options.md`, test-context UI/dashboard specs.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P1-001, state-store decision or temporary local state.
- Expected outputs: upload/batch UI, source preview, field review/correction, warning review, image ordering, EVA preview/export, package generation trigger.
- Acceptance criteria: non-technical staff can complete the first success workflow in `docs/architecture/mvp_interlock.md` without terminal use.
- Verification required: user walkthrough against private corpus sample set; UI/CLI parity checklist.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.

## P1-003 Parser CLI Parity

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/architecture/parser_ui_cli.md`, `docs/plans/operational-core/parser-mvp/plan.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P1-001.
- Expected outputs: CLI commands for parse, validate, export EVA JSON, package evidence, batch runs, and machine-readable warnings.
- Acceptance criteria: CLI uses same parser core and validation/export services as UI.
- Verification required: parity tests compare UI service calls and CLI output for the same fixture set.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.

## P1-004 Provider Principal Admin UI

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/contracts/provider_principal_config_contract_v1.md`, `ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`, `phase7_expanded_markdown_plan/additional_items/08_02_provider_principal_configuration_library.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P0-003, P0-006, state-store decision.
- Expected outputs: provider/principal admin screens, versioning, activation/rollback, alias management, detection phrase and rule editing, plus optional provider routing metadata controls for `delivery_channel`, `query_owner`, `reply_to_handler`, `reply_all`, `cc_list`, `fee_note_handling`, `garage_figures_rule`, `missing_info_chase_limit`, and `special_case_notes`.
- Acceptance criteria: provider-admin role can create draft config, validate against corpus examples, activate, and roll back with audit events; optional routing metadata and fee-note exceptions for `QDOS`, `QCL`, `AX`, `FW`, `OAK`, and `ALS` can be recorded without making them parser-required or authorizing portal/payment/WhatsApp automation in P1.
- Verification required: provider config regression checks, audit event assertions, and schema/UI checks confirming the optional routing metadata fields and fee-note exceptions are supported.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.

## P1-005 Work Item And Review Queue

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/contracts/work_item_contract_v1.md`, `docs/contracts/review_audit_event_contract_v1.md`, `phase7_expanded_markdown_plan/additional_items/08_04_human_review_queue_and_exception_sla.md`, `docs/plans/operational-core/archived_plans/implemented/2026-05-23-implemented-figmaplan.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: state-store decision, P1-001.
- Expected outputs: work item lifecycle, missing-info states, review/correction workflow, audit event persistence, and optional metadata capture for source channel, Box/local folder references, and current payment/portal evidence.
- Acceptance criteria: staff can move cases through draft, missing evidence/instruction, parsed, in review, ready for export, exported, packaged, blocked, archived; work items can record `source_channel`, `source_category`, `source_labels`, `portal_submission_id`, `payment_status`, `payment_chaser_sent`, `box_folder_url`, `box_folder_stage`, `local_network_folder_url`, and `closed_file_reason` without making those fields parser-required or authorizing portal/payment/WhatsApp automation in P1.
- Verification required: lifecycle tests, correction/audit tests, blocked-state tests, and schema checks confirming the full optional metadata field set is accepted but not required.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.

## P1-006 EVA JSON Export

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/contracts/eva_export_contract_v1.md`, `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json`, `docs/research/gptevadeepresearch.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P1-001, P1-005.
- Expected outputs: EVA-ready JSON export adapter and validation gate.
- Acceptance criteria: field order matches final-format example; required provider, dates as `DD/MM/YYYY`, inspection address/image-based marker, mileage/VAT/unit constraints, and warning gates are enforced.
- Verification required: golden export tests, field-order assertion, invalid-export tests.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.

## P1-007 Box-Ready Evidence Package Generation

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/contracts/evidence_package_contract_v1.md`, `docs/contracts/storage_adapter_contract_v1.md`, `ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`, `docs/plans/operational-core/archived_plans/implemented/2026-05-23-implemented-figmaplan.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P1-005, P1-006.
- Expected outputs: local package folder and manifest, with support for current website repair-estimate evidence such as uploaded images, `Invoice.pdf`, `Summary.txt`, source form data, and Box references when that intake channel is the source.
- Acceptance criteria: package includes originals, original email when available, images, EVA JSON when generated, companion report when available, notes, checksums, image preview ordering decision, and optional website/Box metadata where relevant; P1 does not add autonomous external sends or payment processing.
- Verification required: package manifest tests, image order tests, checksum tests, and fixture coverage for portal-originated package metadata.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.
