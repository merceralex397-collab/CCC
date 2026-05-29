"""Render the market valuation evidence report PDF."""

from __future__ import annotations

import sys

from _pdf_common import load_payload, normalise_registration, render_pdf, validate_or_exit


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if len(argv) != 1:
        print("Usage: render_report.py <payload.json>", file=sys.stderr)
        return 2
    payload = load_payload(argv[0])
    validate_or_exit(payload)
    reg = normalise_registration(payload["subject_vehicle"]["registration"])
    path = render_pdf(
        payload,
        "report.html.j2",
        f"{reg}_market_valuation_evidence.pdf",
        "Market Valuation Evidence",
        validate=False,
    )
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
