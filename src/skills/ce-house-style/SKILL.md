---
name: ce-house-style
description: Use whenever a Collision Engineers output needs house visual layout or writing tone. Modes: visual-layout for logo, typography, page headers, footers, PDF/docx templates and brand assets; writing-tone for plain engineer register, CE communication style, concise client/court wording and anti-AI phrasing checks. Consumed by valuation, damage-estimating, rebuttal, roadworthy, finance-document, fee-note, and invoice drafts.
---

# CE House Style

Shared Collision Engineers house style. Load this support skill only when document layout or tone decisions are needed.

## Modes

| Mode | Use when | Load |
| --- | --- | --- |
| `visual-layout` | Building or checking a branded PDF, docx, report, evidence pack, fee note, or invoice. | `references/visual-layout.md` and `assets/` |
| `writing-tone` | Drafting or revising client, court, engineer, invoice, rebuttal, valuation, or status wording. | `references/writing-tone.md` |

## Governance

Assist/reference class. This skill does not approve expert findings or external sends. The calling skill owns sign-off: valuation, roadworthy, rebuttal, salvage, and damage-estimating expert outputs remain AI-assisted drafts until a named human signs off.

## Validation

For repository changes, run:

```powershell
python tools/verify_scaffold.py
```

For generated branded documents, compare against the relevant worked examples in `docs/reference/case-corpus/` and `src/skills/ce-house-style/assets/`.
