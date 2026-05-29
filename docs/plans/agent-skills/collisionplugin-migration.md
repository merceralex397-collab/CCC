# collisionplugin → CCC Migration Record (Phase 4)

Date: 2026-05-29
Status: implemented (file migration and consolidation); follow-ups open
Owner: unassigned
Group: agent-skills (parallel track)
Source links: `src/skills/README.md`, `docs/plans/agent-skills/skill-catalogue.md`, `docs/superpowers/specs/2026-05-29-agent-skills-design.md`

Record of the Phase-4 migration of `../collisionplugin` assets into the CCC repo and the follow-on first-wave consolidation. Decisions (user, 2026-05-29): skills live **under `src/skills/`** and should be coherent runnable units, not compatibility aliases.

## What moved (→ `src/skills/`)

| From (`collisionplugin/`) | To (`src/skills/`) |
| --- | --- |
| `skills/valuation/vehicle-valuation/` | `vehicle-valuation/` (SKILL.md, scripts, references, assets, agents) |
| `skills/valuation/totalloss/` | `damage-estimating/` (`eva-total-loss` mode) |
| `skills/ce-communication-style/` | `ce-house-style/` (`writing-tone` mode) |
| `rebuttal/` | `rebuttal/` |
| `roadworthy/` | `roadworthy/` |
| `assets/` (logo + example PDFs) | `ce-house-style/assets/` |
| reference-data estimating material | `damage-estimating/`, `abp-rates/`, `manufacturer-standards/`, `ce-domain-glossary/` |
| invoice / fee-note material | `finance-document/` |

## Excluded / not migrated

- **`connectors/dvladvsa/connectorurl.md`** — held a **live bearer token**. Not copied. The DVSA-MOT MCP is being rebuilt first-party and the token must be rotated. See `docs/plans/mcp-and-tooling/option-papers/dvsa-mot-first-party-mcp.md`.
- `__pycache__/` + `*.pyc` build artifacts.
- `skills/New folder/` (empty junk dir).

## Adjustments made

- `src/skills/vehicle-valuation/SKILL.md`: render-script invocation paths updated from `skills/vehicle-valuation/...` to `src/skills/vehicle-valuation/...`.

## Follow-ups

Done (2026-05-29):
1. ✅ Render deps added to `pyproject.toml` as the `[skills]` extra (`pip install -e .[skills]`).
2. ✅ Shared layout templates + brand logos consolidated into `ce-house-style/assets/`; `vehicle-valuation` repointed via `CE_HOUSE_STYLE_DIR` in `_pdf_common.py` (static-verified; render test pending deps).
3. ✅ `SKILL.md` wrappers added for `rebuttal` and `roadworthy`.
4. ✅ First-wave consolidation completed: `damage-estimating`, `finance-document`, and `ce-house-style` replaced the split estimating, finance, branding, and style folders.

Open:
5. Bring all skills under the lifecycle substrate (`docs/plans/ai-platform-tools/`) — versioning, eval, redaction.
6. Wire tool deps via the gateway (`docs/plans/mcp-and-tooling/`): Autotrader Codex connector + first-party DVSA-MOT MCP.
7. Rotate the DVSA-MOT token (governance/IT).
8. Run a valuation render with `[skills]` deps installed to confirm the consolidated template/brand paths.
