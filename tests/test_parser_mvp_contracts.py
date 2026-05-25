from __future__ import annotations

import json
from email.message import EmailMessage
from pathlib import Path

import pytest

from ccc_parser.core import ParserCore
from ccc_parser.exporters.eva import export_eva_payload
from ccc_parser.normalization import (
    normalize_date,
    normalize_inspection_address,
    normalize_mileage,
    normalize_vrm,
)
from ccc_parser.providers import detect_provider, load_provider_presets
from ccc_parser.ui.app import parse_drop_paths


ROOT = Path(__file__).resolve().parents[1]
PROVIDERS = ROOT / "docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json"
INSTRUCTIONS = ROOT / "docs/reference/raw/collisionrelateddocs/Instructions"
FINAL_FORMAT = ROOT / "docs/reference/raw/collisionrelateddocs/Final Format Example 02.json"
PROVIDER_FIXTURE = ROOT / "docs/reference/data/parser_provider_presets_v1.json"
CORPUS_LEDGER = ROOT / "docs/reference/data/parser_corpus_fixture_ledger.json"
CORPUS_REPORT = ROOT / "docs/reference/data/parser_corpus_regression_report.json"
PARSERTESTS = ROOT / "tests/parsertests"


def field_value(result, name: str) -> str:
    return result.fields[name].normalized_value or ""


def test_normalization_contracts():
    assert normalize_vrm(" yh14 amk ") == "YH14AMK"
    assert normalize_mileage("Speedo reads 53,600 Km") == "53600"
    assert normalize_date("18 September 2025") == "18/09/2025"
    assert normalize_date("2026-05-06 13:45:00+01:00") == "06/05/2026"

    six_line = normalize_inspection_address("109 Valley View, Hoole, CH49 0DJ")
    assert six_line.split("\n") == ["109 Valley View", "Hoole", "", "", "", "CH49 0DJ"]
    assert normalize_inspection_address("Image-based Assessment").split("\n") == [
        "Image-based Assessment",
        "",
        "",
        "",
        "",
        "",
    ]


def test_provider_detection_requires_all_phrases_and_prefers_specific_provider():
    presets = load_provider_presets(PROVIDERS)
    solicitor = detect_provider("Please see fairwaylegal instruction attached", presets)
    garage = detect_provider(
        "Please see fairwaylegal instruction attached\nInspection Location: Test Garage",
        presets,
    )

    assert solicitor is not None
    assert solicitor.name == "FW (Solicitor)"
    assert garage is not None
    assert garage.name == "FW (Garage)"


def test_parse_docx_fixture_extracts_alison_fields_and_review_blockers():
    result = ParserCore(PROVIDERS).parse(INSTRUCTIONS / "ALISON WORD 01.docx")

    assert result.detected_provider == "ALISON"
    assert result.document_classification == "instruction"
    assert field_value(result, "work_provider") == "ALISON"
    assert field_value(result, "vrm") == "YH14AMK"
    assert field_value(result, "claimant_name") == "Uzair Khan"
    assert field_value(result, "reference") == ""
    assert field_value(result, "incident_date") == "12/09/2025"
    assert "22 Blenheim Rd" in field_value(result, "inspection_address")
    assert result.inspection_mode == "physical"
    assert any(issue.code == "missing_mileage" for issue in result.validation.blockers)
    assert any(issue.code == "missing_vat_status" for issue in result.validation.blockers)


def test_parse_pdf_fixture_extracts_sbl_fields_and_image_based_inspection():
    result = ParserCore(PROVIDERS).parse(INSTRUCTIONS / "SBL 01.pdf")

    assert result.detected_provider == "SBL"
    assert field_value(result, "work_provider") == "SBL"
    assert field_value(result, "vrm") == "SK24KYF"
    assert field_value(result, "vehicle_model") == "FORD SWIFT VOYAGER 494 AUTO"
    assert field_value(result, "claimant_name") == "Mr Craig Motorhome Escapes"
    assert field_value(result, "reference") == "SBL-B0470099"
    assert field_value(result, "incident_date") == "06/04/2026"
    assert field_value(result, "inspection_address").splitlines()[0] == "Image-based Assessment"
    assert result.inspection_mode == "image_based"
    assert any(field.provenance for field in result.fields.values() if field.normalized_value)


def test_parse_cnx_engineer_report_uses_deterministic_fallbacks_for_visible_fields():
    result = ParserCore(PROVIDERS).parse(INSTRUCTIONS / "CNX 01.pdf")

    assert result.detected_provider == "CNX (Engineers)"
    assert field_value(result, "work_provider") == "CNX"
    assert field_value(result, "vrm") == "MW23VWD"
    assert field_value(result, "vehicle_model") == "FORD PUMA ST-LINE VIGNALE MHEV"
    assert field_value(result, "claimant_name") == "Mr A Schunke"
    assert field_value(result, "reference") == "00077114/PK"
    assert field_value(result, "incident_date") == "13/02/2026"
    assert field_value(result, "inspection_address").splitlines()[0] == "Image-based Assessment"
    assert "rear bumper" in field_value(result, "accident_circumstances").lower()
    assert field_value(result, "mileage") == "70552"
    assert field_value(result, "mileage_unit") == "Miles"


