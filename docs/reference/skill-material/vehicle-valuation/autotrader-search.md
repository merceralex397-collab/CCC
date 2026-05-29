When to read this: read immediately before using the live advert search connector.

# Autotrader Search

Use the Codex app connector:

Tool: `mcp__codex_apps__autotrader._search_cars`

Input schema:

```json
{
  "query": "natural-language vehicle search query",
  "postcode": "optional UK postcode"
}
```

The `query` must describe one make/model combination and can include price range, age, mileage, fuel type, gearbox, body type, colour, and distance. If `postcode` is omitted, the search defaults to national-style results and distance filtering is not available.

Default to national search. Shape the first query as:

`[make] [model] [engine/derivative] [fuel] [gearbox] [body] [year range] around [mileage band]`

For `market_only`, continue searching and broadening until the highest defensible value bracket is stable. Do not stop merely because the first three adverts satisfy the minimum evidence threshold if a nearby, reasonable broadening step could reveal stronger comparable evidence.

Broaden in this order when exact evidence is limited:

1. mileage band
2. trim/specification
3. geography/postcode radius if a postcode is available
4. age
5. engine, fuel, gearbox, or body style only when necessary and clearly explained

For import vehicles, include import terms in at least one search pass where the market supports it. If imported comparators are unavailable, use the best UK-market comparators and record the import/provenance limitation neutrally in the advert notes.

Exclude damaged, Cat S/N unless matching the subject, non-runner, auction-only, materially different, suspicious, or insufficient-detail adverts.
