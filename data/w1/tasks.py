"""data · week 1 — cleaning messy text.

WHY THIS MODULE: the project you will build answers questions over a real catalogue, and real
input is messy — stray spaces, inconsistent case, punctuation, numbers buried in prose. Retrieval
lives or dies on normalisation: two spellings of the same thing must become the same string
BEFORE anything tries to match them. This is that muscle.

HOW TO WORK: see the repository README. Done when all tests pass and your pull request is
merged after review.
"""

from __future__ import annotations


def normalize_ws(text: str) -> str:
    """Collapse every run of whitespace (spaces, tabs, newlines) to one space; strip the ends.

    '  hello   world \n' -> 'hello world' · whitespace-only -> ''.
    """
    raise NotImplementedError


def to_slug(text: str) -> str:
    """Lowercase; every run of characters that is not a letter or digit becomes ONE hyphen;
    no hyphen at either end.

    'Angle Valve (Brass)' -> 'angle-valve-brass' · '  Über-Größe!! ' -> keep it simple: anything
    non-ASCII counts as not-a-letter here -> 'ber-gr-e'. Empty in, empty out.
    """
    raise NotImplementedError


def parse_kv(line: str) -> tuple[str, str]:
    """Parse one 'key: value' line. Key is lowercased and stripped; value stripped, case kept.

    ' Size :  22 mm ' -> ('size', '22 mm'). The value may itself contain a colon:
    'note: fits: all' -> ('note', 'fits: all') — split on the FIRST colon only.
    No colon at all, or an empty key: raise ValueError.
    """
    raise NotImplementedError


def extract_numbers(text: str) -> list[float]:
    """Every number in the text, in order, as floats. Decimals count; signs do not.

    'From 22mm to 25.5mm, pack of 10' -> [22.0, 25.5, 10.0] · no numbers -> [].
    """
    raise NotImplementedError
