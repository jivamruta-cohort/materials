"""python · week 2 — the shapes of real code.

WHY THIS MODULE: real code is rarely one clever function. It is grouping records, merging
configuration, holding a little state, and refusing bad operations with a clear error. These four
are miniature versions of things you will build for real in sprint 1.

HOW TO WORK: see the repository README. Done when all tests pass and your pull request is
merged after review.
"""

from __future__ import annotations


def group_by(records: list[dict], key: str) -> dict:
    """Group records by the value of `key`, preserving each group's original order.

    group_by([{"t":"a","v":1},{"t":"b","v":2},{"t":"a","v":3}], "t")
      -> {"a": [{"t":"a","v":1},{"t":"a","v":3}], "b": [{"t":"b","v":2}]}
    A record MISSING the key goes under the group None. Never modify the input.
    """
    raise NotImplementedError


def merge_settings(defaults: dict, overrides: dict) -> dict:
    """Merge two nested dicts: overrides win, but nested dicts merge RECURSIVELY.

    merge_settings({"a": 1, "n": {"x": 1, "y": 2}}, {"n": {"y": 9}})
      -> {"a": 1, "n": {"x": 1, "y": 9}}
    Neither input may be modified — return a new structure. A non-dict override replaces
    wholesale: merge_settings({"n": {"x": 1}}, {"n": 5}) -> {"n": 5}.
    """
    raise NotImplementedError


def parse_int_or(raw: str, default: int) -> int:
    """Parse an int out of messy input, or return the default. ' 42 ' -> 42, '4,200' -> 4200,
    'x' -> default, '' -> default. Never raises."""
    raise NotImplementedError


class InsufficientStock(Exception):
    """Raised when a removal asks for more than is held."""


class Inventory:
    """A tiny stateful object — the seed of the stock tool you will meet in sprint 2.

    add(code, qty): qty must be positive, else ValueError.
    remove(code, qty): removes stock; if the code is unknown or holds less than qty,
        raise InsufficientStock and CHANGE NOTHING — a failed removal must not half-happen.
    total(): sum of all quantities.
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, code: str, qty: int) -> None:
        raise NotImplementedError

    def remove(self, code: str, qty: int) -> None:
        raise NotImplementedError

    def total(self) -> int:
        raise NotImplementedError
