"""data · week 1 — do not edit."""

from __future__ import annotations

import pytest
from tasks import extract_numbers, normalize_ws, parse_kv, to_slug


def test_normalize_ws_collapses_everything() -> None:
    assert normalize_ws("  hello   world \n") == "hello world"
    assert normalize_ws("a\t\tb\nc") == "a b c"


def test_normalize_ws_whitespace_only_is_empty() -> None:
    assert normalize_ws(" \n\t ") == ""


def test_to_slug_basics() -> None:
    assert to_slug("Brake Pad (Front)") == "brake-pad-front"
    assert to_slug("BP--2043!!") == "bp-2043"


def test_to_slug_no_edge_hyphens_and_empty() -> None:
    assert to_slug("(hello)") == "hello"
    assert to_slug("") == ""
    assert to_slug("!!!") == ""


def test_parse_kv_strips_and_lowercases_key_only() -> None:
    assert parse_kv(" Size :  22 mm ") == ("size", "22 mm")


def test_parse_kv_splits_on_first_colon_only() -> None:
    assert parse_kv("note: fits: all") == ("note", "fits: all")


def test_parse_kv_refuses_bad_lines() -> None:
    with pytest.raises(ValueError):
        parse_kv("no colon here")
    with pytest.raises(ValueError):
        parse_kv(":  value with empty key")


def test_extract_numbers_in_order_with_decimals() -> None:
    assert extract_numbers("From 22mm to 25.5mm, pack of 10") == [22.0, 25.5, 10.0]


def test_extract_numbers_none_found() -> None:
    assert extract_numbers("no digits at all") == []
