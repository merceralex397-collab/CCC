# Initial Repo Setup Planning

Date: 2026-05-23
Status: active planning workspace
Owner: unassigned
Created: 2026-05-23
Last reviewed: 2026-05-24
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

## Remaining Setup Todos

These todos are active until closed by a setup ticket or an implemented archive entry.

| Todo | Owner workspace | Source evidence | Done when |
| --- | --- | --- | --- |
| - [ ] Align parser MVP path references after relocation | `initial-repo-setup`, supporting `parser-extraction` | `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`, `docs/plans/parser-extraction/parser-mvp/plan.md`, `docs/repo_map.json`, `AGENTS.md` | Human navigation, machine map, workspace docs, scaffold verification, and source manifests all point to `docs/plans/parser-extraction/parser-mvp/plan.md` as active, with the operational-core path described only as a stub. |
| - [ ] Keep generated workspace docs and generator source in sync | `initial-repo-setup` | `tools/generate_plan_workspaces.py`, `docs/plans/_index.md`, `docs/docs_index.md`, `docs/plans/workspace_ownership_matrix.md` | Re-running the workspace generator would not reintroduce stale parser relocation wording. |
| - [ ] Add a local project navigation/task-start skill plan before creating any skill | `initial-repo-setup`, supporting `agent-skills` | `AGENTS.md`, `docs/docs_index.md`, `docs/repo_map.json`, `docs/plans/agent-skills/plan.md` | A scoped ticket explains when a Codex/ChatGPT/Claude-compatible skill should exist, what it should read first, and how it avoids duplicating AGENTS.md. |
| - [ ] Keep repository documentation lifecycle rules explicit | `initial-repo-setup`, supporting all workspaces | `AGENTS.md`, `docs/docs_index.md`, `docs/roadmap.md`, `docs/plans/_index.md` | Every large task has clear start-of-task and completion documentation checks, including roadmap current-status maintenance. |
| - [ ] Keep roadmap current status accurate | `initial-repo-setup`, supporting `operational-core` | `docs/roadmap.md`, `docs/plans/roadmap.md`, `docs/plans/operational-core/source_synthesis.md` | Roadmap shows both the full sequential plan and the exact current position before parser implementation starts. |
| - [ ] Maintain source manifest coverage for active docs and generated derivatives | `initial-repo-setup` | `docs/source_manifest.md`, `docs/source_manifest.csv`, `docs/source_manifest.json`, `tools/verify_scaffold.py` | All changed docs and new planning files are present in all manifest formats and scaffold verification passes. |
| - [ ] Keep setup roadmap separate from parser implementation | `initial-repo-setup`, supporting `parser-extraction` | `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md`, `docs/plans/parser-extraction/tickets/` | Setup tickets track documentation hygiene only; parser implementation readiness is tracked under `parser-extraction`. |

## Pre-Parser Start Checklist

Required before parser implementation starts:

- [ ] Documentation lifecycle rules are recorded in `AGENTS.md` and `docs/docs_index.md`.
- [ ] `docs/roadmap.md` and `docs/plans/roadmap.md` show the current position and next parser milestone.
- [ ] Parser MVP handoff docs remain active under `docs/plans/parser-extraction/parser-mvp/`.
- [ ] `docs/source_manifest.*` has been regenerated after documentation changes.
- [ ] `python tools/verify_scaffold.py` passes.
- [ ] `python -m pytest tests/test_scaffold_contracts.py` passes.
- [ ] Documentation baseline is committed and pushed.

Non-blocking unless explicitly requested:

- [ ] Create a portable task-start/navigation skill plan under `docs/plans/agent-skills/`.
