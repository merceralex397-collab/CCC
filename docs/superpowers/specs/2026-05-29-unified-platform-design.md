# Unified Platform: Convergence Map + Decommissioning Gates — Design (deferred build)

Date: 2026-05-29
Status: approved design (brainstorming output) — design-only; build deferred to G6
Owner: unassigned
Workspace: `docs/plans/unified-platform/` (group: unified-platform, G6 spine endpoint)
Source links: `docs/plans/unified-platform/context.md`, `docs/architecture/future_system_convergence.md`, `docs/plans/_groups.md`

## Context

The unified platform is the spine endpoint (G6), explicitly built **later, from scratch**, converging everything the other groups deliver. This iteration captures the cross-workspace dependency map + decommissioning gates only; no platform build now.

## Decision captured (user, 2026-05-29)

Capture the **cross-workspace dependency map + decommissioning gates as a design-only convergence plan**; build deferred to G6. (Platform stack/UI direction is *not* decided now.)

## Convergence Dependency Map

The platform inherits and converges, in dependency order:

```text
foundation (continuous: contracts, role model, governance, ops gates)
   │
parser (G1) ─► bridge (G2) ─► casework (G2-G3: work-item store + WinUI hub)
   │                               │
   ├─ mcp-tooling (parallel: tool gateway) ┐
   ├─ agent-skills (parallel: skill catalogue) ┤ serve all of the above
   │                               │
intelligence + ai-platform (G3-G4) ─► business (G5)
   │
   ▼
unified-platform (G6): one mature end-to-end system over the shared
contracts (parser result, work item, review/audit, EVA export, evidence
package, storage adapter, provider/principal config), the casework
operational hub, the tool gateway, the skill catalogue, and the role model.
```

The platform does not reimplement specialist features; it converges them under one case-management system, role model, UI (PWA/mobile/web), automation spine, integrations, analytics, and governance.

## Decommissioning Gates

Retire legacy only on evidence:

- **`cedocumentmapper` monolith** → retire after the CCC parser reaches parity (26 presets + corpus regression), the staff workflow is adopted, and rollback is proven.
- **CE Job Sheet spreadsheet** → retire after `casework` work-item state + review reach operational parity (the spreadsheet's queue/principal/garage roles), with audit + rollback + support ownership.
- Decommissioning is a controlled **operations-quality** release milestone, never an MVP side effect.

## Goals / Non-goals

**Goals:** the dependency map; the decommissioning gates; confirmation that the platform inherits the shared contracts + casework hub + gateway + skills + role model.

**Non-goals:** building the platform; deciding its stack/UI now (the casework local-web-UI option remains the likely seed, decided at G6); domain implementation. Personal injury and KADOE remain out of scope.

## Sequencing

G6 — after parser/bridge/casework/intelligence/ai-platform/business are delivered and parity/rollback/adoption evidence exists. This workspace stays a coordinating endpoint until then.

## Risks & Open Questions

- Platform stack/UI direction deferred (web vs convergence of the WinUI casework app) — decide at G6.
- Parity criteria for decommissioning each legacy system need explicit, measurable definitions.
- Migration approach (big-bang vs incremental) is a G6 decision.

## Acceptance Criteria

- The cross-workspace dependency map is recorded.
- Decommissioning gates for `cedocumentmapper` + the spreadsheet are defined (parity/rollback/adoption).
- The platform's inheritance of the shared contracts/hub/gateway/skills/role model is documented; build remains deferred.
