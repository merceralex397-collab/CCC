# EVA Export Contract v1

## Purpose

EVA export turns a reviewed canonical parser result into EVA-ready JSON and image/package instructions. It does not define CCC's internal data model.

## Export Gates

Export must fail or require review when:

- work provider/principal is missing;
- required dates are missing or not formatted as `DD/MM/YYYY`;
- inspection address is missing and no image-based assessment marker is present;
- mileage, VAT status, or mileage unit constraints fail;
- required provider-specific fields are unresolved;
- image preview ordering has not been reviewed where images are present;
- critical parser warnings remain unresolved.

## Field Order

The EVA JSON field order must match `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json` and be covered by golden tests. Any extra CCC audit metadata must be stored outside the EVA payload if EVA does not support it.

## Image Rules

Image attachment order is controlled by the evidence package/review model:

1. preview full vehicle image;
2. preview close-up damage image;
3. all images, including the first two again.

## Future Sentry/EVA API

Direct Sentry submission is future work. Current research shows the API docs are not enough to treat live submission as a parser MVP requirement. Future work must validate token handling, schema, duplicate prevention, failure recovery, and manual approval.

## Sources

- `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json`
- `docs/research/gptevadeepresearch.md`
- `docs/contracts/parser_result_v1.md`

