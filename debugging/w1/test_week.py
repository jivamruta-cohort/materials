"""debugging · week 1 — do not edit. Every test fails against the planted bug and passes
against the correct fix; a test that cannot tell them apart measures nothing."""

from __future__ import annotations

import pytest
from tasks import average, find_max, pluralize, unique_keep_order


def test_average_is_not_integer_division() -> None:
    assert average([1, 2, 4]) == pytest.approx(2.3333, abs=1e-3)


def test_average_plain_case_still_works() -> None:
    assert average([2, 4]) == 3.0


def test_find_max_survives_all_negative_numbers() -> None:
    """Starting the search at zero means zero 'wins' against every negative."""
    assert find_max([-5, -2, -9]) == -2


def test_find_max_normal_and_empty() -> None:
    assert find_max([3, 9, 1]) == 9
    with pytest.raises(ValueError):
        find_max([])


def test_unique_keeps_first_appearance_order() -> None:
    assert unique_keep_order([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_unique_on_strings_too() -> None:
    assert unique_keep_order(["b", "a", "b"]) == ["b", "a"]


def test_pluralize_only_one_is_singular() -> None:
    assert pluralize("item", 1) == "1 item"
    assert pluralize("item", 2) == "2 items"
    assert pluralize("item", 0) == "0 items"
