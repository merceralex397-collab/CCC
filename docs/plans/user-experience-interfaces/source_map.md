# User Experience Interfaces Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/07_ui_dashboard_spec.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md`, `docs/architecture/parser_ui_cli.md`, `docs/architecture/mvp_interlock.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/23_whatsapp_teams_portal_front_door.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, parser-extraction, provider-principal-config, engineer-communications
Expected outputs: source-to-plan traceability for `docs/plans/user-experience-interfaces/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/user-experience-interfaces/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/07_ui_dashboard_spec.md` | Case-operation dashboard and screen specification. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md` | Dashboard/review queue and UX safeguards. |
| `docs/architecture/parser_ui_cli.md` | Parser UI and CLI architecture. |
| `docs/architecture/mvp_interlock.md` | Staff UI role in first MVP. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/23_whatsapp_teams_portal_front_door.md` | Portal/Teams front-door source. |

## Ownership Boundary

Primary ownership:

- dashboard, holding pen, parser UI, case detail, review, activity/audit, and settings screen maps
- provider-admin UX and role-based workflow surfaces
- internal portal/Teams front-door interaction design
- accessibility, adoption, fallback, and staff mental-model checks

Explicit exclusions:

- business rules implemented by domain workspaces
- parser core logic
- external portal/API product scope

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
