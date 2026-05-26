# Storage Adapter Contract

Box is the first storage integration. Future CCC-owned storage may move to Google Cloud, AWS, or Azure.

## Adapter Boundary

Storage adapters receive a validated case package and return storage references. Parser extraction and EVA export must not know provider-specific SDK details.

## Case Package Contents

- original instruction file;
- original email where available;
- images;
- EVA-ready JSON/payload;
- valuation or companion report where available;
- audit metadata;
- blocker/manual-review notes where relevant.

## Box First

- Folder naming follows case/PO number.
- Metadata must capture principal, claim reference, VRM, source hashes, and upload status.
- Live upload requires credentials and retention decisions outside this scaffold.

## Future Storage

A later architecture decision can choose Google Cloud, AWS, or Azure. Azure remains a serious candidate because Azure Document Intelligence may align document extraction with storage/hosting, but no cloud processing is allowed without privacy, cost, data-residency, and vendor review.
