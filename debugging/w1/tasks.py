"""debugging · week 1 — find the planted bug.

EVERY FUNCTION BELOW IS ALREADY WRITTEN, AND EVERY ONE IS WRONG. Your job is to find each bug
and fix it with the SMALLEST change that makes the tests pass. Do not rewrite from scratch —
reading code you did not write and locating the fault is most of the job of a working engineer.

METHOD (use it every time, it is the module's real content):
  1. Run the tests. READ the failure — expected vs actual is a clue, not noise.
  2. Form a hypothesis: "it fails because ___". Say it out loud.
  3. Check the hypothesis: add a print, or step through with your eyes on paper.
  4. Fix the SMALLEST thing. Re-run. If a different test broke, your fix was a guess.

HOW TO WORK: see the repository README. Done when all tests pass and your PR is merged.
"""

from __future__ import annotations


def average(nums: list[float]) -> float:
    """The arithmetic mean of nums. average([1, 2, 4]) -> 2.333..., not 2."""
    return sum(nums) // len(nums)


def find_max(nums: list[int]) -> int:
    """The largest value. Must work for all-negative lists: find_max([-5, -2, -9]) -> -2.
    Empty list: raise ValueError."""
    if not nums:
        raise ValueError("empty")
    biggest = 0
    for n in nums:
        if n > biggest:
            biggest = n
    return biggest


def unique_keep_order(items: list) -> list:
    """The distinct items, keeping the order of FIRST appearance.
    unique_keep_order([3, 1, 3, 2, 1]) -> [3, 1, 2]."""
    return sorted(set(items))


def pluralize(word: str, n: int) -> str:
    """'1 item' but '0 items', '2 items'. Only n == 1 is singular."""
    if n >= 1:
        return f"{n} {word}"
    return f"{n} {word}s"
