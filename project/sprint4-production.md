# Sprint 4 (weeks 10–11) — make it production-grade

A demo that works once is not a product. This sprint turns the copilot into something that survives
a bad day: costs bounded, dependencies failing gracefully, every answer traceable, quality proven
with numbers. This is the sprint that most separates an AI engineer from someone who "did a chatbot."

## The chunks (mostly cross-track — the copilot as one system)

### Cost & reliability (T1 lead)
- **Hard spend cap, enforced**: `warn` and `hard-stop` thresholds; a runaway loop degrades before
  it burns budget (P0 #4).
- **Provider fallback**: primary model down → fall back to another; the gateway is the one place
  this lives (P0 #3).
- **Degraded mode**: model or ERP down → the copilot still answers what it can from the catalogue,
  or refuses cleanly. Never a 500 to a salesperson.
- *Done when:* kill the model in a test → the app degrades, doesn't crash; the cap blocks a loop.

### Caching (T2/T3)
- **Cache hits are candidates, not answers**: serve a cached retrieval fast, but confirm against the
  structured match before answering — a stale cache must not ship a wrong spec.
- *Done when:* a repeated query is faster; changing a catalogue row invalidates its cached answer.

### Observability (T4 lead)
- **Trace every model call**: one request → a trace of route, retrieval, tool calls, tokens, cost,
  latency. Structured logs you can search.
- *Done when:* for any answer, a mentor can see exactly what the copilot did and what it cost.

### The eval harness, for real (T4)
- **Numeric bars + a failure budget**: grow the gold set to a real size; set the bars (accuracy,
  refusal recall) and a regression budget; **CI fails a change that drops below them** (P0 #6).
- *Done when:* the eval runs in CI; a change that makes the copilot worse is blocked, not merged.

## Week 11 — feature freeze
End of week 11: no new features. The copilot is complete and measured. Everything after is hardening
and handover.

## Primers
- **Cost control & circuit breakers** — thresholds, reserve-before-call, degrade order.
- **Caching without lying** — candidate-not-answer, invalidation.
- **Observability** — traces, structured logs, what to measure per request.

## Wires to the close
By end of week 11 you have a production-grade, benchmarked copilot. Weeks 12–14 harden it (security,
load), write it up, prepare each intern's résumé and certification, and end at the **mentor
acceptance panel**. See `close-harden.md`.
