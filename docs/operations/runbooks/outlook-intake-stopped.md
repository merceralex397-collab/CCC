# Runbook: Outlook Intake Stopped

Status: future P3 runbook placeholder.

## Trigger

Outlook/Graph intake stops creating work items or attachments are missing.

## Immediate Action

- Pause automated intake if partial data is being created.
- Use manual upload workflow for new instructions.
- Preserve mailbox messages and attachments.
- Record incident in audit/operations log.

## Checks

- mailbox credentials and token expiry;
- mailbox permissions;
- API rate limits;
- duplicate detection state;
- attachment download errors.

## Recovery

Replay only from a known mailbox checkpoint and avoid creating duplicate work items.

