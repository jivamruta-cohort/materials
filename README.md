# Cohort 1 — your journey, end to end

Everything you build, in order. Screening → preparation → practice → project. Each step is the
on-ramp to the next; follow them top to bottom.

> **Where you code:** every folder here (and the project starter repo) has a **devcontainer** —
> open it in **GitHub Codespaces** (green "Code" button → Codespaces → one click, runs in your
> browser, nothing to install) or locally in VS Code ("Reopen in Container"). Same environment
> either way. A weak laptop or a Chromebook is fine.

---

## The map

| # | Stage | Weeks | Where | You end able to… |
|---|---|---|---|---|
| 1 | **Screening** | 1 | the screening repo (your mentor invites you) | — it decides what you're taught next |
| 2 | **Ramp modules** | 1–2 | `python/` `data/` `debugging/` `git/` (you're allocated some) | write correct code, handle messy data, debug, use Git & PRs |
| 3 | **Orientation** | 2 | `orientation/apis-llms/` | call an API and an LLM; know what RAG, grounding, refusal mean |
| 4 | **Project setup** | 3 | `project/setup-week3.md` → the [starter repo](https://github.com/jivamruta-cohort/sales-copilot-starter) | stand up FastAPI + pgvector + the gateway; the three hello-worlds |
| 5 | **Thin slice** | 4 | `project/chunks-week4.md` | a working mini Sales Copilot (solo) |
| 6 | **Reality Day** | 5 | `project/reality-day.md` | see it break at scale; form the four tracks |
| 7 | **Sprint 2 — foundations** | 6–7 | `project/sprint2-foundations.md` | the real capsule, four tracks, interfaces frozen |
| 8 | **Sprint 3 — the agent** | 8–9 | `project/sprint3-agents.md` | tool-calling, follow-ups, catalogue upload, the photo capstone |
| 9 | **Sprint 4 — production** | 10–11 | `project/sprint4-production.md` | cost caps, fallbacks, caching, observability, evals |
| 10 | **Harden & hand over** | 12–14 | `project/close-harden.md` | security, docs, benchmark, résumé, the mentor acceptance panel |

Full scope, architecture and the weekly plan: **https://vtu-internship-proposal.vercel.app/project/**

---

## How to work anything here

1. Open the folder in Codespaces (or locally in a dev container).
2. Read the `README.md` or the docstring — it's the spec.
3. Solve; run the tests (`pip install pytest && python -m pytest -q`).
4. Commit small, on a branch; open a PR; your mentor reviews.
5. Done = tests pass **and** the PR is merged after review.

## The rules that never change

- Branch, then PR. Never commit to `main`.
- Don't edit the test files — they define "done".
- Ask in `#help-mentor` after 30 minutes stuck — a precise question is a skill.
- In the project: every answer traces to the catalogue, or the copilot **refuses**. A confident
  wrong spec is the worst outcome. Prices are representative, never a live quote.

## The modules (the study, in detail)

**Orientation** — `orientation/apis-llms/` — do this in week 2, before the project.

| Area | Week 1 | Week 2 |
|---|---|---|
| `python` | Correct from a specification | The shapes of real code |
| `data` | Cleaning messy text | Records and matching |
| `debugging` | Find the planted bug | The classics that bite everyone |
| `git` | Branch, commit, pull request | Conflicts, ignoring, undoing |
