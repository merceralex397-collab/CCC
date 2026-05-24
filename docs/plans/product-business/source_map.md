# Product Business Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/01_project_brief.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/02_company_business_context.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/13_implementation_roadmap_and_roi.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/14_discovery_questions_and_call_prep.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/16_client_pitch_and_positioning.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: analytics-data-platform, governance-security, unified-platform, external-platform-partners
Expected outputs: source-to-plan traceability for `docs/plans/product-business/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/product-business/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/01_project_brief.md` | Project brief and safe framing. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/02_company_business_context.md` | Company/business context and services. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/13_implementation_roadmap_and_roi.md` | Roadmap and ROI evidence. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/14_discovery_questions_and_call_prep.md` | Discovery questions and call-prep source. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/16_client_pitch_and_positioning.md` | Client pitch and positioning source. |

## Ownership Boundary

Primary ownership:

- discovery questions and stakeholder decisions
- ROI/KPI tracking and commercial value framing
- client pitch and objection handling
- conservative product positioning and independence/defensibility wording

Explicit exclusions:

- technical analytics implementation
- governance policy ownership
- domain feature implementation

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
