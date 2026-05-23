# Option Paper: Parser And Staff UI Platform

Date: 2026-05-23

## Status

Open decision.

## Decision Needed

Choose the first staff-facing UI platform for parser review, provider admin, work-item queue, and package generation.

## Evaluation Criteria

- Usable by non-technical office staff.
- Supports local/shared internal deployment.
- Can call the same parser core as the CLI.
- Supports file upload, preview, field review, image ordering, package generation, and provider admin.
- Reasonable installation and maintenance burden.
- Allows future Operational Core screens without a rewrite.

## Options

| Option | Strengths | Risks | Fit |
| --- | --- | --- | --- |
| Local web UI | Fast to build, works with Python/FastAPI or similar, easy UI/CLI parity through shared service layer, simple internal hosting. | Needs browser/server packaging and careful local file handling. | Strong first candidate. |
| Tkinter/PySide desktop | Simple local desktop packaging, direct file access. | Harder to build polished review/admin UI, weaker future multi-user story. | Useful fallback for parser-only tool, weaker for Operational Core. |
| WinUI desktop | Native Windows feel, strong local desktop UX, good fit for office Windows machines. | More build/deployment complexity and .NET/XAML skill requirement. | Good if Windows-native app is preferred after spike. |
| Electron/Tauri | Rich desktop UI and file handling with web frontend skills. | Packaging and update surface grows; Electron can be heavy. | Viable if desktop install is required but web UI quality is needed. |
| Hosted/internal web | Best multi-user operational path, easier central audit/state store. | Requires hosting, auth, storage, and network governance earlier. | Strong future target; may be first if infrastructure decision is made. |

## Current Recommendation

Keep the decision open until a short UI spike compares local web UI and WinUI/Tauri against actual staff workflows. The architecture should assume UI/CLI parity through shared parser services so the platform choice does not change parser core contracts.

## Required Follow-Up

- Build a thin upload-review-export prototype against the parser service boundary.
- Validate file preview requirements for PDF, DOCX/DOC converted output, MSG/EML bodies, images, and batch folders.
- Confirm whether the first deployment is per-machine, shared LAN/server, or hosted internal.

