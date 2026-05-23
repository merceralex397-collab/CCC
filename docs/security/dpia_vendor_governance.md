# DPIA And Vendor Governance

Date: 2026-05-23

## Purpose

This placeholder defines the minimum governance checklist before CCC uses live external services beyond local package generation.

## Services Requiring Review

- Box live upload or Box AI/Extract.
- EVA/Sentry API submission.
- Outlook/Graph intake.
- DVLA/DVSA APIs or bulk-data processing.
- Experian/HPI/valuation services.
- Azure, AWS, or Google cloud OCR/document intelligence.
- Any LLM/VLM service used for extraction, review, valuation, image checks, or communications.

## Required Review Questions

- What data is sent to the service?
- Is data stored by the vendor, and for how long?
- What access controls and audit logs exist?
- What regions/data residency apply?
- What costs and rate limits apply?
- What failure/retry and deletion processes exist?
- What provenance comes back and how does it map into CCC contracts?
- Can the service be disabled by feature flag?
- What manual review gate remains before business action?

## Required Outputs Before Activation

- vendor register row;
- data-map update;
- DPIA decision or explicit lightweight-risk acceptance;
- integration-specific runbook;
- test evidence;
- rollback/fallback plan.

