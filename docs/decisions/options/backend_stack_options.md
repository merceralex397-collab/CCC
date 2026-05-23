# Option Paper: Backend Stack

Date: 2026-05-23

## Status

Open decision.

## Decision Needed

Choose the backend implementation stack for parser core, Operational Core services, and future adapters.

## Options

| Option | Strengths | Risks | Fit |
| --- | --- | --- | --- |
| Python/FastAPI | Best access to parser/OCR/document libraries, fast iteration, natural CLI sharing, strong fit for PyMuPDF/pdfplumber/python-docx/openpyxl. | Needs discipline around typing, service boundaries, packaging, and long-running worker reliability. | Strong first candidate for parser MVP. |
| .NET | Strong Windows/enterprise integration, good WinUI pairing, mature service hosting. | Less direct fit for Python-heavy extraction libraries unless bridged. | Strong if UI/deployment is Windows-native. |
| Node/TypeScript | Strong web UI ecosystem and shared types with frontend. | Weaker local document extraction ecosystem for the current corpus. | Good for frontend/API layer, less ideal for parser core. |
| Hybrid desktop/server | Lets Python own extraction while .NET/TS owns UI. | Cross-process contract and packaging complexity. | Viable if platform choice demands it. |
| Managed cloud stack | Strong scalability and managed auth/storage/logging. | Introduces governance, cost, data residency, and vendor dependencies early. | Future candidate, not required for first parser MVP. |

## Current Recommendation

Keep backend stack open, but design the parser implementation plan around a Python parser core because the current extraction research and local tooling point there. If a non-Python UI is selected, keep the parser behind a stable local API/CLI/service contract.

## Required Follow-Up

- Spike parser core with PyMuPDF, pdfplumber, pypdf, python-docx, legacy DOC conversion, and MSG/EML extraction.
- Spike UI calling parser through the same service methods used by CLI.
- Decide packaging and deployment before building multi-user workflow state.

