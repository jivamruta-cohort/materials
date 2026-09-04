"""debugging · week 2 — the classics that bite everyone.

Same rules as week 1: every function is already written, every one is wrong, fix each with the
smallest change. These four are not random — each is a famous Python trap that professional
code reviews catch weekly. Meeting them here, with a test pointing at the wound, is cheaper
than meeting them in production.

  1 · the mutable default argument that remembers between calls
  2 · the bare except that swallows the error you needed to see
  3 · the off-by-one in pagination
  4 · the shallow copy that is secretly still shared

HOW TO WORK: see the repository README. Done when all tests pass and your PR is merged.
"""

from __future__ import annotations


def append_tag(tag: str, tags: list | None = []) -> list:
    """Return a NEW list of existing tags plus this one. Calls must be independent:
    append_tag('a') then append_tag('b') -> ['a'] then ['b'], never ['a', 'b']."""
    tags.append(tag)
    return tags


def read_scores(text: str) -> list[int]:
    """One integer per line; blank lines are SKIPPED; a malformed line raises ValueError
    naming the bad line. Silently dropping bad data is how a wrong total becomes a mystery
    in week 13."""
    out = []
    for line in text.splitlines():
        try:
            out.append(int(line.strip()))
        except Exception:
            continue
    return out


def page_slice(items: list, page: int, per_page: int) -> list:
    """1-INDEXED pages: page_slice([a,b,c,d,e], 1, 2) -> [a,b]; page 2 -> [c,d]; page 3 -> [e].
    A page past the end -> []. page or per_page below 1: ValueError."""
    if page < 1 or per_page < 1:
        raise ValueError("page and per_page start at 1")
    start = page * per_page
    return items[start : start + per_page]


def clone_grid(grid: list[list[int]]) -> list[list[int]]:
    """An INDEPENDENT copy of a 2-D grid: changing a cell in the copy must never change the
    original. That is the entire contract."""
    return list(grid)
