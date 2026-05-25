from __future__ import annotations

import json
from pathlib import Path

from ccc_parser.cli import main


ROOT = Path(__file__).resolve().parents[1]
PROVIDERS = ROOT / "docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json"
INSTRUCTIONS = ROOT / "docs/reference/raw/collisionrelateddocs/Instructions"


def test_cli_parse_validate_and_export_eva_share_core_services(tmp_path, capsys):
    result_path = tmp_path / "sbl-result.json"
    eva_path = tmp_path / "sbl-eva.json"

    assert main(["--provider-config", str(PROVIDERS), "parse", str(INSTRUCTIONS / "SBL 01.pdf"), "--output", str(result_path)]) == 0
    parsed = json.loads(result_path.read_text(encoding="utf-8"))
    assert parsed["detected_provider"] == "SBL"
    assert parsed["fields"]["vrm"]["normalized_value"] == "SK24KYF"

    assert main(["validate", str(result_path)]) == 1
    validation = json.loads(capsys.readouterr().out)
    assert any(issue["code"] == "missing_mileage" for issue in validation["blockers"])

    assert main(["export-eva", str(result_path), "--allow-blockers", "--output", str(eva_path)]) == 0
    exported = json.loads(eva_path.read_text(encoding="utf-8"))
    assert exported["Work Provider"] == "SBL"
    assert exported["VRM"] == "SK24KYF"


def test_cli_triage_and_providers_subcommands_emit_json(capsys):
    assert main(["triage", str(INSTRUCTIONS / "SBL 01.pdf")]) == 0
    triage = json.loads(capsys.readouterr().out)
    assert triage["items"][0]["role_guess"] == "instruction"
    assert triage["items"][0]["sha256"]

    assert main(["--provider-config", str(PROVIDERS), "providers", "list"]) == 0
    providers = json.loads(capsys.readouterr().out)
    assert len(providers["providers"]) == 26
    assert any(provider["name"] == "SBL" for provider in providers["providers"])


def test_cli_parse_rejects_ambiguous_provider_code(capsys):
    status = main(
        [
            "--provider-config",
            str(PROVIDERS),
            "parse",
            str(INSTRUCTIONS / "FW 02.msg"),
            "--provider",
            "FW",
        ]
    )
    payload = json.loads(capsys.readouterr().out)

    assert status == 1
    assert "matches multiple provider presets" in payload["error"]


def test_cli_package_manifest_applies_preview_then_all_images_order(tmp_path):
    result_path = tmp_path / "images-result.json"
    package_path = tmp_path / "package.json"

    assert main(["--provider-config", str(PROVIDERS), "parse", str(INSTRUCTIONS / "__Images 02.pdf"), "--output", str(result_path)]) == 0
    parsed = json.loads(result_path.read_text(encoding="utf-8"))
    first_two = [image["image_id"] for image in parsed["images"][:2]]
    assert len(first_two) == 2

    assert main(["package", str(result_path), "--output", str(package_path)]) == 0
    package = json.loads(package_path.read_text(encoding="utf-8"))

    assert package["ordered_image_ids"][:2] == first_two
    assert package["ordered_image_ids"][2:4] == first_two
    assert len(package["ordered_images"]) == len(parsed["images"]) + 2
