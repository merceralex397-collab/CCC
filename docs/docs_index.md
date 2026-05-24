# Documentation Index

This is the primary human navigation file for CCC documentation.

## Quick Start

- Product scope and current milestone: `README.md` and `docs/roadmap.md`.
- Plan workspace index: `docs/plans/_index.md`.
- Workspace ownership matrix: `docs/plans/workspace_ownership_matrix.md`.
- Initial setup planning: `docs/plans/initial-repo-setup/README.md`.
- Operational Core coordination: `docs/plans/operational-core/README.md`.
- Active programme source map: `docs/plans/operational-core/source_synthesis.md`.
- Approved folder taxonomy source: `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`.
- Parser MVP plan: `docs/plans/parser-extraction/parser-mvp/plan.md`.
- Parser MVP evidence and divergence review: `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`.
- Active backlog before ticket relocation: `docs/plans/operational-core/tickets/backlog_index.md`.
- Agent path map: `docs/repo_map.json`.
- Full source inventory: `docs/source_manifest.md`, `docs/source_manifest.csv`, and `docs/source_manifest.json`.

## Active Work

| Area | Path | Use |
| --- | --- | --- |
| Plans | `docs/plans/_index.md` | Active plan workspaces and archived plans. |
| Initial Repo Setup | `docs/plans/initial-repo-setup/` | Pre-code repository setup, documentation scaffold, and exhaustive reference idea planning. |
| Operational Core | `docs/plans/operational-core/` | First-slice coordination, source synthesis, and cross-workspace backlog routing. |
| Parser Extraction | `docs/plans/parser-extraction/` | Active parser MVP, extraction rules, provider-rule execution, parser parity, and regression planning. |
| Architecture | `docs/architecture/` | System architecture and programme boundaries. |
| Contracts | `docs/contracts/` | Versioned schemas and integration contracts. |
| Decisions | `docs/decisions/` | ADRs and option papers. |
| Requirements | `docs/requirements/` | Business requirements and open questions. |
| Operations | `docs/operations/` | Runbooks, monitoring, release, rollback, and spreadsheet companion notes. |
| Security | `docs/security/` | Data map, vendor register, DPIA, safety review, and API security. |

## Planning Workspaces

See `docs/plans/_index.md` for the full active workspace table. Each workspace has `README.md`, `source_map.md`, `roadmap.md`, `tickets/`, `option-papers/`, and `archived_plans/`.

## Reference Material

| Area | Path | Use |
| --- | --- | --- |
| Raw evidence | `docs/reference/raw/collisionrelateddocs/` | Immutable source files. Do not edit in place. |
| Normalized companions | `docs/reference/normalized/` | Generated Markdown companions for raw evidence. |
| Reference data | `docs/reference/data/` | Provider matrix and extracted Jam/FigJam derivatives. |
| Original planning | `docs/reference/originalplanning/` | Historical/generated planning packs; reference-only unless promoted. |
| Test context | `docs/reference/test-context/` | Historical test repositories and context packs. |

## Quality Rules

- At task start, read the roadmap, repo map, owning workspace plan, active tickets, and relevant source evidence before changing files.
- At completion of any large task, update `docs/roadmap.md`, the owning plan/ticket, `docs/docs_index.md`, `docs/repo_map.json`, affected key docs, and `docs/source_manifest.*`.
- Update `docs/source_manifest.*` when source files, generated companions, active docs, or archives change.
- Promote ideas from reference material into an owning workspace before treating them as active implementation scope.
- Keep raw evidence immutable and create derivatives under `docs/reference/normalized/` or `docs/reference/data/`.
- Run `python tools/verify_scaffold.py` after documentation structure changes.
