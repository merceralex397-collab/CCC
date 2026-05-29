# Intake Storage Integrations Plan (Bridge)

Date: 2026-05-29
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-29
Group: bridge
Wave: G2 (spine)
Layer: integrations
Source links: `docs/plans/intake-storage-integrations/context.md`, `docs/superpowers/specs/2026-05-29-bridge-design.md`, `docs/contracts/evidence_package_contract_v1.md`, `docs/contracts/storage_adapter_contract_v1.md`, `docs/contracts/eva_export_contract_v1.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md`, `docs/reference/raw/collisionrelateddocs/collision_releated/Sentry_API_Complete_Guide.md`
Roadmap milestone: G2 bridge (spine)
Dependencies: case-workflow-state (casework), mcp-and-tooling (mcp-tooling), governance-security, operations-quality
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/intake-storage-integrations/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/intake-storage-integrations/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

This is the **bridge** broad workspace (group `bridge`, wave G2, second in the development spine). It owns the adapter boundaries between CCC's reviewed parser output and the outside systems, split into three sub-areas: `intake` (Outlook/Graph), `storage` (Box), `eva` (EVA/Sentry). See `docs/plans/_groups.md`.

## This Iteration — Staged Bridge

Approved design: `docs/superpowers/specs/2026-05-29-bridge-design.md`. Decisions (2026-05-29): build read-only Outlook intake; keep Box `package_only` and EVA export-only; option-papers (not built) for the three live writes.

| Sub-area | This iteration | Touch points |
| --- | --- | --- |
| `intake` | **Build** read-only Outlook intake: delta-query polling, app-only `Mail.Read` scoped via App RBAC to `desk@`/`engineers@`/`info@`/`digital@`; email → work item + source manifest; preserve originals; dedup on `internetMessageId`+checksums; attachments via existing `src/ccc_parser/readers.py` triage; never delete source mail. | Ticket `tickets/p3-outlook-intake-adapter.md` |
| `storage` | **Gated** — keep `package_only` (`src/ccc_parser/packaging.py`). | Option-paper `option-papers/live-box-upload-adapter.md` |
| `eva` | **Gated** — keep export-only (`src/ccc_parser/exporters/eva.py`). | Option-paper `option-papers/eva-sentry-submission-adapter.md` |

Plus option-paper `option-papers/spreadsheet-job-sheet-bridge.md`.

## Outlook Intake — Microsoft Graph Decisions (grounded)

Delta-query polling (not webhooks) for the MVP; app-only `Mail.Read`/`Mail.ReadBasic` scoped via Role Based Access Control for Applications (legacy `New-ApplicationAccessPolicy` avoided); preserve original `.eml`/`.msg` + attachments; de-duplicate on `internetMessageId` + content checksums; mark processed via category/move, never delete. Citations in `context.md` and the spec.

## Sequential Plan

### S1 (now)
- [ ] Coordinate a minimal work-item/review target with `casework`.
- [ ] Build the Outlook intake adapter (delta-query polling, App-RBAC-scoped) with dedup + idempotency + mocked-Graph tests.

### S2
- [ ] Write the three governed option-papers (live Box upload, EVA/Sentry submission, spreadsheet bridge).

### S3+
- [ ] Promote an option-paper to a build ticket only after governance-security sign-off and a proven intake + review path.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `casework` (case-workflow-state) | Work-item/review is the source of truth intake attaches to; its contract is a hard dependency. |
| `governance-security` | Graph vendor/privacy/API-security sign-off (live PII email read); approval gates for any future live write. |
| `operations-quality` | Sandbox tests, runbooks (`outlook-intake-stopped`, `box-upload-failure`, `eva-rejected-payload`), rollout gates. |
| `mcp-tooling` | Later wraps these adapters as MCP tools; adapter behaviour stays here, tool exposure there. |

## Non-Overlap Rules

Does not own: the external customer portal product; payment automation; MCP tool exposure; work-item state/review internals; parser extraction. Personal injury and KADOE remain out of scope.

## Source Ownership Rules

- Cite the contracts and spec in every promoted ticket or option paper.
- Keep adapter behaviour separate from MCP exposure.
- Do not edit raw evidence under `docs/reference/raw/collisionrelateddocs/`.

## Promotion Gates

- `tickets/` holds implementation-ready work (the intake adapter ticket).
- `option-papers/` holds the three live-write designs; promotion to a build ticket requires governance-security sign-off.
- No autonomous EVA/Sentry submit, live Box write, payment chasing, or WhatsApp send without explicit approval gates.
