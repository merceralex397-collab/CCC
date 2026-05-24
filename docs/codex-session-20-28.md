# Codex Session Log — 2026-05-23 (20:28)

## User
*2026-05-23 19:31:20 UTC*

all-ideas-plan.md plans-folder-expansion-plan.md 

Scan these folders carefully. Do not use sub agents.

Set each item / folder / area as a todo

For each item that you work on, use brainstorming, and also interview me, ask any and all questions to clarify and scope the area exactly.

Ensure all areas and plans created by this process are aware of eachother as necessary. Ensure nothing is overlapping, contradictory, or otherwise an issue.

As the last phase, we need to create / update a full roadmap for all the ideas, grouping them into sprints / sections that will be worked on in sequential order.

This process must include all items planned and discussed unless I veto them during the interview process. You cannot create a plans subfolder without discussing and interviewing with me.

---

## Codex
*2026-05-23 19:33:29 UTC*

I’ve scanned the requested plan files and the active plan folders. Current inventory:

- 2 existing active plan workspaces: `initial-repo-setup`, `operational-core`
- 20 proposed new top-level planning workspaces
- 32 active Operational Core phase tickets to potentially split/move
- 177 all-ideas ledger rows across 28 domains
- No subagents used, and no files/folders changed

First scoping question: should I treat the 20 proposed workspaces in `plans-folder-expansion-plan.md` as the baseline taxonomy to interview one by one, or should I first challenge/rebuild that taxonomy from the 177 all-ideas ledger rows before accepting any proposed folder?

---

## User
*2026-05-23 19:35:13 UTC*

Clarify if there are any further things to add or if anything should be merged in - dont action any of this until i approve it thoguh

---

## Codex
*2026-05-23 19:35:40 UTC*

Yes. Initial clarification: the taxonomy is broadly good, but I would not approve it unchanged yet.

Likely things to clarify or add before action:

- **Architecture/contracts ownership**: not necessarily a new workspace, but we need a clear rule for who owns cross-cutting contracts, ADRs, and architecture updates after tickets move out of `operational-core`.
- **Migration/decommissioning**: spreadsheet replacement, legacy mapper retirement, Box-to-future-storage migration, and rollout/decommissioning appear in several places. This may need either a dedicated roadmap lane or explicit ownership under `unified-platform` plus `operations-quality`.
- **Knowledge/RAG**: report-clause RAG, internal knowledge base, training, and source-cited drafting are split across `agent-skills`, `ai-platform-tools`, and `engineer-communications`. We should decide whether this stays split or gets a named sub-area.
- **Access control/admin model**: roles, permissions, approval levels, provider admin, tool permissions, external partner access, and audit identity are scattered. Could remain under `governance-security`, but it needs explicit cross-links.
- **Testing/evaluation boundary**: parser regression, integration sandbox tests, AI evals, UI walkthroughs, and release gates span multiple workspaces. `operations-quality` can coordinate, but each domain still needs its own verification section.

Likely merge or boundary decisions:

- **Do not merge** `ai-agents`, `agent-skills`, `mcp-and-tooling`, and `ai-platform-tools`, but define their boundaries very tightly.
- **Do not merge** `parser-extraction` back into `operational-core`; the split is justified.
- **Potentially merge or subordinate** some `automation-centre` content under `unified-platform` unless we want automation patterns to be reusable across every domain.
- **Potential overlap** between `finance-billing` and `external-platform-partners` around portal/payment automation.
- **Potential overlap** between `engineer-communications` and `agent-skills` around chaser drafting, summaries, CE style, and report-clause support.
- **Potential overlap** between `governance-security` and `operations-quality`; policy vs operational verification must be clear.

The biggest structural issue is that there are two phase systems: `S0-S6` in the all-ideas ledger and `P0-P5` in Operational Core tickets. Before any roadmap rewrite, we should decide whether the final roadmap uses one unified sequence or keeps both with a translation table.

One question: do you want me to treat the current 20-workspace taxonomy as mostly accepted and only propose targeted adds/merges, or should I re-derive the taxonomy from the 177 ledger items and challenge every workspace before approval?

---

## User
*2026-05-23 19:37:33 UTC*

Try and re-derive

But propose this to me, dont action anything immediately

---

## Codex
*2026-05-23 19:38:19 UTC*

I’ll re-derive it, but only as a proposal/interview process. No files, folders, moves, or roadmap updates until you approve the final design.

**Proposed Re-Derivation Method**

1. Start from the 177 all-ideas ledger rows, not from the existing proposed folders.
2. Group rows by actual capability boundary: what system responsibility owns the work.
3. Assign exactly one primary planning owner per item.
4. Add supporting/cross-link owners where needed.
5. Check for overlaps, contradictions, missing areas, and phase conflicts.
6. Convert the result into a proposed roadmap sequence.
7. Bring the proposed taxonomy and roadmap back to you for approval before action.

**Three Possible Ways To Re-Derive**

**Option A: Lean Taxonomy**
Use fewer, larger workspaces. This would reduce folder sprawl, but some areas like AI agents, MCP tools, skills, and AI platform governance may become too mixed.

**Option B: Detailed Capability Taxonomy**
Keep more focused workspaces, but derive them from the ledger instead of accepting the current 20-folder proposal blindly. This is my recommendation because the source material has many distinct risk boundaries: parser, provider config, case state, integrations, AI agents, MCP tools, skills, governance, analytics, and partner systems should not blur together.

**Option C: Roadmap-First Taxonomy**
Do not settle folder structure first. Instead, build the sequential roadmap first, then create only the folders needed by near-term and medium-term work. This is cleaner short-term, but long-horizon ideas may stay harder to navigate.

**My Starting Recommendation**

Use **Option B**, but challenge the current taxonomy in these areas:

- Whether `finance-billing` and `external-platform-partners` should stay separate.
- Whether `knowledge/RAG/training` deserves a first-class planning area or remains split across `agent-skills`, `ai-platform-tools`, and `engineer-communications`.
- Whether `architecture/contracts/ADRs` need a planning coordination home or just stronger cross-links from existing docs.
- Whether migration/decommissioning should be explicit under `unified-platform`, `operations-quality`, or both.
- Whether `automation-centre` is truly a standalone reusable system, or just a pattern used by other workspaces.
- Whether `governance-security` needs an explicit access-control/admin sub-area.

Question: should I proceed with **Option A Lean**, **Option B Detailed Capability**, or **Option C Roadmap-First** for the re-derived proposal?

---

## User
*2026-05-23 19:39:32 UTC*

B

Explain all  the questions in more detail though

---

## Codex
*2026-05-23 19:40:17 UTC*

Using Option B, these are the questions I’ll use to re-derive the taxonomy. You do **not** need to answer all at once; I’ll interview one area at a time.

**1. Should This Be A Top-Level Workspace?**
For each capability, we need to decide whether it deserves its own `docs/plans/<area>/` folder.

This matters because a top-level workspace means the area has enough independent planning weight: its own roadmap, source map, tickets, option papers, archive, and ownership boundary.

Example: `parser-extraction` clearly looks top-level because it owns document parsing, OCR fallback, provider extraction behaviour, regression fixtures, and UI/CLI parser parity. Something smaller might just be a section inside another workspace.

**2. What Is The Primary Owner?**
Every idea should have exactly one primary planning home.

This prevents duplicate active tickets. For example, “missing-info chaser drafting” could belong to `engineer-communications`, `agent-skills`, `ai-agents`, or `case-workflow-state`. We need to choose the primary owner and then cross-link the others.

The rule I’d propose is: the owner is the workspace responsible for the artifact that would be built or changed first.

**3. What Are Supporting Workspaces?**
Some work needs cross-links without duplicating ownership.

Example: DVLA/DVSA vehicle intelligence might primarily belong to `vehicle-valuation-data`, but it also needs `governance-security` for licensing/privacy, `mcp-and-tooling` if exposed as a tool, and `analytics-data-platform` if later used in bulk analysis.

This question decides what each workspace needs to be aware of.

**4. Is This Automation, Tooling, Skill, Or Agent Work?**
This is one of the most important boundary questions.

- `automation-centre`: deterministic workflow steps, queues, retries, events, routing.
- `mcp-and-tooling`: callable tools/adapters with schemas, auth, audit, rate limits.
- `agent-skills`: reusable drafting, summarising, explaining, training, RAG behaviours.
- `ai-agents`: orchestrators that choose tools/skills and propose actions under approval controls.
- `ai-platform-tools`: model/prompt/eval/redaction infrastructure behind the above.

A bad split here would make later AI work unsafe and hard to verify.

**5. Is This Product Workflow Or Platform Infrastructure?**
Some items are direct CCC workflow features; others are platform support.

Example: “case review queue” is product workflow. “tool registry and MCP security gateway” is platform infrastructure. “model evaluation loop” is AI platform infrastructure.

This matters for roadmap sequencing: workflow features usually come first, platform abstractions only when they unblock multiple domains.

**6. Is This Near-Term, Medium-Term, Or Governance-Gated?**
The existing files use `S0-S6` and `P0-P5`. We need a unified sequencing model.

