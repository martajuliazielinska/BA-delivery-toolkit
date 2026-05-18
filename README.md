# BA Delivery Toolkit
**AI agents for Business Analysts — built for delivery teams**

*Author: Marta Julia Zielinska | v1.1 | May 2026*

---

## What is this?

A set of AI agents designed to help Business Analysts do their daily work faster and more consistently.

Instead of starting from scratch on every project, you give an agent the right input — and it produces a structured first draft. You review it, approve it, and move on.

**The rule is simple: AI drafts. You decide.**

---

## Who is it for?

Business Analysts working in a delivery model — where IT translates business needs into requirements for a development team.

It also works for:
- Product Owners who write user stories
- Project Managers who need decision traceability
- Anyone who wants to stop losing context between meetings

---

## The Core Problem This Toolkit Solves

> *AI output is only as good as the input it receives. A weak brief produces weak requirements. Weak requirements produce rework. Rework is the most expensive thing in delivery.*

The toolkit addresses this at every stage — starting with a quality gate before any AI generation begins.

---

## What problems does it solve?

| Problem | How the toolkit helps |
|---|---|
| Weak input produces weak requirements | Push Back Agent checks quality before any generation starts |
| Requirements get lost between meetings | Discovery Agent structures everything from transcripts |
| "What should we build first?" | Prioritization Agent scores and ranks requirements |
| Stories go to dev before they're ready | Definition of Ready Agent checks every story before handover |
| Writing user stories takes too long | User Story Agent drafts stories with acceptance criteria |
| Nobody knows why we made that decision | Decision Log Agent records everything, automatically |
| Build doesn't match what was specified | AC Validator compares the build to original requirements |

---

## The Seven Agents — Plain English

### 0. Push Back Agent — `/check-input [brd|epic|story]`
**What it does:** Evaluates the quality of any input — BRD, Epic brief, or User Story brief — before any other agent runs. If the input is weak, it refuses to proceed and returns specific questions to ask the business instead.
**When to use it:** Always. Before `/discover`, before any Epic or Story is created.
**What you give it:** A transcript, BRD draft, Epic description, or brief.
**What you get back:** PASS → proceed | FAIL → list of specific questions to ask first.
**Why it matters:** Catches weak inputs from AI-generated BRDs before they create weak Epics and weak Stories downstream.

---

### 1. Discovery Agent — `/discover`
**What it does:** Takes your meeting notes or brief and turns it into a structured list of requirements — per stakeholder, with success metrics.
**When to use it:** At the start of any new project or feature. Only after `/check-input` returns PASS.
**What you give it:** A transcript, email, or brief description of the problem.
**What you get back:** A clear map of who needs what, and what "done" looks like.

---

### 2. Backlog Prioritization Agent — `/prioritize`
**What it does:** Takes your list of requirements and scores them — so you know what to build first, with a clear reason why.
**When to use it:** Before sprint planning, when you have more requirements than time.
**What you give it:** The output from the Discovery Agent.
**What you get back:** A ranked backlog with rationale for every decision.

---

### 3. Definition of Ready Agent — `/check-dor`
**What it does:** Checks a user story against a quality checklist before it goes to the development team. PASS or FAIL — with specific gaps listed.
**When to use it:** Before any story is handed to dev.
**What you give it:** A user story file.
**What you get back:** A clear verdict — and exactly what needs fixing if it fails.

---

### 4. User Story Agent — `/create-story`
**What it does:** Writes a user story in the standard format (As a / I want / So that) with Gherkin acceptance criteria. One story at a time — waits for your approval before writing the next.
**When to use it:** When you need to write stories for a feature.
**What you give it:** A feature name and the persona it's for.
**What you get back:** A complete, review-ready user story in Jira format.

---

### 5. Decision Log Agent — `/log-session`
**What it does:** At the end of every working session, records what was decided, why, and what happens next.
**When to use it:** Every time you finish a working session.
**What you give it:** A short summary of what happened.
**What you get back:** A structured log entry + a clear start point for next time.

---

### 6. Acceptance Criteria Validator — `/validate-ac`
**What it does:** Compares the finished build against the original acceptance criteria. Shows what matches, what's partial, and what's missing.
**When to use it:** After QA or when dev says the build is done.
**What you give it:** The original story file + QA notes or build description.
**What you get back:** A gap table — so you know exactly what to push back on.

---

## The Flow — How Agents Connect

```
INPUT (transcript / BRD / brief)
        ↓
/check-input → FAIL? → Questions to business → Fix → /check-input again
        ↓ PASS
/discover → Requirements map
        ↓
/prioritize → Ranked backlog
        ↓
/create-story → User story + AC
        ↓
/check-dor → PASS?
        ↓ PASS
Dev handover
        ↓
/validate-ac → Gap report
        ↓
/log-session → Decision log updated
```

Human approves every step. No agent proceeds without BA sign-off.

---

## The PROJECT.md File — The Project Brain

Every project gets one file: `projects/template/PROJECT.md`.

Copy it, rename it, fill it in. Every agent reads this file first — so it knows:
- What we're building and why
- Who the stakeholders are
- What decisions have already been made
- What the rules are for this project

**Agents have no memory between sessions. All context lives in files.** PROJECT.md is the project's memory.

---

## How to Start a New Project

1. Copy `projects/template/` and rename the folder to your project name
2. Fill in `PROJECT.md` — 15 minutes, once per project
3. Open Claude Code
4. Run `/check-input brd` → paste your brief or BRD
5. If PASS → run `/discover`
6. End every session with `/log-session`

---

## POC Hypothesis

> *A structured quality gate between AI-generated content and BA approval reduces rework loops in delivery.*

**Baseline to measure:**
- Clarification meetings after dev handover per sprint
- Stories returned from dev or QA due to unclear requirements

**Success:** Fewer clarification meetings. Fewer stories returned from dev.

**Failure:** Same or more rework despite using the agents.

---

## Compatibility

| Tool | Status | Notes |
|---|---|---|
| Claude Code (local) | ✅ Full — all 7 agents | Requires API key |
| Microsoft Copilot 365 | ✅ Partial — works with manual prompts | No automation, manual steps |
| Copilot Studio | ✅ Partial — 4 agents | Requires Jira + Confluence connectors |
| Rovo (Atlassian) | 🔄 Planned | |

**Start with what you have.** Copy the agent instructions, paste your input into Copilot, follow the template. The thinking is the same — the automation comes later.

---

*MIT License | Marta Julia Zielinska 2026*
