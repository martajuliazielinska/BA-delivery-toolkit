# Command: /discover

## Usage
```
/discover
```
Then paste meeting transcript or brief when prompted.

---

## Agent Instructions

1. Read `CLAUDE.md`
2. Read `projects/{active-project}/PROJECT.md`
3. Ask BA: "Paste the transcript, brief, or meeting notes to analyse."
4. From the input:
   - Extract the business problem in plain language (one paragraph)
   - Identify each stakeholder group mentioned
   - Map pain points per stakeholder
   - Draft success metrics (even rough ones)
   - List what information is missing — do not assume, flag it
5. Output requirements map using format in `AGENTS.md`
6. Save to `projects/{active-project}/discovery/requirements_map_{YYYY-MM-DD}.md`
7. Present to BA: "Here is the requirements map. Please review and approve before we move to prioritization."
8. **Do not proceed to /prioritize without explicit BA approval**
