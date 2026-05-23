from __future__ import annotations

import hashlib
from pathlib import Path

from .models import ParserResult, ParserWarning
from .providers import detect_provider, load_provider_presets


DEFAULT_PROVIDER_CONFIG = Path("docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class ParserCore:
    def __init__(self, provider_config: Path | None = None) -> None:
        self.provider_config = provider_config or DEFAULT_PROVIDER_CONFIG
        self.providers = load_provider_presets(self.provider_config)

    def parse(self, source_path: Path) -> ParserResult:
        source_path = Path(source_path)
        text = self._best_effort_text(source_path)
        provider = detect_provider(text, self.providers)
        warnings: list[ParserWarning] = []
        if provider is None:
            warnings.append(
                ParserWarning(
                    code="provider_not_detected",
                    message="No provider preset matched the available source text.",
                )
            )
        warnings.append(
            ParserWarning(
                code="scaffold_only",
                message="Field extraction is scaffolded; provider golden rules are not implemented yet.",
                severity="info",
            )
        )
        return ParserResult(
            source_path=source_path,
            source_sha256=file_sha256(source_path),
            provider_name=provider.name if provider else None,
            warnings=warnings,
            audit={
                "provider_config": str(self.provider_config),
                "provider_count": len(self.providers),
                "text_preview_length": len(text),
            },
        )

    def _best_effort_text(self, source_path: Path) -> str:
        if source_path.suffix.lower() in {".txt", ".md", ".json"}:
            return source_path.read_text(encoding="utf-8", errors="replace")
        return ""
