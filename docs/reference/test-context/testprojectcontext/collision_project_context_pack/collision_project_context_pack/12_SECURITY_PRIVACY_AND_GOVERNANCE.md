# Security, Privacy, and Governance

## Purpose

Define controls for handling emails, PDFs, images, extracted data, Box storage, and EVA imports.

## Likely data sensitivity

The workflow may include personal data, business confidential data, vehicle information, claims/instruction references, images, and possibly incident-related details. The exact classification must be confirmed during discovery.

## Data protection principles

For UK operations, design should align with UK GDPR principles such as lawfulness, fairness and transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity/confidentiality, and accountability.

This document is not legal advice. It is an engineering governance guide and should be reviewed by the organisation’s data/privacy owner.

## Access control

### Outlook

- Use least-privilege Microsoft Graph permissions.
- Prefer a dedicated intake/shared mailbox over monitoring personal mailboxes.
- Restrict who can configure mailbox rules and automation subscriptions.
- Log which app/service account accessed emails.

### Box

- Use a service account/app integration with only required folders/scopes.
- Restrict source files to staff who need them.
- Avoid broad developer access to production case files.
- Use metadata for classification and retention.

### EVA

- Use a dedicated integration identity where possible.
- Avoid shared human credentials for automation.
- Store secrets in a secure vault.
- Rotate credentials and document ownership.

## Secrets management

Secrets include:

- Microsoft Graph client secret/certificate.
- Box API credentials.
- EVA API keys or import credentials.
- Database credentials.
- Encryption keys.

Requirements:

- Never store secrets in spreadsheets, source code, or markdown files.
- Use a managed secrets store.
- Restrict access by role.
- Rotate on a defined cadence or when staff leave.

## Audit trail

Every work item should be traceable:

```text
source email -> attachments -> Box files -> extraction output -> review decisions -> EVA payload -> EVA response
```

Audit events should include:

- Actor: automation service or human user.
- Timestamp.
- Action.
- Work item ID.
- Before/after values for human corrections.
- Error codes/responses where relevant.

## Data minimisation

Only extract and store fields required for the process. Do not extract additional personal details simply because they appear in the PDF.

## Retention

Define how long to keep:

- Original emails.
- Source PDFs.
- Images.
- Extracted JSON.
- Review events.
- EVA payloads/responses.
- Logs.

Avoid indefinite retention unless there is a documented business/legal reason.

## Logging rules

Logs should help debugging without exposing unnecessary personal data.

Recommended:

- Log work item IDs and status transitions.
- Log file IDs, not full file content.
- Redact or avoid full email bodies in technical logs.
- Store full extraction outputs in controlled Box/database locations, not generic application logs.

## AI/data-processing controls

If third-party AI/OCR services are used, verify:

- Whether customer data is retained for model training.
- Data processing location/region.
- Contract/data processing terms.
- Security certifications.
- Access logging.
- Retention period.
- Ability to delete data.

## Human review privacy

Review interfaces should avoid showing more data than reviewers need. For example, if a reviewer only needs to correct a vehicle registration and reference number, the UI should not expose unrelated personal details by default.

## Incident and breach handling

Prepare a breach/incident runbook covering:

- Accidental upload to wrong Box folder.
- Incorrect EVA record creation.
- Email processed from an unauthorised sender.
- Data sent to an unauthorised third-party service.
- Lost or leaked credentials.

Record the facts, impact, and remedial action for incidents.

## Governance roles

| Role | Responsibility |
|---|---|
| Business owner | Defines process, priorities, and acceptance criteria. |
| Data/privacy owner | Reviews personal data handling and retention. |
| Technical owner | Owns integration architecture and service reliability. |
| EVA owner/vendor contact | Provides EVA schema/API/import details. |
| Box admin | Manages Box app access, folders, metadata, retention. |
| Microsoft 365 admin | Manages app registration and mailbox permissions. |
| Operations reviewer | Handles exceptions and provides feedback. |

## Security checklist

- Dedicated service accounts/integration identities.
- Least-privilege permissions.
- Secrets in a vault.
- Encrypted storage and transport.
- Audit log for every state transition.
- Controlled production data access.
- Retention rules.
- Incident runbook.
- Regular access reviews.
- Sandbox/test environment.

## Source references


## Source references checked on 2026-05-22

The documents below use these official/public sources where vendor-specific behaviour matters:

- Microsoft Graph Outlook Mail API overview: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview?view=graph-rest-1.0
- Microsoft Graph create subscription/change notification API: https://learn.microsoft.com/en-us/graph/api/subscription-post-subscriptions?view=graph-rest-1.0
- Microsoft Graph Outlook change notifications overview: https://learn.microsoft.com/en-us/graph/outlook-change-notifications-overview
- Box Webhooks overview: https://developer.box.com/guides/webhooks
- Box V2 Webhooks: https://developer.box.com/guides/webhooks/v2
- Box metadata instances: https://developer.box.com/guides/metadata/instances/create
- Box AI Extract Structured API: https://developer.box.com/reference/post-ai-extract-structured
- ICO UK GDPR data protection principles: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/
- ICO personal data guidance: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/personal-information-what-is-it/what-is-personal-data/what-is-personal-data/
- ICO personal data breach guide: https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/
