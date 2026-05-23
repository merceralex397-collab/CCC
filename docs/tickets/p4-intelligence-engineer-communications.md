# P4 Intelligence, Engineer Pack, And Communications Tickets

## P4-001 Valuation Evidence Support

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md`, `ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md`.
- Dependencies: P1 work item/package, governance review.
- Expected outputs: valuation evidence records, companion report storage, reviewer approval flow.
- Acceptance criteria: valuation evidence can support a case without automatically deciding uplift.
- Verification: package includes companion report and audit events for valuation decisions.
- Archive target: `archive/plans/implemented/`.

## P4-002 DVLA/DVSA And Mileage Evidence

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md`, `04_mileage_estimation_engine.md`, `05_mileage_anomaly_review.md`, `08_dvla_vrm_attribute_cache.md`.
- Dependencies: P1 work item, vendor/API governance.
- Expected outputs: vehicle attribute cache, mileage evidence/conflict model, MOT/DVLA adapter plan.
- Acceptance criteria: factual vehicle and mileage evidence is available to reviewers with confidence and source.
- Verification: API/mock tests, stale-cache tests, conflict warning tests.
- Archive target: `archive/plans/implemented/`.

## P4-003 Image Intelligence And Evidence Matching

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `ce_phase4_agents_reviewed_plan/07_image_review_evidence_quality_and_matching.md`, `collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md`, `11_visible_vrm_and_image_case_matcher.md`.
- Dependencies: P1 package/review, P2 corpus harness.
- Expected outputs: image quality checks, duplicate/reused evidence review, preview-image recommendations, visible VRM hints.
- Acceptance criteria: image intelligence produces review flags, not automatic case decisions.
- Verification: image sample tests and reviewer override audit tests.
- Archive target: `archive/plans/implemented/`.

## P4-004 Engineer Pack Generator

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `phase7_expanded_markdown_plan/additional_items/08_06_engineer_pack_generator_and_template_manager.md`, `ce_system_plans_enhanced/11_WORK_PACKAGE_ENGINEER_PACK_AND_REPORTING.md`.
- Dependencies: P1 Operational Core and package manifest.
- Expected outputs: engineer pack templates, source-linked case summary, evidence bundle.
- Acceptance criteria: pack is generated from reviewed work item and package metadata, with no unreviewed AI assertions.
- Verification: sample pack review, template tests, source-link checks.
- Archive target: `archive/plans/implemented/`.

## P4-005 Communications Drafting

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Sources: `ce_phase4_agents_reviewed_plan/04_missing_information_and_communication.md`, `collision_engineers_ai_tools_plans_markdown/15_missing_info_checker_and_chaser_drafter.md`, `19_ce_style_communications_skill.md`.
- Dependencies: P1 work item states and governance.
- Expected outputs: missing-info draft generation, status update drafts, approval workflow.
- Acceptance criteria: staff approve every outgoing message; no autonomous WhatsApp or email send in this phase without separate approval.
- Verification: draft review tests and audit events.
- Archive target: `archive/plans/implemented/`.

