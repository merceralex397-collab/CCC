from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


PARSER_VERSION = "0.2.0"


@dataclass(frozen=True)
class ParserWarning:
    code: str
    message: str
    severity: str = "warning"
    source_file_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "code": self.code,
            "message": self.message,
            "severity": self.severity,
        }
        if self.source_file_id:
            payload["source_file_id"] = self.source_file_id
        return payload

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ParserWarning":
        return cls(
            code=str(payload.get("code", "")),
            message=str(payload.get("message", "")),
            severity=str(payload.get("severity", "warning")),
            source_file_id=payload.get("source_file_id"),
        )


@dataclass(frozen=True)
class Provenance:
    source_file_id: str
    extraction_method: str
    page_number: int | None = None
    section: str | None = None
    text_span: tuple[int, int] | None = None
    bbox: tuple[float, float, float, float] | None = None
    snippet: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_file_id": self.source_file_id,
            "extraction_method": self.extraction_method,
            "page_number": self.page_number,
            "section": self.section,
            "text_span": list(self.text_span) if self.text_span else None,
            "bbox": list(self.bbox) if self.bbox else None,
            "snippet": self.snippet,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "Provenance":
        text_span = payload.get("text_span")
        bbox = payload.get("bbox")
        return cls(
            source_file_id=str(payload.get("source_file_id", "")),
            extraction_method=str(payload.get("extraction_method", "")),
            page_number=payload.get("page_number"),
            section=payload.get("section"),
            text_span=tuple(text_span) if text_span else None,
            bbox=tuple(float(part) for part in bbox) if bbox else None,
            snippet=payload.get("snippet"),
        )


@dataclass(frozen=True)
class ExtractedField:
    name: str
    raw_value: str | None = None
    normalized_value: str | None = None
    confidence: float = 0.0
    provenance: list[Provenance] = field(default_factory=list)
    warnings: list[ParserWarning] = field(default_factory=list)
    review_state: str = "unreviewed"

    @property
    def value(self) -> str | None:
        return self.normalized_value

    @property
    def source(self) -> str | None:
        if not self.provenance:
            return None
        return self.provenance[0].source_file_id

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "raw_value": self.raw_value,
            "normalized_value": self.normalized_value,
            "value": self.normalized_value,
            "confidence": self.confidence,
            "provenance": [item.to_dict() for item in self.provenance],
            "warnings": [item.to_dict() for item in self.warnings],
            "review_state": self.review_state,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ExtractedField":
        return cls(
            name=str(payload.get("name", "")),
            raw_value=payload.get("raw_value"),
            normalized_value=payload.get("normalized_value", payload.get("value")),
            confidence=float(payload.get("confidence", 0.0) or 0.0),
            provenance=[Provenance.from_dict(item) for item in payload.get("provenance", [])],
            warnings=[ParserWarning.from_dict(item) for item in payload.get("warnings", [])],
            review_state=str(payload.get("review_state", "unreviewed")),
        )


@dataclass(frozen=True)
class SourceFile:
    file_id: str
    path: Path
    sha256: str
    extension: str
    media_type: str
    role_guess: str
    warnings: list[ParserWarning] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "file_id": self.file_id,
            "path": str(self.path),
            "sha256": self.sha256,
            "extension": self.extension,
            "media_type": self.media_type,
            "role_guess": self.role_guess,
            "warnings": [item.to_dict() for item in self.warnings],
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "SourceFile":
        return cls(
            file_id=str(payload.get("file_id", "")),
            path=Path(str(payload.get("path", ""))),
            sha256=str(payload.get("sha256", "")),
            extension=str(payload.get("extension", "")),
            media_type=str(payload.get("media_type", "")),
            role_guess=str(payload.get("role_guess", "unknown")),
            warnings=[ParserWarning.from_dict(item) for item in payload.get("warnings", [])],
        )


@dataclass(frozen=True)
class ImageRecord:
    image_id: str
    source_file_id: str
    path: Path
    sha256: str
    width: int | None = None
    height: int | None = None
    role_guess: str = "evidence_image"
    order_hint: int | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "image_id": self.image_id,
            "source_file_id": self.source_file_id,
            "path": str(self.path),
            "sha256": self.sha256,
            "width": self.width,
            "height": self.height,
            "role_guess": self.role_guess,
            "order_hint": self.order_hint,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ImageRecord":
        return cls(
            image_id=str(payload.get("image_id", "")),
            source_file_id=str(payload.get("source_file_id", "")),
            path=Path(str(payload.get("path", ""))),
            sha256=str(payload.get("sha256", "")),
            width=payload.get("width"),
            height=payload.get("height"),
            role_guess=str(payload.get("role_guess", "evidence_image")),
            order_hint=payload.get("order_hint"),
        )


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    message: str
    severity: str = "blocker"
    field: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "message": self.message,
            "severity": self.severity,
            "field": self.field,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ValidationIssue":
        return cls(
            code=str(payload.get("code", "")),
            message=str(payload.get("message", "")),
            severity=str(payload.get("severity", "blocker")),
            field=payload.get("field"),
        )


