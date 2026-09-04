"""python · week 1 — correct from a specification.

WHY THIS MODULE: everything you build here starts as a written spec, and the gap between "reads
right" and "is right" lives in the boundaries — the empty list, the value exactly on the limit,
the input the spec says to refuse. Every function below has its boundaries spelled out; the tests
check exactly those. Write to the words, not to the vibe.

HOW TO WORK: see the repository README. Solve top to bottom; run
`python -m pytest ramp/python-w1 -q` after each function. Done when all tests pass and your
pull request is merged after review.
"""

from __future__ import annotations


def clamp(value: float, lo: float, hi: float) -> float:
    """Return value limited to the range [lo, hi] — both ends INCLUDED.

    clamp(5, 0, 10) -> 5 · clamp(-3, 0, 10) -> 0 · clamp(99, 0, 10) -> 10.
    If lo > hi the caller has made an error: raise ValueError.
    """
    raise NotImplementedError


def chunk(items: list, size: int) -> list[list]:
    """Split items into consecutive pieces of `size`; the LAST piece may be shorter.

    chunk([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]] · chunk([], 3) -> [].
    A size below 1 is meaningless: raise ValueError. Never modify the input list.
    """
    raise NotImplementedError


def count_words(text: str) -> dict[str, int]:
    """Count words, case-insensitively. A word is anything separated by whitespace.

    count_words("The cat the DOG") -> {"the": 2, "cat": 1, "dog": 1}.
    Empty or whitespace-only text -> {}.
    """
    raise NotImplementedError


def safe_get(record: dict, path: str, default=None):
    """Walk a dotted path into nested dicts; return `default` when any step is missing.

    safe_get({"a": {"b": 3}}, "a.b") -> 3
    safe_get({"a": {"b": 3}}, "a.x", 0) -> 0
    safe_get({"a": 1}, "a.b", 0) -> 0        # 1 is not a dict, so the path dead-ends
    Never raises for a missing path — that is the whole point of the function.
    """
    raise NotImplementedError
