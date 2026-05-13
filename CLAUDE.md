# BA Delivery Toolkit — Project Brain
**Read this file before every session. Every agent reads this first.**

---

## Layer 1 — What This Is

A lightweight multi-agent system for Business Analysts working in a delivery model.
Agents handle repeatable BA work. Humans make decisions. Always.

**North Star:** Every project delivered with full traceability — from business problem to accepted requirement to working build.

---

## Layer 2 — Working Principles

1. **Human is accountable.** Agents draft. BAs decide.
2. **Context lives in files.** Agents have no memory between sessions. All knowledge is written down.
3. **No output without input validation.** Agents do not generate requirements without a validated problem statement.
4. **Every decision is logged.** Date, rationale, alternatives considered.
5. **Merit over habit.** Tools and approaches chosen on evidence, not convenience.

---

## Layer 3 — Agent Roster

| Agent | Command | Role |
|---|---|---|
| Requirements Discovery Agent | `/discover` | Maps business problem to structured requirements |
| Backlog Prioritization Agent | `/prioritize` | Prioritizes requirements before sprint |
| Definition of Ready Agent | `/check-dor` | Validates story readiness before dev handover |
| User Story Agent | `/create-story` | Writes user stories with Gherkin AC |
| Acceptance Criteria Validator | `/validate-ac` | Compares build output to original AC |
| Decision Log Agent | `/log-session` | Logs decisions and next session start point |

---

## Layer 4 — Working Rules

- Read PROJECT.md in the active project folder before doing anything
- Read the relevant skill file before generating output
- Never skip the human approval step between phases
- Log every decision to `logs/decisionLog.md` in the active project
- If uncertain — ask, do not assume

---

## Layer 5 — Definition of Ready (per phase)

**Requirements Discovery → Done when:**
- Business problem is described in plain language
- Affected stakeholders are named
- Success metric is defined (even roughly)

**User Story → Done when:**
- Follows INVEST criteria
- Has at least 2 Gherkin AC scenarios
- Linked to a validated requirement
- Reviewed and approved by BA

**Dev Handover → Done when:**
- DoR checklist passed
- AC validated by BA
- Decision log updated

---

## Layer 6 — Project Memory

Active project folder: `projects/{project-name}/`
Decision log: `logs/decisionLog.md`
Session log: `logs/sessionLog_{YYYY-MM-DD}.md`

---

*Author: Marta Zielinska | BA Delivery Toolkit v1.0*
*Adapted from IDEASHACK 2026 — Entropy Solvers architecture*
*GitHub: github.com/martajuliazielinska/ba-delivery-toolkit*
