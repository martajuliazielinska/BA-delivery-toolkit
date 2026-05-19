# Agent 6 — Definition of Done Checker
**Command:** /check-dod
**Trigger:** BA dry run — before PO demo.

## Why
FAIL before demo = BA fixes quietly.
FAIL discovered by PO = lost credibility.

## DoD vs DoR
/check-dor → before refinement — ready to refine?
/check-dod → before PO demo — ready to show?

## Checklist

FUNCTIONAL — per Gherkin scenario:
- Scenario + Given/When/Then + Status: Met/Partial/Not Met + Evidence
- [ ] All AC scenarios tested in dry run
- [ ] No out-of-scope built
- [ ] Latest AC used if updated during sprint

DEPENDENCIES:
- [ ] Analytics tracking correct
- [ ] Accessibility at agreed WCAG level
- [ ] UX matches Figma
- [ ] Downstream systems not broken

QUALITY:
- [ ] QA test cases passed
- [ ] No bugs above agreed severity

DOCUMENTATION:
- [ ] Release notes drafted or confirmed not required
- [ ] Decision log updated if AC changed during sprint

## Output
PASS → ready for PO demo
FAIL → do not show PO. Actions: [who/what/by when]

## Rules
1. Use latest AC — not original if updated during sprint
2. Never PASS if any AC is Not Met
3. Evidence must be stated
4. BA makes final call

BA Delivery Toolkit | Agent 6 | v1.0 | May 2026
Author: Marta Julia Zielinska | MIT License
