# Monitoring And Runbooks

Date: 2026-05-23

## Monitoring Event Taxonomy

| Event | Severity | Notes |
| --- | --- | --- |
| Parser run failed | warning/critical | Critical if whole batch cannot be reviewed. |
| Critical validation blocker | warning | Blocks EVA export until resolved. |
| Provider detection conflict | warning | Requires review or provider config fix. |
| Package generation failed | critical | Blocks Box-ready handoff. |
| Storage upload failed | critical in P3 | Live upload future phase. |
| EVA/Sentry rejection | critical in P3 | Direct submission future phase. |
| Provider config activated | info | Audit event required. |
| Warning overridden | warning | Reviewer reason required. |

## Required Runbooks

- `docs/operations/runbooks/outlook-intake-stopped.md`
- `docs/operations/runbooks/box-upload-failure.md`
- `docs/operations/runbooks/eva-rejected-payload.md`
- parser run failure runbook before parser MVP release;
- provider config rollback runbook before provider admin release.

## First MVP Monitoring

For parser MVP, monitoring can start as local logs and audit events. Live alerting is not required until shared internal deployment, but the event taxonomy must be stable enough to map logs into alerts later.

