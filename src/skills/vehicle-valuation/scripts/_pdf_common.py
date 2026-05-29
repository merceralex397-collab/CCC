"""Shared rendering helpers for vehicle valuation PDFs."""

from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ModuleNotFoundError as exc:  # pragma: no cover - exercised in missing dependency environments.
    missing = exc.name or "required package"
    raise SystemExit(
        f"Missing Python dependency: {missing}. Install with: "
        "python -m pip install -r skills/vehicle-valuation/scripts/requirements.txt"
    ) from exc

from validate_evidence_pack import validate_payload


SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_DIR.parents[1]
# Shared CE brand + layout live in the ce-branding skill (consolidated 2026-05-29).
CE_BRANDING_DIR = SKILL_DIR.parent / "ce-branding"
TEMPLATE_DIR = CE_BRANDING_DIR / "assets" / "templates"
CSS_PATH = TEMPLATE_DIR / "styles.css"
LOGO_PATH = CE_BRANDING_DIR / "assets" / "brand" / "logo.png"
_DLL_DIRECTORY_HANDLES: list[object] = []
DESKTOP_CAPTURE_WIDTH = 1440
DESKTOP_CAPTURE_VIEWPORT_HEIGHT = 1200
PDF_HEIGHT_BUFFER_PX = 300
COOKIE_DISMISS_BUTTON_PATTERNS = (
    r"^Reject All$",
    r"^Essential Cookies Only$",
)
COOKIE_BLOCKED_TEXT_MARKERS = (
    "We use cookies on our site",
    "Essential Cookies Only",
)


class CookieBannerNotDismissedError(RuntimeError):
    """Raised when an advert capture would include Autotrader's cookie overlay."""


def load_payload(path: str | Path) -> dict[str, Any]:
    payload_path = Path(path).resolve()
    with payload_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    payload["_payload_path"] = str(payload_path)
    return payload


