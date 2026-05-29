# CCC Skills

Production, portable skills for Collision Engineers, migrated from `../collisionplugin` (2026-05-29). Planning + governance live in `docs/plans/agent-skills/`; the catalogue + lifecycle are `docs/plans/agent-skills/skill-catalogue.md` and `docs/plans/agent-skills/option-papers/skill-lifecycle-and-portable-contract.md`. Contract format: Claude Code `SKILL.md`.

## Skills

| Skill | Folder | Form | Governance |
| --- | --- | --- | --- |
| vehicle-valuation | `vehicle-valuation/` | `SKILL.md` + scripts + references + assets | expert (named-human sign-off) |
| total-loss (Audatex/EVA) | `total-loss/` | `context.md` + `tool.py.md` | expert |
| rebuttal (diminution) | `rebuttal/` | `projecttext.md` | expert |
| roadworthy | `roadworthy/` | `startingprompt.md` + `toolinstructions.md` + `template.md` | expert |
| ce-style | `ce-style/` | style/tone profile (`.docx`) | assist (underpins drafting) |
| ce-branding | `ce-branding/` | `SKILL.md` + brand assets | assist (shared brand/layout) |
| abp-rates | `abp-rates/` | `SKILL.md` + rate reference (md + PDF) | assist/ref (shared rates) |
| manufacturer-standards | `manufacturer-standards/` | `SKILL.md` + OEM index + statements | assist/ref (shared OEM standards) |
| ce-domain-glossary | `ce-domain-glossary/` | `SKILL.md` + glossary + Audatex/ABP context | assist/ref (shared vocabulary) |
| paint-calculation | `paint-calculation/` | `SKILL.md` + AZT method (md + PDF) | assist (costing aid) |
| repair-estimate | `repair-estimate/` | `SKILL.md` + estimate framework | expert (named-human sign-off) |
| salvage-categorisation | `salvage-categorisation/` | `SKILL.md` + ABI COP reference | expert (AQP / named-human sign-off) |
| fee-note | `fee-note/` | `SKILL.md` + fee-note spec | assist (named-human review) |

## Notes

- **Reference-data skills (2026-05-29):** added shared references (`abp-rates`, `manufacturer-standards`, `ce-domain-glossary`), a costing aid (`paint-calculation`), and new skills (`repair-estimate`, `salvage-categorisation`, `fee-note`); `total-loss` gained a `SKILL.md` wrapper. Worked-case examples (real PII) live in the governed store `docs/reference/case-corpus/` and are referenced by path (see each skill's `references/examples.md`).
- **Expert/legal outputs** (valuation, rebuttal, roadworthy, total-loss) produce an "AI-assisted draft" until a named human signs off; no autonomous external send. See the CE role model (`docs/security/role_model.md`).
- **Dependencies:** `vehicle-valuation/scripts/requirements.txt` lists the render deps (reportlab/jinja2/etc.); these are not yet added to the repo's `pyproject.toml`.
- **Tool dependencies:** vehicle-valuation uses the Autotrader Codex connector + the DVSA-MOT MCP (see `docs/plans/mcp-tooling/`).
- **Not migrated:** the DVSA connector config (`collisionplugin/connectors/dvladvsa/connectorurl.md`) — it held a live token; it is being rebuilt first-party and the token must be rotated (`docs/plans/mcp-and-tooling/option-papers/dvsa-mot-first-party-mcp.md`).
- **Done (2026-05-29):** shared layout templates + brand logos consolidated into `ce-branding/assets/`; `vehicle-valuation` renders from there (path repoint static-verified; render test pending `[skills]` deps); `SKILL.md` wrappers added for `rebuttal`/`roadworthy`; render deps added to `pyproject.toml` (`pip install -e .[skills]`).
- **Remaining:** wire skills into the lifecycle substrate (`docs/plans/ai-platform/`); rotate the DVSA token; run a valuation render to confirm the consolidated paths.
