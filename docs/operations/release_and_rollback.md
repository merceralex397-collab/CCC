# Release And Rollback

Date: 2026-05-23

## Purpose

CCC releases must be traceable because parser/provider changes can affect EVA exports and evidence packages.

## Release Checklist

- Update relevant docs/contracts/tickets.
- Run scaffold verification.
- Run targeted parser/corpus tests for affected providers.
- Check provider matrix if provider logic changed.
- Confirm no personal injury or KADOE scope has been introduced.
- Record release notes with changed contracts, provider config versions, parser version, and known limitations.

## Rollback Checklist

- Identify affected version: parser, provider config, UI, CLI, adapter, or package builder.
- Preserve audit and source files.
- Roll back provider config by activation pointer, not deletion.
- Roll back code by normal version-control process.
- Re-run affected private corpus tests.
- Record rollback reason and affected work items.

## Release Gates

- Parser changes require provider regression evidence.
- Provider config activation requires provider-admin role and audit reason.
- Live integrations require dry-run/sandbox evidence and runbook.
- Cloud adapters require DPIA/vendor governance sign-off.

