# P2-001 Golden Corpus Regression Harness

- Status: implemented baseline.
- Owner: TBD.
- Created: 2026-05-23.
- Last reviewed: 2026-05-24.
- Source links: `docs/reference/originalplanning/phase7_expanded_markdown_plan/additional_items/08_10_test_corpus_and_regression_harness.md`, `docs/decisions/0008-private-real-corpus-only.md`.
- Roadmap milestone: P2 Parser Hardening And Provider Parity.
- Dependencies: P1-001 (Parser Core MVP).
- Expected outputs: private corpus fixture registry, expected result snapshots, provider regression runner. Implemented as `docs/reference/data/parser_corpus_fixture_ledger.*`, `docs/reference/data/parser_provider_presets_v1.json`, and `tools/run_parser_corpus.py`.
- Acceptance criteria: all 26 provider presets have golden examples and expected canonical outputs; diffs are reviewable.
- Verification required: corpus regression command passes for current accepted baseline. Current command: `python tools/run_parser_corpus.py`.
- Archive target: `docs/plans/parser-extraction/archived_plans/implemented/`.
- Supersedes: `docs/plans/operational-core/tickets/p2-parser-hardening-provider-parity.md` § P2-001.
- Superseded-by: none.
