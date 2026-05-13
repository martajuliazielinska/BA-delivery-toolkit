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
