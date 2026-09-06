# Week 3 — set up the environment and learn the pieces

**This whole week has one goal: everything runs, and you understand what each piece is.** No
product feature yet. An engineer who rushes past setup pays for it every week after — so we don't.

By Friday you can say: *"FastAPI serves a page, Postgres with pgvector stores a vector, the LLM
gateway answers a question, and I've done a hello-world of each."*

## 1 · The stack you're standing up (and why each exists)

| Piece | What it does | Why |
|---|---|---|
| **Python 3.11 + FastAPI** | the web service | how AI backends are written |
| **Postgres + pgvector** | stores the catalogue **and** its embeddings | retrieval needs vectors next to data |
| **LiteLLM gateway** | one door to cloud LLMs (DeepSeek/Groq/Gemini free tiers) | cost + safety controlled in one place; **no GPU** |
| **httpx** | make HTTP calls | you did the shapes in `orientation/apis-llms` |

If `orientation/apis-llms` felt new, do it first — this week assumes those four shapes.

## 2 · Get it running (in order — each step must pass before the next)

```bash
# a. clone the starter repo, then:
git clone https://github.com/jivamruta-cohort/sales-copilot-starter
cd sales-copilot-starter
python -m venv .venv && . .venv/bin/activate     # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt

# b. FastAPI runs
uvicorn app.main:app --reload
#    open http://127.0.0.1:8000/health  → {"ok": true}

# c. Postgres + pgvector (cloud, free tier — your mentor gives the connection string)
python scripts/db_check.py               # prints: connected, pgvector available

# d. load the fixed catalogue
python scripts/load_catalogue.py         # 35 SKUs inserted
```

**Checkpoint:** all four green. If one fails, that's the week's real work — fixing a setup problem
is engineering, not a detour. Ask in `#help-mentor` with the exact error.

## 3 · The three hello-worlds (read the code, then run each)

Each is a tiny script in `hello/`. Read it, run it, change one thing, run again. That's how you
learn a piece — not by reading about it.

| Hello-world | You run | You learn |
|---|---|---|
| `hello/gateway.py` | ask the LLM one question through the gateway | an LLM call is an API call (the `orientation` shape, live) |
| `hello/embed.py` | turn "angle valve" into a vector, print its length | an embedding is just a list of numbers |
| `hello/search.py` | embed 3 products, embed a query, find the nearest | **this is retrieval** — nearest vector wins |

`hello/search.py` is the important one: it is RAG in 20 lines. Everything in the project grows from
it.

## 4 · Read the architecture (30 minutes)

Read **§3 Architecture** and **§4 Design** on the scope page:
https://vtu-internship-proposal.vercel.app/project/

Then, in your own words, answer these in your week-3 diary entry — the mentor checks understanding,
not code, this week:

- What are the two agents, and what does each do?
- Where does an answer's *grounding* come from — the model, or the catalogue?
- What is the ingestion pipeline for?
- Which of the four interfaces will your track own?

## Done when

- [ ] FastAPI `/health` returns ok
- [ ] Postgres + pgvector connected; the 35-SKU catalogue loaded
- [ ] all three hello-worlds run and you changed one thing in each
- [ ] you can explain the architecture in your diary in your own words

**Do NOT start a feature this week.** Week 4 is the thin slice; this week is the foundation it
stands on.
