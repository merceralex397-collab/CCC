from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProviderPreset:
    name: str
    code: str
    detect_phrases: tuple[str, ...]
    engineer_report: bool
    field_rules: dict


def normalize_code(value: object) -> str:
    return "" if value is None else str(value).strip().upper()


def load_provider_presets(path: Path) -> list[ProviderPreset]:
    data = json.loads(path.read_text(encoding="utf-8"))
    presets: list[ProviderPreset] = []
    for item in data.get("providers", []):
        work_provider = item.get("field_rules", {}).get("work_provider", {})
        presets.append(
            ProviderPreset(
                name=item.get("name", ""),
                code=normalize_code(work_provider.get("config")),
                detect_phrases=tuple(item.get("detect_phrases", [])),
                engineer_report=bool(item.get("engineer_report", False)),
                field_rules=item.get("field_rules", {}),
            )
        )
    return presets


def detect_provider(text: str, presets: list[ProviderPreset]) -> ProviderPreset | None:
    lowered = text.lower()
    for preset in presets:
        if any(phrase.lower() in lowered for phrase in preset.detect_phrases):
            return preset
    return None