def test_parsertests_output1_matches_cnx_eva_export_regression_fixture():
    result = ParserCore(PROVIDERS).parse(INSTRUCTIONS / "CNX 01.pdf")
    payload = export_eva_payload(result, allow_blockers=True)
    expected = json.loads((PARSERTESTS / "output1.json").read_text(encoding="utf-8"))

    assert dict(payload) == expected


def test_eva_export_hard_blocks_non_instruction_sources_even_with_allow_blockers():
    result = ParserCore(PROVIDERS).parse(INSTRUCTIONS / "__Images 02.pdf")

    assert result.document_classification == "image_pack"
    assert any(issue.code == "not_instruction_export_candidate" for issue in result.validation.blockers)
    with pytest.raises(ValueError, match="not an instruction export candidate"):
        export_eva_payload(result, allow_blockers=True)


def test_email_attachment_instruction_is_routed_through_parser_core(tmp_path):
    message = EmailMessage()
    message["Subject"] = "Images attached"
    message["From"] = "sender@example.test"
    message["To"] = "engineers@example.test"
    message.set_content("Please see attached instruction.")
    message.add_attachment(
        "\n".join(
            [
                "Smart Business Link",
                "Date",
                "01/05/2026",
                "From",
                "Registration: SK24 KYF",
                "Vehicle Make: FORD SWIFT VOYAGER 494 AUTO",
                "Policyholder Name: Mr Craig Motorhome Escapes",
                "Claim Number: SBL-B0470099",
                "Incident Date: 06/04/2026",
                "Incident Circumstances",
                "Rear impact damage.",
                "Agreed Value",
                "Policyholder VAT Status: VAT Registered",
            ]
        ),
        subtype="plain",
        filename="attached-instruction.txt",
    )
    eml_path = tmp_path / "instruction-email.eml"
    eml_path.write_bytes(message.as_bytes())

    result = ParserCore(PROVIDERS).parse(eml_path)

    assert result.detected_provider == "SBL"
    assert field_value(result, "work_provider") == "SBL"
    assert field_value(result, "vrm") == "SK24KYF"
    assert field_value(result, "reference") == "SBL-B0470099"
    assert any(source.path.name == "attached-instruction.txt" for source in result.source_files)


def test_forced_provider_code_must_be_unambiguous():
    with pytest.raises(ValueError, match="matches multiple provider presets"):
        ParserCore(PROVIDERS).parse(INSTRUCTIONS / "FW 02.msg", provider="FW")


def test_noisy_doc_fixed_position_values_fall_back_to_visible_fields():
    als = ParserCore(PROVIDERS).parse(INSTRUCTIONS / "ALS 01.DOC")
    bc = ParserCore(PROVIDERS).parse(INSTRUCTIONS / "BC 01.DOC")

    assert field_value(als, "instruction_date") == "07/05/2026"
    assert field_value(als, "vehicle_model") == "Grandland X Sport Nav T D Ss A 1.6"
    assert field_value(bc, "reference") == "RTA135646.001/NE/Usayd Ibrahim"
    assert field_value(bc, "instruction_date") == "06/05/2026"
    assert not any(issue.code.startswith("invalid_") for issue in als.validation.blockers)
    assert not any(issue.code.startswith("invalid_") for issue in bc.validation.blockers)


def test_hyphenated_month_dates_normalize_to_eva_date_format():
    result = ParserCore(PROVIDERS).parse(INSTRUCTIONS / "QCL 01.docx")

    assert field_value(result, "incident_date") == "04/05/2026"
    assert not any(issue.code == "invalid_incident_date" for issue in result.validation.blockers)


def test_ui_drop_path_parser_handles_tk_braced_file_lists():
    raw = r"{C:\Instructions\CNX 01.pdf} {C:\Instructions\photo one.jpg}"

    assert parse_drop_paths(raw) == [
        Path(r"C:\Instructions\CNX 01.pdf"),
        Path(r"C:\Instructions\photo one.jpg"),
    ]


def test_eva_export_uses_final_format_key_order_and_blocks_unreviewed_result():
    result = ParserCore(PROVIDERS).parse(INSTRUCTIONS / "SBL 01.pdf")
    payload = export_eva_payload(result, allow_blockers=True)
    expected_keys = list(json.loads(FINAL_FORMAT.read_text(encoding="utf-8")).keys())

    assert list(payload.keys()) == expected_keys
    assert payload["Work Provider"] == "SBL"
    assert payload["VRM"] == "SK24KYF"
    assert payload["Inspection Address"].splitlines()[0] == "Image-based Assessment"


def test_generated_provider_and_corpus_fixtures_cover_current_private_corpus():
    provider_fixture = json.loads(PROVIDER_FIXTURE.read_text(encoding="utf-8"))
    ledger = json.loads(CORPUS_LEDGER.read_text(encoding="utf-8"))
    report = json.loads(CORPUS_REPORT.read_text(encoding="utf-8"))

    assert provider_fixture["provider_count"] == 26
    assert {provider["name"] for provider in provider_fixture["providers"]} >= {"ALISON", "SBL", "TEN"}
    assert len(ledger) == len(list(INSTRUCTIONS.glob("*")))
    assert report["file_count"] == len(ledger)
    assert report["reader_blocker_count"] == 0
