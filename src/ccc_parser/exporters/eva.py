from __future__ import annotations

from collections import OrderedDict
from typing import Any

from ..constants import EVA_FIELD_ORDER, FIELD_LABELS
from ..models import ParserResult
from ..normalization import normalize_inspection_address


BLANK_EVA_INSPECTION_ADDRESS = "\n".join([""] * 6)
NON_EXPORT_DOCUMENT_CLASSES = {"image", "image_pack"}


def export_eva_payload(result: ParserResult, *, allow_blockers: bool = False) -> OrderedDict[str, str]:
    if result.document_classification in NON_EXPORT_DOCUMENT_CLASSES:
        raise ValueError(f"Cannot export EVA payload because {result.document_classification} is not an instruction export candidate.")
    if result.validation.blockers and not allow_blockers:
        codes = ", ".join(issue.code for issue in result.validation.blockers)
        raise ValueError(f"Cannot export EVA payload while blockers remain: {codes}")
    payload: OrderedDict[str, str] = OrderedDict()
    for field_name in EVA_FIELD_ORDER:
        field = result.fields.get(field_name)
        value = ((field.normalized_value if field else "") or "")
        if field_name == "inspection_address":
            payload[FIELD_LABELS[field_name]] = normalize_inspection_address(value) or BLANK_EVA_INSPECTION_ADDRESS
        else:
            payload[FIELD_LABELS[field_name]] = value.strip()
    return payload


def export_eva_dict(result: ParserResult, *, allow_blockers: bool = False) -> dict[str, Any]:
    return dict(export_eva_payload(result, allow_blockers=allow_blockers))
