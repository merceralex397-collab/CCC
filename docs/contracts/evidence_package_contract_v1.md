# Evidence Package Contract v1

## Purpose

An evidence package is a deterministic local folder and manifest that can be placed into Box now and uploaded by a future storage adapter later.

## Folder Naming

Preferred folder name is reviewed `case_po`. If not available, use `work_item_id` plus VRM when available. Do not invent a case/PO silently.

## Required Contents

| Content | Required | Notes |
| --- | --- | --- |
| Original instruction files | yes | Preserve exact original files. |
| Original email | when available | `.eml` or `.msg` source retained. |
| Evidence images | yes if available | Include all images. |
| Preview image decision | yes | First preview must be full view where available; second preview must be close-up damage where available. |
| EVA JSON export | when generated | Preserve exact exported file and hash. |
| Companion report | when available | Valuation/service report or other supporting PDF. |
| Notes | when available | Staff or source notes. |
| Manifest | yes | Machine-readable package metadata and checksums. |

## Image Ordering Rule

EVA/package preparation must support:

1. first preview image: full vehicle view where available;
2. second preview image: close-up of vehicle damage where available;
3. all images attached after previews, including the first two again.

If staff cannot identify preview images, package generation must record a warning and require review.

## Manifest Fields

- `package_id`;
- `work_item_id`;
- `case_po`;
- `principal_code`;
- `claim_reference`;
- `vrm`;
- `generated_by`;
- `generated_at`;
- `source_files` with path, role, size, hash;
- `image_order` with preview flags;
- `eva_export_id` when present;
- `warnings`;
- `storage_status`.

