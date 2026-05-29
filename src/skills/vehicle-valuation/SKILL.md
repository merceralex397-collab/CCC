---
name: vehicle-valuation
description: Use this skill whenever the user mentions a UK vehicle valuation, pre-accident value, total loss settlement, diminution, import valuation, guide value challenge, CAP / Cazana / Glass's / HPI comparison, no guide value, market-only valuation, evidence pack, internal valuation-system screenshots, Autotrader live adverts, or asks for a Collision Engineers valuation report or advert evidence pack - even if they have not named the skill. Triggers on vehicle registrations, internal guide values, missing guide values, import vehicles, internal screenshots, and requests to support an engineer's assessed retail value with live market evidence.
---

# Vehicle Valuation

Prepare evidence-led UK vehicle valuations for Collision Engineers Ltd using live market adverts, an optional internal guide value starting point, and the bundled PDF templates.

## Core Workflow

1. Extract the subject vehicle details from typed input or from supplied internal system screenshots using vision. Capture registration, make, model, derivative or trim, body, fuel, transmission, engine, colour, first registration or year, mileage, VIN, and service/history/condition notes where visible.
2. Determine the internal `valuation_mode`:
   - Use `guide_supported` when a guide value is supplied by the user or visible in an internal valuation-tab screenshot.
   - Use `market_only` when the user says the vehicle is an import, no guide value is supplied, or screenshots do not show a usable guide value.
3. Confirm the required vehicle comparison facts are available before live advert searching. In `market_only`, do not ask for a guide value before searching. Ask for missing vehicle facts only when they materially affect comparability.
4. Read these references before drafting the payload:
   - `references/valuation-methodology.md`
   - `references/eva-screenshot-intake.md` when an internal system screenshot is supplied
   - `references/example-outputs.md`
   - `references/report-style.md`
   - `references/autotrader-search.md`
5. Search Autotrader nationally by default for comparable retail examples. Use natural-language queries shaped as `[make] [model] [engine/derivative] [fuel] [gearbox] [body] [year range] around [mileage band]`.
6. Select comparable adverts that are favourable but defensible. Prefer retail/trade adverts and explain any material differences in mileage, age, trim, engine, gearbox, fuel, body style, seller type, specification, provenance, VAT, fees, or location.
7. Build a structured JSON payload containing `subject_vehicle`, `valuation_mode`, `assessed_retail_value`, `evidence_assessment`, `adverts`, `market_research`, `valuation_commentary`, `conclusion`, and optional `vat_note`. Include internal `guide_value` only for `guide_supported`; include internal `guide_value_unavailable_reason` for `market_only`.
8. Do not render PDFs unless the claim or matter reference is available, `evidence_assessment.sufficient_for_pdf` is true, and enough comparable live adverts defend the assessed retail value. If evidence is insufficient, stop and explain that insufficient comparable evidence was located.
9. Render both PDFs:

```powershell
python src/skills/vehicle-valuation/scripts/render_report.py payload.json
python src/skills/vehicle-valuation/scripts/render_evidence_pack.py payload.json
```

The scripts validate the payload first and write the PDF outputs to `output/<REG>/`. Do not place the full internal payload in the external output folder.
Existing PDF outputs are preserved. If a filename already exists for the same registration, the renderer appends `_1`, `_2`, `_3`, and so on.

**Evidence Pack** — advert reference table with clickable links (page 1) followed by one captured Autotrader page per comparable advert (pages 2–N)

## Defaults And Assumptions

- Treat valuations as retail basis unless stated otherwise.
- Assume full service history unless the evidence says otherwise.
- Do not request or consider a client-claimed value unless the user volunteers it.
- Date of loss is not required for live advert searching.
- Do not render PDFs with missing key values or placeholder values such as `Not stated`, `Unknown`, or `To be confirmed`.
- In `market_only`, no guide value is required for searching or payload validation, but `guide_value_unavailable_reason` must record why no guide value was used.
- Ask follow-up questions only when missing information materially affects comparability or valuation.
- For commercial vehicles, read `references/vat-and-commercial-vehicles.md` and capture VAT status, admin fees, and delivery fees where visible.

## Required Key Values

Before searching adverts, obtain:

- Registration.
- Vehicle make/model/derivative or the exact internal `Vehicle` field.
- Mileage.
- Year or first registration date.
- Body style.
- Fuel type.
- Transmission.
- Engine size, engine derivative, or power output.

Before rendering PDFs, also obtain the claim or matter reference for PDF `Your Ref`.

For `guide_supported`, obtain the internal guide value used to set the assessed retail value target. For `market_only`, do not ask for a guide value; record `guide_value_unavailable_reason` instead.

