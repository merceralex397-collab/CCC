# Vendor Register

Date: 2026-05-23

| Vendor/Service | Status | Planned Phase | Purpose | Review Required Before Use |
| --- | --- | --- | --- | --- |
| Box | planned package-first | P1/P3 | Case/evidence storage. P1 is local Box-ready package; P3 is live upload. | Yes for live upload and Box AI/Extract. |
| EVA/Sentry | future adapter | P3 | Downstream case/report API submission. | Yes; schema/API access and failure handling must be validated. |
| Microsoft Outlook/Graph | future adapter | P3 | Intake from shared mailboxes. | Yes; mailbox access model and audit identity. |
| DVLA/DVSA | future adapter | P4 | Vehicle and MOT/mileage evidence. | Yes; API terms, caching, and rate limits. |
| Experian/HPI/valuation providers | future adapter | P4 | Adverse history and valuation evidence. | Yes; licensing and evidence storage. |
| Azure AI Document Intelligence | option | P2/P4 | OCR/document intelligence fallback. | Yes; data residency, cost, provenance, feature flag. |
| AWS Textract | option | P2/P4 | OCR/document intelligence fallback. | Yes; data residency, cost, provenance, feature flag. |
| Google Document AI | option | P2/P4 | OCR/document intelligence fallback. | Yes; data residency, cost, provenance, feature flag. |
| Box AI/Box Extract | option | P3/P4 | Metadata extraction over Box content. | Yes; determinism, audit, and Box dependency. |

