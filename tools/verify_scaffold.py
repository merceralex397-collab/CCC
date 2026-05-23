from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ccc_parser.core import ParserCore
from ccc_parser.providers import load_provider_presets


REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    ".gitignore",
    ".gitattributes",
    "pyproject.toml",
    "docs/source_manifest.md",
    "docs/source_manifest.csv",
    "docs/roadmap.md",
    "docs/architecture/overview.md",
    "docs/architecture/programme_architecture.md",
    "docs/architecture/mvp_interlock.md",
    "docs/architecture/governance_security.md",
    "docs/architecture/future_system_convergence.md",
    "docs/architecture/parser_ui_cli.md",
    "docs/planning/source_synthesis.md",
    "docs/plans/parser_mvp_implementation_plan.md",
    "docs/contracts/parser_result_v1.md",
    "docs/contracts/eva_export_contract.md",
    "docs/contracts/eva_export_contract_v1.md",
    "docs/contracts/storage_adapter_contract.md",
    "docs/contracts/storage_adapter_contract_v1.md",
    "docs/contracts/work_item_contract_v1.md",
    "docs/contracts/provider_principal_config_contract_v1.md",
    "docs/contracts/review_audit_event_contract_v1.md",
    "docs/contracts/evidence_package_contract_v1.md",
    "docs/contracts/extraction_adapter_contract_v1.md",
    "docs/decisions/0003-operational-core-mvp.md",
    "docs/decisions/0004-ground-up-compatible-parser-rebuild.md",
    "docs/decisions/0005-shared-internal-app-local-accounts.md",
    "docs/decisions/0006-box-package-before-live-upload.md",
    "docs/decisions/0007-deterministic-first-parser.md",
    "docs/decisions/0008-private-real-corpus-only.md",
    "docs/decisions/options/ui_platform_options.md",
    "docs/decisions/options/backend_stack_options.md",
    "docs/decisions/options/state_store_options.md",
    "docs/decisions/options/cloud_document_intelligence_options.md",
    "docs/tickets/backlog_index.md",
    "docs/tickets/p0-foundation.md",
    "docs/tickets/p1-operational-core-mvp.md",
    "docs/tickets/p2-parser-hardening-provider-parity.md",
    "docs/tickets/p3-integrations-storage-eva-intake.md",
    "docs/tickets/p4-intelligence-engineer-communications.md",
    "docs/tickets/p5-platform-expansion.md",
    "docs/data/provider_coverage_matrix.md",
    "docs/reference/generated_packs_index.md",
    "docs/security/source_safety_review.md",
    "docs/security/data_map.md",
    "docs/security/dpia_vendor_governance.md",
    "docs/security/vendor_register.md",
    "docs/security/api_security_standard.md",
    "docs/operations/release_and_rollback.md",
    "docs/operations/monitoring_runbooks.md",
    "docs/operations/runbooks/outlook-intake-stopped.md",
    "docs/operations/runbooks/box-upload-failure.md",
    "docs/operations/runbooks/eva-rejected-payload.md",
    "src/ccc_parser/core.py",
    "src/ccc_parser/cli.py",
    "src/ccc_parser/ui/app.py",
    "tests/test_scaffold_contracts.py",
    "archive/plans/implemented/2026-05-23-implemented-initrepoplan.md",
]

GENERATED_PACKS = [
    "ce_phase4_agents_reviewed_plan",
    "ce_system_plans_enhanced",
    "cedocumentmapper_rebuild_plan_pack_all_zips",
    "collision_engineers_ai_tools_plans_markdown",
    "collision_engineers_bulk_data_research_pack",
    "originalplans_output",
    "phase7_expanded_markdown_plan",
    "testprojectcontext",
]

RESEARCH_DOCS = [
    "docs/research/gptdeepresearch.md",
    "docs/research/gptevadeepresearch.md",
    "docs/research/siderpdf.md",
]

PROVIDER_PRESETS = [
    "ALISON",
    "ALS",
    "AMS",
    "AX",
    "BC",
    "BLACK",
    "CNX (Engineers)",
    "DFD",
    "EVA (Engineers)",
    "FW (Garage)",
    "FW (Solicitor)",
    "HDUK",
    "KBS",
    "KERR",
    "KMR",
    "MP (Branded)",
    "MP (Simple)",
    "OAK",
    "PCH (Lawshield)",
    "PCH (Performance)",
    "QCL",
    "QDOS",
    "RJS",
    "SBL",
    "SWAN",
    "TEN",
]

