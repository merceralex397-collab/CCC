# P0 Foundation Tickets — Redirected

> **This file is a tombstone/redirect.** Tickets have been relocated to their owning workspaces as part of the docs/plans workspace expansion (2026-05-24). This file is preserved so that scaffold verifier path checks continue to pass.

- Status: redirected.
- Owner: unassigned.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`.
- Roadmap milestone: P0 Foundation.
- Dependencies: none.
- Expected outputs: see new workspace ticket files below.
- Acceptance criteria: all P0 tickets exist in their owning workspace.
- Verification required: scaffold verifier path checks pass.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/` when all P0 work is done.
- Supersedes: none.
- Superseded-by: see new workspace paths below.

## Ticket Relocation Map

| Ticket | New Location |
| --- | --- |
| P0-001 Source Synthesis And Canonical Promotion | Remains in `docs/plans/operational-core/` — cross-workspace coordination. |
| P0-002 Contracts Baseline | Remains in `docs/plans/operational-core/` — cross-workspace coordination. |
| P0-003 Provider Coverage And Migration Baseline | `docs/plans/parser-extraction/tickets/p0-provider-coverage-migration-baseline.md` |
| P0-004 Parser MVP Implementation Plan | `docs/plans/parser-extraction/tickets/p0-parser-mvp-implementation-plan.md` |
| P0-005 Governance, Security, Operations Baseline | `docs/plans/governance-security/` (option-paper first, then ticket). |
| P0-006 ADR And Option Paper Baseline | `docs/plans/operational-core/` — cross-workspace ADR coordination. |

## P0-001 Source Synthesis And Canonical Promotion

- Status: active.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/reference/originalplanning/`, `docs/research/*.md`, `docs/reference/test-context/testprojectcontext/`.
- Roadmap milestone: P0 Foundation.
- Dependencies: none.
- Expected outputs: `docs/plans/operational-core/source_synthesis.md`, promoted phase backlog, all-ideas ledger, superseded list.
- Acceptance criteria: every generated pack and research document is referenced; every promoted idea has a phase or is merged into a canonical doc; no generated pack remains an implicit active plan.
- Verification required: scaffold verifier checks generated pack and research references.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/` when implemented.
- Supersedes: none.
- Superseded-by: none.

## P0-002 Contracts Baseline

- Status: active.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `ce_system_plans_enhanced/05_WORK_PACKAGE_DATA_MODEL_AND_WORKFLOW.md`, `phase7_expanded_markdown_plan/additional_items/08_01_work_item_state_store_and_job_sheet_replacement.md`, `08_04_human_review_queue_and_exception_sla.md`.
- Roadmap milestone: P0 Foundation.
- Dependencies: P0-001.
- Expected outputs: work item, provider/principal config, parser result, review/audit event, evidence package, EVA export, storage adapter, and extraction adapter contracts.
- Acceptance criteria: each contract has required identity fields, lifecycle/gate rules, audit requirements, and source references.
- Verification required: required contract files exist and contain versioned headings.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.
## P0-003 Provider Coverage And Migration Baseline

- Status: active.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json`, `docs/reference/data/provider_coverage_matrix.md`, `ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`.
- Roadmap milestone: P0 Foundation.
- Dependencies: P0-002.
- Expected outputs: provider coverage matrix, provider config contract, migration notes for 26 presets and uncovered job-sheet principals.
- Acceptance criteria: all 26 presets listed; `ACSP`, `OAK/AX`, `PRINCIPAL`, and `WOODLANDS` are tracked as uncovered/job-sheet anomalies; provider admin requirements are captured for P1.
- Verification required: scaffold verifier checks 26 provider presets and uncovered principal evidence.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.

## P0-004 Parser MVP Implementation Plan

- Status: active.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/research/siderpdf.md`, `docs/research/gptdeepresearch.md`, `cedocumentmapper_rebuild_plan_pack_all_zips/`, `docs/reference/raw/collisionrelateddocs/claudechat.md`.
- Roadmap milestone: P0 Foundation.
- Dependencies: P0-002, P0-003.
- Expected outputs: `docs/plans/operational-core/parser-mvp/plan.md`.
- Acceptance criteria: plan covers PDF, DOCX, DOC, MSG/EML, images, batches, all 26 provider presets, UI/CLI parity, deterministic-first extraction, EVA export gates, image package rules, private corpus tests, and known legacy behaviours.
- Verification required: scaffold verifier checks parser-plan coverage terms and provider list.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/` after parser MVP is implemented and plan is marked implemented.
- Supersedes: none.
- Superseded-by: none.

## P0-005 Governance, Security, Operations Baseline

- Status: active.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md`, `08_12_security_dpia_and_vendor_governance.md`, `ce_phase4_agents_reviewed_plan/10_security_governance_audit.md`.
- Roadmap milestone: P0 Foundation.
- Dependencies: P0-001.
- Expected outputs: governance/security architecture doc, data map, DPIA/vendor governance placeholder, API security standard, release/rollback doc, monitoring/runbook docs.
- Acceptance criteria: roles, audit identity, vendor/cloud review, retention placeholders, release rollback, and runbook placeholders exist.
- Verification required: required security/operations docs exist and mention no personal injury or KADOE scope.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.

## P0-006 ADR And Option Paper Baseline

- Status: active.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `ce_phase4_agents_reviewed_plan/12_open_questions_decision_log.md`, `docs/architecture/parser_ui_cli.md`, research docs.
- Roadmap milestone: P0 Foundation.
- Dependencies: P0-001.
- Expected outputs: ADRs for locked decisions and option papers for UI, backend, state store, and cloud document intelligence.
- Acceptance criteria: locked decisions are recorded as accepted ADRs; unresolved decisions have comparison matrices and required follow-up.
- Verification required: scaffold verifier checks ADR and option files exist.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.
