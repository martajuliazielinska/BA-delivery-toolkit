# Definition of Ready Checklist — BA Delivery Toolkit

A story is Ready for development when ALL of the following are true.

---

## Mandatory — FAIL if any are missing

- [ ] User story is written in standard format (As a / I want / So that)
- [ ] At least 2 Gherkin AC scenarios present
- [ ] At least 1 error or edge case scenario included
- [ ] Persona is named and defined in PROJECT.md
- [ ] Business value is stated clearly
- [ ] Story is independent (not blocked by another unstarted story)
- [ ] Out of scope is explicitly listed
- [ ] Story approved by BA (not just drafted)

---

## Strongly Recommended — FLAG if missing

- [ ] Story is estimable by dev (no major unknowns)
- [ ] Dependencies on other teams / systems are named
- [ ] Story fits within one sprint (if not — split it)
- [ ] Linked to a validated requirement in discovery map
- [ ] Decision log updated if any assumptions were made

---

## Output Format for /check-dor

```
## DoR Check — [Story Name]
**Date:** YYYY-MM-DD
**Result:** ✅ PASS | ❌ FAIL

### Mandatory criteria
| Criterion | Status | Notes |
|---|---|---|
| User story format | ✅ / ❌ | |
| 2+ Gherkin scenarios | ✅ / ❌ | |
| Error scenario included | ✅ / ❌ | |
...

### Gaps to fix before dev handover
1. [Specific gap]
2. [Specific gap]

### Recommendation
[PASS — ready for dev] or [FAIL — fix gaps listed above first]
```
