---
name: abp-rates
description: Shared reference for current UK collision-repair charges from the ABP Club rate book (2026 edition). Use whenever a skill needs labour rates, the repair-plan fee, ADAS calibration charges, EV/hybrid handling, alloy/alignment/air-con/recovery/storage specialist charges, paint-protection or mobility charges, or the regional uplift - to build or challenge a repair estimate, total-loss assessment, finance document, or diminution rebuttal. Consumed by damage-estimating, rebuttal, roadworthy, and finance-document. Reference data, not an output-producing skill.
---

# ABP Rates (shared reference)

Single source of truth for ABP Club retail and non-contract charges, so every Collision Engineers document quotes the same current figures instead of re-embedding rate tables.

## Contents

- `references/abp-2026-rates.md` — the structured, queryable rate tables (labour, repair-plan fee, EV/hybrid, environmental/admin, ADAS, specialist operations, parts/consumables, paint-protection, mobility, regional uplift).
- `references/abp2026.pdf` — the authoritative source document.

## Versioning

The bundled rates are the **2026** edition (charges effective 1 January 2026). When the ABP Club publishes a new edition, add `references/abp-<year>-rates.md` + the new PDF alongside, update the banner, and point consumers at the new file. Do not silently overwrite — keep prior editions for matters assessed under them. See `docs/plans/agent-skills/option-papers/reference-data-versioning.md`.

## Usage

Cite a specific rate by section and figure; do not paraphrase a rate from memory. For any charge in an estimate or fee note, the `abp-2026-rates` figure is canonical. Where a charge is time-based, apply the relevant labour rate; where it is a fixed fee, quote it directly. The regional uplift applies only to London and the home counties.

## Governance

Assist / reference class — produces no client-facing output itself; the skills that consume it own their outputs and human sign-off.
