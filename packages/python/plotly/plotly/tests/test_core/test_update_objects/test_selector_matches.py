import pytest

import plotly.graph_objects as go
from plotly.basedatatypes import BaseFigure


def test_selector_none():
    # should return True
    assert BaseFigure._selector_matches({}, None) == True  # arbitrary,


def test_selector_empty_dict():
    # should return True
    assert (
        BaseFigure._selector_matches(dict(hello="everybody"), {}) == True  # arbitrary,
    )


def test_selector_matches_subset_of_obj():
    # should return True
    assert (
        BaseFigure._selector_matches(
            dict(hello="everybody", today="cloudy", myiq=55),
            dict(myiq=55, today="cloudy"),
        )
        == True
    )


def test_selector_has_nonmatching_key():
    # should return False
    assert (
        BaseFigure._selector_matches(
            dict(hello="everybody", today="cloudy", myiq=55),
            dict(myiq=55, cronenberg="scanners"),
        )
        == False
    )


def test_selector_has_nonmatching_value():
    # should return False
    assert (
        BaseFigure._selector_matches(
            dict(hello="everybody", today="cloudy", myiq=55),
            dict(myiq=55, today="sunny"),
        )
        == False
    )


def test_baseplotlytypes_could_match():
    # should return True
    obj = go.layout.Annotation(x=1, y=2, text="pat metheny")
    sel = go.layout.Annotation(x=1, y=2, text="pat metheny")
    assert BaseFigure._selector_matches(obj, sel) == True


def test_baseplotlytypes_could_not_match():
    # should return False
    obj = go.layout.Annotation(x=1, y=3, text="pat metheny")
    sel = go.layout.Annotation(x=1, y=2, text="pat metheny")
    assert BaseFigure._selector_matches(obj, sel) == False


def test_baseplotlytypes_cannot_match_subset():
    # should return False because "undefined" keys in sel return None, and are
    # compared (because "key in sel" returned True, it's value was None)
    obj = go.layout.Annotation(x=1, y=2, text="pat metheny")
    sel = go.layout.Annotation(x=1, y=2,)
    assert BaseFigure._selector_matches(obj, sel) == False


def test_function_selector_could_match():
    # should return True
    obj = go.layout.Annotation(x=1, y=2, text="pat metheny")

    def _sel(d):
        return d["x"] == 1 and d["y"] == 2 and d["text"] == "pat metheny"

    assert BaseFigure._selector_matches(obj, _sel) == True


def test_function_selector_could_not_match():
    # should return False
    obj = go.layout.Annotation(x=1, y=2, text="pat metheny")

    def _sel(d):
        return d["x"] == 1 and d["y"] == 3 and d["text"] == "pat metheny"

    assert BaseFigure._selector_matches(obj, _sel) == False


def test_string_selector_matches_type_key():
    assert BaseFigure._selector_matches(dict(type="bar"), "bar")
    assert BaseFigure._selector_matches(dict(type="scatter"), "bar") == False
