# ADR 0008: Private Real Corpus Is The Authoritative Test Set

Date: 2026-05-23

## Status

Accepted.

## Context

The current parser problem is defined by real Collision Engineers documents. Synthetic fixtures and public examples cannot prove provider parity.

## Decision

The authoritative test data for parser parity is the private real corpus under `docs/reference/raw/collisionrelateddocs/` and its normalized companions. Redacted or synthetic fixtures may be added later for public CI, but they must not replace private corpus tests.

## Consequences

- Golden tests must cover all 26 current provider presets using private corpus examples.
- Provider config changes require corpus regression checks before activation.
- Public sharing of fixtures requires explicit redaction and review.

