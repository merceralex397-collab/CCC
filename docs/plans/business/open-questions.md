# Business Workspace — Open Questions

Date: 2026-05-29
Status: active open-questions log
Owner: unassigned
Group: business (G5)
Source links: `docs/superpowers/specs/2026-05-29-business-design.md`, `docs/plans/business/plan.md`, `docs/plans/business/context.md`

## Resolved (this interview, 2026-05-29)

- **Depth?** — Design + option-papers across all four; build deferred.
- **Flesh out most?** — analytics + finance.
- **Finance fee-note/invoice?** — Plan as a near-term `ce-branding`-based skill over work-item payment metadata.

## Open

1. **Fee rules** — the actual fee/fee-note rules (per provider/principal?) the finance skill applies; source of truth (coordinate `parser/providers`).
2. **Finance doc dependencies** — fee-note/invoice generation needs `agent-skills` ce-branding + `casework` work-item payment metadata first; sequence accordingly.
3. **Accounting integration** — which accounting system (if any) and whether payment automation is ever in scope (governance).
4. **Analytics canonical-events dependency** — analytics can't start until `casework` emits canonical events; what KPI set is v1.
5. **Warehouse trigger** — what justifies moving analytics beyond canonical-events queries into a warehouse/case-lake (retention/licensing/data-quality maturity).
6. **Partner/portal/insurer/Audatex** — all commercial + security-sensitive; each needs its own governed option-paper before any commitment.
7. **Product positioning** — keep CCC framed as intake/evidence/admin support, not autonomous expert judgement; who owns the messaging.
