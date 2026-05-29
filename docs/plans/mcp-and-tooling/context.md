# MCP & Tooling Workspace — Context (Information Document)

Date: 2026-05-29
Status: active context document
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: mcp-tooling (parallel track, layer: ai-tooling) — see `docs/plans/_groups.md`
Source links: `docs/plans/mcp-and-tooling/plan.md`, `docs/architecture/tooling.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md`, `../collisionplugin/connectors/dvladvsa/connectorurl.md`
Purpose: consolidate what is known about CCC's tool/MCP layer so the interview can focus on the registry/gateway design and how to adopt the connectors that already exist.

## What this workspace owns

The MCP/tool layer: MCP servers and tool adapters (EVA/Sentry, Outlook Graph, Box, DVLA/DVSA, spreadsheet, observability), tool schemas, auth boundaries, rate limits, audit, safe discovery, and the **tool registry + security gateway**. It is a **parallel track** that runs alongside the parser and bridge and serves them.

It does **not** own: domain adapter *business behaviour* (the `bridge` owns Outlook/Box/EVA adapter logic); agent orchestration policy (`ai-platform/agents`); portable natural-language skill content (`agent-skills`). The rule is: **mcp-tooling wraps approved adapters as tools; it does not reimplement them or expose secrets.**

## Current state

- No MCP servers are built in-repo yet (`tickets/` empty). Reference plans exist (registry/gateway, EVA/Sentry, Outlook, Box MCPs).
- `docs/architecture/tooling.md` defines the local-first extraction stack and notes MCP servers wrap adapters; OCRmyPDF appears there as "optional batch normalization" (consistent with the parser iteration decision).
- Two connectors already work in practice (via `../collisionplugin`, the agent-skills raw material):

### Connector inventory

| Connector | What it is | Used by | Status / action |
| --- | --- | --- | --- |
| **DVSA-MOT MCP** | Live remote MCP at `dvsa-mot-mcp.collisionengineers.workers.dev/mcp` (Cloudflare Workers), bearer-token auth | `collisionplugin` valuation/vehicle skills | **GOVERNANCE: token is in plaintext in `connectorurl.md` — rotate (treat as compromised) and move to a secret store; then register in the gateway with rate limits + audit.** |
| **Autotrader search/capture** | Codex app connector (`mcp__codex_apps__autotrader._search_cars`, advert page capture) | `collisionplugin` vehicle-valuation skill | Decide: keep as Codex connector + register/document, or formalise as a first-party MCP server. |
| Outlook Graph (future) | Wrap the `bridge` intake adapter as a tool | future agents | Plan only; build after the bridge intake adapter exists. |
| Box (future) | Wrap the `bridge` storage adapter | future agents | Plan only; gated by live-Box option-paper. |
| EVA/Sentry (future) | Wrap the `bridge` eva adapter | future agents | Plan only; gated by EVA submission option-paper. |
| DVLA VRM, observability (future) | Read-only helpers behind the registry | skills/agents | Plan only (S4). |

## Tool registry + security gateway (reference shape, ref 29)

A gateway that registers tools, validates schemas, enforces role/workflow permissions, records invocations, rate-limits, and exposes only the appropriate tool subset per skill/agent. Candidate methods: `register_tool`, `list_allowed_tools(user, context)`, `invoke_tool_checked(tool, args, user)`, `get_tool_audit_log`, `disable_tool`, `simulate_tool_call`. Guardrails: **no broad shell/file/DB tools to general agents; secrets never returned to agents/models; rate-limit external APIs; dangerous actions require workflow state/approval; use tool-search/deferred loading for large tool surfaces.**

Note: the existing connectors are vendor-specific (Cloudflare Workers MCP; OpenAI/Codex app connector). The registry/gateway should be **vendor-neutral** so tools are reusable across approved AI front ends (CE platform, Claude, ChatGPT/Codex) — matching the cross-AI-portability theme of `agent-skills`.

## Dependencies

`governance-security` (vendor/privacy/API-security, secret handling, autonomous-action gates); `bridge` (adapters to wrap); `vehicle-valuation-data` / `agent-skills` (consumers of DVSA/Autotrader tools); `ai-platform/agents` (only call approved tools under permission/audit).

## Guardrails

Wrap approved adapters only; never expose secrets; adapter business behaviour stays in `bridge`. No autonomous external action without approval gates. Personal injury and KADOE remain out of scope.

## Open design questions for the interview

1. Primary deliverable this iteration: design the registry/security gateway, inventory/adopt the existing connectors, or both?
2. DVSA-MOT MCP: adopt the existing remote server (rotate token, secret handling, register) or rebuild first-party?
3. Autotrader: keep as Codex connector (registered) or formalise as a first-party MCP server?
4. Build a minimal registry/gateway now, or design-only (spec + option-paper) with build deferred?