def validate_or_exit(payload: dict[str, Any]) -> None:
    errors, warnings = validate_payload(payload)
    for warning in warnings:
        print("WARNING: " + warning, file=sys.stderr)
    if errors:
        print("Payload validation failed:", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        raise SystemExit(1)


def normalise_registration(registration: str) -> str:
    return "".join(ch for ch in registration.upper() if ch.isalnum())


def output_dir(payload: dict[str, Any]) -> Path:
    reg = normalise_registration(payload["subject_vehicle"]["registration"])
    path = REPO_ROOT / "output" / reg
    path.mkdir(parents=True, exist_ok=True)
    return path


def available_output_path(path: Path) -> Path:
    """Return a non-colliding output path by appending _1, _2, etc."""

    if not path.exists():
        return path

    index = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{index}{path.suffix}")
        if not candidate.exists():
            return candidate
        index += 1


def money(value: Any, decimals: bool = True) -> str:
    if isinstance(value, str):
        cleaned = re.sub(r"(?i)\bgbp\s*", "", value).replace("£", "").replace("Ł", "").replace(",", "").strip()
        try:
            value = float(cleaned)
        except ValueError:
            return pdf_text(value)
    places = 2 if decimals else 0
    return f"£{float(value):,.{places}f}"


def mileage_display(value: Any) -> str:
    if isinstance(value, str):
        return value
    return f"{int(value):,}"


def year_display(value: Any) -> str:
    text = str(value)
    match = re.search(r"\b(19|20)\d{2}\b", text)
    return match.group(0) if match else text


def subject_mileage_display(value: Any) -> str:
    display = mileage_display(value)
    if not any(ch.isdigit() for ch in display):
        return display
    return display if "mile" in display.lower() else f"{display} miles"


def pdf_text(value: Any) -> str:
    return re.sub(r"(?i)\bgbp\s*", "£", str(value)).replace("Ł", "£")


def optional_money(value: Any) -> str | None:
    if value is None or value == "":
        return None
    return money(value)


def today_uk() -> str:
    return datetime.now().strftime("%d/%m/%Y")


def vehicle_label(advert: dict[str, Any]) -> str:
    bits = [
        advert.get("make"),
        advert.get("model"),
        advert.get("derivative_or_engine"),
    ]
    return " ".join(str(bit).strip() for bit in bits if bit)


def subject_display_name(subject: dict[str, Any]) -> str:
    description = subject.get("vehicle_description")
    if description:
        return str(description).strip()
    return " ".join(x for x in [subject.get("make"), subject.get("model"), subject.get("derivative")] if x)


DEFAULT_VEHICLE_HISTORY = "Assumed full service history unless stated otherwise"
CLEAN_HISTORY_MARKERS = (
    "no adverse history",
    "no adverse recorded",
    "clear vehicle history",
    "clear history",
    "history check clear",
    "history clear",
)
MATERIAL_HISTORY_MARKERS = (
    "category",
    "cat s",
    "cat n",
    "write-off",
    "write off",
    "written off",
    "insurance loss",
    "stolen",
    "scrapped",
    "salvage",
    "mileage discrepancy",
    "discrepancy",
    "clock",
    "import",
    "export",
    "damage",
    "outstanding finance",
)


def vehicle_history_display(value: Any) -> str:
    text = str(value or "").strip()
    if not text:
        return DEFAULT_VEHICLE_HISTORY

    normalised = " ".join(text.lower().replace("-", " ").split())
    has_clean_marker = any(marker in normalised for marker in CLEAN_HISTORY_MARKERS)
    has_material_marker = any(marker in normalised for marker in MATERIAL_HISTORY_MARKERS)
    if has_clean_marker and not has_material_marker:
        return "No adverse history recorded"
    return text


def pair_subject_rows(subject: dict[str, Any]) -> list[list[dict[str, str]]]:
    rows = [
        ("Registration", subject.get("registration")),
        ("Make / Model", subject_display_name(subject)),
        ("Body Type", subject.get("body_type")),
        ("Fuel / Transmission", " / ".join(x for x in [subject.get("fuel"), subject.get("transmission")] if x)),
        ("Engine", subject.get("engine")),
        ("First Registered", subject.get("first_registered")),
        ("Mileage", subject_mileage_display(subject.get("mileage"))),
        ("Colour", subject.get("colour", "Not stated")),
        ("Vehicle History", vehicle_history_display(subject.get("vehicle_history"))),
        ("VIN", subject.get("vin", "Not stated")),
    ]
    cells = [{"label": label, "value": str(value or "Not stated")} for label, value in rows]
    return [cells[index : index + 2] for index in range(0, len(cells), 2)]


def template_context(payload: dict[str, Any], title: str) -> dict[str, Any]:
    subject = payload["subject_vehicle"]
    adverts = []
    for advert in payload["adverts"]:
        enriched = dict(advert)
        enriched["vehicle"] = vehicle_label(advert)
        enriched["price"] = pdf_text(advert.get("price", ""))
        enriched["registration_year_display"] = year_display(advert["registration_year"])
        enriched["mileage_display"] = mileage_display(advert["mileage"])
        enriched["report_comment"] = pdf_text(advert.get("report_comment") or (
            f"{advert['comparability_note']} {advert['differences_note']}"
        ).strip())
        enriched["detail_rows"] = advert_detail_rows(enriched)
        adverts.append(enriched)

    meta = payload.get("meta", {})
    meta.setdefault("report_date", today_uk())

    return {
        "title": title,
        "css": CSS_PATH.read_text(encoding="utf-8"),
        "logo_uri": LOGO_PATH.resolve().as_uri(),
        "meta": meta,
        "subject": subject,
        "subject_display": subject_display_name(subject),
        "subject_rows": pair_subject_rows(subject),
        "guide_value": optional_money(payload.get("guide_value")),
        "assessed_value": money(payload["assessed_retail_value"]),
        "adverts": adverts,
        "intro": pdf_text(payload.get(
            "intro",
            "We have undertaken a review of comparable vehicles currently advertised in the retail market.",
        )),
        "market_research": pdf_text(payload.get(
            "market_research",
            "The following comparable retail market evidence has been reviewed having regard to make, model, age, mileage, engine, transmission, specification and general condition.",
        )),
        "valuation_commentary": [pdf_text(paragraph) for paragraph in payload.get("valuation_commentary", [])],
        "conclusion": pdf_text(payload.get("conclusion", "")),
        "vat_note": pdf_text(payload.get("vat_note")) if payload.get("vat_note") else None,
        "search_summary": pdf_text(payload.get(
            "search_summary",
            "Searches were conducted using live Autotrader market evidence for vehicles considered comparable to the subject vehicle.",
        )),
        "body_class": "",
    }


def advert_detail_rows(advert: dict[str, Any]) -> list[dict[str, str]]:
    return [
        {"label": "Source", "value": pdf_text(advert.get("source", ""))},
        {"label": "URL / link", "value": pdf_text(advert.get("url", "")), "url": str(advert.get("url", ""))},
        {"label": "Advert ID", "value": pdf_text(advert.get("advert_id") or "Not stated")},
        {"label": "Date accessed", "value": pdf_text(advert.get("date_accessed", ""))},
        {"label": "Price", "value": pdf_text(advert.get("price", ""))},
        {"label": "Make / model / derivative", "value": pdf_text(advert.get("vehicle", ""))},
        {"label": "Registration year", "value": pdf_text(advert.get("registration_year", ""))},
        {"label": "Mileage", "value": pdf_text(advert.get("mileage_display", ""))},
        {"label": "Fuel", "value": pdf_text(advert.get("fuel", ""))},
        {"label": "Transmission", "value": pdf_text(advert.get("transmission", ""))},
        {"label": "Body style", "value": pdf_text(advert.get("body_style", ""))},
        {"label": "Seller type", "value": pdf_text(advert.get("seller_type", ""))},
        {"label": "Location", "value": pdf_text(advert.get("location", ""))},
        {"label": "Comparability", "value": pdf_text(advert.get("comparability_note", ""))},
        {"label": "Limitations / differences", "value": pdf_text(advert.get("differences_note", ""))},
        {"label": "Evidence role", "value": pdf_text(advert.get("evidence_role", ""))},
    ]


def render_pdf(payload: dict[str, Any], template_name: str, output_name: str, title: str, *, validate: bool = True) -> Path:
    if validate:
        validate_or_exit(payload)
    path = available_output_path(output_dir(payload) / output_name)
    try:
        return _render_weasy(payload, template_name, path, title)
    except (OSError, ImportError) as exc:
        print(
            "WARNING: WeasyPrint is unavailable because its Windows GTK/Pango libraries are not installed. "
            "Falling back to ReportLab for this render.",
            file=sys.stderr,
        )
        print(f"WARNING: {exc}", file=sys.stderr)
        return _render_reportlab(payload, template_name, path, title)


def _render_weasy(payload: dict[str, Any], template_name: str, path: Path, title: str) -> Path:
    configure_weasyprint_native_libraries()
    from weasyprint import HTML

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "xml", "j2"]),
    )
    template = env.get_template(template_name)

    def write_pdf(body_class: str = "") -> None:
        context = template_context(payload, title)
        context["body_class"] = body_class
        html = template.render(**context)
        HTML(string=html, base_url=str(SKILL_DIR)).write_pdf(path)

    write_pdf()
    if template_name == "report.html.j2":
        for body_class in ["report-compact", "report-ultra-compact"]:
            if _pdf_page_count(path) <= 1:
                break
            write_pdf(body_class)
    return path.resolve()


