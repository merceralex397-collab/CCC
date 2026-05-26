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
| Website uploaded images | when source is portal | Preserve all uploaded repair-estimate images exactly as submitted. |
| `Invoice.pdf` | when source is portal/payment | Preserve generated invoice evidence alongside the request package. |
| `Summary.txt` | when source is portal/payment | Preserve form-data summary created for the request package. |
| Source form data | when source is portal | Preserve request fields such as contact, VRM, comments, and timestamps in the manifest/package. |
| Payment and portal metadata | when source is portal | Preserve status evidence such as portal submission id, paid/pending state, and chaser flag if recorded. |
| Box folder reference | when available | Preserve the Box folder URL/id that ties the package back to operational storage. |

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
- `source_channel`;
- `portal_submission_id`;
- `payment_status`;
- `payment_chaser_sent`;
- `box_folder_url`.
