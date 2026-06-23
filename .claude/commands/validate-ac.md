# Command: /validate-ac

## Usage
```
/validate-ac [story-file] [build-description]
```

## Examples
```
/validate-ac projects/crm/stories/search-by-symptom_researcher_2026-06-10.md qa-notes.md
/validate-ac projects/crm/stories/search-by-symptom_researcher_2026-06-10.md
```
If build-description is omitted, agent asks BA to paste QA notes or build summary.

---

## Agent Instructions

1. Read `CLAUDE.md`
2. Read `projects/{active-project}/PROJECT.md`
3. Open the story file provided — read every Gherkin AC scenario
4. If build-description is a file path — read it; if omitted — ask BA: "Paste the QA notes or build summary for this story."
5. For each AC scenario, determine status:
   - Met — build output satisfies the scenario fully
   - Partial — build output satisfies some but not all conditions
   - Not Met — build output does not satisfy the scenario
   - Not Tested — no evidence in the build description either way
6. Produce the gap table (format below)
7. If any scenario is Not Met or Partial — list required actions before sign-off
8. If all scenarios are Met — state: "All AC scenarios met. Story ready for BA sign-off."
9. Save output to `projects/{active-project}/validation/ac_validation_{YYYY-MM-DD}.md`
10. Do not sign off the story — BA makes that decision

---

## Output Format

```
## AC Validation — [Story Name]
**Date:** YYYY-MM-DD
**Story file:** [path]
**Build description:** [path or "pasted inline"]

| AC Scenario | Status | Notes |
|---|---|---|
| Given... When... Then... | Met | |
| Given... When... Then... | Partial | [what is missing] |
| Given... When... Then... | Not Met | [what is missing] |
| Given... When... Then... | Not Tested | [what evidence is needed] |

## Actions required before sign-off
1. [Specific gap — who owns it]
2. [Specific gap — who owns it]

## Recommendation
[All AC met — ready for BA sign-off] or [Gaps listed above must be resolved first]
```

---

## Rules

1. Never mark a scenario Met without evidence in the build description
2. Not Tested is not the same as Not Met — flag it separately
3. One Not Met is enough to block sign-off
4. Partial must include specific notes on what is missing
5. BA approves sign-off — agent only presents findings
6. If the story file cannot be found — stop and ask BA for the correct path

---

## Agent Boundaries

This agent can:
- Compare each Gherkin AC scenario against the build description or QA notes
- Assign a status of Met, Partial, Not Met, or Not Tested to each scenario
- List specific gaps and flag who needs to act on them

This agent cannot:
- Sign off the story — BA makes that decision
- Mark a scenario Met without evidence in the build description
- Rewrite AC scenarios to match what was built
- Conduct testing or access the build directly

Hands off to: BA to review findings and make the sign-off decision. Gaps go back to dev or QA as appropriate.

---

BA Delivery Toolkit | Agent 5 | v1.0 | June 2026
Author: Marta Julia Zielinska | MIT License
