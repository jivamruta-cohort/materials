"""git · week 2 — do not edit. Run from your repository root: python -m pytest ramp/git-w2 -q"""

from __future__ import annotations

import subprocess
from pathlib import Path


def git(*args: str) -> str:
    out = subprocess.run(["git", *args], capture_output=True, text=True, check=False,
                         encoding="utf-8")
    return (out.stdout or "").strip()


def test_task1_a_real_merge_commit_exists() -> None:
    merges = git("log", "--merges", "--pretty=%s", "--", "ramp/git-w2/story.md")
    all_merges = git("log", "--merges", "--oneline")
    assert merges or all_merges, "no merge commit — did you do the two-branch merge?"


def test_task1_no_conflict_markers_survived() -> None:
    # Built at runtime so THIS file never matches its own check.
    marker = "<" * 7
    hits = git("grep", "-l", marker, "--", "ramp/")
    assert hits == "", f"conflict markers still committed in: {hits}"
    story = Path("ramp/git-w2/story.md")
    assert story.exists(), "ramp/git-w2/story.md does not exist"
    assert marker not in story.read_text(encoding="utf-8")


def test_task2_log_files_are_ignored() -> None:
    scratch = Path("ramp/git-w2/scratch.log")
    assert scratch.exists(), "create ramp/git-w2/scratch.log first"
    ignored = subprocess.run(["git", "check-ignore", str(scratch)], capture_output=True)
    assert ignored.returncode == 0, "git does not ignore scratch.log — check your .gitignore"
    assert "scratch.log" not in git("status", "--porcelain"), "scratch.log shows in git status"


def test_task3_the_undo_is_a_revert_not_a_rewrite() -> None:
    subjects = git("log", "--pretty=%s", "-n", "30").splitlines()
    assert any(s.startswith("Revert") for s in subjects), "no revert commit in recent history"
    assert any("temporary" in s.lower() for s in subjects), (
        "the reverted commit itself should still be IN history — revert adds, never erases"
    )
    assert "TEMPORARY: delete me" not in Path("ramp/git-w2/story.md").read_text(
        encoding="utf-8"
    ), "the temporary line is still in the file — the revert did not take"
