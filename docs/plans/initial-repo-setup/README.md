# Initial Repo Setup Planning

Date: 2026-05-23
Status: active planning workspace
Owner: unassigned
Created: 2026-05-23
Last reviewed: 2026-05-23
Source links: `docs/reference/`, `docs/reference/originalplanning/`, `docs/reference/test-context/testprojectcontext/`, `docs/plans/operational-core/source_synthesis.md`
Roadmap milestone: Pre-code repository setup and planning
Dependencies: source manifest, reference corpus, original planning packs, test context packs
Expected outputs: initial setup plan, documentation scaffold plan, complete all-ideas reference backlog
Acceptance criteria: first-step repository setup is separated from Operational Core implementation; every reference-derived idea has a planning home even when long-term
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/initial-repo-setup/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

This workspace captures the project work that happens before real product code: repository setup, documentation structure, source evidence handling, planning consolidation, and the exhaustive all-ideas backlog.

## Layout

| Path | Use |
| --- | --- |
| `documentation-scaffold/` | Plans for repo structure, docs, manifests, verification, and source preservation. |
| `reference-audit/` | Exhaustive plans derived from reference, original planning, and test-context material. |
| `tickets/` | Pre-code documentation and setup tickets. |
| `archived_plans/implemented/` | Completed initial setup plans. |
| `archived_plans/superseded/` | Initial setup plans replaced by later docs. |

## Planning Rule

Operational Core tickets may still narrow MVP scope, but this workspace must not lose ideas by deferring them without a plan. Long-term, speculative, governance-gated, or dependency-heavy ideas belong in the all-ideas plan with an explicit planning phase.
