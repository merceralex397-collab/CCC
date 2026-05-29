# Foundation Workspace — Open Questions

Date: 2026-05-29
Status: active open-questions log
Owner: unassigned
Group: foundation (G0 / continuous)
Source links: `docs/superpowers/specs/2026-05-29-foundation-design.md`, `docs/plans/foundation/plan.md`, `docs/security/role_model.md`, `docs/security/data_retention_policy.md`

## Resolved (this interview, 2026-05-29)

- **Scope?** — Map existing docs + capture cross-cutting gaps; define role model now; update vendor register + retention now.
- Authored: `role_model.md` (draft), `data_retention_policy.md` (draft), `vendor_register.md` update, `data_map.md` pointer, gaps backlog.

## Open (require sign-off / decision)

1. **Role model sign-off** — confirm CE job-title → role mapping, separation-of-duties, reviewer vs engineer distinction, enforcement across Python tools + WinUI app + tool gateway.
2. **Retention periods** — confirm every placeholder with business/DPO (statutory + limitation periods for collision/expert-evidence work); licensing caps on the vehicle evidence store.
3. **DVSA-MOT token rotation** — execute (CE IT) and confirm secret-store handling.
4. **Redaction data map** — which PII fields must be redacted before any external model call (extends `data_map.md` for `ai-platform`).
5. **Deployment/packaging** — Python parser (Tk) + .NET WinUI casework app + work-item service on staff Windows machines; release/rollback + MSIX (operations-quality).
6. **Vendor reviews** — complete the "review required before use" checks for the newly registered vendors before any live use.
