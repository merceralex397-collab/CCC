# Provider Principal Config Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/contracts/provider_principal_config_contract_v1.md`, `docs/reference/data/provider_coverage_matrix.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/28_provider_mapping_assistant.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: parser-extraction, case-workflow-state, operations-quality, governance-security
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/provider-principal-config/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/provider-principal-config/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/provider-principal-config/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/contracts/provider_principal_config_contract_v1.md` | Provider/principal configuration contract. |
| `docs/reference/data/provider_coverage_matrix.md` | Current provider coverage matrix and uncovered principal evidence. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md` | Provider settings and migration work package. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/28_provider_mapping_assistant.md` | Provider mapping assistant plan. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] provider preset migration and coverage baseline | `docs/contracts/provider_principal_config_contract_v1.md`<br>`docs/reference/data/provider_coverage_matrix.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/28_provider_mapping_assistant.md` | `parser-extraction`, `case-workflow-state`, `operations-quality`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] principal, garage, alias, routing, contact, and delivery metadata | `docs/contracts/provider_principal_config_contract_v1.md`<br>`docs/reference/data/provider_coverage_matrix.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/28_provider_mapping_assistant.md` | `parser-extraction`, `case-workflow-state`, `operations-quality`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] provider admin workflow, versioning, activation, rollback, and audit | `docs/contracts/provider_principal_config_contract_v1.md`<br>`docs/reference/data/provider_coverage_matrix.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/28_provider_mapping_assistant.md` | `parser-extraction`, `case-workflow-state`, `operations-quality`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] provider mapping assistant planning | `docs/contracts/provider_principal_config_contract_v1.md`<br>`docs/reference/data/provider_coverage_matrix.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/28_provider_mapping_assistant.md` | `parser-extraction`, `case-workflow-state`, `operations-quality`, `governance-security` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S1

- [ ] Move provider coverage and provider-admin tickets here; preserve all 26 current presets and uncovered-principal triage.

### S2

- [ ] Add regression-backed provider activation, rollback, principal/garage migration, and composite mapping rules.

### S4

- [ ] Add provider mapping assistant as a governed staff skill/tool with approval and backup controls.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `parser-extraction` | Extraction work must preserve CE Document Mapper behavior, deterministic rules, canonical schema, and regression coverage. |
| `case-workflow-state` | Work-item state, review status, blockers, audit events, and approvals are the operational source of truth. |
| `operations-quality` | Release, rollback, regression, monitoring, runbooks, pilot, support, and decommissioning gates must be explicit. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |

## Non-Overlap Rules

The workspace explicitly does not own:

- low-level parser extraction algorithms
- finance invoice generation except fee-note metadata source rules
- external partner APIs

If a proposed ticket touches one of those exclusions, link to the owning workspace and keep this workspace as a supporting dependency only.

## Source Ownership Rules

- Cite the source paths above in every promoted ticket, option paper, or roadmap change.
- Use `source_map.md` to explain how the evidence supports the workspace boundary.
- Keep generated and historical planning packs reference-only until a scoped ticket or option paper promotes them.
- Do not edit raw evidence under `docs/reference/raw/collisionrelateddocs/`; create derivatives only under documented derivative paths.

## Promotion Gates

- Use `tickets/` for implementation-ready work with acceptance criteria and verification.
- Use `option-papers/` before vendor, privacy, external access, autonomous send, payment automation, AI/RAG, cloud OCR/document intelligence, commercial data, or partner/API work.
- Link governance/security approval where privacy, vendor, retention, licensing, expert-boundary, API security, or autonomous-action risk exists.
- Link operations-quality approval where release, rollback, regression, monitoring, runbook, support, pilot, or decommissioning evidence is needed.
