# ADR 0004: Parser Is A Ground-Up Compatible Rebuild

Date: 2026-05-23

## Status

Accepted.

## Context

The legacy CE Document Mapper contains useful provider rules and behaviours but was built before the current corpus, UI requirements, evidence package requirements, and future Operational Core boundaries were understood.

## Decision

Build a ground-up parser core that is compatible with the current mapper's useful behaviours. Use the legacy mapper and `docs/reference/raw/collisionrelateddocs/claudechat.md` as behavioural oracle evidence, not as the architecture to preserve.

## Consequences

- Provider method vocabulary should remain recognisable where it captures real behaviour, for example label extraction, offsets, regex, manual input, engineer-report detection, and provider-specific rules.
- Golden tests must capture legacy behaviours before changing them.
- Parser output must be canonical and provenance-aware, not just EVA JSON.
- The parser must be modular enough to support PDF, DOCX, DOC, MSG/EML, images, and batch folders through adapters.

