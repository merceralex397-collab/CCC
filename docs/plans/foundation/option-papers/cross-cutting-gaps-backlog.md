# Cross-Cutting Gaps Backlog

Status: active backlog
Owner: unassigned
Created: 2026-05-29
Group: foundation (G0 / continuous)
Source links: `docs/superpowers/specs/2026-05-29-foundation-design.md`, all 2026-05-29 workspace specs

The cross-cutting items the workspace interviews surfaced that foundation tracks until closed.

| # | Gap | Surfaced by | Owner | Status |
| --- | --- | --- | --- | --- |
| 1 | **CE role model** (human + agent permissions) | casework, ai-platform, finance, intelligence | governance-security | DRAFT authored: `docs/security/role_model.md` — needs sign-off |
| 2 | **DVSA-MOT token rotation** (plaintext in collisionplugin) | mcp-tooling | CE IT / governance-security | OPEN — rotate immediately, move to secret store |
| 3 | **Retention policy** (evidence store, historical search, analytics, AI logs) | intelligence, casework, business, ai-platform | governance-security / DPO | DRAFT authored: `docs/security/data_retention_policy.md` — confirm periods |
| 4 | **Redaction data map** (PII fields redacted before external model calls) | ai-platform | governance-security | OPEN — extend `docs/security/data_map.md` |
| 5 | **Deployment/packaging** (Python parser + .NET WinUI casework app + work-item service) | casework, parser | operations-quality | OPEN — packaging/update plan (MSIX for WinUI) |
| 6 | **Vendor register** (Graph, Box, DVSA, Autotrader/Codex, model providers) | bridge, mcp-tooling, intelligence, ai-platform | governance-security | UPDATED: `docs/security/vendor_register.md` — complete per-vendor reviews before live use |
| 7 | **Work-item store access boundary** (shared SQLite vs Python service for the .NET UI) | casework | casework / operations-quality | OPEN — option-paper in casework |
| 8 | **Store-access / role enforcement across stacks** (Python + .NET + gateway) | casework, mcp-tooling, ai-platform | governance-security / casework | OPEN — depends on the role model |
| 9 | **Case-corpus PII committed in-repo** (real claimant data under `docs/reference/case-corpus/`) | agent-skills | governance-security / DPO | OPEN — by-decision (2026-05-29); redact before any external skill distribution; access per role model (#1), retention per policy (#3) |

## Rule

No governance-gated build proceeds until its blocking gap here is closed (or an explicit, signed-off risk acceptance is recorded).
