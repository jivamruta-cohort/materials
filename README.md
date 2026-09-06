# Cohort 1 — ramp materials

Weeks 1–2 learning material, one folder per week per skill area. **You were allocated specific
folders** — your dashboard lists which, and why, in plain words. You do not need the rest.

## How to work a module

Every module is solved the same way, and the way itself is part of what you are learning:

```
1  Copy the module folder into YOUR repository, e.g.  ramp/python-w1/
2  git switch -c ramp/python-w1
3  Read the docstring at the top of tasks.py — it is the specification
4  Solve, running the tests as you go:
       pip install pytest
       python -m pytest ramp/python-w1 -q
5  Commit as you go — small commits, subjects under 72 characters
6  Push and open a pull request in your own repository
7  Ask your mentor on Discord to review it. Merge after review.
```

**A module is done when its tests pass AND the pull request is merged after review.** The review
is not a formality — "your first reviewed code merged by the end of week 2" is a programme
promise, and this is where it happens.

## The rules that apply everywhere

- **Don't edit the test files.** They are how "done" is decided; changing them changes nothing
  about what you can do, and it shows in the diff.
- **Standard library only.** Nothing here needs a package beyond pytest.
- **Stuck for more than 30 minutes? Ask in #help-mentor.** Asking a precise question is a
  skill we are actively happy to see.

## Before the modules — orientation

**`orientation/apis-llms/`** — a bridge to do in week 2, before the project: what an API call and
an LLM call look like, and what RAG / grounding / refusal mean. Not scored — it removes the cold
start for week 3.

## The modules

| Area | Week 1 | Week 2 |
|---|---|---|
| `python` | Correct from a specification | The shapes of real code |
| `data` | Cleaning messy text | Records and matching |
| `debugging` | Find the planted bug | The classics that bite everyone |
| `git` | Branch, commit, pull request | Conflicts, ignoring, undoing |
