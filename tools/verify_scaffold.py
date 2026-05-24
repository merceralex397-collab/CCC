from __future__ import annotations

import csv
import json
import subprocess
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
    "docs/docs_index.md",
    "docs/repo_map.json",
    "docs/source_manifest.md",
    "docs/source_manifest.csv",
    "docs/roadmap.md",
    "docs/plans/_index.md",
    "docs/plans/roadmap.md",
    "docs/plans/workspace_ownership_matrix.md",
    "docs/plans/initial-repo-setup/README.md",
    "docs/plans/initial-repo-setup/documentation-scaffold/plan.md",
    "docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md",
    "docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md",
    "docs/plans/initial-repo-setup/tickets/README.md",
    "docs/plans/initial-repo-setup/archived_plans/implemented/.gitkeep",
    "docs/plans/initial-repo-setup/archived_plans/implemented/2026-05-23-implemented-initrepoplan.md",
    "docs/plans/initial-repo-setup/archived_plans/implemented/2026-05-23-implemented-repository-restructure.md",
    "docs/plans/initial-repo-setup/archived_plans/superseded/.gitkeep",
    "docs/architecture/overview.md",
    "docs/architecture/programme_architecture.md",
    "docs/architecture/mvp_interlock.md",
    "docs/architecture/governance_security.md",
    "docs/architecture/future_system_convergence.md",
    "docs/architecture/parser_ui_cli.md",
    "docs/plans/operational-core/source_synthesis.md",
    "docs/plans/operational-core/parser-mvp/plan.md",
    "docs/plans/parser-extraction/parser-mvp/plan.md",
    "docs/plans/parser-extraction/parser-mvp/adjacent-parser-and-inspection-location-review.md",
    "docs/plans/initial-repo-setup/tickets/p0-repo-navigation-and-parser-handoff-alignment.md",
    "docs/plans/parser-extraction/tickets/p0-parser-mvp-plan-enhancement-and-adjacent-evidence.md",
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
    "docs/plans/operational-core/tickets/backlog_index.md",
    "docs/plans/operational-core/tickets/p0-foundation.md",
    "docs/plans/operational-core/tickets/p1-operational-core-mvp.md",
    "docs/plans/operational-core/tickets/p2-parser-hardening-provider-parity.md",
    "docs/plans/operational-core/tickets/p3-integrations-storage-eva-intake.md",
    "docs/plans/operational-core/tickets/p4-intelligence-engineer-communications.md",
    "docs/plans/operational-core/tickets/p5-platform-expansion.md",
    "docs/reference/data/provider_coverage_matrix.md",
    "docs/reference/originalplanning_index.md",
    "docs/reference/_index.md",
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
    "docs/plans/operational-core/archived_plans/superseded/.gitkeep",
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

PLANNED_WORKSPACE_TERMS = [
    "docs/plans/unified-platform/",
    "docs/plans/automation-centre/",
    "docs/plans/parser-extraction/",
    "docs/plans/case-workflow-state/",
    "docs/plans/provider-principal-config/",
    "docs/plans/intake-storage-integrations/",
    "docs/plans/evidence-estimate-review/",
    "docs/plans/vehicle-valuation-data/",
    "docs/plans/engineer-communications/",
    "docs/plans/ai-agents/",
    "docs/plans/mcp-and-tooling/",
    "docs/plans/agent-skills/",
    "docs/plans/ai-platform-tools/",
    "docs/plans/user-experience-interfaces/",
    "docs/plans/finance-billing/",
    "docs/plans/governance-security/",
    "docs/plans/operations-quality/",
    "docs/plans/analytics-data-platform/",
    "docs/plans/external-platform-partners/",
    "docs/plans/product-business/",
]

WORKSPACE_REQUIRED_SUFFIXES = [
    "README.md",
    "plan.md",
    "source_map.md",
    "roadmap.md",
    "tickets/README.md",
    "option-papers/README.md",
    "archived_plans/implemented/.gitkeep",
    "archived_plans/superseded/.gitkeep",
]

for workspace_path in PLANNED_WORKSPACE_TERMS:
    workspace_root = workspace_path.rstrip("/")
    REQUIRED_PATHS.extend(f"{workspace_root}/{suffix}" for suffix in WORKSPACE_REQUIRED_SUFFIXES)

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

PLAN_METADATA_TERMS = [
    "Status:",
    "Owner:",
    "Created:",
    "Last reviewed:",
    "Source links:",
    "Roadmap milestone:",
    "Dependencies:",
    "Expected outputs:",
    "Acceptance criteria:",
    "Verification required:",
    "Archive target:",
    "Supersedes:",
    "Superseded-by:",
]

