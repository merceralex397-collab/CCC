# Intake Storage Integrations Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/contracts/evidence_package_contract_v1.md`, `docs/contracts/storage_adapter_contract_v1.md`, `docs/contracts/eva_export_contract_v1.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, mcp-and-tooling, governance-security, operations-quality
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/intake-storage-integrations/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/intake-storage-integrations/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/contracts/evidence_package_contract_v1.md` | Evidence package contract including portal/payment metadata. |
| `docs/contracts/storage_adapter_contract_v1.md` | Storage adapter contract. |
| `docs/contracts/eva_export_contract_v1.md` | EVA export contract. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md` | Outlook intake and communications source. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md` | Box storage and files work package. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md` | EVA/Sentry integration work package. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] Outlook/Graph intake and polling fallback | `docs/contracts/evidence_package_contract_v1.md`<br>`docs/contracts/storage_adapter_contract_v1.md`<br>`docs/contracts/eva_export_contract_v1.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md` | `case-workflow-state`, `mcp-and-tooling`, `governance-security`, `operations-quality` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] Box-ready package to live Box adapter path | `docs/contracts/evidence_package_contract_v1.md`<br>`docs/contracts/storage_adapter_contract_v1.md`<br>`docs/contracts/eva_export_contract_v1.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md` | `case-workflow-state`, `mcp-and-tooling`, `governance-security`, `operations-quality` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] EVA JSON export and EVA/Sentry adapter planning | `docs/contracts/evidence_package_contract_v1.md`<br>`docs/contracts/storage_adapter_contract_v1.md`<br>`docs/contracts/eva_export_contract_v1.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md` | `case-workflow-state`, `mcp-and-tooling`, `governance-security`, `operations-quality` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] website, WhatsApp, payment, Box, and local-folder metadata boundaries | `docs/contracts/evidence_package_contract_v1.md`<br>`docs/contracts/storage_adapter_contract_v1.md`<br>`docs/contracts/eva_export_contract_v1.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md` | `case-workflow-state`, `mcp-and-tooling`, `governance-security`, `operations-quality` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] job-sheet/spreadsheet transition bridge planning | `docs/contracts/evidence_package_contract_v1.md`<br>`docs/contracts/storage_adapter_contract_v1.md`<br>`docs/contracts/eva_export_contract_v1.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md` | `case-workflow-state`, `mcp-and-tooling`, `governance-security`, `operations-quality` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S1

- [ ] Own EVA JSON export and Box-ready package adapter boundaries with Operational Core coordination.

### S3

- [ ] Plan Outlook intake, live Box upload, EVA/Sentry submission control, and spreadsheet bridge with sandbox tests.

### S5

- [ ] Feed portal/API and payment automation evidence to external-platform-partners and finance-billing option papers.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `case-workflow-state` | Work-item state, review status, blockers, audit events, and approvals are the operational source of truth. |
| `mcp-and-tooling` | MCP/tool exposure must wrap approved adapters with schemas, auth, audit, rate limits, and gateway controls. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `operations-quality` | Release, rollback, regression, monitoring, runbooks, pilot, support, and decommissioning gates must be explicit. |

## Non-Overlap Rules

The workspace explicitly does not own:

- external customer portal product scope
- payment automation itself
- MCP wrappers when the issue is tool exposure rather than adapter behavior

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
