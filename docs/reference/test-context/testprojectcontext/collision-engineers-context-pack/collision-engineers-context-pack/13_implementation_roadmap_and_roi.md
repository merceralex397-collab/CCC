# 13 — Implementation Roadmap and ROI

Generated: 2026-05-22

## Roadmap principle

Start narrow, prove value, then integrate. The project should move from manual-upload demo to live intake only after the evidence-matching and pack-generation logic is trusted.

## Phase 0 — Discovery and scope lock

### Goal

Confirm the real workflow, current tools, data sources and prototype success criteria.

### Activities

- Map intake channels.
- Review holding-pen spreadsheet or case tracker.
- Review sample instruction PDFs.
- Review sample Audatex/estimate PDFs.
- Review current report templates.
- Confirm case categories and required evidence checklists.
- Confirm who reviews and signs reports.
- Confirm data-security constraints.
- Define success metric for first demo.

### Output

- Agreed prototype scope.
- Sample synthetic documents modelled on real formats.
- Required fields list.
- Evidence checklist by report type.

## Phase 1 — Local demo

### Goal

Prove upload → extraction → matching → pack generation.

### Features

- Manual upload.
- Document classification.
- Instruction PDF extraction.
- Estimate parser.
- Evidence matching.
- Holding-pen status.
- Missing-info flags.
- Engineer pack generator.
- Chaser draft.
- Activity log.

### Success criteria

- Demo handles 5 synthetic cases.
- Extracts key fields with visible confidence.
- Correctly flags mismatches and missing evidence.
- Generates usable engineer pack.
- Does not claim final technical decisioning.

## Phase 2 — Internal MVP

### Goal

Make the demo usable by the internal team on controlled, non-live or limited live cases.

### Features

- User login.
- Persistent database.
- Better PDF/OCR handling.
- Editable extracted fields.
- Pack templates.
- Manual status controls.
- Export holding-pen CSV.
- PDF export.
- Admin review workflow.

### Data caution

Use either synthetic data or approved redacted/live data under agreed controls.

## Phase 3 — Intake integration

### Goal

Reduce manual upload by connecting to real intake channels.

### Candidate integrations

- shared Outlook mailbox;
- website/repairer portal submissions;
- SharePoint/OneDrive folder;
- WhatsApp Business API or approved export workflow;
- client API, if available;
- AudaConnect only if licensed and useful.

### Features

- automatic attachment ingestion;
- source sender/subject metadata;
- duplicate file detection;
- notifications for blocked cases;
- management dashboard.

## Phase 4 — Estimate review and ABP support

### Goal

Improve engineer-review efficiency for estimate and charge disputes.

### Features

- Audatex PDF extraction refinement;
- supplementary estimate detection;
- ADAS/alignment/SRS flags;
- ABP charge category flags;
- evidence-required checklist;
- draft rebuttal/review notes for engineer approval.

## Phase 5 — Image quality and duplicate support

### Goal

Improve photo evidence quality and reduce re-contact cycles.

### Features

- standard-angle checklist;
- blur/quality score;
- odometer/VIN/plate image detection;
- damage-zone tagging;
- duplicate-image search across previous cases;
- metadata anomaly prompts.

### Caution

Frame as image-quality and integrity support, not automated fraud detection.

## Phase 6 — Knowledge base and analytics

### Goal

Turn operational data and previous reports into reusable knowledge.

### Features

- internal searchable knowledge base;
- standard clauses library;
- report-template manager;
- management KPI dashboards;
- bottleneck analytics;
- client/source performance reporting;
- basic predictive models for delay/supplementary risk.

## ROI model

The public data is not sufficient to calculate exact ROI. Use a scenario model during discovery.

### Metrics to collect

| Metric | Why it matters |
|---|---|
| Cases per week | Determines scale of savings. |
| Admin minutes per intake | Direct labour saving. |
| Time to match evidence | Core bottleneck. |
| % cases missing images/instruction/estimate | Chaser workload. |
| Time from instruction to engineer-ready | Main operational KPI. |
| Report turnaround time | Client-facing KPI. |
| Rework/misfile rate | Quality KPI. |
| Engineer time spent on admin | Opportunity cost. |
| Chasers sent per case | Friction KPI. |
| Duplicate/unmatched cases | Control KPI. |

### Conservative example

If the system saves only 15 minutes per case and the firm handles 25 cases per week:

```text
25 cases/week × 15 minutes = 375 minutes/week
375 minutes = 6.25 hours/week
6.25 hours × 48 working weeks = 300 hours/year
```

At a fully loaded admin cost of £25–£35/hour, that equals roughly £7,500–£10,500 per year in admin time alone. This excludes faster turnaround, reduced errors, increased capacity, improved client experience and engineer time savings.

If the later workflow saves 40–70 minutes per case, the value increases materially. Validate actual case volumes and time-on-task before quoting ROI.

## KPI dashboard for production

| KPI | Target direction |
|---|---|
| Instruction-to-case-created time | Down |
| Case-created-to-ready-for-engineer time | Down |
| % cases with clear status | Up |
| % cases requiring admin rework | Down |
| Missing-information chasers per case | Down |
| Engineer pack generation time | Down |
| Report turnaround time | Down |
| Unmatched evidence count | Down |
| Duplicate case count | Down |
| User corrections to AI extraction | Down over time |

## Implementation priorities

### Must have

- file upload;
- classification;
- extraction;
- matching;
- missing-info flags;
- engineer pack;
- audit log;
- human approval.

### Should have

- estimate/Audatex parser;
- chaser draft;
- PDF export;
- holding-pen CSV export;
- settings/checklists.

### Later

- email ingestion;
- WhatsApp integration;
- calendar integration;
- AudaConnect;
- image quality scoring;
- duplicate-image search;
- RAG knowledge base;
- analytics/predictive scoring.

## Resourcing

A practical first build can be one developer plus domain review from Collision Engineers. The highest-friction work is not UI; it is understanding real document variability and aligning output to engineer workflow.

## Delivery risk

| Risk | Mitigation |
|---|---|
| Sample PDFs vary widely | Build extractor with confidence and correction workflow. |
| AI misreads fields | Show source snippets; require review. |
| Staff distrust output | Use transparent match reasons and audit trail. |
| Scope expands too early | Keep phase-one to manual upload and pack generation. |
| Compliance anxiety | Explicitly keep engineer sign-off and no auto-final reports. |
| Proprietary Audatex constraints | Parse supplied PDFs first; use AudaConnect only if licensed. |
