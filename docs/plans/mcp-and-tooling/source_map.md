# MCP And Tooling Source Map

Date: 2026-05-24
Status: active source map
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/architecture/tooling.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: governance-security, intake-storage-integrations, vehicle-valuation-data, ai-agents
Expected outputs: source-to-plan traceability for `docs/plans/mcp-and-tooling/`
Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/mcp-and-tooling/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/architecture/tooling.md` | Current tooling architecture summary. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md` | EVA/Sentry API MCP plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md` | Outlook Graph intake MCP plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md` | Box storage metadata MCP plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md` | Tool registry and MCP security gateway plan. |

## Ownership Boundary

Primary ownership:

- EVA/Sentry, Outlook Graph, Box, DVLA/DVSA, spreadsheet, observability, and gateway MCP plans
- tool schemas, auth boundaries, rate limits, audit, and safe discovery
- tool registry and security gateway

Explicit exclusions:

- domain adapter business behavior
- agent orchestration policy
- portable natural-language skill content

## Cross-Link Rules

- Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
- Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
- Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
- Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
