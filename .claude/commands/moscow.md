# Agent 2a — MoSCoW Prioritisation
**Command:** /moscow
**Trigger:** After /discover. Run with business — not solo BA.

## Categories
Must Have — non-negotiable for launch
Should Have — important, include if capacity allows
Could Have — nice to have, only if time permits
Won't Have — explicitly out of scope this cycle

## How It Works
Agent presents each requirement from /discover.
BA and business decide category together.
Agent flags conflicts — who resolves, by when.

## Output
MoSCoW OUTPUT — [Project]
MUST HAVE: [list]
SHOULD HAVE: [list]
COULD HAVE: [list]
WON'T HAVE: [list]
Conflicts: [requirement — owner — deadline]
Approved by: [name] | Date: [date]

## Rules
1. If everything is Must Have — nothing is
2. Won't Have as important as Must Have
3. Conflicts must have named owner
4. Business sign-off before /prioritize

## Agent Boundaries

This agent can:
- Present each requirement for BA and business to categorise
- Record the assigned MoSCoW category as directed
- Flag conflicts where requirements cannot all be Must Have
- Name the conflict owner and deadline as provided by BA and business

This agent cannot:
- Assign MoSCoW categories without BA and business input
- Resolve conflicts — conflicts need a named human owner
- Approve the MoSCoW output — business sign-off is required
- Proceed to /prioritize without explicit sign-off

Hands off to: BA and business to sign off the MoSCoW output, then /prioritize.

---

BA Delivery Toolkit | Agent 2a | v1.0 | May 2026
Author: Marta Julia Zielinska | MIT License
