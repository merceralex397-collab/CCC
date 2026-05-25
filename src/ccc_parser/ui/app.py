from __future__ import annotations

import json
import re
from pathlib import Path
from tkinter import filedialog, messagebox

from ccc_parser.constants import FIELD_KEYS, FIELD_LABELS
from ccc_parser.core import ParserCore
from ccc_parser.exporters.eva import export_eva_payload
from ccc_parser.packaging import build_evidence_package_manifest
from ccc_parser.review import apply_field_overrides

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD

    HAS_DND = True
except Exception:  # pragma: no cover - depends on optional desktop package availability
    DND_FILES = None
    TkinterDnD = None
    HAS_DND = False


class ParserUiController:
    def __init__(self, core: ParserCore | None = None) -> None:
        self.core = core or ParserCore()

    def parse_file(self, path: Path):
        return self.core.parse(path)

    def apply_overrides(self, result, overrides: dict[str, str]):
        return apply_field_overrides(result, overrides)

    def eva_payload(self, result, *, allow_blockers: bool = False):
        return export_eva_payload(result, allow_blockers=allow_blockers)

    def package_manifest(self, result):
        return build_evidence_package_manifest(result)


def parse_drop_paths(raw: str, splitter=None) -> list[Path]:
    raw = (raw or "").strip()
    if not raw:
        return []
    if splitter is not None:
        try:
            return [Path(item) for item in splitter(raw) if str(item).strip()]
        except Exception:
            pass
    parts = [match.group(1) or match.group(2) for match in re.finditer(r"\{([^}]*)\}|(\S+)", raw)]
    return [Path(part.strip()) for part in parts if part and part.strip()]


