# MCP & Tooling: Registry/Security Gateway + Connector Strategy — Design

Date: 2026-05-29
Status: approved design (brainstorming output) — design-only this iteration, build deferred
Owner: unassigned
Workspace: `docs/plans/mcp-and-tooling/` (group: mcp-tooling, parallel track)
Source links: `docs/plans/mcp-and-tooling/context.md`, `docs/architecture/tooling.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md`, `docs/superpowers/specs/2026-05-29-bridge-design.md`, `../collisionplugin/connectors/dvladvsa/connectorurl.md`

## Context

mcp-tooling is a parallel track that gives the parser, bridge, skills, and (future) agents a controlled tool surface. It owns the **tool registry + security gateway**, tool schemas/auth/rate-limits/audit/discovery, and the MCP server adapters — but **not** the adapters' business behaviour (`bridge`), agent orchestration (`ai-platform/agents`), or skill content (`agent-skills`). Two connectors already work in practice via `../collisionplugin`: a remote DVSA-MOT MCP and an Autotrader search/capture connector.

## Decisions captured (user, 2026-05-29)

- **Deliver design only this iteration:** the registry/security-gateway design + a connector inventory. Build deferred.
- **DVSA-MOT:** rebuild as a **first-party CCC-owned MCP server** (replacing the Cloudflare Workers endpoint). Independently, **rotate the leaked token now** (treat as compromised) and move secrets to a store.
- **Autotrader:** **defer / keep as a Codex-wrapping connector.** A standalone first-party Autotrader MCP is **not viable** without paying Autotrader API costs; wrapping Codex's existing Autotrader access is the only economic path. Document this as a fixed constraint.

## Goals / Non-goals

**Goals:** a vendor-neutral registry/gateway design (permissions, schema validation, rate limits, audit, safe discovery, secret isolation); a connector inventory with risk levels and adoption decisions; option-papers for the gateway and the DVSA-MOT first-party rebuild.

**Non-goals (this iteration):** building the gateway or any MCP server; reimplementing bridge adapter behaviour; agent orchestration policy; exposing any secret. Personal injury and KADOE remain out of scope.

## Design — Tool Registry + Security Gateway

A gateway sits between AI front ends (CE platform, Claude, ChatGPT/Codex) and the tools, and:

- **Registers** tools with validated JSON schemas (`register_tool`).
- **Authorises** per role/workflow/work-item state (`list_allowed_tools(user, context)`, `invoke_tool_checked(tool, args, user)`); exposes only the appropriate subset per skill/agent.
- **Audits** every invocation (`get_tool_audit_log`); supports `disable_tool(reason)` and `simulate_tool_call` (dry-run).
- **Rate-limits** external APIs; supports tool-search / deferred loading for large tool surfaces.

**Guardrails (firm):** no broad shell/file/DB tools to general agents; **secrets never returned to agents/models** (held server-side, injected by the gateway); dangerous/external-write actions require explicit workflow state + approval; rate-limit all external calls.

**Vendor-neutral requirement:** tools must be reusable across approved AI front ends, so the registry standardises on MCP/JSON-Schema tool definitions rather than a single vendor's connector format — matching the cross-AI-portability theme of `agent-skills`.

## Connector Strategy

| Connector | Decision | Notes |
| --- | --- | --- |
| DVSA-MOT | **Rebuild first-party MCP**; rotate token now | Option-paper `option-papers/dvsa-mot-first-party-mcp.md`. DVSA data licensing + hosting (CCC-owned Worker vs in-platform) decided there. |
| Autotrader | **Keep as Codex-wrapping connector** (deferred) | Standalone MCP not viable (Autotrader API cost). Register/document the Codex connector; the `agent-skills` valuation skill keeps using it. |
| Outlook Graph / Box / EVar/Sentry | Plan only | Wrap the `bridge` adapters once they exist; gated by the bridge's option-papers. |
| DVLA VRM, observability | Plan only (S4) | Read-only helpers behind the registry. |

## Sequencing

1. Rotate the DVSA-MOT token (immediate governance action — owner: CE IT / governance-security).
2. Write the gateway design + connector-inventory option-papers (this iteration).
3. Build the registry/gateway and the first-party DVSA-MOT MCP only after governance sign-off and once at least one bridge adapter is ready to register.

## Acceptance Criteria (for the design this iteration)

- Gateway option-paper specifies the permission model, schema standard, audit, rate limits, secret isolation, and deferred-loading approach, with decision criteria and governance gates.
- Connector inventory records each connector's status, risk, and adoption decision; the DVSA token-rotation action is recorded and owned.
- DVSA first-party-rebuild option-paper covers hosting, DVSA licensing, token/secret handling, and migration from the current remote endpoint.
- Autotrader's Codex-wrapping constraint is documented as fixed.

## Risks & Open Questions

- The DVSA-MOT token is exposed in `collisionplugin` — must be rotated regardless of the rebuild timeline.
- Gateway adds complexity; needs clear CE role definitions (depends on `casework`/governance role model).
- DVSA API access terms/licensing for a first-party server.
- When to trigger the gateway build (likely when the first bridge adapter or the first multi-tool agent appears).
