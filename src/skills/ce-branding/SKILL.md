---
name: ce-branding
description: Use whenever producing a Collision Engineers branded document - valuation report, evidence pack, fee note, invoice, diminution rebuttal, roadworthy certificate, addendum report, or any client/court-facing output. Provides the canonical CE logo, document layout templates, and house-style/typography spec so every document looks consistent. Other document-producing skills (vehicle-valuation, rebuttal, roadworthy, total-loss, finance fee-note) consume this skill for branding and layout.
---

# CE Branding

The shared Collision Engineers brand + document-layout skill. It is the single source of truth for logo, page layout, and house style, consumed by the document-producing skills so branding is defined once.

## Assets

- **Logo:** `assets/logo.pdf` (vector), plus `../vehicle-valuation/assets/brand/logo.png` and `logo.svg` (to be consolidated here).
- **Example outputs** (reference for layout fidelity): `assets/feenoteexample.pdf`, `assets/addendumreportexample.pdf`, `assets/totallossexample.pdf`.
- **Layout templates** (currently in `../vehicle-valuation/assets/templates/`, to consolidate here): `_base.html.j2`, `report.html.j2`, `evidence_pack.html.j2`, `styles.css`.
- **Specs:** `../vehicle-valuation/references/pdf-template-spec.md` (PDF layout/typography), `../vehicle-valuation/references/brand.md` (brand).

## House style (summary)

A4 portrait, ~2cm margins; logo top-left; refs/date top-right (header on every page); red rule under uppercase bold section headings; centred footer (website + address) in grey. Plain-spoken engineer register, not AI-hedged or lawyer-speak. (Full rules in `pdf-template-spec.md` + the CE communication style profile in `../ce-style/`.)

## Usage

Document-producing skills reference this skill for: the logo, the base layout/templates, and the typography/house-style spec. Keep brand/layout changes here; do not re-define them per skill.

## Status

Migrated brand assets present (logos + example PDFs). Consolidation of the shared templates from `vehicle-valuation` into this skill is a planned follow-up (see `src/skills/README.md` and `docs/plans/agent-skills/`). Branding/layout is `assist` class; the documents it styles are governed by their owning (often expert-class) skill.
