# MCP And Tooling Planning

Date: 2026-05-24
Status: active planning workspace
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/architecture/tooling.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: governance-security, intake-storage-integrations, vehicle-valuation-data, ai-agents
Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `docs/plans/mcp-and-tooling/`
Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/mcp-and-tooling/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

MCP servers, internal tool adapters, registry, schemas, gateway controls, and safe tool discovery planning.

## Main Plan

- Detailed workspace plan: `plan.md`
- Source map: `source_map.md`
- Workspace roadmap: `roadmap.md`

## Owns

- EVA/Sentry, Outlook Graph, Box, DVLA/DVSA, spreadsheet, observability, and gateway MCP plans
- tool schemas, auth boundaries, rate limits, audit, and safe discovery
- tool registry and security gateway

## Does Not Own

- domain adapter business behavior
- agent orchestration policy
- portable natural-language skill content

## Citeable Source Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/architecture/tooling.md` | Current tooling architecture summary. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md` | EVA/Sentry API MCP plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md` | Outlook Graph intake MCP plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md` | Box storage metadata MCP plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md` | Tool registry and MCP security gateway plan. |

## Cross-Workspace Dependencies

- governance-security
- intake-storage-integrations
- vehicle-valuation-data
- ai-agents

## Planning Rules

- Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
- Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
- Archive implemented or superseded work under this workspace's `archived_plans/`.
- Keep raw evidence immutable; cite source paths instead of copying raw content.
