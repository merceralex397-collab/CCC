# CE Skill Catalogue

Date: 2026-05-29
Status: active catalogue (first wave; collisionplugin skills migrated to `src/skills/`)
Owner: unassigned
Group: agent-skills (parallel track)
Source links: `docs/plans/agent-skills/context.md`, `docs/plans/agent-skills/collisionplugin-migration.md`, `docs/superpowers/specs/2026-05-29-agent-skills-design.md`, `src/skills/README.md`

Portable skills under CCC governance, now living in `src/skills/`. Contract format: Claude Code `SKILL.md`. Governance class: **expert** (legal/expert output → mandatory human sign-off, "AI-assisted draft" until signed, no autonomous send) or **assist** (operational drafting/aid). Release state: `migrated` (in repo, pre-lifecycle) / `in-review` / `released`.

| Skill | Location | Output | Governance | Tool / asset deps | Release |
| --- | --- | --- | --- | --- | --- |
| `vehicle-valuation` | `src/skills/vehicle-valuation/` | Valuation report PDF + evidence pack PDF | expert | Autotrader Codex connector, DVSA-MOT MCP (`mcp-tooling`), `ce-branding`; `scripts/requirements.txt` | migrated → in-review |
| `total-loss` | `src/skills/total-loss/` | Audatex/EVA damage-assessment PDF | expert | EVA routing rules (`intelligence/evidence`, `bridge/eva`), `ce-branding` | migrated → in-review |
| `rebuttal` | `src/skills/rebuttal/` | Diminution rebuttal `.docx` (CPR Pt 35) | expert | `ce-branding`; case evidence | migrated → in-review |
| `roadworthy` | `src/skills/roadworthy/` | HS roadworthy certificate `.docx` | expert | engineer-report input, docx template, `ce-branding` | migrated → in-review |
| `ce-style` | `src/skills/ce-style/` | CE communication style/tone profile | assist | — | migrated |
| `ce-branding` (new) | `src/skills/ce-branding/` | Shared logo + document layout | assist | consumed by all document skills | created (SKILL.md + assets); templates to consolidate |
| `abp-rates` (new) | `src/skills/abp-rates/` | Shared UK repair-charge rate reference (ABP 2026) | assist/ref | consumed by total-loss, repair-estimate, paint-calculation, rebuttal, roadworthy, fee-note | created |
| `manufacturer-standards` (new) | `src/skills/manufacturer-standards/` | Shared OEM repair/position-statement library (VW/Volvo seed; US-market) | assist/ref | consumed by roadworthy, repair-estimate, total-loss | created |
| `ce-domain-glossary` (new) | `src/skills/ce-domain-glossary/` | Shared domain vocabulary + Audatex/ABP context | assist/ref | consumed by all document skills | created |
| `paint-calculation` (new) | `src/skills/paint-calculation/` | Paint time + material costing (AZT method) | assist | `abp-rates`; consumed by repair-estimate, total-loss | created |
| `repair-estimate` (new) | `src/skills/repair-estimate/` | Standalone desktop repair estimate (parts/labour/paint/extras) | expert | estimate-framework, `abp-rates`, `paint-calculation`, `manufacturer-standards`, `ce-branding` | created |
| `salvage-categorisation` (new) | `src/skills/salvage-categorisation/` | ABI salvage category (A/B/S/N) + notifications | expert | ABI COP reference; cross-links total-loss, rebuttal | created |
| `fee-note` (new) | `src/skills/fee-note/` | CE fee note / expert-services invoice | assist | `ce-branding`, `abp-rates`; business/finance owns the billing workflow | created |
| `case-summary` | (planned) | Case summary/status draft | assist | work-item data (`casework`) | plan → build |
| `missing-info` | (planned) | Missing-information checklist/chaser draft | assist | work-item state (`casework`) | plan → build |

Later (not first wave): valuation-explanation, report-clause RAG (needs approved corpus + licensing), AI-literacy, provider-mapping.

## Notes

- Migration record: `docs/plans/agent-skills/collisionplugin-migration.md`. The DVSA connector config was **not** migrated (held a live token).
- "migrated → in-review" = in `src/skills/` without behaviour change; review + bring under the lifecycle (`docs/plans/ai-platform/`) next.
- Expert-class skills cannot auto-send; a named human signs off the document (`docs/security/role_model.md`).
- `rebuttal`/`roadworthy` use their existing doc form; `total-loss` gained a `SKILL.md` wrapper (2026-05-29).
- **Reference-data skills (2026-05-29):** added `abp-rates`, `manufacturer-standards`, `ce-domain-glossary` (shared references), `paint-calculation`, `repair-estimate`, `salvage-categorisation`, `fee-note` — draining the `src/skills/infointake/` staging folder (now removed). Design: `docs/superpowers/specs/2026-05-29-reference-data-skills-design.md`.
- **Worked-case corpus:** real case artifacts (PII) live in the governed store `docs/reference/case-corpus/` and are referenced by each skill's `references/examples.md` by path. See `option-papers/reference-data-versioning.md` and `option-papers/oem-standards-uk-applicability.md`.
