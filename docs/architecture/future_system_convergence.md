# Future System Convergence

This document keeps future ideas aligned with the Operational Core without pretending they are part of the first parser runtime build.

## Convergence Spine

All future modules should attach to the same spine:

1. Work item.
2. Source files and evidence.
3. Canonical parser result.
4. Review/audit events.
5. Provider/principal configuration.
6. Evidence package.
7. Export/integration adapters.

If a future module cannot read or write through that spine, it should not be built until its contract is clarified.

Current operational evidence already reaches beyond Outlook email alone: website portal/payment status, WhatsApp traffic, Box request folders, and local network folder links are part of the real workflow evidence. They should attach to the same work-item/source/evidence spine now as metadata, while automation stays gated by later approvals.

## Future Streams

| Stream | Phase | Convergence Rule |
| --- | --- | --- |
| Outlook intake | P3 | Create work items and source manifests; do not bypass review. |
| Website portal/payment evidence | P3 boundary, P5 automation | Record current submission/payment metadata on the work item and evidence package, but keep portal/payment automation out of MVP. |
| WhatsApp evidence context | P3 boundary, P4/P5 automation | Preserve WhatsApp as a current source/evidence channel without adding autonomous sending or scraping in MVP. |
| Live Box upload | P3 | Upload the same package that local generation already builds. |
| EVA/Sentry API adapter | P3 | Submit reviewed/exportable data only; keep manual approval and token handling separate from parser. |
| Valuation support | P4 | Store valuation evidence and companion reports; no automatic uplift decisions without reviewer approval. |
| Mileage/DVLA/DVSA support | P4 | Cache factual vehicle/mileage evidence and expose confidence/conflicts. |
| Image intelligence | P4 | Check quality, ordering, duplicate evidence, and visible VRM where useful; do not replace staff review. |
| Engineer pack | P4 | Generate pack from reviewed work item, source evidence, and provider config. |
| Communications | P4 | Draft missing-info and status messages; staff approve before sending. |
| Analytics | P5 | Consume audit/work-item events, not raw mailbox scraping. |
| Portal/API | P5 | Expose reviewed workflow states and packages through controlled external interfaces. |
| Data warehouse | P5 | Use canonical event and package metadata after retention/security model is approved. |

## Scope Guardrail

Portal/payment scope guardrail: current portal, payment, Box, and WhatsApp findings should be modeled as source/evidence metadata and governance inputs first. They do not authorize autonomous sending, autonomous payment chasing, autonomous WhatsApp messaging, or parser-owned checkout/portal behavior in P1.

## Parked Items

The following ideas are intentionally parked until the core workflow is live and measurable:

- predictive engineer scheduling;
- external partner APIs;
- insurer platform integrations;
- Audatex partnership workflows;
- broad RAG/report-clause systems;
- autonomous portal/payment actions;
- autonomous client communications;
- autonomous EVA submission;
- data warehouse and broad BI outside operational metrics.
