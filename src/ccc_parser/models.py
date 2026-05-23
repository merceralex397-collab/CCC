from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ParserWarning:
    code: str
    message: str
    severity: str = "warning"


@dataclass(frozen=True)
class ExtractedField:
    name: str
    value: str | None
    confidence: float = 0.0
    source: str | None = None


@dataclass(frozen=True)
class ParserResult:
    source_path: Path
    source_sha256: str
    provider_name: str | None
    fields: dict[str, ExtractedField] = field(default_factory=dict)
    warnings: list[ParserWarning] = field(default_factory=list)
    audit: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_path": str(self.source_path),
            "source_sha256": self.source_sha256,
            "provider_name": self.provider_name,
            "fields": {
                key: {
                    "name": value.name,
                    "value": value.value,
                    "confidence": value.confidence,
                    "source": value.source,
                }
                for key, value in self.fields.items()
            },
            "warnings": [
                {"code": item.code, "message": item.message, "severity": item.severity}
                for item in self.warnings
            ],
            "audit": self.audit,
        }
