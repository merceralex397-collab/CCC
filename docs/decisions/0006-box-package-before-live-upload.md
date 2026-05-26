# ADR 0006: Box Package Generation Before Live Box Upload

Date: 2026-05-23

## Status

Accepted.

## Context

Box is part of the current operating model, but direct API upload adds authentication, permissions, retention, duplicate handling, and recovery complexity. Staff can benefit earlier from deterministic package generation.

## Decision

The first Box integration is local Box-ready package generation with a manifest. Live Box upload is a later storage adapter.

## Consequences

- Package generation must preserve originals, images, instructions, companion reports, notes, EVA JSON, and checksums.
- The package folder should be named using the reviewed case/PO when available.
- Live upload later must upload the same package shape rather than invent a second storage model.