@dataclass(frozen=True)
class ValidationResult:
    blockers: list[ValidationIssue] = field(default_factory=list)
    warnings: list[ValidationIssue] = field(default_factory=list)

    @property
    def can_export(self) -> bool:
        return not self.blockers

    def to_dict(self) -> dict[str, Any]:
        return {
            "can_export": self.can_export,
            "blockers": [item.to_dict() for item in self.blockers],
            "warnings": [item.to_dict() for item in self.warnings],
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ValidationResult":
        return cls(
            blockers=[ValidationIssue.from_dict(item) for item in payload.get("blockers", [])],
            warnings=[ValidationIssue.from_dict(item) for item in payload.get("warnings", [])],
        )


@dataclass(frozen=True)
class ParserResult:
    source_path: Path
    source_sha256: str
    source_files: list[SourceFile]
    detected_provider: str | None
    provider_confidence: float
    document_classification: str
    fields: dict[str, ExtractedField] = field(default_factory=dict)
    images: list[ImageRecord] = field(default_factory=list)
    validation: ValidationResult = field(default_factory=ValidationResult)
    warnings: list[ParserWarning] = field(default_factory=list)
    audit_metadata: dict[str, Any] = field(default_factory=dict)
    parser_result_id: str = ""
    work_item_id: str | None = None
    parser_version: str = PARSER_VERSION
    provider_config_version: str = ""
    inspection_mode: str = "unknown"
    inspection_site_source: str = "unknown"
    inspection_address_lines: list[str] = field(default_factory=list)
    inspection_site_name: str | None = None
    inspection_postcode: str | None = None
    inspection_location_confidence: float = 0.0
    inspection_location_evidence: list[Provenance] = field(default_factory=list)

    @property
    def provider_name(self) -> str | None:
        return self.detected_provider

    @property
    def audit(self) -> dict[str, Any]:
        return self.audit_metadata

    @property
    def source_file_ids(self) -> list[str]:
        return [item.file_id for item in self.source_files]

    def to_dict(self) -> dict[str, Any]:
        return {
            "parser_result_id": self.parser_result_id,
            "work_item_id": self.work_item_id,
            "source_path": str(self.source_path),
            "source_sha256": self.source_sha256,
            "source_file_ids": self.source_file_ids,
            "source_files": [item.to_dict() for item in self.source_files],
            "parser_version": self.parser_version,
            "provider_config_version": self.provider_config_version,
            "detected_provider": self.detected_provider,
            "provider_name": self.detected_provider,
            "provider_confidence": self.provider_confidence,
            "document_classification": self.document_classification,
            "fields": {key: value.to_dict() for key, value in self.fields.items()},
            "images": [item.to_dict() for item in self.images],
            "validation": self.validation.to_dict(),
            "warnings": [item.to_dict() for item in self.warnings],
            "audit_metadata": self.audit_metadata,
            "audit": self.audit_metadata,
            "inspection_mode": self.inspection_mode,
            "inspection_site_source": self.inspection_site_source,
            "inspection_address_lines": self.inspection_address_lines,
            "inspection_site_name": self.inspection_site_name,
            "inspection_postcode": self.inspection_postcode,
            "inspection_location_confidence": self.inspection_location_confidence,
            "inspection_location_evidence": [item.to_dict() for item in self.inspection_location_evidence],
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ParserResult":
        return cls(
            parser_result_id=str(payload.get("parser_result_id", "")),
            work_item_id=payload.get("work_item_id"),
            source_path=Path(str(payload.get("source_path", ""))),
            source_sha256=str(payload.get("source_sha256", "")),
            source_files=[SourceFile.from_dict(item) for item in payload.get("source_files", [])],
            parser_version=str(payload.get("parser_version", PARSER_VERSION)),
            provider_config_version=str(payload.get("provider_config_version", "")),
            detected_provider=payload.get("detected_provider", payload.get("provider_name")),
            provider_confidence=float(payload.get("provider_confidence", 0.0) or 0.0),
            document_classification=str(payload.get("document_classification", "unknown")),
            fields={key: ExtractedField.from_dict(value) for key, value in payload.get("fields", {}).items()},
            images=[ImageRecord.from_dict(item) for item in payload.get("images", [])],
            validation=ValidationResult.from_dict(payload.get("validation", {})),
            warnings=[ParserWarning.from_dict(item) for item in payload.get("warnings", [])],
            audit_metadata=dict(payload.get("audit_metadata", payload.get("audit", {}))),
            inspection_mode=str(payload.get("inspection_mode", "unknown")),
            inspection_site_source=str(payload.get("inspection_site_source", "unknown")),
            inspection_address_lines=list(payload.get("inspection_address_lines", [])),
            inspection_site_name=payload.get("inspection_site_name"),
            inspection_postcode=payload.get("inspection_postcode"),
            inspection_location_confidence=float(payload.get("inspection_location_confidence", 0.0) or 0.0),
            inspection_location_evidence=[
                Provenance.from_dict(item) for item in payload.get("inspection_location_evidence", [])
            ],
        )


@dataclass(frozen=True)
class TriageManifest:
    root_path: Path
    items: list[SourceFile]
    warnings: list[ParserWarning] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "root_path": str(self.root_path),
            "items": [item.to_dict() for item in self.items],
            "warnings": [item.to_dict() for item in self.warnings],
        }
