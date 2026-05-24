# Codex Session Log — 2026-05-23 (18:07)

## User
*2026-05-23 17:08:34 UTC*

Do a detailed examination of originalplanning 

Is there anything in here that is not covered by either plans or tickets ?

Be thorough, examine every file.

Report back.

---

## Codex
*2026-05-23 17:13:36 UTC*

I examined the full `originalplanning` corpus: 143 on-disk files, including 138 Markdown files, 1 JSON manifest, and 4 ZIP archives. I also inspected the 56 Markdown members inside those ZIPs. I compared them against all 15 files under `docs/plans`, including `source_synthesis.md`, parser MVP, P0-P5 tickets, and implemented plan archives. No repo files were changed; `git status --short` is clean.

Short answer: no whole pack is orphaned, but yes, several specific workstreams are not adequately covered by active plans/tickets. Some are explicitly parked in source_synthesis.md; others are only implied by broad tickets.

**Clearest Gaps**
- **Estimate / ABP review tooling**: 12_audatex_estimate_parser_and_qa_assistant.md, 13_abp_charge_review_assistant.md, and 08_08_estimate_abp_review_pack.md. Current plans cover valuation and Audatex partnerships broadly, but not supplied-estimate parsing, line-item QA flags, ABP/rate context, or estimate review summaries as a workstream.
- **Knowledge base / clause RAG**: 22_knowledge_base_report_clause_rag_skill.md and 08_13_knowledge_base_and_standard_clause_rag.md. `source_synthesis` parks broad RAG/training, but there is no ticket for approved-source retrieval, clause drafting, source versioning, or role-limited access.
- **Model evaluation / feedback loop**: 25_model_evaluation_feedback_loop.md. P2 has a corpus regression harness, but not the fuller service described here: reviewer correction capture, model/prompt/parser version comparison, quality reports, and failure-category metrics.
- **Job Sheet / SharePoint spreadsheet bridge**: 20_job_sheet_spreadsheet_bridge_mcp.md. Current plans cover job-sheet replacement, provider migration, and optional metadata, but not a transitional read/write bridge, conditional-format checks, or controlled row export/update workflow.
- **Risk indicators / anomaly review**: 07_02_risk_indicators_and_review_scoring.md. Plans correctly avoid fraud conclusions, and some signals are covered via duplicate/image/analytics work, but there is no dedicated deterministic risk-indicator schema, dashboard, DPIA gate, or false-positive measurement ticket.
- **Historical search beyond duplicate detection**: 08_15_duplicate_case_and_historical_search.md and bulk-data prior-case material. Duplicate detection is partially covered; historical search UI, same-VRM prior case context, merge/link/split workflow, and prior total-loss review are not directly ticketed.
- **Continuous improvement programme**: 07_09_continuous_improvement_programme.md. The backlog index mentions continuous improvement, but there is no concrete ticket for ownership, feedback channels, weekly/monthly review cadence, improvement backlog, or release-note loop.

**Explicitly Parked, Not Missing**
These are covered only as parked/future scope, not as implementation tickets: weather/road-safety/traffic enrichment, predictive scheduling, external portal/API/payment automation, insurer/Audatex partner integrations, ANDIE, broad training/RAG, invoices, and data warehouse expansion.

**Covered Well**
The parser rebuild, provider config, work-item/review queue, Box package/live upload path, Outlook intake, EVA/Sentry export/import control, image/evidence matching, engineer pack generation, governance/security baseline, provider parity, and operations analytics are covered by the active P0-P5 structure.

---

## User
*2026-05-23 17:24:12 UTC*

Small task but with potential for a few changes.

Under plans we need a new subfolder for the initial repo setup and planning and documentation creation

so this is basically the FIRST step of the project before we even start writing any real code

Make sure you examine any files that would need changing as a result of this creation.

Create the relevant subfolders for this new folder

After this, set todos. You are to go through all reference and all originalplanning and testprojectcontext looking for anything we havent got formal planning for. Anything at all.

Just create a large plan file of every single potential idea, feature, or thing we can implement.

I dont want things "parked" - I want everything planned even if its a LONG way off.

source_synthesis.md has some stuff too

Be thorough in checking every single file

---

## Codex
*2026-05-23 17:38:35 UTC*

Implemented.

