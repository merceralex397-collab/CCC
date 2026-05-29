"""Structural text-layer diff helper for generated PDFs."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ModuleNotFoundError as exc:  # pragma: no cover
    raise SystemExit(
        "Missing Python dependency: pypdf. Install with: "
        "python -m pip install -r tools/vehicle-valuation/requirements.txt"
    ) from exc


SECTION_HEADINGS = [
    "MARKET VALUATION EVIDENCE",
    "ADVERT EVIDENCE PACK",
    "SUBJECT VEHICLE DETAILS",
    "ASSESSED RETAIL MARKET VALUE",
    "MARKET RESEARCH",
    "VALUATION COMMENTARY",
    "CONCLUSION",
    "ADVERT REFERENCES",
    "SEARCH SUMMARY",
]

REPORT_TABLE_HEADERS = [
    "No.",
    "Vehicle / Derivative",
    "Year",
    "Mileage",
    "Seller",
    "Asking Price",
    "Comment",
]

EVIDENCE_TABLE_HEADERS = [
    "No.",
    "Advert ID",
    "Vehicle / Derivative",
    "Year",
    "Mileage",
    "Price",
    "Link",
]

REPORT_SUBJECT_LABELS = [
    "Registration",
    "Make / Model",
    "Body Type",
    "Fuel / Transmission",
    "Engine",
    "First Registered",
    "Mileage",
    "Colour",
    "Vehicle History",
    "VIN",
]

FOOTER_TEXT = "Collision Engineers Ltd | www.CollisionEngineers.co.uk | engineers@collisionengineers.co.uk"

FORBIDDEN_WORDING = [
    ("cherry-picked", re.compile(r"cherry-picked", re.IGNORECASE)),
    ("selected to increase value", re.compile(r"selected\s+to\s+increase\s+value", re.IGNORECASE)),
    ("highest adverts found", re.compile(r"highest\s+adverts\s+found", re.IGNORECASE)),
    ("client-favourable only", re.compile(r"client-favourable\s+only", re.IGNORECASE)),
    ("we ignored lower adverts", re.compile(r"we\s+ignored\s+lower\s+adverts", re.IGNORECASE)),
    ("lower adverts were disregarded", re.compile(r"lower\s+adverts\s+were\s+disregarded", re.IGNORECASE)),
    ("adverts chosen to beat the guide", re.compile(r"adverts\s+chosen\s+to\s+beat\s+the\s+guide", re.IGNORECASE)),
    ("EVA", re.compile(r"\bEVA\b", re.IGNORECASE)),
    ("uplift", re.compile(r"\buplift(?:s|ed|ing)?\b", re.IGNORECASE)),
    ("guide value", re.compile(r"\bguide\s+value\b", re.IGNORECASE)),
    ("guide valuation", re.compile(r"\bguide\s+valuation\b", re.IGNORECASE)),
    ("guide price", re.compile(r"\bguide\s+price\b", re.IGNORECASE)),
    ("Engineer Value", re.compile(r"\bEngineer\s+Value\b", re.IGNORECASE)),
    ("Original Eng Value", re.compile(r"\bOriginal\s+Eng(?:ineer)?\s+Value\b", re.IGNORECASE)),
]


def extract_text(path: Path) -> str:
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def normalise_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("Ł", "£")).strip()


def present_items(text: str, items: list[str]) -> list[str]:
    normalised = normalise_text(text)
    return [item for item in items if item in normalised]


def ordered_positions(text: str, items: list[str]) -> list[tuple[str, int]]:
    normalised = normalise_text(text)
    found = []
    for item in items:
        index = normalised.find(item)
        if index >= 0:
            found.append((item, index))
    return sorted(found, key=lambda item: item[1])


def section_slice(text: str, start: str, end: str) -> str:
    normalised = normalise_text(text)
    start_index = normalised.find(start)
    if start_index < 0:
        return normalised
    end_index = normalised.find(end, start_index + len(start))
    if end_index < 0:
        return normalised[start_index:]
    return normalised[start_index:end_index]


def check_presence_and_order(label: str, example_text: str, generated_text: str, items: list[str]) -> list[str]:
    problems = []
    expected = present_items(example_text, items)
    actual = present_items(generated_text, items)
    missing = [item for item in expected if item not in actual]
    extra = [item for item in actual if item not in expected]
    if missing:
        problems.append(f"Missing {label}: " + ", ".join(missing))
    if extra:
        problems.append(f"Extra {label}: " + ", ".join(extra))

    generated_positions = ordered_positions(generated_text, expected)
    if [item for item, _position in generated_positions] != expected:
        problems.append(f"{label.capitalize()} are out of expected order")
    return problems


def extract_assessed_value(text: str) -> str | None:
    normalised = normalise_text(text)
    match = re.search(
        r"Engineer's assessed retail value\s*(?:GBP\s*|£)?([0-9][0-9,]*(?:\.[0-9]{2})?)",
        normalised,
        flags=re.IGNORECASE,
    )
    if not match:
        return None
    return match.group(1).replace(",", "")


def has_currency_value(text: str, expected_number: str) -> bool:
    normalised = normalise_text(text)
    values = re.findall(r"(?:GBP\s*|£)?([0-9][0-9,]*(?:\.[0-9]{2})?)", normalised, flags=re.IGNORECASE)
    return expected_number in {value.replace(",", "") for value in values}


def check_report_specific_structure(example_text: str, generated_text: str) -> list[str]:
    if "MARKET VALUATION EVIDENCE" not in normalise_text(example_text):
        return []

    problems = []
    subject_text = section_slice(generated_text, "SUBJECT VEHICLE DETAILS", "ASSESSED RETAIL MARKET VALUE")
    subject_labels = present_items(subject_text, REPORT_SUBJECT_LABELS)
    if subject_labels != REPORT_SUBJECT_LABELS:
        missing = [label for label in REPORT_SUBJECT_LABELS if label not in subject_labels]
        if missing:
            problems.append("Missing subject detail labels: " + ", ".join(missing))
        if not missing:
            problems.append("Subject detail labels are out of expected order")

    value_box_text = section_slice(generated_text, "ASSESSED RETAIL MARKET VALUE", "MARKET RESEARCH")
    assessed_label_count = normalise_text(value_box_text).count("Engineer's assessed retail value")
    if assessed_label_count != 1:
        problems.append(f"Expected one assessed-value row, found {assessed_label_count}")
    unexpected_value_labels = [
        "Guide value reviewed",
        "Guide value",
        "Guide price",
    ]
    found_unexpected = [label for label in unexpected_value_labels if label in normalise_text(value_box_text)]
    if found_unexpected:
        problems.append("Unexpected value-box row labels: " + ", ".join(found_unexpected))
    return problems


def compare(example: Path, generated: Path) -> list[str]:
    example_text = extract_text(example)
    generated_text = extract_text(generated)
    problems = []
    problems.extend(check_presence_and_order("section headings", example_text, generated_text, SECTION_HEADINGS))
    if "ADVERT EVIDENCE PACK" in normalise_text(example_text):
        table_headers = EVIDENCE_TABLE_HEADERS
        example_table_text = section_slice(example_text, "ADVERT REFERENCES", "SEARCH SUMMARY")
        generated_table_text = section_slice(generated_text, "ADVERT REFERENCES", "SEARCH SUMMARY")
    else:
        table_headers = REPORT_TABLE_HEADERS
        example_table_text = section_slice(example_text, "MARKET RESEARCH", "VALUATION COMMENTARY")
        generated_table_text = section_slice(generated_text, "MARKET RESEARCH", "VALUATION COMMENTARY")
    problems.extend(check_presence_and_order("table headers", example_table_text, generated_table_text, table_headers))
    problems.extend(check_report_specific_structure(example_text, generated_text))

    if FOOTER_TEXT not in normalise_text(generated_text):
        problems.append("Footer text missing from generated PDF text layer")

    expected_value = extract_assessed_value(example_text)
    if expected_value and not has_currency_value(generated_text, expected_value):
        problems.append(f"Expected final value missing from generated PDF text layer: {expected_value}")

    normalised = normalise_text(generated_text)
    found = [label for label, pattern in FORBIDDEN_WORDING if pattern.search(normalised)]
    if found:
        problems.append("Forbidden external wording found: " + ", ".join(found))
    return problems


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if len(argv) != 2:
        print("Usage: diff_against_example.py <example.pdf> <generated.pdf>", file=sys.stderr)
        return 2
    problems = compare(Path(argv[0]), Path(argv[1]))
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1
    print("Structural PDF diff passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
