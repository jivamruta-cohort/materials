"""data · week 2 — records and matching.

WHY THIS MODULE: this is retrieval in miniature — load records, index them, score how well a
query matches, and refuse to answer when nothing matches well enough. In sprint 1 you will do
exactly this over a real catalogue; the shape of the code is identical, only the size changes.
Note best_match's rules carefully: DETERMINISTIC ties and an honest None are what separate a
system you can trust from a demo.

HOW TO WORK: see the repository README. Done when all tests pass and your pull request is
merged after review.
"""

from __future__ import annotations

import json  # noqa: F401 — you will want this


def load_products(json_text: str) -> tuple[list[dict], int]:
    """Parse a JSON array of product dicts. Keep records that have a non-empty 'code' and
    'name'; count the rest as skipped.

    Returns (kept_records, skipped_count). Malformed JSON entirely: raise ValueError.
    """
    raise NotImplementedError


def index_by_code(products: list[dict]) -> dict[str, dict]:
    """Index products by their 'code'. On a duplicate code the FIRST record wins — the same
    rule the screening dedupe used, for the same reason: re-imports must not reshuffle truth."""
    raise NotImplementedError


def token_overlap(a: str, b: str) -> float:
    """How alike two texts are, 0.0 to 1.0: shared distinct words / total distinct words
    (case-insensitive; words split on whitespace). Both empty -> 0.0.

    token_overlap('brake pad', 'PAD brake') -> 1.0
    token_overlap('brake pad', 'brake disc') -> 1/3
    """
    raise NotImplementedError


def best_match(query: str, products: list[dict]) -> dict | None:
    """The product whose 'name' best matches the query, by token_overlap.

    Rules, all of which the tests check:
    - score 0 for every product -> return None. NEVER return an arbitrary product: a wrong
      answer delivered confidently is worse than an honest "no match".
    - a TIE on score breaks alphabetically by 'code' — the same query must always give the
      same answer, or two runs of your system disagree and neither is wrong.
    """
    raise NotImplementedError
