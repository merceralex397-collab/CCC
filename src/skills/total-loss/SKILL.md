---
name: total-loss
description: Generate an Audatex/EVA-compatible vehicle damage-assessment PDF from photo-based damage analysis - routing-aware Labour / Paint / Parts / Extras with ABP-aligned rates, cost-targeting (clear total loss vs conservative vs target-bounded), and SRS/airbag and specialist checks. Use for total-loss and damage-assessment estimates destined for EVA/Audatex. Expert class - an AI-assisted draft until a named human signs off.
---

# Total Loss (Audatex/EVA damage assessment)

Produces an EVA/Audatex-compatible damage-assessment PDF from vehicle photos + an engineer brief.

## How this skill is defined

- `context.md` — the working handover: labour-rate matrix, material-rate scale, ABP extras package, EVA routing rules (operation type → PDF section → EVA classification → engineer's-report visibility), cost-targeting guidance, critical mistakes to avoid, tone.
- `tool.py.md` — the Audatex generator (routing rules, coordinates, pagination, totals).
- `references/authoritative-sources.md` — the shared references this skill now cites.
- `references/examples.md` — worked examples in the governed case corpus.

## Authoritative sources

ABP charges are maintained in the **`abp-rates`** skill (canonical). The estimating doctrine (failure modes, repair-vs-replace, completeness walkthrough) is shared with **`repair-estimate`** via `repair-estimate/references/estimate-framework.md`. Paint time/material comes from **`paint-calculation`**. Where the assessment touches the scrap/repairable boundary, cross-refer **`salvage-categorisation`** (the ABI category is a separate determination from cost). See `references/authoritative-sources.md`.

## Governance

Expert class — AI-assisted draft until a named human signs off; no autonomous external send. Branding via `ce-branding`.
