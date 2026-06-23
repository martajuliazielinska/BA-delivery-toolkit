# Command: /refine

## Usage
```
/refine [story-file]
```

## Example
```
/refine projects/crm/stories/search-by-symptom_researcher_2026-06-10.md
```

---

## When to Run

Trigger: After PO prioritization. BA runs before scheduling the refinement session.
Purpose: Identify the correct stakeholder list for the story, generate targeted questions per stakeholder, map the critical path, and confirm the story is ready to go into refinement.

---

## Agent Instructions

1. Read `CLAUDE.md`
2. Read `projects/{active-project}/PROJECT.md`
3. Read the story file provided
4. Identify the change type from the story content — if ambiguous, ask BA: "What type of change is this? Frontend/UI, 3rd party integration, New product/content, Backend/data, or Compliance/finance?"
5. Map the change type to the required stakeholder list using the table below
6. For each stakeholder, generate specific questions based on the story's AC and scope
7. Identify the critical path — which stakeholder inputs are needed before others can proceed
8. List any blockers that would prevent a productive refinement session
9. Produce the refinement plan (format below)
10. Present to BA: "Here is the refinement plan. Review before scheduling the session."
11. Do not schedule the session — BA does that

---

## Change Type to Stakeholder Mapping

| Change Type | Required Stakeholders |
|---|---|
| Frontend / UI | Dev, QA, Analytics, Accessibility, UX |
| 3rd party integration | Dev, QA, 3rd party vendor, Analytics |
| New product / content | Dev, QA, Content, UX, Analytics, Accessibility, Ops |
| Backend / data | Dev, QA, Architect, Analytics |
| Compliance / finance | Dev, QA, Architect, Data Privacy, relevant business stakeholder |

If the story spans more than one change type, combine the stakeholder lists and remove duplicates.

---

## Output Format

```
## Refinement Plan — [Story Name]
**Date:** YYYY-MM-DD
**Change type:** [type identified]
**Story file:** [path]

### Required Stakeholders
- [Stakeholder role] — [why they are needed for this story]

### Questions per Stakeholder

**Dev**
1. [Specific question from story scope or AC]
2. ...

**QA**
1. [Specific question from story scope or AC]
2. ...

**[Other stakeholders as applicable]**
1. ...

### Critical Path
1. [Stakeholder / input needed first] — reason: [why this unblocks others]
2. ...

### Blockers
- [Specific blocker] — owner: [role] — must be resolved before refinement
- None identified

### Status
READY FOR REFINEMENT — all inputs available, no blockers
or
BLOCKED BY — [blocker] — resolve before scheduling
```

---

## Rules

1. Always derive the stakeholder list from the change type — do not guess or omit
2. Questions must be specific to the story — not generic refinement questions
3. If the story spans multiple change types — combine stakeholder lists and remove duplicates
4. Critical path must name which inputs are needed before others — not just a list
5. BLOCKED BY must name an owner and resolution step
6. Do not present a READY status if any blocker is unresolved

---

## Agent Boundaries

This agent can:
- Identify the change type from the story content
- Map the change type to the correct stakeholder list
- Generate specific questions per stakeholder based on the story
- Identify the critical path and any blockers

This agent cannot:
- Contact or notify stakeholders
- Conduct the refinement session
- Negotiate scope or AC on behalf of the BA
- Schedule the refinement session

Hands off to: BA to review the plan, resolve any blockers, and run the refinement session.

---

BA Delivery Toolkit | Refinement Agent | v1.0 | June 2026
Author: Marta Julia Zielinska | MIT License
