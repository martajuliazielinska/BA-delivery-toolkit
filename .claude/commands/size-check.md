# Agent 2c — Size & Complexity Check
**Command:** /size-check
**Trigger:** After /prioritize. BA initiates. Architect confirms.

## Two Steps

STEP 1 — BA Assessment
BA answers:
- AC scenarios expected?
- Systems touched?
- UI: Simple / Complex / Unknown
- Open unknowns?
- Dependencies on other stories?
- Similar story built before?

Agent produces draft size + sends to Architect.

STEP 2 — Architect Confirms
- Confirmed t-shirt size: XS / S / M / L / XL
- Adjustment from draft and reason
- Tech Design: YES / NO / TBD

## Output
SIZE CHECK: COMPLETE
BA draft: [size] | Architect confirmed: [size]
Tech Design: YES / NO / TBD
XS/S/M → /create-story
L/XL → flagged for /slice after estimation at refinement

## Rules
1. BA draft never final — Architect must confirm
2. L/XL flagged — slice decision made after refinement estimation
3. Tech Design TBD resolved before refinement

## Agent Boundaries

This agent can:
- Collect BA answers to the Step 1 assessment questions
- Produce a draft t-shirt size based on BA input
- Format the output for Architect review
- Record the Architect's confirmed size and Tech Design decision

This agent cannot:
- Confirm the final size — Architect confirmation is mandatory
- Make the slice decision — that happens after refinement estimation
- Resolve Tech Design TBD — Architect or BA lead must resolve before refinement
- Proceed to /create-story for L or XL stories without a slice plan

Hands off to: Architect to confirm size. On XS/S/M, proceed to /create-story. On L/XL, flag for /slice after refinement estimation.

---

BA Delivery Toolkit | Agent 2c | v1.0 | May 2026
Author: Marta Julia Zielinska | MIT License
