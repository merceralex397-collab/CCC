from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .normalization import normalize_search_text


@dataclass(frozen=True)
class ProviderPreset:
    name: str
    code: str
    detect_phrases: tuple[str, ...]
    engineer_report: bool
    field_rules: dict[str, dict[str, Any]]
    use_current_date_for_inspection_date: bool = False
    force_postcode_for_inspection_address: bool = False


@dataclass(frozen=True)
class ProviderMatch:
    provider: ProviderPreset | None
    score: int
    matched_phrases: tuple[str, ...] = ()
    missing_phrases: tuple[str, ...] = ()

    @property
    def name(self) -> str:
        return self.provider.name if self.provider else "Unknown / Unmapped"

    @property
    def confidence(self) -> float:
        if not self.provider or not self.provider.detect_phrases:
            return 0.0
        return min(1.0, self.score / max(self.score, 100))


def normalize_code(value: object) -> str:
    return "" if value is None else str(value).strip().upper()


def derive_provider_code(name: str, configured_code: object = "") -> str:
    code = normalize_code(configured_code)
    if code:
        return code
    prefix = str(name or "").split("(", 1)[0].strip()
    return "".join(char for char in prefix.upper() if char.isalnum())


def _normalize_rule(rule: object) -> dict[str, Any]:
    payload = dict(rule or {}) if isinstance(rule, dict) else {}
    payload.setdefault("method", "single_label")
    payload.setdefault("config", "")
    return payload


def load_provider_presets(path: Path) -> list[ProviderPreset]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    presets: list[ProviderPreset] = []
    for item in data.get("providers", []):
        field_rules = {
            str(field_name): _normalize_rule(rule)
            for field_name, rule in (item.get("field_rules") or {}).items()
        }
        work_provider = field_rules.get("work_provider", {})
        presets.append(
            ProviderPreset(
                name=str(item.get("name", "")),
                code=derive_provider_code(str(item.get("name", "")), work_provider.get("config")),
                detect_phrases=tuple(str(phrase) for phrase in item.get("detect_phrases", []) if str(phrase).strip()),
                engineer_report=bool(item.get("engineer_report", False)),
                field_rules=field_rules,
                use_current_date_for_inspection_date=bool(item.get("use_current_date_for_inspection_date", False)),
                force_postcode_for_inspection_address=bool(item.get("force_postcode_for_inspection_address", False)),
            )
        )
    return presets


def provider_config_version(path: Path) -> str:
    digest = hashlib.sha256(Path(path).read_bytes()).hexdigest()
    return f"sha256:{digest}"


def detect_provider_match(text: str, presets: list[ProviderPreset], forced_provider: str | None = None) -> ProviderMatch:
    if forced_provider:
        forced = forced_provider.strip().lower()
        for preset in presets:
            if preset.name.lower() == forced:
                return ProviderMatch(provider=preset, score=999, matched_phrases=preset.detect_phrases)
        code_matches = [preset for preset in presets if preset.code.lower() == forced]
        if len(code_matches) == 1:
            preset = code_matches[0]
            return ProviderMatch(provider=preset, score=999, matched_phrases=preset.detect_phrases)
        if len(code_matches) > 1:
            names = ", ".join(preset.name for preset in code_matches)
            raise ValueError(
                f"Provider override '{forced_provider}' matches multiple provider presets: {names}. Use the full provider name."
            )
        raise ValueError(f"Provider override '{forced_provider}' does not match any provider preset.")

    lower_text = (text or "").lower()
    normalized_text = normalize_search_text(text)
    best = ProviderMatch(provider=None, score=0)
    best_match_count = 0
    best_longest = 0

    for preset in presets:
        if not preset.detect_phrases:
            continue
        score = 0
        matched: list[str] = []
        missing: list[str] = []
        longest = 0
        for phrase in preset.detect_phrases:
            raw_phrase = phrase.lower().strip()
            normalized_phrase = normalize_search_text(phrase)
            if (raw_phrase and raw_phrase in lower_text) or (
                normalized_phrase and normalized_phrase in normalized_text
            ):
                matched.append(phrase)
                longest = max(longest, len(normalized_phrase or raw_phrase))
                score += max(10, len(normalized_phrase or raw_phrase))
            else:
                missing.append(phrase)
                break
        if missing:
            continue
        if (
            score > best.score
            or (score == best.score and len(matched) > best_match_count)
            or (score == best.score and len(matched) == best_match_count and longest > best_longest)
        ):
            best = ProviderMatch(provider=preset, score=score, matched_phrases=tuple(matched))
            best_match_count = len(matched)
            best_longest = longest
    return best


def detect_provider(text: str, presets: list[ProviderPreset]) -> ProviderPreset | None:
    return detect_provider_match(text, presets).provider


def providers_to_dicts(presets: list[ProviderPreset]) -> list[dict[str, Any]]:
    return [
        {
            "name": preset.name,
            "code": preset.code,
            "detect_phrases": list(preset.detect_phrases),
            "engineer_report": preset.engineer_report,
            "use_current_date_for_inspection_date": preset.use_current_date_for_inspection_date,
            "force_postcode_for_inspection_address": preset.force_postcode_for_inspection_address,
            "field_rules": preset.field_rules,
        }
        for preset in presets
    ]
