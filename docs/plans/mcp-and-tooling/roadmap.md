# MCP And Tooling Roadmap

Date: 2026-05-24
Status: active workspace roadmap
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/architecture/tooling.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: governance-security, intake-storage-integrations, vehicle-valuation-data, ai-agents
Expected outputs: phased promotion sequence for `docs/plans/mcp-and-tooling/`
Acceptance criteria: roadmap stages cite source-backed workspace scope and do not duplicate another workspace's primary ownership
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/mcp-and-tooling/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## S3

- Plan domain MCP wrappers around approved adapters without exposing secrets or bypassing review.

## S4

- Add observability, DVLA/DVSA, and controlled read-only helper tools behind the registry.

## S5-S6

- Use gateway permissions, audit, and rate limits before agents or external partners can call tools.

## Promotion Gate

Any item promoted from this roadmap must cite `source_map.md`, name dependencies, define acceptance criteria, and state whether governance/security or operations-quality approval is required.
