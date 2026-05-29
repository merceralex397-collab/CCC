# MCP And Tooling Plan

Date: 2026-05-29
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-29
Group: mcp-tooling
Wave: parallel (alongside G1 parser / G2 bridge)
Layer: ai-tooling
Source links: `docs/plans/mcp-and-tooling/context.md`, `docs/superpowers/specs/2026-05-29-mcp-tooling-design.md`, `docs/architecture/tooling.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md`
Roadmap milestone: parallel track (ai-tooling)
Dependencies: governance-security, intake-storage-integrations (bridge), vehicle-valuation-data, agent-skills, ai-agents
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/mcp-and-tooling/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/mcp-and-tooling/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

This is the **mcp-tooling** broad workspace (group `mcp-tooling`, a parallel track developed alongside the parser and bridge). It owns the tool registry + security gateway and the MCP server adapters; it wraps approved adapters and never exposes secrets. See `docs/plans/_groups.md`.

## This Iteration — Design Only

Approved design: `docs/superpowers/specs/2026-05-29-mcp-tooling-design.md`. Decisions (2026-05-29): deliver the registry/gateway **design** + connector inventory (build deferred); **rebuild DVSA-MOT as a first-party MCP** (rotate the leaked token now); **keep Autotrader as a Codex-wrapping connector** (standalone MCP not economically viable).

Deliverables: this plan, `context.md`, `open-questions.md`, and two option-papers — `option-papers/tool-registry-security-gateway.md`, `option-papers/dvsa-mot-first-party-mcp.md`.

## Connector Inventory (summary)

| Connector | Decision |
| --- | --- |
| DVSA-MOT MCP | Rebuild first-party; **rotate exposed token now**; register with rate-limit + audit. |
| Autotrader | Keep as Codex-wrapping connector (API-cost constraint); register/document. |
| Outlook Graph / Box / EVA/Sentry | Plan only; wrap the `bridge` adapters once built + governance-approved. |
| DVLA VRM, observability | Plan only (later read-only helpers behind the registry). |

## Sequential Plan

### Now (parallel with parser/bridge)
- [ ] Rotate the DVSA-MOT token (CE IT / governance-security) — immediate.
- [ ] Write the gateway and DVSA-rebuild option-papers; record the connector inventory.

### Next
- [ ] Build the registry/gateway + first-party DVSA-MOT MCP after governance sign-off and once a bridge adapter is ready to register.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `governance-security` | Secret handling, vendor/API-security, DVSA licensing, autonomous-action gates. |
| `bridge` (intake-storage-integrations) | Owns the Outlook/Box/EVA adapter behaviour that mcp-tooling wraps as tools. |
| `vehicle-valuation-data` / `agent-skills` | Consumers of the DVSA/Autotrader tools; valuation skill already uses them. |
| `ai-platform/agents` | May only call approved tools under the gateway's permission + audit. |

## Non-Overlap Rules

Does not own: domain adapter business behaviour (`bridge`); agent orchestration (`ai-platform/agents`); portable skill content (`agent-skills`). Personal injury and KADOE remain out of scope.

## Promotion Gates

- `option-papers/` holds the gateway and DVSA-rebuild designs; promotion to build tickets requires governance-security sign-off.
- Secrets never committed; the DVSA token rotation is a precondition, not optional.
- No tool may bypass review/approval gates for external writes.
