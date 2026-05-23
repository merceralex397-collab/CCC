from __future__ import annotations

from pathlib import Path

from ccc_parser.core import ParserCore


class ParserUiController:
    def __init__(self, core: ParserCore | None = None) -> None:
        self.core = core or ParserCore()

    def parse_file(self, path: Path):
        return self.core.parse(path)


def main() -> int:
    import tkinter as tk
    from tkinter import filedialog, messagebox, scrolledtext

    controller = ParserUiController()
    root = tk.Tk()
    root.title("Collision Command Centre Parser")
    root.geometry("980x640")

    output = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    output.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

    def open_file() -> None:
        selected = filedialog.askopenfilename(
            title="Select instruction file",
            filetypes=[
                ("Supported documents", "*.pdf *.docx *.doc *.msg *.eml *.txt *.md *.json"),
                ("All files", "*.*"),
            ],
        )
        if not selected:
            return
        try:
            result = controller.parse_file(Path(selected)).to_dict()
        except Exception as exc:
            messagebox.showerror("Parse failed", str(exc))
            return
        output.delete("1.0", tk.END)
        output.insert(tk.END, str(result))

    toolbar = tk.Frame(root)
    toolbar.pack(fill=tk.X, padx=12, pady=(12, 0))
    tk.Button(toolbar, text="Import instruction", command=open_file).pack(side=tk.LEFT)
    tk.Label(toolbar, text="Scaffold UI: review/edit/export screens will be built over the shared parser core.").pack(
        side=tk.LEFT, padx=12
    )

    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
