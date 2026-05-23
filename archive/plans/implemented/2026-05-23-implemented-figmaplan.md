# Implemented State

- Status: implemented
- Implemented date: 2026-05-23
- Delivered summary: FigJam/Jam export evidence was reviewed and promoted into canonical documentation for current portal, payment, Box, Outlook, WhatsApp, job-sheet, SOP, and provider-routing context; source manifests were updated for the Jam derivatives and archived plan lifecycle.
- Verification performed: `python tools\verify_scaffold.py`, manifest consistency checks, Jam export file count check, and targeted checks for `.obsidian` ignore/removal from tracking.
- Follow-up work moved elsewhere: Future portal/payment/WhatsApp automation, vendor/security governance, and implementation of optional metadata/routing fields remain in roadmap tickets and contract follow-up work.

---

# Whiteboard Evidence Capture And Documentation Update Plan

## Summary

Retry Figma MCP, capture the useful local `.jam` evidence safely, and update CCC docs with the extra workflow context found in the whiteboard images.

Figma connector usage is now successful. The board at https://www.figma.com/board/klGsJGOEG41oP459EbH0ea/Collision-Engineers-Whiteboard?t=1uUOSUp9VtqVuFtN-6 was inspected with Figma `get_figjam` against root node `0:1`.

Do not save extracted derivatives back into `collisionrelateddocs/`. That folder is raw immutable evidence under `AGENTS.md`. Keep the raw `.jam` there, and save extracted images/data under `docs/data/`.

## Implementation Status

| Section | Status | Notes |
| --- | --- | --- |
| Figma connector retry and whiteboard inspection | completed | Authenticated connector was available after retry; board URL was inspected with `get_figjam`. |
| Local `.jam` image/data export | completed | 44 embedded images, thumbnail, metadata JSON, image index, Figma inspection summary, and contact sheets were saved under `docs/data/jam_exports/`. |
| Canonical documentation promotion | completed | Target docs were updated with the workflow context listed below while keeping automation scope in future tickets. |

## Jam Export Evidence Reviewed

All files currently under `docs/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/` were reviewed for this documentation pass: 56 files total, comprising 1 metadata JSON, 1 image index CSV, 1 Figma inspection summary, 8 contact sheets, 44 frame images, and 1 thumbnail image.

| Evidence file or group | What it contributes | Use in this plan |
| --- | --- | --- |
| `jam_meta.json` | Source `.jam` path, source SHA256, Figma board URL, Figma file key, local export timestamp, original Jam export timestamp, render coordinates, and inspection status. | Establishes traceability back to immutable raw evidence and confirms the Figma/local extraction status. |
| `image_index.csv` | Per-image sequence, source archive entry, export path, source hash, image hash, byte size, dimensions, category, and short description. | Acts as the coverage ledger for every exported frame and the thumbnail. |
| `figma_inspection.md` | Node-level workflow notes from Figma `get_figjam`: intake splitting, query handling, WhatsApp evidence handling, job setup, report delivery, website form flow, payment chaser timing, 4-week missing-info closure, and Box backup on closure. | Supplies workflow context that is not always visible from the frame screenshots alone. |
| `contact_sheets/whiteboard-images-01.jpg`, `contact_sheets/whiteboard-images-02.jpg`, `contact_sheets/whiteboard-images-03.jpg`, `contact_sheets/whiteboard-images-04.jpg`, `contact_sheets/whiteboard-images-05.jpg`, `contact_sheets/whiteboard-images-06.jpg`, `contact_sheets/whiteboard-images-07.jpg`, `contact_sheets/whiteboard-images-08.jpg` | Visual review sheets covering `frame-001.png` through `frame-044.png`. | Used as visual verification that the frame-level categories and descriptions match the screenshots. |
| `images/thumbnail.png` | Jam/FigJam overview thumbnail showing the whiteboard layout and major channel/process clusters. | Evidence and orientation only; not a functional requirement. |
| `images/frame-001.png` through `images/frame-044.png` | Direct extracted frame evidence listed in the matrix below. | Source images for the documentation-impact findings. |

## Source Evidence To Documentation Impact Matrix

