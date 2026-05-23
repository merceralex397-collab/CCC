# ADR 0007: Parser Is Deterministic First

Date: 2026-05-23

## Status

Accepted.

## Context

The parser must be auditable, repeatable, and testable against private real corpus examples. Research notes recommend native extraction and layout-aware parsing before OCR or AI.

## Decision

The parser is deterministic first. OCR, cloud document intelligence, and AI/VLM extraction are fallback or future adapters used only when justified by file type, quality, or approved feature flags.

## Consequences

- PDF extraction starts with native geometry-aware parsing, then table/layout fallback, then text fallback, then OCR only where justified.
- Every extracted field must carry source/provenance and method metadata where available.
- Manual review gates remain mandatory for low confidence, missing required fields, conflicts, or fallback extraction.

