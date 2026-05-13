# Command: /check-dor

## Usage
```
/check-dor [story-file-path]
```

## Example
```
/check-dor projects/crm-update/stories/search-by-symptom_researcher_2026-05-13.md
```

---

## Agent Instructions

1. Read `CLAUDE.md`
2. Read `.claude/skills/dor-checklist.md`
3. Read `.claude/skills/invest-criteria.md`
4. Read the specified story file
5. Check every mandatory criterion — FAIL if any are missing
6. Check every recommended criterion — FLAG if missing
7. Output the DoR check report in the format specified in `dor-checklist.md`
8. State clearly: PASS or FAIL
9. If FAIL — list specific gaps with instructions for BA to fix
10. Do not suggest fixes yourself — flag gaps, let BA decide how to resolve
