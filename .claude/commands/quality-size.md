# Command: /quality-size

## Usage
```
/quality-size [mode] [epic-or-fta-file]
```

Mode options: `enhancement` | `project`

## Examples
```
/quality-size enhancement projects/crm/backlog/epic-search-by-symptom.md
/quality-size project projects/crm/backlog/fta-reporting-dashboard.md
```

---

## When to Run

Trigger: An Epic or FTA lands in the backlog.
Run by: Senior BA, before PO prioritization.
Purpose: Validate the item is well-formed and sized enough for PO to make a prioritization decision.

---

## Two Modes

### Enhancement mode
Full Quality and Size evaluation. Used for changes to existing systems.
Output goes to PO with a recommendation.

### Project mode
Lightweight checklist only. Used for new projects where full scoping has not yet happened.
Output flags what is missing before a full Q&S can be run.

---

## Agent Instructions

1. Read `CLAUDE.md`
2. Read `projects/{active-project}/PROJECT.md`
3. Read the Epic or FTA file provided
4. Identify the mode from the command argument — if omitted, ask BA: "Is this an enhancement to an existing system or a new project?"

**If mode is `enhancement` — run full evaluation:**

5. Evaluate requirements content validity:
   - Is the business problem stated clearly?
   - Is the success metric defined?
   - Is the persona named?
   - Is out of scope stated?
6. Identify systems touched — list each system affected, even if partially
7. Map dependencies — other epics, stories, or external systems this item relies on
8. Generate architect questions — specific technical unknowns that require architect input before sizing can be confirmed
9. Produce a draft t-shirt size: XS / S / M / L / XL with rationale
   - Base on: number of systems touched, AC complexity, dependency count, open unknowns
   - State assumptions explicitly
10. Produce structured output (format below) with READY TO PRIORITIZE or BLOCKED BY recommendation
11. Present to BA: "Here is the Quality and Size report. Review with architect before sending to PO."

**If mode is `project` — run lightweight checklist:**

5. Check the four universal criteria from `/check-input`: Problem, Owner, Success, Context
6. List what is present and what is missing
7. Do not score or size — flag that full Q&S requires more input first
8. Output: checklist result with READY FOR FULL Q&S or BLOCKED BY missing items

---

## Output Format — Enhancement

```
## Quality and Size Report — [Epic / FTA Name]
**Date:** YYYY-MM-DD
**Mode:** Enhancement
**Prepared by:** BA Delivery Toolkit — Quality and Size Agent

### Requirements Content
| Criterion | Status | Notes |
|---|---|---|
| Business problem stated | PASS / FAIL | |
| Success metric defined | PASS / FAIL | |
| Persona named | PASS / FAIL | |
| Out of scope stated | PASS / FAIL | |

### Systems Touched
- [System name] — [how it is affected]

### Dependencies
- [Epic / story / system] — [nature of dependency]
- None identified

### Architect Questions
1. [Specific technical question — cannot be answered without architect input]
2. ...
None — proceed without architect review

### T-shirt Size Draft
**Draft size:** XS / S / M / L / XL
**Rationale:** [basis for the size]
**Assumptions:** [list — must be confirmed before size is final]

### Recommendation for PO
READY TO PRIORITIZE — [brief rationale]
or
BLOCKED BY — [specific blocker] — owner: [BA / Architect / Business Owner]
```

---

## Output Format — Project

```
## Quality and Size — Lightweight Checklist — [Epic / FTA Name]
**Date:** YYYY-MM-DD
**Mode:** Project

| Criterion | Status | Notes |
|---|---|---|
| Business problem stated | PASS / FAIL | |
| Named owner | PASS / FAIL | |
| Success metric defined | PASS / FAIL | |
| Sufficient context | PASS / FAIL | |

**Result:**
READY FOR FULL Q&S — all criteria present
or
BLOCKED BY — [missing items] — run /check-input to resolve before full Q&S
```

---

## Rules

1. Never run full evaluation in project mode — flag what is missing and stop
2. State every sizing assumption explicitly — do not size silently
3. Architect questions must be specific — not generic uncertainty
4. BLOCKED BY must name an owner — not just a gap
5. Do not send output to PO without BA review first

---

## Agent Boundaries

This agent can:
- Evaluate requirements content validity against defined criteria
- Identify systems touched and dependencies based on the input provided
- Generate specific architect questions for unknowns in the input
- Produce a draft t-shirt size with explicit assumptions
- Recommend READY TO PRIORITIZE or BLOCKED BY for PO

This agent cannot:
- Make architectural decisions or answer architect questions
- Replace the architect conversation
- Assign a final confirmed size — that requires architect input
- Send output directly to PO — BA reviews first

Hands off to: BA to review with architect, resolve blockers, then pass to PO for prioritization.

---

BA Delivery Toolkit | Quality and Size Agent | v1.0 | June 2026
Author: Marta Julia Zielinska | MIT License
