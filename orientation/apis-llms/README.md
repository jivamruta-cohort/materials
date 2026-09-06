# Orientation — APIs & LLMs, the basics

**Do this in week 2, before the project starts.** It is a *bridge*, not a scored test — it removes
the cold start so that in week 3, calling an API and calling an LLM for the first time isn't a wall.

Everything up to now (the ramp modules) was local Python. The project talks to the outside world:
it calls a language model over HTTP and reads product data from an API. This module gives you the
four shapes you'll use constantly, on building-materials examples so it primes the real project.

## Read this first (10 minutes)

**An API call is a function call over the network.** You send a request (a URL, a method like GET
or POST, maybe a JSON body); you get back a response (a status code + usually JSON).

- **Status codes**: `200` ok · `4xx` you did something wrong (bad request, `401` no/!bad key,
  `404` not found) · `5xx` the server broke. Your code must *branch* on these, not assume `200`.
- **JSON** is how APIs speak: objects (`{}`) and arrays (`[]`) → Python dicts and lists.
- **An API key** identifies you and is secret — it goes in a header, never in the URL, never in
  code, never in git.

**An LLM call is just an API call with a particular shape.** You POST a list of *messages*
(a `system` instruction + the `user` question); you get back JSON with the model's reply inside.
That's it — no magic. In the project every model call goes through **one gateway** (so cost and
safety can be controlled in one place), but the shape is the same.

**RAG, grounding, refusal** — the ideas the project is built on, in a sentence each:
- **RAG** (retrieval-augmented generation): find the relevant facts *first* (from the catalogue),
  then let the model answer *using only those facts*.
- **Grounding**: the answer must trace to those facts — a product spec comes from the catalogue,
  never from the model's imagination.
- **Refusal**: if the facts aren't there, the agent says so instead of guessing. A confident wrong
  spec is the worst outcome.

## The exercises (`tasks.py`)

Four network-free functions — the shapes you'll use in week 3, testable today with no key:

1. `status_meaning(code)` — classify an HTTP status.
2. `parse_products(json_text)` — turn a JSON API response into a list of products.
3. `build_llm_request(system, user)` — build the message payload an LLM gateway expects.
4. `extract_answer(response_json)` — pull the reply text out of an LLM response.

Run them:
```
pip install pytest
python -m pytest -q          # from this folder
```

## See the real thing (read; you'll run it live in week 3)

This is what an actual call looks like — you don't need to run it now (it needs the gateway that
week 3 sets up), but read it so it's familiar:

```python
import httpx

# 1 · a real GET to a product API — returns JSON
resp = httpx.get("https://api.example.com/products?q=angle+valve",
                 headers={"Authorization": "Bearer <key>"}, timeout=10)
products = resp.json()          # -> a list of dicts, like parse_products handles

# 2 · a real LLM call through the gateway
answer = httpx.post("https://gateway.example.com/ask",
                    headers={"Authorization": "Bearer <key>"},
                    json=build_llm_request(
                        system="Answer only from the given catalogue facts, or say you don't know.",
                        user="What size is the AV-2043 angle valve?"),
                    timeout=30)
reply = extract_answer(answer.json())
```

Notice the system message in #2 — *"answer only from the facts, or say you don't know"* — that one
line is grounding and refusal in miniature. You'll build the real version in the project.
