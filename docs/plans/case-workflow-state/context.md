# Casework Workspace — Context (Information Document)

Date: 2026-05-29
Status: active context document
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Group: casework (G2–G3, layer: operational) — see `docs/plans/_groups.md`
Source links: `docs/plans/case-workflow-state/plan.md`, `docs/contracts/work_item_contract_v1.md`, `docs/contracts/review_audit_event_contract_v1.md`, `docs/architecture/mvp_interlock.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_01_work_item_state_store_and_job_sheet_replacement.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md`, `src/ccc_parser/ui/app.py`
Purpose: consolidate what is known about the case/work-item layer so the interview can focus on the build scope — especially the minimal work-item/review target the bridge intake adapter hard-depends on.

## What this workspace owns

The operational spine between parser output and export/packaging: **state** (work-item lifecycle, review queue, holding pen, missing-info state machine, audit stream, duplicate/merge/link/split, historical search), **ui** (the human review/dashboard surfaces), and **automation** (deterministic triggers/queues/retries/exception routing). Absorbs `case-workflow-state` (state), `user-experience-interfaces` (ui), `automation-centre` (automation).

It does **not** own: parser extraction internals (`parser`); live Outlook/Box/EVA adapters (`bridge`); MCP exposure (`mcp-tooling`).

## Current state — the model is specified by contracts; the store is not built

`work_item_contract_v1.md` already defines:
- **Identity**: `work_item_id`, `case_po`, `claim_reference`, `principal_code`, `vrm`, `created_at/by`, `status`.
- **Lifecycle**: `draft → needs_evidence / needs_instruction → ready_to_parse → parsed → in_review → ready_for_export → exported → packaged`, plus `blocked` and `archived`.
- **Relationships**: `source_file_ids`, `parser_run_ids`, `review_event_ids`, `package_ids`, `export_ids`.
- **Bridge-aware source metadata** (already in the contract): `source_channel`, `source_category`, `source_labels`, `portal_submission_id`, `payment_status`, `payment_chaser_sent`, `box_folder_url`, `box_folder_stage`, `local_network_folder_url`, `closed_file_reason`.
- **Validation gates**: can't reach `ready_for_export` without reviewed principal/dates/inspection-address-or-image-marker/VRM and resolved critical warnings; can't be `packaged` without manifest + image order; can't `archive` with unresolved blockers unless a reason is recorded.

`review_audit_event_contract_v1.md` defines an append-only event stream (envelope + types incl. `field_corrected`, `warning_overridden`, `status_changed`, `eva_json_exported`, `integration_attempted`, `integration_failed`); critical-warning overrides need reviewer role + reason.

**Not built:** the work-item store/service, the review queue, the missing-info state machine, and the UI over them. The parser Tk UI (`src/ccc_parser/ui/app.py`) already does field review/correction but operates per-file, not over a persistent work-item queue.

## The bridge dependency (why this is next)

The bridge Outlook intake adapter needs a **minimal work-item target**: a create API, the lifecycle entry states (`needs_evidence`/`needs_instruction`/`ready_to_parse`), the source-metadata fields (already in the contract), and the `work_item_created` / `file_added` / `integration_attempted` audit events. The contract already accommodates all of this — the work is to implement the store + queue.

## Sub-areas

- `state` (← case-workflow-state): work-item store, review queue, missing-info machine, audit, dedup/merge (later), historical search (later, contract defers to S5).
- `ui` (← user-experience-interfaces): dashboard/holding-pen/review screens — thin over work-item services; per the parser decision, likely extends the Tk staff UI.
- `automation` (← automation-centre): deterministic triggers/retries/exception routing — later; not the MVP priority.

## Dependencies

`parser` (feeds the review queue; shares the canonical result contract); `bridge` (intake creates work items); `provider-principal-config` (principal/routing on the work item); `governance-security` (role model, audit, retention); `operations-quality` (queue health metrics, rollout).

## Guardrails

Append-only audit; human review is the gate before export/package; reviewed data gates all downstream; UI stays thin over work-item services; no autonomous actions. Personal injury and KADOE remain out of scope.

## Open design questions for the interview

1. Build scope this iteration: the minimal work-item store + review queue (the bridge/parser dependency), the full state model (incl. duplicate/merge/link/split + historical search), or UI-first?
2. Work-item store implementation: a local SQLite store, a JSON/file store, or defer the tech to an option-paper?
3. UI: extend the existing parser Tk UI with the work-item queue/holding-pen, a separate casework UI, or service/CLI-first?
4. Is the `automation` sub-area in scope now, or deferred until work-item state + review are proven?
