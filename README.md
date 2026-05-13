# BA Delivery Toolkit
**A multi-agent system for Business Analysts in delivery models**

*Author: Marta Zielinska | v1.0 | May 2026*

---

## What This Is

A lightweight Claude Code agent architecture that handles the repeatable parts of BA work — so BAs can focus on decisions, not documentation.

Built for teams working in a delivery model where IT translates business needs into requirements for development teams.

**Core principle:** AI drafts. Humans decide.

---

## The Problem It Solves

In a delivery model, BAs spend significant time on:
- Structuring requirements from messy meeting transcripts
- Writing user stories from scratch for every feature
- Checking if stories are ready before dev handover
- Validating that what was built matches what was specified
- Remembering what was decided and why

These are important tasks — but most of the *work* within them is repeatable.
This toolkit handles the repeatable parts. BAs handle the judgment.

---

## Six Agents

| Agent | What It Does |
|---|---|
| **Requirements Discovery** | Maps business problem to structured requirements per stakeholder |
| **Backlog Prioritization** | Prioritizes requirements using RICE/INVEST before sprint planning |
| **Definition of Ready Checker** | Validates story readiness before dev handover |
| **User Story Agent** | Writes user stories with Gherkin Acceptance Criteria in Jira format |
| **Acceptance Criteria Validator** | Compares build output to original AC — flags gaps |
| **Decision Log Agent** | Logs all decisions with date, rationale, and next actions |

---

## Project Structure

```
/
├── CLAUDE.md                          # Project brain — read by every agent
├── README.md                          # This file
├── .claude/
│   ├── AGENTS.md                      # Agent roster and detailed instructions
│   ├── commands/                      # Workflow commands
│   │   ├── discover.md                # /discover
│   │   ├── prioritize.md              # /prioritize
│   │   ├── check-dor.md               # /check-dor
│   │   ├── create-story.md            # /create-story
│   │   ├── validate-ac.md             # /validate-ac
│   │   └── log-session.md             # /log-session
│   └── skills/                        # Frameworks and templates
│       ├── user-story-template.md     # User story + Gherkin format
│       ├── invest-criteria.md         # INVEST validation checklist
│       ├── dor-checklist.md           # Definition of Ready checklist
│       ├── rice-prioritization.md     # RICE scoring framework
│       └── decision-log-template.md   # Decision log format
├── logs/
│   ├── decisionLog.md                 # All decisions across projects
│   └── sessionLog_{YYYY-MM-DD}.md     # Per-session logs
└── projects/
    └── template/                      # Copy this for every new project
        └── PROJECT.md                 # Project brain (fill in per project)
```

---

## How to Use

1. Copy `projects/template/` → rename to your project name
2. Fill in `PROJECT.md` with project details
3. Start Claude Code — it reads `CLAUDE.md` automatically
4. Use commands: `/discover`, `/create-story`, `/check-dor`, etc.
5. Approve each output before moving to next phase
6. Run `/log-session` at the end of every working session

---

## Human in the Loop — Always

The BA approves every phase transition:

1. Problem statement validated → before `/discover`
2. Requirements accepted → before `/prioritize`
3. Top priorities confirmed → before `/create-story`
4. Story approved → before `/check-dor`
5. DoR passed → before dev handover
6. Build reviewed → before `/validate-ac`

**No agent proceeds without BA approval.**

---

## Compatibility

| Environment | Status |
|---|---|
| Claude Code (local) | ✅ Full architecture |
| Copilot Studio | ✅ Partial (4/6 agents) — see `/copilot` branch |
| Rovo (Atlassian) | 🔄 Planned |

---

## Origin

Architecture adapted from IDEASHACK 2026 — Entropy Solvers team.

The hackathon architecture proved that one PM/BA with an AI agent system can run a full product discovery cycle. This toolkit applies the same pattern to enterprise delivery.

---

*MIT License | Marta Julia Zielinska 2026*
