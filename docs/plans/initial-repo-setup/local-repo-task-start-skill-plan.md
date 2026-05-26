# Local Repo Task-Start Skill Plan

Date: 2026-05-24
Status: implemented locally; not archived until current docs are committed
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `AGENTS.md`, `docs/docs_index.md`, `docs/repo_map.json`, `docs/roadmap.md`, `docs/plans/initial-repo-setup/README.md`, `docs/plans/initial-repo-setup/tickets/p0-repo-navigation-and-parser-handoff-alignment.md`, local Codex `skill-creator` guidance, local Codex writing-skills guidance
Roadmap milestone: Section 0 - Taxonomy And Planning Scaffold
Dependencies: AGENTS navigation rules, source manifest workflow, scaffold verification, future local skill installation location
Expected outputs: a local CCC repo-development task-start/navigation skill for AI coding agents and a source-backed plan/evaluation record
Acceptance criteria: the skill is clearly separated from production Collision Engineers skills; the skill creation workflow follows skill-creator and writing-skills guidance where possible without subagents; the skill validates with skill tooling; repository docs and manifests are updated
Verification required: `python tools/verify_scaffold.py`, `python -m pytest tests/test_scaffold_contracts.py`
Archive target: `docs/plans/initial-repo-setup/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Scope

This plan is for a local development skill that helps AI coding agents start tasks in the CCC repository. It is not a production Collision Engineers skill, not a staff/engineer-facing workflow skill, and not owned by `docs/plans/agent-skills/`.

The production `agent-skills` workspace remains reserved for CE-facing reusable skills such as case summaries, missing-info drafting, CE style, valuation explanation, report-clause/RAG support, AI literacy/training, and provider mapping.

## Intended Skill

Proposed skill name: `ccc-repo-task-start`.

Proposed trigger: use when an AI coding agent starts, resumes, plans, implements, verifies, or completes a task in the CCC repository.

Installation target: the user's local Codex skills home as `ccc-repo-task-start`.

The repository plan remains here under `docs/plans/initial-repo-setup/` so it is versioned with the project.

## Required Skill-Creation Guidance

From `skill-creator`:

- Use lowercase hyphenated skill naming.
- Keep `SKILL.md` concise and self-contained unless references are genuinely needed.
- Include YAML frontmatter with only required `name` and `description`.
- Write a description that clearly states when the skill should trigger.
- Do not create extra files such as README, changelog, or installation guides inside the skill.
- Use `scripts/init_skill.py` when actually creating the skill.
- Run `scripts/quick_validate.py <path-to-skill>` after creating the skill.

From `superpowers:writing-skills`:

- Treat skill creation as TDD for process documentation.
- Define pressure scenarios before writing the skill.
- Watch baseline behavior fail without the skill before trusting the skill.
- Keep the description focused on trigger conditions, not workflow summary.
- Add explicit counters for rationalizations that would skip roadmap/key-doc checks or manifest updates.
- Do not deploy the skill until it has been tested and validated.

## Planned Skill Responsibilities

- Read `AGENTS.md`, `docs/docs_index.md`, `docs/repo_map.json`, `docs/roadmap.md`, and the owning workspace plan at task start.
- Identify the owning workspace, active ticket or plan, source evidence, and required verification before edits.
- Distinguish raw evidence from generated derivatives and active docs.
- Remind the agent to update roadmap current status, active tickets, key docs, manifests, and verification records at task completion.
- Route parser work to `docs/plans/parser-extraction/parser-mvp/plan.md` and its adjacent parser review.
- Preserve the distinction between local repo-development skills and production CE skills.

## Non-Responsibilities

- Do not encode production Collision Engineers prompts or staff workflows.
- Do not own CE case summary, chaser drafting, valuation explanation, report-clause/RAG, or provider mapping skills.
- Do not replace `AGENTS.md`; repository-wide rules stay there.
- Do not edit raw evidence or source manifests directly without the documented generator/verification flow.
- Do not install the skill as part of this plan.

## Pressure Scenarios For Future Testing

These are candidate RED/GREEN tests for the future skill:

1. A parser task starts and the agent tries to inspect code before reading the parser MVP plan or adjacent parser review.
2. A quick documentation edit completes and the agent says the task is too small to update roadmap/key docs or source manifests.
3. A skill-planning task tries to place a repo-development skill under `docs/plans/agent-skills/`.
4. A task touches raw evidence and the agent attempts to normalize or overwrite it in place.
5. A task changes active planning status and the agent forgets to update `docs/roadmap.md`.

Subagent testing is disallowed for this repository. Validation therefore uses local pressure-scenario review, skill quick validation, and repository verification instead of subagent forward-testing.

## Baseline Pressure Findings

Baseline failures observed before the local skill existed:

| Scenario | Observed failure | Skill counter |
| --- | --- | --- |
| Plan checklist requested as todos | Checklist items were collapsed into broad todo items instead of every plan row being represented. | Skill requires every active plan/ticket checklist item to be placed in the todo tool. |
| Documentation lifecycle wording | Earlier rules used scoped qualifiers that could create ambiguity about small tasks. | Skill states the rule applies to every task. |
| Repo-development skill ownership | Local coding-agent skill planning was initially pointed at `docs/plans/agent-skills/`. | Skill separates local repo-development skills under `initial-repo-setup` from production CE skills under `agent-skills`. |
| Completion after docs changed | Manifest and verification updates can be skipped if not explicit. | Skill requires manifest regeneration and fresh verification after final changes. |

## Creation Checklist

- [x] Confirm final skill name and installation target.
- [x] Confirm the trigger description and avoid workflow summary in frontmatter.
- [x] Write baseline pressure scenarios before creating the skill.
- [x] Run baseline scenarios without the skill and record failures or rationalizations.
- [x] Initialize the skill with `skill-creator` tooling.
- [x] Write minimal `SKILL.md` focused on CCC task-start and completion checks.
- [x] Validate the skill with quick validation tooling.
- [x] Run pressure scenarios with the skill and record whether behavior improves.
- [x] Add explicit counters for any rationalizations found.
- [x] Install or commit the skill only after approval.

## Installed Skill Verification

The local skill was installed in the user's local Codex skills home as `ccc-repo-task-start`. It is not a production CE skill and is not stored under `docs/plans/agent-skills/`.

Pressure-scenario review after writing the skill:

- Parser task start is covered by explicit parser plan and adjacent review reads.
- Small task ambiguity is addressed by `every task` wording.
- Local skill ownership is addressed by explicit `initial-repo-setup` versus `agent-skills` ownership rules.
- Raw evidence handling and manifest regeneration are explicit completion requirements.
- Subagent forward-testing was not run because this repository currently forbids subagents.
