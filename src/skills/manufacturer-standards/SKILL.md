---
name: manufacturer-standards
description: Shared reference library of vehicle-manufacturer (OEM) repair position statements - wheel and tyre reconditioning prohibitions, genuine-parts policies, and authoritative repair-procedure sources (erWin, ElsaPro, VIDA). Use whenever a repair estimate, total-loss assessment, or roadworthy certificate must respect an OEM constraint, e.g. confirming a damaged alloy must be replaced (not refurbished) or that only genuine parts are approved. Consumed by roadworthy, repair-estimate and total-loss. Reference data, not an output-producing skill.
---

# Manufacturer Standards (shared reference)

A growing library of OEM repair/position statements so estimating and certification decisions can cite the manufacturer's own ruling (e.g. "reconditioned wheels are not approved") rather than asserting it unsourced.

## Contents

- `references/oem-index.md` — index of statements (make · topic · ruling · market · source · date).
- `references/volkswagen-wheel-repair.pdf`, `references/volvo-wheels-tyres.pdf` — source statements.

## Market caveat

The seed statements are **US-market** (Volkswagen of America; Volvo Car USA). Their engineering intent (no reconditioned wheels; genuine parts; OEM procedures) is widely applicable, but **confirm UK/EU applicability before relying on a statement in a UK matter** — a UK OEM equivalent or technical bulletin should be sourced and added. See `docs/plans/agent-skills/option-papers/oem-standards-uk-applicability.md`.

## Usage

Look up the make + topic in `oem-index.md`; if a statement applies, cite the manufacturer ruling and force the corresponding estimate decision (e.g. replace, not refurbish). Record the market and date alongside the citation. Add new OEM statements as a PDF in `references/` plus a row in the index.

## Governance

Assist / reference class.
