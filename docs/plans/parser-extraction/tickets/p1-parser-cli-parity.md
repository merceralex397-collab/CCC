# P1-003 Parser CLI Parity

- Status: implemented baseline.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/architecture/parser_ui_cli.md`, `docs/plans/parser-extraction/parser-mvp/plan.md`.
- Roadmap milestone: P1 Operational Core MVP.
- Dependencies: P1-001 (Parser Core MVP).
- Expected outputs: CLI commands for triage, parse, validate, export EVA JSON, package evidence, batch runs, provider listing/validation, and machine-readable warnings.
- Acceptance criteria: CLI uses same parser core and validation/export services as UI; every UI parser/export/package action has a CLI equivalent.
- Verification required: parity tests comparing UI service calls and CLI output for the same fixture set. Current command: `python -m pytest tests/test_parser_cli_mvp.py`.
- Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p1-operational-core-mvp.md` § P1-003.
- Superseded-by: none.
