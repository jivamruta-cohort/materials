"""python · week 2 — do not edit."""

from __future__ import annotations

import pytest
from tasks import InsufficientStock, Inventory, group_by, merge_settings, parse_int_or


def test_group_by_groups_and_preserves_order() -> None:
    rows = [{"t": "a", "v": 1}, {"t": "b", "v": 2}, {"t": "a", "v": 3}]
    out = group_by(rows, "t")
    assert [r["v"] for r in out["a"]] == [1, 3]
    assert [r["v"] for r in out["b"]] == [2]


def test_group_by_missing_key_goes_under_none_and_input_survives() -> None:
    rows = [{"v": 1}, {"t": "a", "v": 2}]
    out = group_by(rows, "t")
    assert [r["v"] for r in out[None]] == [1]
    assert rows == [{"v": 1}, {"t": "a", "v": 2}]


def test_merge_settings_recursive_override() -> None:
    assert merge_settings({"a": 1, "n": {"x": 1, "y": 2}}, {"n": {"y": 9}}) == {
        "a": 1, "n": {"x": 1, "y": 9}
    }


def test_merge_settings_non_dict_replaces_and_nothing_mutates() -> None:
    d, o = {"n": {"x": 1}}, {"n": 5}
    assert merge_settings(d, o) == {"n": 5}
    assert d == {"n": {"x": 1}} and o == {"n": 5}


def test_parse_int_or_variants() -> None:
    assert parse_int_or(" 42 ", 0) == 42
    assert parse_int_or("4,200", 0) == 4200
    assert parse_int_or("x", 7) == 7
    assert parse_int_or("", 7) == 7


def test_inventory_add_remove_total() -> None:
    inv = Inventory()
    inv.add("BP-2043", 5)
    inv.add("BP-2043", 3)
    inv.add("GF-101", 2)
    inv.remove("BP-2043", 6)
    assert inv.total() == 4


def test_inventory_refuses_bad_add() -> None:
    inv = Inventory()
    with pytest.raises(ValueError):
        inv.add("X", 0)


def test_failed_removal_changes_nothing() -> None:
    """The half-happened operation is the bug that costs real money later."""
    inv = Inventory()
    inv.add("A", 3)
    with pytest.raises(InsufficientStock):
        inv.remove("A", 5)
    with pytest.raises(InsufficientStock):
        inv.remove("UNKNOWN", 1)
    assert inv.total() == 3