Created the new initial setup planning workspace under docs/plans/initial-repo-setup, with:

- documentation-scaffold/plan.md
- reference-audit/all-ideas-plan.md
- tickets/README.md
- `archived_plans/implemented/`
- `archived_plans/superseded/`

I moved the implemented repo setup/restructure planning records into the new setup archive, updated navigation, and regenerated `docs/source_manifest.*`.

The main output is all-ideas-plan.md. It records 160 planned items across S0-S6, based on a scan of 549 files under `docs/reference/`, including all 143 `originalplanning` files, all 43 `testprojectcontext` files, and source_synthesis.md.

I also changed active planning language away from “parked” dispositions: future/non-MVP work is now captured in the all-ideas ledger or marked long-range planned. Remaining `parked` hits are only in historical archived setup text or raw/normalized evidence wording.

Verification passed:

```powershell
python tools\verify_scaffold.py
python -m pytest tests\test_scaffold_contracts.py
python -m json.tool docs\repo_map.json
```

`verify_scaffold` passed and the targeted pytest run was `6 passed`.

---

## User
*2026-05-23 18:19:41 UTC*

Okay, begin by analyzing everything you gathered here. Now plan out all the different folders to go under plans and what will go in each one

Create a full plan for this and present.

Make sure everything is covered. Double check originalplanning in full

---

## User
*2026-05-23 18:24:01 UTC*

save the plan

Check further, dont we have plans for like an entirely new system that combines everything too? Where is this

---

## Codex
*2026-05-23 18:25:39 UTC*

Saved the plan here:

plans-folder-expansion-plan.md

I also updated `docs/source_manifest.md`, `.csv`, and `.json`, and `python tools\verify_scaffold.py` passes.

You were right about the “new system that combines everything.” The key sources are:

- phase_new_system.md - near-term integrated case-intake/management platform.
- phase_bespoke_system.md - Phase 6 bespoke end-to-end system.
- 00_README_PLAN_INDEX.md - explicitly says those are the same target platform at different maturity levels.
- 03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md - detailed mature single-platform plan.
- future_system_convergence.md - current active canonical summary.

I revised the saved plan to include `docs/plans/unified-platform/` as a first-class future workspace for that combined/bespoke platform, separate from the specialist folders.

---

## User
*2026-05-23 18:37:58 UTC*

okay, check even further then, thats a big fucking thing to miss

Are there any other areas/categories that should be included

---

## Codex
*2026-05-23 18:40:04 UTC*

Yes. I found more, and I updated the saved plan:

plans-folder-expansion-plan.md

Additional top-level planning areas now included:

- `docs/plans/parser-extraction/`
- `docs/plans/case-workflow-state/`
- `docs/plans/provider-principal-config/`
- `docs/plans/agentic-workflow-assistance/`
- `docs/plans/user-experience-interfaces/`
- `docs/plans/finance-billing/`

These were too important to leave buried under broader folders. The biggest ones were parser/extraction, case workflow/state, and provider/principal config. The original planning files treat those as major programme tracks, not just features.

I also added a “Further Category Audit” section explaining why those folders are needed. The saved taxonomy now includes the earlier `unified-platform/` folder for the full bespoke/new system, plus these more specific workstream folders.

Verification passed again:

```powershell
python tools\verify_scaffold.py
python -m pytest tests\test_scaffold_contracts.py
```

`verify_scaffold` passed and pytest was `6 passed`.

---

## User
*2026-05-23 18:41:36 UTC*

since parser-extraction is planned are you reworking operational-core as part of the plan?

---

## Codex
*2026-05-23 18:42:21 UTC*

Yes, but only lightly.

I updated the saved plan with an explicit Operational Core Rework Rule. It says:

- keep `docs/plans/operational-core/parser-mvp/plan.md` where it is for now
- keep P0-P3 Operational Core tickets in place
- update `source_synthesis.md` and tickets with pointers to `parser-extraction/`, `case-workflow-state/`, and `provider-principal-config/`
- avoid moving active parser MVP files until `parser-extraction/source_map.md` exists and the move will not break current implementation references

So: `operational-core/` stays the first executable delivery slice. `parser-extraction/` becomes the long-term planning owner for parser/extraction work, but the current MVP plan should not be moved prematurely.

