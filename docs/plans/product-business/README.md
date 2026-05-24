# Product Business Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/01_project_brief.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/02_company_business_context.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/13_implementation_roadmap_and_roi.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/14_discovery_questions_and_call_prep.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/16_client_pitch_and_positioning.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: analytics-data-platform, governance-security, unified-platform, external-platform-partners
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/product-business/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/product-business/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Business framing, discovery, ROI/KPI tracking, client positioning, objections, and defensibility planning.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- discovery questions and stakeholder decisions
- ROI/KPI tracking and commercial value framing
- client pitch and objection handling
- conservative product positioning and independence/defensibility wording

## Does Not Own

- technical analytics implementation
- governance policy ownership
- domain feature implementation

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/01_project_brief.md` | Project brief and safe framing. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/02_company_business_context.md` | Company/business context and services. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/13_implementation_roadmap_and_roi.md` | Roadmap and ROI evidence. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/14_discovery_questions_and_call_prep.md` | Discovery questions and call-prep source. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/16_client_pitch_and_positioning.md` | Client pitch and positioning source. |

## Cross-Workspace Dependencies

- analytics-data-platform
- governance-security
- unified-platform
- external-platform-partners

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
