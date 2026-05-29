# MCP & Tooling Workspace — Open Questions

Date: 2026-05-29
Status: active open-questions log
Owner: unassigned
Group: mcp-tooling (parallel track)
Source links: `docs/superpowers/specs/2026-05-29-mcp-tooling-design.md`, `docs/plans/mcp-and-tooling/plan.md`, `docs/plans/mcp-and-tooling/context.md`

## Resolved (this interview, 2026-05-29)

- **Focus this iteration?** — Design the registry/security gateway + connector inventory; build deferred.
- **DVSA-MOT?** — Rebuild as a first-party CCC-owned MCP server; rotate the leaked token regardless.
- **Autotrader?** — Defer / keep as a Codex-wrapping connector; a standalone Autotrader MCP is not viable without paying Autotrader API costs.

## Open — action required

1. **ROTATE THE DVSA-MOT TOKEN.** A live bearer token is in plaintext at `../collisionplugin/connectors/dvladvsa/connectorurl.md`. Treat as compromised: rotate at the DVSA-MOT endpoint, scrub the value from any tracked file, move to a secret store. Owner: CE IT / governance-security. This is independent of the rebuild timeline.

## Open — design

2. DVSA first-party MCP hosting: CCC-owned Cloudflare Worker vs in-platform service; DVSA API access terms/licensing.
3. Gateway build trigger: which event justifies building it (first bridge adapter to register? first multi-tool agent?).
4. Vendor-neutral tool-schema standard (MCP/JSON-Schema) so tools are reusable across CE platform / Claude / ChatGPT-Codex.
5. CE role/permission model the gateway enforces — depends on the `casework` role model.
6. Autotrader Codex-connector dependency: what happens to the valuation skill if Codex access changes; is there a fallback?
