# Reference-Data Skills, Worked-Case Corpus & Information Folds — Design

Date: 2026-05-29
Status: implemented (this pass); lifecycle wiring open
Group: agent-skills (parallel track)
Source links: `docs/plans/agent-skills/skill-catalogue.md`, `docs/plans/agent-skills/plan.md`, `src/skills/README.md`, `docs/reference/case-corpus/README.md`

## Problem

`src/skills/infointake/` was a raw staging folder holding (A) seven authoritative reference documents (ABP 2026 rate book, AZT paint method, ABI salvage Code of Practice, VW + Volvo OEM wheel statements, a desktop repair-estimate framework, and a duplicate v1 of it) and (B) ~25 real worked-case files (valuation reports, Audatex estimates, instruction letters, image packs, court expert/diminution reports, a fee note, and diminution templates) — most containing claimant PII. None of this was wired into the skillset; the existing skills (vehicle-valuation, total-loss, rebuttal, roadworthy, ce-style, ce-branding) re-embedded rate data by hand and had no governed example corpus.

## Goal

(1) Add skills not covered by the existing set, and (2) fold in information not yet in the skillset — organising the reference docs as useful reference data factored into the estimation/valuation skills, deep-designing every gap.

## Decisions (user, 2026-05-29)

- Hybrid architecture: shared reference skills + new decision skills + fold-ins.
- The estimate framework lives **both** as a shared reference into `total-loss` and as a new standalone `repair-estimate` skill.
- New `manufacturer-standards` reference skill seeded with VW/Volvo.
- **Commit the worked-case files into a governed in-repo store** (PII accepted in git history).
- **Design a `fee-note` skill now.**
- Skills live under `src/skills/`; expert outputs keep mandatory human sign-off.

## Architecture

- **Shared reference skills** (assist; consumed by others): `abp-rates`, `manufacturer-standards`, `ce-domain-glossary` — define data once, cite everywhere.
- **New decision-logic skills** (expert; human sign-off): `repair-estimate`, `salvage-categorisation`; plus `paint-calculation` (assist costing aid) and `fee-note` (assist; named-human review before send).
- **Governed case corpus**: `docs/reference/case-corpus/<skill>/` holds the real artifacts once; skills reference them by path as golden examples/fixtures. Operational templates (diminution report template + anticipated-arguments) bundle into `rebuttal`.
- **Fold-ins**: existing skills gain `references/authoritative-sources.md` (cite the shared refs) + `references/examples.md` (point to the corpus); `total-loss` gains its missing `SKILL.md` wrapper.

## New skills

| Skill | Class | Home | Core reference |
| --- | --- | --- | --- |
| `abp-rates` | assist/ref | `src/skills/abp-rates/` | `abp-2026-rates.md` (+ `abp2026.pdf`) — versioned |
| `manufacturer-standards` | assist/ref | `src/skills/manufacturer-standards/` | `oem-index.md` (+ VW/Volvo PDFs); US-market caveat |
| `ce-domain-glossary` | assist/ref | `src/skills/ce-domain-glossary/` | `glossary.md`, `audatex-abp-context.md` |
| `paint-calculation` | assist | `src/skills/paint-calculation/` | `azt-paint-method.md` (+ AZT PDF) |
| `repair-estimate` | expert | `src/skills/repair-estimate/` | `estimate-framework.md` (from 02A) |
| `salvage-categorisation` | expert | `src/skills/salvage-categorisation/` | `abi-salvage-cop.md` (+ COP PDF) |
| `fee-note` | assist | `src/skills/fee-note/` | `fee-note-spec.md` |

`repair-estimate` composes `estimate-framework` + `abp-rates` + `paint-calculation` + `manufacturer-standards`. `total-loss` shares `estimate-framework` and now cites `abp-rates` as canonical (its inline matrix retained as a working copy). `fee-note` produces the document only; the billing workflow stays in the business/finance track.

## Governed case corpus (PII)

Committed to `docs/reference/case-corpus/` by explicit decision. `README.md` records: real claimant PII; access per role model (DRAFT); retention per retention policy (DRAFT); **redact before external distribution** (skills reference by path, so a packaged skill need not ship the corpus). Logged in the foundation cross-cutting backlog.

## Time-sensitive & provenance caveats

- ABP rates (effective 1 Jan 2026) and the ABI COP (28.05.2025) carry validity banners; refresh tracked in `option-papers/reference-data-versioning.md`.
- VW/Volvo statements are US-market; verify UK applicability before relying — `option-papers/oem-standards-uk-applicability.md`.
- The AZT method's specific multi-panel blend chains are practitioner conventions consistent with the method, not verbatim AZT data (the source books blending generically); flagged in `azt-paint-method.md`.

## Verification

`python tools/verify_scaffold.py` green after regenerating the source manifest; `src/skills/infointake/` removed; each new skill has `SKILL.md` + `references/`; catalogue + README list all new skills; corpus README documents PII governance.

## Open follow-ups

Lifecycle substrate (versioning/eval/redaction) via `ai-platform/platform-tools`; tool wiring (Autotrader Codex, DVSA-MOT MCP) via `mcp-tooling`; render scripts for `repair-estimate`/`fee-note` (deferred); UK OEM equivalents; governance sign-off on role model + retention.
