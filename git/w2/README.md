# git · week 2 — conflicts, ignoring, undoing

Three things every engineer meets in their first month, practised where they are cheap. Work
**inside your own cohort repository**; copy this folder in as `ramp/git-w2/`.

## Task 1 — cause a conflict on purpose, then resolve it

Merge conflicts are not accidents to fear; they are git asking a fair question — *two truths
changed the same line, which do you want?* You will create one deliberately:

1. `git switch -c ramp/git-w2` · copy this folder in · create `ramp/git-w2/story.md` with a
   line like `The part costs 100 rupees.` and commit.
2. Branch A: `git switch -c ramp/git-w2-a` → change the line to `...costs 120 rupees.` →
   commit → switch back to `ramp/git-w2`.
3. Branch B: `git switch -c ramp/git-w2-b` → change the SAME line to `...costs 90 rupees.` →
   commit → switch back to `ramp/git-w2`.
4. `git merge ramp/git-w2-a` (clean) then `git merge ramp/git-w2-b` — **conflict.** Open the
   file, see the `<<<<<<<` markers, decide the truth (any price you like), remove the markers,
   `git add`, `git commit`.

Your history now contains a real merge commit and zero markers — the test checks both.

## Task 2 — teach git what to ignore

1. Create `ramp/git-w2/scratch.log` with anything in it.
2. Add a `.gitignore` **in the repository root** (or extend the existing one) so that `*.log`
   files are ignored. `git status` must not show scratch.log; `git check-ignore` must confirm.

Byproducts polluting history is the exact bug the screening grader had — now you have fixed it
yourself.

## Task 3 — undo a commit without rewriting history

1. Add a line `TEMPORARY: delete me` to story.md, commit it with subject `Add temporary line`.
2. Undo it the safe way: `git revert HEAD` (keep the default `Revert "Add temporary line"`
   subject). History keeps both commits — the mistake AND its correction, visible. That is the
   difference between revert (a public undo) and the history-rewriting commands this programme
   forbids on shared branches.

## Check, then ship

```
python -m pytest ramp/git-w2 -q
```
Push, open the PR, mentor review. **Done when tests pass and the PR is merged.**
