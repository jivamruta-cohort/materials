"""Orientation — APIs & LLMs, the basics. The only file you edit.

Four network-free functions that teach the shapes you'll use in week 3, on building-materials
examples. Fill in the ones that raise NotImplementedError. See README.md for the concepts.
"""

from __future__ import annotations

import json  # noqa: F401 — you'll want this


def status_meaning(code: int) -> str:
    """Classify an HTTP status code. Your code must branch on these, not assume success.

    200-299 -> 'ok' · 400-499 -> 'client_error' (you did something wrong) ·
    500-599 -> 'server_error' (their side broke) · anything else -> 'other'.
    """
    raise NotImplementedError


def parse_products(json_text: str) -> list[dict]:
    """A product API returns a JSON object like {"products": [ {...}, {...} ]}.
    Return just the list of product dicts. If the text is not valid JSON, raise ValueError.
    Missing "products" key -> return [].
    """
    raise NotImplementedError


def build_llm_request(system: str, user: str) -> dict:
    """Build the payload an LLM gateway expects: a messages list, system first, then user.

    Returns exactly:
      {"messages": [{"role": "system", "content": <system>},
                    {"role": "user",   "content": <user>}]}
    This is the shape of every model call in the project.
    """
    raise NotImplementedError


def extract_answer(response_json: dict) -> str:
    """Pull the reply text out of an LLM response shaped like:
      {"choices": [{"message": {"role": "assistant", "content": "the answer"}}]}
    Return the content string. If there are no choices, return '' (never crash on an empty reply).
    """
    raise NotImplementedError