def _pdf_page_count(path: Path) -> int:
    from pypdf import PdfReader

    return len(PdfReader(str(path)).pages)


def configure_weasyprint_native_libraries() -> None:
    """Point WeasyPrint at the MSYS2 native DLLs on Windows when available."""

    if not sys.platform.startswith("win"):
        return

    configured = os.environ.get("WEASYPRINT_DLL_DIRECTORIES")
    candidates = [Path(path) for path in configured.split(os.pathsep) if path] if configured else []
    candidates.extend(
        [
            Path(r"C:\msys64\mingw64\bin"),
            Path(r"C:\msys64\ucrt64\bin"),
        ]
    )

    for candidate in candidates:
        if (candidate / "libgobject-2.0-0.dll").exists() and (candidate / "libpango-1.0-0.dll").exists():
            os.environ.setdefault("WEASYPRINT_DLL_DIRECTORIES", str(candidate))
            if hasattr(os, "add_dll_directory"):
                handle = os.add_dll_directory(str(candidate))
                _DLL_DIRECTORY_HANDLES.append(handle)
            return


def _render_reportlab(payload: dict[str, Any], template_name: str, path: Path, title: str) -> Path:
    try:
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import mm
        from reportlab.platypus import HRFlowable, Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    except ModuleNotFoundError as exc:  # pragma: no cover
        raise SystemExit(
            f"Missing Python dependency: {exc.name}. Install with: "
            "python -m pip install -r skills/vehicle-valuation/scripts/requirements.txt"
        ) from exc

    context = template_context(payload, title)
    brand_red = colors.HexColor("#C80A32")
    grid_grey = colors.HexColor("#BEBEBE")
    styles = getSampleStyleSheet()
    normal = ParagraphStyle("NormalCE", parent=styles["Normal"], fontName="Helvetica", fontSize=9.2, leading=11.2)
    small = ParagraphStyle("SmallCE", parent=normal, fontSize=8.0, leading=9.5)
    table_text = ParagraphStyle("TableTextCE", parent=normal, fontSize=8.8, leading=10.5)
    table_small = ParagraphStyle("TableSmallCE", parent=normal, fontSize=8.2, leading=9.6)
    header_cell = ParagraphStyle("HeaderCellCE", parent=table_text, textColor=colors.white, fontName="Helvetica-Bold")
    heading = ParagraphStyle(
        "HeadingCE",
        parent=normal,
        textColor=colors.HexColor("#222222"),
        fontName="Helvetica-Bold",
        fontSize=11.5,
        leading=13,
        spaceBefore=7,
        spaceAfter=1,
    )
    centered_title = ParagraphStyle(
        "TitleCE",
        parent=normal,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=16,
        spaceAfter=3,
    )
    subtitle = ParagraphStyle("SubtitleCE", parent=normal, alignment=TA_CENTER, fontName="Helvetica-Bold", fontSize=10.2, leading=12, spaceAfter=10)
    right = ParagraphStyle("RightCE", parent=normal, alignment=TA_RIGHT)
    value_style = ParagraphStyle("ValueCE", parent=normal, alignment=TA_CENTER, fontName="Helvetica-Bold", fontSize=12.5, leading=14.5, textColor=brand_red)
    link_style = ParagraphStyle("LinkCE", parent=normal, textColor=brand_red)

    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=12 * mm,
        rightMargin=12 * mm,
        topMargin=1 * mm,
        bottomMargin=22 * mm,
    )

    def footer(canvas, document):
        canvas.saveState()
        canvas.setStrokeColor(brand_red)
        canvas.setLineWidth(0.6)
        canvas.line(17 * mm, 14 * mm, A4[0] - 17 * mm, 14 * mm)
        canvas.setFont("Helvetica", 8.5)
        canvas.setFillColor(colors.HexColor("#555555"))
        canvas.drawCentredString(
            A4[0] / 2,
            10 * mm,
            "Collision Engineers Ltd | www.CollisionEngineers.co.uk | engineers@collisionengineers.co.uk",
        )
        canvas.restoreState()

    story = []
    story.extend(_reportlab_header(context, normal, brand_red, Image, Paragraph, Table, TableStyle, mm))
    story.append(Paragraph(title.upper(), centered_title))
    subject = context["subject"]
    story.append(Paragraph(f"RE: {context['subject_display']} - Registration {subject['registration']}", subtitle))

    if template_name == "report.html.j2":
        story.extend(
            _reportlab_report_body(
                context,
                normal,
                small,
                table_text,
                table_small,
                header_cell,
                heading,
                right,
                value_style,
                brand_red,
                grid_grey,
                Paragraph,
                Spacer,
                HRFlowable,
                Table,
                TableStyle,
                colors,
                mm,
            )
        )
    else:
        story.extend(
            _reportlab_evidence_body(
                context,
                normal,
                table_text,
                header_cell,
                heading,
                link_style,
                brand_red,
                grid_grey,
                Paragraph,
                Spacer,
                HRFlowable,
                Table,
                TableStyle,
                colors,
                mm,
            )
        )

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return path.resolve()


