import pytest
from _plotly_utils.basevalidators import ColorValidator
import numpy as np


# Fixtures


@pytest.fixture()
def validator():
    return ColorValidator("prop", "parent")


@pytest.fixture()
def validator_colorscale():
    return ColorValidator("prop", "parent", colorscale_path="parent.colorscale")


@pytest.fixture()
def validator_aok():
    return ColorValidator("prop", "parent", array_ok=True)


@pytest.fixture()
def validator_aok_colorscale():
    return ColorValidator(
        "prop", "parent", array_ok=True, colorscale_path="parent.colorscale"
    )


# Array not ok, numbers not ok
@pytest.mark.parametrize(
    "val",
    [
        "red",
        "BLUE",
        "rgb(255, 0, 0)",
        "var(--accent)",
        "hsl(0, 100%, 50%)",
        "hsla(0, 100%, 50%, 100%)",
        "hsv(0, 100%, 100%)",
        "hsva(0, 100%, 100%, 50%)",
    ],
)
def test_acceptance(val, validator):
    assert validator.validate_coerce(val) == val


# Rejection by type
@pytest.mark.parametrize("val", [set(), 23, 0.5, {}, ["red"], [12]])
def test_rejection_1(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


# Rejection by value
@pytest.mark.parametrize("val", ["redd", "rgbbb(255, 0, 0)", "hsl(0, 1%0000%, 50%)"])
def test_rejection_2(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


# Array not ok, numbers ok


# Acceptance
@pytest.mark.parametrize(
    "val",
    [
        "red",
        "BLUE",
        23,
        15,
        "rgb(255, 0, 0)",
        "var(--accent)",
        "hsl(0, 100%, 50%)",
        "hsla(0, 100%, 50%, 100%)",
        "hsv(0, 100%, 100%)",
        "hsva(0, 100%, 100%, 50%)",
    ],
)
def test_acceptance_colorscale(val, validator_colorscale):
    assert validator_colorscale.validate_coerce(val) == val


# Rejection by type
@pytest.mark.parametrize("val", [set(), {}, ["red"], [12]])
def test_rejection_colorscale_1(val, validator_colorscale):
    with pytest.raises(ValueError) as validation_failure:
        validator_colorscale.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


# Rejection by value
@pytest.mark.parametrize("val", ["redd", "rgbbb(255, 0, 0)", "hsl(0, 1%0000%, 50%)"])
def test_rejection_colorscale_2(val, validator_colorscale):
    with pytest.raises(ValueError) as validation_failure:
        validator_colorscale.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


# Array ok, numbers not ok


# Acceptance
@pytest.mark.parametrize(
    "val",
    [
        "blue",
        ["red", "rgb(255, 0, 0)"],
        np.array(["red", "rgb(255, 0, 0)"]),
        ["hsl(0, 100%, 50%)", "hsla(0, 100%, 50%, 100%)", "hsv(0, 100%, 100%)"],
        np.array(
            ["hsl(0, 100%, 50%)", "hsla(0, 100%, 50%, 100%)", "hsv(0, 100%, 100%)"]
        ),
        ["hsva(0, 100%, 100%, 50%)"],
    ],
)
def test_acceptance_aok(val, validator_aok):
    coerce_val = validator_aok.validate_coerce(val)

    if isinstance(val, np.ndarray):
        assert np.array_equal(coerce_val, val)
    elif isinstance(val, list):
        assert validator_aok.present(coerce_val) == tuple(val)
    else:
        assert coerce_val == val


@pytest.mark.parametrize(
    "val",
    [
        "green",
        [["blue"]],
        [["red", "rgb(255, 0, 0)"], ["hsl(0, 100%, 50%)", "hsla(0, 100%, 50%, 100%)"]],
        np.array(
            [
                ["red", "rgb(255, 0, 0)"],
                ["hsl(0, 100%, 50%)", "hsla(0, 100%, 50%, 100%)"],
            ]
        ),
    ],
)
def test_acceptance_aok_2D(val, validator_aok):
    coerce_val = validator_aok.validate_coerce(val)

    if isinstance(val, np.ndarray):
        assert np.array_equal(coerce_val, val)
    elif isinstance(val, list):
        assert validator_aok.present(coerce_val) == tuple(val)
    else:
        assert coerce_val == val


# Rejection
@pytest.mark.parametrize(
    "val",
    [
        [23],
        [0, 1, 2],
        ["redd", "rgb(255, 0, 0)"],
        ["hsl(0, 100%, 50_00%)", "hsla(0, 100%, 50%, 100%)", "hsv(0, 100%, 100%)"],
        ["hsva(0, 1%00%, 100%, 50%)"],
    ],
)
def test_rejection_aok(val, validator_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


@pytest.mark.parametrize(
    "val",
    [
        [["redd", "rgb(255, 0, 0)"]],
        [
            ["hsl(0, 100%, 50_00%)", "hsla(0, 100%, 50%, 100%)"],
            ["hsv(0, 100%, 100%)", "purple"],
        ],
        [
            np.array(["hsl(0, 100%, 50_00%)", "hsla(0, 100%, 50%, 100%)"]),
            np.array(["hsv(0, 100%, 100%)", "purple"]),
        ],
        [["blue"], [2]],
    ],
)
def test_rejection_aok_2D(val, validator_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


# Array ok, numbers ok


# Acceptance
@pytest.mark.parametrize(
    "val",
    [
        "blue",
        23,
        [0, 1, 2],
        ["red", 0.5, "rgb(255, 0, 0)"],
        ["hsl(0, 100%, 50%)", "hsla(0, 100%, 50%, 100%)", "hsv(0, 100%, 100%)"],
        ["hsva(0, 100%, 100%, 50%)"],
    ],
)
def test_acceptance_aok_colorscale(val, validator_aok_colorscale):
    coerce_val = validator_aok_colorscale.validate_coerce(val)
    if isinstance(val, (list, np.ndarray)):
        assert np.array_equal(list(coerce_val), val)
    else:
        assert coerce_val == val


# Rejection
@pytest.mark.parametrize(
    "val",
    [
        ["redd", 0.5, "rgb(255, 0, 0)"],
        ["hsl(0, 100%, 50_00%)", "hsla(0, 100%, 50%, 100%)", "hsv(0, 100%, 100%)"],
        ["hsva(0, 1%00%, 100%, 50%)"],
    ],
)
def test_rejection_aok_colorscale(val, validator_aok_colorscale):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok_colorscale.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


# Description


# Test dynamic description logic
def test_acceptance_aok_none(validator_aok):
    """None input should pass through unchanged (typed_array_spec path)."""
    assert validator_aok.validate_coerce(None) is None


def test_acceptance_aok_typed_array_spec(validator_aok):
    """Typed array spec dict should pass through unchanged."""
    spec = {"bdata": "AQID", "dtype": "i1"}
    result = validator_aok.validate_coerce(spec)
    assert result == spec


@pytest.mark.parametrize(
    "val",
    [
        np.array(["redd", "rgb(255, 0, 0)"]),
        np.array(["bad_color"]),
    ],
)
def test_rejection_aok_numpy_1d(val, validator_aok):
    """Invalid colors in a 1D numpy array should raise."""
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


def test_rejection_aok_numpy_1d_colorscale(validator_aok_colorscale):
    """Invalid colors in a 1D numpy string array with numbers_allowed should raise."""
    val = np.array(["redd", "rgb(255, 0, 0)"])
    with pytest.raises(ValueError) as validation_failure:
        validator_aok_colorscale.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


def test_rejection_aok_nested_list_with_invalid(validator_aok):
    """Nested list with invalid colors should raise, exercising find_invalid_els."""
    val = [["redd", "rgb(255, 0, 0)"], ["blue", "not_a_color"]]
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


def test_acceptance_aok_3d_nested_list(validator_aok):
    """3-level nested list should validate, exercising recursive find_invalid_els."""
    val = [[["red", "blue"], ["green"]]]
    result = validator_aok.validate_coerce(val)
    assert validator_aok.present(result) == tuple(val)


def test_rejection_aok_3d_nested_list(validator_aok):
    """3-level nested list with invalid colors should raise."""
    val = [[["redd", "blue"], ["green"]]]
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


@pytest.mark.parametrize(
    "val",
    [
        np.array([["redd", "rgb(255, 0, 0)"], ["blue", "not_a_color"]]),
        np.array([["bad_color", "blue"]]),
    ],
)
def test_rejection_aok_numpy_2d(val, validator_aok):
    """Invalid colors in a 2D numpy array should raise."""
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


def test_acceptance_aok_colorscale_numpy_numeric(validator_aok_colorscale):
    """Numeric numpy array with numbers_allowed should pass through (numeric fast path)."""
    val = np.array([0, 1, 2, 3])
    result = validator_aok_colorscale.validate_coerce(val)
    assert np.array_equal(result, val)


def test_description(validator):
    desc = validator.description()
    assert "A number that will be interpreted as a color" not in desc
    assert "A list or array of any of the above" not in desc


def test_description_aok(validator_aok):
    desc = validator_aok.description()
    assert "A number that will be interpreted as a color" not in desc
    assert "A list or array of any of the above" in desc


def test_description_aok_colorscale(validator_aok_colorscale):
    desc = validator_aok_colorscale.description()
    assert "A number that will be interpreted as a color" in desc
    assert "A list or array of any of the above" in desc
