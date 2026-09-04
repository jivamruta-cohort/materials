"""debugging · week 2 — do not edit."""

from __future__ import annotations

import pytest
from tasks import append_tag, clone_grid, page_slice, read_scores


def test_append_tag_calls_are_independent() -> None:
    """The default list is created ONCE at definition time — unless you fix it."""
    assert append_tag("a") == ["a"]
    assert append_tag("b") == ["b"]  # fails while the default remembers 'a'


def test_append_tag_with_an_explicit_list() -> None:
    existing = ["x"]
    out = append_tag("y", existing)
    assert "y" in out and "x" in out


def test_read_scores_skips_blank_lines_only() -> None:
    assert read_scores("10\n\n20\n") == [10, 20]


def test_read_scores_raises_on_a_malformed_line_naming_it() -> None:
    """Silently dropping bad data turns a wrong total into a mystery."""
    with pytest.raises(ValueError) as e:
        read_scores("10\noops\n20")
    assert "oops" in str(e.value)


def test_page_slice_is_one_indexed() -> None:
    items = ["a", "b", "c", "d", "e"]
    assert page_slice(items, 1, 2) == ["a", "b"]
    assert page_slice(items, 2, 2) == ["c", "d"]
    assert page_slice(items, 3, 2) == ["e"]


def test_page_slice_past_the_end_and_bad_input() -> None:
    assert page_slice(["a"], 5, 2) == []
    with pytest.raises(ValueError):
        page_slice(["a"], 0, 2)


def test_clone_grid_is_truly_independent() -> None:
    grid = [[1, 2], [3, 4]]
    copy = clone_grid(grid)
    copy[0][0] = 99
    assert grid[0][0] == 1  # fails while the inner lists are shared
