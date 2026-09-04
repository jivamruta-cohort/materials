"""python · week 1 — do not edit. Every test targets a boundary the spec names."""

from __future__ import annotations

import pytest
from tasks import chunk, clamp, count_words, safe_get


def test_clamp_inside_low_high() -> None:
    assert clamp(5, 0, 10) == 5
    assert clamp(-3, 0, 10) == 0
    assert clamp(99, 0, 10) == 10


def test_clamp_ends_are_included() -> None:
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10


def test_clamp_refuses_an_inverted_range() -> None:
    with pytest.raises(ValueError):
        clamp(5, 10, 0)


def test_chunk_even_and_ragged() -> None:
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_empty_and_oversize() -> None:
    assert chunk([], 3) == []
    assert chunk([1], 5) == [[1]]


def test_chunk_refuses_size_below_one_and_keeps_input_intact() -> None:
    with pytest.raises(ValueError):
        chunk([1, 2], 0)
    items = [1, 2, 3]
    chunk(items, 2)
    assert items == [1, 2, 3]


def test_count_words_case_insensitive() -> None:
    assert count_words("The cat the DOG") == {"the": 2, "cat": 1, "dog": 1}


def test_count_words_empty_variants() -> None:
    assert count_words("") == {}
    assert count_words("   \n\t ") == {}


def test_safe_get_walks_and_defaults() -> None:
    data = {"a": {"b": {"c": 3}}}
    assert safe_get(data, "a.b.c") == 3
    assert safe_get(data, "a.b.x", 0) == 0
    assert safe_get(data, "z", "missing") == "missing"


def test_safe_get_dead_ends_on_a_non_dict() -> None:
    assert safe_get({"a": 1}, "a.b", 0) == 0  # 1 is not a dict — default, never a crash
