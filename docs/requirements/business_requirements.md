# Business Requirements

## Scope

CCC supports vehicle-damage instruction parsing and evidence preparation for Collision Engineers.

Collision Engineers do not do personal injury or KADOE work. Those workflows are out of scope and must not be planned into CCC.

## Current Workflow

1. Instructions arrive by email in three Outlook mailboxes.
2. Staff enter details into the CE Job Sheet.
3. Staff chase vehicle damage images when absent.
4. Once instructions and images are available, staff enter the case into EVA.
5. Staff add mileage, valuation evidence, Experian/adverse-history checks, and inspection address where required.
6. Images must be added in a required order.
7. Case evidence is stored in Box by case/PO number.
8. The case is handed to an engineer.

## MVP Requirements

- Preserve current provider parsing behavior before expanding.
- Provide a full UI for office staff.
- Provide equivalent CLI functionality for automation.
- Track missing images/instructions as blockers.
- Generate validated EVA-ready output.
- Preserve raw evidence and source traceability.