I refreshed the manifest and `python tools\verify_scaffold.py` still passes.

---

## User
*2026-05-23 18:51:07 UTC*

# Diff comments:

## Comment 1
File: docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md
Side: R
Lines: 152
Diff hunk:
```diff
@@ -133,11 +147,12 @@
 4. Update `docs/plans/_index.md` with the full workspace table.
 5. Update `docs/docs_index.md` and `docs/repo_map.json` so humans and agents can route work by planning area.
 6. Add a workspace assignment section to `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md`.
-7. Update `docs/plans/operational-core/source_synthesis.md` so long-range items point to owning workspaces, especially `unified-platform/`.
-8. Keep existing `docs/plans/operational-core/tickets/p4-*` and `p5-*` files in place for now, but add pointers to the new owning workspaces for future split-out.
-9. Update `tools/verify_scaffold.py` so it checks required new planning folders, README files, archive folders, and source-map files.
-10. Update `tools/scaffold_initial_repo.py` so regenerated scaffold docs preserve the same folder taxonomy.
-11. Regenerate `docs/source_manifest.md`, `docs/source_manifest.csv`, and `docs/source_manifest.json`.
+7. Rework `docs/plans/operational-core/source_synthesis.md` lightly so long-range items point to owning workspaces, especially `unified-platform/`, `parser-extraction/`, `case-workflow-state/`, and `provider-principal-config/`.
+8. Keep existing `docs/plans/operational-core/parser-mvp/plan.md` and P0-P3 tickets in place for now; add pointers to new owning workspaces rather than moving active executable work.
+9. Keep existing `docs/plans/operational-core/tickets/p4-*` and `p5-*` files in place for now, but add pointers to the new owning workspaces for future split-out.
+10. Update `tools/verify_scaffold.py` so it checks required new planning folders, README files, archive folders, and source-map files.
+11. Update `tools/scaffold_initial_repo.py` so regenerated scaffold docs preserve the same folder taxonomy.
+12. Regenerate `docs/source_manifest.md`, `docs/source_manifest.csv`, and `docs/source_manifest.json`.
 
 ## Verification Plan
 
```
Comment:
no these should be split out now and any links/paths altered

## Comment 2
File: docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md
Side: R
Lines: 151
Diff hunk:
```diff
@@ -133,11 +147,12 @@
 4. Update `docs/plans/_index.md` with the full workspace table.
 5. Update `docs/docs_index.md` and `docs/repo_map.json` so humans and agents can route work by planning area.
 6. Add a workspace assignment section to `docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md`.
-7. Update `docs/plans/operational-core/source_synthesis.md` so long-range items point to owning workspaces, especially `unified-platform/`.
-8. Keep existing `docs/plans/operational-core/tickets/p4-*` and `p5-*` files in place for now, but add pointers to the new owning workspaces for future split-out.
-9. Update `tools/verify_scaffold.py` so it checks required new planning folders, README files, archive folders, and source-map files.
-10. Update `tools/scaffold_initial_repo.py` so regenerated scaffold docs preserve the same folder taxonomy.
-11. Regenerate `docs/source_manifest.md`, `docs/source_manifest.csv`, and `docs/source_manifest.json`.
+7. Rework `docs/plans/operational-core/source_synthesis.md` lightly so long-range items point to owning workspaces, especially `unified-platform/`, `parser-extraction/`, `case-workflow-state/`, and `provider-principal-config/`.
+8. Keep existing `docs/plans/operational-core/parser-mvp/plan.md` and P0-P3 tickets in place for now; add pointers to new owning workspaces rather than moving active executable work.
+9. Keep existing `docs/plans/operational-core/tickets/p4-*` and `p5-*` files in place for now, but add pointers to the new owning workspaces for future split-out.
+10. Update `tools/verify_scaffold.py` so it checks required new planning folders, README files, archive folders, and source-map files.
+11. Update `tools/scaffold_initial_repo.py` so regenerated scaffold docs preserve the same folder taxonomy.
+12. Regenerate `docs/source_manifest.md`, `docs/source_manifest.csv`, and `docs/source_manifest.json`.
 
 ## Verification Plan
 
```
Comment:
no,  refactor as needed

