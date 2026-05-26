# User Experience Interfaces Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/07_ui_dashboard_spec.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md`, `docs/architecture/parser_ui_cli.md`, `docs/architecture/mvp_interlock.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/23_whatsapp_teams_portal_front_door.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, parser-extraction, provider-principal-config, engineer-communications
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/user-experience-interfaces/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/user-experience-interfaces/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Human-facing screen, workflow, and interaction design across staff, engineer, admin, and front-door surfaces.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- dashboard, holding pen, parser UI, case detail, review, activity/audit, and settings screen maps
- provider-admin UX and role-based workflow surfaces
- internal portal/Teams front-door interaction design
- accessibility, adoption, fallback, and staff mental-model checks

## Does Not Own

- business rules implemented by domain workspaces
- parser core logic
- external portal/API product scope

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/07_ui_dashboard_spec.md` | Case-operation dashboard and screen specification. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md` | Dashboard/review queue and UX safeguards. |
| `docs/architecture/parser_ui_cli.md` | Parser UI and CLI architecture. |
| `docs/architecture/mvp_interlock.md` | Staff UI role in first MVP. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/23_whatsapp_teams_portal_front_door.md` | Portal/Teams front-door source. |

## Cross-Workspace Dependencies

- case-workflow-state
- parser-extraction
- provider-principal-config
- engineer-communications

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
