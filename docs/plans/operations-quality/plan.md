# Operations Quality Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/operations/monitoring_runbooks.md`, `docs/operations/release_and_rollback.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: parser-extraction, intake-storage-integrations, governance-security, unified-platform
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/operations-quality/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/operations-quality/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/operations-quality/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/operations/monitoring_runbooks.md` | Current monitoring and runbooks baseline. |
| `docs/operations/release_and_rollback.md` | Current release and rollback baseline. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md` | Test corpus and regression harness plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md` | Monitoring, runbooks, and release management plan. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md` | Security, testing, rollout, and decommissioning plan. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] test corpus and regression harness planning | `docs/operations/monitoring_runbooks.md`<br>`docs/operations/release_and_rollback.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md` | `parser-extraction`, `intake-storage-integrations`, `governance-security`, `unified-platform` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] release and rollback process | `docs/operations/monitoring_runbooks.md`<br>`docs/operations/release_and_rollback.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md` | `parser-extraction`, `intake-storage-integrations`, `governance-security`, `unified-platform` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] monitoring, runbooks, alerts, incident/failure playbooks | `docs/operations/monitoring_runbooks.md`<br>`docs/operations/release_and_rollback.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md` | `parser-extraction`, `intake-storage-integrations`, `governance-security`, `unified-platform` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] pilot, shadow run, controlled rollout, support ownership, and decommissioning gates | `docs/operations/monitoring_runbooks.md`<br>`docs/operations/release_and_rollback.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md`<br>`docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md` | `parser-extraction`, `intake-storage-integrations`, `governance-security`, `unified-platform` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S1-S2

- [ ] Create regression harness, provider corpus gates, and release checklist for parser/provider changes.

### S3

- [ ] Add integration sandbox tests, monitoring events, failure runbooks, and rollout gates.

### S4-S6

- [ ] Control pilot, staff training, adoption, rollback, and legacy decommissioning evidence.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `parser-extraction` | Extraction work must preserve CE Document Mapper behavior, deterministic rules, canonical schema, and regression coverage. |
| `intake-storage-integrations` | Outlook, Box, EVA/Sentry, website/WhatsApp, and spreadsheet bridges own live system boundaries and source capture. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `unified-platform` | Mature platform convergence coordinates system-wide sequencing and decommissioning only after parity and rollback evidence. |

## Non-Overlap Rules

The workspace explicitly does not own:

- domain-specific feature design
- model-evaluation substrate owned by ai-platform-tools
- business analytics dashboards beyond operational health

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
