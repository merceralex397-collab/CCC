from pathlib import Path

from ccc_parser.core import ParserCore
from ccc_parser.exporters import EVA_FIELD_ORDER
from ccc_parser.providers import load_provider_presets
from ccc_parser.ui.app import ParserUiController


ROOT = Path(__file__).resolve().parents[1]


def test_provider_config_loads_current_presets():
    presets = load_provider_presets(ROOT / "collisionrelateddocs/Settings Backup/providers.json")
    assert len(presets) == 26
    names = {preset.name for preset in presets}
    assert "ALISON" in names
    assert "TEN" in names


def test_ui_controller_and_cli_share_parser_core():
    core = ParserCore(ROOT / "collisionrelateddocs/Settings Backup/providers.json")
    controller = ParserUiController(core)
    assert controller.core is core


def test_eva_export_field_order_contains_required_core_fields():
    assert EVA_FIELD_ORDER[:4] == ["work_provider", "vrm", "vehicle_model", "claimant_name"]
    assert "inspection_address" in EVA_FIELD_ORDER
    assert "mileage" in EVA_FIELD_ORDER
