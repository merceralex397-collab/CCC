# collisionplugin → CCC Migration Record (Phase 4)

Date: 2026-05-29
Status: implemented (file migration); follow-ups open
Owner: unassigned
Group: agent-skills (parallel track)
Source links: `src/skills/README.md`, `docs/plans/agent-skills/skill-catalogue.md`, `docs/superpowers/specs/2026-05-29-agent-skills-design.md`

Record of the Phase-4 migration of `../collisionplugin` assets into the CCC repo. Decisions (user, 2026-05-29): skills live **under `src/`**; **migrate the files now**.

## What moved (→ `src/skills/`)

| From (`collisionplugin/`) | To (`src/skills/`) |
| --- | --- |
| `skills/valuation/vehicle-valuation/` | `vehicle-valuation/` (SKILL.md, scripts, references, assets, agents) |
| `skills/valuation/totalloss/` | `total-loss/` |
| `skills/ce-communication-style/` | `ce-style/` |
| `rebuttal/` | `rebuttal/` |
| `roadworthy/` | `roadworthy/` |
| `assets/` (logo + example PDFs) | `ce-branding/assets/` |
| (new) | `ce-branding/SKILL.md`, `README.md` |

## Excluded / not migrated

- **`connectors/dvladvsa/connectorurl.md`** — held a **live bearer token**. Not copied. The DVSA-MOT MCP is being rebuilt first-party and the token must be rotated. See `docs/plans/mcp-and-tooling/option-papers/dvsa-mot-first-party-mcp.md`.
- `__pycache__/` + `*.pyc` build artifacts.
- `skills/New folder/` (empty junk dir).

## Adjustments made

- `src/skills/vehicle-valuation/SKILL.md`: render-script invocation paths updated from `skills/vehicle-valuation/...` to `src/skills/vehicle-valuation/...`.

## Follow-ups

Done (2026-05-29):
1. ✅ Render deps added to `pyproject.toml` as the `[skills]` extra (`pip install -e .[skills]`).
2. ✅ Shared layout templates + brand logos consolidated into `ce-branding/assets/`; `vehicle-valuation` repointed via `CE_BRANDING_DIR` in `_pdf_common.py` (static-verified; render test pending deps).
3. ✅ `SKILL.md` wrappers added for `rebuttal` and `roadworthy`.

Open:
4. Bring all skills under the lifecycle substrate (`docs/plans/ai-platform/`) — versioning, eval, redaction.
5. Wire tool deps via the gateway (`docs/plans/mcp-tooling/`): Autotrader Codex connector + first-party DVSA-MOT MCP.
6. Rotate the DVSA-MOT token (governance/IT).
7. Run a valuation render with `[skills]` deps installed to confirm the consolidated template/brand paths.