## Comment 3
File: docs/plans/initial-repo-setup/documentation-scaffold/plans-folder-expansion-plan.md
Side: R
Lines: 138
Diff hunk:
```diff
@@ -125,6 +125,20 @@
 
 Governance-gated areas must start in `option-papers/`, not `tickets/`: cloud OCR, external APIs, portal/payment automation, WhatsApp send automation, valuation providers, DVLA/DVSA, Audatex partnerships, AI/RAG, and EVA/Sentry submit.
 
+## Operational Core Rework Rule
+
+Creating `parser-extraction/` does require a small rework of `docs/plans/operational-core/`, but not a wholesale restructure.
+
+The first pass should:
+
+1. keep `docs/plans/operational-core/parser-mvp/plan.md` where it is, because it is the current executable parser MVP plan;
+2. keep P0-P3 Operational Core tickets where they are, because they define the first implementation slice;
+3. update `docs/plans/operational-core/source_synthesis.md` to point parser-specific long-range work to `docs/plans/parser-extraction/`;
+4. add cross-links in Operational Core tickets where parser, provider-config, or case-state work has a future owning workspace;
+5. avoid moving parser MVP files until `parser-extraction/source_map.md` exists and the move can be done without breaking current implementation references.
+
+After that first pass, a later migration may move completed or long-range parser planning into `parser-extraction/`, but active executable parser MVP work should stay under Operational Core until the MVP implementation is complete or explicitly superseded.
+
 ## Implementation Steps For This Taxonomy
 
 1. Create the new top-level workspace folders listed above.
```
Comment:
plan out the move for this and implement in this plan

## My request for Codex:
address the comments. 

Also, what is the difference between parser extraction and the operational core?

Advise me on this, also note the difference in the plan

---

## Codex
*2026-05-23 18:53:30 UTC*

Addressed in the saved plan:

plans-folder-expansion-plan.md

I removed the “keep it in Operational Core for now” approach. The plan now says to split the active files now, including moving:

- `operational-core/parser-mvp/plan.md` to `parser-extraction/parser-mvp/plan.md`
- parser tickets to `parser-extraction/`
- provider/principal tickets to `provider-principal-config/`
- work item/review queue tickets to `case-workflow-state/`
- P3 integration tickets to `intake-storage-integrations/`
- P4/P5 tickets into their real owning workspaces

I also added the distinction in the plan:

`parser-extraction/` owns how files become structured, source-linked parser output: triage, extraction adapters, mapper compatibility, OCR fallback, field mapping, parser warnings, regression corpus, parser UI/CLI behavior.

`operational-core/` owns the first end-to-end operating slice and coordination: source synthesis, dependency sequencing, how parser output moves through work item state, review gates, export/package readiness, and cross-workspace delivery. It should consume parser output, not own parser internals.

Verification passed after the edit:

```powershell
python tools\verify_scaffold.py
python -m pytest tests\test_scaffold_contracts.py
```

`pytest` result: `6 passed`.

---

## User
*2026-05-23 19:19:19 UTC*

Are there automation plans in this? 

AI Agent plans?

MCP plans?

Agent Skills plans?

Explain whats there, add whats missing

---

## Codex
*2026-05-23 19:26:25 UTC*

Yes. They were present in the source material, but not explicit enough in the plan taxonomy.

I updated the plan so these now have first-class homes:

- Automation: `docs/plans/automation-centre/`
- AI agents: `docs/plans/ai-agents/`
- MCP/tooling: `docs/plans/mcp-and-tooling/`
- Agent skills: `docs/plans/agent-skills/`

I also added a clear boundary note: automation runs fixed workflows; MCP/tools expose narrow callable capabilities; agent skills draft/summarise/explain/retrieve/train; AI agents orchestrate approved tools and skills but must stop at approval boundaries.

Updated files include:
- plans-folder-expansion-plan.md
- all-ideas-plan.md
- source_synthesis.md
- docs/plans/_index.md
- repo_map.json
- scaffold verification/generation tooling updated to require these categories.

I expanded the all-ideas ledger to 177 planned items and added explicit rows for automation-centre work, AI agents, MCPs, and agent skills.

Verification run:
- `python tools\verify_scaffold.py` passed
- `python -m pytest tests\test_scaffold_contracts.py` passed: 6/6
- `python -m json.tool docs\repo_map.json` passed

---
