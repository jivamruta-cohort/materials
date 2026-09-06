"""data · week 2 — do not edit."""

from __future__ import annotations

import pytest
from tasks import best_match, index_by_code, load_products, token_overlap

CATALOGUE = [
    {"code": "AV-2043", "name": "angle valve brass"},
    {"code": "WB-1100", "name": "wash basin"},
    {"code": "HF-330", "name": "health faucet"},
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
    assert token_overlap("angle valve", "VALVE angle") == 1.0
    assert token_overlap("angle valve", "angle tap") == pytest.approx(1 / 3)
    assert token_overlap("", "") == 0.0


def test_best_match_finds_the_obvious_one() -> None:
    assert best_match("brass angle valve", CATALOGUE)["code"] == "AV-2043"


def test_no_overlap_is_none_never_a_guess() -> None:
    """A wrong answer delivered confidently is worse than an honest no-match."""
    assert best_match("wiper blade", CATALOGUE) is None


def test_ties_break_alphabetically_every_time() -> None:
    """The same query must always give the same answer — determinism is a feature you build,
    not luck you have."""
    tied = [{"code": "Z-9", "name": "tap set"}, {"code": "A-1", "name": "tap set"}]
    for _ in range(3):
        assert best_match("tap", tied)["code"] == "A-1"