def _reportlab_header(context, normal, brand_red, Image, Paragraph, Table, TableStyle, mm):
    logo = Image(str(LOGO_PATH), width=53 * mm, height=30.3 * mm)
    logo.hAlign = "LEFT"
    meta = context["meta"]
    ref_rows = [["Our Ref:", context["subject"]["registration"]]]
    if meta.get("your_ref"):
        ref_rows.append(["Your Ref:", meta["your_ref"]])
    ref_rows.append(["Date:", meta["report_date"]])
    ref_table = Table(
        [[Paragraph(f"<b>{label}</b>", normal), Paragraph(f"<b>{value}</b>", normal)] for label, value in ref_rows],
        colWidths=[25 * mm, 36 * mm],
    )
    ref_table.setStyle(
        TableStyle(
            [
                ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    header = Table([[logo, ref_table]], colWidths=[124 * mm, 61 * mm])
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (1, 0), (1, 0), 28),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 27),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("LEFTPADDING", (0, 0), (0, 0), 7 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return [header]


def _section_title(text, heading, Paragraph, Spacer, HRFlowable, mm, brand_red):
    return [
        Paragraph(text, heading),
        HRFlowable(width="100%", thickness=1.4, color=brand_red, spaceBefore=1, spaceAfter=5),
    ]


def _red_rule(Paragraph, Spacer, mm):
    return Spacer(1, 1.5 * mm)


def _table_commands(brand_red, colors):
    return [
        ("BACKGROUND", (0, 0), (-1, 0), brand_red),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D7D7D7")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F5F5")]),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
    ]


