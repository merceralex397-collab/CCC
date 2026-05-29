# CCC Skills

Production, portable skills for Collision Engineers. Planning and governance live in `docs/plans/agent-skills/`; the catalogue and lifecycle option paper are `docs/plans/agent-skills/skill-catalogue.md` and `docs/plans/agent-skills/option-papers/skill-lifecycle-and-portable-contract.md`.

## Runnable Skills

| Skill | Folder | Modes / role | Governance |
| --- | --- | --- | --- |
| vehicle-valuation | `vehicle-valuation/` | market valuation, evidence pack, valuation explanation, dispute response | expert; named-human sign-off |
| damage-estimating | `damage-estimating/` | repair-estimate, eva-total-loss, paint-costing, charge-review | expert for estimate outputs; assist for costing/review inputs |
| salvage-categorisation | `salvage-categorisation/` | ABI salvage category and notification obligations | expert/AQP; named-human sign-off |
| rebuttal | `rebuttal/` | diminution rebuttal draft | expert/legal; named-human sign-off |
| roadworthy | `roadworthy/` | HS roadworthy certificate draft | expert; named-human sign-off |
| finance-document | `finance-document/` | fee-note, standard-audatex-invoice, website-invoice, invoice-email-draft | assist; named-human review |
| ce-house-style | `ce-house-style/` | visual-layout, writing-tone support | assist/reference |

## Shared Reference Skills

| Skill | Folder | Role |
| --- | --- | --- |
| abp-rates | `abp-rates/` | ABP 2026 rate and charge reference |
| manufacturer-standards | `manufacturer-standards/` | OEM repair constraint reference |
| ce-domain-glossary | `ce-domain-glossary/` | CE vocabulary and Audatex/ABP context |

## Notes

- Worked-case examples with PII live in `docs/reference/case-corpus/` and are referenced by path, not bundled into portable skill packages.
- Expert/legal outputs remain AI-assisted drafts until a named human signs off; no autonomous external send.
- `vehicle-valuation` render dependencies are listed in `tools/vehicle-valuation/requirements.txt` and in `pyproject.toml` extras.
- `damage-estimating` now owns the former repair estimate, total-loss/Audatex, paint costing, and ABP charge-review material.
- `finance-document` now owns fee-note and invoice-template drafting; finance workflow, ledger, approvals, payment state, and chasing remain in `docs/plans/finance-billing/`.
