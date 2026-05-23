from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ccc_parser.core import ParserCore
from ccc_parser.exporters import EVA_FIELD_ORDER
from ccc_parser.providers import load_provider_presets
from ccc_parser.ui.app import ParserUiController
import tools.scaffold_initial_repo as scaffold

def test_provider_config_loads_current_presets():
    presets = load_provider_presets(ROOT / "docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json")
    assert len(presets) == 26
    names = {preset.name for preset in presets}
    assert "ALISON" in names
    assert "TEN" in names


def test_parser_core_default_provider_config_loads_current_presets(monkeypatch):
    monkeypatch.chdir(ROOT)
    core = ParserCore()
    assert len(core.providers) == 26


def test_ui_controller_and_cli_share_parser_core():
    core = ParserCore(ROOT / "docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json")
    controller = ParserUiController(core)
    assert controller.core is core


def test_eva_export_field_order_contains_required_core_fields():
    assert EVA_FIELD_ORDER[:4] == ["work_provider", "vrm", "vehicle_model", "claimant_name"]
    assert "inspection_address" in EVA_FIELD_ORDER
    assert "mileage" in EVA_FIELD_ORDER


def test_scaffold_manifest_ignores_local_artifacts(monkeypatch, tmp_path):
    monkeypatch.setattr(scaffold, "ROOT", tmp_path)
    (tmp_path / "README.md").write_text("# Test\n", encoding="utf-8")
    (tmp_path / ".env").write_text("SECRET=value\n", encoding="utf-8")
    (tmp_path / ".env.example").write_text("SECRET=\n", encoding="utf-8")
    (tmp_path / ".venv").mkdir()
    (tmp_path / ".venv" / "artifact.py").write_text("ignored\n", encoding="utf-8")
    (tmp_path / "tmp").mkdir()
    (tmp_path / "tmp" / "scratch.txt").write_text("ignored\n", encoding="utf-8")
    (tmp_path / "debug.log").write_text("ignored\n", encoding="utf-8")

    paths = {record["path"] for record in scaffold.build_manifest()}

    assert "README.md" in paths
    assert ".env.example" in paths
    assert ".env" not in paths
    assert ".venv/artifact.py" not in paths
    assert "tmp/scratch.txt" not in paths
    assert "debug.log" not in paths


def test_scaffold_archive_migration_removes_empty_legacy_root(monkeypatch, tmp_path):
    monkeypatch.setattr(scaffold, "ROOT", tmp_path)
    legacy_plan = tmp_path / "archive" / "plans" / "implemented" / "done.md"
    legacy_plan.parent.mkdir(parents=True)
    legacy_plan.write_text("# Done\n", encoding="utf-8")

    scaffold.organize_reference_packs()

    migrated = tmp_path / "docs" / "plans" / "operational-core" / "archived_plans" / "implemented" / "done.md"
    assert migrated.exists()
    assert not (tmp_path / "archive").exists()
