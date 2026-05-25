from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .core import DEFAULT_PROVIDER_CONFIG, ParserCore
from .exporters.eva import export_eva_payload
from .packaging import build_evidence_package_manifest
from .providers import load_provider_presets, providers_to_dicts


def _write_json(payload: Any, output: Path | None = None) -> None:
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ccc-parser")
    parser.add_argument("--provider-config", type=Path, default=DEFAULT_PROVIDER_CONFIG)
    sub = parser.add_subparsers(dest="command", required=True)

    triage_cmd = sub.add_parser("triage", help="Triage one source file or folder")
    triage_cmd.add_argument("source", type=Path)

    parse_cmd = sub.add_parser("parse", help="Parse one source file with the shared parser core")
    parse_cmd.add_argument("source", type=Path)
    parse_cmd.add_argument("--provider")
    parse_cmd.add_argument("--output", type=Path)

    validate_cmd = sub.add_parser("validate", help="Validate a parser result JSON file")
    validate_cmd.add_argument("result", type=Path)

    export_cmd = sub.add_parser("export-eva", help="Export EVA JSON from a parser result")
    export_cmd.add_argument("result", type=Path)
    export_cmd.add_argument("--allow-blockers", action="store_true")
    export_cmd.add_argument("--output", type=Path)

    package_cmd = sub.add_parser("package", help="Emit evidence package manifest inputs for a parser result")
    package_cmd.add_argument("result", type=Path)
    package_cmd.add_argument("--preview-full-vehicle-image-id")
    package_cmd.add_argument("--preview-damage-image-id")
    package_cmd.add_argument("--output", type=Path)

    batch_cmd = sub.add_parser("batch", help="Parse all instruction candidates in a folder")
    batch_cmd.add_argument("folder", type=Path)
    batch_cmd.add_argument("--output", type=Path)

    providers_cmd = sub.add_parser("providers", help="Provider preset utilities")
    providers_sub = providers_cmd.add_subparsers(dest="providers_command")
    providers_sub.add_parser("list", help="List provider presets")
    validate_providers = providers_sub.add_parser("validate", help="Validate provider config can load")
    validate_providers.add_argument("config", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    core = ParserCore(args.provider_config)

    if args.command == "triage":
        _write_json(core.triage(args.source).to_dict())
        return 0

    if args.command == "parse":
        try:
            result = core.parse(args.source, provider=args.provider)
        except ValueError as exc:
            _write_json({"error": str(exc)}, args.output)
            return 1
        _write_json(result.to_dict(), args.output)
        return 0 if not any(warning.severity == "blocker" for warning in result.warnings) else 1

    if args.command == "validate":
        result = ParserCore.result_from_json(args.result)
        _write_json(result.validation.to_dict())
        return 0 if result.validation.can_export else 1

    if args.command == "export-eva":
        result = ParserCore.result_from_json(args.result)
        try:
            payload = export_eva_payload(result, allow_blockers=args.allow_blockers)
        except ValueError as exc:
            _write_json({"error": str(exc)})
            return 1
        _write_json(payload, args.output)
        return 0

    if args.command == "package":
        result = ParserCore.result_from_json(args.result)
        manifest = build_evidence_package_manifest(
            result,
            preview_full_vehicle_image_id=args.preview_full_vehicle_image_id,
            preview_damage_image_id=args.preview_damage_image_id,
        )
        _write_json(manifest, args.output)
        return 0

    if args.command == "batch":
        report = core.parse_batch_report(args.folder)
        _write_json(
            {
                "results": [result.to_dict() for result in report["results"]],
                "errors": report["errors"],
            },
            args.output,
        )
        return 1 if report["errors"] else 0

    if args.command == "providers":
        provider_command = args.providers_command or "list"
        if provider_command == "list":
            _write_json({"providers": providers_to_dicts(core.providers)})
            return 0
        if provider_command == "validate":
            presets = load_provider_presets(args.config)
            _write_json({"provider_count": len(presets), "providers": [preset.name for preset in presets]})
            return 0 if presets else 1

    raise AssertionError(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