PARSER_PLAN_TERMS = [
    "PDF",
    "DOCX",
    "DOC",
    "MSG",
    "EML",
    "images",
    "batch",
    "PyMuPDF",
    "pdfplumber",
    "pypdf",
    "OCR only",
    "DD/MM/YYYY",
    "six-line",
    "EVA JSON field order",
    "UI/CLI",
    "deterministic-first",
    "private real corpus",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def read_doc(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require_terms(text: str, terms: list[str], context: str) -> None:
    missing = [term for term in terms if term not in text]
    require(not missing, f"{context} missing terms: {missing}")


def require_scope_guardrails() -> None:
    allowed_markers = [
        "out of scope",
        "must not",
        "does not plan",
        "do not plan",
        "do not add",
        "no personal injury",
        "no pi",
        "not plan",
        "confirm no",
    ]
    checked_roots = [
        "README.md",
        "AGENTS.md",
        "docs/architecture",
        "docs/contracts",
        "docs/decisions",
        "docs/planning",
        "docs/plans",
        "docs/roadmap.md",
        "docs/security",
        "docs/tickets",
    ]
    files: list[Path] = []
    for item in checked_roots:
        path = ROOT / item
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(path.rglob("*.md"))
    bad_lines: list[str] = []
    for path in files:
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            lowered = line.lower()
            if "personal injury" in lowered or "kadoe" in lowered:
                if not any(marker in lowered for marker in allowed_markers):
                    bad_lines.append(f"{path.relative_to(ROOT).as_posix()}:{line_number}: {line}")
    require(not bad_lines, "Personal injury/KADOE references must be explicit out-of-scope guardrails: " + repr(bad_lines[:5]))


def main() -> int:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]
    require(not missing, f"Missing required paths: {missing}")

    ambiguous_roots = [
        "originalplans_output",
        "ce_system_plans_enhanced",
        "ce_phase4_agents_reviewed_plan",
        "phase7_expanded_markdown_plan",
        "collision_engineers_ai_tools_plans_markdown",
        "collision_engineers_bulk_data_research_pack",
        "cedocumentmapper_rebuild_plan_pack_all_zips",
        "testprojectcontext",
    ]
    still_root = [path for path in ambiguous_roots if (ROOT / path).exists()]
    require(not still_root, f"Generated/reference packs still at repository root: {still_root}")

    providers = load_provider_presets(ROOT / "collisionrelateddocs/Settings Backup/providers.json")
    require(len(providers) == 26, f"Expected 26 providers, got {len(providers)}")
    provider_names = {provider.name for provider in providers}
    require(provider_names == set(PROVIDER_PRESETS), f"Provider preset names changed: {sorted(provider_names)}")

    manifest_rows = list(csv.DictReader((ROOT / "docs/source_manifest.csv").open(encoding="utf-8")))
    require(any(row["path"].startswith("collisionrelateddocs/Instructions/") for row in manifest_rows), "Instruction corpus missing from manifest")
    require(any(row["normalized_companion"] for row in manifest_rows if row["path"].startswith("collisionrelateddocs/")), "No normalized companions recorded")

    matrix_rows = list(csv.DictReader((ROOT / "docs/data/provider_coverage_matrix.csv").open(encoding="utf-8")))
    require(any(row["code"] == "ACSP" and row["parser_covered"] == "no" for row in matrix_rows), "ACSP uncovered status missing")
    require(any(row["code"] == "WOODLANDS" and row["parser_covered"] == "no" for row in matrix_rows), "WOODLANDS uncovered status missing")

    plan_text = (ROOT / "archive/plans/implemented/2026-05-23-implemented-initrepoplan.md").read_text(encoding="utf-8")
    require("Status: implemented" in plan_text, "Archived initrepoplan missing implemented status")

    synthesis_text = read_doc("docs/planning/source_synthesis.md")
    require_terms(synthesis_text, GENERATED_PACKS, "Source synthesis")
    require_terms(synthesis_text, RESEARCH_DOCS, "Source synthesis")

    parser_plan = read_doc("docs/plans/parser_mvp_implementation_plan.md")
    require_terms(parser_plan, PROVIDER_PRESETS, "Parser MVP plan")
    require_terms(parser_plan, PARSER_PLAN_TERMS, "Parser MVP plan")

    for ticket_file in [
        "docs/tickets/p0-foundation.md",
        "docs/tickets/p1-operational-core-mvp.md",
        "docs/tickets/p2-parser-hardening-provider-parity.md",
        "docs/tickets/p3-integrations-storage-eva-intake.md",
        "docs/tickets/p4-intelligence-engineer-communications.md",
        "docs/tickets/p5-platform-expansion.md",
    ]:
        ticket_text = read_doc(ticket_file)
        require_terms(
            ticket_text,
            ["Status:", "Owner:", "Created:", "Sources:", "Dependencies:", "Expected outputs:", "Acceptance criteria:", "Verification:", "Archive target:"],
            ticket_file,
        )

    require_scope_guardrails()

    core = ParserCore(ROOT / "collisionrelateddocs/Settings Backup/providers.json")
    require(len(core.providers) == 26, "ParserCore did not load providers")

    json.loads((ROOT / "docs/source_manifest.json").read_text(encoding="utf-8"))
    manifest_paths = {row["path"] for row in manifest_rows}
    require(all(path in manifest_paths for path in REQUIRED_PATHS), "Source manifest missing required active docs")
    print("Scaffold verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
