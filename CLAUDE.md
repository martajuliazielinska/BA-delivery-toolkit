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

## Layer 3 — Delivery Flows

**Enhancement / FTA:**
`/check-input` → `/quality-size` → [PO prioritizes] → `/refine` → `/create-story` → `/check-dor` → `/check-dod`

**Project:**
`/check-input` → `/discover` → `/expand` → `/moscow` → `/prioritize` → `/create-story` → `/check-dor` → `/slice` (if L/XL) → `/check-dod`

---

## Layer 4 — Agent Roster

| Agent | Command | Role |
|---|---|---|
| Input Quality Gate | `/check-input` | Validates input quality before any work begins |
| Quality and Size Agent | `/quality-size` | Evaluates Epic or FTA readiness for PO prioritization |
| Requirements Discovery Agent | `/discover` | Maps business problem to structured requirements |
| Discovery Expansion Agent | `/expand` | Expands problem space using Lotus Blossom |
| MoSCoW Agent | `/moscow` | Categorises requirements with BA and business |
| Backlog Prioritization Agent | `/prioritize` | Scores and prioritizes requirements using RICE |
| Refinement Agent | `/refine` | Maps stakeholders and prepares refinement plan |
| User Story Agent | `/create-story` | Writes user stories with Gherkin AC |
| Definition of Ready Agent | `/check-dor` | Validates story readiness before dev handover |
| Size and Complexity Agent | `/size-check` | Assesses t-shirt size with BA and architect |
| Story Slice Agent | `/slice` | Splits large stories after estimation |
| Acceptance Criteria Validator | `/validate-ac` | Compares build output to original AC |
| Definition of Done Agent | `/check-dod` | Validates delivery against Definition of Done |
| Decision Log Agent | `/log-session` | Logs decisions and next session start point |

For full agent instructions see `.claude/AGENTS.md`. For each command see `.claude/commands/`.

---

## Layer 5 — Working Rules

- Read PROJECT.md in the active project folder before doing anything
- Read the relevant skill file before generating output
- Never skip the human approval step between phases
- Log every decision to `logs/decisionLog.md` in the active project
- If uncertain — ask, do not assume

---

## Layer 6 — Definition of Ready

See `.claude/skills/dor-checklist.md` for the full DoR checklist per phase.

---

## Layer 7 — Project Memory

Active project folder: `projects/{project-name}/`
Decision log: `logs/decisionLog.md`
Session log: `logs/sessionLog_{YYYY-MM-DD}.md`

---

*Author: Marta Zielinska | BA Delivery Toolkit v1.0*
*Adapted from IDEASHACK 2026 — Entropy Solvers architecture*
*GitHub: github.com/martajuliazielinska/ba-delivery-toolkit*
