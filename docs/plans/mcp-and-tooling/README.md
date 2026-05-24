# MCP And Tooling Workspace

## Purpose

This workspace owns all planning for MCP servers, internal tool adapters, tool registry, tool schemas, audit trail, rate limits, and security gateway for the CCC tooling layer.

## Scope Rules

- MCP tools must be registered and pass security gateway review before use.
- Rate limits and audit must be implemented before any MCP tool interacts with external providers.
- Personal injury and KADOE are out of scope.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md` | AI tools phase plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md` | Box storage metadata MCP design. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/` | CE tool plans covering MCP, registry, and security gateway. |

## Workspace Layout

- `README.md` — this file
- `tickets/` — active tickets
- `option-papers/` — tool registry and security gateway proposals
- `archived_plans/` — implemented and superseded plans