Some areas can be planned now but not built until governance is approved: cloud OCR, WhatsApp send automation, external APIs, payment automation, valuation providers, DVLA/DVSA, Audatex, partner portals, AI/RAG.

The question is whether those live as `tickets/` or `option-papers/` first. My default: governance-gated work starts as option papers.

**7. Is There A Merge Candidate?**
Some proposed folders may be separate only because the source material named them separately.

Potential merge questions:
- Should `finance-billing` stay separate from `external-platform-partners`, or is it mostly portal/payment partner work?
- Should `automation-centre` stay standalone, or become a pattern within `unified-platform` and `operations-quality`?
- Should `product-business` be top-level, or part of roadmap/governance/discovery docs?
- Should knowledge/RAG/training be a first-class workspace, or distributed across `agent-skills`, `ai-platform-tools`, and `engineer-communications`?

**8. Is There A Missing Workspace?**
The current 20-workspace proposal may still miss something.

Possible missing areas:
- `architecture-contracts-decisions`: if cross-cutting ADRs/contracts become too hard to coordinate.
- `migration-decommissioning`: if spreadsheet replacement, legacy mapper retirement, Box migration, and rollout need one owner.
- `knowledge-rag-training`: if source-linked report clauses, internal guidance, training, and retrieval become too large for `agent-skills`.

I’m not saying these should be added yet; these are candidates to test.

**9. What Must Not Be Mixed?**
Some boundaries should be strict.

Examples:
- Parser output must not become EVA’s internal data model.
- AI must not make expert engineering conclusions.
- Portal/payment metadata capture must not imply payment automation approval.
- Review drafts must not imply autonomous sending.
- Box-ready packaging must not imply live Box upload.
- Provider config editing must not silently change active parser behaviour without version/audit gates.

This question catches contradictions early.

**10. What Is The Sequential Roadmap Logic?**
The final roadmap needs to order work so later areas depend on real foundations.

A likely order is:
1. Repository/planning foundation.
2. Parser, provider config, contracts, private corpus.
3. Work item state, review queue, staff parser UI/CLI.
4. EVA export and Box-ready package.
5. Intake/storage/live integrations.
6. Engineer comms, valuation, image/estimate review.
7. Automation, MCP tools, agent skills, controlled AI agents.
8. Analytics, data warehouse, partner portals, finance/payment, mature platform.

We’ll refine this after the taxonomy is clear.

First interview question: should `architecture`, `contracts`, `ADRs`, and cross-workspace dependency rules remain in the existing shared `docs/architecture`, `docs/contracts`, and `docs/decisions` folders only, or should the re-derived taxonomy include a dedicated planning workspace for architecture/contracts/decisions coordination?

---

## User
*2026-05-23 19:40:45 UTC*

Okay, go one at a time, and explain each thing clearly with the supporting documents and information you can find

---

## Codex
*2026-05-23 19:41:25 UTC*

**Thing 1: Architecture, Contracts, ADRs**

This question is about whether we need a new planning workspace like:

`docs/plans/architecture-contracts-decisions/`

or whether architecture, contracts, and decisions should stay in the existing shared folders:

- docs/architecture
- docs/contracts
- docs/decisions

**What The Current Docs Say**

The current project already treats these as shared canonical outputs, not as one product area.

docs/plans/operational-core/source_synthesis.md lists:

- `docs/architecture/` for programme architecture, MVP interlock, governance, and future convergence.
- `docs/contracts/` for parser, work item, provider config, audit, package, EVA, storage, and extraction contracts.
- `docs/decisions/` for ADRs and option papers.

docs/architecture/programme_architecture.md defines the shared spine: intake, work item, provider config, parser, review, EVA export, package, audit, governance.

docs/architecture/mvp_interlock.md says contracts come first because parser, UI, CLI, review, and exports must share one model.

docs/architecture/future_system_convergence.md says future modules must attach to the same spine: work item, source files, parser result, review/audit events, provider config, package, and adapters.

docs/plans/operational-core/tickets/p0-foundation.md already has `P0-002 Contracts Baseline` and `P0-006 ADR And Option Paper Baseline`.

**The Tension**

Once we split work out of `operational-core`, many future workspaces will depend on these shared docs. For example:

- `parser-extraction` depends on parser result and extraction adapter contracts.
- `case-workflow-state` depends on work item and audit event contracts.
- `intake-storage-integrations` depends on EVA, storage, source, and package contracts.
- `ai-agents`, `mcp-and-tooling`, and `agent-skills` depend on governance, permissions, audit, and approval boundaries.

So we need a clear ownership rule. Otherwise every workspace may start editing shared architecture and contracts independently.

**Options**

**Option A: No New Workspace, Keep Shared Canonical Folders**

Architecture, contracts, and decisions stay where they are. Each planning workspace references them but does not own them. Cross-workspace changes are coordinated through `operational-core` early on, then `unified-platform` later.

This keeps the taxonomy cleaner and avoids creating a meta-workspace.

**Option B: Add `architecture-contracts-decisions` Workspace**

Create a dedicated planning home for architecture changes, contract evolution, ADR sequencing, and cross-workspace dependency management.

This is explicit, but it risks becoming a dumping ground for anything complicated.

**Option C: Hybrid Rule**

Do not create a new workspace now, but add a clear rule: shared architecture, contracts, and decisions remain in their existing folders, while each planning workspace must list which shared docs it depends on or proposes to change. `operational-core` coordinates near-term shared decisions; `unified-platform` coordinates mature system-wide convergence.

This is my recommendation.

It gives us coordination without adding another top-level workspace too early.

**Question 1**

For the re-derived taxonomy, should architecture/contracts/ADRs be handled as:

A. Existing shared folders only  
B. New `architecture-contracts-decisions` planning workspace  
C. Hybrid rule: shared folders stay, with explicit cross-workspace ownership/dependency rules under `operational-core` then `unified-platform`

---

## User
*2026-05-23 19:42:10 UTC*

C

---

## Codex
*2026-05-23 19:42:53 UTC*

Recorded proposed decision for Thing 1: **use the hybrid rule**. Architecture, contracts, and ADRs stay in `docs/architecture`, `docs/contracts`, and `docs/decisions`; planning workspaces must list dependencies/proposed changes to those shared docs.

**Thing 2: Operational Core After The Split**

The question is whether `docs/plans/operational-core/` remains a real planning workspace after we create specialist workspaces, or whether it should be replaced by the new folders.

**What The Current Docs Support**

docs/roadmap.md says the first programme milestone is the **Operational Core MVP**: parser, provider admin, work-item/review queue, EVA export, and Box-ready package.

README.md says the parser is the first executable MVP inside Operational Core, not the whole programme.

plans-folder-expansion-plan.md says `operational-core/` should become the **first-slice coordination workspace** after the split. It should retain source synthesis, roadmap/backlog coordination, MVP interlock, cross-workspace dependency sequencing, and truly cross-cutting P0 foundation items.

The same plan explicitly says it should **not** remain the physical home for parser, provider config, case-state, integration, UI, intelligence, analytics, or partner tickets once those owning workspaces exist.

**My Re-Derived View**

`operational-core` is not really a capability like parser, case workflow, or integrations. It is a **delivery slice**: the first usable end-to-end operating system.

So I would keep it, but make it thinner.

It should own:

- first MVP milestone definition;
- cross-workspace sequencing;
- dependency map between parser, provider config, case state, UI, EVA export, and packaging;
- source synthesis history;
- coordination backlog index;
- acceptance criteria for “Operational Core MVP is actually usable end to end.”

It should not own long-term detailed tickets for:

- parser internals;
- provider/principal configuration;
- case workflow state;
- intake/storage/EVA adapter implementation;
- staff UI design;
- analytics;
- AI tools;
- external partner systems.

Those should move to their primary planning workspaces when approved.

**Options**

A. Keep `operational-core` as the master workspace with most P0-P5 tickets inside it.  
This is simpler short term, but it keeps the overlap problem.

B. Keep `operational-core` as a slim coordination workspace.  
Domain tickets move to their real owners, while Operational Core tracks MVP sequencing and acceptance. This is my recommendation.

C. Retire `operational-core` after creating the new workspaces.  
This is too aggressive because the first MVP needs one place to coordinate the full end-to-end slice.

Question 2: should the re-derived taxonomy use **Option B**, keeping `operational-core` as a slim first-slice coordination workspace?

---

## User
*2026-05-23 19:43:38 UTC*

b

---

## Codex
*2026-05-23 19:44:05 UTC*

**Thing 3: Initial Repo Setup Workspace**

This question is whether `docs/plans/initial-repo-setup/` should stay as an active workspace after the taxonomy expansion, and what it should own.

**What The Current Docs Support**

docs/plans/initial-repo-setup/README.md says this workspace captures pre-product-code work:

- repository setup;
- documentation structure;
- source evidence handling;
- planning consolidation;
- exhaustive all-ideas backlog.

docs/plans/initial-repo-setup/documentation-scaffold/plan.md says it owns:

- repository hygiene;
- docs navigation and machine map;
- source manifest parity;
- raw evidence immutability;
- normalized companion conventions;
- reference pack classification;
- plan/ticket lifecycle rules;
- verification script coverage.

