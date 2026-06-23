# Command: /prioritize

## Usage
```
/prioritize
```
Run after `/moscow` sign-off. Requires an approved requirements map.

---

## Agent Instructions

1. Read `CLAUDE.md`
2. Read `projects/{active-project}/PROJECT.md`
3. Read `projects/{active-project}/discovery/requirements_map_{YYYY-MM-DD}.md` — use the most recent file if multiple exist
4. Read `.claude/skills/rice-prioritization.md`
5. Check that `/moscow` sign-off is recorded in the requirements map or decision log — if not, stop and ask BA: "Has the MoSCoW session been completed and approved? I need sign-off before scoring."
6. For each requirement in the map:
   - Score Reach, Impact, Confidence, Effort using the RICE framework
   - State the assumption behind each score explicitly
   - Calculate RICE score: (Reach x Impact x Confidence) / Effort
7. Sort requirements by RICE score, highest first
8. Assign priority tier:
   - Must Have — top-scoring requirements critical to the stated success metric
   - Should Have — high value, include if sprint capacity allows
   - Nice to Have — lower RICE, defer if needed
9. Flag dependencies between requirements — name which must be done before which
10. Present the full scored backlog to BA with assumptions listed
11. Ask BA: "Please review scores and assumptions. Adjust any that do not reflect reality before I save."
12. After BA approval: save to `projects/{active-project}/backlog/prioritized_backlog_{YYYY-MM-DD}.md`
13. Log to `logs/decisionLog.md`: date, prioritization approach used, any scores adjusted by BA and why
14. Do not proceed to `/create-story` without explicit BA approval of the backlog

---

## Output Format

```
## Backlog Prioritization — [Project Name]
**Date:** YYYY-MM-DD
**Input:** [requirements map file path]
**Approved by:** [BA name] | [date]

| Requirement | Reach | Impact | Confidence | Effort | RICE Score | Priority |
|---|---|---|---|---|---|---|
| [Name] | 50 | 2 | 80% | 1 | 80 | Must Have |

## Recommended Sprint Sequence
1. [Highest RICE] — [rationale]
2. ...

## Dependencies
- [Requirement A] must be completed before [Requirement B] — reason: [why]

## Assumptions — needs BA validation
- [Requirement]: Reach scored 50 because [assumption] — confirm with [stakeholder]
- [Requirement]: Effort scored 2 because [assumption] — confirm with dev
```

---

## Rules

1. Never score requirements without a validated and approved requirements map
2. State every scoring assumption explicitly — do not score silently
3. Do not assign all requirements to Must Have — if everything is critical, nothing is
4. Dependencies must be named, not implied
5. BA reviews and approves scores before the backlog is saved
6. Do not start story writing until BA explicitly approves the prioritized backlog

---

## Agent Boundaries

This agent can:
- Score requirements using the RICE framework with explicit assumptions
- Sort and assign priority tiers based on scores
- Flag dependencies between requirements
- Present the scored backlog for BA review before saving

This agent cannot:
- Score requirements without an approved requirements map
- Proceed without confirmed MoSCoW sign-off
- Save the backlog without BA approval of scores and assumptions
- Assign all requirements to Must Have
- Proceed to /create-story without explicit BA approval

Hands off to: BA to review and approve scores. After approval, proceed to /size-check then /create-story.

---

BA Delivery Toolkit | Agent 2 | v1.0 | June 2026
Author: Marta Julia Zielinska | MIT License
