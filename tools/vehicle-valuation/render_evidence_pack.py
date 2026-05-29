"""Render the advert evidence pack PDF with Playwright-captured advert pages."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

from _pdf_common import (
    available_output_path,
    capture_advert_page,
    CookieBannerNotDismissedError,
    load_payload,
    merge_pdfs,
    normalise_registration,
    output_dir,
    render_pdf,
    validate_or_exit,
)
from validate_evidence_pack import validate_payload


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if len(argv) != 1:
        print("Usage: render_evidence_pack.py <payload.json>", file=sys.stderr)
        return 2

    payload = load_payload(argv[0])
    validate_or_exit(payload)

    # Hard-fail early if playwright is not installed — all captures would fail and the
    # agent would incorrectly be told to find more adverts.
    try:
        from playwright.sync_api import sync_playwright as _sync_playwright  # noqa: F401
        from playwright_stealth import Stealth as _Stealth  # noqa: F401
    except ModuleNotFoundError as exc:
        print(
            f"Missing dependency: {exc.name}. Install with: "
            "pip install playwright playwright-stealth && playwright install chromium",
            file=sys.stderr,
        )
        return 2

    failed_urls: list[str] = []
    captured_paths: list[str] = []
    working_adverts: list[dict] = []

    with tempfile.TemporaryDirectory() as tmp_dir:
        for advert in payload["adverts"]:
            url = advert["url"]
            try:
                path = capture_advert_page(url, tmp_dir)
                captured_paths.append(path)
                working_adverts.append(advert)
            except CookieBannerNotDismissedError as exc:
                print(f"ERROR: {exc}", file=sys.stderr)
                return 2
            except Exception as exc:
                failed_urls.append(url)
                print(f"WARNING: Capture failed for {url}: {exc}", file=sys.stderr)

        if failed_urls:
            working_payload = {**payload, "adverts": working_adverts}
            errors, _ = validate_payload(working_payload)
            # Match sufficiency errors from _validate_evidence_assessment and the early-exit
            # at line 244-245 of validate_evidence_pack.py (empty adverts list).
            sufficiency_errors = [
                e for e in errors
                if "suitable live adverts" in e
                or "materially comparable" in e
                or "adverts must be a non-empty list" in e
            ]
            if sufficiency_errors:
                print(
                    json.dumps({
                        "status": "insufficient_evidence",
                        "failed_captures": failed_urls,
                        "adverts_excluded": len(failed_urls),
                        "adverts_still_needed": _adverts_still_needed(working_adverts),
                    }),
                    file=sys.stderr,
                )
                return 1
        else:
            working_payload = payload

        reg = normalise_registration(payload["subject_vehicle"]["registration"])
        table_pdf = None
        final_path = available_output_path(
            output_dir(working_payload) / f"{reg}_advert_evidence_pack.pdf"
        )
        try:
            table_pdf = render_pdf(
                working_payload,
                "evidence_pack.html.j2",
                f"{reg}_advert_evidence_pack_table_tmp.pdf",
                "Advert Evidence Pack",
                validate=False,
            )
            merge_pdfs([str(table_pdf)] + captured_paths, str(final_path))
        finally:
            if table_pdf is not None:
                Path(table_pdf).unlink(missing_ok=True)

    print(str(final_path))
    return 0


def _adverts_still_needed(working_adverts: list[dict]) -> int:
    # max() rather than sum() because a single well-chosen advert can satisfy
    # both the suitable-count and the supportive-comparable-count thresholds.
    suitable = [a for a in working_adverts if a.get("evidence_role") != "excluded"]
    supportive_comparable = [
        a for a in suitable
        if a.get("supports_assessed_value") is True
        and a.get("is_materially_comparable") is True
        and a.get("evidence_role") == "supportive"
    ]
    return max(max(0, 3 - len(suitable)), max(0, 2 - len(supportive_comparable)))


if __name__ == "__main__":
    raise SystemExit(main())
