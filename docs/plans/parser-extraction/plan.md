# Parser Extraction Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`, `docs/decisions/0004-ground-up-compatible-parser-rebuild.md`, `docs/decisions/0007-deterministic-first-parser.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`, `docs/contracts/extraction_adapter_contract_v1.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: provider-principal-config, operations-quality, governance-security, user-experience-interfaces
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/parser-extraction/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/parser-extraction/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/plans/parser-extraction/parser-mvp/plan.md` | Active parser MVP implementation plan. |
| `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md` | Adjacent parser comparison, inspection-location decision register, and EVA/Sentry lookup constraint. |
| `docs/decisions/0004-ground-up-compatible-parser-rebuild.md` | Accepted ground-up compatible parser rebuild decision. |
| `docs/decisions/0007-deterministic-first-parser.md` | Accepted deterministic-first parser decision. |
| `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md` | Document Mapper and extraction work package. |
| `docs/contracts/extraction_adapter_contract_v1.md` | Versioned extraction adapter contract. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] PDF, DOCX, DOC, MSG, EML, image, ZIP, and batch extraction | `docs/plans/parser-extraction/parser-mvp/plan.md`<br>`docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`<br>`docs/decisions/0004-ground-up-compatible-parser-rebuild.md`<br>`docs/decisions/0007-deterministic-first-parser.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`<br>`docs/contracts/extraction_adapter_contract_v1.md` | `provider-principal-config`, `operations-quality`, `governance-security`, `user-experience-interfaces` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] deterministic-first parser core and provider-rule execution behavior | `docs/plans/parser-extraction/parser-mvp/plan.md`<br>`docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`<br>`docs/decisions/0004-ground-up-compatible-parser-rebuild.md`<br>`docs/decisions/0007-deterministic-first-parser.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`<br>`docs/contracts/extraction_adapter_contract_v1.md` | `provider-principal-config`, `operations-quality`, `governance-security`, `user-experience-interfaces` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] OCR/cloud document-intelligence option papers | `docs/plans/parser-extraction/parser-mvp/plan.md`<br>`docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`<br>`docs/decisions/0004-ground-up-compatible-parser-rebuild.md`<br>`docs/decisions/0007-deterministic-first-parser.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`<br>`docs/contracts/extraction_adapter_contract_v1.md` | `provider-principal-config`, `operations-quality`, `governance-security`, `user-experience-interfaces` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] parser CLI parity and extraction regression corpus | `docs/plans/parser-extraction/parser-mvp/plan.md`<br>`docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`<br>`docs/decisions/0004-ground-up-compatible-parser-rebuild.md`<br>`docs/decisions/0007-deterministic-first-parser.md`<br>`docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md`<br>`docs/contracts/extraction_adapter_contract_v1.md` | `provider-principal-config`, `operations-quality`, `governance-security`, `user-experience-interfaces` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S1

- [ ] Maintain active parser MVP planning here, then deliver deterministic parser core and shared UI/CLI service behavior.

### S2

- [ ] Harden extraction adapters, provider corpus coverage, export blockers, and UI/CLI parity.

### S3-S4

- [ ] Evaluate OCR/cloud fallback and AI extraction only behind governance and measurable regression evidence.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `provider-principal-config` | Provider/principal presets, routing, aliases, and admin workflows must stay separate from parser mechanics. |
| `operations-quality` | Release, rollback, regression, monitoring, runbooks, pilot, support, and decommissioning gates must be explicit. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `user-experience-interfaces` | Human-facing surfaces must use shared domain contracts and keep UI thin over parser/work-item services. |

## Non-Overlap Rules

The workspace explicitly does not own:

- provider business routing metadata after extraction
- case-state transitions after parse
- human-facing UI design beyond parser-specific requirements

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
