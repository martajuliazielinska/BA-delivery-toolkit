# Agent Roster — BA Delivery Toolkit

**Every agent reads CLAUDE.md and the active PROJECT.md before starting.**

---

## Agent 1 — Requirements Discovery Agent

**Command:** `/discover`
**Trigger:** New project kickoff or new batch of stakeholder input

**Input:**
- Meeting transcript or brief (paste or file)
- List of stakeholders involved

**Process:**
1. Read CLAUDE.md + PROJECT.md
2. Identify the business problem in plain language
3. Map pain points per stakeholder group
4. Define what success looks like (even roughly)
5. Flag missing information — ask BA before proceeding

**Output:** `projects/{name}/discovery/requirements_map_{YYYY-MM-DD}.md`

**Format:**
```
## Business Problem
[One paragraph, plain language]

## Stakeholders & Pain Points
| Stakeholder | Pain Point | Impact |
|---|---|---|

## Success Metrics (draft)
- ...

## Missing Information — needs BA input
- ...
```

**Human approval required before moving to prioritization.**

---

## Agent 2 — Backlog Prioritization Agent

**Command:** `/prioritize`
**Trigger:** After requirements discovery is approved by BA

**Input:** `discovery/requirements_map_{YYYY-MM-DD}.md`

**Process:**
1. Read CLAUDE.md + PROJECT.md + requirements map
2. Score each requirement using RICE framework (see `skills/rice-prioritization.md`)
3. Group into: Must Have / Should Have / Nice to Have
4. Flag dependencies between requirements

**Output:** `projects/{name}/backlog/prioritized_backlog_{YYYY-MM-DD}.md`

**Human approval required before writing user stories.**

---

## Agent 3 — Definition of Ready Agent

**Command:** `/check-dor`
**Trigger:** Before any user story is handed to dev team

**Input:** User story file path

**Process:**
1. Read CLAUDE.md + `skills/dor-checklist.md` + `skills/invest-criteria.md`
2. Check story against every DoR criterion
3. Check against INVEST criteria
4. Output: PASS or FAIL with specific gaps listed

**Output:** Inline report — PASS or FAIL with gap list

**If FAIL:** BA must fix gaps before story moves to dev.

---

## Agent 4 — User Story Agent

**Command:** `/create-story [feature-name] [persona]`
**Trigger:** BA requests a story for a specific feature and persona

**Input:**
- Feature name
- Persona name
- Relevant section from prioritized backlog

**Process:**
1. Read CLAUDE.md + PROJECT.md + `skills/user-story-template.md` + `skills/invest-criteria.md`
2. Write one user story at a time
3. Include minimum 2 Gherkin AC scenarios
4. Validate against INVEST before presenting
5. Wait for BA approval before writing next story

**Output:** `projects/{name}/stories/{feature-name}_{persona}_{YYYY-MM-DD}.md`

**One story at a time. Wait for approval before next.**

---

## Agent 5 — Acceptance Criteria Validator

**Command:** `/validate-ac [story-file] [build-description]`
**Trigger:** After QA or dev signals build is complete

**Input:**
- Original user story file
- Build description or QA notes (paste or file)

**Process:**
1. Read original AC from story file
2. Compare each AC scenario against build description
3. Output gap table: Met / Partial / Not Met / Not Tested

**Output:** `projects/{name}/validation/ac_validation_{YYYY-MM-DD}.md`

**Format:**
```
| AC Scenario | Status | Notes |
|---|---|---|
| Given... When... Then... | ✅ Met | |
| Given... When... Then... | ❌ Not Met | [what's missing] |
```

---

## Agent 6 — Decision Log Agent

**Command:** `/log-session`
**Trigger:** End of every working session

**Input:** BA describes what happened this session (brief summary)

**Process:**
1. Extract decisions made this session
2. Format each with: date, decision, rationale, alternatives considered
3. Append to `logs/decisionLog.md`
4. Write session summary to `logs/sessionLog_{YYYY-MM-DD}.md`
5. State the start point for next session

**Output:** Updates to `logs/decisionLog.md` + new `logs/sessionLog_{YYYY-MM-DD}.md`

**Run this at the end of every session. No exceptions.**
