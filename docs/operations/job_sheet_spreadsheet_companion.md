# CE Job Sheet Spreadsheet Companion

## Sources

- `docs/reference/raw/collisionrelateddocs/collision_releated/Backup of CE Job Sheet 260429.xlsm`
- `docs/reference/raw/collisionrelateddocs/collision_releated/Backup of CE Job Sheet 260309.xlsm`
- `docs/reference/raw/collisionrelateddocs/collision_releated/Mapped Principals.xlsx`

## Observed Workbook Structure

Both CE Job Sheet backups contain a `Jobs` sheet, `Principals` sheet, and `Garages` sheet. The newer backup also contains `Own figures`.

## Operational Reading

The `Jobs` sheet is the operational queue. Rows near the top include cases missing something or waiting for instructions/images; rows lower in the sheet are jobs ready for EVA once images, instructions, timing, and other blockers are resolved.

The `Principals` sheet is the provider/principal operational lookup. It maps solicitor or work-provider names to EVA codes, Box codes, inbox ownership, instruction receipt style, whether a job can be dragged into EVA, and notes such as direct-job handling or WhatsApp dependence.

The `Garages` sheet is an inspection-address/contact lookup. It contains garage name, address, email, phone, and figure-related notes. This is operationally sensitive and must be treated as raw source data.

`Mapped Principals.xlsx` appears to be a coverage/control sheet linking current parser provider names to known principals, plus lost-cause entries such as `ACSP` where OCR quality is too low.

## Automation Implications

- Do not treat the parser provider config as complete coverage for operational providers.
- Build a provider coverage matrix before adding new parser rules.
- Separate parser preset coverage from EVA/Box principal-code coverage.
- Preserve raw spreadsheet files unchanged. Generated summaries and CSVs are derivative and must link back to source hashes.
- Do not execute workbook macros during source analysis. Macro behavior must be documented separately before any automation depends on it.

## Known Spreadsheet Flow Requirements

- Missing instruction/image cases must remain visible as blocked/manual-review states.
- Jobs can be blocked if images are absent, instructions are absent, images cannot be linked to a case, or the requested date is in the future.
- Garage contact method varies by garage and can include email or WhatsApp outside the workbook.
- Principal code generation resets yearly and must be implemented as a controlled reference generator, not a spreadsheet side effect.
