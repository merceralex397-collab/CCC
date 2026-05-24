from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import textwrap


ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-05-24"


@dataclass(frozen=True)
class Evidence:
    path: str
    note: str


@dataclass(frozen=True)
class Workspace:
    slug: str
    title: str
    purpose: str
    owns: list[str]
    not_own: list[str]
    dependencies: list[str]
    evidence: list[Evidence]
    roadmap: list[tuple[str, list[str]]]

    @property
    def path(self) -> str:
        return f"docs/plans/{self.slug}"


WORKSPACES: list[Workspace] = [
    Workspace(
        slug="unified-platform",
        title="Unified Platform",
        purpose="Mature end-to-end CCC platform planning and convergence roadmap.",
        owns=[
            "full case-management target platform",
            "system-wide convergence roadmap",
            "migration and legacy decommissioning strategy",
            "cross-workspace platform dependency map",
        ],
        not_own=[
            "domain implementation tickets owned by specialist workspaces",
            "first parser-runtime implementation details",
            "vendor activation decisions without governance-security sign-off",
        ],
        dependencies=["operational-core", "case-workflow-state", "automation-centre", "user-experience-interfaces", "governance-security"],
        evidence=[
            Evidence("docs/reference/originalplanning/originalplans_output/phase_new_system.md", "Near-term integrated case-intake system scope."),
            Evidence("docs/reference/originalplanning/originalplans_output/phase_bespoke_system.md", "Mature bespoke system direction."),
            Evidence("docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md", "Detailed mature single-platform plan."),
            Evidence("docs/architecture/future_system_convergence.md", "Canonical convergence spine and guardrails for later modules."),
        ],
        roadmap=[
            ("S0-S1", ["Track how foundational parser, work item, provider, UI, and export work align to the shared platform spine."]),
            ("S2-S3", ["Coordinate storage, intake, EVA/Sentry, and automation-centre decisions so they use common contracts."]),
            ("S4-S6", ["Sequence mature platform capabilities, adoption, and legacy decommissioning only after parity and rollback evidence."]),
        ],
    ),
    Workspace(
        slug="automation-centre",
        title="Automation Centre",
        purpose="Deterministic automation architecture, operating cadence, and reusable workflow patterns.",
        owns=[
            "automation-vs-agent decision framework",
            "workflow triggers, queues, retries, idempotency, and exception routing",
            "automation operating model and KPIs",
            "shared automation service boundaries",
        ],
        not_own=[
            "domain adapters such as Outlook, Box, EVA, finance, or portal implementations",
            "AI agent orchestration",
            "MCP tool schemas and gateway controls",
        ],
        dependencies=["case-workflow-state", "operations-quality", "governance-security", "mcp-and-tooling"],
        evidence=[
            Evidence("docs/reference/originalplanning/originalplans_output/phase_initial_automation.md", "Initial automation phase source."),
            Evidence("docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/15_AUTOMATION_CENTRE_OPERATING_MODEL.md", "Reusable automation-centre operating model."),
            Evidence("docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md", "Boundary between automation, draft-only skills, and agents."),
            Evidence("docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/10_WORKFLOW_STATES_AND_ORCHESTRATION.md", "Workflow states, retries, and orchestration evidence."),
        ],
        roadmap=[
            ("S1-S2", ["Define event taxonomy and deterministic automation boundaries alongside work-item state."]),
            ("S3", ["Plan intake/storage/EVA retry and exception patterns with runbook hooks."]),
            ("S4-S6", ["Promote only measured, low-risk workflows from assisted mode toward controlled automation."]),
        ],
    ),
    Workspace(
        slug="parser-extraction",
        title="Parser Extraction",
        purpose="Parser, document extraction, CE Document Mapper evolution, and extraction-regression planning.",
        owns=[
            "PDF, DOCX, DOC, MSG, EML, image, ZIP, and batch extraction",
            "deterministic-first parser core and provider-rule execution behavior",
            "OCR/cloud document-intelligence option papers",
            "parser CLI parity and extraction regression corpus",
        ],
        not_own=[
            "provider business routing metadata after extraction",
            "case-state transitions after parse",
            "human-facing UI design beyond parser-specific requirements",
        ],
        dependencies=["provider-principal-config", "operations-quality", "governance-security", "user-experience-interfaces"],
        evidence=[
            Evidence("docs/plans/parser-extraction/parser-mvp/plan.md", "Active parser MVP implementation plan."),
            Evidence("docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md", "Adjacent parser comparison, inspection-location decision register, and EVA/Sentry lookup constraint."),
            Evidence("docs/decisions/0004-ground-up-compatible-parser-rebuild.md", "Accepted ground-up compatible parser rebuild decision."),
            Evidence("docs/decisions/0007-deterministic-first-parser.md", "Accepted deterministic-first parser decision."),
            Evidence("docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md", "Document Mapper and extraction work package."),
            Evidence("docs/contracts/extraction_adapter_contract_v1.md", "Versioned extraction adapter contract."),
        ],
        roadmap=[
            ("S1", ["Maintain active parser MVP planning here, then deliver deterministic parser core and shared UI/CLI service behavior."]),
            ("S2", ["Harden extraction adapters, provider corpus coverage, export blockers, and UI/CLI parity."]),
            ("S3-S4", ["Evaluate OCR/cloud fallback and AI extraction only behind governance and measurable regression evidence."]),
        ],
    ),
    Workspace(
        slug="case-workflow-state",
        title="Case Workflow State",
        purpose="Canonical work-item state, review queue, audit stream, missing-info state, and historical search planning.",
        owns=[
            "work item lifecycle and state transitions",
            "holding pen, review queue, and approval states",
            "missing-information checklist and state machine",
            "duplicate, merge, link, split, and historical search workflows",
        ],
        not_own=[
            "parser extraction internals",
            "UI visual design",
            "live Outlook, Box, or EVA adapter implementation",
        ],
        dependencies=["parser-extraction", "provider-principal-config", "governance-security", "user-experience-interfaces"],
        evidence=[
            Evidence("docs/contracts/work_item_contract_v1.md", "Canonical work item contract."),
            Evidence("docs/contracts/review_audit_event_contract_v1.md", "Review and audit event contract."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_01_work_item_state_store_and_job_sheet_replacement.md", "Work item state store and job-sheet replacement plan."),
            Evidence("docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md", "Dashboard, review queue, evidence matching, and safeguards."),
            Evidence("docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md", "Whiteboard-derived workflow and closure/payment metadata evidence."),
        ],
        roadmap=[
            ("S1", ["Define work-item state store, review queue, missing blockers, and audit event shape."]),
            ("S2-S3", ["Add duplicate/case association and missing-information closure rules with source-linked decisions."]),
            ("S5", ["Plan historical search and merge/link/split workflows once reliable case history exists."]),
        ],
    ),
    Workspace(
        slug="provider-principal-config",
        title="Provider Principal Config",
        purpose="Provider, principal, garage, routing, and provider-rule lifecycle planning.",
        owns=[
            "provider preset migration and coverage baseline",
            "principal, garage, alias, routing, contact, and delivery metadata",
            "provider admin workflow, versioning, activation, rollback, and audit",
            "provider mapping assistant planning",
        ],
        not_own=[
            "low-level parser extraction algorithms",
            "finance invoice generation except fee-note metadata source rules",
            "external partner APIs",
        ],
        dependencies=["parser-extraction", "case-workflow-state", "operations-quality", "governance-security"],
        evidence=[
            Evidence("docs/contracts/provider_principal_config_contract_v1.md", "Provider/principal configuration contract."),
            Evidence("docs/reference/data/provider_coverage_matrix.md", "Current provider coverage matrix and uncovered principal evidence."),
            Evidence("docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md", "Provider settings and migration work package."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/28_provider_mapping_assistant.md", "Provider mapping assistant plan."),
        ],
        roadmap=[
            ("S1", ["Move provider coverage and provider-admin tickets here; preserve all 26 current presets and uncovered-principal triage."]),
            ("S2", ["Add regression-backed provider activation, rollback, principal/garage migration, and composite mapping rules."]),
            ("S4", ["Add provider mapping assistant as a governed staff skill/tool with approval and backup controls."]),
        ],
    ),
    Workspace(
        slug="intake-storage-integrations",
        title="Intake Storage Integrations",
        purpose="Intake channels, source capture, storage adapters, EVA/Sentry adapters, and transitional spreadsheet bridge planning.",
        owns=[
            "Outlook/Graph intake and polling fallback",
            "Box-ready package to live Box adapter path",
            "EVA JSON export and EVA/Sentry adapter planning",
            "website, WhatsApp, payment, Box, and local-folder metadata boundaries",
            "job-sheet/spreadsheet transition bridge planning",
        ],
        not_own=[
            "external customer portal product scope",
            "payment automation itself",
            "MCP wrappers when the issue is tool exposure rather than adapter behavior",
        ],
        dependencies=["case-workflow-state", "mcp-and-tooling", "governance-security", "operations-quality"],
        evidence=[
            Evidence("docs/contracts/evidence_package_contract_v1.md", "Evidence package contract including portal/payment metadata."),
            Evidence("docs/contracts/storage_adapter_contract_v1.md", "Storage adapter contract."),
            Evidence("docs/contracts/eva_export_contract_v1.md", "EVA export contract."),
            Evidence("docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/07_WORK_PACKAGE_OUTLOOK_AND_COMMUNICATIONS.md", "Outlook intake and communications source."),
            Evidence("docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/08_WORK_PACKAGE_BOX_STORAGE_AND_FILES.md", "Box storage and files work package."),
            Evidence("docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/10_WORK_PACKAGE_EVA_SENTRY_INTEGRATION.md", "EVA/Sentry integration work package."),
        ],
        roadmap=[
            ("S1", ["Own EVA JSON export and Box-ready package adapter boundaries with Operational Core coordination."]),
            ("S3", ["Plan Outlook intake, live Box upload, EVA/Sentry submission control, and spreadsheet bridge with sandbox tests."]),
            ("S5", ["Feed portal/API and payment automation evidence to external-platform-partners and finance-billing option papers."]),
        ],
    ),
    Workspace(
        slug="evidence-estimate-review",
        title="Evidence Estimate Review",
        purpose="Evidence matching, image review, estimate parsing, ABP review, and damage workbench planning.",
        owns=[
            "evidence matching and duplicate/reused evidence flags",
            "image quality, visible VRM, and image ordering assistance",
            "Audatex/repair estimate parsing and estimate QA flags",
            "ABP charge review pack and ANDIE-style long-range damage workbench",
        ],
        not_own=[
            "vehicle valuation source selection",
            "engineer final technical judgement",
            "Audatex commercial partnership discovery",
        ],
        dependencies=["case-workflow-state", "vehicle-valuation-data", "engineer-communications", "governance-security"],
        evidence=[
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/10_image_evidence_quality_and_schedule_checker.md", "Image evidence quality and schedule checker plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/11_visible_vrm_and_image_case_matcher.md", "Visible VRM and image case matcher plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/12_audatex_estimate_parser_and_qa_assistant.md", "Audatex estimate parser and QA assistant plan."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_08_estimate_abp_review_pack.md", "Estimate and ABP review pack plan."),
            Evidence("docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/11_audatex_abp_industry_context.md", "Audatex and ABP industry context and safe positioning."),
        ],
        roadmap=[
            ("S2-S3", ["Use case-state and review queues to surface evidence matching and image-order issues."]),
            ("S4", ["Promote image intelligence, estimate parsing, ABP review, and evidence duplicate flags as review aids."]),
            ("S6", ["Plan advanced damage workbench only after evidence, governance, and engineer-review controls are mature."]),
        ],
    ),
    Workspace(
        slug="vehicle-valuation-data",
        title="Vehicle Valuation Data",
        purpose="Vehicle identity, DVLA/DVSA, MOT, mileage, valuation evidence, salvage, and vehicle-history support.",
        owns=[
            "DVLA/DVSA and MOT evidence planning",
            "mileage estimation, anomaly review, and source confidence",
            "vehicle identity normalization and conflict resolution",
            "valuation evidence store, salvage benchmarking, and prior vehicle/case context",
        ],
        not_own=[
            "final valuation or uplift decisions",
            "market/commercial-provider activation without governance",
            "broad analytics warehouse",
        ],
        dependencies=["mcp-and-tooling", "governance-security", "analytics-data-platform", "engineer-communications"],
        evidence=[
            Evidence("docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/03_mot_bulk_delta_ingestion.md", "MOT bulk/delta ingestion plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/04_mileage_estimation_engine.md", "Mileage estimation engine plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/08_dvla_vrm_attribute_cache.md", "DVLA VRM attribute cache plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/10_market_valuation_evidence_store.md", "Market valuation evidence store plan."),
            Evidence("docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/05_valuation_vehicle_data_and_uplift.md", "Vehicle data and uplift review guardrails."),
        ],
        roadmap=[
            ("S4", ["Plan factual DVLA/DVSA, MOT, mileage, and valuation evidence with source confidence and review boundaries."]),
            ("S5", ["Add salvage benchmarking and prior same-VRM context once retention/licensing controls are approved."]),
            ("S6", ["Keep weather, road, and traffic context as option papers unless directly needed for review."]),
        ],
    ),
    Workspace(
        slug="engineer-communications",
        title="Engineer Communications",
        purpose="Engineer pack, template, reporting, status, and communication workflow planning.",
        owns=[
            "engineer pack generation workflow",
            "template manager and report-support workflow",
            "missing-info and status communication workflow",
            "communications approval, audit, and handoff patterns",
        ],
        not_own=[
            "portable natural-language skill specs",
            "expert judgement or final report conclusions",
            "external channel automation without separate approval",
        ],
        dependencies=["case-workflow-state", "agent-skills", "user-experience-interfaces", "governance-security"],
        evidence=[
            Evidence("docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/11_WORK_PACKAGE_ENGINEER_PACK_AND_REPORTING.md", "Engineer pack and reporting work package."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_06_engineer_pack_generator_and_template_manager.md", "Engineer pack generator and template manager plan."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_09_communications_chaser_and_status_drafting.md", "Communications chaser and status drafting plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/17_engineer_pack_generator.md", "Engineer pack generator skill/tool plan."),
        ],
        roadmap=[
            ("S4", ["Generate engineer packs and communication drafts only from reviewed work items and approved source evidence."]),
            ("S5", ["Add engineer support/report drafting assistants with explicit engineer sign-off boundaries."]),
            ("S6", ["Connect mature report/template support to unified-platform rollout and decommissioning gates."]),
        ],
    ),
    Workspace(
        slug="ai-agents",
        title="AI Agents",
        purpose="Bounded workflow agents that orchestrate approved tools and portable skills under permission and approval gates.",
        owns=[
            "inbox triage, missing-information, valuation/uplift, engineer support, and continuous-learning agent plans",
            "agent permission levels, escalation, and approval boundaries",
            "agent-vs-automation decision framework",
        ],
        not_own=[
            "deterministic automation engine",
            "MCP tool implementation",
            "portable skill prompt specs",
            "model hosting and evaluation substrate",
        ],
        dependencies=["mcp-and-tooling", "agent-skills", "automation-centre", "governance-security", "ai-platform-tools"],
        evidence=[
            Evidence("docs/reference/originalplanning/originalplans_output/phase_ai_agents.md", "Original AI agents phase source."),
            Evidence("docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/00_README.md", "Reviewed correction that most features are automation, tools, dashboards, or drafts rather than free-running agents."),
            Evidence("docs/reference/originalplanning/ce_phase4_agents_reviewed_plan/ce_phase4_agents_reviewed_plan/02_agent_vs_automation_decision_framework.md", "Agent-vs-automation decision framework."),
            Evidence("docs/architecture/governance_security.md", "Human approval and governance guardrails."),
        ],
        roadmap=[
            ("S3", ["Define agent permission model only after tools, skills, and audit contracts exist."]),
            ("S4-S5", ["Pilot read-only or draft-only agents for triage, missing-info, valuation support, and engineer support."]),
            ("S6", ["Continuous-learning agents remain recommendation-only and cannot self-modify production behavior."]),
        ],
    ),
    Workspace(
        slug="mcp-and-tooling",
        title="MCP And Tooling",
        purpose="MCP servers, internal tool adapters, registry, schemas, gateway controls, and safe tool discovery planning.",
        owns=[
            "EVA/Sentry, Outlook Graph, Box, DVLA/DVSA, spreadsheet, observability, and gateway MCP plans",
            "tool schemas, auth boundaries, rate limits, audit, and safe discovery",
            "tool registry and security gateway",
        ],
        not_own=[
            "domain adapter business behavior",
            "agent orchestration policy",
            "portable natural-language skill content",
        ],
        dependencies=["governance-security", "intake-storage-integrations", "vehicle-valuation-data", "ai-agents"],
        evidence=[
            Evidence("docs/architecture/tooling.md", "Current tooling architecture summary."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/01_eva_sentry_api_mcp.md", "EVA/Sentry API MCP plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/02_outlook_graph_intake_mcp.md", "Outlook Graph intake MCP plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/03_box_storage_metadata_mcp.md", "Box storage metadata MCP plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/29_tool_registry_and_mcp_security_gateway.md", "Tool registry and MCP security gateway plan."),
        ],
        roadmap=[
            ("S3", ["Plan domain MCP wrappers around approved adapters without exposing secrets or bypassing review."]),
            ("S4", ["Add observability, DVLA/DVSA, and controlled read-only helper tools behind the registry."]),
            ("S5-S6", ["Use gateway permissions, audit, and rate limits before agents or external partners can call tools."]),
        ],
    ),
    Workspace(
        slug="agent-skills",
        title="Agent Skills",
        purpose="Portable reusable staff/engineer skills with prompt/version/evaluation lifecycle and cross-AI portability.",
        owns=[
            "case summary, missing-info, CE style, valuation explanation, report-clause RAG, AI literacy, and provider mapping skill specs",
            "skill prompt/version/evaluation/release lifecycle",
            "portable skill contracts for CE platform, agents, ChatGPT, Claude Desktop, or other approved AI front ends",
        ],
        not_own=[
            "workflow orchestration",
            "model hosting or global AI run logging",
            "business workflow ownership where the skill is used",
        ],
        dependencies=["ai-platform-tools", "governance-security", "engineer-communications", "mcp-and-tooling"],
        evidence=[
            Evidence("docs/reference/originalplanning/originalplans_output/phase_ai_tools.md", "Natural-language skills for staff and engineers."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/README.md", "AI tools, MCPs, and skills plan index."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md", "Case summary/status skill plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md", "CE communication style skill plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/22_knowledge_base_report_clause_rag_skill.md", "Knowledge-base/report-clause RAG skill plan."),
        ],
        roadmap=[
            ("S4", ["Define portable skill catalogue and golden examples for case summary, chasers, CE style, and valuation explanation."]),
            ("S5", ["Add RAG/report-clause and training skills with source-citation and no-source refusal rules."]),
            ("S6", ["Keep skills portable across approved AI front ends while adapters and orchestration remain elsewhere."]),
        ],
    ),
    Workspace(
        slug="ai-platform-tools",
        title="AI Platform Tools",
        purpose="Shared AI substrate behind tools, skills, and agents.",
        owns=[
            "model/provider selection and hosting option papers",
            "prompt/version governance and AI run logging",
            "evaluation datasets, gold standards, reviewer corrections, and regression alerts",
            "redaction/training-data controls and AI policy implementation",
        ],
        not_own=[
            "portable skill content",
            "workflow agents",
            "MCP tool gateway",
        ],
        dependencies=["governance-security", "operations-quality", "agent-skills", "parser-extraction"],
        evidence=[
            Evidence("docs/reference/originalplanning/originalplans_output/phase_ai_tools.md", "Model hosting, data collection, and evaluation/feedback-loop source."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/25_model_evaluation_feedback_loop.md", "Model evaluation and feedback loop plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/27_pii_redaction_audit_governance_tool.md", "PII redaction, audit, and governance tool plan."),
            Evidence("docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/10_ai_modules_and_prompts.md", "AI modules and prompt-pattern evidence."),
        ],
        roadmap=[
            ("S2", ["Version prompts and schemas for any AI-assisted module before release."]),
            ("S4", ["Build evaluation datasets, correction feedback loops, and redaction controls."]),
            ("S5-S6", ["Support model hosting and training/evaluation only after governance approval and source minimisation."]),
        ],
    ),
    Workspace(
        slug="user-experience-interfaces",
        title="User Experience Interfaces",
        purpose="Human-facing screen, workflow, and interaction design across staff, engineer, admin, and front-door surfaces.",
        owns=[
            "dashboard, holding pen, parser UI, case detail, review, activity/audit, and settings screen maps",
            "provider-admin UX and role-based workflow surfaces",
            "internal portal/Teams front-door interaction design",
            "accessibility, adoption, fallback, and staff mental-model checks",
        ],
        not_own=[
            "business rules implemented by domain workspaces",
            "parser core logic",
            "external portal/API product scope",
        ],
        dependencies=["case-workflow-state", "parser-extraction", "provider-principal-config", "engineer-communications"],
        evidence=[
            Evidence("docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/07_ui_dashboard_spec.md", "Case-operation dashboard and screen specification."),
            Evidence("docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md", "Dashboard/review queue and UX safeguards."),
            Evidence("docs/architecture/parser_ui_cli.md", "Parser UI and CLI architecture."),
            Evidence("docs/architecture/mvp_interlock.md", "Staff UI role in first MVP."),
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/23_whatsapp_teams_portal_front_door.md", "Portal/Teams front-door source."),
        ],
        roadmap=[
            ("S1", ["Plan staff parser UI and review/correction flows over the shared parser and work-item services."]),
            ("S2-S4", ["Add case operation dashboard, evidence matching, estimate review, activity log, and engineer pack UX."]),
            ("S5-S6", ["Plan internal portal/Teams, engineer PWA/mobile, and mature platform surfaces."]),
        ],
    ),
    Workspace(
        slug="finance-billing",
        title="Finance Billing",
        purpose="Finance, invoice, fee-note, payment-status, payment evidence, and billing automation option planning.",
        owns=[
            "invoice and fee-note document generation",
            "fee rules and finance approval workflow",
            "payment status, payment chaser metadata, overdue visibility",
            "payment/accounting integration option papers",
        ],
        not_own=[
            "repair estimate review",
            "external customer portal product scope",
            "early parser-owned payment automation",
        ],
        dependencies=["case-workflow-state", "provider-principal-config", "intake-storage-integrations", "governance-security"],
        evidence=[
            Evidence("docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/31_invoice_fee_note_generation_tool.md", "Invoice/fee-note generation tool plan."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_14_invoice_and_payment_workflow_automation.md", "Invoice and payment workflow automation plan."),
            Evidence("docs/reference/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md", "Website form, payment status, invoice, and chaser evidence."),
            Evidence("docs/contracts/work_item_contract_v1.md", "Payment status and chaser metadata fields."),
            Evidence("docs/contracts/evidence_package_contract_v1.md", "Invoice, summary, and payment metadata package rules."),
        ],
        roadmap=[
            ("S3", ["Record payment and invoice evidence as metadata without authorising payment automation."]),
            ("S5", ["Plan draft invoice/fee-note generation from approved case data and provider fee rules."]),
            ("S6", ["Evaluate accounting/payment integrations and autonomous chasers only through option papers and governance approval."]),
        ],
    ),
    Workspace(
        slug="governance-security",
        title="Governance Security",
        purpose="Cross-programme governance, security, privacy, vendor, licensing, audit, and expert-boundary planning.",
        owns=[
            "DPIA/vendor governance tickets and risk acceptance",
            "data map, retention, redaction, access review, and audit policy backlog",
            "expert-evidence boundary and risk-language policy",
            "public/commercial data licensing controls and API security standards",
        ],
        not_own=[
            "all domain implementation of controls",
            "operations runbooks except governance incident requirements",
            "MCP gateway implementation details",
        ],
        dependencies=["all workspaces"],
        evidence=[
            Evidence("docs/architecture/governance_security.md", "Canonical governance and security architecture."),
            Evidence("docs/security/dpia_vendor_governance.md", "DPIA and vendor governance checklist."),
            Evidence("docs/security/vendor_register.md", "Current vendor register."),
            Evidence("docs/security/api_security_standard.md", "API security standard."),
            Evidence("docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/12_compliance_governance_and_risk.md", "Expert evidence and AI governance risk source."),
        ],
        roadmap=[
            ("S0-S1", ["Gate core architecture, data map, roles, audit, and no personal injury or KADOE scope."]),
            ("S2-S4", ["Review cloud OCR, AI, Box/Graph/EVA, valuation, and redaction controls before activation."]),
            ("S5-S6", ["Gate partner APIs, portals, analytics, warehouse, risk indicators, payment automation, and commercial data use."]),
        ],
    ),
    Workspace(
        slug="operations-quality",
        title="Operations Quality",
        purpose="Shared QA, release, rollout, monitoring, support, regression, and decommissioning planning.",
        owns=[
            "test corpus and regression harness planning",
            "release and rollback process",
            "monitoring, runbooks, alerts, incident/failure playbooks",
            "pilot, shadow run, controlled rollout, support ownership, and decommissioning gates",
        ],
        not_own=[
            "domain-specific feature design",
            "model-evaluation substrate owned by ai-platform-tools",
            "business analytics dashboards beyond operational health",
        ],
        dependencies=["parser-extraction", "intake-storage-integrations", "governance-security", "unified-platform"],
        evidence=[
            Evidence("docs/operations/monitoring_runbooks.md", "Current monitoring and runbooks baseline."),
            Evidence("docs/operations/release_and_rollback.md", "Current release and rollback baseline."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md", "Test corpus and regression harness plan."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/additional_items/08_11_monitoring_runbooks_and_release_management.md", "Monitoring, runbooks, and release management plan."),
            Evidence("docs/reference/originalplanning/ce_system_plans_enhanced/ce_system_plans_enhanced/13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md", "Security, testing, rollout, and decommissioning plan."),
        ],
        roadmap=[
            ("S1-S2", ["Create regression harness, provider corpus gates, and release checklist for parser/provider changes."]),
            ("S3", ["Add integration sandbox tests, monitoring events, failure runbooks, and rollout gates."]),
            ("S4-S6", ["Control pilot, staff training, adoption, rollback, and legacy decommissioning evidence."]),
        ],
    ),
    Workspace(
        slug="analytics-data-platform",
        title="Analytics Data Platform",
        purpose="Data, analytics, historical mining, BI, data quality, and continuous improvement planning.",
        owns=[
            "operations analytics and KPI dictionaries",
            "client/principal intelligence and data quality metrics",
            "data warehouse, archival, EVA report mining, and historical case lake option papers",
            "risk indicators, predictive scheduling, and continuous improvement programme",
        ],
        not_own=[
            "operational monitoring and incident runbooks",
            "vehicle evidence facts needed in active case review",
            "AI model evaluation substrate",
        ],
        dependencies=["case-workflow-state", "operations-quality", "governance-security", "vehicle-valuation-data"],
        evidence=[
            Evidence("docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/20_job_sheet_and_operations_analytics.md", "Job sheet and operations analytics plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/21_client_principal_management_intelligence.md", "Client/principal management intelligence plan."),
            Evidence("docs/reference/originalplanning/collision_engineers_bulk_data_research_pack/22_data_quality_confidence_and_explainability.md", "Data quality, confidence, and explainability plan."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_07_advanced_analytics.md", "Advanced analytics and BI plan."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_08_data_warehouse_and_archival.md", "Data warehouse and archival plan."),
        ],
        roadmap=[
            ("S4-S5", ["Start from canonical event/work-item data for operations analytics, data quality, and ROI metrics."]),
            ("S5", ["Add client/principal intelligence and continuous improvement workflows."]),
            ("S6", ["Plan warehouse, EVA mining, risk indicators, scheduling, and BI only after governance and data quality mature."]),
        ],
    ),
    Workspace(
        slug="external-platform-partners",
        title="External Platform Partners",
        purpose="External-facing systems, customer/partner portals, partner APIs, insurer integrations, Audatex partnerships, and partner access controls.",
        owns=[
            "customer self-service portal option papers",
            "external partner API option papers",
            "insurer platform and structured-feed integrations",
            "Audatex/estimating-system partnership discovery",
            "partner access controls and security gates",
        ],
        not_own=[
            "internal intake metadata capture",
            "finance billing logic",
            "estimate parsing of supplied PDFs",
        ],
        dependencies=["governance-security", "case-workflow-state", "intake-storage-integrations", "product-business"],
        evidence=[
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_05_customer_self_service_portal.md", "Customer self-service portal plan."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_06_api_for_external_partners.md", "External partner API plan."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_01_integration_with_insurance_platforms.md", "Insurance platform integration plan."),
            Evidence("docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/original_items/07_03_audatex_and_estimating_system_partnerships.md", "Audatex/estimating-system partnership plan."),
            Evidence("docs/architecture/future_system_convergence.md", "Portal/API guardrails and convergence rule."),
        ],
        roadmap=[
            ("S3", ["Consume source metadata from intake integrations without creating external access yet."]),
            ("S5", ["Write option papers for customer portal, partner API, and high-value partner commitments."]),
            ("S6", ["Pursue insurer/Audatex partnerships only through approved licensed routes and governance sign-off."]),
        ],
    ),
    Workspace(
        slug="product-business",
        title="Product Business",
        purpose="Business framing, discovery, ROI/KPI tracking, client positioning, objections, and defensibility planning.",
        owns=[
            "discovery questions and stakeholder decisions",
            "ROI/KPI tracking and commercial value framing",
            "client pitch and objection handling",
            "conservative product positioning and independence/defensibility wording",
        ],
        not_own=[
            "technical analytics implementation",
            "governance policy ownership",
            "domain feature implementation",
        ],
        dependencies=["analytics-data-platform", "governance-security", "unified-platform", "external-platform-partners"],
        evidence=[
            Evidence("docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/01_project_brief.md", "Project brief and safe framing."),
            Evidence("docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/02_company_business_context.md", "Company/business context and services."),
            Evidence("docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/13_implementation_roadmap_and_roi.md", "Roadmap and ROI evidence."),
            Evidence("docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/14_discovery_questions_and_call_prep.md", "Discovery questions and call-prep source."),
            Evidence("docs/reference/test-context/testprojectcontext/collision-engineers-context-pack/collision-engineers-context-pack/16_client_pitch_and_positioning.md", "Client pitch and positioning source."),
        ],
        roadmap=[
            ("S0-S1", ["Keep CCC positioned as vehicle-damage intake, evidence, and admin support, not autonomous expert judgement."]),
            ("S3-S5", ["Track ROI, adoption, throughput, and provider bottlenecks from operational evidence."]),
            ("S5-S6", ["Prepare client/partner positioning, objections, and commercial prioritisation for external ecosystem work."]),
        ],
    ),
]


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = textwrap.dedent(content).strip()
    if not text:
        path.write_text("", encoding="utf-8")
        return
    first_nonempty = next((line for line in text.splitlines() if line.strip()), "")
    if first_nonempty.startswith("#"):
        lines = []
        for line in text.splitlines():
            if line.startswith("        "):
                lines.append(line[8:])
            elif line.startswith("    "):
                lines.append(line[4:])
            else:
                lines.append(line)
        text = "\n".join(lines)
    path.write_text(text + "\n", encoding="utf-8")


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def evidence_table(evidence: list[Evidence]) -> str:
    rows = ["| Source | Planning evidence |", "| --- | --- |"]
    for item in evidence:
        rows.append(f"| `{item.path}` | {item.note} |")
    return "\n".join(rows)


DEPENDENCY_NOTES = {
    "all workspaces": "Governance/security owns cross-programme risk, data, vendor, licensing, audit, and expert-boundary gates for every workspace.",
    "agent-skills": "Portable skills must stay separate from runtime orchestration and cite approved skill prompts/evaluation examples.",
    "ai-agents": "Workflow agents can only call approved tools/skills under permission, audit, and human-approval boundaries.",
    "ai-platform-tools": "AI-assisted behavior needs model/prompt governance, evaluation data, redaction, and run logging before expansion.",
    "analytics-data-platform": "Analytics must consume reviewed canonical events and approved data products, not raw operational side effects.",
    "automation-centre": "Deterministic automation owns triggers, retries, idempotency, queues, and exception routing used by domain workflows.",
    "case-workflow-state": "Work-item state, review status, blockers, audit events, and approvals are the operational source of truth.",
    "evidence-estimate-review": "Evidence and estimate findings must be reviewable, source-linked, and bounded away from final expert conclusions.",
    "external-platform-partners": "External access, partner APIs, portals, and insurer/estimating-system partnerships require option papers and governance gates.",
    "finance-billing": "Payment, invoice, fee-note, and overdue workflows need finance approval and cannot be hidden inside parser or intake automation.",
    "governance-security": "Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation.",
    "intake-storage-integrations": "Outlook, Box, EVA/Sentry, website/WhatsApp, and spreadsheet bridges own live system boundaries and source capture.",
    "mcp-and-tooling": "MCP/tool exposure must wrap approved adapters with schemas, auth, audit, rate limits, and gateway controls.",
    "operational-core": "Operational Core coordinates the first executable slice and points specialist work to its owning workspace.",
    "operations-quality": "Release, rollback, regression, monitoring, runbooks, pilot, support, and decommissioning gates must be explicit.",
    "parser-extraction": "Extraction work must preserve CE Document Mapper behavior, deterministic rules, canonical schema, and regression coverage.",
    "product-business": "Commercial framing, discovery, objections, ROI, and independence wording shape priority without owning implementation.",
    "provider-principal-config": "Provider/principal presets, routing, aliases, and admin workflows must stay separate from parser mechanics.",
    "unified-platform": "Mature platform convergence coordinates system-wide sequencing and decommissioning only after parity and rollback evidence.",
    "user-experience-interfaces": "Human-facing surfaces must use shared domain contracts and keep UI thin over parser/work-item services.",
    "vehicle-valuation-data": "Vehicle facts and valuation evidence need licensing, confidence, provenance, and human review boundaries.",
}


def source_links(evidence: list[Evidence]) -> str:
    return ", ".join(f"`{item.path}`" for item in evidence)


def todo_table(workspace: Workspace) -> str:
    sources = "<br>".join(f"`{item.path}`" for item in workspace.evidence)
    rows = [
        "| Todo area | Specific source evidence | Required coordination | Acceptance check |",
        "| --- | --- | --- | --- |",
    ]
    for item in workspace.owns:
        rows.append(
            "| "
            + " | ".join(
                [
                    f"- [ ] {item}",
                    sources,
                    ", ".join(f"`{dependency}`" for dependency in workspace.dependencies),
                    "Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner.",
                ]
            )
            + " |"
        )
    return "\n".join(rows)


def dependency_table(workspace: Workspace) -> str:
    rows = ["| Workspace | Why it must be coordinated |", "| --- | --- |"]
    for dependency in workspace.dependencies:
        rows.append(f"| `{dependency}` | {DEPENDENCY_NOTES.get(dependency, 'Coordinate source ownership, sequencing, acceptance criteria, and verification before ticket promotion.')} |")
    return "\n".join(rows)


def roadmap_plan_sections(workspace: Workspace) -> str:
    sections: list[str] = []
    for phase, items in workspace.roadmap:
        sections.append(f"### {phase}")
        sections.append("")
        sections.extend(f"- [ ] {item}" for item in items)
        sections.append("")
    return "\n".join(sections).strip()


def write_workspace(workspace: Workspace) -> None:
    root = ROOT / workspace.path
    write_text(
        root / "README.md",
        f"""
        # {workspace.title} Planning

        Date: {TODAY}
        Status: active planning workspace
        Owner: unassigned
        Created: {TODAY}
        Last reviewed: {TODAY}
        Source links: {", ".join(f"`{item.path}`" for item in workspace.evidence)}
        Roadmap milestone: Whole-programme roadmap
        Dependencies: {", ".join(workspace.dependencies)}
        Expected outputs: source-backed roadmap, scoped tickets, option papers, and archived plans for `{workspace.path}/`
        Acceptance criteria: every promoted item in this workspace cites source evidence and states cross-workspace dependencies
        Verification required: `python tools/verify_scaffold.py`
        Archive target: `{workspace.path}/archived_plans/implemented/`
        Supersedes: none
        Superseded-by: none

        ## Purpose

        {workspace.purpose}

        ## Main Plan

        - Detailed workspace plan: `plan.md`
        - Source map: `source_map.md`
        - Workspace roadmap: `roadmap.md`

        ## Owns

        {bullets(workspace.owns)}

        ## Does Not Own

        {bullets(workspace.not_own)}

        ## Citeable Source Evidence

        {evidence_table(workspace.evidence)}

        ## Cross-Workspace Dependencies

        {bullets(workspace.dependencies)}

        ## Planning Rules

        - Promote work into `tickets/` only after scope, dependencies, acceptance criteria, verification, and governance gates are explicit.
        - Put vendor, privacy, external-access, autonomous-send, payment, AI/RAG, cloud OCR, and partner/API decisions in `option-papers/` first.
        - Archive implemented or superseded work under this workspace's `archived_plans/`.
        - Keep raw evidence immutable; cite source paths instead of copying raw content.
        """,
    )
    write_text(
        root / "plan.md",
        f"""
        # {workspace.title} Plan

        Date: {TODAY}
        Status: active workspace plan
        Owner: unassigned
        Created: {TODAY}
        Last reviewed: {TODAY}
        Source links: {source_links(workspace.evidence)}
        Roadmap milestone: Whole-programme roadmap
        Dependencies: {", ".join(workspace.dependencies)}
        Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `{workspace.path}/`
        Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
        Verification required: `python tools/verify_scaffold.py`
        Archive target: `{workspace.path}/archived_plans/implemented/`
        Supersedes: none
        Superseded-by: none

        ## Planning Decision

        `{workspace.path}/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

        ## Citeable Evidence

        {evidence_table(workspace.evidence)}

        ## Todo Areas

        {todo_table(workspace)}

        ## Sequential Plan

        {roadmap_plan_sections(workspace)}

        ## Dependency Cross-Check

        {dependency_table(workspace)}

        ## Non-Overlap Rules

        The workspace explicitly does not own:

        {bullets(workspace.not_own)}

        If a proposed ticket touches one of those exclusions, link to the owning workspace and keep this workspace as a supporting dependency only.

        ## Source Ownership Rules

        - Cite the source paths above in every promoted ticket, option paper, or roadmap change.
        - Use `source_map.md` to explain how the evidence supports the workspace boundary.
        - Keep generated and historical planning packs reference-only until a scoped ticket or option paper promotes them.
        - Do not edit raw evidence under `docs/reference/raw/collisionrelateddocs/`; create derivatives only under documented derivative paths.

        ## Promotion Gates

        - Use `tickets/` for implementation-ready work with acceptance criteria and verification.
        - Use `option-papers/` before vendor, privacy, external access, autonomous send, payment automation, AI/RAG, cloud OCR/document intelligence, commercial data, or partner/API work.
        - Link governance/security approval where privacy, vendor, retention, licensing, expert-boundary, API security, or autonomous-action risk exists.
        - Link operations-quality approval where release, rollback, regression, monitoring, runbook, support, pilot, or decommissioning evidence is needed.
        """,
    )
    write_text(
        root / "source_map.md",
        f"""
        # {workspace.title} Source Map

        Date: {TODAY}
        Status: active source map
        Owner: unassigned
        Created: {TODAY}
        Last reviewed: {TODAY}
        Source links: {", ".join(f"`{item.path}`" for item in workspace.evidence)}
        Roadmap milestone: Whole-programme roadmap
        Dependencies: {", ".join(workspace.dependencies)}
        Expected outputs: source-to-plan traceability for `{workspace.path}/`
        Acceptance criteria: source evidence can be traced to workspace ownership and roadmap items
        Verification required: `python tools/verify_scaffold.py`
        Archive target: `{workspace.path}/archived_plans/implemented/`
        Supersedes: none
        Superseded-by: none

        ## Source Evidence

        {evidence_table(workspace.evidence)}

        ## Ownership Boundary

        Primary ownership:

        {bullets(workspace.owns)}

        Explicit exclusions:

        {bullets(workspace.not_own)}

        ## Cross-Link Rules

        - Link to `docs/plans/operational-core/` when the item affects first-slice sequencing.
        - Link to `docs/plans/governance-security/` when the item needs privacy, vendor, licensing, retention, expert-boundary, or API security review.
        - Link to `docs/plans/operations-quality/` when release, regression, rollout, monitoring, or runbook gates are required.
        - Link to the domain workspace that owns the business behavior when this workspace provides supporting tooling, skills, UI, or analysis.
        """,
    )
    roadmap_lines: list[str] = []
    for phase, items in workspace.roadmap:
        roadmap_lines.append(f"## {phase}")
        roadmap_lines.append("")
        roadmap_lines.extend(f"- {item}" for item in items)
        roadmap_lines.append("")
    write_text(
        root / "roadmap.md",
        f"""
        # {workspace.title} Roadmap

        Date: {TODAY}
        Status: active workspace roadmap
        Owner: unassigned
        Created: {TODAY}
        Last reviewed: {TODAY}
        Source links: {", ".join(f"`{item.path}`" for item in workspace.evidence)}
        Roadmap milestone: Whole-programme roadmap
        Dependencies: {", ".join(workspace.dependencies)}
        Expected outputs: phased promotion sequence for `{workspace.path}/`
        Acceptance criteria: roadmap stages cite source-backed workspace scope and do not duplicate another workspace's primary ownership
        Verification required: `python tools/verify_scaffold.py`
        Archive target: `{workspace.path}/archived_plans/implemented/`
        Supersedes: none
        Superseded-by: none

        {chr(10).join(roadmap_lines).strip()}

        ## Promotion Gate

        Any item promoted from this roadmap must cite `source_map.md`, name dependencies, define acceptance criteria, and state whether governance/security or operations-quality approval is required.
        """,
    )
    write_text(
        root / "tickets" / "README.md",
        f"""
        # {workspace.title} Tickets

        Use this folder for executable implementation tickets owned by `{workspace.path}/`.

        Each ticket must include status, owner, created date, last reviewed date, source links, roadmap milestone, dependencies, expected outputs, acceptance criteria, verification required, archive target, and supersedes/superseded-by fields.
        """,
    )
    write_text(
        root / "option-papers" / "README.md",
        f"""
        # {workspace.title} Option Papers

        Use this folder for decisions that must be explored before implementation.

        Option papers are required before work involving vendors, external access, live writes, autonomous sends, payment automation, cloud OCR/document intelligence, AI/RAG, commercial data sources, or partner APIs.
        """,
    )
    write_text(root / "archived_plans" / "implemented" / ".gitkeep", "")
    write_text(root / "archived_plans" / "superseded" / ".gitkeep", "")


def write_operational_core_readme() -> None:
    write_text(
        ROOT / "docs/plans/operational-core/README.md",
        f"""
        # Operational Core Planning

        Date: {TODAY}
        Status: active coordination workspace
        Owner: unassigned
        Created: {TODAY}
        Last reviewed: {TODAY}
        Source links: `docs/plans/operational-core/source_synthesis.md`, `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md`, `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`
        Roadmap milestone: Operational Core MVP coordination
        Dependencies: parser-extraction, provider-principal-config, case-workflow-state, intake-storage-integrations, user-experience-interfaces, operations-quality, governance-security
        Expected outputs: cross-workspace sequencing, dependency coordination, and first-slice acceptance gates
        Acceptance criteria: Operational Core coordinates owning workspaces without duplicating their active domain tickets
        Verification required: `python tools/verify_scaffold.py`
        Archive target: `docs/plans/operational-core/archived_plans/implemented/`
        Supersedes: none
        Superseded-by: none

        Operational Core is the first executable slice of CCC. After the planning workspace expansion, it coordinates sequencing across owning workspaces rather than permanently owning every parser, provider, workflow, integration, UI, intelligence, analytics, or partner ticket.

        ## Coordination Responsibilities

        - Maintain `source_synthesis.md` as the source-promotion and canonical-destination map.
        - Maintain a cross-workspace backlog index for the first-slice delivery sequence.
        - Keep MVP interlock visible across parser, provider config, work item state, review, export, package, UI, governance, and operations gates.
        - Link to the owning workspace when a ticket moves out of Operational Core.

        ## Current Source Evidence

        | Source | Planning evidence |
        | --- | --- |
        | `docs/plans/operational-core/source_synthesis.md` | Current source promotion map. |
        | `docs/plans/operational-core/tickets/backlog_index.md` | Current phased backlog before full ticket relocation. |
        | `docs/architecture/mvp_interlock.md` | Parser, UI, CLI, provider admin, work-item, review, and package interlock. |
        | `docs/roadmap.md` | Whole-programme roadmap. |
        """,
    )


def write_programme_roadmap() -> None:
    source_basis = [
        "docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md",
        "docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md",
        "docs/plans/operational-core/source_synthesis.md",
        "docs/architecture/future_system_convergence.md",
        "docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/14_IMPLEMENTATION_ROADMAP.md",
        "docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/02_prioritised_roadmap.md",
    ]
    workspace_entry_rows = "\n".join(
        f"| `{workspace.path}/` | `{workspace.path}/plan.md` | {workspace.purpose} |"
        for workspace in WORKSPACES
    )
    roadmap = f"""
    # Roadmap

    Date: 2026-05-24
    Status: active programme roadmap
    Owner: unassigned
    Created: 2026-05-24
    Last reviewed: 2026-05-24
    Source links: `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md`, `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`, `docs/plans/operational-core/source_synthesis.md`, `docs/architecture/future_system_convergence.md`, `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/14_IMPLEMENTATION_ROADMAP.md`, `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/02_prioritised_roadmap.md`
    Roadmap milestone: Whole-programme roadmap
    Dependencies: source manifest, workspace source maps, governance/security gates, operations-quality gates
    Expected outputs: sequential implementation and planning order for all reference-derived workspaces
    Acceptance criteria: every roadmap section points to an owning workspace and source-backed evidence; high-risk work is gated before implementation
    Verification required: `python tools/verify_scaffold.py`
    Archive target: owning workspace `archived_plans/implemented/`
    Supersedes: previous P0-P5-only roadmap structure
    Superseded-by: none

    CCC starts with vehicle-damage instruction parsing and evidence preparation, then expands through controlled workflow, integrations, intelligence, AI/tooling, external ecosystem, analytics, and mature platform convergence. Collision Engineers do not do personal injury or KADOE work; those workflows remain out of scope.

    ## Current Status

    Current position: Section 0 - Taxonomy And Planning Scaffold, final pre-parser documentation and handoff alignment.

    Current milestone: make the repository documentation, roadmap, source manifests, workspace ownership, and parser handoff rules reliable enough for parser MVP implementation to start from a known baseline.

    Parser implementation status: not started. The active parser MVP plan is `docs/plans/parser-extraction/parser-mvp/plan.md`; the operational-core parser path is only a compatibility stub.

    Pre-parser readiness gates: repository documentation lifecycle rules must be explicit, this Current Status section must be up to date, source manifests must match the working tree, scaffold verification and scaffold contract tests must pass, and parser work should start from a committed/pushed documentation baseline.

    Optional pre-parser action: decide whether to create a portable task-start/navigation skill before parser implementation. This is not a parser blocker unless the project requires the same task-start checklist to be enforced outside this repository's `AGENTS.md`.

    ## Source Basis

    | Source | Why it is used |
    | --- | --- |
    | `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md` | Exhaustive ledger of reference-derived ideas and phases. |
    | `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md` | Approved workspace taxonomy and split-out plan. |
    | `docs/plans/operational-core/source_synthesis.md` | Current source-promotion map and generated-pack disposition. |
    | `docs/architecture/future_system_convergence.md` | Convergence spine and scope guardrails for future modules. |
    | `docs/reference/test-context/testprojectcontext/collision_project_context_pack/collision_project_context_pack/14_IMPLEMENTATION_ROADMAP.md` | Incremental delivery strategy from discovery through expansion. |
    | `docs/reference/originalplanning/phase7_expanded_markdown_plan/phase7_expanded_markdown_plan/02_prioritised_roadmap.md` | Longer-horizon platform, portal, analytics, partner, and governance sequencing. |

    ## Workspace Plan Entry Points

    | Workspace | Detailed plan | Purpose |
    | --- | --- | --- |
    {workspace_entry_rows}

    ## Section 0 - Taxonomy And Planning Scaffold

    Owning workspaces: `initial-repo-setup`, `operational-core`, all newly created planning workspaces.

    - Create workspace folders, README files, source maps, roadmaps, tickets folders, option-paper folders, and archives.
    - Update `docs/plans/_index.md`, `docs/docs_index.md`, `docs/repo_map.json`, `docs/source_manifest.*`, and scaffold verification.
    - Add source-backed ownership matrix so each future item has one primary planning home.

    ## Section 1 - Foundation And Governance

    Owning workspaces: `operational-core`, `governance-security`, `operations-quality`, `product-business`.

    - Lock contracts, ADRs, option papers, data map, vendor register, release/rollback baseline, and scope guardrails.
    - Keep raw evidence immutable and source-backed.
    - Gate cloud OCR, AI processing, live APIs, partner access, payment automation, WhatsApp sends, and external writes before implementation.

    ## Section 2 - Parser, Provider, And Corpus Core

    Owning workspaces: `parser-extraction`, `provider-principal-config`, `operations-quality`, `user-experience-interfaces`.

    - Maintain active parser MVP planning in `parser-extraction`; the old operational-core parser path is only a compatibility stub.
    - Preserve current CE Document Mapper behavior, all 26 provider presets, deterministic-first parsing, and private real corpus tests.
    - Split provider/principal, garage, routing, provider-admin, and provider coverage work into `provider-principal-config`.
    - Establish regression harness and release gates before broad automation.

    ## Section 3 - Operational Core First Slice

    Owning workspaces: `case-workflow-state`, `user-experience-interfaces`, `intake-storage-integrations`, coordinated by `operational-core`.

    - Build work item state, review queue, audit events, missing-info blockers, staff parser UI, CLI parity, EVA JSON export, and Box-ready package.
    - Keep UI and CLI thin over shared parser and service contracts.
    - Use reviewed data as the gate before export, packaging, or later live integration.

    ## Section 4 - Intake And Live Integration Boundaries

    Owning workspaces: `intake-storage-integrations`, `mcp-and-tooling`, `automation-centre`, `operations-quality`, `governance-security`.

    - Plan Outlook intake, live Box upload, EVA/Sentry adapter, website/WhatsApp metadata capture, and spreadsheet bridge.
    - Add dry-run/sandbox tests, idempotency, duplicate prevention, runbooks, and manual approval gates.
    - Keep adapter implementation separate from MCP exposure and agent orchestration.

    ## Section 5 - Evidence, Vehicle, Engineer Pack, Communications

    Owning workspaces: `evidence-estimate-review`, `vehicle-valuation-data`, `engineer-communications`, `agent-skills`, `user-experience-interfaces`.

    - Promote image quality/order/duplicate review, visible VRM hints, estimate/ABP review, DVLA/DVSA, MOT/mileage, valuation evidence, salvage context, engineer packs, and communication drafting.
    - Keep all outputs source-linked and reviewable.
    - Preserve engineer judgement and human sign-off for technical conclusions, valuation, roadworthiness, causation, and final reports.

    ## Section 6 - AI Platform, Tools, And Agents

    Owning workspaces: `agent-skills`, `ai-platform-tools`, `mcp-and-tooling`, `ai-agents`, `automation-centre`, `governance-security`.

    - Specify portable skills separately from workflow agents so they can be reused by the CE platform, approved agents, ChatGPT, Claude Desktop, or other approved AI front ends.
    - Build model/prompt versioning, eval datasets, redaction, correction loops, and AI run logging before expanding AI-assisted behavior.
    - Use bounded agents only with approved tools/skills, permissions, audit, and human approval boundaries.

    ## Section 7 - Finance And External Ecosystem

    Owning workspaces: `finance-billing`, `external-platform-partners`, `provider-principal-config`, `governance-security`, `product-business`.

    - Record current portal/payment/invoice evidence as metadata first.
    - Plan invoice/fee-note generation, fee rules, finance approvals, payment status, and overdue visibility.
    - Put portal, partner API, insurer integration, Audatex partnership, payment automation, and partner access into option papers before implementation.

    ## Section 8 - Analytics And Continuous Improvement

    Owning workspaces: `analytics-data-platform`, `operations-quality`, `product-business`, `governance-security`.

    - Build analytics only from canonical events, reviewed work items, package metadata, and approved data sources.
    - Track operations analytics, provider/principal intelligence, data quality, ROI, queue health, and continuous improvement.
    - Defer warehouse, EVA mining, risk indicators, scheduling models, and broad BI until retention, licensing, and data-quality controls are mature.

    ## Section 9 - Unified Platform And Decommissioning

    Owning workspaces: `unified-platform`, `operations-quality`, all specialist workspaces.

    - Coordinate mature end-to-end platform convergence across case management, workflow, automation, role model, UI/PWA/mobile, integrations, analytics, and governance.
    - Retire spreadsheet or legacy mapper only after parity, audit, rollback, support ownership, and adoption evidence.
    - Keep legacy decommissioning as a controlled release milestone, not a side effect of early MVP delivery.

    ## Cross-Workspace Guardrails

    - Every all-ideas row has one primary workspace and may have supporting cross-links.
    - Operational Core coordinates first-slice sequencing; it does not permanently own specialist domain work after relocation.
    - Governance-gated work starts in option papers, not implementation tickets.
    - No autonomous EVA/Sentry submit, payment chasing, WhatsApp sending, partner API, portal automation, cloud OCR, valuation provider, or broad AI/RAG work bypasses approval gates.
    - AI outputs assist with reading, drafting, summarising, or review prompts; named humans retain expert judgement and final approvals.
    """
    write_text(ROOT / "docs/roadmap.md", roadmap)
    write_text(
        ROOT / "docs/plans/roadmap.md",
        roadmap.replace("# Roadmap", "# Plans Roadmap", 1)
        + "\n\nThis file mirrors the root roadmap so planning workspace navigation has a local roadmap entry point.\n",
    )
    write_text(
        ROOT / "docs/plans/workspace_ownership_matrix.md",
        "# Workspace Ownership Matrix\n\n"
        f"Date: {TODAY}\n"
        "Status: active ownership matrix\n"
        "Owner: unassigned\n"
        f"Created: {TODAY}\n"
        f"Last reviewed: {TODAY}\n"
        f"Source links: {', '.join(f'`{source}`' for source in source_basis)}\n"
        "Roadmap milestone: Whole-programme roadmap\n"
        "Dependencies: all workspace source maps\n"
        "Expected outputs: one primary workspace per reference-derived planning area\n"
        "Acceptance criteria: ownership boundaries prevent duplicate active tickets and source evidence is citeable\n"
        "Verification required: `python tools/verify_scaffold.py`\n"
        "Archive target: owning workspace `archived_plans/implemented/`\n"
        "Supersedes: none\n"
        "Superseded-by: none\n\n"
        "## Matrix\n\n"
        "| Workspace | Primary owns | Explicit exclusions | Key source evidence |\n"
        "| --- | --- | --- | --- |\n"
        + "\n".join(
            "| `{}` | {} | {} | {} |".format(
                f"{workspace.path}/",
                "; ".join(workspace.owns),
                "; ".join(workspace.not_own),
                "; ".join(f"`{item.path}`" for item in workspace.evidence[:3]),
            )
            for workspace in WORKSPACES
        )
        + "\n",
    )


def write_indexes() -> None:
    rows = "\n".join(
        f"| {workspace.title} | `{workspace.path}/` | {workspace.purpose} |"
        for workspace in WORKSPACES
    )
    write_text(
        ROOT / "docs/plans/_index.md",
        f"""
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
        {rows}

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
        """,
    )
    write_text(
        ROOT / "docs/docs_index.md",
        """
        # Documentation Index

        This is the primary human navigation file for CCC documentation.

        ## Quick Start

        - Product scope and current milestone: `README.md` and `docs/roadmap.md`.
        - Plan workspace index: `docs/plans/_index.md`.
        - Workspace ownership matrix: `docs/plans/workspace_ownership_matrix.md`.
        - Initial setup planning: `docs/plans/initial-repo-setup/README.md`.
        - Operational Core coordination: `docs/plans/operational-core/README.md`.
        - Active programme source map: `docs/plans/operational-core/source_synthesis.md`.
        - Approved folder taxonomy source: `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`.
        - Parser MVP plan: `docs/plans/parser-extraction/parser-mvp/plan.md`.
        - Parser MVP evidence and divergence review: `docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md`.
        - Active backlog before ticket relocation: `docs/plans/operational-core/tickets/backlog_index.md`.
        - Agent path map: `docs/repo_map.json`.
        - Full source inventory: `docs/source_manifest.md`, `docs/source_manifest.csv`, and `docs/source_manifest.json`.

        ## Active Work

        | Area | Path | Use |
        | --- | --- | --- |
        | Plans | `docs/plans/_index.md` | Active plan workspaces and archived plans. |
        | Initial Repo Setup | `docs/plans/initial-repo-setup/` | Pre-code repository setup, documentation scaffold, and exhaustive reference idea planning. |
        | Operational Core | `docs/plans/operational-core/` | First-slice coordination, source synthesis, and cross-workspace backlog routing. |
        | Parser Extraction | `docs/plans/parser-extraction/` | Active parser MVP, extraction rules, provider-rule execution, parser parity, and regression planning. |
        | Architecture | `docs/architecture/` | System architecture and programme boundaries. |
        | Contracts | `docs/contracts/` | Versioned schemas and integration contracts. |
        | Decisions | `docs/decisions/` | ADRs and option papers. |
        | Requirements | `docs/requirements/` | Business requirements and open questions. |
        | Operations | `docs/operations/` | Runbooks, monitoring, release, rollback, and spreadsheet companion notes. |
        | Security | `docs/security/` | Data map, vendor register, DPIA, safety review, and API security. |

        ## Planning Workspaces

        See `docs/plans/_index.md` for the full active workspace table. Each workspace has `README.md`, `source_map.md`, `roadmap.md`, `tickets/`, `option-papers/`, and `archived_plans/`.

        ## Reference Material

        | Area | Path | Use |
        | --- | --- | --- |
        | Raw evidence | `docs/reference/raw/collisionrelateddocs/` | Immutable source files. Do not edit in place. |
        | Normalized companions | `docs/reference/normalized/` | Generated Markdown companions for raw evidence. |
        | Reference data | `docs/reference/data/` | Provider matrix and extracted Jam/FigJam derivatives. |
        | Original planning | `docs/reference/originalplanning/` | Historical/generated planning packs; reference-only unless promoted. |
        | Test context | `docs/reference/test-context/` | Historical test repositories and context packs. |

        ## Quality Rules

        - At task start, read the roadmap, repo map, owning workspace plan, active tickets, and relevant source evidence before changing files.
        - At completion of any large task, update `docs/roadmap.md`, the owning plan/ticket, `docs/docs_index.md`, `docs/repo_map.json`, affected key docs, and `docs/source_manifest.*`.
        - Update `docs/source_manifest.*` when source files, generated companions, active docs, or archives change.
        - Promote ideas from reference material into an owning workspace before treating them as active implementation scope.
        - Keep raw evidence immutable and create derivatives under `docs/reference/normalized/` or `docs/reference/data/`.
        - Run `python tools/verify_scaffold.py` after documentation structure changes.
        """,
    )
    repo_map = {
        "version": 2,
        "updated": TODAY,
        "entry_points": {
            "human_index": "docs/docs_index.md",
            "machine_map": "docs/repo_map.json",
            "source_manifest": "docs/source_manifest.md",
            "roadmap": "docs/roadmap.md",
            "plans_index": "docs/plans/_index.md",
            "workspace_ownership_matrix": "docs/plans/workspace_ownership_matrix.md",
        },
        "plans": {
            "index": "docs/plans/_index.md",
            "roadmap": "docs/plans/roadmap.md",
            "workspace_ownership_matrix": "docs/plans/workspace_ownership_matrix.md",
            "workspace_expansion_plan": "docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md",
            "initial_repo_setup": {
                "root": "docs/plans/initial-repo-setup",
                "readme": "docs/plans/initial-repo-setup/README.md",
                "documentation_scaffold": "docs/plans/initial-repo-setup/documentation-scaffold",
                "reference_audit": "docs/plans/initial-repo-setup/reference-audit",
                "tickets": "docs/plans/initial-repo-setup/tickets",
                "implemented_archive": "docs/plans/initial-repo-setup/archived_plans/implemented",
                "superseded_archive": "docs/plans/initial-repo-setup/archived_plans/superseded",
            },
            "operational_core": {
                "root": "docs/plans/operational-core",
                "readme": "docs/plans/operational-core/README.md",
                "source_synthesis": "docs/plans/operational-core/source_synthesis.md",
                "parser_mvp_plan_stub": "docs/plans/operational-core/parser-mvp/plan.md",
                "tickets": "docs/plans/operational-core/tickets",
                "implemented_archive": "docs/plans/operational-core/archived_plans/implemented",
                "superseded_archive": "docs/plans/operational-core/archived_plans/superseded",
            },
            "workspaces": {
                workspace.slug.replace("-", "_"): {
                    "root": workspace.path,
                    "readme": f"{workspace.path}/README.md",
                    "plan": f"{workspace.path}/plan.md",
                    "source_map": f"{workspace.path}/source_map.md",
                    "roadmap": f"{workspace.path}/roadmap.md",
                    "tickets": f"{workspace.path}/tickets",
                    "option_papers": f"{workspace.path}/option-papers",
                    "implemented_archive": f"{workspace.path}/archived_plans/implemented",
                    "superseded_archive": f"{workspace.path}/archived_plans/superseded",
                }
                for workspace in WORKSPACES
            },
            "active_parser_mvp": {
                "plan": "docs/plans/parser-extraction/parser-mvp/plan.md",
                "evidence_review": "docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md",
            },
        },
        "reference": {
            "index": "docs/reference/_index.md",
            "raw_evidence": "docs/reference/raw/collisionrelateddocs",
            "normalized_companions": "docs/reference/normalized",
            "reference_data": "docs/reference/data",
            "provider_coverage_matrix": "docs/reference/data/provider_coverage_matrix.md",
            "original_planning": "docs/reference/originalplanning",
            "original_planning_index": "docs/reference/originalplanning_index.md",
            "test_context": "docs/reference/test-context",
        },
        "active_docs": {
            "architecture": "docs/architecture",
            "contracts": "docs/contracts",
            "decisions": "docs/decisions",
            "requirements": "docs/requirements",
            "operations": "docs/operations",
            "security": "docs/security",
            "glossary": "docs/glossary.md",
        },
        "rules": {
            "raw_evidence": "Do not edit files under docs/reference/raw/collisionrelateddocs in place.",
            "reference_material": "Reference material is not active scope unless promoted into plans, tickets, architecture, contracts, or decisions.",
            "workspace_ownership": "Every reference-derived idea should have exactly one primary planning workspace, with supporting cross-links where needed.",
            "manifest": "Update docs/source_manifest.md, docs/source_manifest.csv, and docs/source_manifest.json whenever source files, generated companions, active docs, or archives change.",
        },
    }
    write_text(ROOT / "docs/repo_map.json", json.dumps(repo_map, indent=2))


def main() -> None:
    for workspace in WORKSPACES:
        write_workspace(workspace)
    write_operational_core_readme()
    write_programme_roadmap()
    write_indexes()


if __name__ == "__main__":
    main()
