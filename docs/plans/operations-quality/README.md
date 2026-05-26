# Operations Quality Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/operations/monitoring_runbooks.md`, `docs/operations/release_and_rollback.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: parser-extraction, intake-storage-integrations, governance-security, unified-platform
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/operations-quality/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/operations-quality/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Shared QA, release, rollout, monitoring, support, regression, and decommissioning planning.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- test corpus and regression harness planning
- release and rollback process
- monitoring, runbooks, alerts, incident/failure playbooks
- pilot, shadow run, controlled rollout, support ownership, and decommissioning gates

## Does Not Own

- domain-specific feature design
- model-evaluation substrate owned by ai-platform-tools
- business analytics dashboards beyond operational health

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/operations/monitoring_runbooks.md` | Current monitoring and runbooks baseline. |
| `docs/operations/release_and_rollback.md` | Current release and rollback baseline. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md` | Test corpus and regression harness plan. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md` | Monitoring, runbooks, and release management plan. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md` | Security, testing, rollout, and decommissioning plan. |

## Cross-Workspace Dependencies

- parser-extraction
- intake-storage-integrations
- governance-security
- unified-platform

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
