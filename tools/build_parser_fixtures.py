from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ccc_parser.core import DEFAULT_PROVIDER_CONFIG, ParserCore  # noqa: E402
from ccc_parser.providers import load_provider_presets, providers_to_dicts, provider_config_version  # noqa: E402


CORPUS = ROOT / "docs/reference/raw/collisionrelateddocs/Instructions"
DATA_DIR = ROOT / "docs/reference/data"
NORMALIZED_DIR = ROOT / "docs/reference/normalized"


def _relative(path: Path) -> str:
    path = path if path.is_absolute() else ROOT / path
    return str(path.relative_to(ROOT)).replace("\\", "/")


def _normalized_companion_for(path: Path) -> Path | None:
    source_name = path.name.lower()
    for companion in NORMALIZED_DIR.glob("collisionrelateddocs__instructions__*.md"):
        if source_name in companion.name.lower().replace("-", " "):
            return companion
    return None


def _snapshot_status(result) -> str:
    if result.validation.can_export:
        return "full-eva-export"
    if any(issue.code == "not_instruction_export_candidate" for issue in result.validation.blockers):
        return "not-eva-export-candidate"
    if any(issue.code in {"provider_not_detected", "missing_work_provider", "missing_vrm"} for issue in result.validation.blockers):
        return "review-required"
    return "partial-review-required"


def build_provider_fixture() -> dict[str, Any]:
    provider_config = ROOT / DEFAULT_PROVIDER_CONFIG
    presets = load_provider_presets(provider_config)
    return {
        "version": 1,
        "source": _relative(provider_config),
        "source_version": provider_config_version(provider_config),
        "provider_count": len(presets),
        "providers": providers_to_dicts(presets),
    }


def build_corpus_ledger() -> list[dict[str, Any]]:
    core = ParserCore(ROOT / DEFAULT_PROVIDER_CONFIG)
    rows: list[dict[str, Any]] = []
    for path in sorted(item for item in CORPUS.rglob("*") if item.is_file()):
        result = core.parse(path)
        companion = _normalized_companion_for(path)
        rows.append(
            {
                "raw_path": _relative(path),
                "sha256": result.source_sha256,
                "normalized_companion": _relative(companion) if companion else "",
                "document_type": result.document_classification,
                "reader_method": result.audit_metadata.get("reader_method", ""),
                "detected_provider": result.detected_provider or "",
                "expected_provider_status": "matched" if result.detected_provider else "review-required",
                "expected_fields": {
                    name: field.normalized_value
                    for name, field in result.fields.items()
                    if (field.normalized_value or "").strip()
                },
                "review_blockers": [issue.code for issue in result.validation.blockers],
                "export_snapshot_status": _snapshot_status(result),
            }
        )
    return rows


def write_outputs() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    provider_fixture = build_provider_fixture()
    provider_path = DATA_DIR / "parser_provider_presets_v1.json"
    provider_path.write_text(json.dumps(provider_fixture, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    ledger = build_corpus_ledger()
    ledger_json = DATA_DIR / "parser_corpus_fixture_ledger.json"
    ledger_csv = DATA_DIR / "parser_corpus_fixture_ledger.csv"
    ledger_json.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    with ledger_csv.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = [
            "raw_path",
            "sha256",
            "normalized_companion",
            "document_type",
            "reader_method",
            "detected_provider",
            "expected_provider_status",
            "expected_fields",
            "review_blockers",
            "export_snapshot_status",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in ledger:
            writer.writerow(
                {
                    **row,
                    "expected_fields": json.dumps(row["expected_fields"], ensure_ascii=False, sort_keys=True),
                    "review_blockers": ";".join(row["review_blockers"]),
                }
            )


def main() -> int:
    write_outputs()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
