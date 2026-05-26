# EVA Export Contract

EVA-ready means local validation and manual review, not direct Sentry submission.

## Export Requirements

- Preserve the field order and shape represented by `docs/reference/raw/collisionrelateddocs/Final Format Example 02.json`.
- Export only after required parser warnings are reviewed.
- Include source audit metadata outside the EVA payload when EVA does not support it.
- Keep image ordering requirements separate from field JSON: first two preview images, then all images including the first two again.

## Open Items

- Confirm final EVA JSON field names against live EVA import behavior.
- Add golden tests for all 26 parser presets.
- Decide how manual corrections are represented in audit metadata.
