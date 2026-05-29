---
name: salvage-categorisation
description: Determine the ABI salvage category (A / B / S / N) for a damaged vehicle using the ABI Code of Practice, with a reasoned justification and the regulatory notification obligations (MIAFTR, V5C/DVLA, Certificate of Destruction). Use when assessing whether a vehicle is scrap, break, repairable-structural, or repairable-non-structural, including EV high-voltage battery cases and water/fire damage. Expert class - the output is an AI-assisted draft until a named, appropriately qualified person signs off.
---

# Salvage Categorisation

Applies the ABI Code of Practice to recommend a salvage category (A/B/S/N) with a defensible justification and the notification steps that follow.

## Reference

- `references/abi-salvage-cop.md` — distilled decision reference (categories, 4-question framework, definitions, structural vs non-structural, EV HV-battery rules §8, water/fire §13, disposal §14, MIAFTR / V5C / V860 / retention).
- `references/abi-salvage-cop.pdf` — the authoritative source (version-sensitive; 28.05.2025).
- Vocabulary: `ce-domain-glossary`. Cost context (a separate insurer decision): `abp-rates`, `repair-estimate`/`total-loss`.

## Workflow

1. Gather inputs: damage description / structural assessment, parts-reuse view, EV/battery status, water/fire flags.
2. Walk the four-question framework (scope → repairable → reuse → structural, including structural HV battery).
3. Recommend the category with a clause-level justification grounded in the COP.
4. Produce the notification checklist (MIAFTR within 2 working days; V5C handling per category — destroyed for A & B; RSV rules; V860 where applicable; 6-year retention).

## Governance

Expert class. Categorisation must be by an **Appropriately Qualified Person (AQP)**; the skill output is an **AI-assisted draft** until a named human signs off. No autonomous external notification. The ABI category turns on repairability / structural damage / reuse, **not** a repair-cost-vs-value ratio (that is a separate insurer commercial decision).
