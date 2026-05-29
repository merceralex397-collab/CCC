# Plan Workspace Groups And Development Sequence

Date: 2026-05-29
Status: active grouping overlay
Owner: unassigned
Created: 2026-05-29
Last reviewed: 2026-05-29
Source links: `docs/plans/_index.md`, `docs/plans/roadmap.md`, `docs/plans/workspace_ownership_matrix.md`, `docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: all workspace source maps, governance/security gates, operations-quality gates
Expected outputs: a seamless, dependency-ordered development roadmap that groups the planning workspaces by broad area, wave, and capability layer
Acceptance criteria: every current workspace belongs to exactly one broad group; the spine and parallel tracks are explicit; high-risk work is gated before implementation
Verification required: `python tools/verify_scaffold.py`
Archive target: owning workspace `archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Purpose

This file groups the planning workspaces under `docs/plans/` into **10 broad areas** so the programme reads as one seamless development roadmap instead of 22 flat folders. It is a **logical overlay**: the workspace folders have not moved yet. A later, dedicated migration step will physically consolidate them into the broad-workspace folders named below (`Target folder`), rewriting the verifier, generators, manifests, and cross-references in a single committed pass.

Two axes describe each group:

- **Wave** — *when* the work is built. Waves run roughly in order (G0 continuous, then G1 → G6), with two parallel tracks that run alongside G1–G2.
- **Layer** — *what kind* of work it is (capability area), independent of timing.

The near-term **spine** is: **parser redesign (G1) → Outlook + Box + EVA bridge (G2) → unified system (G6, later)**. **MCP** and **agent-skills** are **parallel tracks** developed alongside the spine, not blockers on it. **Foundation** (governance, operations-quality, setup, coordination) is **continuous** and gates every wave.

## Group Map

| Group (target folder) | Wave | Layer | Role | Member workspaces (current paths) |
| --- | --- | --- | --- | --- |
| `foundation/` | G0 / continuous | cross-cutting | gates every wave | `governance-security/`, `operations-quality/`, `initial-repo-setup/`, `operational-core/` |
| `parser/` | **G1** | ingest-parse | **spine** | `parser-extraction/` (→ `extraction`), `provider-principal-config/` (→ `providers`) |
| `bridge/` | **G2** | integrations | **spine** | `intake-storage-integrations/` (→ `intake` + `storage` + `eva`) |
| `casework/` | G2–G3 | operational | spine support | `case-workflow-state/` (→ `state`), `user-experience-interfaces/` (→ `ui`), `automation-centre/` (→ `automation`) |
| `intelligence/` | G3–G4 | intelligence | domain depth | `evidence-estimate-review/` (→ `evidence`), `vehicle-valuation-data/` (→ `vehicle`), `engineer-communications/` (→ `comms`) |
| `mcp-tooling/` | **parallel** | ai-tooling | **parallel track** | `mcp-and-tooling/` |
| `agent-skills/` | **parallel** | ai-tooling | **parallel track** | `agent-skills/` (+ promoted `collisionplugin` skills) |
| `ai-platform/` | G4 | ai-tooling | domain depth | `ai-agents/` (→ `agents`), `ai-platform-tools/` (→ `platform-tools`) |
| `business/` | G5 | business-external | later | `finance-billing/` (→ `finance`), `external-platform-partners/` (→ `partners`), `product-business/` (→ `product`), `analytics-data-platform/` (→ `analytics`) |
| `unified-platform/` | **G6** | platform | **spine (later)** | `unified-platform/` |

## Development Sequence

```text
continuous:  foundation  ───────────────────────────────────────────────►  (gates every wave)

spine:       parser ──► bridge ──► casework ──► intelligence/ai-platform ──► business ──► unified-platform
             (G1)       (G2)       (G2–G3)      (G3–G4)                      (G5)         (G6)

parallel:    mcp-tooling   ┐
             agent-skills  ┘  run alongside G1–G2 (serve parser + bridge; do not block them)
```

- **Spine is sequential**: each spine group should reach its planned exit gate before the next starts in earnest, though planning interviews can run ahead.
- **Parallel tracks**: `mcp-tooling` and `agent-skills` are planned and built alongside the parser and bridge. They wrap/serve those capabilities (e.g. an Outlook Graph MCP, a case-summary skill) but are not on the critical path.
- **Continuous**: `foundation` work (DPIA/vendor governance, release/rollback, regression gates, coordination) applies across all waves.

## Interview Order

Each broad workspace gets a full brainstorming interview producing `context.md` (information), an expanded `plan.md`, `open-questions.md`, and a dated design spec in `docs/superpowers/specs/`. Priority order for the current effort:

1. `parser` (G1) — framed as a redesign improving on the legacy `cedocumentmapper`, building on the existing `src/ccc_parser/` baseline.
2. `bridge` (G2) — Outlook + Box + EVA; Outlook/Graph intake grounded via the Microsoft Learn MCP.
3. `mcp-tooling` (parallel) — tool registry/gateway + DVSA-MOT and Autotrader connectors.
4. `agent-skills` (parallel) — skill catalogue + promotion of `collisionplugin` skills.

`unified-platform` (G6) is the later spine endpoint; no interview is scheduled for it yet.

## Per-Wave Gates

- **G0 foundation** is a precondition, not a phase: privacy/vendor/retention/expert-boundary and release/rollback/regression gates must be cleared before any governed activation in later waves.
- **G1 parser** preserves all 26 provider presets, deterministic-first parsing, UI/CLI parity, and the private real corpus regression; no behaviour regression is allowed.
- **G2 bridge** keeps live Outlook intake, live Box upload, and EVA/Sentry submission behind dry-run/sandbox tests, idempotency, duplicate prevention, runbooks, and manual approval gates.
- **Parallel tracks** expose only approved adapters/skills behind permissions, audit, and human-approval boundaries.
- **G5–G6** (business, unified-platform, decommissioning) start in option papers and require governance + operations sign-off before implementation.

## Relationship To Existing Docs

- `docs/plans/_index.md` lists the current (flat) workspace folders.
- `docs/plans/roadmap.md` holds the programme roadmap (Sections 0–9); this file re-expresses that sequence as broad groups with spine/parallel roles.
- `docs/plans/workspace_ownership_matrix.md` holds the per-workspace ownership boundaries that survive the eventual folder consolidation.
- The physical consolidation into the `Target folder` names above is a **deferred, separately-committed migration**; until then, cite the current flat paths.
