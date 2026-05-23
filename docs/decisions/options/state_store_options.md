# Option Paper: State Store

Date: 2026-05-23

## Status

Open decision.

## Decision Needed

Choose the first durable state store for work items, parser runs, provider config versions, review events, package manifests, and export records.

## Options

| Option | Strengths | Risks | Fit |
| --- | --- | --- | --- |
| SQLite | Simple local deployment, good for parser MVP and single-machine proof, easy backup. | Multi-user contention and shared internal app limitations. | Good parser-only starting point. |
| Postgres | Strong shared app fit, concurrency, audit/event tables, future analytics source. | Requires server setup and maintenance. | Strong Operational Core candidate. |
| File manifests | Transparent and easy to inspect, pairs with package generation. | Harder queries, concurrency, and audit integrity. | Good package format, not enough as sole app store. |
| DuckDB | Good local analytics over manifests and corpus metadata. | Not a primary transactional workflow database. | Useful analytics companion later. |
| Cloud-managed database | Managed reliability, backup, scale, and access control. | Earlier vendor, network, and governance decisions. | Future option if hosted/internal cloud is selected. |

## Current Recommendation

Keep the decision open. Use file manifests for evidence packages regardless of app store. For parser-only development, SQLite can support local runs. For the shared Operational Core, Postgres is the strongest default unless deployment constraints rule it out.

## Required Follow-Up

- Confirm expected concurrent users.
- Confirm whether the first deployment is local desktop, shared office server, or hosted internal.
- Define backup/restore and audit retention requirements.

