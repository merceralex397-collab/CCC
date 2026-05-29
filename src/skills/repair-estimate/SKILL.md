---
name: repair-estimate
description: Produce a standalone desktop vehicle repair estimate from damage photographs and vehicle details - parts, labour, paint and extras - independent of the Audatex/EVA total-loss generator. Use for repairable-vehicle estimates, second opinions, and estimates supporting a diminution rebuttal. Applies the CE estimate framework (failure modes, repair-vs-replace, completeness walkthrough), ABP rates, AZT paint costing, and OEM repair constraints. Expert class - an AI-assisted draft until a named human signs off.
---

# Repair Estimate

Builds a methodical, defensible desktop repair estimate from photos + vehicle details, using the CE estimate doctrine and the shared rate/method references. This is the general repair-cost estimate; the Audatex/EVA total-loss output remains in the `total-loss` skill (both share the estimate framework).

## References and dependencies

- `references/estimate-framework.md` — **canonical** CE estimating doctrine (named failure modes; side determination; repair-vs-replace indicators; impact-path and co-located fragile-item propagation; time anchors; baseline charges; the 15-step commercial-completeness walkthrough; paint taxonomy).
- `references/archive/valuationinfo-v1.txt` — retired v1 of the framework (provenance only; do not use).
- Charges: `abp-rates` (`abp-2026-rates.md`). Paint: `paint-calculation`. OEM constraints (replace-not-refurbish): `manufacturer-standards`. Vocabulary: `ce-domain-glossary`. Branding for any rendered output: `ce-branding`.
- Worked examples: `references/examples.md`.

## Workflow

1. Establish the vehicle and damage scope from photos + details; apply side determination.
2. Walk the estimate framework: damaged panels → repair vs replace → impact-path / co-located propagation → baseline + conditional charges.
3. Cost labour at the `abp-rates` rate; obtain paint hours + material from `paint-calculation`; apply OEM constraints from `manufacturer-standards` (e.g. a distorted alloy must be replaced, not refurbished).
4. Run the 15-step commercial-completeness walkthrough; guard against the named failure modes (thin output, zero parts, under-replacement, wrong side, missed inferred damage).
5. Output a structured estimate (parts / labour / paint / extras) and, where required, a CE-branded estimate PDF.

## Governance

Expert class — AI-assisted draft until a named human signs off; no autonomous external send.
