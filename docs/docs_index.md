# Documentation Index

This is the primary human navigation file for CCC documentation.

## Quick Start

- Product scope and current milestone: `README.md` and `docs/roadmap.md`.
- Active programme plan: `docs/plans/operational-core/source_synthesis.md`.
- Parser MVP plan: `docs/plans/operational-core/parser-mvp/plan.md`.
- Active backlog: `docs/plans/operational-core/tickets/backlog_index.md`.
- Agent path map: `docs/repo_map.json`.
- Full source inventory: `docs/source_manifest.md`, `docs/source_manifest.csv`, and `docs/source_manifest.json`.

## Active Work

| Area | Path | Use |
| --- | --- | --- |
| Plans | `docs/plans/_index.md` | Active plan workspaces and archived plans. |
| Operational Core | `docs/plans/operational-core/` | Current programme plan, parser MVP plan, and tickets. |
| Architecture | `docs/architecture/` | System architecture and programme boundaries. |
| Contracts | `docs/contracts/` | Versioned schemas and integration contracts. |
| Decisions | `docs/decisions/` | ADRs and option papers. |
| Requirements | `docs/requirements/` | Business requirements and open questions. |
| Operations | `docs/operations/` | Runbooks, monitoring, release, rollback, and spreadsheet companion notes. |
| Security | `docs/security/` | Data map, vendor register, DPIA, safety review, and API security. |

## Reference Material

| Area | Path | Use |
| --- | --- | --- |
| Raw evidence | `docs/reference/raw/collisionrelateddocs/` | Immutable source files. Do not edit in place. |
| Normalized companions | `docs/reference/normalized/` | Generated Markdown companions for raw evidence. |
| Reference data | `docs/reference/data/` | Provider matrix and extracted Jam/FigJam derivatives. |
| Original planning | `docs/reference/originalplanning/` | Historical/generated planning packs; reference-only unless promoted. |
| Test context | `docs/reference/test-context/` | Historical test repositories and context packs. |

## Quality Rules

- Update `docs/source_manifest.*` when source files, generated companions, active docs, or archives change.
- Promote ideas from reference material into `docs/plans/operational-core/tickets/` before treating them as active scope.
- Keep raw evidence immutable and create derivatives under `docs/reference/normalized/` or `docs/reference/data/`.
- Run `python tools/verify_scaffold.py` after documentation structure changes.
