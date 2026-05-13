# RICE Prioritization Framework — BA Delivery Toolkit

Use this to prioritize requirements before sprint planning.

---

## The Formula

**RICE Score = (Reach × Impact × Confidence) / Effort**

---

## How to Score

### Reach — how many users/processes affected per sprint?
| Score | Meaning |
|---|---|
| 100 | Affects all users / entire process |
| 50 | Affects majority |
| 25 | Affects a significant minority |
| 10 | Affects few users |

### Impact — how much does it move the needle?
| Score | Meaning |
|---|---|
| 3 | Massive impact — critical to delivery |
| 2 | High impact — significant improvement |
| 1 | Medium impact — noticeable |
| 0.5 | Low impact — minor improvement |

### Confidence — how sure are we about Reach and Impact?
| Score | Meaning |
|---|---|
| 100% | Strong evidence from stakeholders |
| 80% | Good evidence, some assumptions |
| 50% | Mixed signals, significant assumptions |
| 20% | Mostly guessing |

### Effort — person-weeks to build (estimate from dev if possible)
| Score | Meaning |
|---|---|
| 0.5 | Half a week |
| 1 | One week |
| 2 | Two weeks |
| 4+ | More than a month |

---

## Output Format for /prioritize

```
## Backlog Prioritization — [Project Name]
**Date:** YYYY-MM-DD

| Requirement | Reach | Impact | Confidence | Effort | RICE Score | Priority |
|---|---|---|---|---|---|---|
| [Name] | 50 | 2 | 80% | 1 | 80 | Must Have |

## Recommended Sprint Sequence
1. [Highest RICE] — [rationale]
2. ...

## Dependencies flagged
- [Requirement A] must be done before [Requirement B]

## Assumptions made — needs BA validation
- ...
```
