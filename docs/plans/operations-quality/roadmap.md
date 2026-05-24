# Operations Quality Roadmap

Date: 2026-05-24
Status: active workspace roadmap
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/operations/monitoring_runbooks.md`, `docs/operations/release_and_rollback.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: parser-extraction, intake-storage-integrations, governance-security, unified-platform
Expected outputs: phased promotion sequence for `docs/plans/operations-quality/`
Acceptance criteria: roadmap stages cite source-backed workspace scope and do not duplicate another workspace's primary ownership
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/operations-quality/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## S1-S2

- Create regression harness, provider corpus gates, and release checklist for parser/provider changes.

## S3

- Add integration sandbox tests, monitoring events, failure runbooks, and rollout gates.

## S4-S6

- Control pilot, staff training, adoption, rollback, and legacy decommissioning evidence.

## Promotion Gate

Any item promoted from this roadmap must cite `source_map.md`, name dependencies, define acceptance criteria, and state whether governance/security or operations-quality approval is required.
