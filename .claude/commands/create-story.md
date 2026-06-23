# Command: /create-story

## Usage
```
/create-story [feature-name] [persona]
```

## Example
```
/create-story search-by-symptom researcher
```

---

## Agent Instructions

1. Read `CLAUDE.md`
2. Read `projects/{active-project}/PROJECT.md`
3. Read `.claude/skills/user-story-template.md`
4. Read `.claude/skills/invest-criteria.md`
5. Find the relevant requirement in `projects/{active-project}/backlog/`
6. Write ONE user story using the standard template
7. Include minimum 2 Gherkin scenarios (1 happy path + 1 error/edge)
8. Run INVEST check — fix before presenting if any fail
9. Present to BA for approval
10. **Do not write the next story until BA explicitly approves this one**
11. After approval: save to `projects/{active-project}/stories/`
12. Log to `logs/decisionLog.md`: story name, persona, date, approved by

---

## Agent Boundaries

This agent can:
- Write one user story at a time using the standard template
- Run an INVEST check and fix the story before presenting it
- Include Gherkin AC scenarios based on the requirement and persona provided
- Save an approved story to the correct project folder

This agent cannot:
- Choose the persona or feature — these must be provided by BA
- Approve its own story
- Write the next story without explicit BA approval of the current one
- Invent requirements not present in the prioritized backlog

Hands off to: BA for approval. After approval, run /check-dor before dev handover.
