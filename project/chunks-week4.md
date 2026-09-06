# Week 4 — the thin slice

Now you build. **Everyone builds the same thin slice, alone** — a mini Sales Copilot over the
35-SKU catalogue. Four small chunks; by Friday each of you has a working (if naive) copilot. Next
week it meets real scale and breaks — that's the plan.

Work each chunk the way the real team does: a short design → mentor GATE 0 → build on a branch →
tests → PR. Small commits. The six P0 rules apply from the first line (scope page §12).

---

## Chunk 1 — load & normalise the catalogue

**Goal.** Read `data/catalogue.json` into memory and make every product *matchable*.

**Build.** A `load()` that returns the 35 products; a `normalise(text)` that lowercases, collapses
whitespace and unifies separators (you built this in `data` ramp — reuse it); tolerate missing
fields (not every SKU has `extra_heavy` or every dimension).

**Done when.** `load()` returns 35 records; a test proves a messy query string
(`"  Square  12X12 "`) normalises to a stable form; no crash on a record missing a field.

**P0 touched.** #2 structured-first (you're indexing structured fields, not flat text).

---

## Chunk 2 — resolve a query to a product

**Goal.** Given a question, return the best-matching SKU(s) — or nothing.

**Build.** Match the normalised query against `code`, `category`, `size`, `colours`. Start simple
(structured field match + token overlap — the `best_match` you wrote in ramp). Return ranked
candidates with a score.

**Done when.** `"12x12 square manhole"` → `MHC 102` (or the right square 12x12); an unanswerable
query (`"kitchen sink"`) returns **empty**, not a wrong guess. Tests for both.

**P0 touched.** #2 structured-first · #1 grounding (you can only return what's in the catalogue).

---

## Chunk 3 — the grounded answer (with refusal)

**Goal.** Turn the resolved product into a sentence a salesperson can read — grounded, or a refusal.

**Build.** Compose an answer from the product's own fields (`"MHC 102 — square 12×12, 5-ton load,
dark grey, ₹1,200"`). If chunk 2 returned nothing, or the top score is weak, **refuse**:
*"I couldn't find that in the catalogue — could you give the size or category?"* Every fact in the
sentence must come from the record. You may use the LLM gateway to phrase it — but it may only use
the facts you pass it (the `orientation` system-message trick).

**Done when.** A found product yields a sentence containing only real fields; an unfound one yields
a refusal, never an invented spec. A test asserts the answer contains no number that isn't in the
record.

**P0 touched.** #1 grounding & abstention · #3 one gateway.

---

## Chunk 4 — a tiny gold set + score

**Goal.** Measure it. You cannot improve what you can't measure.

**Build.** Hand-write ~15 question→expected-SKU pairs (include 3 that *should* refuse). A `score()`
that runs them and reports: resolved-correctly %, refused-correctly %.

**Done when.** `python score.py` prints the two numbers; your naive copilot scores *something* —
and you can see exactly which queries it gets wrong. Keep this gold set; it grows all term.

**P0 touched.** #6 golden set before judges.

---

## End of week 4

You have a working mini-copilot and a number for how good it is. **It works because the catalogue
is small and clean.** Week 5: we scale it and feed it real Tanglish mess — and you'll watch it
break. That failure list becomes the four-track plan. See you at Reality Day.
