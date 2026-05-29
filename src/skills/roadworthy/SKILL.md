---
name: roadworthy
description: Use when generating an HS (Hackney Solutions) roadworthy certificate from an engineer's accident-damage report (PDF or docx). Extracts the required fields from the report and fills the roadworthy docx template. Triggers on "roadworthy", "roadworthy certificate", "HS roadworthy", "taxi / private-hire roadworthy".
---

# Roadworthy Certificate

Generate an HS roadworthy certificate by extracting the required fields from an engineer's report and filling the approved template copy.

**Governance: expert output.** Named-human sign-off; no autonomous external send. Uses `../ce-house-style` for layout and tone (see `docs/security/role_model.md`).

The 14-field extraction guide and worked example are in `toolinstructions.md`, `startingprompt.md`, and `template.md`. The current repository does not contain a master DOCX template; use a supplied approved template copy or promote one through the source manifest before rendering.

## Status

Lifecycle pending the substrate in `docs/plans/ai-platform-tools/`. Catalogue: `docs/plans/agent-skills/skill-catalogue.md`.
