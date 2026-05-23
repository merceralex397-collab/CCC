# P5 Platform Expansion Tickets

## P5-001 Operations Analytics

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `ce_phase4_agents_reviewed_plan/08_operations_management_intelligence.md`, `collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md`.
- Roadmap milestone: P5 Platform Expansion.
- Dependencies: P1/P3 event data.
- Expected outputs: queue metrics, missing-info metrics, parser quality metrics, provider throughput reporting.
- Acceptance criteria: analytics consume canonical work item and audit events rather than scraping mailbox state.
- Verification required: metrics definitions and sample dashboard tests.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/`.
- Supersedes: none.
- Superseded-by: none.

## P5-002 Portal And External API

- Status: parked-planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md`, `07_06_api_for_external_partners.md`, `docs/plans/operational-core/archived_plans/implemented/2026-05-23-implemented-figmaplan.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`.
- Roadmap milestone: P5 Platform Expansion.
- Dependencies: Operational Core, security model, external access approval.
- Expected outputs: option paper and ADR before implementation.
- Acceptance criteria: no external access until auth, audit, retention, and data minimisation are approved; current website portal and payment evidence may inform the design, but external portal/API/payment automation stays parked until governance approval.
- Verification required: security review, API tests, and governance sign-off on the portal/payment scope guardrail.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/` or `docs/plans/operational-core/archived_plans/superseded/`.
- Supersedes: none.
- Superseded-by: none.

## P5-003 Data Warehouse And Historical Mining

- Status: parked-planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md`, `collision_engineers_bulk_data_research_pack/17_eva_report_mining_and_sentry_bulk_sync.md`.
- Roadmap milestone: P5 Platform Expansion.
- Dependencies: canonical events, retention policy, storage decision.
- Expected outputs: data warehouse option paper, retention model, ingestion contract.
- Acceptance criteria: warehouse contains only approved canonical data and package metadata.
- Verification required: data map, retention tests, sample reconciliation.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/` or `docs/plans/operational-core/archived_plans/superseded/`.
- Supersedes: none.
- Superseded-by: none.

## P5-004 External Ecosystem Integrations

- Status: parked-planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md`, `07_03_audatex_and_estimating_system_partnerships.md`.
- Roadmap milestone: P5 Platform Expansion.
- Dependencies: Operational Core maturity and partner agreement.
- Expected outputs: integration option papers and approved ADRs.
- Acceptance criteria: integrations use canonical contracts and cannot bypass review/audit gates.
- Verification required: partner sandbox tests and security review.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/` or `docs/plans/operational-core/archived_plans/superseded/`.
- Supersedes: none.
- Superseded-by: none.

## P5-005 Portal, Payment, And Messaging Automation Governance

- Status: parked-planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-23.
- Source links: `docs/plans/operational-core/archived_plans/implemented/2026-05-23-implemented-figmaplan.md`, `docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`, `docs/architecture/future_system_convergence.md`.
- Roadmap milestone: P5 Platform Expansion.
- Dependencies: P1 metadata capture, P3 intake/storage boundaries, governance approval.
- Expected outputs: ADR and controls for any future external portal/API/payment automation or WhatsApp/send automation.
- Acceptance criteria: no implementation starts until privacy, retention, vendor, payment, and operator-approval controls are agreed; current evidence capture remains distinct from autonomous external actions.
- Verification required: governance approval package and updated risk documentation.
- Archive target: `docs/plans/operational-core/archived_plans/implemented/` or `docs/plans/operational-core/archived_plans/superseded/`.
- Supersedes: none.
- Superseded-by: none.
