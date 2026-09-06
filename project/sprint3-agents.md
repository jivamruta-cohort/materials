# Sprint 3 (weeks 8–9) — the agent comes alive

The copilot answers one question well. This sprint it holds a conversation, acts through tools for
real, ingests a catalogue it's never seen, and — if the core is solid — gains sight.

## Week 8 — the go/no-go

At the start of week 8, the mentor panel judges: **is the core solid?** (Sprint-2 done-bars met,
gold-set numbers healthy, no track blocking another.) If yes → the capstone is on. If not → the
capstone waits, and this sprint deepens the core instead. **We never ship two half-built things.**

## The chunks

### T1 — tool-calling & context, for real
- **Real tool-calling loop**: the supervisor decides when to call `StockTool`, calls it, and folds
  the result into the answer ("in stock at Branch-CBE: 12").
- **Session memory**: a follow-up ("…and in dark grey?") continues the last product.
- *Done when:* a two-turn conversation resolves a follow-up; a stock question returns a real
  (stub-backed) quantity in the answer.

### T3 — dynamic catalogue upload
- **Upload endpoint**: a mentor uploads a **second catalogue**; the ingestion pipeline parses,
  normalises, embeds and indexes it live — **no redeploy** (P0 #5, idempotent).
- *Done when:* upload a 2nd catalogue, then immediately ask about a product only in it, and the
  copilot answers. Re-uploading the same file changes no row counts.

### T2 — the capstone (if go): photo → product
- **Image embeddings with open CLIP (ViT-B-32) on CPU** — free, no GPU. Embed each product image
  at ingestion; embed an uploaded photo; return the nearest catalogue product.
- **Competitor photo → equivalent**: the same path — a competitor's product photo returns the
  closest Pupa-catalogue item, with a confidence and a refusal below threshold.
- *Done when:* uploading a product photo returns the right SKU; an unrelated photo (a car) is
  refused, not force-matched.
- *If no-go:* T2 instead hardens retrieval — synonyms, size-range queries, better rerank.

### T4 — integrate & show
- **Wire the tracks together**: one copilot, real retrieval + real gate + real ingestion behind the
  API; the chat UI shows photos, stock, and (if capstone) a photo-upload box.
- **Grow the gold set**: add follow-up cases, upload cases, and (if capstone) image cases.
- *Done when:* the whole flow works in the browser end-to-end against real components.

## Primers
- **Tool-calling** — how an agent decides to call a function and uses the result.
- **Session memory** — anchoring a conversation on the last entity.
- **Multimodal embeddings with CLIP** — image → vector, on CPU, precomputed at ingestion.

## Wires to Sprint 4
By end of week 9 the copilot is feature-complete on real components. Sprint 4 makes it
**production-grade**: cost caps, fallbacks, caching, observability, and the eval harness with
numeric bars and a failure budget. See `sprint4-production.md`.
