# Initial Repository Documentation Scaffold Plan

Date: 2026-05-23
Status: active planning record
Owner: unassigned
Created: 2026-05-23
Last reviewed: 2026-05-23
Source links: `docs/plans/initial-repo-setup/archived_plans/implemented/2026-05-23-implemented-initrepoplan.md`, `docs/plans/initial-repo-setup/archived_plans/implemented/2026-05-23-implemented-repository-restructure.md`, `docs/docs_index.md`, `docs/repo_map.json`, `docs/source_manifest.md`
Roadmap milestone: Pre-code repository setup and planning
Dependencies: repository scaffold, source manifest, reference folder structure
Expected outputs: durable documentation scaffold, navigation files, manifest checks, plan lifecycle rules
Acceptance criteria: repo setup work is discoverable separately from product implementation plans
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/initial-repo-setup/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

Capture the first project step: setting up the repository, documentation hierarchy, source evidence rules, manifesting, verification, and planning structure before product code work starts.

## Scope

- repository hygiene and ignore rules;
- documentation navigation and machine-readable path map;
- source manifest generation and parity checks;
- raw evidence immutability and normalized companion conventions;
- reference pack classification;
- plan and ticket lifecycle rules;
- initial verification script coverage;
- source-derived idea inventory.

## Subfolders

- `documentation-scaffold/` owns this setup plan and future docs-scaffold follow-up plans.
- `reference-audit/` owns exhaustive inventories and all-ideas plans derived from reference material.
- `tickets/` owns pre-code tickets that are not part of Operational Core implementation.
- `archived_plans/implemented/` and `archived_plans/superseded/` mirror the active plan lifecycle used elsewhere.

## Follow-Up Outputs

- Keep `docs/plans/_index.md` current.
- Keep `docs/docs_index.md` current.
- Keep `docs/repo_map.json` current.
- Keep `docs/source_manifest.*` current after any file addition, move, or archive.
