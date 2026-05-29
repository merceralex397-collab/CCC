---
name: finance-document
description: Use to draft Collision Engineers finance documents: fee-note, standard-audatex-invoice, website-invoice, and invoice-email-draft. Produces document drafts only; billing workflow, ledger, payment status, approvals, and chasing remain owned by finance/business. Human review required before send.
---

# Finance Document

Draft CE finance documents in house style while keeping business finance state out of the skill.

## Modes

| Mode | Use for | Load |
| --- | --- | --- |
| `fee-note` | Expert-services fee note. | `references/fee-note.md` |
| `standard-audatex-invoice` | Invoice matching the raw Standard Audatex template. | `references/invoice-templates.md` |
| `website-invoice` | Website-origin invoice matching the raw website template. | `references/invoice-templates.md` |
| `invoice-email-draft` | Email wording to send a reviewed invoice/fee note. | `references/email-draft.md` and `src/skills/ce-house-style/` in `writing-tone` mode |

## Required Inputs

- Matter/reference, addressee, invoice or fee-note type, services/charge lines, VAT treatment, payment terms, and any approved template variant.
- Do not infer paid/unpaid status or finance ledger state unless supplied by finance.

## References

- `references/fee-note.md`
- `references/invoice-templates.md`
- `references/email-draft.md`
- `src/skills/ce-house-style/`

## Governance

Assist class. A named human reviews every finance document before send. No autonomous payment chasing, external send, ledger update, or payment-state conclusion.

## Validation

Run repository verification after skill changes:

```powershell
python tools/verify_scaffold.py
```
