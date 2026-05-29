# EVA Total-Loss Mode

Use this mode for damage assessments that need to fit EVA/Audatex routing conventions or total-loss review.

## Workflow

1. Read the engineer brief, vehicle details, images, and any Audatex/EVA estimate.
2. Route cost lines into labour, paint, parts, and extras using the estimate framework.
3. Keep repair cost and salvage category separate. If a category is required, load `src/skills/salvage-categorisation/`.
4. Check SRS, airbag, ADAS, alloy, geometry, air-conditioning, recovery, storage, and specialist extras where visible or inferable.
5. Produce an AI-assisted draft only; a named engineer signs off before external use.

## Implementation Provenance

Detailed EVA routing and PDF-generation notes live in `references/eva-total-loss-context.md`. The Audatex generator source note lives in `scripts/eva-audatex-generator.py.md`.