def _plain_table_commands(grid_grey, colors):
    return [
        ("GRID", (0, 0), (-1, -1), 0.4, grid_grey),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]


def _reportlab_report_body(
    context,
    normal,
    small,
    table_text,
    table_small,
    header_cell,
    heading,
    right,
    value_style,
    brand_red,
    grid_grey,
    Paragraph,
    Spacer,
    HRFlowable,
    Table,
    TableStyle,
    colors,
    mm,
):
    story = [Paragraph(context["intro"], normal)]
    story.extend(_section_title("SUBJECT VEHICLE DETAILS", heading, Paragraph, Spacer, HRFlowable, mm, brand_red))
    kv_data = []
    for row in context["subject_rows"]:
        kv_data.append(
            [
                Paragraph(row[0]["label"], table_text),
                Paragraph(row[0]["value"], table_text),
                Paragraph(row[1]["label"], table_text),
                Paragraph(row[1]["value"], table_text),
            ]
        )
    kv = Table(kv_data, colWidths=[30 * mm, 53 * mm, 35 * mm, 62 * mm], repeatRows=0)
    kv.setStyle(TableStyle(_plain_table_commands(grid_grey, colors)))
    story.append(kv)

    story.extend(_section_title("ASSESSED RETAIL MARKET VALUE", heading, Paragraph, Spacer, HRFlowable, mm, brand_red))
    val = Table(
        [[Paragraph("<b>Engineer's assessed retail value</b>", table_text), Paragraph(context["assessed_value"], value_style)]],
        colWidths=[90 * mm, 90 * mm],
    )
    val.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.4, grid_grey),
                ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#F2F2F2")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]
        )
    )
    story.append(val)

    story.extend(_section_title("MARKET RESEARCH", heading, Paragraph, Spacer, HRFlowable, mm, brand_red))
    story.append(Paragraph(context["market_research"], normal))
    data = [[Paragraph(label, header_cell) for label in ["No.", "Vehicle / Derivative", "Year", "Mileage", "Seller", "Asking Price", "Comment"]]]
    for idx, advert in enumerate(context["adverts"], start=1):
        data.append(
            [
                Paragraph(str(idx), table_text),
                Paragraph(advert["vehicle"], table_small),
                Paragraph(str(advert["registration_year_display"]), table_text),
                Paragraph(advert["mileage_display"], table_text),
                Paragraph(advert["seller_type"], table_small),
                Paragraph(advert["price"], table_text),
                Paragraph(advert["report_comment"], table_small),
            ]
        )
    table = Table(data, colWidths=[8 * mm, 45 * mm, 17 * mm, 22 * mm, 23 * mm, 23 * mm, 41 * mm], repeatRows=1)
    table.setStyle(
        TableStyle(
            _table_commands(brand_red, colors)
            + [
                ("GRID", (0, 0), (-1, -1), 0.4, grid_grey),
                ("ALIGN", (0, 1), (0, -1), "CENTER"),
                ("ALIGN", (5, 1), (5, -1), "RIGHT"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(table)

    story.extend(_section_title("VALUATION COMMENTARY", heading, Paragraph, Spacer, HRFlowable, mm, brand_red))
    for paragraph in context["valuation_commentary"]:
        story.append(Paragraph(paragraph, normal))
    if context.get("vat_note"):
        story.append(Paragraph(context["vat_note"], normal))
    story.extend(_section_title("CONCLUSION", heading, Paragraph, Spacer, HRFlowable, mm, brand_red))
    story.append(Paragraph(context["conclusion"], normal))
    return story


def _reportlab_evidence_body(
    context,
    normal,
    table_text,
    header_cell,
    heading,
    link_style,
    brand_red,
    grid_grey,
    Paragraph,
    Spacer,
    HRFlowable,
    Table,
    TableStyle,
    colors,
    mm,
):
    story = [Paragraph("Comparable advert references corresponding with the market valuation evidence report.", normal)]
    story.extend(_section_title("ADVERT REFERENCES", heading, Paragraph, Spacer, HRFlowable, mm, brand_red))
    data = [[Paragraph(label, header_cell) for label in ["No.", "Advert ID", "Vehicle / Derivative", "Year", "Mileage", "Price", "Link"]]]
    for idx, advert in enumerate(context["adverts"], start=1):
        link = f"<link href='{advert['url']}' color='#0057B8'><u>Open advert</u></link>"
        data.append(
            [
                Paragraph(str(idx), table_text),
                Paragraph(advert.get("advert_id") or "Not stated", table_text),
                Paragraph(advert["vehicle"], table_text),
                Paragraph(str(advert["registration_year_display"]), table_text),
                Paragraph(advert["mileage_display"], table_text),
                Paragraph(advert["price"], table_text),
                Paragraph(link, link_style),
            ]
        )
    table = Table(data, colWidths=[8 * mm, 31 * mm, 56 * mm, 15 * mm, 21 * mm, 20 * mm, 28 * mm], repeatRows=1)
    table.setStyle(
        TableStyle(
            _table_commands(brand_red, colors)
            + [
                ("GRID", (0, 0), (-1, -1), 0.4, grid_grey),
                ("ALIGN", (0, 1), (0, -1), "CENTER"),
                ("ALIGN", (5, 1), (5, -1), "RIGHT"),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(table)

    story.extend(_section_title("SEARCH SUMMARY", heading, Paragraph, Spacer, HRFlowable, mm, brand_red))
    story.append(Paragraph(context["search_summary"], normal))
    story.append(Paragraph("The advert numbering above mirrors the numbering used in the valuation evidence report.", normal))
    return story


def capture_advert_page(url: str, tmp_dir: str) -> str:
    """Capture a web page to PDF using Playwright with stealth. Returns temp file path."""
    import uuid

    try:
        from playwright.sync_api import sync_playwright
        from playwright_stealth import Stealth
    except ModuleNotFoundError as exc:
        raise SystemExit(
            f"Missing Python dependency: {exc.name}. Install with: "
            "python -m pip install playwright playwright-stealth && playwright install chromium"
        ) from exc

    tmp_path = Path(tmp_dir) / f"capture_{uuid.uuid4().hex}.pdf"
    with Stealth().use_sync(sync_playwright()) as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": DESKTOP_CAPTURE_WIDTH, "height": DESKTOP_CAPTURE_VIEWPORT_HEIGHT},
            screen={"width": DESKTOP_CAPTURE_WIDTH, "height": DESKTOP_CAPTURE_VIEWPORT_HEIGHT},
            device_scale_factor=1,
            is_mobile=False,
            has_touch=False,
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
        )
        page = context.new_page()
        page.goto(url, wait_until="networkidle", timeout=30000)
        dismiss_autotrader_cookie_banner(page)
        _prepare_desktop_pdf_capture(page)
        dismiss_autotrader_cookie_banner(page)
        _assert_autotrader_cookie_banner_cleared(page, url)
        page_size = _desktop_pdf_page_size(page)
        page.pdf(
            path=str(tmp_path),
            width=f"{page_size['width']}px",
            height=f"{page_size['height']}px",
            margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"},
            print_background=True,
            prefer_css_page_size=False,
        )
        _assert_pdf_not_cookie_blocked(tmp_path, url)
        browser.close()
    return str(tmp_path)


def _prepare_desktop_pdf_capture(page: Any) -> None:
    """Keep Autotrader in desktop screen layout and load lazy sections before printing."""

    page.emulate_media(media="screen")
    _scroll_page_to_load_lazy_content(page)
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(500)


def _scroll_page_to_load_lazy_content(page: Any, max_steps: int = 8) -> None:
    scroll_step = DESKTOP_CAPTURE_VIEWPORT_HEIGHT
    last_height = 0
    for _ in range(2):
        height = _document_scroll_height(page)
        y_position = 0
        steps = 0
        while y_position < height and steps < max_steps:
            page.evaluate("(y) => window.scrollTo(0, y)", y_position)
            page.wait_for_timeout(300)
            y_position += scroll_step
            steps += 1

        page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)")
        page.wait_for_timeout(800)
        new_height = _document_scroll_height(page)
        if abs(new_height - height) < 50 and abs(new_height - last_height) < 50:
            break
        last_height = new_height


def _desktop_pdf_page_size(page: Any) -> dict[str, int]:
    width = max(DESKTOP_CAPTURE_WIDTH, int(page.evaluate("window.innerWidth")))
    height = max(
        DESKTOP_CAPTURE_VIEWPORT_HEIGHT,
        _document_scroll_height(page) + PDF_HEIGHT_BUFFER_PX,
    )
    return {"width": width, "height": height}


def _document_scroll_height(page: Any) -> int:
    return int(page.evaluate(
        "Math.ceil(Math.max(document.body.scrollHeight, document.documentElement.scrollHeight))"
    ))


def dismiss_autotrader_cookie_banner(page: Any, timeout_ms: int = 7000) -> bool:
    """Dismiss the Autotrader CMP iframe when it appears before PDF capture."""

    deadline = time.monotonic() + (timeout_ms / 1000)
    while time.monotonic() < deadline:
        saw_banner = False
        for frame in list(page.frames):
            try:
                if not _frame_has_visible_cookie_banner(frame):
                    continue

                saw_banner = True
                for pattern in COOKIE_DISMISS_BUTTON_PATTERNS:
                    if _click_cookie_choice(frame, pattern):
                        _wait_after_cookie_choice(page)
                        if not autotrader_cookie_banner_visible(page):
                            return True
                        break
            except Exception:
                continue

        if not saw_banner:
            return False

        page.wait_for_timeout(250)
    return False


def _click_cookie_choice(frame: Any, button_pattern: str) -> bool:
    if not _is_autotrader_cookie_frame(frame):
        return False

    button = frame.get_by_role("button", name=re.compile(button_pattern, re.IGNORECASE)).first
    if not button.is_visible(timeout=500):
        return False

    button.click(timeout=3000)
    return True


def autotrader_cookie_banner_visible(page: Any) -> bool:
    return any(_frame_has_visible_cookie_banner(frame) for frame in list(page.frames))


def _frame_has_visible_cookie_banner(frame: Any) -> bool:
    if not _is_autotrader_cookie_frame(frame):
        return False

    try:
        heading = frame.get_by_text("We use cookies on our site", exact=True).first
        if heading.is_visible(timeout=500):
            return True
    except Exception:
        pass

    for pattern in COOKIE_DISMISS_BUTTON_PATTERNS:
        try:
            button = frame.get_by_role("button", name=re.compile(pattern, re.IGNORECASE)).first
            if button.is_visible(timeout=500):
                return True
        except Exception:
            continue
    return False


def _is_autotrader_cookie_frame(frame: Any) -> bool:
    if "cmpv2.autotrader.co.uk" in frame.url:
        return True
    try:
        return frame.get_by_text("We use cookies on our site", exact=True).count() > 0
    except Exception:
        return False


def _wait_after_cookie_choice(page: Any) -> None:
    try:
        page.wait_for_load_state("networkidle", timeout=5000)
    except Exception:
        page.wait_for_timeout(1000)


def _assert_autotrader_cookie_banner_cleared(page: Any, url: str) -> None:
    if autotrader_cookie_banner_visible(page):
        raise CookieBannerNotDismissedError(
            f"Autotrader cookie banner is still visible before PDF capture: {url}"
        )


def _assert_pdf_not_cookie_blocked(path: Path, url: str) -> None:
    from pypdf import PdfReader

    text = "\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages)
    if any(marker in text for marker in COOKIE_BLOCKED_TEXT_MARKERS):
        path.unlink(missing_ok=True)
        raise CookieBannerNotDismissedError(
            f"Autotrader cookie banner text was captured in the PDF: {url}"
        )


def merge_pdfs(pdf_paths: list[str], output_path: str) -> None:
    """Merge an ordered list of PDF files into a single output PDF."""
    from pypdf import PdfWriter

    writer = PdfWriter()
    for path in pdf_paths:
        writer.append(str(path))
    with open(output_path, "wb") as f:
        writer.write(f)