docs/plans/initial-repo-setup/reference-audit/all-ideas-plan.md has 12 `Repository setup` rows, including source safety, docs navigation, source manifest, raw evidence immutability, normalized companions, original planning preservation, test context preservation, plan lifecycle, all-ideas ledger, scaffold verification, provider coverage baseline, and ADR baseline.

The verifier tools/verify_scaffold.py currently hard-checks the setup docs, all-ideas plan, source manifest, planned workspace terms, parser plan coverage, and source-manifest integrity.

**My Re-Derived View**

`initial-repo-setup` should remain, but it should not become a permanent product planning home.

It should own:

- source evidence rules;
- source manifest integrity;
- documentation scaffold rules;
- plan lifecycle rules;
- all-ideas ledger until items are assigned to primary workspaces;
- verification/scaffold maintenance;
- taxonomy expansion planning until the expansion is implemented.

It should not own:

- parser implementation planning;
- provider config implementation;
- case workflow;
- AI/automation work;
- analytics;
- mature platform roadmap, except as source-capture before promotion.

Once the taxonomy is approved, the all-ideas ledger should gain a workspace assignment section. After that, `initial-repo-setup` becomes mostly a governance/scaffold maintenance area, not a place where product ideas keep accumulating forever.

**Potential Merge Or Change**

I do **not** think `initial-repo-setup` should merge into `operational-core`. They have different jobs:

- `initial-repo-setup` protects evidence, docs structure, manifests, and planning hygiene.
- `operational-core` coordinates the first usable MVP slice.

**Options**

A. Keep `initial-repo-setup` active long-term as the permanent source and planning hygiene workspace.  
Clear and safe, but it may stay too central.

B. Keep it active through taxonomy expansion, then narrow it to scaffold/source-manifest/reference-audit maintenance.  
This is my recommendation.

C. Archive most of it after taxonomy expansion and move all-ideas ownership elsewhere.  
This risks losing the capture point for unpromoted reference ideas.

Question 3: should the re-derived taxonomy use **Option B**, keeping `initial-repo-setup` but narrowing it after expansion to scaffold, source, manifest, lifecycle, and unpromoted reference-audit maintenance?

---

## User
*2026-05-23 19:44:49 UTC*

B

---

## Codex
*2026-05-23 19:45:42 UTC*

**Thing 4: Unified Platform**

This question is whether `docs/plans/unified-platform/` should exist as a top-level planning workspace, and what it should own.

**What The Supporting Docs Say**

plans-folder-expansion-plan.md explicitly says the “new system that combines everything” is real and should not be hidden inside domain folders.

The main source docs are:

- phase_new_system.md: near-term integrated case-intake and management platform.
- phase_bespoke_system.md: long-term bespoke end-to-end system.
- 00_README_PLAN_INDEX.md: says those two plans overlap and describe the same target platform at different maturity levels.
- 03_PHASE_6_BESPOKE_PLATFORM_ENHANCED.md: mature platform plan.
- docs/architecture/future_system_convergence.md: active canonical convergence spine.

The enhanced index is important: it says Phase 2 builds the operating core, and Phase 6 expands and hardens that core rather than rebuilding it.

**What Unified Platform Would Own**

This workspace would not own every domain ticket. Instead, it would own the **system-wide target shape**:

- mature end-to-end case management platform;
- how all specialist workspaces converge into one product;
- migration from spreadsheet/mapper/Box/manual workflow into CCC;
- platform-level role model and lifecycle;
- system-wide roadmap after Operational Core;
- legacy decommissioning criteria;
- architecture convergence and rollout sequencing.

It would coordinate specialist workspaces like:

- `parser-extraction`
- `case-workflow-state`
- `provider-principal-config`
- `intake-storage-integrations`
- `user-experience-interfaces`
- `engineer-communications`
- `operations-quality`
- `analytics-data-platform`

**What It Should Not Own**

It should not become a duplicate ticket home for every feature.

For example:

- Parser internals belong in `parser-extraction`.
- Work item states belong in `case-workflow-state`.
- Box/EVA/Outlook adapters belong in `intake-storage-integrations`.
- Engineer PWA screens belong in `user-experience-interfaces`, with engineer workflow links.
- Runbooks and rollout tests belong in `operations-quality`.

Unified Platform should explain how those parts become one mature platform.

**Main Risk**

The risk is overlap with `operational-core`.

My proposed boundary:

- `operational-core`: first usable MVP slice.
- `unified-platform`: mature system target and migration/decommissioning roadmap.

So Operational Core asks: “What must work first?”  
Unified Platform asks: “What does the full system become, and how do we retire the legacy workflow safely?”

**Options**

A. Create `unified-platform` as a top-level coordination workspace for mature system convergence.  
This is my recommendation.

B. Do not create it; keep mature platform planning split across specialist workspaces.  
This avoids one more folder, but loses the “whole system” view.

C. Merge it with `operational-core`.  
This would blur first MVP scope with long-term platform ambition.

Question 4: should the re-derived taxonomy include `docs/plans/unified-platform/` as a top-level workspace for mature platform convergence, migration, and legacy decommissioning, with specialist work remaining in their owning workspaces?

---

## User
*2026-05-23 19:46:16 UTC*

A

---

## Codex
*2026-05-23 19:47:01 UTC*

**Thing 5: Automation Centre**

This question is whether `docs/plans/automation-centre/` should remain a top-level workspace, or whether its content should be absorbed into `unified-platform`, `case-workflow-state`, `intake-storage-integrations`, and `operations-quality`.

**What The Supporting Docs Say**

Automation Centre Operating Model frames the workflow as the first capability in a broader automation centre. It names reusable platform capabilities:

- intake connectors;
- document services;
- workflow engine;
- integration adapters;
- governance and audit;
- observability;
- operating cadence;
- automation KPIs.

phase_initial_automation.md focuses on immediate automation: mapper upgrade, Outlook inbox automation, EVA/Sentry interaction, Box upload, and replacing the spreadsheet with a structured database.

Agent vs Automation Decision Framework gives the key boundary:

- deterministic automation for clear triggers, inputs, outputs, and rules;
- AI assistance for messy classification, summarisation, drafting, semantic matching;
- controlled agents only when the system chooses among approved tools and stops at permission boundaries.

Workflow States and Orchestration adds state machines, queues, idempotency, retry strategy, reconciliation, audit events, config management, and failure visibility.

The all-ideas ledger has three `Automation centre` rows:

- reusable automation-centre operating model;
- workflow orchestration and retry engine;
- automation-vs-agent promotion rules.

**My Re-Derived View**

`automation-centre` is a valid top-level workspace, but only if we keep it focused on **reusable deterministic automation patterns**, not domain features.

It should own:

- workflow engine patterns;
- trigger/event model;
- queue/retry/idempotency standards;
- exception routing;
- reconciliation jobs;
- automation KPIs;
- operating cadence;
- automation-vs-agent decision rules;
- reusable automation service boundaries.

It should not own:

- Outlook adapter details: `intake-storage-integrations`;
- parser internals: `parser-extraction`;
- work item states themselves: `case-workflow-state`;
- live Box/EVA adapter details: `intake-storage-integrations`;
- runbook execution/testing: `operations-quality`;
- AI orchestration: `ai-agents`;
- callable tool schemas: `mcp-and-tooling`.

**Overlap Risk**

The overlap risk is real. `unified-platform` also talks about workflow engine and system-wide orchestration. My proposed distinction:

- `unified-platform`: product/system convergence and mature platform roadmap.
- `automation-centre`: reusable automation mechanics and operating model.

So unified platform asks: “How does the whole product fit together?”  
Automation centre asks: “How do automated workflows run safely and predictably?”

**Options**

A. Keep `automation-centre` as a top-level workspace for reusable deterministic automation architecture.  
This is my recommendation.

B. Merge automation into `unified-platform`.  
This reduces folders, but makes automation rules less reusable across domains.

C. Do not create it; distribute automation into each domain workspace.  
This would likely cause inconsistent retry, idempotency, exception, and audit patterns.

Question 5: should the re-derived taxonomy include `docs/plans/automation-centre/` as a top-level workspace for deterministic automation patterns, workflow orchestration, retries, idempotency, exception routing, and automation-vs-agent rules?

---

## User
*2026-05-23 19:47:22 UTC*

A

---

## Codex
*2026-05-23 19:48:07 UTC*

**Thing 6: Parser Extraction**

This question is whether `docs/plans/parser-extraction/` should be a top-level workspace, and what it should own after being split out of `operational-core`.

**What The Supporting Docs Say**

The current parser MVP lives at docs/plans/operational-core/parser-mvp/plan.md. It covers:

- file triage and classification;
- PDF, DOCX, legacy DOC, MSG, EML, images, batch folders;
- provider detection and mapping-rule engine;
- all 26 provider presets;
- canonical parser result with provenance/confidence/warnings;
- UI/CLI parity;
- EVA JSON export gate;
- private corpus golden tests.

ADR 0004 says the parser is a ground-up compatible rebuild. The legacy mapper is behavioural evidence, not architecture to import wholesale.

ADR 0007 says the parser is deterministic first. OCR, cloud document intelligence, and AI extraction are fallback/future adapters.

