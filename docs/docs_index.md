# Documentation Index

This is the primary human navigation file for CCC documentation.

## Quick Start

- Product scope and current milestone: `README.md` and `docs/roadmap.md`.
- Initial setup planning: `docs/plans/initial-repo-setup/README.md`.
- Active programme coordination: `docs/plans/operational-core/source_synthesis.md`.
- Cross-workspace backlog: `docs/plans/operational-core/tickets/backlog_index.md`.
- Planned folder taxonomy (implemented 2026-05-24): `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`.
- **Parser MVP plan (active)**: `docs/plans/parser-extraction/parser-mvp/plan.md`.
- Agent path map: `docs/repo_map.json`.
- Full source inventory: `docs/source_manifest.md`, `docs/source_manifest.csv`, and `docs/source_manifest.json`.

## Active Work

| Area | Path | Use |
| --- | --- | --- |
| Plans | `docs/plans/_index.md` | Active plan workspaces and archived plans. |
| Initial Repo Setup | `docs/plans/initial-repo-setup/` | Pre-code repository setup, documentation scaffold, and exhaustive reference idea planning. |
| Operational Core | `docs/plans/operational-core/` | Cross-workspace programme coordination, source synthesis, and tombstone index. |
| Parser Extraction | `docs/plans/parser-extraction/` | Parser MVP plan, extraction adapter tickets, corpus regression tickets. |
| Case Workflow State | `docs/plans/case-workflow-state/` | Work item lifecycle, review queue, audit. |
| Provider Principal Config | `docs/plans/provider-principal-config/` | Provider presets, admin UI, parity triage. |
| Intake Storage Integrations | `docs/plans/intake-storage-integrations/` | Outlook, Box, EVA/Sentry, and intake boundary tickets. |
| User Experience Interfaces | `docs/plans/user-experience-interfaces/` | Staff UI, engineer UI, accessibility. |
| Vehicle Valuation Data | `docs/plans/vehicle-valuation-data/` | DVLA/DVSA, mileage, valuation evidence. |
| Evidence Estimate Review | `docs/plans/evidence-estimate-review/` | Image quality, duplicate evidence, damage workbench. |
| Engineer Communications | `docs/plans/engineer-communications/` | Engineer pack, communications drafting. |
| Analytics Data Platform | `docs/plans/analytics-data-platform/` | Operations analytics, data warehouse. |
| External Platform Partners | `docs/plans/external-platform-partners/` | Portal, partner API, insurer/Audatex integrations. |
| Governance Security | `docs/plans/governance-security/` | DPIA, vendor governance, API security. |
| Operations Quality | `docs/plans/operations-quality/` | Test corpus, regression, release/rollback. |
| AI Agents | `docs/plans/ai-agents/` | Controlled workflow agents. |
| MCP And Tooling | `docs/plans/mcp-and-tooling/` | MCP servers, tool registry, security gateway. |
| Agent Skills | `docs/plans/agent-skills/` | Reusable natural-language skills. |
| AI Platform Tools | `docs/plans/ai-platform-tools/` | Model evaluation, prompt governance. |
| Finance Billing | `docs/plans/finance-billing/` | Invoice, fee-note, payment status. |
| Automation Centre | `docs/plans/automation-centre/` | Deterministic automation, workflows, retries. |
| Unified Platform | `docs/plans/unified-platform/` | Convergence roadmap. |
| Product Business | `docs/plans/product-business/` | Product discovery, ROI, client pitch. |
| Architecture | `docs/architecture/` | System architecture and programme boundaries. |
| Contracts | `docs/contracts/` | Versioned schemas and integration contracts. |
| Decisions | `docs/decisions/` | ADRs and option papers. |
| Requirements | `docs/requirements/` | Business requirements and open questions. |
| Operations | `docs/operations/` | Runbooks, monitoring, release, rollback, and spreadsheet companion notes. |
| Security | `docs/security/` | Data map, vendor register, DPIA, safety review, and API security. |

## Reference Material

| Area | Path | Use |
| --- | --- | --- |
| Raw evidence | `docs/reference/raw/collisionrelateddocs/` | Immutable source files. Do not edit in place. |
| Normalized companions | `docs/reference/normalized/` | Generated Markdown companions for raw evidence. |
| Reference data | `docs/reference/data/` | Provider matrix and extracted Jam/FigJam derivatives. |
| Original planning | `docs/reference/originalplanning/` | Historical/generated planning packs; reference-only unless promoted. |
| Test context | `docs/reference/test-context/` | Historical test repositories and context packs. |

## Quality Rules

- Update `docs/source_manifest.*` when source files, generated companions, active docs, or archives change.
- Promote ideas from reference material into `docs/plans/initial-repo-setup/reference-audit/`, the appropriate domain workspace tickets, or another owning plan before treating them as active scope.
- Keep raw evidence immutable and create derivatives under `docs/reference/normalized/` or `docs/reference/data/`.
- Run `python tools/verify_scaffold.py` after documentation structure changes.
