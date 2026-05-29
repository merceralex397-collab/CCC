# Repair Estimate Mode

Use this mode for a standalone desktop estimate that is not specifically an EVA/Audatex total-loss PDF.

## Workflow

1. Establish vehicle identity, side, impact location, and visible damage scope.
2. Walk `estimate-framework.md`: visible damage, inferred impact-path damage, co-located fragile items, repair-vs-replace decisions, labour, parts, paint, extras, and completeness checks.
3. Price labour and extras from `src/skills/abp-rates/references/abp-2026-rates.md`.
4. Calculate paint through `paint-costing` mode.
5. Apply OEM constraints from `src/skills/manufacturer-standards/references/oem-index.md`.
6. Output parts, labour, paint, extras, VAT treatment, assumptions, exclusions, and required human review points.

## Output

Produce a structured estimate. If a branded document is needed, load `src/skills/ce-house-style/` in `visual-layout` mode.