parser_result_v1.md says parser output is canonical before EVA-specific export. EVA JSON must not become the internal model.

extraction_adapter_contract_v1.md defines extraction adapters for PDF, DOCX, DOC, MSG, EML, images, and batch folders, with provenance and warning requirements.

plans-folder-expansion-plan.md already proposes the boundary: if the question is “how do we read/classify/extract/map this document?”, it belongs in `parser-extraction`.

**My Re-Derived View**

`parser-extraction` should definitely be a top-level workspace.

It should own:

- parser MVP plan;
- file triage/classification;
- extraction adapters and adapter IR;
- provider detection mechanics;
- mapping-rule engine behaviour;
- parser warnings/blockers;
- parser result contract dependencies;
- parser CLI parity;
- private corpus/golden parser regression;
- OCR/cloud-document-intelligence option papers from the parser perspective;
- legacy CE Document Mapper behaviour preservation.

It should not own:

- provider/principal business configuration lifecycle: `provider-principal-config`;
- staff UI product design: `user-experience-interfaces`;
- work item state/review queue: `case-workflow-state`;
- EVA/Sentry submission adapter: `intake-storage-integrations`;
- live Box upload: `intake-storage-integrations`;
- model evaluation/prompt governance for AI assistance: `ai-platform-tools`.

**Important Boundary Detail**

There is one tricky overlap: provider rules.

My proposed split:

- `parser-extraction` owns **how rules execute**: labels, offsets, regex, transforms, source evidence, warnings.
- `provider-principal-config` owns **what the active provider/principal/garage configuration contains**: aliases, contacts, routing metadata, activation, rollback, admin UI, coverage gaps.

**Options**

A. Create `parser-extraction` as a top-level workspace and move parser-specific active plans/tickets there.  
This is my recommendation.

B. Keep parser planning in `operational-core` until MVP is complete, then split later.  
Simpler short term, but it preserves the current overlap.

C. Split parser more narrowly into “document extraction” and “provider mapping.”  
Too much fragmentation right now; provider config can handle the business-config side.

Question 6: should the re-derived taxonomy include `docs/plans/parser-extraction/` as a top-level workspace for parser internals, extraction adapters, mapping execution, parser CLI parity, and parser regression coverage?

---

## User
*2026-05-23 19:48:30 UTC*

A

---

## Codex
*2026-05-23 19:49:19 UTC*

**Thing 7: Case Workflow State**

This question is whether `docs/plans/case-workflow-state/` should be a top-level workspace, and what it owns versus UI, integrations, automation, and communications.

**What The Supporting Docs Say**

plans-folder-expansion-plan.md says case workflow/state appears repeatedly as the operational spine: work item state store, holding pen, review queue, audit trail, missing-info state, duplicate/historical search, and job-sheet replacement.

The all-ideas ledger has 13 `Work items` rows, including:

- canonical work item store;
- work item state machine;
- holding pen and review queue;
- human approval and exception SLA;
- missing-information checklist/state machine;
- audit event stream;
- case association hierarchy;
- duplicate case service;
- historical search UI;
- merge/link/split workflow;
- job-sheet replacement;
- spreadsheet bridge.

work_item_contract_v1.md defines the work item as the case candidate moving from uploaded evidence to reviewed EVA export and Box-ready package. It also defines lifecycle states and validation gates.

review_audit_event_contract_v1.md defines append-only audit events for corrections, warnings, provider changes, exports, package generation, integration attempts, and status changes.

08_01_work_item_state_store_and_job_sheet_replacement.md says the state store should become the central operational record replacing the job sheet as system of record.

08_04_human_review_queue_and_exception_sla.md says no weak or ambiguous data should silently reach EVA, partner updates, report drafting, or engineer packs.

08_15_duplicate_case_and_historical_search.md defines duplicate signals, confidence levels, historical search, and merge/link/split audit controls.

**My Re-Derived View**

`case-workflow-state` should be a top-level workspace. It owns the operational spine once a case/work item exists.

It should own:

- work item lifecycle and state machine;
- holding pen/review queue behaviour;
- missing-info checklist and missing-info state transitions;
- human approval and exception SLA;
- audit event stream from the workflow perspective;
- duplicate case service;
- historical search workflow;
- merge/link/split decisions;
- job-sheet replacement logic;
- spreadsheet bridge requirements from the workflow perspective.

It should not own:

- visual UI layout of dashboards/review screens: `user-experience-interfaces`;
- parser extraction logic: `parser-extraction`;
- evidence/image intelligence logic: `evidence-estimate-review`;
- Outlook/Box/EVA adapters: `intake-storage-integrations`;
- retry/idempotency engine pattern: `automation-centre`;
- chaser wording/drafting: `engineer-communications` or `agent-skills`;
- analytics dashboards beyond workflow fields: `analytics-data-platform`.

**Important Boundary Detail**

There are two overlaps to handle carefully:

- Missing-info **state** belongs here. Missing-info **message drafting** belongs in communications/skills. Missing-info **sending automation** is governance-gated and likely later.
- Duplicate **case workflow** belongs here. Duplicate **image similarity/evidence reuse detection** belongs in `evidence-estimate-review`; broader risk analytics belongs later in `analytics-data-platform` and `governance-security`.

**Options**

A. Create `case-workflow-state` as a top-level workspace for work item state, review, audit, missing-info, duplicates, historical search, and job-sheet replacement.  
This is my recommendation.

B. Keep this inside `operational-core` until MVP is complete.  
Simpler initially, but it keeps the operational spine mixed with parser/integration details.

C. Merge it into `unified-platform`.  
This would blur concrete near-term workflow with mature platform convergence.

Question 7: should the re-derived taxonomy include `docs/plans/case-workflow-state/` as a top-level workspace for work item state, review/audit flow, missing-info state, duplicate/historical search, and job-sheet replacement?

---

## User
*2026-05-23 19:50:02 UTC*

A

---

## Codex
*2026-05-23 19:50:48 UTC*

**Thing 8: Provider Principal Config**

This question is whether `docs/plans/provider-principal-config/` should be a top-level workspace, and how it should split from parser extraction.

**What The Supporting Docs Say**

provider_principal_config_contract_v1.md says provider/principal configuration controls:

- provider detection;
- EVA principal values;
- case/PO reference sequencing;
- field mapping rules;
- provider-specific validation;
- activation, versioning, rollback, and audit.

It also includes optional routing metadata such as delivery channel, reply handling, CC list, fee-note handling, garage figures rules, chase limits, and special-case notes.

provider_coverage_matrix.md says there are:

- 26 parser provider presets;
- 50 job-sheet principal table codes;
- 20 actual job principal codes observed;
- actual job principal codes not parser-covered: `ACSP`, `OAK/AX`, `PRINCIPAL`, `WOODLANDS`.

Work Package 12 - Provider Settings and Migration says provider, principal, garage, and mapping configuration should move out of spreadsheets/JSON into a central audited admin area.

8.2 Provider and Principal Configuration Library says provider-specific differences are likely to be a major source of automation errors and should be configuration, not hardcoded logic.

Provider Mapping Assistant proposes a staff skill/tool to suggest and test provider mapping rules, but with approval and backup guardrails.

**My Re-Derived View**

`provider-principal-config` should be a top-level workspace.

It should own:

- provider/principal/garage configuration model;
- provider coverage matrix ownership after setup;
- 26 preset parity from a configuration perspective;
- uncovered principal triage;
- composite mapping cases like `OAK/AX`;
- provider admin UI requirements;
- versioning, activation, rollback, and audit;
- principal and garage migration;
- routing metadata;
- provider onboarding flow;
- provider mapping assistant planning from the config-management side.

It should not own:

- the parser engine that executes labels/offsets/regex: `parser-extraction`;
- general admin UI design system: `user-experience-interfaces`;
- outbound message drafting: `engineer-communications` or `agent-skills`;
- Outlook/Box/EVA adapter implementation: `intake-storage-integrations`;
- AI prompt/evaluation governance: `ai-platform-tools`.

**Important Boundary Detail**

Provider config will be used by many workspaces, but that does not mean those workspaces own it.

My proposed split:

- `provider-principal-config` owns the authoritative config records.
- `parser-extraction` consumes config for detection/mapping execution.
- `intake-storage-integrations` consumes config for Box/EVA/routing defaults.
- `engineer-communications` consumes config for report/chaser routing rules.
- `case-workflow-state` consumes config for required fields and review gates.

**Options**

A. Create `provider-principal-config` as a top-level workspace.  
This is my recommendation.

B. Keep provider config inside `parser-extraction`.  
This is tempting, but wrong long-term because provider config includes EVA, Box, routing, garages, contacts, and operational rules beyond parsing.

C. Put it inside `case-workflow-state`.  
This would overload the workflow spine with configuration lifecycle work.

Question 8: should the re-derived taxonomy include `docs/plans/provider-principal-config/` as a top-level workspace for provider/principal/garage configuration, coverage, admin, migration, routing metadata, versioning, and provider-rule lifecycle?

---

## User
*2026-05-23 19:51:13 UTC*

A

---

## Codex
*2026-05-23 19:52:10 UTC*

