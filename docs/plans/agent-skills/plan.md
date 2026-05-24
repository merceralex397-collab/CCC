# Agent Skills Plan

Date: 2026-05-24
Status: active workspace plan
Owner: unassigned
Created: 2026-05-24
Last reviewed: 2026-05-24
Source links: `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/README.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md`, `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/22_knowledge_base_report_clause_rag_skill.md`
Roadmap milestone: Whole-programme roadmap
Dependencies: ai-platform-tools, governance-security, engineer-communications, mcp-and-tooling
Expected outputs: source-backed todos, scoped tickets, option papers, roadmap updates, and archive records for `docs/plans/agent-skills/`
Acceptance criteria: each todo is promoted only with source citations, dependency links, ownership boundaries, verification, and governance/operations gates where required
Verification required: `python tools/verify_scaffold.py`
Archive target: `docs/plans/agent-skills/archived_plans/implemented/`
Supersedes: none
Superseded-by: none

## Planning Decision

`docs/plans/agent-skills/` is a separate active workspace. It owns the items listed below and must coordinate with its dependency workspaces before any item becomes an implementation ticket.

## Citeable Evidence

| Source | Planning evidence |
| --- | --- |
| `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md` | Natural-language skills for staff and engineers. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/README.md` | AI tools, MCPs, and skills plan index. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md` | Case summary/status skill plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md` | CE communication style skill plan. |
| `docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/22_knowledge_base_report_clause_rag_skill.md` | Knowledge-base/report-clause RAG skill plan. |

## Todo Areas

| Todo area | Specific source evidence | Required coordination | Acceptance check |
| --- | --- | --- | --- |
| - [ ] case summary, missing-info, CE style, valuation explanation, report-clause RAG, AI literacy, and provider mapping skill specs | `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/README.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/22_knowledge_base_report_clause_rag_skill.md` | `ai-platform-tools`, `governance-security`, `engineer-communications`, `mcp-and-tooling` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] skill prompt/version/evaluation/release lifecycle | `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/README.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/22_knowledge_base_report_clause_rag_skill.md` | `ai-platform-tools`, `governance-security`, `engineer-communications`, `mcp-and-tooling` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |
| - [ ] portable skill contracts for CE platform, agents, ChatGPT, Claude Desktop, or other approved AI front ends | `docs/reference/originalplanning/originalplans_output/phase_ai_tools.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/README.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/16_case_summary_status_skill.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/19_ce_style_communications_skill.md`<br>`docs/reference/originalplanning/collision_engineers_ai_tools_plans_markdown/22_knowledge_base_report_clause_rag_skill.md` | `ai-platform-tools`, `governance-security`, `engineer-communications`, `mcp-and-tooling` | Promoted ticket or option paper cites source evidence, names dependencies, and does not duplicate an excluded owner. |

## Sequential Plan

### S4

- [ ] Define portable skill catalogue and golden examples for case summary, chasers, CE style, and valuation explanation.

### S5

- [ ] Add RAG/report-clause and training skills with source-citation and no-source refusal rules.

### S6

- [ ] Keep skills portable across approved AI front ends while adapters and orchestration remain elsewhere.

## Dependency Cross-Check

| Workspace | Why it must be coordinated |
| --- | --- |
| `ai-platform-tools` | AI-assisted behavior needs model/prompt governance, evaluation data, redaction, and run logging before expansion. |
| `governance-security` | Privacy, vendor, retention, licensing, expert-boundary, API security, and autonomous-action controls must be approved before activation. |
| `engineer-communications` | Coordinate source ownership, sequencing, acceptance criteria, and verification before ticket promotion. |
| `mcp-and-tooling` | MCP/tool exposure must wrap approved adapters with schemas, auth, audit, rate limits, and gateway controls. |

## Non-Overlap Rules

The workspace explicitly does not own:

- workflow orchestration
- model hosting or global AI run logging
- business workflow ownership where the skill is used

If a proposed ticket touches one of those exclusions, link to the owning workspace and keep this workspace as a supporting dependency only.

## Source Ownership Rules

- Cite the source paths above in every promoted ticket, option paper, or roadmap change.
- Use `source_map.md` to explain how the evidence supports the workspace boundary.
- Keep generated and historical planning packs reference-only until a scoped ticket or option paper promotes them.
- Do not edit raw evidence under `docs/reference/raw/collisionrelateddocs/`; create derivatives only under documented derivative paths.

## Promotion Gates

- Use `tickets/` for implementation-ready work with acceptance criteria and verification.
- Use `option-papers/` before vendor, privacy, external access, autonomous send, payment automation, AI/RAG, cloud OCR/document intelligence, commercial data, or partner/API work.
- Link governance/security approval where privacy, vendor, retention, licensing, expert-boundary, API security, or autonomous-action risk exists.
- Link operations-quality approval where release, rollback, regression, monitoring, runbook, support, pilot, or decommissioning evidence is needed.
