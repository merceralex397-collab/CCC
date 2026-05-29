# Option paper: OEM standards UK applicability

Date: 2026-05-29
Status: open
Group: agent-skills

## Problem

The `manufacturer-standards` skill is seeded with two OEM position statements — Volkswagen of America (wheel repair) and Volvo Car USA (wheels & tyres). Both are **US-market** documents. Their engineering intent (reconditioned wheels not approved; cosmetic refinishing only; genuine parts; follow OEM procedures via erWin/ElsaPro/VIDA) is widely applicable, but they are not authoritative for UK matters as-is.

## Risk

Citing a US position statement in a UK expert document (estimate, roadworthy certificate, rebuttal) could be challenged on jurisdiction/market grounds.

## Options

1. **Seed-now, verify-before-use (recommended).** Keep VW/Volvo as illustrative seeds with a clear `market: US` flag in `oem-index.md` and a caveat in `SKILL.md`; require a UK OEM equivalent or technical bulletin to be sourced before a statement is relied upon in a UK matter.
2. Remove the US seeds until UK equivalents are obtained (loses the illustrative library now).
3. Treat them as universal (not recommended — jurisdiction risk).

## Recommendation

Option 1 (implemented). Next: source UK/EU OEM equivalents (VW UK / Volvo Cars technical positions, Thatcham guidance where relevant) and add them with `market: UK/EU`. Until then, where an estimate forces replace-not-refurbish on the basis of an OEM statement, note the statement's market.

## Owner / next step

Unassigned. Action: gather UK OEM wheel/tyre and genuine-parts positions; expand `oem-index.md`.