**Thing 9: Intake Storage Integrations**

This question is whether `docs/plans/intake-storage-integrations/` should be a top-level workspace, and what it owns versus workflow, MCP/tooling, external partners, and finance.

**What The Supporting Docs Say**

The all-ideas ledger has a large S3 integration cluster:

- manual upload and batch intake;
- Outlook Graph intake connector;
- mailbox monitoring and polling fallback;
- separate image email correlation;
- website repair-estimate intake boundary;
- WhatsApp evidence/status channel;
- Box-ready evidence package;
- Box metadata and folder design;
- live Box upload adapter;
- closed-file backup/archive;
- CCC-owned storage decision;
- EVA JSON export adapter;
- EVA/Sentry API adapter;
- payload preview and supervised submit;
- spreadsheet bridge.

p3-integrations-storage-eva-intake.md currently groups Outlook intake, live Box upload, website/payment intake boundary, EVA/Sentry adapter, and CCC-owned storage decision.

future_system_convergence.md says Outlook intake should create work items and source manifests without bypassing review. It also says website/payment evidence and WhatsApp context should be recorded as metadata first, not automation approval.

evidence_package_contract_v1.md defines the local Box-ready evidence package and manifest, including original files, images, EVA export, portal/payment metadata, and Box references.

storage_adapter_contract_v1.md says the first storage deliverable is package-only; live Box upload is a later adapter using the same package shape.

eva_export_contract_v1.md says direct Sentry/EVA API submission is future work and must validate token handling, schema, duplicate prevention, failure recovery, and manual approval.

Work Package 07 - Outlook Intake and Communications covers mailbox model, Graph intake, deterministic email classification, related-email correlation, duplicate detection, chaser drafting, approval gate, and communication audit.

Work Package 08 - Box Storage and File Handling covers Box folder structure, metadata, checksums, original file preservation, generated files, image handling, and failure recovery.

**My Re-Derived View**

`intake-storage-integrations` should be a top-level workspace.

It should own:

- intake adapter planning: manual upload boundary, Outlook Graph, polling fallback, website/portal metadata, WhatsApp evidence capture boundary;
- storage adapter planning: Box-ready package, live Box upload, Box metadata, closed-file backup/archive, future storage decision inputs;
- EVA/Sentry integration planning: EVA JSON export adapter, supervised submit, API adapter, token/failure/duplicate controls;
- spreadsheet bridge integration from the adapter side;
- source manifests and adapter metadata contracts;
- integration sandbox planning in coordination with `operations-quality`.

It should not own:

- work item state machine: `case-workflow-state`;
- queue/retry/idempotency standards: `automation-centre`;
- MCP wrappers for tools/agents: `mcp-and-tooling`;
- external partner/customer portal product: `external-platform-partners`;
- payment automation/finance approvals: `finance-billing`;
- chaser wording and drafting: `engineer-communications` or `agent-skills`;
- integration runbooks and rollout QA: `operations-quality`.

**Important Boundary Details**

Two splits matter here:

- **Adapter vs MCP wrapper**: this workspace owns the business integration adapter. `mcp-and-tooling` owns callable MCP/tool surfaces around those adapters for agents or internal tools.
- **Evidence capture vs automation approval**: website/payment/WhatsApp data can be recorded as source metadata here, but autonomous portal/payment/WhatsApp action belongs later and is governance-gated.

**Options**

A. Create `intake-storage-integrations` as a top-level workspace for intake channels, storage adapters, EVA/Sentry integration, website/WhatsApp metadata boundaries, and spreadsheet bridge adapter work.  
This is my recommendation.

B. Split it into separate `intake`, `storage`, and `eva-sentry` workspaces.  
This may be too fragmented now; these integrations all attach to the same first operational spine.

C. Keep it under `operational-core` until live integrations begin.  
This keeps the current P3 shape but leaves a lot of future integration work without a durable home.

Question 9: should the re-derived taxonomy include `docs/plans/intake-storage-integrations/` as a top-level workspace for intake, Box/storage, EVA/Sentry, website/WhatsApp metadata boundaries, and spreadsheet bridge adapter planning?

---

## User
*2026-05-23 19:52:31 UTC*

A

---

## Codex
*2026-05-23 19:53:19 UTC*

**Thing 10: Evidence Estimate Review**

This question is whether `docs/plans/evidence-estimate-review/` should be a top-level workspace, and how it splits from case workflow, intake, valuation, and engineer communications.

**What The Supporting Docs Say**

The all-ideas ledger has dedicated `Evidence` and `Estimates` rows:

- evidence matching service;
- image ordering and preview selection;
- image quality checker;
- visible VRM image matcher;
- duplicate image and reused evidence review;
- damage review workbench extension;
- Audatex estimate parser;
- estimate QA flag rules;
- ABP retail/non-contract charge review;
- Audatex/estimating-system partnership discovery.

Image Evidence Quality and Schedule Checker focuses on whether images are present, usable, correctly ordered for EVA, and sufficient for engineer review.

Visible VRM and Image Case Matcher focuses on using visible registrations and image metadata as review hints for matching photos to cases.

Evidence Matcher and Duplicate Detector defines matching documents, images, estimates, emails, and notes into the correct work item, with visible reasons and human approval for ambiguous matches.

8.7 Image Quality and Required Photo Coverage Assistant says to start with manual tagging, then add lightweight checks and image-to-case matching.

8.8 Estimate and ABP Review Pack says estimate review supports but does not replace technical judgement, and should parse supplied estimate files only.

evidence_package_contract_v1.md defines image ordering and package manifest requirements, but it does not own the review intelligence around image quality or estimates.

**My Re-Derived View**

`evidence-estimate-review` should be a top-level workspace.

It should own:

- evidence matching service logic;
- image ordering and preview-selection rules from a review perspective;
- required image category checklist;
- image quality and duplicate/reused evidence flags;
- visible VRM image matching hints;
- estimate/Audatex parsing of supplied files;
- estimate QA flag taxonomy;
- ABP/rate-context review pack;
- ANDIE-style damage workbench as a long-horizon option paper.

It should not own:

- basic file intake/storage: `intake-storage-integrations`;
- parser file triage and metadata adapters: `parser-extraction`;
- case state/merge/link/split workflow: `case-workflow-state`;
- valuation evidence/MOT/DVLA: `vehicle-valuation-data`;
- engineer pack assembly and communications: `engineer-communications`;
- external Audatex partnerships: `external-platform-partners`;
- fraud/risk scoring language: `governance-security` and later `analytics-data-platform`.

**Important Boundary Detail**

Evidence matching overlaps with case workflow. My proposed split:

- `evidence-estimate-review` owns the scoring/flags/reasons for “this evidence may belong to this case” or “this image/estimate has an issue.”
- `case-workflow-state` owns the human decision workflow: approve, reject, link, merge, split, dismiss, audit.

Estimate review also overlaps with engineer judgement. The boundary should be explicit: flags and summaries are allowed; final technical conclusion stays human/engineer-approved.

**Options**

A. Create `evidence-estimate-review` as a top-level workspace.  
This is my recommendation.

B. Merge image/evidence review into `case-workflow-state` and estimate review into `vehicle-valuation-data`.  
This reduces folders but mixes review intelligence with workflow state and valuation.

C. Keep it as a later section under `engineer-communications`.  
This undervalues evidence/estimate review as a distinct technical review area.

Question 10: should the re-derived taxonomy include `docs/plans/evidence-estimate-review/` as a top-level workspace for evidence matching, image review, image ordering, duplicate/reused evidence flags, supplied estimate parsing, ABP review packs, and long-horizon damage workbench planning?

---

## User
*2026-05-23 19:53:24 UTC*

A

---

## Codex
*2026-05-23 19:54:21 UTC*

**Thing 11: Vehicle Valuation Data**

This question is whether `docs/plans/vehicle-valuation-data/` should be a top-level workspace, and what belongs there versus estimate review, analytics, MCP tools, and human valuation judgement.

**What The Supporting Docs Say**

future_system_convergence.md says valuation support should store valuation evidence and companion reports, with **no automatic uplift decisions** without reviewer approval. It also says mileage/DVLA/DVSA support should cache factual vehicle/mileage evidence and expose confidence/conflicts.

p4-intelligence-engineer-communications.md currently has two relevant tickets:

- `P4-001 Valuation Evidence Support`
- `P4-002 DVLA/DVSA And Mileage Evidence`

Valuation, Vehicle Data and Uplift Evidence says this should be renamed from “Valuation and Uplift Agent” to **Valuation Evidence Assistant**. It explicitly says the system should gather evidence, draft notes, and require reviewer acceptance, not decide final value.

DVLA VRM Attribute Cache covers vehicle identity facts: make, colour, fuel type, engine, tax/MOT status, registration date, mismatch flags.

Mileage Estimation Engine says MOT-based mileage is evidence-backed estimation, not verified dashboard mileage, and should never overwrite verified mileage.

Market Valuation Evidence Store says valuation lookups should preserve source, date, mileage used, raw response, licence restrictions, and final human approval.

The all-ideas ledger includes vehicle/valuation rows for:

