from __future__ import annotations

from typing import Any

from .models import ParserResult, ValidationIssue


def build_evidence_package_manifest(
    result: ParserResult,
    *,
    preview_full_vehicle_image_id: str | None = None,
    preview_damage_image_id: str | None = None,
) -> dict[str, Any]:
    images = list(result.images)
    selected_preview_ids = [
        image_id
        for image_id in (preview_full_vehicle_image_id, preview_damage_image_id)
        if image_id
    ]
    if not selected_preview_ids:
        selected_preview_ids = [image.image_id for image in images[:2]]
    ordered_ids = selected_preview_ids + [image.image_id for image in images]
    warnings: list[ValidationIssue] = []
    if images and len(selected_preview_ids) < 2:
        warnings.append(
            ValidationIssue(
                code="image_previews_need_review",
                message="Select full-vehicle and close-up damage preview images before final package export.",
                severity="warning",
                field="images",
            )
        )
    image_lookup = {image.image_id: image for image in images}
    return {
        "parser_result_id": result.parser_result_id,
        "source_file_ids": result.source_file_ids,
        "image_order_rule": "preview_full_vehicle, preview_damage_closeup, all_images_including_previews",
        "preview_image_ids": selected_preview_ids,
        "ordered_image_ids": ordered_ids,
        "images": [image.to_dict() for image in images],
        "ordered_images": [
            image_lookup[image_id].to_dict()
            for image_id in ordered_ids
            if image_id in image_lookup
        ],
        "warnings": [warning.to_dict() for warning in warnings],
    }