If one screenshot tab does not show all values, combine details from any supplied valuation, vehicle, and overview tabs. If the supplied screenshots and typed prompt still do not provide a required value for the current stage, ask the user for the missing values in one concise follow-up list.

## Internal Screenshot Field Map

When extracting details from internal system screenshots, prefer the labelled fields in the active inspection window:

- Vehicle registration: read the header `Registration` field and place it in `subject_vehicle.registration` and the PDF `Our Ref`.
- Vehicle description: read the header `Vehicle` field. Treat the exact visible text as the primary make/model/derivative wording for PDF display and as the first search seed.
- Claim or matter reference: read `Claim No` or claim reference when present and place it in `meta.your_ref`.
- Internal guide value: on the valuation tab, compare the visible `Retail` prices across sources such as Glass's, cap hpi, Cazana, UK Vehicle Data, Parkers, AutoTrader, and the consolidated retail field. Use the highest visible retail price as internal `guide_value`.
- Audit context: preserve visible fields such as `Principal`, `Insured`, `Reference`, `Engineer`, `Type`, `Guide Month`, `Guide Used`, `Guide Code`, `Incident Date`, source retail/trade values, `Engineer Value`, and `Original Eng Value` in optional internal audit/source context where useful. Never include those audit labels in external PDFs.
- Do not use `Engineer Value` or `Original Eng Value` as the internal `guide_value` for valuation-tab screenshots. They may be retained only as internal audit context.
- If no usable retail guide value is visible and the vehicle comparison facts are available, switch to `market_only` instead of blocking the live advert search.
- Other tabs may show `Reg No`, `Speedo`, body, fuel, transmission, colour, VIN, condition, or history fields. Use those labelled fields to enrich the subject vehicle profile when visible.

If labelled fields disagree, state the discrepancy and proceed with the clearest field only if the intended subject vehicle and required mode-specific values are still obvious.

## Valuation Rules

Shared rules:

- Do not average adverts mechanically. Recommend the strongest client-supportive figure that remains reasonable and defensible.
- Use `scripts/round_valuation.py` only as an advisory rounding helper. The engineer's reasoned judgement remains authoritative.
- Each advert must use `supports_assessed_value` and `evidence_role`. Use roles such as `supportive`, `limiting`, `contextual`, or `excluded`.

For `guide_supported`:

- Aim to support an assessed retail value at least GBP 300 above the internal guide value where defensible.
- Once the live evidence supports a GBP 300-400 increase over the internal guide value, prioritise credibility over forcing a marginally higher figure.
- For higher-value and commercial vehicles, larger differences may be appropriate where evidence supports them.

For `market_only`:

- Search iteratively for comparable vehicles and choose the highest rounded retail value that remains defensible from the live evidence.
- Do not use guide-relative terms, uplift targets, or missing-guide explanations in external wording.
- Treat `supports_assessed_value: true` as meaning the advert can defend the chosen assessed retail value after mileage, specification, provenance, seller type, import status, and other material differences are considered.
- For imports, record import status internally, prefer imported comparators where available, and use standard UK-market comparators only with a clear neutral limitation where import status may affect value.
- Stop broadening the search once at least three suitable adverts and two materially comparable supportive adverts exist and further reasonable broadening does not reveal a higher defensible value bracket.

## External Wording

Use professional, neutral report language. Suitable phrases include "comparable retail market evidence", "relevant live market examples", "current replacement market", "evidence supportive of the assessed retail value", and "the selected examples are considered sufficiently comparable to the subject vehicle".

The external report and evidence pack must not materially differ between `guide_supported` and `market_only`. Do not include mode labels, guide availability notes, missing-guide explanations, or internal workflow descriptions. Both modes should read as the same professional market valuation evidence report.

Keep the `Vehicle History` row concise and close to the reference report. For routine clean-history checks, write `No adverse history recorded`. Do not expand this row with the history-check provider, check date, or MOT mileage source unless there is a material history point, mileage discrepancy, adverse marker, or other caveat that must be disclosed.

Do not use internal strategy language in external PDFs, including "cherry-picked", "highest adverts found", "client-favourable only", "selected to increase value", "we ignored lower adverts", "EVA", "Engineer Value", "Original Eng Value", "guide value", "guide valuation", "guide price", or "uplift".

For valuation commentary, follow the reference report style closely: closest comparator, why it aligns with the subject vehicle, wider market evidence, then the assessed retail value. Do not argue against the assessed retail value in the core commentary. Avoid undercutting phrases such as "although it has lower mileage" or "but with much lower mileage" when explaining the closest comparator.

## Chat Response

After rendering, reply briefly with the subject, assessed retail value, short reasoning, and links to both generated PDFs. Do not mention internal guide figures, missing guide values, valuation mode, or the concept of an increase over the guide figure in chat summaries.
