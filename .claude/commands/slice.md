# Agent 5 — Story Slice
**Command:** /slice
**Trigger:** After refinement — story estimated > 8 SP.
Also triggered when Architect flags L/XL at /size-check.

## Two Moments for Slice
1. Early flag — Architect confirms L/XL at size-check. Note and proceed. Final decision after estimation.
2. Confirmed at refinement — dev estimates > 8 SP. Run /slice after the call.

## Slice Patterns
By dev stream (most common):
- Frontend story — UI, interactions, display
- Backend story — API, data, business logic
- Can run in parallel once dependencies clear

By functionality:
- Core flow — minimum path that delivers value
- Enhancement — additional scenarios, edge cases

## Steps
1. BA provides: original story + SP estimate + available streams + refinement notes
2. Agent proposes 2-3 slice options. BA selects.
3. Agent generates sliced stories with dependency map.

## Output per slice
SLICE [n] — [name]
Story: As a... I want... So that...
Scope: [included]
Out of scope: [moves to other slice]
Depends on: [other slice / nothing]
Parallel with: [other slice / nothing]
Stream: Frontend / Backend

DEPENDENCY MAP:
[Slice 1] must be done before [Slice 2]
[Slice 2] parallel with [Slice 3]

Original story: RETIRED

## Rules
1. Every slice has standalone value — no orphaned stories
2. Dependencies explicit
3. Original story retired when sliced
4. BA confirms slices with PO before Jira sub-tasks

BA Delivery Toolkit | Agent 5 | v1.0 | May 2026
Author: Marta Julia Zielinska | MIT License
