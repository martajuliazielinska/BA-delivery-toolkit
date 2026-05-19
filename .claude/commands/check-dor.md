# Agent 3 — Definition of Ready Agent
**Command:** `/check-dor`
**Trigger:** After /create-story. Before refinement session.

## Why
A failed DoR means the refinement session wastes the team's time.
This agent checks readiness BEFORE booking refinement — not before dev handover.

## DoR Checklist

### FUNCTIONAL — mandatory
- [ ] User story in standard format (As a / I want / So that)
- [ ] Named persona — not "the user"
- [ ] Business value clearly stated
- [ ] Minimum 2 Gherkin AC (happy path + edge case)
- [ ] Out of scope explicitly listed
- [ ] Linked to parent Epic or requirement

### DEPENDENCIES — checked by BA
Downstream Systems:
- [ ] All systems this story touches identified
- [ ] Impact on downstream systems assessed
- [ ] Dependencies on other stories or Epics named

Analytics:
- [ ] Tracking requirements defined OR confirmed not required

Accessibility:
- [ ] WCAG level confirmed OR confirmed not applicable

UX Design:
- [ ] Designs attached (Figma link) OR in progress with expected date OR confirmed not required

Tech Design:
- [ ] Flagged for architect: YES / NO / TBD

### SIZE
- [ ] T-shirt size: XS / S / M / L / XL
- [ ] If L or XL — flagged for potential slice after estimation

## Output

PASS:
DoR CHECK: PASS — ready for refinement session.
[Summary of each area]

FAIL:
DoR CHECK: FAIL — do not book refinement yet.
Failed: [list]
Actions: [who does what]
Run /check-dor again when resolved.

## After PASS
Refinement session → Effort estimation → Tech Design (if needed)
→ QA test case review → /slice if >8 SP → Dev handover

## Rules
1. FAIL if any mandatory functional criterion missing
2. Dependencies must be explicitly confirmed — not assumed
3. "Not required" is valid — but must be stated
4. Size must be assessed — even if rough

BA Delivery Toolkit | Agent 3 | v2.0 | May 2026
Author: Marta Julia Zielinska | MIT License
