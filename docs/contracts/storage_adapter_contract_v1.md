# Storage Adapter Contract v1

## Purpose

Storage adapters receive a validated evidence package and return storage references. Parser extraction and EVA export must not know provider-specific SDK details.

## Adapter Input

- evidence package manifest;
- local package folder path;
- reviewed work item metadata;
- actor account;
- dry-run/live mode flag.

## Adapter Output

| Field | Required | Notes |
| --- | --- | --- |
| `storage_attempt_id` | yes | Stable id for upload/package attempt. |
| `adapter_name` | yes | `box`, `gcs`, `s3`, `azure_blob`, etc. |
| `mode` | yes | `package_only`, `dry_run`, or `live_upload`. |
| `status` | yes | `created`, `uploaded`, `failed`, `partial`, `skipped`. |
| `remote_references` | no | Folder/file ids or URLs where allowed. |
| `checksums` | yes | Hashes of local files and uploaded files where available. |
| `warnings` | yes | Permission, duplicate, retention, or mismatch warnings. |
| `audit_event_id` | yes | Link to audit event. |

## Box First Rule

The first storage deliverable is `package_only`: a Box-ready local package and manifest. Live Box upload must be a later adapter using the same package shape.

## Future Storage

Google Cloud, AWS, and Azure storage remain future options. Selection must be tied to deployment, governance, cost, and document-intelligence decisions.

