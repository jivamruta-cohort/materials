# Week 5 — Reality Day

Your week-4 thin slice works. This week we prove it only works because the data was small and
clean — then that failure list becomes the four-track plan. Reality Day is a house tradition, not a
punishment: **the losing configurations are the lesson.**

## Part 1 — scale and mess (morning)

Run your copilot against conditions it was never built for:

| We do | What breaks | The lesson (→ which track fixes it)|
|---|---|---|
| Load the **full catalogue** (hundreds of SKUs, from the PDF via a rough parse) | resolution accuracy falls | structured-first + dense retrieval → **T2/T3** |
| Feed **real Tanglish** queries with typos | matching misses | normalisation isn't enough → **T2** |
| Ask something not in the catalogue | some copilots guess | grounding/refusal must hold at scale → **T1** |
| Ask the same thing twice, fast | duplicate work / cost | idempotency, caching → **T1/T4** |
| Pull the model (no gateway) | crash | degrade, don't die → **T1** |

Write down every failure. That list **is** Sprint 2's backlog.

## Part 2 — the bake-off (afternoon)

Each intern runs their copilot against a **shared held-out query set** (you have not seen it).
Report three numbers: resolved-correctly %, refused-correctly %, and the one query that embarrassed
you most. Then, together:

- Whose approach held up best at scale, and **why** — stage order? structured-first? a threshold?
- Which failures are common to all four → the shared priorities.

## Part 3 — form the four tracks

From the failure list, split into the four tracks (see `sprint2-foundations.md`). Everyone has now
built the whole thing solo, so every track owner understands the whole system — which is the point
of having built it alone first.

## Done when

- [ ] every intern has run their copilot at full scale and against the held-out set
- [ ] a shared, written failure list exists — the Sprint-2 backlog
- [ ] the four tracks are assigned, each owner can say why their track exists

**The mindset:** today your toy broke. That is the most valuable thing that happens in the twelve
weeks — because now you know, from your own code, why production systems are built the way they are.
