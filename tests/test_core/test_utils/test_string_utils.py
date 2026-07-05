"""Unit tests for the pure string helpers in ``_plotly_utils.utils``.

These functions back error messages that point at the offending part of a
property path (split the path, find character positions, mark them, and
suggest the closest valid key). They had no direct test coverage.
"""

from _plotly_utils.utils import (
    _natural_sort_strings,
    chomp_empty_strings,
    display_string_positions,
    find_closest_string,
    levenshtein,
    split_multichar,
    split_string_positions,
)

SAMPLE = "a.string[0].with_separators"
SEPARATORS = ".[]_"


def test_split_multichar_splits_on_every_char():
    assert split_multichar([SAMPLE], list(SEPARATORS)) == [
        "a",
        "string",
        "0",
        "",
        "with",
        "separators",
    ]


def test_split_multichar_no_chars_returns_input():
    assert split_multichar([SAMPLE], []) == [SAMPLE]


def test_split_string_positions():
    parts = split_multichar([SAMPLE], list(SEPARATORS))
    assert split_string_positions(parts) == [0, 2, 9, 11, 12, 17]


def test_display_string_positions_single_index():
    pos = split_string_positions(split_multichar([SAMPLE], list(SEPARATORS)))
    assert display_string_positions(pos, 4) == "            ^"


def test_display_string_positions_offset_length_char_no_trim():
    pos = split_string_positions(split_multichar([SAMPLE], list(SEPARATORS)))
    assert (
        display_string_positions(pos, 4, offset=1, length=3, char="~", trim=False)
        == "             ~~~      "
    )


def test_display_string_positions_all_indices():
    pos = split_string_positions(split_multichar([SAMPLE], list(SEPARATORS)))
    assert display_string_positions(pos) == "^ ^      ^ ^^    ^"


def test_chomp_empty_strings_basic():
    assert chomp_empty_strings(["hey", "", "why", "", "", "whoa", "", ""], "_") == [
        "hey_",
        "why__",
        "whoa__",
    ]


def test_chomp_empty_strings_leading_empty():
    assert chomp_empty_strings(["", "hi", "", "I'm", "bob", "", ""], "_") == [
        "_",
        "hi_",
        "I'm",
        "bob__",
    ]


def test_chomp_empty_strings_no_empties_unchanged():
    strings = ["hi", "i'm", "a", "good", "string"]
    assert chomp_empty_strings(strings, "_") == strings


def test_chomp_empty_strings_special_cases():
    assert chomp_empty_strings([], "_") == []
    assert chomp_empty_strings([""], "_") == [""]
    assert chomp_empty_strings(["", ""], "_") == ["_"]
    assert chomp_empty_strings(["", "", "", ""], "_") == ["___"]


def test_chomp_empty_strings_reverse():
    # In reverse, an empty string attaches to the neighbor on its right.
    assert chomp_empty_strings(["hey", "", "why"], "_", reverse=True) == [
        "hey",
        "_why",
    ]


def test_levenshtein():
    assert levenshtein("kitten", "sitting") == 3
    assert levenshtein("flaw", "lawn") == 2
    assert levenshtein("abc", "abc") == 0
    assert levenshtein("", "abc") == 3
    # symmetric
    assert levenshtein("abc", "") == levenshtein("", "abc")


def test_find_closest_string():
    assert find_closest_string("helo", ["hello", "world", "help"]) == "hello"


def test_find_closest_string_ties_break_lexicographically():
    # "ax" and "ay" are both distance 1 from "aa"; the lexicographically
    # smaller one wins for a stable result.
    assert find_closest_string("aa", ["ay", "ax"]) == "ax"


def test_natural_sort_strings():
    assert _natural_sort_strings(["a10", "a2", "a1", "a10b"]) == [
        "a1",
        "a2",
        "a10",
        "a10b",
    ]
    assert _natural_sort_strings(["a1", "a2", "a10"], reverse=True) == [
        "a10",
        "a2",
        "a1",
    ]
