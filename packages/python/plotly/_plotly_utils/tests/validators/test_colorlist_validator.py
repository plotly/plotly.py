import pytest
import numpy as np

from _plotly_utils.basevalidators import ColorlistValidator
from plotly.tests.b64 import b64

# Fixtures
# --------
@pytest.fixture()
def validator():
    return ColorlistValidator("prop", "parent")


# Rejection
# ---------
@pytest.mark.parametrize("val", [set(), 23, 0.5, {}, "redd"])
def test_rejection_value(validator, val):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


@pytest.mark.parametrize("val", [[set()], [23, 0.5], [{}, "red"], ["blue", "redd"]])
def test_rejection_element(validator, val):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


# Acceptance
# ----------
@pytest.mark.parametrize(
    "val",
    [
        ["blue"],
        ["red", "rgb(255, 0, 0)"],
        np.array(["red", "rgb(255, 0, 0)"]),
        ["hsl(0, 100%, 50%)", "hsla(0, 100%, 50%, 100%)", "hsv(0, 100%, 100%)"],
        np.array(
            ["hsl(0, 100%, 50%)", "hsla(0, 100%, 50%, 100%)", "hsv(0, 100%, 100%)"]
        ),
        ["hsva(0, 100%, 100%, 50%)"],
    ],
)
def test_acceptance_aok(val, validator):
    coerce_val = validator.validate_coerce(val)
    assert isinstance(coerce_val, list)
    assert validator.present(coerce_val) == tuple(val)

# Test that it doesn't use a base64 array
# Numpy v2 has a StrDType but we don't want to convert it yet.
# Change this test if you add support for it.
def test_acceptance_b64_aok(validator):
    val = b64(np.array(["red", "rgb(255, 0, 0)"]))
    coerce_val = validator.validate_coerce(val)
    assert coerce_val[0] == "red"
    assert coerce_val[1] == "rgb(255, 0, 0)"