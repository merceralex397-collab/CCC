---
name: fee-note
description: Produce a Collision Engineers fee note (expert-services invoice) in house style - header and matter reference, services rendered, time/rate lines, expenses, totals and payment terms. Use when issuing or drafting a fee note for expert/engineering services on a matter. Assist class - a named human reviews before any send; the billing workflow and ledger remain owned by the business/finance track.
---

# Fee Note

Drafts a Collision Engineers fee note for expert-services billing, in CE house style.

## References and dependencies

- `references/fee-note-spec.md` — the fee-note structure and house-style rules (derived from a worked example).
- Branding/layout: `ce-branding` (logo, templates, footer). Charge references where applicable: `abp-rates`.
- Worked example: `docs/reference/case-corpus/fee-note/GX18XEB-fee.pdf`.

## Workflow

1. Capture the matter reference, addressee, and services rendered.
2. Add time/rate lines and expenses; total with the correct VAT treatment.
3. Render in CE house style via `ce-branding`.

## Governance and non-overlap

Assist class — a **named human reviews before send**; no autonomous external send. This skill produces the *document* only. The billing **workflow**, ledger, payment tracking and finance reporting are owned by the **business/finance** track (`docs/plans/business/`) — coordinate, do not duplicate.