- DVLA VRM attribute cache;
- DVSA MOT bulk/delta ingestion;
- vehicle identity normalization;
- mileage estimation;
- mileage anomaly review;
- maintenance/condition score;
- MOT failure pattern intelligence;
- prior total loss/previous claim review;
- market valuation evidence store;
- valuation evidence assistant;
- valuation explanation/dispute response;
- salvage benchmarking.

**My Re-Derived View**

`vehicle-valuation-data` should be a top-level workspace.

It should own:

- DVLA/DVSA vehicle fact enrichment;
- MOT history and mileage evidence;
- mileage estimation and anomaly review;
- vehicle identity normalization;
- valuation evidence store;
- salvage benchmarking;
- prior total loss / previous same-VRM context;
- valuation evidence assistant requirements from the domain side;
- governance-gated valuation provider option papers;
- source-backed valuation explanation data requirements.

It should not own:

- supplied estimate/Audatex parsing: `evidence-estimate-review`;
- final valuation judgement: human/engineer process, guarded by `governance-security`;
- valuation explanation prompt/skill lifecycle: `agent-skills`;
- valuation/uplift orchestration agent: `ai-agents`;
- DVLA/DVSA MCP wrapper/tool interface: `mcp-and-tooling`;
- licensing/vendor approval: `governance-security`;
- bulk BI/data warehouse: `analytics-data-platform`.

**Boundary Detail**

Weather, road-safety, and traffic context appear in the bulk-data plans. I would **not** put them in the core `vehicle-valuation-data` roadmap by default. They are long-horizon contextual enrichment and should probably start as S6 option papers under `analytics-data-platform`, cross-linked here only if they directly support case/vehicle review.

**Options**

A. Create `vehicle-valuation-data` as a top-level workspace for factual vehicle intelligence, MOT/mileage evidence, valuation evidence, salvage, and prior-case context.  
This is my recommendation.

B. Merge it into `evidence-estimate-review`.  
This would mix factual vehicle/valuation data with estimate/image review.

C. Move it into `analytics-data-platform`.  
This undervalues near-term reviewer-facing vehicle and mileage evidence.

Question 11: should the re-derived taxonomy include `docs/plans/vehicle-valuation-data/` as a top-level workspace for DVLA/DVSA, MOT/mileage evidence, vehicle identity, valuation evidence, salvage, and prior vehicle/case context, while leaving weather/road/traffic enrichment as later analytics option papers?

---

## User
*2026-05-23 19:54:44 UTC*

A

---

## Codex
*2026-05-23 19:55:36 UTC*

**Thing 12: Engineer Communications**

This question is whether `docs/plans/engineer-communications/` should be top-level, and how it differs from `agent-skills`, `ai-agents`, `case-workflow-state`, and `user-experience-interfaces`.

**What The Supporting Docs Say**

plans-folder-expansion-plan.md proposes this workspace for engineer pack, templates, report drafting support, engineer copilot, missing-info chasers, CE style communication, status summaries, and report-clause/RAG support.

The all-ideas ledger has `Engineer support` rows for:

- engineer pack generator;
- template manager;
- engineer copilot;
- report drafting assistant.

It also has `Communications` rows for:

- case summary/status skill;
- missing-info chaser drafts;
- CE style communications skill;
- status update drafting;
- report clause knowledge/RAG assistant.

Work Package 11 - Engineer Pack and Reporting defines the pack contents: case summary, provider, VRM, claimant, dates, inspection details, instruction, ordered images, estimate, notes/chaser history, missing/uncertain items, and Box links.

8.6 Engineer Pack Generator and Template Manager says the pack should be source-linked, separate automation output from engineer conclusions, and support approval.

8.9 Communications, Chaser and Status Drafting says drafts should use verified case data only, be draft-first, and require approval before sending.

Engineer Pack Generator frames the engineer pack as a safe MVP output: AI prepares the pack; the engineer makes the judgement.

CE Communication Style Skill defines a reusable tone layer: concise, factual, no added facts, and approval before external send.

**My Re-Derived View**

`engineer-communications` should be a top-level workspace, but its ownership needs tightening.

It should own the **business workflows and artefacts**:

- engineer pack requirements;
- pack template variants;
- pack generation workflow;
- report upload/reporting workflow;
- missing-info chaser workflow;
- status update workflow;
- communication approval workflow;
- communication audit requirements;
- how drafts attach to work items and engineer packs.

It should not own the reusable AI/prompt asset itself when that asset is shared.

Those should split as:

- `agent-skills`: reusable CE style skill, case summary skill, chaser drafting skill, valuation explanation skill, report-clause/RAG skill.
- `ai-agents`: engineer support agent or missing-info agent that coordinates tools/skills.
- `case-workflow-state`: missing-info states and chaser due dates.
- `user-experience-interfaces`: screens for pack review, message approval, engineer portal/PWA.
- `evidence-estimate-review`: image/estimate summaries feeding into the pack.
- `vehicle-valuation-data`: valuation/MOT/DVLA evidence feeding into the pack.

**Important Boundary Detail**

I would keep “report-clause/RAG” cross-linked here, but not primarily owned here. It is a reusable skill/knowledge capability, so primary ownership should probably be `agent-skills`, with `engineer-communications` defining where it is used in engineer/report workflows.

**Options**

A. Keep `engineer-communications` as a top-level workspace for engineer pack, reporting workflow, chaser/status workflow, templates, and approval/audit flow.  
This is my recommendation.

B. Merge it into `agent-skills`.  
This would blur workflow artefacts with reusable prompting/skill lifecycle.

C. Merge it into `case-workflow-state`.  
This would overload state management with communication content and engineer-facing outputs.

Question 12: should the re-derived taxonomy include `docs/plans/engineer-communications/` as a top-level workspace for engineer pack/reporting and communication workflows, while reusable drafting/style/RAG skills are primarily owned by `agent-skills` and cross-linked here?

---

## User
*2026-05-23 19:55:53 UTC*

A

---

## Codex
*2026-05-23 19:56:42 UTC*

**Thing 13: AI Agents**

This question is whether `docs/plans/ai-agents/` should be top-level, and how it differs from automation, MCP/tools, reusable skills, and AI platform infrastructure.

**What The Supporting Docs Say**

phase_ai_agents.md proposes agents for:

- inbox triage;
- missing information;
- valuation/uplift;
- engineer support;
- continuous learning.

It says these agents should operate within defined boundaries and defer critical decisions to humans.

Agent vs Automation Decision Framework gives the key rule: use deterministic automation when the trigger/input/output/rule is clear; use AI assistance for classification, summarisation, drafting, or semantic matching; use a controlled agent only when AI must choose among approved tools, inspect multiple sources, prepare a sequence of actions, and stop at permission boundaries.

That framework also defines prohibited agent actions:

- final valuation;
- causation;
- roadworthiness;
- fraud allegation;
- liability conclusion;
- report sign-off;
- deletion of original evidence;
- disputed external communications.

The all-ideas ledger has five `AI agents` rows:

- inbox triage agent;
- missing-information agent;
- valuation and uplift agent;
- engineer support agent;
- continuous learning agent.

The expansion plan says `ai-agents`, `mcp-and-tooling`, and `agent-skills` are intentionally separate:

- MCP/tools expose callable business capabilities.
- Agent skills draft, summarise, explain, retrieve, or train.
- AI agents orchestrate approved tools and skills under permission levels.

**My Re-Derived View**

`ai-agents` should be a top-level workspace, but it should be explicitly later-stage and approval-gated.

It should own:

- agent role definitions;
- permission levels and escalation behaviour from the agent perspective;
- tool/skill orchestration rules;
- agent-specific approval boundaries;
- inbox triage agent;
- missing-information agent;
- valuation/uplift evidence agent;
- engineer support agent;
- continuous learning/recommendation agent;
- agent test/evaluation scenarios at the workflow level;
- “what the agent may propose versus do” matrices.

It should not own:

- deterministic workflow execution: `automation-centre`;
- underlying MCP/tool schemas and adapters: `mcp-and-tooling`;
- reusable prompts/skills: `agent-skills`;
- model hosting/evals/prompt governance: `ai-platform-tools`;
- domain source data: owned by the relevant domain workspaces;
- business governance policy: `governance-security`.

**Important Boundary Detail**

Some source docs call these “agents” too early. I would tighten language:

- inbox polling is automation, not an agent;
- exact case matching is automation, not an agent;
- chaser drafting is a skill, not an agent;
- sending a chaser is approved automation, not an agent by default;
- an agent is only needed when it reasons across multiple approved tools/skills and prepares suggestions/actions under permission gates.

So `ai-agents` should exist, but it should not be the default owner for AI-assisted features.

**Options**

A. Create `ai-agents` as a top-level workspace for controlled orchestrators only, with strict permission and approval boundaries.  
This is my recommendation.

B. Merge agents into `automation-centre`.  
This would blur deterministic workflow with AI orchestration.

C. Merge agents into `agent-skills`.  
This would blur reusable drafting/summarisation behaviours with multi-step tool orchestration.

Question 13: should the re-derived taxonomy include `docs/plans/ai-agents/` as a top-level workspace for controlled workflow agents that orchestrate approved tools/skills under permission levels, while keeping deterministic automation, MCP tools, and reusable skills separate?

