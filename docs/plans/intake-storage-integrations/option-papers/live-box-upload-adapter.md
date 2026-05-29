# Option Paper: Live Box Upload Adapter

Status: open (design only — not approved for build)
Owner: unassigned
Created: 2026-05-29
Group: bridge / storage (G2)
Source links: `docs/contracts/storage_adapter_contract_v1.md`, `docs/contracts/evidence_package_contract_v1.md`, `docs/superpowers/specs/2026-05-29-bridge-design.md`, `docs/operations/runbooks/box-upload-failure.md`

## Context

Storage is `package_only` today: `src/ccc_parser/packaging.py` produces a deterministic Box-ready local folder + manifest. This paper evaluates promoting that to a live Box upload adapter, using the **same package shape** per the storage adapter contract (`mode: package_only → dry_run → live_upload`). Live upload must not change the package-only MVP rule.

## Options To Evaluate

1. **Box official SDK / API** with a dry-run mode first, then gated live upload.
2. **Manual upload retained** (staff drag the local package into Box) — no adapter; lowest risk, no automation benefit.
3. **Deferred** until CCC-owned storage decision (GCS/S3/Azure) is made, to avoid building a Box-specific path that is later replaced.

## Decision Criteria

Security/auth model and secret handling; duplicate handling and upload-status tracking; dry-run parity with the local package; mapping to `box_folder_url`/`box_folder_stage`/`closed_files_reference` in the contract; failure recovery (runbook); cost; alignment with the future CCC-owned storage decision; governance/vendor sign-off.

## Governance Gates

Vendor/privacy/API-security review required before any live write. No autonomous upload without explicit approval and a proven `package_only` baseline.

## Open Questions

Box tenant/app registration ownership; folder-stage taxonomy (`repair-estimate-request` / `package-only` / `live-upload` / `closed-files-backup`); relationship to the `Closed Files` backup convention.