| Evidence theme | Source files reviewed | Specific information to add or preserve |
| --- | --- | --- |
| Website repair-estimate portal | `frame-001.png`, `frame-005.png`, `frame-007.png`, `frame-008.png`, `frame-010.png`, `frame-032.png`, `frame-034.png`, `frame-043.png`; supported by `image_index.csv` and `figma_inspection.md` | Current portal context exists now, not only as future portal work. It captures request ID/time, repairer or contact name, contact number, email address, vehicle registration, comments, uploaded vehicle images, paid status, Box folder URL, and the CE-facing new repair-estimate request email. |
| Payment and invoice flow | `frame-003.png`, `frame-013.png`, `frame-028.png`, `frame-040.png`; supported by `figma_inspection.md` | Checkout/payment evidence for a Collision Engineers/Audatex assessment, payment-received confirmation, `Invoice.pdf`, current test recipients, and pending-payment chaser logic: every 5 minutes for submissions at least 15 minutes old where payment is pending and no chaser has been sent. |
| Box and package lifecycle | `frame-009.png`, `frame-024.png`, `frame-031.png`; supported by `figma_inspection.md` | Box is used for `Repair Estimate Requests`, per-request folders, uploaded images, `Invoice.pdf`, `Summary.txt`, `Closed Files`, and backup on closure when missing information is not supplied within the chase window. |
| Outlook intake and categories | `frame-002.png`, `frame-004.png`, `frame-012.png`, `frame-019.png`, `frame-027.png`, `frame-030.png`, `frame-044.png`; supported by `figma_inspection.md` | Outlook is a current intake/status channel. Evidence includes instruction emails, attachments, `Green category`, `Red category`, `PCH Audit`, `Logged on sheet`, query folder/label handling, and image attachments. |
| WhatsApp workflows | `frame-006.png`, `frame-011.png`, `frame-014.png`, `frame-026.png`, `frame-029.png`, `frame-033.png`, `frame-037.png`, `frame-038.png`, `frame-039.png`; supported by `figma_inspection.md` | WhatsApp is current operational evidence/status/query traffic, not just a future communications idea. Evidence includes image and estimate chasers, valuation/right-off queries, supplement queries, report PDF delivery, and QDOS authorisation notes. |
| Job-sheet states and actions | `frame-016.png`, `frame-023.png`, `frame-025.png`, `frame-041.png`, `frame-042.png`; supported by `figma_inspection.md` | Operational queue terminology and actions include `READY TO SET UP`, `NOT READY YET`, columns `Date`, `VRM`, `Principal`, `Client`, `Vehicle`, `Missing`, `Due`, `Notes`, and actions/links such as `Create Folder`, local network path, `Move Up`, and `Move Down`. |
| SOP, setup, and provider routing | `frame-017.png`, `frame-018.png`, `frame-021.png`, `frame-022.png`, `frame-035.png`, `frame-036.png`; supported by `figma_inspection.md` | SOP inventory includes `UN-RW REASONS SOP.xlsx`, `Report Sending SOP Guide.docx`, `PCH SOP Guide.docx`, `AX SALVAGE.xlsx`, `SBL SOP Guide.docx`, `QDOS SOP Guide.docx`, and `EVA Setup Guide.docx`. Provider routing evidence includes separate fee-note exceptions for `QDOS`, `QCL`, `AX`, `FW`, `OAK`, and `ALS`, plus reply/CC/routing handling. |
| Branding and visual context | `frame-015.png`, `frame-020.png`, `thumbnail.png`; supported by contact sheets | Collision Engineers branding and whiteboard overview are useful visual references only. They should not be promoted into parser, workflow, or contract requirements. |

## Project-Wide Docs That Could Benefit

The following are candidate downstream documentation updates. They should be handled in later scoped edits rather than changing all files in this pass.

| Candidate doc | Information to add from Jam export evidence |
| --- | --- |
| `README.md` | Acknowledge that current operational evidence includes portal, WhatsApp, and Box context while keeping parser/Operational Core MVP scope unchanged. |
| `docs/requirements/business_requirements.md` | Update the current workflow so it no longer implies Outlook email is the only current intake channel; include website portal and WhatsApp as current evidence/status sources. |
| `docs/operations/job_sheet_spreadsheet_companion.md` | Add exact job-sheet states, columns, and actions: `READY TO SET UP`, `NOT READY YET`, `Date`, `VRM`, `Principal`, `Client`, `Vehicle`, `Missing`, `Due`, `Notes`, `Create Folder`, local network folder link, `Move Up`, and `Move Down`. |
| `docs/contracts/work_item_contract_v1.md` | Consider future metadata fields for source channel, source labels, portal submission ID, payment status, Box URL, local folder URL, and closure reason. |
| `docs/contracts/provider_principal_config_contract_v1.md` | Add provider delivery channel, query owner, fee-note, reply-to, reply-all, CC, garage-figures, and special-case routing concepts. |
| `docs/contracts/evidence_package_contract_v1.md` | Add website repair-estimate package contents such as uploaded images, `Invoice.pdf`, `Summary.txt`, source form data, and payment/portal metadata. |
| `docs/contracts/storage_adapter_contract_v1.md` | Add Box folder references, package stage, live-upload references, and closed-file/archive references as future adapter metadata. |
| `docs/architecture/future_system_convergence.md` | Distinguish current portal/payment/WhatsApp evidence from future automation; attach these channels to the work-item/source/evidence spine. |
| `docs/roadmap.md` and tickets `docs/tickets/p1-operational-core-mvp.md`, `docs/tickets/p3-integrations-storage-eva-intake.md`, `docs/tickets/p4-intelligence-engineer-communications.md`, `docs/tickets/p5-platform-expansion.md` | Track current portal/payment/WhatsApp evidence without moving autonomous sending, live payment automation, or external portal/API implementation into parser MVP. |
| `docs/security/data_map.md`, `docs/security/dpia_vendor_governance.md`, `docs/security/vendor_register.md`, and `docs/integrations/external_services.md` | Add website portal, Stripe/Amazon Pay checkout, WhatsApp, Google Drive/SOP evidence, and live Box upload as governance or vendor-review candidates where appropriate. |
| `docs/glossary.md` | Add or refine terms for `Ready to Set Up`, `Not Ready Yet`, `fee note`, `repair estimate request`, `source channel`, and `Box folder`. |
| `docs/source_manifest.md`, `docs/source_manifest.csv`, `docs/source_manifest.json` | Keep Jam export derivatives represented and traceable whenever source files, generated companions, active docs, or archives change. |

