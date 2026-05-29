# Case Corpus (governed worked-example store)

Real Collision Engineers case artifacts — example **outputs**, example **inputs**, and worked references — used as golden examples and fixtures by the skills in `src/skills/`. Organised by the skill each set primarily supports.

## Contains personal data

These files contain **real claimant personal data** (names, addresses, phone numbers, vehicle registrations) and court/matter references. They are committed to this repository as a governed internal store, by explicit decision (2026-05-29).

- **Access** is governed by the CE role model (`docs/security/role_model.md`, DRAFT).
- **Retention** follows `docs/security/data_retention_policy.md` (DRAFT).
- **Redact before external distribution.** The portable skills in `src/skills/` reference these files **by repo path** as examples — a skill can be packaged and shared without shipping this corpus. Anonymise/synthesise before any external use, model training, or skill distribution.
- Logged in the cross-cutting governance backlog: `docs/plans/foundation/option-papers/cross-cutting-gaps-backlog.md`.

## Layout

| Folder | Contents | Used by |
| --- | --- | --- |
| `vehicle-valuation/` | Autotrader comparable adverts, a Percayso companion report, internal EVA valuation-system screenshots (`eva-screenshots/`) | vehicle-valuation |
| `total-loss/` | Audatex damage estimates + damage image packs | total-loss, repair-estimate |
| `roadworthy/` | Instruction letters to the engineer + a roadworthiness/total-loss advisory report | roadworthy, repair-estimate |
| `rebuttal/` | Court expert / diminution reports + report figures/images | rebuttal |
| `fee-note/` | A Collision Engineers fee note (expert-services invoice) | fee-note |

## Provenance

Migrated 2026-05-29 from the `src/skills/infointake/` staging folder (now removed) — see `docs/plans/agent-skills/collisionplugin-migration.md` and the design spec `docs/superpowers/specs/2026-05-29-reference-data-skills-design.md`.
