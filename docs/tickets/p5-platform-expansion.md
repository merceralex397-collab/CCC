# P5 Platform Expansion Tickets

## P5-001 Operations Analytics

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `ce_phase4_agents_reviewed_plan/08_operations_management_intelligence.md`, `collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md`.
- Dependencies: P1/P3 event data.
- Expected outputs: queue metrics, missing-info metrics, parser quality metrics, provider throughput reporting.
- Acceptance criteria: analytics consume canonical work item and audit events rather than scraping mailbox state.
- Verification: metrics definitions and sample dashboard tests.
- Archive target: `archive/plans/implemented/`.

## P5-002 Portal And External API

- Status: parked-planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`, `07_06_api_for_external_partners.md`, `archive/plans/implemented/2026-05-23-implemented-figmaplan.md`, `docs/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`.
- Dependencies: Operational Core, security model, external access approval.
- Expected outputs: option paper and ADR before implementation.
- Acceptance criteria: no external access until auth, audit, retention, and data minimisation are approved; current website portal and payment evidence may inform the design, but external portal/API/payment automation stays parked until governance approval.
- Verification: security review, API tests, and governance sign-off on the portal/payment scope guardrail.
- Archive target: `archive/plans/implemented/` or `archive/plans/superseded/`.

## P5-003 Data Warehouse And Historical Mining

- Status: parked-planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md`, `collision_engineers_bulk_data_research_pack/17_eva_report_mining_and_sentry_bulk_sync.md`.
- Dependencies: canonical events, retention policy, storage decision.
- Expected outputs: data warehouse option paper, retention model, ingestion contract.
- Acceptance criteria: warehouse contains only approved canonical data and package metadata.
- Verification: data map, retention tests, sample reconciliation.
- Archive target: `archive/plans/implemented/` or `archive/plans/superseded/`.

## P5-004 External Ecosystem Integrations

- Status: parked-planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md`, `07_03_audatex_and_estimating_system_partnerships.md`.
- Dependencies: Operational Core maturity and partner agreement.
- Expected outputs: integration option papers and approved ADRs.
- Acceptance criteria: integrations use canonical contracts and cannot bypass review/audit gates.
- Verification: partner sandbox tests and security review.
- Archive target: `archive/plans/implemented/` or `archive/plans/superseded/`.

## P5-005 Portal, Payment, And Messaging Automation Governance

- Status: parked-planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `archive/plans/implemented/2026-05-23-implemented-figmaplan.md`, `docs/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`, `docs/architecture/future_system_convergence.md`.
- Dependencies: P1 metadata capture, P3 intake/storage boundaries, governance approval.
- Expected outputs: ADR and controls for any future external portal/API/payment automation or WhatsApp/send automation.
- Acceptance criteria: no implementation starts until privacy, retention, vendor, payment, and operator-approval controls are agreed; current evidence capture remains distinct from autonomous external actions.
- Verification: governance approval package and updated risk documentation.
- Archive target: `archive/plans/implemented/` or `archive/plans/superseded/`.
