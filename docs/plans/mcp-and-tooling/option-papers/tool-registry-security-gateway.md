# Option Paper: Tool Registry + Security Gateway

Status: open (design — not approved for build)
Owner: unassigned
Created: 2026-05-29
Group: mcp-tooling (parallel track)
Source links: `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md`, `docs/superpowers/specs/2026-05-29-mcp-tooling-design.md`, `docs/architecture/tooling.md`

## Context

As MCP/tools grow (DVSA-MOT, Autotrader, future Outlook/Box/EVA), exposing every tool to every model is risky and inefficient. CCC needs a gateway that registers tools, validates schemas, enforces role/workflow permissions, rate-limits, audits, and exposes only the right subset per skill/agent — vendor-neutral so tools work across the CE platform, Claude, and ChatGPT/Codex.

## Options To Evaluate

1. **Build a thin first-party gateway** over MCP/function tools (`register_tool`, `list_allowed_tools`, `invoke_tool_checked`, `get_tool_audit_log`, `disable_tool`, `simulate_tool_call`). Full control; CE-specific permissions/audit.
2. **Adopt an existing MCP gateway/proxy** and add CE permission/audit on top. Less to build; dependency + fit risk.
3. **Per-front-end native tool config only** (no central gateway). Simplest now; fails the audit/permission/secret-isolation goals as tools grow — likely rejected.

## Decision Criteria

Secret isolation (never returned to agents); role/workflow/work-item permission model; JSON-Schema validation; rate limiting of external APIs; audit completeness; safe discovery / deferred tool loading for large surfaces; vendor neutrality; operational complexity; alignment with the `casework` role model and `governance-security` policy.

## Guardrails

No broad shell/file/DB tools to general agents; dangerous/external-write actions require workflow state + approval; rate-limit external calls; secrets server-side only.

## Governance Gates

Role definitions + API-security review required before build. Build is triggered when the first bridge adapter or first multi-tool agent needs controlled exposure.

## Open Questions

Hosting/runtime; how permissions map to CE roles (depends on `casework`); tool-schema standard; build-vs-adopt for the gateway core.
