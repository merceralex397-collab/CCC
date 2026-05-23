from __future__ import annotations

import argparse
import json
from pathlib import Path

from .core import DEFAULT_PROVIDER_CONFIG, ParserCore
from .providers import load_provider_presets


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ccc-parser")
    parser.add_argument("--provider-config", type=Path, default=DEFAULT_PROVIDER_CONFIG)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("providers", help="List configured provider presets")

    parse_cmd = sub.add_parser("parse", help="Parse one source file with scaffold extraction")
    parse_cmd.add_argument("source", type=Path)
    parse_cmd.add_argument("--output", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "providers":
        presets = load_provider_presets(args.provider_config)
        for preset in presets:
            print(f"{preset.name}\t{preset.code}")
        return 0
    if args.command == "parse":
        core = ParserCore(args.provider_config)
        result = core.parse(args.source).to_dict()
        payload = json.dumps(result, indent=2)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(payload + "\n", encoding="utf-8")
        else:
            print(payload)
        return 0
    raise AssertionError(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
