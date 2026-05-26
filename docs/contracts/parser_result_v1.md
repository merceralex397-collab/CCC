# Parser Result Contract v1

Parser output is canonical before it becomes EVA-specific.

## Required Concepts

- source file path and hash;
- detected provider and provider confidence;
- extracted fields with value, confidence, source span/page where available, and warning state;
- validation warnings;
- image extraction/package metadata;
- audit metadata for tool version and extraction methods.

## Core Fields

- work provider/principal;
- VRM;
- vehicle model;
- claimant/client name;
- client claim/reference number;
- incident date;
- instruction date;
- inspection date;
- inspection address or image-based assessment marker;
- accident circumstances;
- VAT status;
- mileage and mileage unit;
- evidence image list.

## Rule

EVA field shape is an export adapter. Do not let EVA-specific JSON become the only internal representation.