---

## User
*2026-05-23 19:57:08 UTC*

A

---

## Codex
*2026-05-23 19:57:57 UTC*

**Thing 14: MCP And Tooling**

This question is whether `docs/plans/mcp-and-tooling/` should be top-level, and how it differs from domain adapters, agents, skills, and AI platform infrastructure.

**What The Supporting Docs Say**

plans-folder-expansion-plan.md says the AI tools pack has named MCP plans for EVA/Sentry, Outlook Graph, Box, DVLA/DVSA, job-sheet bridge, observability, and the MCP security gateway. It says these are platform/tool contracts, not ordinary product tickets.

The all-ideas ledger has `MCP/tools` rows for:

- EVA/Sentry API MCP;
- Outlook Graph intake MCP;
- Box storage metadata MCP;
- DVLA/DVSA vehicle intelligence MCP;
- Job Sheet / SharePoint spreadsheet bridge MCP;
- Observability and runbook MCP;
- Tool registry and MCP security gateway.

EVA / Sentry API MCP says the MCP should wrap EVA actions as narrow validated tools, keep secrets server-side, validate payloads, store responses, and return typed results.

Outlook / Microsoft Graph Intake MCP says production intake creates work items, while the MCP exposes read/search operations for agents.

Box Storage and Metadata MCP says the workflow layer decides when to create/upload, while agents can search/fetch metadata and cannot delete or move originals.

Tool Registry and MCP Security Gateway says a gateway should control which agents can call which tools, using permissions, schemas, rate limits, audit logging, and safe discovery.

The expansion plan gives the boundary rule: MCP/tools expose narrow callable capabilities; AI agents orchestrate approved tools and skills; agent skills draft/summarise/explain/retrieve/train.

**My Re-Derived View**

`mcp-and-tooling` should be a top-level workspace.

It should own:

- callable tool/MCP interface plans;
- tool schemas and typed inputs/outputs;
- tool permission boundaries;
- tool audit logging;
- rate limits and secret-handling rules;
- safe tool discovery;
- tool registry/security gateway;
- MCP wrappers for EVA, Outlook, Box, DVLA/DVSA, job sheet, observability;
- tool-level dry-run/simulation requirements.

It should not own:

- business adapter implementation details: `intake-storage-integrations`, `vehicle-valuation-data`, etc.;
- workflow orchestration: `automation-centre`;
- AI agent behaviour: `ai-agents`;
- reusable natural-language behaviours: `agent-skills`;
- model/prompt evaluation governance: `ai-platform-tools`;
- domain acceptance criteria beyond tool contracts.

**Important Boundary Detail**

An adapter and an MCP wrapper are related but not the same.

Example:

- `intake-storage-integrations` owns the EVA/Sentry adapter’s business behaviour: when to submit, what approval is needed, what failure means.
- `mcp-and-tooling` owns the callable MCP/tool surface around that adapter: tool schema, auth isolation, allowed callers, audit, rate limits, dry-run, disabled-tool behaviour.

**Options**

A. Create `mcp-and-tooling` as a top-level workspace for MCP/tool surfaces, schemas, permissions, audit, rate limits, safe discovery, and the tool registry/security gateway.  
This is my recommendation.

B. Merge it into `ai-agents`.  
This would blur tools with the agents that call them.

C. Merge each MCP wrapper into its domain workspace.  
This would lose consistent tool security, schema, and audit controls across domains.

Question 14: should the re-derived taxonomy include `docs/plans/mcp-and-tooling/` as a top-level workspace for MCP/tool contracts and the tool security gateway, while domain adapters remain owned by their domain workspaces?

---

## User
*2026-05-23 19:58:22 UTC*

A

---

## User
*2026-05-23 20:00:40 UTC*

skills are seperate as they would also potentially be integrated into other AIs e.g. chatgpt or claude desktop

---

## Codex
*2026-05-23 20:01:56 UTC*

Noted: `agent-skills` stays separate, and I’ll add a portability rule so skills can be reused by CE’s own platform, workflow agents, ChatGPT, Claude Desktop, or another approved AI front end.

**Thing 16: AI Platform Tools**

The question is whether `docs/plans/ai-platform-tools/` should be its own top-level planning workspace.

Supporting docs point to a platform layer behind skills and agents:

- plans-folder-expansion-plan.md proposes AI platform ownership for model hosting, eval datasets, prompt/version governance, feedback loops, redaction/training-data controls, and AI policy implementation.
- all-ideas-plan.md has AI platform rows for model evaluation, document mapper learning, prompt guardrails, controlled helper tools, and redaction/training-data controls.
- phase_ai_tools.md calls out model hosting, anonymised datasets, and evaluation/feedback loops.
- 25_model_evaluation_feedback_loop.md says reviewer corrections and test corpora should become measurable extraction/classification/image/valuation metrics.
- 06_WORK_PACKAGE_DOCUMENT_MAPPER_AND_EXTRACTION.md requires AI outputs to include evidence snippets and logs of prompt version, model/provider, input hash, and output.

My re-derived view: **include `ai-platform-tools` as a separate workspace**. It should own the shared AI substrate: model/provider choices, prompt registry/versioning, eval datasets, gold-standard fixtures, reviewer-correction feedback loops, AI run logging, redaction for evaluation/training, and release/rollback controls for AI behaviours.

It should **not** own the portable skills themselves; those stay in `agent-skills`. It should **not** own agent orchestration; that stays in `ai-agents`. It should **not** own MCP schemas/security gateway; that stays in `mcp-and-tooling`, though there will be cross-links.

Options:

A. Create `docs/plans/ai-platform-tools/` as its own top-level workspace for the shared AI substrate.

B. Merge it into `agent-skills`, making skills and platform governance one area.

C. Merge it into `governance-security` and keep only policy/control planning there.

Which do you want?

---

## User
*2026-05-23 20:02:03 UTC*

A

---

## Codex
*2026-05-23 20:03:25 UTC*

Recorded: `ai-platform-tools` = **A**, separate top-level workspace.

**Thing 17: User Experience And Interfaces**

The question is whether `docs/plans/user-experience-interfaces/` should be its own top-level workspace.

Supporting docs show UI/UX is not just one screen:

- plans-folder-expansion-plan.md proposes a workspace for dashboard, holding pen UI, case detail, review screens, parser UI, admin UI, internal portal/Teams front door, engineer mobile/PWA, accessibility, and adoption checks.
- 07_ui_dashboard_spec.md says the UI should be a case-operation dashboard that moves matters from messy intake to engineer-ready pack.
- 09_WORK_PACKAGE_DASHBOARD_REVIEW_AND_MATCHING.md frames the dashboard/review UI as the replacement for the job sheet holding pen.
- mvp_interlock.md defines staff UI as a first MVP capability: upload, preview, review, correction, and export.
- parser_ui_cli.md says UI and CLI must use the same parser, validation, export, and package services.
- 23_whatsapp_teams_portal_front_door.md introduces a portal/Teams-style front door that maps user requests into approved tools with permissions and audit.

My re-derived view: **include `user-experience-interfaces` as a separate workspace**.

It should own human-facing interaction design across staff, admin, engineer, and internal portal/chat surfaces: screen maps, dashboard mental model, review/correction UX, evidence matching UI, parser UI, provider admin UX, audit visibility, role-based views, accessibility, adoption/fallback design, and front-door interaction patterns.

It should **not** own the business rules themselves. Parser logic stays in `parser-extraction`; work states stay in `case-workflow-state`; provider rules stay in `provider-principal-config`; skills stay in `agent-skills`; Teams/WhatsApp/API implementation boundaries stay with intake/external integrations.

Options:

A. Create `docs/plans/user-experience-interfaces/` as the shared UX/interface planning home.

B. Keep UI tickets inside each domain workspace and only cross-link them.

C. Split UX into multiple homes now: staff UI, admin UI, engineer UI, and portal/chat UI.

Which do you want?

---

## User
*2026-05-23 20:03:41 UTC*

A

---

## Codex
*2026-05-23 20:04:44 UTC*

Recorded: `user-experience-interfaces` = **A**, separate top-level workspace.

**Thing 18: Finance And Billing**

The question is whether `docs/plans/finance-billing/` should be its own top-level workspace.

Supporting docs:

- plans-folder-expansion-plan.md proposes a finance workspace for invoice/fee-note generation, payment tracking, chaser metadata, repairer portal payment evidence, approvals, and payment automation option papers.
- all-ideas-plan.md separates invoice/fee-note generation from payment-status/chaser metadata.
- 31_invoice_fee_note_generation_tool.md describes deterministic invoice rendering from approved data and provider rules.
- 08_14_invoice_and_payment_workflow_automation.md covers invoice generation, payment-status tracking, invoice storage, fee rules, overdue visibility, and accounting export.
- work_item_contract_v1.md already allows `payment_status`, and evidence_package_contract_v1.md preserves portal/payment files like `Invoice.pdf` and `Summary.txt`.
- future_system_convergence.md says website portal/payment evidence should be recorded now, but portal/payment automation stays out of MVP.

