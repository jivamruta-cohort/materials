# Primer — the safety gate (T1, Sprint 2)

The gate is the one place every answer passes through before it reaches a person. Its job is to make
a wrong or unsafe answer *impossible to send*, not merely unlikely.

## The three outcomes: send · ask · escalate

Every turn ends in exactly one:

- **send** — the answer is grounded (traces to catalogue sources) and confident → deliver it.
- **ask** — under-specified or ambiguous → ask one clarifying question ("what size?").
- **escalate/refuse** — can't ground it, or it's out of scope → say so, hand to a human. **Never
  guess a spec.**

```python
def gate(query, candidates, answer):
    if not candidates or candidates[0].score < THRESHOLD:
        return Refuse("no confident match — could you give the size or category?")
    if answer.sources == ():                 # nothing to ground on
        return Refuse("I can't back that up from the catalogue.")
    return Send(answer)
```

## The rule that makes it real: confidence is external

**The model never scores its own confidence.** An LLM will happily say "definitely the X-200" about
a product that doesn't exist. Confidence comes from *retrieval* (the match score) and *grounding*
(are there real sources?), decided outside the model. This is P0 #1.

## The other three jobs of the gate

- **PII redaction** — strip phone numbers, names, ids *before* the payload reaches the gateway.
  A redactor that runs after the model call is useless.
- **Injection filtering** — a customer message saying "ignore your instructions" must not reach the
  system prompt unfiltered.
- **Spend cap** — the gate refuses to make a call that would cross the budget line (P0 #4).

## Watch for
- **Redact before, not after.** The single most common gate bug.
- **A refusal is a code, not a sentence** — return a reason your UI can branch on, then phrase it.
- **The gate is one place.** If grounding logic also lives in the capsule and the UI, they drift.
  One gate, called by everything (P0 #3 is the same idea for the model boundary).

## Your task uses this for
The supervisor loop wraps every turn in the gate; tests prove a PII string never reaches the
gateway and an ungroundable query is refused, not answered.
