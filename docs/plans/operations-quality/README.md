# Operations Quality Workspace

## Purpose

This workspace owns all planning for test corpus management, regression harness infrastructure, release and rollback procedures, monitoring, runbooks, staged rollout, and decommissioning.

## Scope Rules

- Private real corpus only — no synthetic or publicly sourced test data unless explicitly approved (see ADR 0008).
- Release gates must verify scaffold, contracts, and corpus regression before MVP acceptance.
- Decommissioning plans must address the Excel job sheet and network folder dependencies documented in `handover.docx`.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md` | Test corpus and regression harness design. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md` | Monitoring, runbooks, and release management. |
| `docs/decisions/0008-private-real-corpus-only.md` | ADR: private real corpus only. |
| `docs/reference/normalized/collisionrelateddocs__collision_releated__handover.docx.md` | Job sheet VBA and network folder dependencies that decommissioning must address. |

## Workspace Layout

- `README.md` — this file
- `tickets/` — active tickets
- `option-papers/` — unresolved decisions
- `archived_plans/` — implemented and superseded plans
