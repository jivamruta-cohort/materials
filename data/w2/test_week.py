"""data · week 2 — do not edit."""

from __future__ import annotations

import pytest
from tasks import best_match, index_by_code, load_products, token_overlap

CATALOGUE = [
    {"code": "BP-2043", "name": "brake pad front"},
    {"code": "BD-1100", "name": "brake disc"},
    {"code": "AF-330", "name": "air filter"},
]


def test_load_keeps_good_and_counts_bad() -> None:
    text = '[{"code":"A","name":"x"},{"code":"","name":"y"},{"name":"z"},{"code":"B","name":"w"}]'
    kept, skipped = load_products(text)
    assert [r["code"] for r in kept] == ["A", "B"]
    assert skipped == 2


def test_load_refuses_malformed_json() -> None:
    with pytest.raises(ValueError):
        load_products("not json at all {")


def test_index_first_record_wins() -> None:
    items = [{"code": "A", "name": "first"}, {"code": "A", "name": "second"}]
    assert index_by_code(items)["A"]["name"] == "first"


def test_token_overlap_scores() -> None:
    assert token_overlap("brake pad", "PAD brake") == 1.0
    assert token_overlap("brake pad", "brake disc") == pytest.approx(1 / 3)
    assert token_overlap("", "") == 0.0


def test_best_match_finds_the_obvious_one() -> None:
    assert best_match("front brake pad", CATALOGUE)["code"] == "BP-2043"


def test_no_overlap_is_none_never_a_guess() -> None:
    """A wrong answer delivered confidently is worse than an honest no-match."""
    assert best_match("wiper blade", CATALOGUE) is None


def test_ties_break_alphabetically_every_time() -> None:
    """The same query must always give the same answer — determinism is a feature you build,
    not luck you have."""
    tied = [{"code": "Z-9", "name": "brake kit"}, {"code": "A-1", "name": "brake kit"}]
    for _ in range(3):
        assert best_match("brake", tied)["code"] == "A-1"
