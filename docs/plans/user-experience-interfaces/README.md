# User Experience Interfaces Workspace

## Purpose

This workspace owns all planning for the staff parser UI, engineer UI, admin screens, review/correction workflow, dashboard, portal/front-door interface, and accessibility planning.

## Scope Rules

- UI must be thin — it calls the same parser core and shares validation/export contracts as the CLI.
- No extraction logic is duplicated in the UI layer.
- Personal injury and KADOE are out of scope.
- External portal/API/payment automation is long-range planned and requires governance approval before implementation starts.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/architecture/parser_ui_cli.md` | UI/CLI parity architecture. |
| `docs/decisions/options/ui_platform_options.md` | UI platform options paper. |
| `docs/reference/normalized/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md` | Whiteboard UI/dashboard expectations, case detail page, review queue. |
| `docs/plans/operational-core/archived_plans/implemented/2026-05-23-implemented-figmaplan.md` | Implemented Figma plan — review screens, upload flow, image ordering panel. |
| `docs/reference/originalplanning/originalplans_output/` | Practical MVP framing: holding pen, intake/upload, evidence matching, case detail page, engineer pack, provider management. |

## Workspace Layout

- `README.md` — this file
- `tickets/` — active tickets
- `option-papers/` — unresolved decisions (UI platform choice, state-store approach)
- `archived_plans/` — implemented and superseded plans
