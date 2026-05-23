# 15 — Demo Dataset and Test Plan

Generated: 2026-05-22

## Principle

Use synthetic data only for the first demo. The documents should look realistic enough to show value, but contain no real claimant, client, vehicle or insurer data.

## Demo case set

### Case A — Complete desktop damage assessment

**Purpose:** show the happy path.

Files:

- instruction PDF;
- Audatex-style estimate PDF;
- 8 vehicle images;
- short email note.

Expected output:

- case created;
- registration extracted;
- claim ref extracted;
- estimate parsed;
- images matched;
- status `ready_for_engineer`;
- engineer pack generated;
- no blocking missing items.

### Case B — Missing images

**Purpose:** show missing-info chaser.

Files:

- instruction PDF;
- estimate PDF;
- only 1 close-up image.

Expected output:

- status `awaiting_images`;
- missing front/rear/nearside/offside images;
- chaser draft generated;
- pack includes missing-info warning.

### Case C — Registration mismatch

**Purpose:** show low-confidence admin review.

Files:

- instruction for AB12 CDE;
- estimate for AB12 CDF;
- images named `AB12CDE_damage_1.jpg`.

Expected output:

- match confidence below threshold;
- `vehicle_reg_mismatch` review flag;
- status `needs_admin_review`;
- no automatic high-confidence match.

### Case D — Possible duplicate

**Purpose:** show duplicate-case control.

Files:

- two uploads with same reg and claim ref;
- overlapping image filenames.

Expected output:

- `possible_duplicate` status;
- merge/split controls visible;
- match reasons include registration and claim ref.

### Case E — Supplementary estimate

**Purpose:** show estimate review flags.

Files:

- instruction PDF;
- original estimate PDF;
- supplementary estimate PDF.

Expected output:

- supplementary detected;
- engineer question added: compare original and supplementary;
- pack lists both estimates.

### Case F — ABP/charge dispute

**Purpose:** show later-phase charge-review value.

Files:

- insurer challenge note;
- repair invoice/estimate with wheel alignment, ADAS calibration, QC time and environmental charge;
- images.

Expected output:

- ABP charge-review flags;
- required evidence list;
- draft internal review note, not final rebuttal.

### Case G — Unknown/unrelated attachment

**Purpose:** show classifier restraint.

Files:

- unrelated PDF;
- unrelated image.

Expected output:

- document classified as `unknown`;
- no auto-created valid case;
- admin review required.

## Synthetic instruction PDF fields

Each synthetic instruction should include:

- work provider;
- contact email;
- vehicle registration;
- vehicle make/model;
- claim reference;
- client reference;
- date of loss;
- instruction date;
- required report type;
- desktop/physical preference;
- location;
- special questions;
- list of attachments.

## Synthetic estimate PDF fields

Each estimate should include:

- repairer name;
- estimate reference;
- vehicle registration;
- VIN;
- estimate date;
- parts total;
- labour total;
- paint total;
- VAT;
- grand total;
- sample operations;
- optional ADAS/alignment/SRS keywords;
- optional supplementary marker.

## Required image set for a complete demo case

- full front;
- full rear;
- nearside;
- offside;
- close-up damage 1;
- close-up damage 2;
- odometer;
- VIN/chassis plate, if available.

## Acceptance tests

| Test | Expected result |
|---|---|
| Upload mixed files | All files stored and listed. |
| Classify instruction PDF | Type = `instruction_pdf` with confidence. |
| Classify estimate PDF | Type = `audatex_estimate` or `repair_estimate`. |
| Extract vehicle reg | Correct field extracted from instruction. |
| Extract claim ref | Correct field extracted. |
| Parse estimate total | Parts/labour/paint/VAT/total extracted. |
| Match by reg/ref | Matching evidence attached to same case. |
| Mismatch case | Low confidence and review flag. |
| Missing images | Status set to `awaiting_images`. |
| Chaser draft | Missing items reflected accurately. |
| Generate pack | Pack includes case summary, documents, images, estimate, missing items, engineer questions. |
| Audit event | Each major action logged. |
| Unknown document | Does not force classification. |

## Regression tests

Run these after every change:

1. Good case still reaches `ready_for_engineer`.
2. Mismatch case still requires review.
3. Missing-images case still generates chaser.
4. Unknown document remains unknown.
5. Pack generator does not create final technical opinions.
6. Original uploaded files are never modified.
7. Audit log records AI module name and timestamp.

## Pack content QA checklist

The generated engineer pack must include:

- vehicle registration;
- claim reference;
- report type;
- instruction summary;
- documents received;
- image schedule;
- estimate summary;
- missing information;
- review flags;
- engineer questions;
- confidence summary;
- audit trail summary;
- clear statement that the pack is for human review.

## Chaser message QA checklist

A chaser draft must:

- identify the vehicle/reference;
- state what has been received;
- state what is missing;
- request only factual evidence;
- avoid technical conclusions;
- avoid allegations;
- be copy/approval only in demo.

## Demonstration script

1. Open dashboard and show empty/new holding pen.
2. Load demo data for complete case.
3. Run processing.
4. Show extracted fields and confidence.
5. Approve suggested matches.
6. Generate engineer pack.
7. Load missing-images case.
8. Show missing items and chaser draft.
9. Load mismatch case.
10. Show low-confidence review and match reasons.
11. Open activity log and show traceability.
12. Close by reiterating that engineer judgement is untouched.
