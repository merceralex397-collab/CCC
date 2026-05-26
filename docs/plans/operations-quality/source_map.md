# Operations Quality Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/operations/monitoring_runbooks.md`, `docs/operations/release_and_rollback.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: parser-extraction, intake-storage-integrations, governance-security, unified-platform
Expected outputs: source-to-plan traceability for `docs/plans/operations-quality/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/operations-quality/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/operations/monitoring_runbooks.md` | Current monitoring and runbooks baseline. |
| `docs/operations/release_and_rollback.md` | Current release and rollback baseline. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md` | Test corpus and regression harness plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md` | Monitoring, runbooks, and release management plan. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md` | Security, testing, rollout, and decommissioning plan. |

## Ownership Boundary

Primary ownership:

- test corpus and regression harness planning
- release and rollback process
- monitoring, runbooks, alerts, incident/failure playbooks
- pilot, shadow run, controlled rollout, support ownership, and decommissioning gates

Explicit exclusions:

- domain-specific feature design
- model-evaluation substrate owned by ai-platform-tools
- business analytics dashboards beyond operational health

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
