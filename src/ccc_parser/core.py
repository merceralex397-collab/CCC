from __future__ import annotations

import json
import uuid
from pathlib import Path

from .models import PARSER_VERSION, ExtractedField, ParserResult, ParserWarning, SourceFile
from .providers import ProviderMatch, detect_provider_match, load_provider_presets, provider_config_version
from .readers import DocumentModel, read_document
from .rules import detect_inspection_mode, extract_fields
from .triage import build_manifest, triage_file
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


def _field_value(field: ExtractedField | None) -> str:
    if field is None:
        return ""
    return (field.normalized_value or field.raw_value or "").strip()


def _is_export_candidate(document: DocumentModel) -> bool:
    return document.document_type not in {"image", "image_pack", "unknown"}


def _merge_engineer_fields(
    instruction_fields: dict[str, ExtractedField],
    engineer_fields: dict[str, ExtractedField],
    *,
    engineer_source_file_id: str,
) -> tuple[dict[str, ExtractedField], list[ParserWarning], list[str]]:
    merged = dict(instruction_fields)
    warnings: list[ParserWarning] = []
    overrides: list[str] = []
    for field_name, engineer_field in engineer_fields.items():
        if field_name == "work_provider" or not _field_value(engineer_field):
            continue
        current = merged.get(field_name)
        current_value = _field_value(current)
        engineer_value = _field_value(engineer_field)
        if current_value and current_value != engineer_value:
            warnings.append(
                ParserWarning(
                    code="engineer_report_field_override",
                    message=f"Engineer report value replaced instruction field '{field_name}'.",
                    severity="warning",
                    source_file_id=engineer_source_file_id,
                )
            )
            overrides.append(field_name)
        if not current_value or current_value != engineer_value:
            merged[field_name] = engineer_field
    return merged, warnings, overrides


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

        root_candidates = [item for item in manifest.items if item.role_guess in {"instruction", "image_pack"}]
        if not root_candidates:
            root_candidates = [manifest.items[0]]
        primary = root_candidates[0]
        parser_warnings = list(manifest.warnings)
        source_files = list(manifest.items)
        candidates: list[tuple[SourceFile, DocumentModel]] = []
        queue = list(root_candidates)
        seen_candidate_ids: set[str] = set()

        while queue:
            candidate_source = queue.pop(0)
            if candidate_source.file_id in seen_candidate_ids:
                continue
            seen_candidate_ids.add(candidate_source.file_id)
            candidate_document = read_document(candidate_source)
            parser_warnings.extend(candidate_document.reader_notes)
            candidates.append((candidate_source, candidate_document))

            for attachment in candidate_document.attachments:
                attachment_path = Path(attachment)
                if not attachment_path.is_absolute():
                    attachment_path = candidate_source.path.parent / attachment_path
                if not attachment_path.exists():
                    parser_warnings.append(
                        ParserWarning(
                            code="attachment_missing",
                            message=f"Email attachment {attachment} was referenced but was not available for parsing.",
                            severity="warning",
                            source_file_id=candidate_source.file_id,
                        )
                    )
                    continue
                attachment_source = triage_file(attachment_path)
                source_files.append(attachment_source)
                queue.append(attachment_source)

        matched_candidates = [
            (source_file, candidate_document, detect_provider_match(candidate_document.text, self.providers, forced_provider=provider))
            for source_file, candidate_document in candidates
        ]

        def candidate_rank(candidate: tuple[SourceFile, DocumentModel, ProviderMatch]) -> tuple[int, int, int, int, int]:
            _source_file, candidate_document, candidate_match = candidate
            has_provider = 1 if candidate_match.provider else 0
            is_instruction = 1 if _is_export_candidate(candidate_document) else 0
            is_attachment_document = 1 if _source_file not in manifest.items and candidate_document.document_type != "email" else 0
            return (has_provider, candidate_match.score, is_instruction, is_attachment_document, len(candidate_document.text or ""))

        selected_source, document, match = max(matched_candidates, key=candidate_rank)
        engineer_merge: tuple[SourceFile, DocumentModel, ProviderMatch] | None = None
        if source_path.is_dir():
            instruction_matches = [
                candidate
                for candidate in matched_candidates
                if candidate[2].provider and not candidate[2].provider.engineer_report and _is_export_candidate(candidate[1])
            ]
            engineer_matches = [
                candidate
                for candidate in matched_candidates
                if candidate[2].provider and candidate[2].provider.engineer_report and _is_export_candidate(candidate[1])
            ]
            if len(instruction_matches) == 1 and len(engineer_matches) == 1:
                selected_source, document, match = instruction_matches[0]
                engineer_merge = engineer_matches[0]

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
        engineer_overrides: list[str] = []
        if engineer_merge is not None:
            engineer_source, engineer_document, engineer_match = engineer_merge
            engineer_fields = extract_fields(engineer_document, engineer_match.provider)
            fields, engineer_warnings, engineer_overrides = _merge_engineer_fields(
                fields,
                engineer_fields,
                engineer_source_file_id=engineer_source.file_id,
            )
            parser_warnings.extend(engineer_warnings)

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
        source_sha = primary.sha256 if source_path.is_file() else selected_source.sha256
        audit_metadata = {
            "parser_version": PARSER_VERSION,
            "provider_config": str(self.provider_config),
            "provider_count": len(self.providers),
            "provider_match_score": match.score,
            "matched_provider_phrases": list(match.matched_phrases),
            "reader_method": document.reader_method,
            "extraction_source_file_id": selected_source.file_id,
            "attachment_count": max(0, len(source_files) - len(manifest.items)),
            "text_preview_length": len(document.text),
        }
        if engineer_merge is not None:
            engineer_source, _engineer_document, engineer_match = engineer_merge
            audit_metadata.update(
                {
                    "engineer_report_provider": engineer_match.provider.name if engineer_match.provider else None,
                    "engineer_report_source_file_id": engineer_source.file_id,
                    "engineer_report_field_overrides": engineer_overrides,
                }
            )
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
            audit_metadata=audit_metadata,
            inspection_mode=inspection_mode,
            inspection_site_source=inspection_source,
            inspection_address_lines=address_lines,
            inspection_postcode=postcode,
            inspection_location_confidence=inspection_confidence,
            inspection_location_evidence=evidence,
        )

    def parse_batch(self, folder: Path) -> list[ParserResult]:
        return list(self.parse_batch_report(folder)["results"])

    def parse_batch_report(self, folder: Path) -> dict[str, list[ParserResult] | list[dict[str, str]]]:
        manifest = build_manifest(Path(folder))
        results: list[ParserResult] = []
        errors: list[dict[str, str]] = []
        for item in manifest.items:
            if item.role_guess not in {"instruction", "image_pack"}:
                continue
            try:
                results.append(self.parse(item.path))
            except Exception as exc:
                errors.append({"path": str(item.path), "message": str(exc), "error_type": type(exc).__name__})
        return {"results": results, "errors": errors}

    @staticmethod
    def result_from_json(path: Path) -> ParserResult:
        return ParserResult.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))
