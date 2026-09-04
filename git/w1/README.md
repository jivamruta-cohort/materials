# git · week 1 — branch, commit, pull request

Git is graded the way the screening graded it: **on the repository you leave behind**, not on
answers about git. You will build a small practice history, and a test file will read your repo
and judge it.

## The task

Work **inside your own cohort repository**.

1. Copy this folder in as `ramp/git-w1/`.
2. Create and switch to a branch called **`ramp/git-w1`**:
   ```
   git switch -c ramp/git-w1
   ```
3. Create a file `ramp/git-w1/notes.md`. Build it up over **at least four commits**, each one a
   single coherent addition — for example: create the file with a title; add a section on
   branching; add a section on commit messages; add a section on pull requests. Write real
   sentences in your own words; the notes are for future-you.
4. Every commit subject: **under 72 characters, imperative mood, no full stop at the end.**
   "Add branching notes" — not "Added some stuff.".
5. Finish with a **clean tree** (`git status` shows nothing to commit).
6. Check yourself before pushing:
   ```
   python -m pytest ramp/git-w1 -q
   ```
7. Push, open a pull request, ask your mentor to review. **Done when the tests pass and the
   PR is merged.**

## Why these exact habits

- **A branch per piece of work** keeps `main` always releasable — the rule every team you
  join will have, spelled or unspelled.
- **Small commits with honest subjects** are how a reviewer — or you, in three months —
  navigates history. `git log --oneline` should read like a story.
- **The clean tree** is the habit that stops "oops, I committed my scratch files" forever.
