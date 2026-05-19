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

BA Delivery Toolkit | Agent 4 | v2.0 | May 2026
Author: Marta Julia Zielinska | MIT License
