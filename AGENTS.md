# AGENTS.md

## Repository Hygiene

- Treat `collisionrelateddocs/` raw files as immutable evidence. Do not edit, rename destructively, overwrite, or normalize in place.
- Keep generated derivatives under `docs/normalized/`, `docs/data/`, or another documented derivative path.
- Update `docs/source_manifest.md`, `docs/source_manifest.csv`, and `docs/source_manifest.json` whenever source files, generated companions, active docs, or archives change.
- Keep `README.md`, `docs/roadmap.md`, `docs/architecture/`, `docs/contracts/`, `docs/requirements/`, and `docs/glossary.md` current with behavior-changing work.
- Do not commit secrets, API keys, tokens, OAuth material, mailbox credentials, or provider credentials. Run the scaffold verification and a targeted secret scan before any commit or push.
- Preserve unrelated local configuration, auth state, MCP settings, and user files.
- Use `rg` or `rg --files` first for search. Use structured parsers for JSON, spreadsheets, DOCX, and PDFs when available.
- Use `apply_patch` for manual edits. Do not create or edit files with shell write tricks.

## Planning And Ticket Lifecycle

- Every active plan or ticket must include status, owner, created date, last reviewed date, source links, roadmap milestone, dependencies, expected outputs, acceptance criteria, verification required, archive target, and supersedes/superseded-by fields where applicable.
- When a plan or ticket is implemented, move it to `archive/plans/implemented/`, rename it with the completion date, and add an implemented-state block at the top.
- Superseded or merged plans go to `archive/plans/superseded/` with a pointer to the replacement doc or ticket.
- Generated plan packs are reference material unless explicitly promoted into active docs or tickets.

## Parser Rules

- Keep UI and CLI thin. Both must call the same parser core and share validation/export contracts.
- Do not import the legacy `cedocumentmapper` monolith wholesale. Reference it for behavior and migrate requirements deliberately.
- Parser output must pass canonical schema validation before EVA-specific output.
- Provider coverage must be tracked in `docs/data/provider_coverage_matrix.md` before adding or changing provider rules.
- Any cloud OCR/document-intelligence path requires privacy, cost, data-residency, and vendor review before use.

## Verification

- Verify before claiming completion. Prefer reproducible commands and direct checks.
- For this scaffold, run `tools/verify_scaffold.py`.
- If pytest or external parser dependencies are not installed, document that instead of claiming test coverage from unavailable tools.
