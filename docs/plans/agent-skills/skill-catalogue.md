# CE Skill Catalogue

Date: 2026-05-29
Status: active catalogue (first wave)
Owner: unassigned
Group: agent-skills (parallel track)
Source links: `docs/plans/agent-skills/context.md`, `docs/superpowers/specs/2026-05-29-agent-skills-design.md`

Portable skills under CCC governance. Contract format: Claude Code `SKILL.md`. Governance class: **expert** (legal/expert output → mandatory human sign-off, "AI-assisted draft" until signed, no autonomous send) or **assist** (operational drafting/aid). Release state: `draft` / `in-review` / `released`.

| Skill | Source | Output | Governance | Tool / asset deps | Release |
| --- | --- | --- | --- | --- | --- |
| `vehicle-valuation` | `collisionplugin/.../vehicle-valuation/` (full SKILL.md) | Valuation report PDF + evidence pack PDF | expert | Autotrader Codex connector, DVSA-MOT MCP (`mcp-tooling`), `ce-branding` | adopt → in-review |
| `rebuttal` | `collisionplugin/rebuttal/projecttext.md` | Diminution rebuttal `.docx` (CPR Pt 35) | expert | `ce-branding`; case evidence | adopt → in-review |
| `roadworthy` | `collisionplugin/roadworthy/` | HS roadworthy certificate `.docx` | expert | engineer-report input, docx template, `ce-branding` | adopt → in-review |
| `total-loss` | `collisionplugin/.../totalloss/` | Audatex/EVA damage-assessment PDF | expert | EVA routing rules (`intelligence/evidence`, `bridge/eva`), `ce-branding` | adopt → in-review |
| `ce-style` | `collisionplugin/skills/style/` | CE communication style/tone profile | assist (underpins drafting) | — | adopt → released |
| `ce-branding` (new) | `collisionplugin/assets/` + `.../templates/` + `references/brand.md`, `pdf-template-spec.md` | Shared logo + document layout templates | assist (shared asset module) | consumed by all document skills | define |
| `case-summary` | ref `16_case_summary_status_skill.md` | Case summary/status draft | assist | work-item data (`casework`) | plan → build |
| `missing-info` | ref plans (missing-info) | Missing-information checklist/chaser draft | assist | work-item state (`casework`) | plan → build |

Later (not first wave): valuation-explanation, report-clause RAG (needs approved corpus + licensing), AI-literacy, provider-mapping.

## Notes

- "adopt → in-review" = bring the existing collisionplugin skill under the lifecycle without behaviour change, then review.
- Expert-class skills cannot auto-send; a named human signs off the document.
- Tool-dependent skills are gated by `mcp-tooling` gateway availability.
