# Governance Security Workspace

## Purpose

This workspace owns all planning for DPIA, vendor governance, privacy, PII redaction, data licensing, expert-boundary rules, API security, retention policy, and audit identity.

## Scope Rules

- Governance-gated areas must start in `option-papers/` before promotion to tickets.
- Personal injury and KADOE are out of scope — any future change to this scope boundary requires a written governance decision.
- Cloud OCR/document intelligence requires privacy, cost, data-residency, and vendor review before use.
- No secrets, API keys, tokens, OAuth material, mailbox credentials, or provider credentials are committed to the repository.

## Evidence Sources

| Source | Key Facts |
| --- | --- |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_12_security_dpia_and_vendor_governance.md` | Security, DPIA, and vendor governance design. |
| `docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/10_security_governance_audit.md` | Security, governance, and audit requirements. |
| `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md` | Monitoring, runbooks, and release management. |
| `docs/architecture/governance_security.md` | Current governance/security architecture. |

## Workspace Layout

- `README.md` — this file
- `tickets/` — active tickets (only after option-paper approval)
- `option-papers/` — DPIA, vendor governance, cloud data-intelligence proposals
- `archived_plans/` — implemented and superseded plans
