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


VALID_COLORS = [
    "red",
    "BLUE",
    "#8574b2",
    "#8574B2",
    "#8574b2cc",
    "#8574B2CC",
    "#87b",
    "#87B",
    "#87bc",
    "#87BC",
    "rgb(248, 12, 0)",
    "rgb(248 12 0)",
    "rgba(248, 12, 0, 0.5)",
    "rgba(248 12 0 / 0.5)",
    "var(--accent)",
    "hsl(0, 100%, 50%)",
    "hsl(0 100% 50%)",
    "hsl(0deg 100% 50%)",
    "hsla(0, 100%, 50%, 100%)",
    "hsla(0 100% 50% 100%)",
    "hsla(0deg 100% 50% 100%)",
    "hwb(0 100% 50%)",
    "hwb(0 100% 50% 0.5)",
    "oklch(0.7 0.15 180)",
    "oklab(0.7 0.15 0.5)",
    "lab(70 15 50)",
    "lch(70 15 180)",
    "color(display-p3 1 0 0)",
]

INVALID_COLORS_WRONG_TYPE = [
    set(),
    {},
    ["red"],
    [12],
]

INVALID_COLORS_WRONG_FORMAT = [
    "redd",
    "rgbbb(255, 0, 0)",
    "hsl(0, 1%0000%, 50%)",
    "hsv(0, 100%, 100%)",
    "hsva(0, 100%, 100%, 50%)",
]


# Array not ok, numbers not ok
@pytest.mark.parametrize("val", VALID_COLORS)
def test_acceptance(val, validator):
    assert validator.validate_coerce(val) == val


# Rejection by type
@pytest.mark.parametrize("val", INVALID_COLORS_WRONG_TYPE + [23, 0.5])
def test_rejection_1(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


# Rejection by value
@pytest.mark.parametrize("val", INVALID_COLORS_WRONG_FORMAT)
def test_rejection_2(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


# Array not ok, numbers ok


# Acceptance
@pytest.mark.parametrize("val", VALID_COLORS + [23, 15])
def test_acceptance_colorscale(val, validator_colorscale):
    assert validator_colorscale.validate_coerce(val) == val


# Rejection by type
@pytest.mark.parametrize("val", INVALID_COLORS_WRONG_TYPE)
def test_rejection_colorscale_1(val, validator_colorscale):
    with pytest.raises(ValueError) as validation_failure:
        validator_colorscale.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


# Rejection by value
@pytest.mark.parametrize("val", INVALID_COLORS_WRONG_FORMAT)
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
        ["hsl(0, 100%, 50%)", "hsla(0, 100%, 50%, 100%)", "hsl(0, 100%, 100%)"],
        np.array(
            ["hsl(0, 100%, 50%)", "hsla(0, 100%, 50%, 100%)", "hsl(0, 100%, 100%)"]
        ),
        ["hsla(0, 100%, 100%, 50%)"],
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
        ["hsl(0, 100%, 50_00%)", "hsla(0, 100%, 50%, 100%)", "hsl(0, 100%, 100%)"],
        ["hsla(0, 1%00%, 100%, 50%)"],
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
            ["hsl(0, 100%, 100%)", "purple"],
        ],
        [
            np.array(["hsl(0, 100%, 50_00%)", "hsla(0, 100%, 50%, 100%)"]),
            np.array(["hsl(0, 100%, 100%)", "purple"]),
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
        ["hsl(0, 100%, 50%)", "hsla(0, 100%, 50%, 100%)", "hsl(0, 100%, 100%)"],
        ["hsla(0, 100%, 100%, 50%)"],
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
        ["hsl(0, 100%, 50_00%)", "hsla(0, 100%, 50%, 100%)", "hsl(0, 100%, 100%)"],
        ["hsla(0, 1%00%, 100%, 50%)"],
    ],
)
def test_rejection_aok_colorscale(val, validator_aok_colorscale):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok_colorscale.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


# Description


# Test dynamic description logic
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
