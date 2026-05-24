# Provider Principal Config Workspace

## Purpose

This workspace owns all planning for provider configuration, principal configuration, garage routing metadata, provider-admin UI, and provider settings migration.

## Scope Rules

- Provider coverage must be tracked in `docs/reference/data/provider_coverage_matrix.md` before adding or changing provider rules.
- Provider config is versioned and must support activation, rollback, and audit events.
- Personal injury and KADOE are out of scope.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json` | 26 provider presets with extraction methods and optional routing metadata fields. |
| `docs/reference/raw/collisionrelateddocs/collision_releated/Mapped Principals.xlsx` (via normalized companion) | Job sheet principal rows; reveals `ACSP`, `OAK/AX`, `PRINCIPAL`, `WOODLANDS` as uncovered. |
| `docs/reference/normalized/collisionrelateddocs__collision_releated__handover.docx.md` | Fee-note handling exceptions for `QDOS`, `QCL`, `AX`, `FW`, `OAK`, `ALS`; garage figures rule. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md` | Provider settings migration requirements. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_02_provider_principal_configuration_library.md` | Provider/principal library design. |

## Workspace Layout

- `README.md` — this file
- `source_map.md` — reference-to-plan traceability
- `roadmap.md` — sequencing
- `tickets/` — active tickets
- `option-papers/` — unresolved decisions
- `archived_plans/` — implemented and superseded plans
