from __future__ import annotations

import json
import uuid
from pathlib import Path

from .models import PARSER_VERSION, ParserResult, ParserWarning, SourceFile
from .providers import detect_provider_match, load_provider_presets, provider_config_version
from .readers import read_document
from .rules import detect_inspection_mode, extract_fields
from .triage import build_manifest, file_sha256, triage_file
from .validation import validate_fields


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROVIDER_CONFIG = REPO_ROOT / "docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json"


def _dedupe_source_files(source_files: list[SourceFile]) -> list[SourceFile]:
    seen: set[str] = set()
    output: list[SourceFile] = []
    for source_file in source_files:
        if source_file.file_id in seen:
            continue
        seen.add(source_file.file_id)
        output.append(source_file)
    return output


class ParserCore:
    def __init__(self, provider_config: Path | None = None) -> None:
        self.provider_config = Path(provider_config or DEFAULT_PROVIDER_CONFIG)
        self.providers = load_provider_presets(self.provider_config)
        self.provider_config_version = provider_config_version(self.provider_config)

    def triage(self, source_path: Path):
        return build_manifest(Path(source_path))

    def parse(self, source_path: Path, provider: str | None = None) -> ParserResult:
        source_path = Path(source_path)
        manifest = build_manifest(source_path)
        if not manifest.items:
            warnings = manifest.warnings or [
                ParserWarning(code="no_files", message="No files were available to parse.", severity="blocker")
            ]
            return ParserResult(
                parser_result_id=f"parser-{uuid.uuid4()}",
                source_path=source_path,
                source_sha256="",
                source_files=[],
                provider_config_version=self.provider_config_version,
                detected_provider=None,
                provider_confidence=0.0,
                document_classification="unknown",
                warnings=warnings,
                audit_metadata={"parser_version": PARSER_VERSION, "provider_config": str(self.provider_config)},
            )

        primary = next(
            (item for item in manifest.items if item.role_guess in {"instruction", "image_pack"}),
            manifest.items[0],
        )
        primary_document = read_document(primary)
        parser_warnings = list(manifest.warnings) + list(primary_document.reader_notes)
        source_files = list(manifest.items)
        candidates = [(primary, primary_document)]

        for attachment in primary_document.attachments:
            attachment_path = Path(attachment)
            if not attachment_path.is_absolute():
                attachment_path = primary.path.parent / attachment_path
            if not attachment_path.exists():
                parser_warnings.append(
                    ParserWarning(
                        code="attachment_missing",
                        message=f"Email attachment {attachment} was referenced but was not available for parsing.",
                        severity="warning",
                        source_file_id=primary.file_id,
                    )
                )
                continue
            attachment_source = triage_file(attachment_path)
            attachment_document = read_document(attachment_source)
            source_files.append(attachment_source)
            parser_warnings.extend(attachment_document.reader_notes)
            candidates.append((attachment_source, attachment_document))

        matched_candidates = [
            (source_file, candidate_document, detect_provider_match(candidate_document.text, self.providers, forced_provider=provider))
            for source_file, candidate_document in candidates
        ]

        def candidate_rank(candidate) -> tuple[int, int, int, int, int]:
            _source_file, candidate_document, candidate_match = candidate
            has_provider = 1 if candidate_match.provider else 0
            is_instruction = 1 if candidate_document.document_type not in {"image", "image_pack", "unknown"} else 0
            is_attachment_document = 1 if candidate_document is not primary_document and candidate_document.document_type != "email" else 0
            return (has_provider, candidate_match.score, is_instruction, is_attachment_document, len(candidate_document.text or ""))

        selected_source, document, match = max(matched_candidates, key=candidate_rank)
        if match.provider is None:
            parser_warnings.append(
                ParserWarning(
                    code="provider_not_detected",
                    message="No provider preset matched the available source text.",
                    severity="warning",
                    source_file_id=primary.file_id,
                )
            )

        fields = extract_fields(document, match.provider)
        all_images = []
        for _source_file, candidate_document in candidates:
            all_images.extend(candidate_document.images)
        for source_file in manifest.items:
            if source_file.role_guess == "evidence_image" and source_file.file_id != primary.file_id:
                image_document = read_document(source_file)
                all_images.extend(image_document.images)
                parser_warnings.extend(image_document.reader_notes)

        inspection_mode, inspection_source, address_lines, postcode, inspection_confidence, evidence = detect_inspection_mode(
            fields
        )
        validation = validate_fields(
            fields,
            detected_provider=match.provider.name if match.provider else None,
            parser_warnings=parser_warnings,
            has_images=bool(all_images),
            export_required=document.document_type not in {"image", "image_pack"},
        )
        source_sha = primary.sha256 if source_path.is_file() else file_sha256(primary.path)
        return ParserResult(
            parser_result_id=f"parser-{uuid.uuid4()}",
            source_path=source_path,
            source_sha256=source_sha,
            source_files=_dedupe_source_files(source_files),
            parser_version=PARSER_VERSION,
            provider_config_version=self.provider_config_version,
            detected_provider=match.provider.name if match.provider else None,
            provider_confidence=match.confidence,
            document_classification=document.document_type if source_path.is_file() else "batch",
            fields=fields,
            images=all_images,
            validation=validation,
            warnings=parser_warnings,
            audit_metadata={
                "parser_version": PARSER_VERSION,
                "provider_config": str(self.provider_config),
                "provider_count": len(self.providers),
                "provider_match_score": match.score,
                "matched_provider_phrases": list(match.matched_phrases),
                "reader_method": document.reader_method,
                "extraction_source_file_id": selected_source.file_id,
                "attachment_count": max(0, len(source_files) - len(manifest.items)),
                "text_preview_length": len(document.text),
            },
            inspection_mode=inspection_mode,
            inspection_site_source=inspection_source,
            inspection_address_lines=address_lines,
            inspection_postcode=postcode,
            inspection_location_confidence=inspection_confidence,
            inspection_location_evidence=evidence,
        )

    def parse_batch(self, folder: Path) -> list[ParserResult]:
        manifest = build_manifest(Path(folder))
        return [self.parse(item.path) for item in manifest.items if item.role_guess in {"instruction", "image_pack"}]

    @staticmethod
    def result_from_json(path: Path) -> ParserResult:
        return ParserResult.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))
