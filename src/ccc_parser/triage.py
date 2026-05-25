from __future__ import annotations

import hashlib
import mimetypes
from pathlib import Path

from .constants import DOCUMENT_EXTENSIONS, IMAGE_EXTENSIONS
from .models import ParserWarning, SourceFile, TriageManifest


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_id_for(path: Path, sha256: str | None = None) -> str:
    digest = sha256 or file_sha256(path)
    return f"file-{digest[:16]}"


def classify_path(path: Path) -> tuple[str, str]:
    suffix = path.suffix.lower()
    if suffix in IMAGE_EXTENSIONS:
        return "image", "evidence_image"
    if suffix in {".msg", ".eml"}:
        return "email", "instruction"
    if suffix in {".pdf", ".docx", ".doc", ".txt", ".md", ".json"}:
        lowered = path.name.lower()
        if "image" in lowered or lowered.startswith("__images"):
            return "document", "image_pack"
        return "document", "instruction"
    return "unknown", "unknown"


def media_type_for(path: Path) -> str:
    guessed, _ = mimetypes.guess_type(path.name)
    if guessed:
        return guessed
    suffix = path.suffix.lower()
    return {
        ".msg": "application/vnd.ms-outlook",
        ".doc": "application/msword",
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    }.get(suffix, "application/octet-stream")


def triage_file(path: Path) -> SourceFile:
    path = Path(path)
    warnings: list[ParserWarning] = []
    suffix = path.suffix.lower()
    if suffix not in DOCUMENT_EXTENSIONS and suffix not in IMAGE_EXTENSIONS:
        warnings.append(
            ParserWarning(
                code="unsupported_file_type",
                message=f"Unsupported file extension '{suffix or '<none>'}' requires manual review.",
            )
        )
    sha = file_sha256(path)
    _, role = classify_path(path)
    return SourceFile(
        file_id=file_id_for(path, sha),
        path=path,
        sha256=sha,
        extension=suffix,
        media_type=media_type_for(path),
        role_guess=role,
        warnings=warnings,
    )


def build_manifest(path: Path) -> TriageManifest:
    path = Path(path)
    warnings: list[ParserWarning] = []
    if path.is_file():
        return TriageManifest(root_path=path, items=[triage_file(path)], warnings=warnings)
    if not path.is_dir():
        return TriageManifest(
            root_path=path,
            items=[],
            warnings=[ParserWarning(code="path_missing", message=f"{path} does not exist.", severity="blocker")],
        )
    items: list[SourceFile] = []
    for item in sorted(candidate for candidate in path.rglob("*") if candidate.is_file()):
        try:
            items.append(triage_file(item))
        except OSError as exc:
            warnings.append(
                ParserWarning(
                    code="triage_failed",
                    message=f"Could not triage {item}: {exc}",
                    severity="warning",
                )
            )
    return TriageManifest(root_path=path, items=items, warnings=warnings)
