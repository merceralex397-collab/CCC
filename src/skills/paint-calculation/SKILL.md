---
name: paint-calculation
description: Compute paint time and material cost for collision repair using the AZT (Allianz) paint-calculation method - paint systems (1-4 coat, solid/metallic/multi-effect), metal vs plastic substrate stages, preparation/masking, scratch-resistant clearcoat surcharges, 2-colour work, and multi-panel blend propagation. Use when an estimate needs defensible paint hours and material figures, especially for multi-panel or metallic/pearl blends. A costing aid consumed by repair-estimate and total-loss; its figures are drafts the calling skill signs off.
---

# Paint Calculation (costing aid)

Produces defensible paint **time** and **material** figures for a repair by applying the AZT method, so paint lines in an estimate are methodical rather than guessed.

## References

- `references/azt-paint-method.md` — the distilled AZT method (systems, substrate stages, prep, surcharges, blend rules, how-to).
- `references/atzpaintcalculation.pdf` — the authoritative source.
- Material-cost anchors: cite the `abp-rates` skill (`abp-2026-rates.md`) for £ figures.

## Workflow

1. Identify each panel to be painted, its substrate (metal vs plastic), and its paint system (solid / metallic / multi-effect / 3-4 coat).
2. Determine the painting process (on-vehicle, on-vehicle with pre-painting, or dismounted).
3. Apply multi-panel **blend** propagation (e.g. rear quarter blends into rear door / C-pillar / sometimes roof) per the method.
4. Add surcharges (scratch-resistant clearcoat: +0.3h per horizontal panel / +0.1h per vertical panel; 2-colour work where applicable).
5. Output paint hours + material cost + the blend-panel list, showing the method steps.

## Output and governance

Assist class. Outputs are a **draft** input to `repair-estimate` / `total-loss`; the calling expert skill validates and a named human signs off the final document. Do not present paint figures as a standalone client output.
