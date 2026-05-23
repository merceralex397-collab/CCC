# Business Requirements

## Scope

CCC supports vehicle-damage instruction parsing and evidence preparation for Collision Engineers.

Collision Engineers do not do personal injury or KADOE work. Those workflows are out of scope and must not be planned into CCC.

## Current Workflow

1. Instructions and status evidence currently arrive through multiple channels, including three Outlook mailboxes, the website repair-estimate portal, and WhatsApp.
2. Staff enter details into the CE Job Sheet and keep blocked cases visible as `NOT READY YET` or `READY TO SET UP` according to the evidence available.
3. Staff chase vehicle damage images or other missing information when absent, including email or WhatsApp follow-up according to provider/garage practice.
4. Website repair-estimate submissions can add current evidence such as payment status, `Invoice.pdf`, `Summary.txt`, uploaded images, and Box folder references.
5. Once instructions and images are available, staff enter the case into EVA.
6. Staff add mileage, valuation evidence, Experian/adverse-history checks, and inspection address where required.
7. Images must be added in a required order.
8. Case evidence is stored in Box by case/PO number, with local network folders and closure backups used operationally where relevant.
9. The case is handed to an engineer.

## MVP Requirements

- Preserve current provider parsing behavior before expanding.
- Provide a full UI for office staff.
- Provide equivalent CLI functionality for automation.
- Track missing images/instructions as blockers.
- Generate validated EVA-ready output.
- Preserve raw evidence and source traceability.
- Preserve current source/evidence context from Outlook, website portal/payment status, WhatsApp, Box, and local folder references without making portal/payment automation part of parser MVP.
