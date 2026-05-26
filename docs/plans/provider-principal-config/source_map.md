# Provider Principal Config Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/contracts/provider_principal_config_contract_v1.md`, `docs/reference/data/provider_coverage_matrix.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/28_provider_mapping_assistant.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: parser-extraction, case-workflow-state, operations-quality, governance-security
Expected outputs: source-to-plan traceability for `docs/plans/provider-principal-config/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/provider-principal-config/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/contracts/provider_principal_config_contract_v1.md` | Provider/principal configuration contract. |
| `docs/reference/data/provider_coverage_matrix.md` | Current provider coverage matrix and uncovered principal evidence. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md` | Provider settings and migration work package. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/28_provider_mapping_assistant.md` | Provider mapping assistant plan. |

## Ownership Boundary

Primary ownership:

- provider preset migration and coverage baseline
- principal, garage, alias, routing, contact, and delivery metadata
- provider admin workflow, versioning, activation, rollback, and audit
- provider mapping assistant planning

Explicit exclusions:

- low-level parser extraction algorithms
- finance invoice generation except fee-note metadata source rules
- external partner APIs

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
