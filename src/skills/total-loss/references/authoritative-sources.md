# Total Loss — authoritative sources

This skill's charges and doctrine are now maintained in shared reference skills rather than re-embedded. The inline rate matrix in `../context.md` is retained as a working copy, but the canonical source is `abp-rates`.

| Need | Canonical source |
| --- | --- |
| Labour rates, repair-plan fee, ADAS, EV/hybrid, specialist/admin charges, regional uplift | `abp-rates` → `references/abp-2026-rates.md` |
| Estimating doctrine: failure modes, repair-vs-replace, impact-path propagation, completeness walkthrough | `repair-estimate` → `references/estimate-framework.md` |
| Paint time + material (AZT method, blends, surcharges) | `paint-calculation` → `references/azt-paint-method.md` |
| Scrap / repairable category (A/B/S/N), MIAFTR/V5C | `salvage-categorisation` → `references/abi-salvage-cop.md` |
| Domain vocabulary (Audatex/ABP/BS 10125 terms) | `ce-domain-glossary` |

When an ABP figure in `context.md` and `abp-rates` disagree, **`abp-rates` wins** (it is the version-managed source).
