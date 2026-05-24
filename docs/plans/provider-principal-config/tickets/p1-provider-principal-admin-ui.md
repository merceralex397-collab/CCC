# P1-004 Provider Principal Admin UI

- Status: planned.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/contracts/provider_principal_config_contract_v1.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_02_provider_principal_configuration_library.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P0-003 (Provider Coverage Baseline), P0-006 (ADR And Option Paper Baseline), state-store decision.
- Expected outputs: provider/principal admin screens, versioning, activation/rollback, alias management, detection phrase and rule editing, plus optional provider routing metadata controls for `delivery_channel`, `query_owner`, `reply_to_handler`, `reply_all`, `cc_list`, `fee_note_handling`, `garage_figures_rule`, `missing_info_chase_limit`, and `special_case_notes`.
- Acceptance criteria: provider-admin role can create draft config, validate against corpus examples, activate, and roll back with audit events; optional routing metadata and fee-note exceptions for `QDOS`, `QCL`, `AX`, `FW`, `OAK`, and `ALS` can be recorded without making them parser-required or authorizing portal/payment/WhatsApp automation in P1.
- Verification required: provider config regression checks, audit event assertions, and schema/UI checks confirming the optional routing metadata fields and fee-note exceptions are supported.
- Archive target: `docs/plans/provider-principal-config/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p1-operational-core-mvp.md` § P1-004.
- Superseded-by: none.
