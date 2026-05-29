When to read this: read before drafting a valuation payload or checking generated PDFs against the example report and evidence pack.

# Example Output Structure

Mirror the two bundled examples structurally: same section order, same section titles, same core table columns, and the same Collision Engineers Ltd header/footer treatment.

## Market Valuation Evidence Report

Use this section order:

1. Header block with `Our Ref`, `Your Ref`, and `Date`.
2. Collision Engineers logo at the top left.
3. Centred title `MARKET VALUATION EVIDENCE`.
4. Subtitle `RE: <Make> <Model> <Derivative> - Registration <REG>`.
5. One-sentence scope paragraph.
6. `SUBJECT VEHICLE DETAILS`.
7. `ASSESSED RETAIL MARKET VALUE`, showing only the engineer's assessed retail value.
8. `MARKET RESEARCH`.
9. `VALUATION COMMENTARY`.
10. `CONCLUSION`.
11. Footer: `Collision Engineers Ltd | www.CollisionEngineers.co.uk | engineers@collisionengineers.co.uk`.

Report advert table columns:

`No.`, `Vehicle / Derivative`, `Year`, `Mileage`, `Seller`, `Asking Price`, `Comment`.

Subject vehicle table wording should stay close to the reference PDF. In the `Vehicle History` row, routine clean-history checks should be rendered as `No adverse history recorded`. Do not add the check provider, check date, or MOT mileage source to this row unless those details disclose a material caveat.

Useful neutral phrases:

- "having regard to make, model, age, mileage, engine, transmission, specification and general condition"
- "selected examples are considered the most relevant vehicles identified from the search results"
- "we consider a retail pre-accident market value of GBP X,XXX.XX to be reasonable for the subject vehicle"
- "The closest comparator identified is the [year] [vehicle] advertised at GBP X. This is closely aligned to the subject vehicle in respect of age, engine, trim, body style and transmission."
- "The wider market evidence includes further [trim/model] examples advertised between GBP X and GBP Y. These examples support the view that a retail market value of GBP Z is reasonable for the subject vehicle."

For internal valuation-tab screenshot inputs, keep the highest visible retail figure in the payload as internal `guide_value` only. Do not describe the source system, `Engineer Value`, `Original Eng Value`, any guide figure, or any increase over a guide figure in the external report.

For `market_only` inputs, keep `valuation_mode` and `guide_value_unavailable_reason` internal only. The generated report and evidence pack should look and read the same as a guide-supported output: same title, same sections, same assessed value presentation, same advert tables, and no wording that explains no guide value was supplied.

Valuation commentary should defend the assessed retail value rather than list reasons against it. Keep caveats short and factual in advert comments only where needed for transparency; do not place undercutting caveats in the core commentary sentence that identifies the closest comparator.

Do not render the report or evidence pack until the required key values listed in `eva-screenshot-intake.md` are available. Ask the user for missing values rather than inserting placeholders.

## Advert Evidence Pack

Use this section order:

1. Same header and footer as the report.
2. Centred title `ADVERT EVIDENCE PACK`.
3. Same `RE:` subtitle.
4. Lead sentence: `Comparable advert references corresponding with the market valuation evidence report.`
5. `ADVERT REFERENCES`.
6. `SEARCH SUMMARY`.

Do not include per-advert detail tables in the external evidence pack. The payload may retain comparability notes, limitations, source URLs, and internal evidence-role fields for audit, but the PDF should mirror the concise reference pack structure.

Evidence pack table columns:

`No.`, `Advert ID`, `Vehicle / Derivative`, `Year`, `Mileage`, `Price`, `Link`.

Links must be clickable in the PDF and displayed as `Open advert`.
