# Implemented State

- Status: implemented
- Implemented date: 2026-05-23
- Delivered summary: Repository planning, archive, raw evidence, normalized companions, generated planning packs, reference data, indexes, manifests, parser defaults, scaffold tooling, and verification paths were reorganized into the `docs/plans/` and `docs/reference/` structure.
- Verification performed: `python tools/verify_scaffold.py`, `pytest`, `python -m py_compile tools/verify_scaffold.py tools/scaffold_initial_repo.py src/ccc_parser/core.py tests/test_scaffold_contracts.py`, targeted stale-path scans, JSON parsing checks, manifest CSV/JSON parity check, and targeted secret scan.
- Follow-up work moved elsewhere: none.

---

# Repository Documentation Restructure Plan

Original status: active implementation plan
Owner: unassigned
Created: 2026-05-23
Last reviewed: 2026-05-23
Source links: `AGENTS.md`, `README.md`, `docs/plans/operational-core/parser-mvp/plan.md`, `docs/plans/operational-core/source_synthesis.md`, `docs/plans/operational-core/tickets/`, `docs/reference/`, `docs/reference/normalized/`, `docs/reference/data/`, `docs/reference/raw/collisionrelateddocs/`, `archive/`
Roadmap milestone: repository hygiene and planning scaffold
Dependencies: current scaffold verification passes; path blast-radius scan completed; plan unit selected as programme plan
Expected outputs: reorganized plan/reference folders, updated navigation docs, updated scaffold tooling, regenerated manifests, passing verification
Acceptance criteria: no active docs depend on old paths; new plan/reference structure is discoverable; scaffold verifier and tests pass
Verification required: `python tools/verify_scaffold.py`, `pytest`, targeted stale-path scan, targeted secret scan before any commit or push
Archive target: `docs/plans/operational-core/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Summary

Reorganize the repository around one clear split:

- `docs/plans/` is for active and archived planning work.
- `docs/reference/` is for raw evidence, normalized derivatives, generated/original planning packs, test contexts, and extracted data.
- root docs/code/tests/tools remain the active product, parser, and verification surface.

Use `docs/plans/operational-core/` as the active programme plan workspace.

## Target Structure

```text
docs/
  plans/
    _index.md
    repository-restructure/
      plan.md
    operational-core/
      source_synthesis.md
      parser-mvp/
        plan.md
      tickets/
        README.md
        backlog_index.md
        p0-foundation.md
        p1-operational-core-mvp.md
        p2-parser-hardening-provider-parity.md
        p3-integrations-storage-eva-intake.md
        p4-intelligence-engineer-communications.md
        p5-platform-expansion.md
      archived_plans/
        implemented/
        superseded/

  reference/
    _index.md
    raw/
      collisionrelateddocs/
    normalized/
    data/
      provider_coverage_matrix.md
      provider_coverage_matrix.csv
      jam_exports/
    originalplanning/
    test-context/

  docs_index.md
  repo_map.json