FALLBACK_IGNORED_MANIFEST_PARTS = {
    ".git",
    ".obsidian",
    ".pytest_cache",
    "__pycache__",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "env",
    "outputs",
    "tmp",
    "dist",
    "build",
    "node_modules",
}
FALLBACK_IGNORED_MANIFEST_NAMES = {".DS_Store", "Thumbs.db"}
FALLBACK_IGNORED_MANIFEST_SUFFIXES = {".pyc", ".pyo", ".pyd", ".log", ".tmp", ".bak"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def read_doc(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require_terms(text: str, terms: list[str], context: str) -> None:
    missing = [term for term in terms if term not in text]
    require(not missing, f"{context} missing terms: {missing}")


def is_fallback_ignored_manifest_artifact(path: Path) -> bool:
    parts = path.relative_to(ROOT).parts
    if set(parts) & FALLBACK_IGNORED_MANIFEST_PARTS:
        return True
    if any(part.endswith(".egg-info") for part in parts):
        return True
    name = path.name
    if name == ".env.example":
        return False
    if name == ".env" or name.startswith(".env."):
        return True
    if name in FALLBACK_IGNORED_MANIFEST_NAMES:
        return True
    return any(name.endswith(suffix) for suffix in FALLBACK_IGNORED_MANIFEST_SUFFIXES)


def manifest_candidate_paths() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        candidates = []
        for path in ROOT.rglob("*"):
            if path.is_file() and not is_fallback_ignored_manifest_artifact(path):
                candidates.append(path.relative_to(ROOT).as_posix())
        return sorted(candidates)

    candidates = []
    for relative in result.stdout.split("\0"):
        if not relative:
            continue
        path = ROOT / relative
        if path.is_file():
            candidates.append(Path(relative).as_posix())
    return sorted(set(candidates))


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
        "docs/plans/operational-core",
        "docs/plans",
        "docs/roadmap.md",
        "docs/security",
        "docs/plans/operational-core/tickets",
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

    legacy_roots = [
        "archive",
        "collisionrelateddocs",
        "docs/planning",
        "docs/tickets",
        "docs/normalized",
        "docs/data",
        "docs/reference/generated-packs",
    ]
    still_legacy = [path for path in legacy_roots if (ROOT / path).exists()]
    require(not still_legacy, f"Legacy documentation roots still exist: {still_legacy}")

    doubled_path_prefixes = [
        "docs/reference/raw/" + "docs/reference/raw",
        "docs/reference/data/jam_exports/" + "docs/reference/raw",
    ]
    doubled_path_hits: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if set(path.relative_to(ROOT).parts) & {".git", ".obsidian", ".pytest_cache", "__pycache__"}:
            continue
        rel_path = path.relative_to(ROOT).as_posix()
        if rel_path.startswith("docs/reference/raw/collisionrelateddocs/"):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".pdf", ".doc", ".docx", ".msg", ".xlsm", ".xlsx", ".jam", ".zip"}:
            continue
        text = path.read_text(encoding="utf-8")
        if any(prefix in text for prefix in doubled_path_prefixes):
            doubled_path_hits.append(rel_path)
    require(not doubled_path_hits, f"Doubled migrated path prefixes found: {doubled_path_hits[:10]}")

    providers = load_provider_presets(ROOT / "docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json")
    require(len(providers) == 26, f"Expected 26 providers, got {len(providers)}")
    provider_names = {provider.name for provider in providers}
    require(provider_names == set(PROVIDER_PRESETS), f"Provider preset names changed: {sorted(provider_names)}")

    manifest_rows = list(csv.DictReader((ROOT / "docs/source_manifest.csv").open(encoding="utf-8")))
    require(any(row["path"].startswith("docs/reference/raw/collisionrelateddocs/Instructions/") for row in manifest_rows), "Instruction corpus missing from manifest")
    require(any(row["normalized_companion"] for row in manifest_rows if row["path"].startswith("docs/reference/raw/collisionrelateddocs/")), "No normalized companions recorded")

    matrix_rows = list(csv.DictReader((ROOT / "docs/reference/data/provider_coverage_matrix.csv").open(encoding="utf-8")))
    require(any(row["code"] == "ACSP" and row["parser_covered"] == "no" for row in matrix_rows), "ACSP uncovered status missing")
    require(any(row["code"] == "WOODLANDS" and row["parser_covered"] == "no" for row in matrix_rows), "WOODLANDS uncovered status missing")

    plan_text = (ROOT / "docs/plans/initial-repo-setup/archived_plans/implemented/2026-05-23-implemented-initrepoplan.md").read_text(encoding="utf-8")
    require("Status: implemented" in plan_text, "Archived initrepoplan missing implemented status")

    synthesis_text = read_doc("docs/plans/operational-core/source_synthesis.md")
    require_terms(synthesis_text, GENERATED_PACKS, "Source synthesis")
    require_terms(synthesis_text, RESEARCH_DOCS, "Source synthesis")

    expansion_plan = read_doc("docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md")
    require_terms(expansion_plan, PLANNED_WORKSPACE_TERMS, "Plans folder expansion plan")
    require_terms(
        expansion_plan,
        ["Deterministic automation", "AI agents", "MCP plans", "Agent skills"],
        "Plans folder expansion coverage",
    )
    require_terms(read_doc("docs/plans/_index.md"), PLANNED_WORKSPACE_TERMS, "Plans index planned workspaces")
    require_terms(read_doc("docs/plans/roadmap.md"), PLANNED_WORKSPACE_TERMS, "Plans roadmap workspaces")
    require_terms(read_doc("docs/plans/workspace_ownership_matrix.md"), PLANNED_WORKSPACE_TERMS, "Workspace ownership matrix")

    for workspace_path in PLANNED_WORKSPACE_TERMS:
        workspace_root = workspace_path.rstrip("/")
        for plan_file in ["README.md", "plan.md", "source_map.md", "roadmap.md"]:
            relative = f"{workspace_root}/{plan_file}"
            plan_text = read_doc(relative)
            require_terms(plan_text, PLAN_METADATA_TERMS, f"{relative} metadata")
            require("Source links:" in plan_text, f"{relative} missing source links")
            if plan_file == "plan.md":
                require_terms(
                    plan_text,
                    ["## Todo Areas", "## Dependency Cross-Check", "## Non-Overlap Rules", "## Source Ownership Rules"],
                    f"{relative} plan detail",
                )

    parser_plan = read_doc("docs/plans/parser-extraction/parser-mvp/plan.md")
    require_terms(parser_plan, PLAN_METADATA_TERMS, "Parser MVP plan metadata")
    require_terms(parser_plan, PROVIDER_PRESETS, "Parser MVP plan")
    require_terms(parser_plan, PARSER_PLAN_TERMS, "Parser MVP plan")

    for plan_file in [
        "docs/plans/operational-core/source_synthesis.md",
        "docs/plans/operational-core/tickets/backlog_index.md",
    ]:
        require_terms(read_doc(plan_file), PLAN_METADATA_TERMS, f"{plan_file} metadata")

    for ticket_file in [
        "docs/plans/operational-core/tickets/p0-foundation.md",
        "docs/plans/operational-core/tickets/p1-operational-core-mvp.md",
        "docs/plans/operational-core/tickets/p2-parser-hardening-provider-parity.md",
        "docs/plans/operational-core/tickets/p3-integrations-storage-eva-intake.md",
        "docs/plans/operational-core/tickets/p4-intelligence-engineer-communications.md",
        "docs/plans/operational-core/tickets/p5-platform-expansion.md",
    ]:
        ticket_text = read_doc(ticket_file)
        require_terms(
            ticket_text,
            PLAN_METADATA_TERMS,
            ticket_file,
        )

    require_scope_guardrails()

    core = ParserCore(ROOT / "docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json")
    require(len(core.providers) == 26, "ParserCore did not load providers")

    manifest_json_rows = json.loads((ROOT / "docs/source_manifest.json").read_text(encoding="utf-8"))
    require(len(manifest_json_rows) == len(manifest_rows), "Source manifest CSV/JSON row counts differ")
    manifest_paths = {row["path"] for row in manifest_rows}
    json_paths = {row["path"] for row in manifest_json_rows}
    require(json_paths == manifest_paths, "Source manifest CSV/JSON path sets differ")
    require(all(path in manifest_paths for path in REQUIRED_PATHS), "Source manifest missing required active docs")
    stale_manifest_paths = [path for path in manifest_paths if not (ROOT / path).exists()]
    require(not stale_manifest_paths, f"Source manifest includes missing files: {stale_manifest_paths[:10]}")
    missing_from_manifest: list[str] = []
    for relative in manifest_candidate_paths():
        if relative not in manifest_paths:
            missing_from_manifest.append(relative)
    require(not missing_from_manifest, f"Files missing from source manifest: {missing_from_manifest[:10]}")
    print("Scaffold verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
