# Primer — hybrid retrieval (T2, Sprint 2)

On Reality Day flat dense search collapsed. Hybrid retrieval is why the real system doesn't: it
combines three legs, each catching what the others miss.

## The three legs

1. **Structured-first** — match the query against real fields (code, category, size, colour). If
   someone asks "12x12 square", an exact field match is *right*, fast, and free. Do this first.
2. **Dense (pgvector)** — for the fuzzy remainder ("something for a drain outside"), embed the query
   and find the nearest product vectors. Catches meaning that exact-match can't.
3. **Rerank** — take the top candidates from both and order them by a sharper score before you
   answer.

```python
def resolve(query):
    structured = field_match(query)          # exact/near-exact on fields — highest trust
    if structured and structured[0].score >= STRONG:
        return structured                    # don't even embed — you're sure
    dense = pgvector_search(embed(query), k=10)
    return rerank(query, structured + dense)[:5]
```

## Why order matters (the Reality-Day lesson)

Dense-only search on a **structured** catalogue throws away the very thing that makes it
answerable — the fields. "5 ton load" is a number in a column; a pure embedding blurs it into
vibes. **Never flat-search structured data** (P0 #2). Structured-first, dense as the fallback.

## RRF — combining two ranked lists

When you have two rankings (structured, dense), Reciprocal Rank Fusion is a simple, robust merge:
each item scores `sum(1 / (k + rank))` across the lists it appears in (k≈60). Items that rank well
in *both* rise to the top. It needs no tuning and beats naive score-adding.

## Watch for
- **Confidence still comes from the match, not the model** (feeds the gate — see the gate primer).
- **Benchmark every change** against the gold set — "it feels better" is not a result. This is how
  you'll show "raised accuracy from X% to Y%" (P0 #6).
- **Return sources.** The answer must cite which SKUs it used, or grounding can't be checked.

## Your task uses this for
Replacing the week-4 token-overlap resolver with structured-first + dense + rerank, and proving on
the gold set that it beats the thin slice at full scale.