My re-derived view: **include `finance-billing` as a separate workspace**.

It should own invoice/fee-note planning, fee rules, finance approval flow, invoice document generation/storage, payment-status tracking, payment chaser metadata, overdue visibility, and later payment/accounting integration option papers.

It should **not** own repair estimate review; that stays in `evidence-estimate-review`. It should **not** own portal/API partner access; that stays in `external-platform-partners`. It should **not** make autonomous payment chasing part of parser or operational MVP without approval.

Options:

A. Create `docs/plans/finance-billing/` as a separate workspace.

B. Merge finance/payment metadata into `intake-storage-integrations`, with invoice generation later.

C. Merge invoice/fee-note work into `provider-principal-config` because fee rules are provider-specific.

Which do you want?

---

## User
*2026-05-23 20:05:02 UTC*

A

---

## Codex
*2026-05-23 20:06:00 UTC*

Recorded: `finance-billing` = **A**, separate top-level workspace.

**Thing 19: Governance And Security**

The question is whether `docs/plans/governance-security/` should be its own active planning workspace.

Supporting docs:

- all-ideas-plan.md has governance rows for roles, audit, approvals, vendor review, retention, data protection, redaction, licensing, risk-language policy, and expert-evidence boundaries.
- governance_security.md says governance must be built into earliest parser and Operational Core work, not added after automation.
- dpia_vendor_governance.md defines required checks before live external services.
- vendor_register.md already tracks vendors like Box, EVA/Sentry, Graph, DVLA/DVSA, OCR providers, and valuation services.
- 08_12_security_dpia_and_vendor_governance.md calls for a formal governance layer before high-risk analytics, partner APIs, or AI-assisted review expand.
- 12_compliance_governance_and_risk.md defines the expert-evidence boundary: AI assists; named engineers keep professional judgement.

My re-derived view: **include `governance-security` as a separate active planning workspace**, but keep canonical reference docs under `docs/security/`, `docs/architecture/`, and `docs/contracts/`.

This workspace should own active governance work: DPIA/vendor review tickets, risk acceptance, security option papers, privacy/data-map updates, redaction controls, retention/archival policy, role/access review, audit requirements, expert-boundary policy, public/commercial data licensing, and approval gates for high-risk work.

It should **not** own implementation of every control. For example, `mcp-and-tooling` implements tool-gateway controls, `ai-platform-tools` implements AI run logging/evals, and `intake-storage-integrations` implements adapter-specific audit. Governance defines the rules and sign-off gates.

Options:

A. Create `docs/plans/governance-security/` as the active planning workspace for governance/security work.

B. Do not create a workspace; keep governance only in shared docs and require each domain to own its controls.

C. Split it into multiple workspaces now: privacy/DPIA, security/API, audit/retention, and expert-evidence policy.

Which do you want?

---

## User
*2026-05-23 20:06:13 UTC*

a

---

## Codex
*2026-05-23 20:07:44 UTC*

Recorded: `governance-security` = **A**, separate active planning workspace.

**Thing 20: Operations And Quality**

The question is whether `docs/plans/operations-quality/` should be its own top-level workspace.

Supporting docs:

- plans-folder-expansion-plan.md proposes a workspace for test corpus, regression harness, release/rollback, monitoring, runbooks, pilot rollout, decommissioning, and integration sandbox testing.
- all-ideas-plan.md has operations rows for monitoring/runbooks, release/rollback, failure runbooks, and packaged deployment.
- monitoring_runbooks.md defines event taxonomy and required runbooks.
- release_and_rollback.md defines release gates and rollback checks.
- 08_10_test_corpus_and_regression_harness.md calls for a controlled corpus and regression harness before releases.
- 13_WORK_PACKAGE_SECURITY_TESTING_ROLLOUT.md covers testing, rollout, training, monitoring, rollback, and legacy decommissioning.

My re-derived view: **include `operations-quality` as a separate workspace**.

It should own shared delivery reliability: regression harness planning, release gates, rollout stages, support ownership, operational monitoring, runbook library, incident/failure playbooks, pilot/parallel-run criteria, portable deployment support, and decommissioning quality gates.

It should **not** own every domain’s feature tests. Parser-specific tests stay with `parser-extraction`; AI/model evals stay with `ai-platform-tools`; integration implementation tests stay with the owning integration workspace. `operations-quality` owns the shared quality system and release/operational gates.

Options:

A. Create `docs/plans/operations-quality/` as the shared QA, release, rollout, and support workspace.

B. Keep these concerns inside `operational-core` until later.

C. Split now into separate workspaces for testing, operations/runbooks, and rollout/decommissioning.

Which do you want?

---

## User
*2026-05-23 20:07:47 UTC*

Just set them all as seperate workspaces with whatever you recommend, then proceed to the cross-check for overlaps, dependancies, source ownership

Then, propose the final roadmap grouping 

Await my approval

---

## Codex
*2026-05-23 20:10:05 UTC*

No files changed. This is the proposal to approve before I create/update anything.

**Workspace Decision**
Set the remaining areas as separate workspaces:

- `analytics-data-platform/`: analytics, BI, historical mining, warehouse, risk indicators, scheduling, continuous improvement.
- `external-platform-partners/`: customer portal, partner API, insurer integrations, Audatex/estimating partnerships, partner access controls.
- `product-business/`: discovery, ROI/KPI framing, pitch, objections, independence/defensibility.

That gives the full proposed structure from plans-folder-expansion-plan.md, with existing `initial-repo-setup/` and `operational-core/` retained.

**Cross-Check Findings**
Primary ownership rule: every idea from all-ideas-plan.md should have exactly one primary workspace, with cross-links allowed.

Resolved overlaps:

- `operational-core/` becomes coordination only after split. Domain tickets move out.
- `parser-extraction/` owns document reading/extraction; `provider-principal-config/` owns provider/principal rules; `case-workflow-state/` owns lifecycle/review/missing-info state.
- `user-experience-interfaces/` owns screens and interactions, not business logic.
- `automation-centre/`, `ai-agents/`, `mcp-and-tooling/`, `agent-skills/`, and `ai-platform-tools/` stay separate.
- `agent-skills/` includes portable skill specs usable from CE platform, workflow agents, ChatGPT, Claude Desktop, or other approved AI front ends.
- `finance-billing/` owns billing/payment workflow; `intake-storage-integrations/` only records portal/payment metadata early.
- `external-platform-partners/` owns portals/APIs/partner integrations; domain adapters still live in their owning workspaces.
- `governance-security/` defines gates; owning workspaces implement the controls.
- `operations-quality/` owns release, rollout, test harness, runbooks, and support gates.

Contradiction guardrails:

- No autonomous EVA/Sentry submit, payment chasing, WhatsApp sending, partner API, portal automation, cloud OCR, valuation provider, or broad AI/RAG work before governance approval.
- AI assists with extraction, drafting, summarising, and review prompts; it does not own expert judgement.
- Raw evidence remains immutable.
- Active tickets must not be duplicated in `operational-core/` after split.

**Roadmap Proposal**
1. **Section 0: Taxonomy And Planning Scaffold**
Create all workspace folders, README/source map/roadmap stubs, indexes, repo map updates, manifest updates, and verifier updates.

2. **Section 1: Foundation And Governance**
Lock contracts, ADRs/options, governance/security, release/rollback, data map, vendor register, and source ownership.

3. **Section 2: Parser, Provider, And Corpus Core**
Move parser MVP into `parser-extraction/`; split provider coverage/admin into `provider-principal-config/`; create regression/test ownership in `operations-quality/`.

4. **Section 3: Operational Core First Slice**
Build/plan work item state, review queue, staff UI, CLI parity, EVA JSON export, and Box-ready package under their owning workspaces, coordinated by `operational-core/`.

5. **Section 4: Intake And Live Integration Boundaries**
Plan Outlook intake, Box live upload, EVA/Sentry adapter, spreadsheet bridge, website/WhatsApp metadata, runbooks, and sandbox tests.

6. **Section 5: Evidence, Vehicle, Engineer Pack, Communications**
Promote image/evidence review, estimate/ABP review, DVLA/DVSA, mileage, valuation evidence, engineer pack, communication workflows, and portable skills.

7. **Section 6: AI Platform, Tools, And Agents**
Only after controlled tools/skills exist: model evals, prompt governance, MCP gateway, bounded workflow agents, and AI run logging.

8. **Section 7: Finance And External Ecosystem**
Invoice/fee-note workflow, payment tracking, portal/API option papers, insurer/Audatex partnership discovery, partner access controls.

9. **Section 8: Analytics And Continuous Improvement**
Operations analytics, client/principal intelligence, data quality, BI, warehouse, risk indicators, scheduling, ROI tracking, product/business review.

10. **Section 9: Unified Platform And Decommissioning**
Mature convergence roadmap, migration from legacy spreadsheet/mapper, full rollout gates, and decommissioning only after parity, rollback, and adoption evidence.

Awaiting your approval before I create or update plan files.

---

## User
*2026-05-23 20:12:07 UTC*

Agreed, generate the roadmap, and all relevant files. Ensure everything you do is clearly referenced from project source materials and specifically citeable evidence.

---
