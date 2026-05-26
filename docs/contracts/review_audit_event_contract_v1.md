# Review Audit Event Contract v1

## Purpose

Review and audit events preserve human accountability and make parser corrections, overrides, exports, provider changes, and package generation traceable.

## Event Envelope

| Field | Required | Notes |
| --- | --- | --- |
| `event_id` | yes | Stable id. |
| `event_type` | yes | See event types. |
| `work_item_id` | no | Required for case/workflow events. |
| `actor_account_id` | yes | Named local CCC account. |
| `actor_role` | yes | Role at time of action. |
| `occurred_at` | yes | ISO timestamp. |
| `source_id` | no | File, parser run, package, export, or config id. |
| `before` | no | Previous value for changed fields/config. |
| `after` | no | New value for changed fields/config. |
| `reason` | no | Required for overrides, rejected warnings, provider activation, rollback. |
| `severity` | no | `info`, `warning`, `critical`. |

## Event Types

- `work_item_created`
- `file_added`
- `parser_run_started`
- `parser_run_completed`
- `field_corrected`
- `warning_resolved`
- `warning_overridden`
- `provider_config_created`
- `provider_config_activated`
- `provider_config_rolled_back`
- `eva_json_exported`
- `evidence_package_generated`
- `status_changed`
- `integration_attempted`
- `integration_failed`

## Rules

- Manual correction events must preserve extracted value and corrected value.
- Critical warnings cannot be overridden without reviewer role and reason.
- Provider config activation requires provider-admin role and a source-linked change reason.
- Audit events are append-only.

