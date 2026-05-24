# Repo Navigation And Parser Handoff Alignment

Date: 2026-05-24
Status: active setup ticket
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `AGENTS.md`, `docs/docs_index.md`, `docs/repo_map.json`, `docs/plans/_index.md`, `docs/plans/initial-repo-setup/README.md`, `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`, `docs/plans/parser-extraction/parser-mvp/plan.md`, `tools/generate_plan_workspaces.py`, `tools/verify_scaffold.py`
Roadmap milestone: Section 0 - Taxonomy And Planning Scaffold
Dependencies: source manifest, workspace generator, scaffold verifier, parser-extraction workspace
Expected outputs: corrected navigation references, parser handoff routing, setup todo ledger, manifest updates, verifier coverage
Acceptance criteria: all active navigation identifies `docs/plans/parser-extraction/parser-mvp/plan.md` as the active parser MVP; operational-core parser path is explicitly a stub; setup todos are source-backed; roadmap current status is explicit; task start/completion documentation sync rules are recorded; manifests and verification pass
Verification required: `rg "operational-core/parser-mvp|pending physical relocation|parser ticket relocation" AGENTS.md docs tools`, `python tools/verify_scaffold.py`
Archive target: `docs/plans/initial-repo-setup/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Todo Checklist

- [ ] Update `AGENTS.md`, `docs/docs_index.md`, `docs/plans/_index.md`, `docs/repo_map.json`, and `docs/plans/workspace_ownership_matrix.md` so the active parser plan path is `docs/plans/parser-extraction/parser-mvp/plan.md`.
- [ ] Update `docs/plans/operational-core/source_synthesis.md` so Operational Core is described as coordinator and source-promotion map, not the permanent owner of parser implementation.
- [ ] Update `docs/plans/parser-extraction/README.md`, `plan.md`, `source_map.md`, and `roadmap.md` so they cite the active parser MVP plan and its adjacent-repo/inspection-location review.
- [ ] Update `tools/generate_plan_workspaces.py` so generated workspace docs keep the corrected parser references.
- [ ] Keep `docs/plans/operational-core/parser-mvp/plan.md` as a compatibility stub until verifier and historical links no longer require it.
- [ ] Add a setup todo for a future local project task-start skill, but do not create the skill until its prompts, ownership, portability target, and overlap with `AGENTS.md` are agreed.
- [ ] Add repository documentation lifecycle rules requiring large tasks to check roadmap/key docs at start and update roadmap/key docs at completion.
- [ ] Add a roadmap Current Status section showing the full plan, current phase, next milestone, parser implementation status, required pre-parser actions, and optional pre-parser actions.
- [ ] Regenerate `docs/source_manifest.md`, `docs/source_manifest.csv`, and `docs/source_manifest.json`.
- [ ] Run scaffold verification and record any residual stale-path findings.

## Skill Decision Note

A project navigation/task-start skill may be useful because the user has identified that skills should remain portable across Codex, ChatGPT, Claude Desktop, and other approved AI surfaces. That skill should not be created as part of this ticket. First create a small plan under `docs/plans/agent-skills/` that states:

- whether the skill is for task start, parser implementation, evidence review, or all repo work;
- which files it must read first (`AGENTS.md`, `docs/docs_index.md`, `docs/repo_map.json`, and the relevant workspace plan);
- which instructions stay in `AGENTS.md` because they are repository-wide rules;
- how the skill avoids changing raw evidence or bypassing source-manifest updates;
- how it is evaluated before installation into any AI front end.
