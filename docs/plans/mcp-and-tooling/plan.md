# MCP And Tooling Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/architecture/tooling.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: governance-security, intake-storage-integrations, vehicle-valuation-data, ai-agents
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/mcp-and-tooling/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/mcp-and-tooling/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/mcp-and-tooling/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/architecture/tooling.md` | Current tooling architecture summary. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md` | EVA/Sentry API MCP plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md` | Outlook Graph intake MCP plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md` | Box storage metadata MCP plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md` | Tool registry and MCP security gateway plan. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] EVA/Sentry, Outlook Graph, Box, DVLA/DVSA, spreadsheet, observability, and gateway MCP plans | `docs/architecture/tooling.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md` | `governance-security`, `intake-storage-integrations`, `vehicle-valuation-data`, `ai-agents` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] tool schemas, auth boundaries, rate limits, audit, and safe discovery | `docs/architecture/tooling.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md` | `governance-security`, `intake-storage-integrations`, `vehicle-valuation-data`, `ai-agents` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] tool registry and security gateway | `docs/architecture/tooling.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md` | `governance-security`, `intake-storage-integrations`, `vehicle-valuation-data`, `ai-agents` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S3

- [ ] Plan domain MCP wrappers around approved adapters without exposing secrets or bypassing review.

### S4

- [ ] Add observability, DVLA/DVSA, and controlled read-only helper tools behind the registry.

### S5-S6

- [ ] Use gateway permissions, audit, and rate limits before agents or external partners can call tools.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `intake-storage-integrations` | Outlook, Box, EVA/Sentry, website/WhatsApp, and spreadsheet bridges own live system boundaries and source capture. |
| `vehicle-valuation-data` | Vehicle facts and valuation evidence need licensing, confidence, provenance, and human review boundaries. |
| `ai-agents` | Workflow agents can only call approved tools/skills under permission, audit, and human-approval boundaries. |

## Non-Overlap Rules

The workspace explicitly does not own:

- domain adapter business behavior
- agent orchestration policy
- portable natural-language skill content

If a proposed ticket touches one of those exclusions, link to the owning workspace and keep this workspace as a supporting dependency only.

## Source Ownership Rules

- Cite the source paths above in every promoted ticket, option paper, or roadmap change.
- Use `source_map.md` to explain how the evidence supports the workspace boundary.
- Keep generated and historical planning packs reference-only until a scoped ticket or option paper promotes them.
- Do not edit raw evidence under `docs/reference/raw/collisionrelateddocs/`; create derivatives only under documented derivative paths.

## Promotion Gates

- Use `tickets/` for implementation-ready work with acceptance criteria and verification.
- Use `option-papers/` before vendor, privacy, external access, autonomous send, payment automation, AI/RAG, cloud OCR/document intelligence, commercial data, or partner/API work.
- Link governance/security approval where privacy, vendor, retention, licensing, expert-boundary, API security, or autonomous-action risk exists.
- Link operations-quality approval where release, rollback, regression, monitoring, runbook, support, pilot, or decommissioning evidence is needed.
