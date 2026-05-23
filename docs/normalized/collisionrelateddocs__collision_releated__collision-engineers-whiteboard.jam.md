# Normalized Companion: Collision Engineers Whiteboard.jam

- Raw source: `collisionrelateddocs/collision_releated/Collision Engineers Whiteboard.jam`
- SHA256: `710a56041e42fb4755838bd90944b2f69d1c8ba819bea0fd030f21f1e5c2fa31`
- Extraction method: local `.jam` ZIP image export plus Figma `get_figjam` inspection
- Extraction confidence: partial-review-required
- Figma board: https://www.figma.com/board/klGsJGOEG41oP459EbH0ea/Collision-Engineers-Whiteboard?t=1uUOSUp9VtqVuFtN-6
- Figma file key: `klGsJGOEG41oP459EbH0ea`
- Export folder: `docs/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/`
- Image index: `docs/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/image_index.csv`
- Figma inspection summary: `docs/data/jam_exports/collisionrelateddocs__collision_releated__collision-engineers-whiteboard.jam/figma_inspection.md`

This companion is a derivative working copy. The raw source remains the source of truth and must stay unchanged.

## Archive Contents

The `.jam` archive contains:

| Entry | Notes |
| --- | --- |
| `canvas.fig` | Binary FigJam canvas data. Not treated as reliable text source directly. |
| `thumbnail.png` | Exported to the whiteboard image export folder. |
| `meta.json` | Exported to `jam_meta.json`; original export timestamp is `2026-05-22T08:29:55.387Z`. |
| `images/` | 44 embedded image assets exported as `frame-001.png` through `frame-044.png`. |

## Figma Inspection Additions

The connected Figma board was inspected successfully after the board URL was supplied. The node tree confirms and extends the local image review:

- Admin intake splits email into instruction, vehicle images, or query.
- WhatsApp is also a first-class source for images and queries.
- Outlook labels are applied based on instruction type and work provider.
- If instruction and images are both present, the case goes to Table 2, `Ready to Set Up`.
- If anything is missing, the case goes to Table 1, `Not Ready Yet`.
- For some providers CE waits for the garage to send images and repair estimate; for others CE messages the garage on WhatsApp.
- Missing information is chased for up to 4 weeks, then CE closes the file, informs the work provider, and backs up the information to Box.com in case the file is reopened.
- Job setup follows the `EVA Setup Guide` and per-work-provider SOP exceptions.
- Engineers complete the inspection in the EVA integration of Glass's Repair Estimate or in standalone Audatex.
- Inspection reports are backed up to Box.com and delivered by Outlook and/or WhatsApp depending on work provider rules.
- The website form flow uses Stripe checkout. On successful checkout, CE updates spreadsheet paid status and Box URL, creates a Box folder with `Invoice.pdf`, `Summary.txt`, and attachments, sends confirmation email with invoice, and sends CE a new repair estimate request email with form data and Box link.
- Pending-payment jobs are checked every 5 minutes; if payment is pending, no chaser has been sent, and the submission is at least 15 minutes old, a chaser email is sent and the chaser flag is set.

## Embedded Image Evidence Summary

The exported frames include evidence for:

- website repair-estimate spreadsheet and portal form;
- Stripe/payment confirmation and invoice email;
- Box `Repair Estimate Requests` folders with uploaded images, `Invoice.pdf`, and `Summary.txt`;
- Outlook categories and attachment handling;
- WhatsApp image, valuation, query, and report-delivery flows;
- job sheet `NOT READY YET` and `READY TO SET UP` sections;
- local network folder creation from the spreadsheet;
- provider fee-note/report-routing exceptions;
- SOP guide folder references;
- EVA setup guide screenshots;
- `Closed Files` lifecycle evidence.

See `image_index.csv` for per-image dimensions, hashes, archive entries, categories, and descriptions.

## Documentation Implications

- Current CCC docs should distinguish the existing repair-estimate website portal from future external portal/API expansion.
- Work item source metadata should support Outlook, WhatsApp, website portal, Box link, payment state, local-network folder link, and source labels.
- Provider/principal config should cover delivery channel, query handling, fee-note routing, report routing, garage-figures rules, and SOP exceptions.
- Operations docs should include the 4-week missing-information closure rule and Box backup on closure.
- Parser MVP should remain deterministic parser-first; payment automation and live portal integration belong in later phases unless separately approved.
