# HS Roadworthy Report — Generation Instructions

## CRITICAL OPERATING RULES — read first

1. **Do not ask clarifying questions.** Generate the report from the engineer's report alone. The user wants the file produced, not a conversation about it.
2. **Only the 14 highlighted fields change.** Nothing else in the template is ever modified — not the wording, not the engineer's name, not the qualifications, not the paragraphs, not the footer, not the fonts, not the highlighting.
3. **Our Ref is always the vehicle registration number.** No exceptions, no other formats, no asking.
4. **If a field's source value isn't in the engineer's report, use the fallback in the table below** — do not stop and ask.
5. **Work on a copy.** Never edit `HS_roadworthy_report_template.docx` itself.

---

## The 14 fields — fill these and only these

| # | HS template field | Value to insert | Fallback if not in engineer's report |
|---|---|---|---|
| 1 | Our Ref (header) | Vehicle registration number | — (registration is always present) |
| 2 | Your Ref (header) | Engineer's "Your Ref" value | Leave the existing template value |
| 3 | Date (header) | Today's date, `DD/MM/YYYY` | — |
| 4 | RE: line — accident date | Date of road traffic accident | Use today's date |
| 5 | RE: line — registration | Vehicle registration | — |
| 6 | "instructions received on" date (body) | Today's date, `DD/MM/YYYY` | — |
| 7 | Make (table) | Make, capitalised normally (e.g. "Toyota" not "TOYOTA") | — |
| 8 | Registration (table) | Vehicle registration | — |
| 9 | Model (table) | Model — short form only (e.g. "Corolla", not "Corolla Icon VVT-I"; "Astra" not "Astra SRi 1.4T") | — |
| 10 | VIN (table) | VIN | "TBC" |
| 11 | Status (table) | **Always "Repaired"** | — |
| 12 | Cat S (table) | "Yes" only if the engineer's report records the vehicle as a total loss Category S. Every other case — Cat N, Cat A, Cat B, "Repair", blank, Salvage, anything else — is "No". | "No" |
| 13 | Passed MOT (taxi) (table) | **Always "TBC"** | — |
| 14 | Legal Status (table) | **Always "Roadworthy"** | — |

Plus one inline edit in the body paragraph that begins *"We understand the vehicle has been previously sustained damage to the ___"*:

| Field | Value | Fallback |
|---|---|---|
| Damage location word(s) | Directional words from engineer's "Nature of incident" — e.g. "left hand rear", "nearside front", "offside", "rear" | Use "rear" |

That paragraph is part of the body, not the table. The yellow-highlighted word(s) replace whatever directional placeholder is currently there.

---

## Process

1. Read `/mnt/skills/public/docx/SKILL.md` first for the docx unpack/edit/pack workflow.
2. Copy `HS_roadworthy_report_template.docx` to the working directory.
3. Unpack: `python /mnt/skills/public/docx/scripts/office/unpack.py template.docx unpacked/`
4. Read the engineer's report (PDF or docx) and extract the values.
5. Edit two XML files only:
   - `unpacked/word/header1.xml` — Our Ref, Your Ref, Date
   - `unpacked/word/document.xml` — everything else
6. **Header date special case**: the date is split across six separate `<w:r>` runs (e.g. "20", "/", "0", "4", "/202", "6"). Replace the text in the **first** run with the full new date (e.g. "08/05/2026") and **delete the other five `<w:r>...</w:r>` blocks entirely**.
7. Pack: `python /mnt/skills/public/docx/scripts/office/pack.py unpacked/ output.docx --original template.docx` — this validates automatically.
8. Save to `/mnt/user-data/outputs/HS_roadworthy_<REGISTRATION>.docx` and present.
9. Tell the user the report is ready and they need to drag images in manually. **Keep the message short — do not list every field that was filled in.**

---

## Worked example (Toyota YC19JDY)

Engineer's report contained: Your Ref `225763.TA`, accident date `02/04/2026`, Registration `YC19JDY`, Make `TOYOTA`, Model `COROLLA ICON VVT-I`, VIN `SB1Z93BE40E055307`, Status "Repair", Nature of incident "moderate collision/impact damage to the left hand rear".

Resulting HS report fields:

- Our Ref: `YC19JDY` · Your Ref: `225763.TA` · Date: today's date
- RE: line: `02/04/2026 YC19JDY`
- "instructions received on": today's date
- Make: `Toyota` · Registration: `YC19JDY` · Model: `Corolla` · VIN: `SB1Z93BE40E055307`
- Status: `Repaired` · Cat S: `No` · Passed MOT (taxi): `TBC` · Legal Status: `Roadworthy`
- Damage location word: `left hand rear`