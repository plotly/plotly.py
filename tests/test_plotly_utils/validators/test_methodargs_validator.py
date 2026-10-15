import pytest
from _plotly_utils.basevalidators import MethodArgsValidator


# Fixtures


@pytest.fixture()
def validator():
    return MethodArgsValidator(
        "args",
        "layout.updatemenu.button",
        items=[{"valType": "any"}, {"valType": "any"}, {"valType": "any"}],
        free_length=True,
    )


# Tests


# Title strings are mapped to title.text
@pytest.mark.parametrize(
    "val,expected",
    [
        ({"title": "T"}, {"title.text": "T"}),
        ({"xaxis.title": "T"}, {"xaxis.title.text": "T"}),
        ({"yaxis2.title": 2}, {"yaxis2.title.text": 2}),
        ({"scene.xaxis.title": "T"}, {"scene.xaxis.title.text": "T"}),
        (
            {"coloraxis.colorbar.title": "T"},
            {"coloraxis.colorbar.title.text": "T"},
        ),
        ({"xaxis": {"title": "T"}}, {"xaxis": {"title": {"text": "T"}}}),
        (
            {"scene": {"xaxis": {"title": "T"}}},
            {"scene": {"xaxis": {"title": {"text": "T"}}}},
        ),
        (
            {"marker": {"colorbar": {"title": "T"}}},
            {"marker": {"colorbar": {"title": {"text": "T"}}}},
        ),
    ],
)
def test_title_strings_coerced(val, expected, validator):
    assert validator.validate_coerce([val]) == [expected]


# Already valid title values are left alone
@pytest.mark.parametrize(
    "val",
    [
        {"title.text": "T"},
        {"xaxis.title.text": "T"},
        {"title": {"text": "T"}},
        {"xaxis.title": {"text": "T", "font": {"color": "red"}}},
        {"xaxis": {"title": {"text": "T"}}},
        {"xaxis.title": None},
        {"xaxis.title.font.color": "red"},
    ],
)
def test_title_objects_unchanged(val, validator):
    assert validator.validate_coerce([val]) == [val]


# Strings for other properties are left alone
@pytest.mark.parametrize(
    "val",
    [
        [{"visible": [True, False]}, {"annotations[0].text": "T"}],
        [{"name": "title"}, {"subtitle": "T", "xaxis.titlefont": "T"}],
        [["frame1", "frame2"], {"mode": "immediate"}],
        ["title", {"title": {"text": "T"}}],
        [None, {"xaxis.range": [0, 1]}],
    ],
)
def test_other_values_unchanged(val, validator):
    assert validator.validate_coerce(val) == val


def test_title_string_in_each_arg(validator):
    assert validator.validate_coerce(
        [{"marker.colorbar.title": "A"}, {"xaxis.title": "B"}, [0]]
    ) == [{"marker.colorbar.title.text": "A"}, {"xaxis.title.text": "B"}, [0]]


def test_existing_title_text_key_not_overwritten(validator):
    val = {"xaxis.title": "A", "xaxis.title.text": "B"}
    assert validator.validate_coerce([val]) == [
        {"xaxis.title": {"text": "A"}, "xaxis.title.text": "B"}
    ]


def test_input_not_mutated(validator):
    val = [{"xaxis.title": "A", "yaxis": {"title": "B"}}]
    validator.validate_coerce(val)
    assert val == [{"xaxis.title": "A", "yaxis": {"title": "B"}}]


def test_none(validator):
    assert validator.validate_coerce(None) is None
