When to read this: read whenever the user provides an internal valuation-system screenshot or asks to extract vehicle details from an internal system image.

# Internal Screenshot Intake

Internal valuation-system screenshots show the subject vehicle in a tabbed inspection window. Extract from the labelled fields rather than guessing from nearby text. No single tab should be assumed to contain the full valuation input set.

Before searching adverts or rendering PDFs, combine the supplied typed details and all supplied screenshots. If a required vehicle comparison value is still missing, ask the user for the missing values and stop until they provide them. A missing guide value alone should switch the workflow to `market_only` rather than block advert searching.

## Primary Field Mapping

- `Registration` = subject vehicle registration. Put this into `subject_vehicle.registration` and use it as `Our Ref` in the PDF.
- `Vehicle` = primary visible make/model/derivative text. Preserve the exact visible text in `subject_vehicle.vehicle_description` where possible, use it for the PDF subject line/details, and split it into `make`, `model`, and `derivative` only as needed for searching and schema compatibility.
- `Claim No` or claim reference = claim or matter reference. Put this into `meta.your_ref` for the report header.
- Highest visible `Retail` guide price = `guide_value`. Compare the retail values shown by the visible valuation sources and the consolidated retail field.
- `Reference` = internal inspection reference. Keep for audit notes if useful; do not substitute it for `Claim No` unless the user specifically asks.

## Required Before Search Or PDF

Ask the user for any of these before advert searching if not visible or supplied:

- Registration.
- Vehicle make/model/derivative or exact `Vehicle` text.
- Mileage.
- Year or first registration date.
- Body style.
- Fuel type.
- Transmission.
- Engine size, engine derivative, or power output.

Before PDF rendering, also obtain the claim or matter reference for `Your Ref`.

For `guide_supported`, obtain the internal guide value used to set the assessed retail value target. If no usable retail guide value is visible or supplied, use `market_only` and record `guide_value_unavailable_reason` internally.

Do not proceed to PDF generation with placeholder values such as `Not stated`, `Unknown`, `Not visible`, or `To be confirmed`.

## Tab Roles

- `Valuation` tab: guide values, source retail/trade values, guide month/source/code, incident date, valuation audit context, and header case fields. It usually does not show mileage or full vehicle specification.
- `Vehicle` tab: vehicle details for advert comparability, including `Reg No`, `Speedo`, body/body description, transmission, fuel, cc, engine BHP, year made, first registration, model ID, VIN, colour, condition, notes, damage/roadworthiness notes, and vehicle history notes. It usually does not show guide value.
- `Overview` tab: case/admin context, including principal, insured, claim number, policy number, inspection type, inspection dates, location, report dates, fees, file status, and progress notes. It usually does not show guide value or full vehicle specification.

## Guide Value Rule

For valuation-tab screenshots, use the highest visible retail price shown on the screen as internal `guide_value`. Sources may include Glass's, cap hpi, Cazana, UK Vehicle Data, Parkers, AutoTrader, and the consolidated `Retail` field in the lower panel.

Do not use `Engineer Value` or `Original Eng Value` to set `guide_value` in this flow. Those fields may be captured in audit/source context, but they are not the internal guide price for the skill and must never appear in external PDFs.

If no usable retail guide price is visible, do not infer one from `Engineer Value`, `Original Eng Value`, or other audit fields. Use `market_only` and set `guide_value_unavailable_reason` to a concise internal reason such as `no usable retail guide value visible`.

If a retail value appears in both a source panel and the consolidated lower-panel `Retail` field, treat that as the same visible guide evidence rather than a separate comparator. If retail prices differ, select the highest visible retail price and retain the other visible figures in audit context.

## Other Useful Fields And Audit Context

- `Body Type` and `Body Desc` = body style. Prefer the more descriptive field when they differ.
- `Transmission` = gearbox.
- `Fuel` = fuel type.
- `C.C.` = engine size in cc.
- `Engine BHP` = power output.
- `Year Made` and `1st Reg'd` = year and first registration date.
- `Colour` = colour.
- `VIN No` = VIN.
- `Condition`, `Eng Notes on Vehicle`, `VRM Notes`, and `Vehicle History Check` = condition, history, damage, MOT/history assumptions, and caveats. For a routine clean history check, set the external `Vehicle History` wording to `No adverse history recorded`; do not repeat the provider name, check date, or MOT mileage source unless it is a material caveat.
- `Principal`, `Insured`, `Reference`, `Engineer`, `Type`, `Guide Month`, `Guide Used`, `Guide Code`, `Incident Date`, source retail/trade values, `Adverts`, `Values adjusted`, `Prev TL Adjust`, `Engineer Value`, and `Original Eng Value` = optional audit/source context.

## Conflict Handling

If registration fields differ across tabs, do not silently choose one. State the conflict and ask only if the intended registration is not obvious from the screenshot or prompt.

If the `Vehicle` field is truncated, use visible separate fields such as fuel, transmission, cc, body, year, and notes to complete the subject vehicle profile. State any assumptions clearly.

If Speedo appears unusually high or a note says mileage was converted from kilometres, record the displayed Speedo value and include the note in vehicle history or valuation commentary where it affects comparability.

## Sample Screenshot Expectations

The sample screenshots under `tests/sample_screenshots/` demonstrate the expected extraction pattern:

- Treat `tests/sample_screenshots/full_window/` and `tests/sample_screenshots/small_window/` as separate case examples, not paired screenshots of the same vehicles.
- For each sample, extract `Registration`, `Claim No`, `Vehicle`, all visible retail guide prices, and select the highest visible retail guide price as `guide_value`.
- See `tests/fixtures/eva_screenshot_field_map.md` for the expected sample-level field map.
