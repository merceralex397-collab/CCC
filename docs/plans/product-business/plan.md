# Product Business Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/01_project_brief.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/02_company_business_context.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/13_implementation_roadmap_and_roi.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/14_discovery_questions_and_call_prep.md`, `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/16_client_pitch_and_positioning.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: analytics-data-platform, governance-security, unified-platform, external-platform-partners
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/product-business/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/product-business/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/product-business/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/01_project_brief.md` | Project brief and safe framing. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/02_company_business_context.md` | Company/business context and services. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/13_implementation_roadmap_and_roi.md` | Roadmap and ROI evidence. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/14_discovery_questions_and_call_prep.md` | Discovery questions and call-prep source. |
| `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/16_client_pitch_and_positioning.md` | Client pitch and positioning source. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] discovery questions and stakeholder decisions | `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/01_project_brief.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/02_company_business_context.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/13_implementation_roadmap_and_roi.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/14_discovery_questions_and_call_prep.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/16_client_pitch_and_positioning.md` | `analytics-data-platform`, `governance-security`, `unified-platform`, `external-platform-partners` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] ROI/KPI tracking and commercial value framing | `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/01_project_brief.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/02_company_business_context.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/13_implementation_roadmap_and_roi.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/14_discovery_questions_and_call_prep.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/16_client_pitch_and_positioning.md` | `analytics-data-platform`, `governance-security`, `unified-platform`, `external-platform-partners` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] client pitch and objection handling | `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/01_project_brief.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/02_company_business_context.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/13_implementation_roadmap_and_roi.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/14_discovery_questions_and_call_prep.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/16_client_pitch_and_positioning.md` | `analytics-data-platform`, `governance-security`, `unified-platform`, `external-platform-partners` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] conservative product positioning and independence/defensibility wording | `docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/01_project_brief.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/02_company_business_context.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/13_implementation_roadmap_and_roi.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/14_discovery_questions_and_call_prep.md`<br>`docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/16_client_pitch_and_positioning.md` | `analytics-data-platform`, `governance-security`, `unified-platform`, `external-platform-partners` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S0-S1

- [ ] Keep CCC positioned as vehicle-damage intake, evidence, and admin support, not autonomous expert judgement.

### S3-S5

- [ ] Track ROI, adoption, throughput, and provider bottlenecks from operational evidence.

### S5-S6

- [ ] Prepare client/partner positioning, objections, and commercial prioritisation for external ecosystem work.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `analytics-data-platform` | Analytics must consume reviewed canonical events and approved data products, not raw operational side effects. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `unified-platform` | Mature platform convergence coordinates system-wide sequencing and decommissioning only after parity and rollback evidence. |
| `external-platform-partners` | External access, partner APIs, portals, and insurer/estimating-system partnerships require option papers and governance gates. |

## Non-Overlap Rules

The workspace explicitly does not own:

- technical analytics implementation
- governance policy ownership
- domain feature implementation

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
