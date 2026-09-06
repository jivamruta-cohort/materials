"""Orientation — do not edit. Network-free; every test fails against the unsolved file."""

from __future__ import annotations

import pytest
from tasks import build_llm_request, extract_answer, parse_products, status_meaning


def test_status_meaning() -> None:
    assert status_meaning(200) == "ok"
    assert status_meaning(204) == "ok"
    assert status_meaning(401) == "client_error"
    assert status_meaning(404) == "client_error"
    assert status_meaning(503) == "server_error"
    assert status_meaning(100) == "other"


def test_parse_products_reads_the_list() -> None:
    text = '{"products": [{"code": "AV-2043", "name": "angle valve"}, {"code": "WB-1100"}]}'
    out = parse_products(text)
    assert [p["code"] for p in out] == ["AV-2043", "WB-1100"]


def test_parse_products_missing_key_is_empty() -> None:
    assert parse_products('{"count": 0}') == []


def test_parse_products_bad_json_raises() -> None:
    with pytest.raises(ValueError):
        parse_products("not json {")


def test_build_llm_request_shape() -> None:
    req = build_llm_request("answer only from the facts", "size of AV-2043?")
    assert req == {
        "messages": [
            {"role": "system", "content": "answer only from the facts"},
            {"role": "user", "content": "size of AV-2043?"},
        ]
    }


def test_extract_answer_pulls_the_content() -> None:
    resp = {"choices": [{"message": {"role": "assistant", "content": "It is 15mm."}}]}
    assert extract_answer(resp) == "It is 15mm."


def test_extract_answer_empty_reply_is_empty_string_not_a_crash() -> None:
    assert extract_answer({"choices": []}) == ""
