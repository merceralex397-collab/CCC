# Option Paper: Spreadsheet / Job-Sheet Transition Bridge

Status: open (design only — not approved for build)
Owner: unassigned
Created: 2026-05-29
Group: bridge / intake (G2)
Source links: `docs/operations/job_sheet_spreadsheet_companion.md`, `docs/reference/data/provider_coverage_matrix.md`, `docs/superpowers/specs/2026-05-29-bridge-design.md`, `docs/reference/raw/collisionrelateddocs/collision_releated/Backup of CE Job Sheet 260309.xlsm`

## Context

CE currently runs operations from the legacy CE Job Sheet workbook (Jobs / Principals / Garages sheets) plus `Mapped Principals.xlsx`. This paper evaluates a transition bridge from that workbook to CCC work-item state, so the spreadsheet can eventually be retired without losing the operational queue, principal lookup, or garage/inspection-contact data.

## Options To Evaluate

1. **One-way import** of current workbook state into work items (snapshot migration), then operate in CCC.
2. **Read-only sync companion** — keep the workbook authoritative for a transition period; CCC reads it for triage but does not write back.
3. **Two-way sync** — highest risk (macro side effects, conflicts); likely rejected.

## Decision Criteria

No macro execution during analysis; preserve raw workbook files unchanged (derivatives only); map Jobs → work items, Principals → provider/principal config (coordinate with `parser/providers`), Garages → inspection-contact lookup; reconcile with the provider coverage matrix; staff adoption and fallback; decommissioning gate owned by `operations-quality`.

## Governance Gates

Operationally sensitive data (garage contacts, principal mappings) — privacy/retention review. Legacy decommissioning is a controlled release milestone, not an MVP side effect.

## Open Questions

Authoritative-source ownership during transition; principal-code yearly reset as a controlled reference generator (not a spreadsheet side effect); overlap with `casework` work-item state and `parser/providers` config ownership.
