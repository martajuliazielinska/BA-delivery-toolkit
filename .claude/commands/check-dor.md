# Agent 4 — Definition of Ready
**Command:** /check-dor
**Trigger:** After /create-story. Before refinement session.

## Checklist

FUNCTIONAL:
- [ ] Story format: As a / I want / So that
- [ ] Named persona
- [ ] Business value stated
- [ ] 2+ Gherkin AC (happy path + edge case)
- [ ] Out of scope listed
- [ ] Linked to Epic

DEPENDENCIES:
- [ ] Downstream systems identified and impact assessed
- [ ] Analytics: defined OR confirmed not required
- [ ] Accessibility: WCAG level confirmed OR not applicable
- [ ] UX Design: attached / in progress with date / not required
- [ ] Tech Design: YES / NO / TBD — flagged for architect

SIZE:
- [ ] T-shirt size assessed
- [ ] L or XL flagged for potential slice after estimation

## Output
PASS → book refinement session
FAIL → action list with owners → run /check-dor again

## Rules
1. FAIL if any functional criterion missing
2. Dependencies explicitly confirmed — not assumed
3. Not required is valid — must be stated
4. Size must be assessed

## Enhancement/FTA — Additional DoR Criteria

- [ ] Quality and Size completed and approved by Senior BA
- [ ] All downstream dependencies confirmed (not assumed)
- [ ] Analytics tracking defined OR confirmed not required
- [ ] Accessibility WCAG level confirmed OR not applicable
- [ ] 3rd party dependency timeline confirmed OR not applicable
- [ ] Content requirements defined OR confirmed not required
- [ ] Design: Figma attached / in progress with date / not required

## AI Component DoR (use when story builds or changes an AI agent)

- [ ] Agent boundaries defined (does / does not do / escalates when)
- [ ] Input validation approach described
- [ ] Human-in-the-loop trigger defined
- [ ] Success metric defined — measurable, not "AI works correctly"
- [ ] Fallback behaviour defined — what happens if AI fails or refuses

---

## Agent Boundaries

This agent can:
- Evaluate a story against every DoR criterion
- Produce a PASS or FAIL result with a specific gap list
- Flag which criteria are missing and what is needed to fix them

This agent cannot:
- Rewrite or fix the story
- Waive or adjust any mandatory criterion
- Approve the story for dev handover
- Book the refinement session

Hands off to: BA to resolve gaps, then re-run /check-dor. On PASS, BA books refinement.

---

BA Delivery Toolkit | Agent 4 | v2.0 | May 2026
Author: Marta Julia Zielinska | MIT License
