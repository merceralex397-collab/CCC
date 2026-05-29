# Intelligence Workspace — Open Questions

Date: 2026-05-29
Status: active open-questions log
Owner: unassigned
Group: intelligence (G3-G4)
Source links: `docs/superpowers/specs/2026-05-29-intelligence-design.md`, `docs/plans/intelligence/plan.md`, `docs/plans/intelligence/context.md`

## Resolved (this interview, 2026-05-29)

- **Depth?** — Design + boundaries + governance option-papers; build deferred until parser/casework/DVSA land.
- **Lead sub-area?** — `vehicle`.
- **Vehicle data?** — Three-pronged: keep live-fetch (DVSA-MOT + Autotrader) **and** build a CCC valuation/MOT evidence store over time **and** research & develop the CCC valuation methodology.

## Open

1. **Data licensing/retention** for DVLA/DVSA/MOT + market evidence in a CCC store (governance-security); how long evidence is retained and at what granularity.
2. **Evidence store vs analytics boundary** — the store accumulates reviewed evidence without becoming an ungoverned warehouse (`analytics-data-platform`).
3. **Valuation methodology ownership** — who owns/signs off the CCC methodology and its evolution (it is expert IP encoded by the valuation skill).
4. **Live-fetch vs stored consistency** — the same VRM fetched at different times can differ; how the store reconciles/versions evidence.
5. **Audatex/ABP positioning** — keeping estimate-review commentary factual and defensible, clear of commercial-partnership scope.
6. **Skill vs workflow boundary** in practice — confirm with `agent-skills` where each valuation/estimate/report skill ends and the intelligence workflow begins.
