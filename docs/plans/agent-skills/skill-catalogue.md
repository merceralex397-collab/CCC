# CE Skill Catalogue

Date: 2026-05-29
Status: active catalogue (consolidated first wave in `src/skills/`)
Owner: unassigned
Group: agent-skills (parallel track)
Source links: `docs/plans/agent-skills/context.md`, `docs/plans/agent-skills/collisionplugin-migration.md`, `docs/superpowers/specs/2026-05-29-agent-skills-design.md`, `docs/superpowers/specs/2026-05-29-reference-data-skills-design.md`, `src/skills/README.md`, `docs/reference/case-corpus/README.md`

Portable skills under CCC governance, living in `src/skills/`. Contract format: `SKILL.md`. Governance class: **expert** (legal/expert output requiring mandatory human sign-off), **assist** (drafting/calculation aid), or **reference** (shared source material).

| Skill | Location | Modes / output | Governance | Dependencies | Release |
| --- | --- | --- | --- | --- | --- |
| `vehicle-valuation` | `src/skills/vehicle-valuation/` | `market-valuation`, `evidence-pack`, `valuation-explanation`, `dispute-response`; valuation report PDF + evidence pack PDF | expert | Autotrader connector, DVSA-MOT MCP, `ce-house-style` | in-review |
| `damage-estimating` | `src/skills/damage-estimating/` | `repair-estimate`, `eva-total-loss`, `paint-costing`, `charge-review`; estimate and damage-assessment drafts | expert for estimates, assist for costing/review | `abp-rates`, `manufacturer-standards`, `ce-domain-glossary`, `ce-house-style` | in-review |
| `salvage-categorisation` | `src/skills/salvage-categorisation/` | ABI category A/B/S/N and notification reasoning | expert/AQP | ABI COP reference, `damage-estimating` as cost context only | in-review |
| `rebuttal` | `src/skills/rebuttal/` | diminution rebuttal `.docx` draft | expert/legal | `ce-house-style`, `damage-estimating`, case evidence | in-review |
| `roadworthy` | `src/skills/roadworthy/` | HS roadworthy certificate draft | expert | engineer-report input, approved DOCX template, `ce-house-style`, `manufacturer-standards` | in-review |
| `finance-document` | `src/skills/finance-document/` | `fee-note`, `standard-audatex-invoice`, `website-invoice`, `invoice-email-draft` | assist | `ce-house-style`, raw/normalized invoice templates | in-review |
| `ce-house-style` | `src/skills/ce-house-style/` | `visual-layout`, `writing-tone`; logo/layout/tone support | assist/reference | CE brand assets and tone profile | in-review |
| `abp-rates` | `src/skills/abp-rates/` | ABP 2026 rates and charge reference | reference | ABP PDF + Markdown distillation | in-review |
| `manufacturer-standards` | `src/skills/manufacturer-standards/` | OEM repair-position reference | reference | VW/Volvo seed documents; UK applicability option paper | in-review |
| `ce-domain-glossary` | `src/skills/ce-domain-glossary/` | CE vocabulary and Audatex/ABP context | reference | glossary references | in-review |
| `case-status` | planned | `case-summary`, `missing-info`, `chaser-draft` | assist | canonical work-item data | planned |

## Consolidation Record

- `ce-house-style` owns the former visual branding and communication style material.
- `damage-estimating` owns the former total-loss, repair-estimate, paint-calculation, and ABP charge-review material.
- `finance-document` owns the former fee-note material plus raw and normalized invoice templates from `docs/reference/raw/collisionrelateddocs/collision_releated/`.
- `salvage-categorisation`, `vehicle-valuation`, `rebuttal`, and `roadworthy` remain separate because they carry distinct expert or legal sign-off boundaries.
- Worked-case corpus files stay in `docs/reference/case-corpus/` and are referenced by path because they contain PII.

Expert-class skills cannot auto-send; a named human signs off the final document (`docs/security/role_model.md`).