```

Notes:

- `archive/plans/...` moves to `docs/plans/operational-core/archived_plans/...`.
- Raw evidence moves from `collisionrelateddocs/` to `docs/reference/raw/collisionrelateddocs/`; do not edit raw files.
- `docs/normalized/` moves to `docs/reference/normalized/`.
- `docs/data/` moves to `docs/reference/data/`.
- `docs/reference/generated-packs/` moves to `docs/reference/originalplanning/`.
- `docs/reference/generated_packs_index.md` becomes `docs/reference/originalplanning_index.md`.
- `docs/planning/source_synthesis.md` moves to `docs/plans/operational-core/source_synthesis.md`.
- `docs/plans/parser_mvp_implementation_plan.md` moves to `docs/plans/operational-core/parser-mvp/plan.md`.
- `docs/tickets/*` moves to `docs/plans/operational-core/tickets/*`.

## Implementation Steps

1. Baseline verification:
   - Run `python tools/verify_scaffold.py`.
   - Run `pytest tests/test_scaffold_contracts.py`.
   - Capture `git status --short`.

2. Create the plan file:
   - Add `docs/plans/repository-restructure/plan.md` with this restructure plan.
   - Keep the metadata block at the top current until the plan is implemented or superseded.

3. Move directories with `git mv`:
   - `archive/plans/implemented` -> `docs/plans/operational-core/archived_plans/implemented`.
   - Create `docs/plans/operational-core/archived_plans/superseded`.
   - `docs/planning/source_synthesis.md` -> `docs/plans/operational-core/source_synthesis.md`.
   - `docs/plans/parser_mvp_implementation_plan.md` -> `docs/plans/operational-core/parser-mvp/plan.md`.
   - `docs/tickets/*` -> `docs/plans/operational-core/tickets/`.
   - `collisionrelateddocs` -> `docs/reference/raw/collisionrelateddocs`.
   - `docs/normalized` -> `docs/reference/normalized`.
   - `docs/data` -> `docs/reference/data`.
   - `docs/reference/generated-packs` -> `docs/reference/originalplanning`.

4. Update runtime and test path contracts:
   - Change `src/ccc_parser/core.py` default provider config to `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json`.
   - Update `tests/test_scaffold_contracts.py` provider config references.
   - Update any CLI/help text that names the raw provider path.

5. Update scaffold tooling:
   - In `tools/verify_scaffold.py`, replace required paths with the new structure.
   - Teach verifier that `docs/plans/**/archived_plans/**` is archived material, not active planning.
   - Update manifest checks to `docs/reference/raw/collisionrelateddocs/`.
   - Update provider matrix checks to `docs/reference/data/...`.
   - Add stale-path assertions for `archive/`, root `collisionrelateddocs/`, `docs/planning/`, `docs/tickets/`, `docs/normalized/`, `docs/data/`, and `docs/reference/generated-packs/`.
   - Allow old strings only inside migration history where intentionally documented.

6. Update `tools/scaffold_initial_repo.py`:
   - Change generation targets to the new structure.
   - Change classification rules for raw evidence, normalized derivatives, reference data, original planning, test context, active plans, and archived plans.
   - Change companion path generation to `docs/reference/normalized/{slug}.md`.
   - Change generated/original planning path handling to `docs/reference/originalplanning`.
   - Regenerate any embedded README/AGENTS/template text that still instructs old paths.

7. Update documentation links and instructions:
   - Update `AGENTS.md` with a short Navigation section naming active plans, archived plans, raw evidence, normalized/reference data, original planning packs, and agent entry points.
   - Update `README.md` Source Of Truth section.
   - Update moved plan/ticket files to use the new archive target.
   - Update `docs/roadmap.md`, architecture docs, contracts, decisions, operations docs, and reference indexes for moved paths.
   - Preserve historical archive content, but add a short migration note where old paths appear as historical references.

8. Add navigation artifacts:
   - Create `docs/docs_index.md` as the human entry point.
   - Create `docs/repo_map.json` as machine-readable navigation for agents.
   - Include for each major area: purpose, status, owner/type, canonical path, old path if migrated, and when to use it.
   - Mirror the useful pattern from the `openai-docs` skill: quick start, reference map, quality rules, fallback guidance.

9. Regenerate manifests:
   - Update `docs/source_manifest.md`.
   - Update `docs/source_manifest.csv`.
   - Update `docs/source_manifest.json`.
   - Ensure raw-source rows now point to `docs/reference/raw/collisionrelateddocs/...`.
   - Ensure normalized companions point to `docs/reference/normalized/...`.
   - Ensure archived plans are not marked as active plans.

10. Update generated metadata with path provenance:
    - Update `docs/reference/data/provider_coverage_matrix.md`.
    - Update `docs/reference/data/provider_coverage_matrix.csv`.
    - Update Jam export metadata paths under `docs/reference/data/jam_exports/**`, especially `jam_meta.json` and `image_index.csv`.

11. Verify stale paths:
    - Run targeted `rg` checks for old prefixes.
    - Confirm remaining matches are either intentionally historical or listed in a migration note.
    - No executable code, verifier logic, tests, active docs, or navigation docs should depend on old paths.

12. Final verification:
    - Run `python tools/verify_scaffold.py`.
    - Run `pytest`.
    - Run a targeted secret scan before any commit or push.
    - Confirm `git status --short` only shows intended moves/edits.

## Files Expected To Be Touched

High-confidence must-touch files:

- `AGENTS.md`
- `README.md`
- `src/ccc_parser/core.py`
- `tests/test_scaffold_contracts.py`
- `tools/verify_scaffold.py`
- `tools/scaffold_initial_repo.py`
- `docs/source_manifest.md`
- `docs/source_manifest.csv`
- `docs/source_manifest.json`

Moved planning files:

- `docs/planning/source_synthesis.md`
- `docs/plans/parser_mvp_implementation_plan.md`
- `docs/tickets/*`
- `archive/plans/implemented/*`

Moved reference areas:

- `collisionrelateddocs/**`
- `docs/normalized/**`
- `docs/data/**`
- `docs/reference/generated-packs/**`
- `docs/reference/test-context/**` remains under `docs/reference/test-context/**`.

Docs likely needing path edits:

- `docs/roadmap.md`
- `docs/architecture/*`
- `docs/contracts/*`
- `docs/decisions/*`
- `docs/operations/*`
- `docs/security/*`
- `docs/requirements/*`
- `docs/reference/originalplanning_index.md`

## Acceptance Criteria

- No root-level `archive/` or `collisionrelateddocs/` remains.
- No active `docs/planning/`, root `docs/tickets/`, root `docs/normalized/`, or root `docs/data/` remains.
- Active plan work is discoverable from `docs/plans/_index.md`.
- Agent navigation is discoverable from `AGENTS.md`, `docs/docs_index.md`, and `docs/repo_map.json`.
- Scaffold verifier passes with the new paths.
- Pytest passes.
- Manifest files accurately describe every moved raw source, derivative, reference pack, active plan, and archived plan.

## Assumptions

- The raw evidence move is intentional despite its larger blast radius.
- No compatibility symlinks or duplicate old folders will be kept.
- Historical archive files may mention old paths as history, but active instructions must use new paths.
- `originalplanning` is used exactly as requested, with index text clarifying that it contains generated and historical planning packs, not authoritative active plans.
