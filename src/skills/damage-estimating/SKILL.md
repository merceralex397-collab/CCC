---
name: damage-estimating
description: Use for UK collision damage estimating work: standalone repair estimates, EVA/Audatex total-loss damage assessments, AZT paint costing, ABP charge review, and estimate challenge support. Modes: repair-estimate, eva-total-loss, paint-costing, charge-review. Expert modes produce AI-assisted drafts until named-human sign-off; paint and charge-review modes are assistive inputs.
---

# Damage Estimating

Single dispatcher for repair-cost logic: repair estimates, EVA/Audatex total-loss damage assessments, paint costing, and ABP charge review.

## Modes

| Mode | Use for | Load |
| --- | --- | --- |
| `repair-estimate` | Standalone desktop estimate from vehicle details and damage photos. | `references/repair-estimate.md`, `references/estimate-framework.md`, `references/examples.md` |
| `eva-total-loss` | EVA/Audatex-compatible damage-assessment or total-loss PDF. | `references/eva-total-loss.md`, `references/estimate-framework.md`, `references/examples.md` |
| `paint-costing` | AZT paint time/material calculation for panels, blends, substrates, and surcharges. | `references/paint-costing.md` |
| `charge-review` | ABP rate and extra-charge sanity review for a repair estimate. | `references/charge-review.md` |

## Shared References

- ABP rates: `src/skills/abp-rates/references/abp-2026-rates.md`.
- AZT paint method: `references/azt-paint-method.md`.
- OEM constraints: `src/skills/manufacturer-standards/references/oem-index.md`.
- Domain terms: `src/skills/ce-domain-glossary/references/`.
- House style: `src/skills/ce-house-style/`.
- Salvage category decisions: `src/skills/salvage-categorisation/` when categorisation or notification obligations are in scope.

## Required Inputs

- Vehicle registration, make/model, derivative where relevant, mileage if available, and damage location.
- Clear damage photos or source estimate/Audatex PDF.
- Required output mode and intended audience.
- Any instruction constraints, target system requirements, or known total-loss/salvage context.

## Governance

`repair-estimate` and `eva-total-loss` are expert outputs and remain AI-assisted drafts until a named engineer signs off. `paint-costing` and `charge-review` are assistive calculations only. No autonomous external send.

## Validation

Run repository verification after skill changes:

```powershell
python tools/verify_scaffold.py
```

When rendering a valuation-linked evidence pack, also run `python tools/vehicle-valuation/validate_evidence_pack.py payload.json`.
