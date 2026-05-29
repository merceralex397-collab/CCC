# Option Paper: External Portal + Partner API (+ Insurer / Audatex)

Status: open (design only — all governance + security gated)
Owner: unassigned
Created: 2026-05-29
Group: business / partners (G5)
Source links: `docs/superpowers/specs/2026-05-29-business-design.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md`

## Context

External-facing systems are the latest, most sensitive scope. All are option-papers with security + access gates; none build until earlier waves + governance are mature.

## Items (each a future governed decision)

1. **Customer self-service portal** — external submission/status; relationship to the `bridge` intake metadata (internal capture is bridge; the external product is here).
2. **External partner API** — partner-facing API with access controls, auth, rate limits, audit.
3. **Insurer platform / structured-feed integration** — inbound/outbound structured feeds.
4. **Audatex/estimating-system partnership discovery** — commercial partnership (distinct from `intelligence/evidence` estimate *parsing*).
5. **Partner access controls + security gates** — the access model underpinning all of the above.

## Decision Criteria

Security/auth/access model; data-sharing + privacy; commercial terms; which partners/insurers; relationship to `bridge` + `intelligence`; build-vs-partner; sequencing after internal platform maturity.

## Governance Gates

All external access + partner APIs + portals + insurer/Audatex partnerships require governance + security sign-off and start as option-papers; no external exposure before internal platform + access controls are proven.

## Open Questions

Portal vs bridge boundary; partner/insurer identities + terms; Audatex partnership scope vs estimate parsing; the access-control/security model.
