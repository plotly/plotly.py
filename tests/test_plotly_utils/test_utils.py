"""
Tests for the pure string and utility helpers in _plotly_utils.utils.

These functions have no external dependencies and back the "did you mean"
suggestions and path-parsing used in validator error messages. The expected
values below were taken from the function docstrings and confirmed against the
actual output.
"""

import pytest

from _plotly_utils.utils import (
    chomp_empty_strings,
    display_string_positions,
    find_closest_string,
    is_skipped_key,
    levenshtein,
    split_multichar,
    split_string_positions,
    _natural_sort_strings,
)


@pytest.mark.parametrize(
    "s1,s2,expected",
    [
        ("kitten", "sitting", 3),
        ("", "abc", 3),
        ("abc", "", 3),
        ("abc", "abc", 0),
        ("flaw", "lawn", 2),
    ],
)
def test_levenshtein_distance(s1, s2, expected):
    assert levenshtein(s1, s2) == expected


def test_levenshtein_is_symmetric():
    assert levenshtein("kitten", "sitting") == levenshtein("sitting", "kitten")


def test_find_closest_string_exact_match():
    assert find_closest_string("range", ["rang", "range", "orange"]) == "range"


def test_find_closest_string_picks_nearest():
    assert find_closest_string("colour", ["color", "colored", "scale"]) == "color"


def test_find_closest_string_ties_break_lexicographically():
    # "ac" and "ad" are both distance 1 from "ab"; the lexicographically
    # smaller one wins regardless of input order.
    assert find_closest_string("ab", ["ad", "ac", "xy"]) == "ac"


def test_split_multichar_splits_on_every_char():
    ss = ["a.string[0].with_separators"]
    assert split_multichar(ss, list(".[]_")) == [
        "a",
        "string",
        "0",
        "",
        "with",
        "separators",
    ]


def test_split_multichar_no_chars_returns_input():
    assert split_multichar(["abc"], []) == ["abc"]


def test_split_string_positions():
    ss = split_multichar(["a.string[0].with_separators"], list(".[]_"))
    assert split_string_positions(ss) == [0, 2, 9, 11, 12, 17]


def test_display_string_positions_single_index():
    p = [0, 2, 9, 11, 12, 17]
    assert display_string_positions(p, 4) == "            ^"


def test_display_string_positions_offset_length_char_no_trim():
    p = [0, 2, 9, 11, 12, 17]
    assert (
        display_string_positions(p, 4, offset=1, length=3, char="~", trim=False)
        == "             ~~~      "
    )


def test_display_string_positions_all_indices():
    p = [0, 2, 9, 11, 12, 17]
    assert display_string_positions(p) == "^ ^      ^ ^^    ^"


@pytest.mark.parametrize(
    "strings,expected",
    [
        ([], []),
        ([""], [""]),
        (["", ""], ["_"]),
        (["", "", "", ""], ["___"]),
        (["hey", "", "why", "", "", "whoa", "", ""], ["hey_", "why__", "whoa__"]),
        (["", "hi", "", "I'm", "bob", "", ""], ["_", "hi_", "I'm", "bob__"]),
        (["hi", "i'm", "a", "good", "string"], ["hi", "i'm", "a", "good", "string"]),
    ],
)
def test_chomp_empty_strings(strings, expected):
    assert chomp_empty_strings(strings, "_") == expected


def test_chomp_empty_strings_reverse():
    strings = ["", "hi", "", "I'm", "bob", "", ""]
    assert chomp_empty_strings(strings, "_", reverse=True) == [
        "_hi",
        "_I'm",
        "bob",
        "__",
    ]


@pytest.mark.parametrize("key", ["geojson", "layer", "layers", "range"])
def test_is_skipped_key_true(key):
    assert is_skipped_key(key) is True


@pytest.mark.parametrize("key", ["x", "y", "geo", "Range", ""])
def test_is_skipped_key_false(key):
    assert is_skipped_key(key) is False


def test_natural_sort_strings_orders_numbers_naturally():
    assert _natural_sort_strings(["x10", "x2", "x1"]) == ["x1", "x2", "x10"]


def test_natural_sort_strings_reverse():
    assert _natural_sort_strings(["x10", "x2", "x1"], reverse=True) == [
        "x10",
        "x2",
        "x1",
    ]
