# Bridge Workspace — Open Questions

Date: 2026-05-29
Status: active open-questions log
Owner: unassigned
Group: bridge (G2, spine)
Source links: `docs/superpowers/specs/2026-05-29-bridge-design.md`, `docs/plans/intake-storage-integrations/plan.md`, `docs/plans/intake-storage-integrations/context.md`

## Resolved (this interview, 2026-05-29)

- **How far this iteration?** — Staged: build read-only Outlook intake; keep Box `package_only` and EVA export-only.
- **Outlook mechanism?** — Delta-query polling + app-only `Mail.Read` scoped via App RBAC to the four mailboxes (not delegated, not webhooks-now).
- **Live writes?** — None built; governed option-papers only for live Box upload, EVA/Sentry submission, and the spreadsheet/job-sheet bridge.

## Open

1. **Entra setup ownership.** Who registers the Entra app, grants admin consent, and configures the App RBAC security group of the four mailboxes (CE IT / governance-security)?
2. **Auto-create vs stage.** Does intake auto-create work items, or stage candidates into a review queue first? Depends on the `casework` work-item contract.
3. **Folder scope.** Whole Inbox per mailbox, or a controlled subfolder/category that staff route relevant mail into?
4. **`Mail.Read` vs `Mail.ReadBasic`.** Attachments are needed for instruction intake, so `Mail.Read` is likely required — confirm no `Mail.ReadBasic`-only path suffices.
5. **Backfill throttling.** Initial historical backfill volume and Graph throttling limits — bounded batch + delta token strategy.
6. **Work-item contract dependency.** Intake cannot land until `casework` exposes a minimal work-item/review target; sequence with the casework interview.
7. **Webhook upgrade trigger.** What real-time requirement (if any) would justify moving from polling to change-notification webhooks later?
