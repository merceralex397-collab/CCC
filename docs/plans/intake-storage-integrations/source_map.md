# Intake Storage Integrations Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/contracts/evidence_package_contract_v1.md`, `docs/contracts/storage_adapter_contract_v1.md`, `docs/contracts/eva_export_contract_v1.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, mcp-and-tooling, governance-security, operations-quality
Expected outputs: source-to-plan traceability for `docs/plans/intake-storage-integrations/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/contracts/evidence_package_contract_v1.md` | Evidence package contract including portal/payment metadata. |
| `docs/contracts/storage_adapter_contract_v1.md` | Storage adapter contract. |
| `docs/contracts/eva_export_contract_v1.md` | EVA export contract. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md` | Outlook intake and communications source. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md` | Box storage and files work package. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md` | EVA/Sentry integration work package. |

## Ownership Boundary

Primary ownership:

- Outlook/Graph intake and polling fallback
- Box-ready package to live Box adapter path
- EVA JSON export and EVA/Sentry adapter planning
- website, WhatsApp, payment, Box, and local-folder metadata boundaries
- job-sheet/spreadsheet transition bridge planning

Explicit exclusions:

- external customer portal product scope
- payment automation itself
- MCP wrappers when the issue is tool exposure rather than adapter behavior

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
