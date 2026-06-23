# Command: /log-session

## Usage
```
/log-session
```
Run at the end of every working session. No exceptions.

---

## Agent Instructions

1. Read `CLAUDE.md`
2. Read `logs/decisionLog.md` (to avoid duplicates)
3. Ask BA: "What decisions were made this session? (brief summary)"
4. Extract individual decisions from BA's summary
5. Format each decision using the template in `.claude/skills/decision-log-template.md`
6. Append to `logs/decisionLog.md` — newest entries first
7. Create `logs/sessionLog_{YYYY-MM-DD}.md` with:
   - What was worked on
   - What was completed
   - What was decided
   - Blockers or open questions
   - **Start point for next session** (exact first action)
8. Confirm to BA: "Session logged. Next session starts with: [action]"

---

## Agent Boundaries

This agent can:
- Extract and format decisions from BA's session summary
- Append new entries to the decision log
- Write a session summary with a clear next-session start point

This agent cannot:
- Invent or infer decisions not described by BA
- Modify or delete existing log entries
- Decide what counts as a significant decision — BA provides the summary
- Replace the BA's obligation to describe what happened

Hands off to: next session. The logged start point is the first action for the next agent invocation.
