# ADR 0005: Shared Internal App With Named Local Accounts

Date: 2026-05-23

## Status

Accepted.

## Context

Collision Engineers currently use shared Outlook mailboxes. Shared mailbox identity is not sufficient for audit, correction history, provider configuration changes, or approval gates.

## Decision

The first deployment target is a shared internal app with named local app accounts, roles, and audit identity.

## Consequences

- The app must distinguish operators, reviewers, provider admins, viewers, and admins.
- Manual corrections, provider config edits, export approvals, and package generation must record actor identity.
- Later SSO can replace local accounts if approved, but shared mailbox credentials must not become CCC audit identity.

