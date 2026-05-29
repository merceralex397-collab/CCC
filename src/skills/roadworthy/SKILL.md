---
name: roadworthy
description: Use when generating an HS (Hackney Solutions) roadworthy certificate from an engineer's accident-damage report (PDF or docx). Extracts the required fields from the report and fills the roadworthy docx template. Triggers on "roadworthy", "roadworthy certificate", "HS roadworthy", "taxi / private-hire roadworthy".
---

# Roadworthy Certificate

Generate an HS roadworthy certificate by extracting the required fields from an engineer's report and filling the docx template (the template is never edited in place).

**Governance: expert output.** Named-human sign-off; no autonomous external send. Uses `../ce-branding` for branding (see `docs/security/role_model.md`).

The system prompt, the 14-field extraction guide, and the worked example are in `startingprompt.md`, `toolinstructions.md`, and `template.md`.

## Status

Adopted from collisionplugin (2026-05-29). Lifecycle pending the substrate in `docs/plans/ai-platform/`. Catalogue: `docs/plans/agent-skills/skill-catalogue.md`.
