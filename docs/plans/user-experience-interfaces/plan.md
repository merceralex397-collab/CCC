# User Experience Interfaces Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/07_ui_dashboard_spec.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md`, `docs/architecture/parser_ui_cli.md`, `docs/architecture/mvp_interlock.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/23_whatsapp_teams_portal_front_door.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: case-workflow-state, parser-extraction, provider-principal-config, engineer-communications
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/user-experience-interfaces/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/user-experience-interfaces/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/user-experience-interfaces/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/07_ui_dashboard_spec.md` | Case-operation dashboard and screen specification. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md` | Dashboard/review queue and UX safeguards. |
| `docs/architecture/parser_ui_cli.md` | Parser UI and CLI architecture. |
| `docs/architecture/mvp_interlock.md` | Staff UI role in first MVP. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/23_whatsapp_teams_portal_front_door.md` | Portal/Teams front-door source. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] dashboard, holding pen, parser UI, case detail, review, activity/audit, and settings screen maps | `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/07_ui_dashboard_spec.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md`<br>`docs/architecture/parser_ui_cli.md`<br>`docs/architecture/mvp_interlock.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/23_whatsapp_teams_portal_front_door.md` | `case-workflow-state`, `parser-extraction`, `provider-principal-config`, `engineer-communications` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] provider-admin UX and role-based workflow surfaces | `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/07_ui_dashboard_spec.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md`<br>`docs/architecture/parser_ui_cli.md`<br>`docs/architecture/mvp_interlock.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/23_whatsapp_teams_portal_front_door.md` | `case-workflow-state`, `parser-extraction`, `provider-principal-config`, `engineer-communications` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] internal portal/Teams front-door interaction design | `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/07_ui_dashboard_spec.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md`<br>`docs/architecture/parser_ui_cli.md`<br>`docs/architecture/mvp_interlock.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/23_whatsapp_teams_portal_front_door.md` | `case-workflow-state`, `parser-extraction`, `provider-principal-config`, `engineer-communications` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] accessibility, adoption, fallback, and staff mental-model checks | `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/07_ui_dashboard_spec.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md`<br>`docs/architecture/parser_ui_cli.md`<br>`docs/architecture/mvp_interlock.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/23_whatsapp_teams_portal_front_door.md` | `case-workflow-state`, `parser-extraction`, `provider-principal-config`, `engineer-communications` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S1

- [ ] Plan staff parser UI and review/correction flows over the shared parser and work-item services.

### S2-S4

- [ ] Add case operation dashboard, evidence matching, estimate review, activity log, and engineer pack UX.

### S5-S6

- [ ] Plan internal portal/Teams, engineer PWA/mobile, and mature platform surfaces.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `case-workflow-state` | Work-item state, review status, blockers, audit events, and approvals are the operational source of truth. |
| `parser-extraction` | Extraction work must preserve CE Document Mapper behavior, deterministic rules, canonical schema, and regression coverage. |
| `provider-principal-config` | Provider/principal presets, routing, aliases, and admin workflows must stay separate from parser mechanics. |
| `engineer-communications` | Coordinate source ownership, sequencing, acceptance criteria, and verification before ticket promotion. |

## Non-Overlap Rules

The workspace explicitly does not own:

- business rules implemented by domain workspaces
- parser core logic
- external portal/API product scope

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
