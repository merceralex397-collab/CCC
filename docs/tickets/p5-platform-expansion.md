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
- Sources: `phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`, `07_06_api_for_external_partners.md`.
- Dependencies: Operational Core, security model, external access approval.
- Expected outputs: option paper and ADR before implementation.
- Acceptance criteria: no external access until auth, audit, retention, and data minimisation are approved.
- Verification: security review and API tests.
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

