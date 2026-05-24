# Plans Index

`docs/plans/` contains active plan workspaces and plan archives.

| Plan Area | Path | Status |
| --- | --- | --- |
| Initial Repo Setup | `docs/plans/initial-repo-setup/` | active pre-code planning workspace |
| Operational Core | `docs/plans/operational-core/` | active first-slice coordination workspace |
| Programme Roadmap | `docs/plans/roadmap.md` | active roadmap mirror |
| Workspace Ownership Matrix | `docs/plans/workspace_ownership_matrix.md` | active ownership and source matrix |
| Workspace Expansion Plan | `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md` | approved taxonomy source |

## Active Planning Workspaces

| Area | Path | Owns |
| --- | --- | --- |
| Unified Platform | `docs/plans/unified-platform/` | Mature end-to-end CCC platform planning and convergence roadmap. |
| Automation Centre | `docs/plans/automation-centre/` | Deterministic automation architecture, operating cadence, and reusable workflow patterns. |
| Parser Extraction | `docs/plans/parser-extraction/` | Parser, document extraction, CE Document Mapper evolution, and extraction-regression planning. |
| Case Workflow State | `docs/plans/case-workflow-state/` | Canonical work-item state, review queue, audit stream, missing-info state, and historical search planning. |
| Provider Principal Config | `docs/plans/provider-principal-config/` | Provider, principal, garage, routing, and provider-rule lifecycle planning. |
| Intake Storage Integrations | `docs/plans/intake-storage-integrations/` | Intake channels, source capture, storage adapters, EVA/Sentry adapters, and transitional spreadsheet bridge planning. |
| Evidence Estimate Review | `docs/plans/evidence-estimate-review/` | Evidence matching, image review, estimate parsing, ABP review, and damage workbench planning. |
| Vehicle Valuation Data | `docs/plans/vehicle-valuation-data/` | Vehicle identity, DVLA/DVSA, MOT, mileage, valuation evidence, salvage, and vehicle-history support. |
| Engineer Communications | `docs/plans/engineer-communications/` | Engineer pack, template, reporting, status, and communication workflow planning. |
| AI Agents | `docs/plans/ai-agents/` | Bounded workflow agents that orchestrate approved tools and portable skills under permission and approval gates. |
| MCP And Tooling | `docs/plans/mcp-and-tooling/` | MCP servers, internal tool adapters, registry, schemas, gateway controls, and safe tool discovery planning. |
| Agent Skills | `docs/plans/agent-skills/` | Portable reusable staff/engineer skills with prompt/version/evaluation lifecycle and cross-AI portability. |
| AI Platform Tools | `docs/plans/ai-platform-tools/` | Shared AI substrate behind tools, skills, and agents. |
| User Experience Interfaces | `docs/plans/user-experience-interfaces/` | Human-facing screen, workflow, and interaction design across staff, engineer, admin, and front-door surfaces. |
| Finance Billing | `docs/plans/finance-billing/` | Finance, invoice, fee-note, payment-status, payment evidence, and billing automation option planning. |
| Governance Security | `docs/plans/governance-security/` | Cross-programme governance, security, privacy, vendor, licensing, audit, and expert-boundary planning. |
| Operations Quality | `docs/plans/operations-quality/` | Shared QA, release, rollout, monitoring, support, regression, and decommissioning planning. |
| Analytics Data Platform | `docs/plans/analytics-data-platform/` | Data, analytics, historical mining, BI, data quality, and continuous improvement planning. |
| External Platform Partners | `docs/plans/external-platform-partners/` | External-facing systems, customer/partner portals, partner APIs, insurer integrations, Audatex partnerships, and partner access controls. |
| Product Business | `docs/plans/product-business/` | Business framing, discovery, ROI/KPI tracking, client positioning, objections, and defensibility planning. |

## Existing Workspace Layout

- `docs/plans/initial-repo-setup/` captures repo setup, documentation scaffold, source evidence handling, and exhaustive reference-derived idea planning.
- `docs/plans/operational-core/` coordinates first-slice MVP dependencies across owning workspaces.
- `docs/plans/parser-extraction/parser-mvp/plan.md` is the active parser MVP plan. `docs/plans/operational-core/parser-mvp/plan.md` is preserved only as a compatibility stub for historical links and scaffold checks.

## Standard Workspace Layout

Each top-level workspace uses:

```text
README.md
plan.md
source_map.md
roadmap.md
tickets/README.md
option-papers/README.md
archived_plans/implemented/
archived_plans/superseded/
```
