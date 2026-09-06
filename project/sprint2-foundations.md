# Sprint 2 (weeks 6–7) — foundations, four tracks

The solo phase is over. Now four people build one copilot in one repo — and the only way that works
is to **freeze the interfaces first**, then each track builds behind its own contract against the
others' fakes. This is the CORE-C1 lesson from the platform, lived.

## Week 6, day 1 — freeze the four interfaces (everyone, together)

Before anyone writes track code, agree and freeze the four contracts from
[/project §4](https://vtu-internship-proposal.vercel.app/project/#design): `ProductKB`,
`Retriever`, `StockTool`, `Gateway`. The starter repo already ships them in `app/interfaces.py`
with fakes — review them together, adjust if a track needs a field, then **freeze**. After this,
a change to an interface is a shared decision, never a surprise.

**Why it matters:** with frozen contracts + fakes, T4 can build the API against a fake retriever
while T2 is still building the real one. Nobody waits.

## The four tracks

| Track | Owns | This sprint's goal |
|---|---|---|
| **T1 · Platform & gate** | supervisor loop, the safety gate, tool routing | requests flow through a gate that grounds/refuses; the stock tool is callable |
| **T2 · Retrieval & answers** | the matcher, the grounded answer | structured-first + dense retrieval at full scale; the answer engine |
| **T3 · Data & KB** | ingestion, the Product KB (Postgres + pgvector) | the catalogue loaded into pgvector; the ingestion pipeline, v1 |
| **T4 · API, UI & evals** | FastAPI, the web chat, the eval harness | a chat UI that shows products with photos; the gold-set harness with numbers |

## The chunks

### T1 — the gate
- **Supervisor loop**: route a request → capsule → response, with a trace of what happened.
- **The safety gate**: grounding check (answer must cite catalogue sources) · refusal when it
  can't · PII redaction before any model call · a hard spend cap at the gateway (P0 #1,#3,#4).
- **Tool routing**: the supervisor calls `StockTool` when the query needs stock. `FakeStockTool`
  now; real interface shape.
- *Done when:* a query with no grounded answer is refused, not guessed; a PII string never reaches
  the gateway (test proves it); the spend cap blocks a runaway loop.

### T2 — retrieval & answers
- **Hybrid retrieval**: structured-first match + dense (pgvector) fallback + a rerank. This is
  where flat search died on Reality Day — beat it and benchmark the difference (P0 #2).
- **The grounded answer**: compose from the resolved product's fields; refuse on weak match.
- *Done when:* accuracy on the gold set beats the week-4 thin slice by a measured margin; every
  answer cites its SKU sources.

### T3 — data & KB
- **Product KB on pgvector**: load the catalogue + embeddings into Postgres; `ProductKB.search/get`.
- **Ingestion pipeline v1**: parse the catalogue → normalise → chunk at the record boundary →
  embed → index. Idempotent — re-running updates, never duplicates (P0 #5).
- *Done when:* the full catalogue is searchable from pgvector; re-ingesting changes no row counts.

### T4 — API, UI & evals
- **FastAPI + web chat**: `/ask` returns a grounded answer; a simple chat page renders the product
  **with its photo**.
- **The eval harness**: the gold set as a runnable suite reporting accuracy · refusal · stability
  (P0 #6). Everyone's work is measured against it from now on.
- *Done when:* a mentor can chat to the copilot in a browser and see photos; `python score.py`
  prints the three numbers.

## Primers (read the one for your track)

- **pgvector in 15 minutes** — a vector column, an index, a nearest-neighbour query.
- **The safety gate** — send / ask / escalate, and why confidence never comes from the generator.
- **Hybrid retrieval** — BM25 + dense + RRF, and why structured-first wins on a catalogue.
- **FastAPI beyond hello-world** — request models, dependency injection, testing routes.

*(Primers live in `project/primers/` — short reads, each with a runnable snippet.)*

## How this wires to Sprint 3

By end of week 7 the copilot works end-to-end at scale, on stubs where the real thing isn't ready.
Sprint 3 makes it conversational (follow-ups), wires the real tool-calling, adds the **second-
catalogue upload**, and takes the **capstone go/no-go**. See `sprint3-agents.md`.
