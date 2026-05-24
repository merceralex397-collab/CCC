# Provider Principal Config Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/contracts/provider_principal_config_contract_v1.md`, `docs/reference/data/provider_coverage_matrix.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/28_provider_mapping_assistant.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: parser-extraction, case-workflow-state, operations-quality, governance-security
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/provider-principal-config/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/provider-principal-config/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Provider, principal, garage, routing, and provider-rule lifecycle planning.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- provider preset migration and coverage baseline
- principal, garage, alias, routing, contact, and delivery metadata
- provider admin workflow, versioning, activation, rollback, and audit
- provider mapping assistant planning

## Does Not Own

- low-level parser extraction algorithms
- finance invoice generation except fee-note metadata source rules
- external partner APIs

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/contracts/provider_principal_config_contract_v1.md` | Provider/principal configuration contract. |
| `docs/reference/data/provider_coverage_matrix.md` | Current provider coverage matrix and uncovered principal evidence. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md` | Provider settings and migration work package. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/28_provider_mapping_assistant.md` | Provider mapping assistant plan. |

## Cross-Workspace Dependencies

- parser-extraction
- case-workflow-state
- operations-quality
- governance-security

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
