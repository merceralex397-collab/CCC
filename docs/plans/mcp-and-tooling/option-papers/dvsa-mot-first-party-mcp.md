# Option Paper: First-Party DVSA-MOT MCP (and Token Rotation)

Status: open (design — not approved for build)
Owner: unassigned
Created: 2026-05-29
Group: mcp-tooling (parallel track)
Source links: `docs/superpowers/specs/2026-05-29-mcp-tooling-design.md`, `docs/plans/mcp-and-tooling/context.md`, `../collisionplugin/connectors/dvladvsa/connectorurl.md`, `docs/plans/vehicle-valuation-data/`

## Immediate Security Action (not optional)

A live bearer token for the existing DVSA-MOT MCP endpoint (`dvsa-mot-mcp.collisionengineers.workers.dev`) is stored **in plaintext** in `../collisionplugin/connectors/dvladvsa/connectorurl.md`. Treat it as **compromised**: rotate it at the endpoint, remove the value from any tracked file, and move it to a secret store. This must happen regardless of whether/when the rebuild proceeds. Owner: CE IT / governance-security.

## Context

A working remote DVSA-MOT MCP already exists (Cloudflare Workers) and is used by the `collisionplugin` valuation/vehicle skills. Decision (2026-05-29): rebuild it as a **first-party CCC-owned MCP server** so CCC controls hosting, auth, rate limits, audit, and DVSA data handling, and registers it behind the gateway.

## Options To Evaluate

1. **CCC-owned Cloudflare Worker MCP** (same platform, CCC-owned + secret-managed). Closest to current; low migration friction.
2. **In-platform MCP service** (part of the CCC backend). Most control + unified audit; more infra.
3. **Keep the current remote endpoint** but CCC-secured (rotate token, restrict, register). Fastest; least ownership — bridge to options 1/2.

## Decision Criteria

DVSA MOT API access terms / licensing and rate limits; hosting + secret management; audit + rate-limit integration with the gateway; latency/cost; migration from the current endpoint without breaking the valuation skill; data-retention/privacy for vehicle data (coordinate `vehicle-valuation-data` + `governance-security`).

## Governance Gates

DVSA data licensing + API-security review; secret handling; no vehicle data retained beyond policy.

## Open Questions

DVSA API key ownership/terms; whether the MOT data is cached and for how long; how the valuation skill is repointed from the old endpoint to the first-party server with zero downtime.
