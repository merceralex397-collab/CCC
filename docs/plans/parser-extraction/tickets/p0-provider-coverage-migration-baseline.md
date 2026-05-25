# P0-003 Provider Coverage And Migration Baseline

- Status: implemented baseline.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json`, `docs/reference/data/provider_coverage_matrix.md`, `docs/reference/originalplanning/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`.
- Roadmap milestone: P0 Foundation.
- Dependencies: P0-002 (Contracts Baseline).
- Expected outputs: provider coverage matrix, provider config contract, migration notes for 26 presets and uncovered job-sheet principals, plus versioned parser provider fixture with derived codes for blank-code engineer presets.
- Acceptance criteria: all 26 presets listed; `ACSP`, `OAK/AX`, `PRINCIPAL`, and `WOODLANDS` are tracked as uncovered/job-sheet anomalies; provider admin requirements are captured for P1.
- Verification required: scaffold verifier checks 26 provider presets and uncovered principal evidence; parser tests check `docs/reference/data/parser_provider_presets_v1.json`.
- Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p0-foundation.md` § P0-003.
- Superseded-by: none.

## Context

`docs/reference/raw/collisionrelateddocs/Settings Backup/providers.json` defines 26 provider presets using extraction methods:
- `Single Label` — most common; one field label locates the value.
- `Two Labels` — bracketed between two labels.
- `Fixed Position` — row/column offset from a known anchor.
- `Regex` — pattern match.
- `Manual Input` — no extraction; staff enters value.
- `Address Block` — multi-line extraction with six-line handling.

Known job-sheet principals not covered by a preset: `ACSP`, `OAK/AX` (composite), `PRINCIPAL` (likely header artefact), `WOODLANDS`. These must be triaged before parity is claimed.
