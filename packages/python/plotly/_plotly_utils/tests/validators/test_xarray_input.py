import pytest
import numpy as np
import xarray
import datetime
from _plotly_utils.basevalidators import (
    NumberValidator,
    IntegerValidator,
    DataArrayValidator,
    ColorValidator,
)


@pytest.fixture
def data_array_validator(request):
    return DataArrayValidator("prop", "parent")


@pytest.fixture
def integer_validator(request):
    return IntegerValidator("prop", "parent", array_ok=True)


@pytest.fixture
def number_validator(request):
    return NumberValidator("prop", "parent", array_ok=True)


@pytest.fixture
def color_validator(request):
    return ColorValidator("prop", "parent", array_ok=True, colorscale_path="")


@pytest.fixture(
    params=[
        "int8",
        "int16",
        "int32",
        "int64",
        "uint8",
        "uint16",
        "uint32",
        "uint64",
        "float16",
        "float32",
        "float64",
    ]
)
def numeric_dtype(request):
    return request.param


@pytest.fixture(params=[xarray.DataArray])
def xarray_type(request):
    return request.param


@pytest.fixture
def numeric_xarray(request, xarray_type, numeric_dtype):
    return xarray_type(np.arange(10, dtype=numeric_dtype))


@pytest.fixture
def color_object_xarray(request, xarray_type):
    return xarray_type(["blue", "green", "red"] * 3)


def test_numeric_validator_numeric_xarray(number_validator, numeric_xarray):
    res = number_validator.validate_coerce(numeric_xarray)

    # Check type
    assert isinstance(res, np.ndarray)

    # Check dtype
    assert res.dtype == numeric_xarray.dtype

    # Check values
    np.testing.assert_array_equal(res, numeric_xarray)


def test_integer_validator_numeric_xarray(integer_validator, numeric_xarray):
    res = integer_validator.validate_coerce(numeric_xarray)

    # Check type
    assert isinstance(res, np.ndarray)

    # Check dtype
    if numeric_xarray.dtype.kind in ("u", "i"):
        # Integer and unsigned integer dtype unchanged
        assert res.dtype == numeric_xarray.dtype
    else:
        # Float datatypes converted to default integer type of int32
        assert res.dtype == "int32"

    # Check values
    np.testing.assert_array_equal(res, numeric_xarray)


def test_data_array_validator(data_array_validator, numeric_xarray):
    res = data_array_validator.validate_coerce(numeric_xarray)

    # Check type
    assert isinstance(res, np.ndarray)

    # Check dtype
    assert res.dtype == numeric_xarray.dtype

    # Check values
    np.testing.assert_array_equal(res, numeric_xarray)


def test_color_validator_numeric(color_validator, numeric_xarray):
    res = color_validator.validate_coerce(numeric_xarray)

    # Check type
    assert isinstance(res, np.ndarray)

    # Check dtype
    assert res.dtype == numeric_xarray.dtype

    # Check values
    np.testing.assert_array_equal(res, numeric_xarray)


def test_color_validator_object(color_validator, color_object_xarray):

    res = color_validator.validate_coerce(color_object_xarray)

    # Check type
    assert isinstance(res, np.ndarray)

    # Check dtype
    assert res.dtype == "object"

    # Check values
    np.testing.assert_array_equal(res, color_object_xarray)
