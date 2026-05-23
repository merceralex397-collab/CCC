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
| `box_folder_url` | no | Box folder URL when a Box adapter is used or referenced. |
| `box_folder_stage` | no | Stage marker such as `repair-estimate-request`, `package-only`, `live-upload`, or `closed-files-backup`. |
| `live_upload_references` | no | Adapter-specific uploaded folder/file ids when `mode` is `live_upload`. |
| `closed_files_reference` | no | Reference to `Closed Files` or archive location where closure backup is stored. |
| `archive_reference` | no | Canonical archive pointer when the package is moved or mirrored later. |
| `local_network_folder_url` | no | Local network folder reference carried through from spreadsheet/work-item metadata. |

## Box First Rule

The first storage deliverable is `package_only`: a Box-ready local package and manifest. Live Box upload must be a later adapter using the same package shape.

Box-first means the contract can carry Box folder URL/stage metadata now, but live upload remains a separate adapter concern and must not change the package-only MVP rule.

## Future Storage

Google Cloud, AWS, and Azure storage remain future options. Selection must be tied to deployment, governance, cost, and document-intelligence decisions.
