# Collision Command Centre

Collision Command Centre (CCC) is the canonical private repository for rebuilding Collision Engineers' vehicle-damage instruction parser and related evidence-handling foundations.

## Current Scope

The first programme milestone is the Operational Core MVP. The parser is the first executable MVP inside it:

- shared Python parser core;
- non-technical office-staff UI;
- equivalent CLI for automation and AI-agent usage;
- provider/principal admin;
- work-item and review queue;
- provider configuration and coverage tracking;
- EVA-ready JSON/payload validation;
- Box-ready evidence-package generation;
- raw-source preservation with normalized Markdown/metadata companions.

Collision Engineers do not do personal injury or KADOE work. Those workflows must not be planned into CCC.

## Source Of Truth

Raw operational files under `collisionrelateddocs/` remain immutable source evidence. Generated plan packs are reference-only unless promoted into canonical docs or tickets. The current canonical entry points are:

- `docs/source_manifest.md`
- `docs/roadmap.md`
- `docs/planning/source_synthesis.md`
- `docs/plans/parser_mvp_implementation_plan.md`
- `docs/architecture/`
- `docs/contracts/`
- `docs/decisions/`
- `docs/tickets/backlog_index.md`
- `docs/requirements/`
- `docs/data/provider_coverage_matrix.md`
- `docs/reference/generated_packs_index.md`
- `archive/plans/implemented/`

## Local Verification

Run:

```powershell
$py='C:\Users\PC\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $py tools/verify_scaffold.py
```

The verifier checks the promoted planning scaffold, provider coverage evidence, decision docs, parser MVP plan coverage, and source-manifest integrity.
