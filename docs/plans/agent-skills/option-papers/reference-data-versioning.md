# Option paper: reference-data versioning (ABP / ABI COP / AZT)

Date: 2026-05-29
Status: open
Group: agent-skills

## Problem

Several new shared references are **time-sensitive authorities** that the issuing bodies revise:

- `abp-rates` — ABP Club rate book; the bundled edition is **2026** (charges effective 1 Jan 2026). New edition expected annually.
- `salvage-categorisation` — ABI Code of Practice; bundled version **28.05.2025** (PDF labelled "V12 – Final, March 2025"). ABI revises periodically.
- `paint-calculation` — AZT method (EN, 03 June 2020); AZT updates per-part time/material values continuously (index-based).

If these are silently overwritten, prior matters lose the basis they were assessed under, and outputs may quote stale figures.

## Options

1. **Versioned-alongside (recommended).** Keep each edition as a dated file (`abp-<year>-rates.md` + PDF; `abi-salvage-cop-<date>.md`), update the skill banner + the "canonical" pointer, and retain prior editions. Matters cite the edition in force at assessment.
2. Overwrite-in-place with git history only. Simpler, but the working tree only ever shows the latest; citing a superseded edition means digging through history.
3. External rates service. Out of scope now (no substrate); revisit with `ai-platform`.

## Recommendation

Option 1. Add a short "valid for / supersede on" banner to each reference (done for the 2026/2025 editions). On a new release: add the new dated file, repoint consumers, keep the old file, and note the change here.

## Owner / next step

Unassigned. Trigger: next ABP edition or ABI COP revision. Coordinate eval/versioning with `ai-platform/platform-tools` when that substrate exists.