## Candidate Interface And Contract Notes

No immediate code, schema, or contract change is planned from this pass. Future documentation and contract work should treat the following as candidate metadata only, not hardcoded parser behavior:

- work-item/source metadata: `source_channel`, `source_category`, `source_labels`, `portal_submission_id`, `payment_status`, `payment_chaser_sent`, `box_folder_url`, `box_folder_stage`, `local_network_folder_url`, and `closed_file_reason`;
- provider routing metadata: delivery channel, query owner, reply-to handler, reply-all rule, CC list, fee-note rule, garage-figures rule, missing-info chase limit, and provider special-case notes.

## Key Changes

- Export `.jam` contents to:
  - `docs/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/images/frame-001.png` onward.
  - `docs/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/image_index.csv`.
  - Optional contact sheets under the same export folder for review.
- Update the normalized whiteboard companion with:
  - `.jam` ZIP contents: `canvas.fig`, `thumbnail.png`, `meta.json`, and 44 embedded images.
  - source hash, export timestamp from `meta.json`, per-image hashes, dimensions, and short human descriptions.
  - Figma MCP retry status and local-extraction fallback.
- Add whiteboard insights to canonical docs:
  - current repair-estimate website portal exists now, with form, payment, Box folder, invoice, summary text, and spreadsheet tracking.
  - WhatsApp is a current evidence/status channel, not just a future communications channel.
  - operational queues are explicitly `NOT READY YET` and `READY TO SET UP`, with columns `Date`, `VRM`, `Principal`, `Client`, `Vehicle`, `Missing`, `Due`, `Notes`.
  - Outlook categories include `Green category`, `Red category`, `PCH Audit`, and `Logged on sheet`.
  - provider/principal config must include fee-note and report-routing rules, including exceptions for `QDOS`, `QCL`, `AX`, `FW`, `OAK`, and `ALS`.
  - Box lifecycle needs `Repair Estimate Requests`, per-request folders, Box links, and `Closed Files`.
  - SOP evidence includes EVA Setup Guide, Report Sending SOP, PCH SOP, SBL SOP, QDOS SOP, and AX Salvage references.
  - Figma node-level review adds: website Stripe checkout, paid-status and Box URL update, `Invoice.pdf` and `Summary.txt` package creation, current test recipients `digital@` and `ed@`, pending-payment chaser check every 5 minutes after 15 minutes, query routing via Outlook query folder/labels, 4-week missing-info closure, Box backup on closure, and report delivery by Outlook and/or WhatsApp according to provider rules.
- Update contracts/backlog so these are modeled as future-capable fields, not hardcoded parser behavior:
  - `source_channel`, `source_category`, `source_labels`, `portal_submission_id`, `payment_status`, `payment_chaser_sent`, `box_folder_url`, `box_folder_stage`, `local_network_folder_url`, and `closed_file_reason`.
  - provider routing fields for inbox, query owner, delivery channel, reply-to-handler, reply-all, CC list, fee-note handling, garage-figures rule, missing-info chase limit, and special-case notes.

## Target Docs

Update the relevant canonical docs rather than only reference packs:

- `docs/normalized/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam.md`
- `docs/operations/job_sheet_spreadsheet_companion.md`
- `docs/contracts/work_item_contract_v1.md`
- `docs/contracts/provider_principal_config_contract_v1.md`
- `docs/contracts/evidence_package_contract_v1.md`
- `docs/contracts/storage_adapter_contract_v1.md`
- `docs/architecture/future_system_convergence.md`
- `docs/requirements/business_requirements.md`
- `docs/tickets/p1-operational-core-mvp.md`
- `docs/tickets/p3-integrations-storage-eva-intake.md`
- `docs/tickets/p5-platform-expansion.md`
- `docs/source_manifest.md`, `.csv`, and `.json`

## Test Plan

- Verify the export folder contains all embedded `.jam` images plus index metadata.
- Verify every exported image has a hash, dimensions, source archive entry, and human description.
- Verify manifest files include new derivatives and updated whiteboard extraction status.
- Verify Figma inspection summary includes the Stripe/payment chaser flow, query routing, 4-week closure rule, Box backup rule, and delivery-channel rule.
- Verify docs no longer imply Outlook is the only current intake channel.
- Verify portal/payment/WhatsApp/fee-note routing are documented without moving them into parser MVP scope.
- Run `python tools\verify_scaffold.py`.

## Assumptions

- Raw `collisionrelateddocs/` remains immutable; extracted images are derivatives and belong under `docs/data/`.
- Repair-estimate portal and payment flow are real current workflow context, but automation for portal/payment remains future-phase unless separately approved.
- Figma connector inspection is now available, but the local `.jam` export remains useful as a stable derivative evidence bundle.
