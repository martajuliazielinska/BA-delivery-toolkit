# INVEST Criteria — BA Delivery Toolkit

Use this to validate a user story before presenting it to the BA.
Every story must pass all six criteria. Fix before presenting if any fail.

---

## The Six Criteria

### I — Independent
The story can be built and delivered without depending on another unstarted story.
Not blocked by a story that is not yet in progress or done.

FAIL: "Requires the API from story X which is not started"
PASS: "Relies only on existing auth service already in production"

### N — Negotiable
The story describes what is needed, not how to build it.
Details can be discussed with dev and PO. It is not a fixed specification.

FAIL: "Must use React component with specific CSS class names"
PASS: "User can filter results by date — implementation approach open"

### V — Valuable
Delivering this story alone produces value for a named user or the business.
It is not a partial feature that only makes sense alongside other stories.

FAIL: "Sets up database schema — no user-facing outcome"
PASS: "Researcher can search by symptom and view matching studies"

### E — Estimable
Dev has enough information to give a rough size estimate.
No major unknowns that would prevent estimation.

FAIL: "Integrate with third-party system — no API documentation available"
PASS: "Integrate with Salesforce CRM using existing internal connector"

### S — Small
The story fits within one sprint.
If dev estimates more than 8 story points, flag for /slice.

FAIL: "Covers the entire onboarding journey for all persona types"
PASS: "New user completes email verification step"

### T — Testable
Each acceptance criterion is specific enough to write a test against.
The outcome is observable and unambiguous.

FAIL: "The experience should feel intuitive"
PASS: "Given a valid email, when the user submits, then a confirmation message appears within 3 seconds"

---

## Output Format for INVEST Check

Used by: /create-story, /check-dor

```
## INVEST Check — [Story Name]

| Criterion | Result | Notes |
|---|---|---|
| Independent | PASS / FAIL | [reason if FAIL] |
| Negotiable | PASS / FAIL | [reason if FAIL] |
| Valuable | PASS / FAIL | [reason if FAIL] |
| Estimable | PASS / FAIL | [reason if FAIL] |
| Small | PASS / FAIL | [reason if FAIL] |
| Testable | PASS / FAIL | [reason if FAIL] |

Overall: PASS | FAIL
Gaps to fix: [list, or "none"]
```

---

## Rules

1. Run INVEST check before presenting any story to BA
2. One FAIL is enough to fix the story before presenting
3. Do not present a story that fails INVEST — fix it first
4. If Small fails — flag for /slice, do not trim scope arbitrarily
5. If Estimable fails — list the specific unknowns so BA can resolve them

---

BA Delivery Toolkit | Skill | v1.0 | June 2026
Author: Marta Julia Zielinska | MIT License
