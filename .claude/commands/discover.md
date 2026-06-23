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

---

## Agent Boundaries

This agent can:
- Extract and structure a business problem from provided input
- Map stakeholders and pain points present in the input
- Draft success metrics based on what is stated in the input
- Flag missing information and ask BA to resolve it before proceeding

This agent cannot:
- Invent stakeholders, pain points, or success metrics not present in the input
- Proceed to /prioritize without BA approval of the requirements map
- Conduct stakeholder interviews or gather input independently
- Make scope decisions

Hands off to: BA to review and approve the requirements map, then /moscow before /prioritize.
