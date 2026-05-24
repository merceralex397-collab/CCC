# Intake Storage Integrations Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/contracts/evidence_package_contract_v1.md`, `docs/contracts/storage_adapter_contract_v1.md`, `docs/contracts/eva_export_contract_v1.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, mcp-and-tooling, governance-security, operations-quality
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/intake-storage-integrations/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Intake channels, source capture, storage adapters, EVA/Sentry adapters, and transitional spreadsheet bridge planning.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- Outlook/Graph intake and polling fallback
- Box-ready package to live Box adapter path
- EVA JSON export and EVA/Sentry adapter planning
- website, WhatsApp, payment, Box, and local-folder metadata boundaries
- job-sheet/spreadsheet transition bridge planning

## Does Not Own

- external customer portal product scope
- payment automation itself
- MCP wrappers when the issue is tool exposure rather than adapter behavior

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/contracts/evidence_package_contract_v1.md` | Evidence package contract including portal/payment metadata. |
| `docs/contracts/storage_adapter_contract_v1.md` | Storage adapter contract. |
| `docs/contracts/eva_export_contract_v1.md` | EVA export contract. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md` | Outlook intake and communications source. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md` | Box storage and files work package. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md` | EVA/Sentry integration work package. |

## Cross-Workspace Dependencies

- case-workflow-state
- mcp-and-tooling
- governance-security
- operations-quality

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
