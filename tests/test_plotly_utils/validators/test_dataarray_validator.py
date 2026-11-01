import pytest
from _plotly_utils.basevalidators import DataArrayValidator
import numpy as np
import pandas as pd


# Fixtures
@pytest.fixture()
def validator():
    return DataArrayValidator("prop", "parent")


# Tests


# Acceptance
@pytest.mark.parametrize(
    "val",
    [
        [],
        [1],
        [""],
        (),
        ("Hello, ", "world!"),
        ["A", 1, "B", 0, "C"],
        [np.array(1), np.array(2)],
    ],
)
def test_validator_acceptance_simple(val, validator):
    coerce_val = validator.validate_coerce(val)
    assert isinstance(coerce_val, list)
    assert validator.present(coerce_val) == tuple(val)


@pytest.mark.parametrize(
    "val",
    [np.array([2, 3, 4]), pd.Series(["a", "b", "c"]), np.array([[1, 2, 3], [4, 5, 6]])],
)
def test_validator_acceptance_homogeneous(val, validator):
    coerce_val = validator.validate_coerce(val)
    assert isinstance(coerce_val, np.ndarray)
    assert np.array_equal(validator.present(coerce_val), val)


@pytest.mark.parametrize(
    "val,expected",
    [
        (np.ma.array([1, 2, 3], mask=[0, 1, 0]), np.array([1, np.nan, 3])),
        (
            np.ma.array([1, 2, 3], mask=[0, 1, 0], dtype="float32"),
            np.array([1, np.nan, 3], dtype="float32"),
        ),
        (np.ma.array([1, 2, 3], mask=True), np.array([np.nan, np.nan, np.nan])),
        (np.ma.array([1, 2, 3], mask=False), np.array([1, 2, 3])),
        (
            np.ma.array([[1, 2], [3, 4]], mask=[[0, 1], [0, 0]]),
            np.array([[1, np.nan], [3, 4]]),
        ),
        (
            np.ma.array(["a", "b", "c"], mask=[0, 1, 0]),
            np.array(["a", None, "c"], dtype="object"),
        ),
        (
            np.ma.array([True, False, True], mask=[0, 1, 0]),
            np.array([True, None, True], dtype="object"),
        ),
    ],
)
def test_validator_acceptance_masked(val, expected, validator):
    coerce_val = validator.validate_coerce(val)
    assert not np.ma.isMaskedArray(coerce_val)
    assert coerce_val.dtype == expected.dtype
    np.testing.assert_array_equal(coerce_val, expected)


# Rejection
@pytest.mark.parametrize("val", ["Hello", 23, set(), {}])
def test_rejection(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)