def main() -> int:
    import tkinter as tk
    from tkinter import scrolledtext, ttk

    controller = ParserUiController()
    current_result = {"value": None}

    root = TkinterDnD.Tk() if HAS_DND and TkinterDnD is not None else tk.Tk()
    root.title("Collision Command Centre Parser")
    root.geometry("1180x760")

    toolbar = ttk.Frame(root, padding=8)
    toolbar.pack(fill=tk.X)

    status_var = tk.StringVar(
        value="Import or drop an instruction, email, document, image pack, or batch source."
        if HAS_DND
        else "Import an instruction, email, document, image pack, or batch source."
    )
    provider_var = tk.StringVar(value="Provider: -")
    validation_var = tk.StringVar(value="Validation: -")
    field_vars: dict[str, tk.StringVar] = {key: tk.StringVar(value="") for key in FIELD_KEYS if key != "inspection_address"}

    ttk.Label(toolbar, textvariable=status_var).pack(side=tk.LEFT, fill=tk.X, expand=True)

    body = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
    body.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 8))

    left = ttk.Frame(body, padding=8)
    right = ttk.Frame(body, padding=8)
    body.add(left, weight=2)
    body.add(right, weight=3)

    header = ttk.Frame(left)
    header.pack(fill=tk.X, pady=(0, 8))
    ttk.Label(header, textvariable=provider_var).pack(anchor=tk.W)
    ttk.Label(header, textvariable=validation_var).pack(anchor=tk.W)

    fields_frame = ttk.Frame(left)
    fields_frame.pack(fill=tk.BOTH, expand=True)

    text_widgets: dict[str, tk.Text] = {}
    row = 0
    for field_name in FIELD_KEYS:
        ttk.Label(fields_frame, text=FIELD_LABELS[field_name]).grid(row=row, column=0, sticky=tk.NW, pady=3, padx=(0, 8))
        if field_name in {"inspection_address", "accident_circumstances"}:
            height = 5 if field_name == "inspection_address" else 4
            widget = tk.Text(fields_frame, height=height, width=48, wrap=tk.WORD)
            widget.grid(row=row, column=1, sticky=tk.EW, pady=3)
            text_widgets[field_name] = widget
        else:
            ttk.Entry(fields_frame, textvariable=field_vars[field_name], width=52).grid(
                row=row, column=1, sticky=tk.EW, pady=3
            )
        row += 1
    fields_frame.columnconfigure(1, weight=1)

    warnings_box = scrolledtext.ScrolledText(right, height=12, wrap=tk.WORD)
    warnings_box.pack(fill=tk.X, expand=False)
    preview_box = scrolledtext.ScrolledText(right, wrap=tk.WORD)
    preview_box.pack(fill=tk.BOTH, expand=True, pady=(8, 0))

    def set_text(widget: tk.Text, value: str) -> None:
        widget.delete("1.0", tk.END)
        widget.insert(tk.END, value or "")

    def refresh(result) -> None:
        current_result["value"] = result
        provider_var.set(f"Provider: {result.detected_provider or 'Unknown / Unmapped'}")
        validation_var.set(
            f"Validation: {len(result.validation.blockers)} blocker(s), {len(result.validation.warnings)} warning(s)"
        )
        for field_name in FIELD_KEYS:
            value = (result.fields.get(field_name).normalized_value if result.fields.get(field_name) else "") or ""
            if field_name in text_widgets:
                set_text(text_widgets[field_name], value)
            else:
                field_vars[field_name].set(value)
        warnings_box.delete("1.0", tk.END)
        for issue in result.validation.blockers:
            warnings_box.insert(tk.END, f"BLOCKER {issue.code}: {issue.message}\n")
        for issue in result.validation.warnings:
            warnings_box.insert(tk.END, f"WARNING {issue.code}: {issue.message}\n")
        for warning in result.warnings:
            warnings_box.insert(tk.END, f"{warning.severity.upper()} {warning.code}: {warning.message}\n")
        preview_box.delete("1.0", tk.END)
        preview_box.insert(tk.END, json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
        status_var.set(f"Parsed {result.source_path}")

    def collect_overrides() -> dict[str, str]:
        overrides: dict[str, str] = {}
        for field_name in FIELD_KEYS:
            if field_name in text_widgets:
                overrides[field_name] = text_widgets[field_name].get("1.0", tk.END).strip()
            else:
                overrides[field_name] = field_vars[field_name].get().strip()
        return overrides

    def parse_paths(paths: list[Path]) -> None:
        if not paths:
            return
        selected = paths[0]
        try:
            refresh(controller.parse_file(selected))
            if len(paths) > 1:
                status_var.set(f"Parsed {selected}. Dropped {len(paths)} paths; use a folder for a full batch parse.")
        except Exception as exc:
            messagebox.showerror("Parse failed", str(exc))

    def import_file() -> None:
        selected = filedialog.askopenfilename(
            title="Select instruction or evidence file",
            filetypes=[
                ("Supported files", "*.pdf *.docx *.doc *.msg *.eml *.txt *.md *.json *.jpg *.jpeg *.png *.tif *.tiff"),
                ("All files", "*.*"),
            ],
        )
        if not selected:
            return
        parse_paths([Path(selected)])

    def on_drop(event) -> None:
        parse_paths(parse_drop_paths(getattr(event, "data", ""), splitter=root.tk.splitlist))

    def register_drop_targets() -> None:
        if not HAS_DND or DND_FILES is None:
            return
        widgets = [root, toolbar, body, left, right, warnings_box, preview_box]
        seen: set[str] = set()
        for widget in widgets:
            widget_id = str(widget)
            if widget_id in seen:
                continue
            seen.add(widget_id)
            try:
                widget.drop_target_register(DND_FILES)
                widget.dnd_bind("<<Drop>>", on_drop)
            except Exception:
                continue

    def apply_review() -> None:
        result = current_result["value"]
        if result is None:
            return
        refresh(controller.apply_overrides(result, collect_overrides()))
        status_var.set("Manual review applied.")

    def save_result() -> None:
        result = current_result["value"]
        if result is None:
            return
        target = filedialog.asksaveasfilename(title="Save parser result", defaultextension=".json")
        if target:
            Path(target).write_text(json.dumps(result.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def save_eva() -> None:
        result = current_result["value"]
        if result is None:
            return
        allow = bool(result.validation.blockers) and messagebox.askyesno(
            "Export with blockers?", "Validation blockers remain. Export a review copy anyway?"
        )
        try:
            payload = controller.eva_payload(result, allow_blockers=allow)
        except ValueError as exc:
            messagebox.showerror("Export blocked", str(exc))
            return
        target = filedialog.asksaveasfilename(title="Save EVA JSON", defaultextension=".json")
        if target:
            Path(target).write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def save_package() -> None:
        result = current_result["value"]
        if result is None:
            return
        target = filedialog.asksaveasfilename(title="Save evidence package manifest", defaultextension=".json")
        if target:
            Path(target).write_text(
                json.dumps(controller.package_manifest(result), indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

    ttk.Button(toolbar, text="Import", command=import_file).pack(side=tk.RIGHT, padx=(6, 0))
    ttk.Button(toolbar, text="Apply Review", command=apply_review).pack(side=tk.RIGHT, padx=(6, 0))
    ttk.Button(toolbar, text="Save Result", command=save_result).pack(side=tk.RIGHT, padx=(6, 0))
    ttk.Button(toolbar, text="Export EVA", command=save_eva).pack(side=tk.RIGHT, padx=(6, 0))
    ttk.Button(toolbar, text="Package", command=save_package).pack(side=tk.RIGHT, padx=(6, 0))

    register_drop_targets()

    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
