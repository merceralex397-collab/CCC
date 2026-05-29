# Option Paper: Model/Provider Selection + Hosting

Status: open (design — not approved for build)
Owner: unassigned
Created: 2026-05-29
Group: ai-platform / platform-tools (G4)
Source links: `docs/superpowers/specs/2026-05-29-ai-platform-design.md`, `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`, `docs/architecture/governance_security.md`

## Context

CCC's AI runs today via approved front ends (Claude / Codex). The decision (2026-05-29) is a **two-track** strategy: keep multi-provider front-end access now (no self-hosting) **and** evaluate self-hosting in parallel.

## Track A — Multi-provider via approved front ends (now)

Use Claude / Codex (and other approved front ends) via API; standardise prompt/version/eval across providers; redaction before external calls per policy. Lowest cost/ops; matches current usage and the cross-AI-portability theme of `agent-skills`. Provider choice per task (e.g. Claude for drafting, Codex connector for Autotrader).

## Track B — Self-hosting evaluation (parallel option-paper)

Evaluate CCC-hosted / open models on: data residency, cost at volume, control/independence, latency, maintenance/ops burden, and which workloads (if any) justify it (e.g. high-volume redaction-sensitive extraction). **Evaluation, not commitment.**

## Decision Criteria

Data residency + privacy (redaction-before-external-call); cost at expected volume; control/independence; portability across front ends; ops burden; per-workload fit; governance/vendor approval.

## Governance Gates

Vendor + privacy + data-residency review before any provider is relied upon for PII-bearing calls; redaction policy applies regardless of provider.

## Open Questions

What workload (if any) triggers self-hosting; per-provider data-handling terms; how prompt/version/eval stays consistent across providers.
