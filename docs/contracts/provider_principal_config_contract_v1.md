# Provider Principal Config Contract v1

## Purpose

Provider/principal configuration controls provider detection, EVA principal values, case/PO reference sequencing, field mapping rules, and provider-specific validation.

## Config Record

| Field | Required | Notes |
| --- | --- | --- |
| `provider_config_id` | yes | Stable id for the provider preset. |
| `display_name` | yes | Human-readable name, for example `FW (Garage)`. |
| `principal_code` | yes | EVA/CE principal code when known. |
| `aliases` | no | Alternative names/codes used in job sheets or documents. |
| `detect_phrases` | yes | Ordered deterministic provider detection phrases. |
| `field_rules` | yes | Mapping rules using the CE Document Mapper-compatible method vocabulary. |
| `validation_rules` | yes | Provider-specific requirements and warning severity. |
| `case_po_sequence` | no | Annual reset and provider code sequencing rules where used. |
| `active` | yes | Only active versions can be used by default parser runs. |
| `version` | yes | Monotonic config version. |
| `created_by` | yes | Named account. |
| `created_at` | yes | ISO timestamp. |
| `change_reason` | yes | Required for activation or mapping-rule changes. |

## Method Vocabulary Baseline

The rebuild should preserve useful legacy method concepts so old behaviours can be tested:

- manual input;
- single label;
- two labels;
- single label with offset;
- regex extraction;
- provider-specific transforms;
- engineer-report detection;
- address block extraction;
- image/evidence handling flags.

## Activation Rules

- Draft config can be edited without affecting parser runs.
- Activation requires provider-admin role, change reason, and regression check against relevant private corpus examples.
- Rollback creates a new active pointer and an audit event.
- Deletion should be logical only; historical parser runs must resolve their config version.

## Current Provider Presets

The current 26 parser presets are:

`ALISON`, `ALS`, `AMS`, `AX`, `BC`, `BLACK`, `CNX (Engineers)`, `DFD`, `EVA (Engineers)`, `FW (Garage)`, `FW (Solicitor)`, `HDUK`, `KBS`, `KERR`, `KMR`, `MP (Branded)`, `MP (Simple)`, `OAK`, `PCH (Lawshield)`, `PCH (Performance)`, `QCL`, `QDOS`, `RJS`, `SBL`, `SWAN`, `TEN`.

Known job-sheet coverage gaps requiring review are `ACSP`, `OAK/AX`, `PRINCIPAL`, and `WOODLANDS`.

## Sources

- `collisionrelateddocs/Settings Backup/providers.json`
- `docs/data/provider_coverage_matrix.md`
- `docs/reference/generated-packs/ce_system_plans_enhanced/ce_system_plans_enhanced/12_WORK_PACKAGE_PROVIDER_SETTINGS_AND_MIGRATION.md`

