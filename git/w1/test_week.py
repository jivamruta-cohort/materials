"""git · week 1 — do not edit. Reads YOUR repository and judges the history you built.

Run from your repository root:  python -m pytest ramp/git-w1 -q
Quality checks are gated on the work existing at all — an empty repo scores nothing, it does
not pass by default (the lesson the screening's first draft taught us).
"""

from __future__ import annotations

import subprocess

import pytest

BRANCH = "ramp/git-w1"
MIN_COMMITS = 4
MAX_SUBJECT = 72


def git(*args: str) -> str:
    out = subprocess.run(["git", *args], capture_output=True, text=True, check=False,
                         encoding="utf-8")
    return (out.stdout or "").strip()


@pytest.fixture(scope="module")
def subjects() -> list[str]:
    """Subjects of the commits that touch this module's notes file."""
    log = git("log", "--pretty=%s", "--", "ramp/git-w1/notes.md")
    return [s for s in log.splitlines() if s.strip()]


def test_the_branch_exists() -> None:
    branches = [b.strip() for b in git("branch", "--format=%(refname:short)").splitlines()]
    assert BRANCH in branches, f"no `{BRANCH}` branch — found {branches}"


def test_notes_file_exists_with_real_content() -> None:
    from pathlib import Path

    p = Path("ramp/git-w1/notes.md")
    assert p.exists(), "ramp/git-w1/notes.md does not exist"
    assert len(p.read_text(encoding="utf-8").split()) >= 40, "write real notes, not a stub"


def test_built_up_over_at_least_four_commits(subjects: list[str]) -> None:
    assert len(subjects) >= MIN_COMMITS, (
        f"{len(subjects)} commit(s) touch notes.md — the point is building history in steps"
    )


def test_subjects_are_short_imperative_and_unpunctuated(subjects: list[str]) -> None:
    assert len(subjects) >= MIN_COMMITS, "not enough commits to judge"
    assert not [s for s in subjects if len(s) > MAX_SUBJECT], "subject over 72 characters"
    assert not [s for s in subjects if s.rstrip().endswith(".")], "no full stop at the end"
    assert len(set(subjects)) >= MIN_COMMITS, "repeated subjects — each commit is one change"


def test_finished_with_a_clean_tree(subjects: list[str]) -> None:
    assert len(subjects) >= MIN_COMMITS, "not enough commits to judge"
    assert git("status", "--porcelain") == "", "uncommitted changes left behind"
