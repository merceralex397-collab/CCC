from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ccc_parser.core import DEFAULT_PROVIDER_CONFIG, ParserCore  # noqa: E402


DEFAULT_CORPUS = ROOT / "docs/reference/raw/collisionrelateddocs/Instructions"


def _relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def build_report(corpus: Path, provider_config: Path = DEFAULT_PROVIDER_CONFIG) -> dict[str, Any]:
    corpus = corpus if corpus.is_absolute() else ROOT / corpus
    provider_config = provider_config if provider_config.is_absolute() else ROOT / provider_config
    core = ParserCore(provider_config)
    files = sorted(path for path in corpus.rglob("*") if path.is_file())
    provider_counts: Counter[str] = Counter()
    reader_counts: Counter[str] = Counter()
    blocker_counts: Counter[str] = Counter()
    warning_counts: Counter[str] = Counter()
    rows: list[dict[str, Any]] = []
    reader_blockers: list[dict[str, Any]] = []

    for path in files:
        result = core.parse(path)
        provider = result.detected_provider or "UNKNOWN"
        reader = str(result.audit_metadata.get("reader_method", "unknown"))
        provider_counts[provider] += 1
        reader_counts[reader] += 1
        for issue in result.validation.blockers:
            blocker_counts[issue.code] += 1
        for warning in result.warnings:
            warning_counts[warning.code] += 1
            if warning.severity == "blocker":
                reader_blockers.append(
                    {
                        "path": _relative(path),
                        "code": warning.code,
                        "message": warning.message,
                    }
                )
        rows.append(
            {
                "path": _relative(path),
                "sha256": result.source_sha256,
                "document_classification": result.document_classification,
                "reader_method": reader,
                "detected_provider": provider,
                "blockers": [issue.code for issue in result.validation.blockers],
                "warnings": [warning.code for warning in result.warnings],
                "nonempty_fields": sorted(
                    name for name, field in result.fields.items() if (field.normalized_value or "").strip()
                ),
            }
        )

    return {
        "corpus": _relative(corpus),
        "file_count": len(files),
        "reader_blocker_count": len(reader_blockers),
        "reader_blockers": reader_blockers,
        "provider_counts": dict(sorted(provider_counts.items())),
        "reader_counts": dict(sorted(reader_counts.items())),
        "blocker_counts": dict(sorted(blocker_counts.items())),
        "warning_counts": dict(sorted(warning_counts.items())),
        "files": rows,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--provider-config", type=Path, default=DEFAULT_PROVIDER_CONFIG)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    report = build_report(args.corpus, args.provider_config)
    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0 if report["reader_blocker_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
