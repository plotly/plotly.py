import pytest
import numpy as np
import pandas as pd
from datetime import datetime
from _plotly_utils.basevalidators import (NumberValidator,
                                          IntegerValidator,
                                          DataArrayValidator,
                                          ColorValidator)


@pytest.fixture
def data_array_validator(request):
    return DataArrayValidator('prop', 'parent')


@pytest.fixture
def integer_validator(request):
    return IntegerValidator('prop', 'parent', array_ok=True)


@pytest.fixture
def number_validator(request):
    return NumberValidator('prop', 'parent', array_ok=True)


@pytest.fixture
def color_validator(request):
    return ColorValidator('prop', 'parent', array_ok=True, colorscale_path='')


@pytest.fixture(
    params=['int8', 'int16', 'int32', 'int64',
            'uint8', 'uint16', 'uint32', 'uint64',
            'float16', 'float32', 'float64'])
def numeric_dtype(request):
    return request.param


@pytest.fixture(
    params=[pd.Series, pd.Index])
def pandas_type(request):
    return request.param


@pytest.fixture
def numeric_pandas(request, pandas_type, numeric_dtype):
    return pandas_type(np.arange(10), dtype=numeric_dtype)


@pytest.fixture
def color_object_pandas(request, pandas_type):
    return pandas_type(['blue', 'green', 'red']*3, dtype='object')


@pytest.fixture
def color_categorical_pandas(request, pandas_type):
    return pandas_type(pd.Categorical(['blue', 'green', 'red']*3))


@pytest.fixture
def dates_array(request):
    return np.array([
        datetime(year=2013, month=10, day=10),
        datetime(year=2013, month=11, day=10),
        datetime(year=2013, month=12, day=10),
        datetime(year=2014, month=1, day=10),
        datetime(year=2014, month=2, day=10)
    ])


@pytest.fixture
def datetime_pandas(request, pandas_type, dates_array):
    return pandas_type(dates_array)


def test_numeric_validator_numeric_pandas(number_validator, numeric_pandas):
    res = number_validator.validate_coerce(numeric_pandas)

    # Check type
    assert isinstance(res, np.ndarray)

    # Check dtype
    assert res.dtype == numeric_pandas.dtype

    # Check values
    np.testing.assert_array_equal(res, numeric_pandas)


def test_integer_validator_numeric_pandas(integer_validator, numeric_pandas):
    res = integer_validator.validate_coerce(numeric_pandas)

    # Check type
    assert isinstance(res, np.ndarray)

    # Check dtype
    if numeric_pandas.dtype.kind in ('u', 'i'):
        # Integer and unsigned integer dtype unchanged
        assert res.dtype == numeric_pandas.dtype
    else:
        # Float datatypes converted to default integer type of int32
        assert res.dtype == 'int32'

    # Check values
    np.testing.assert_array_equal(res, numeric_pandas)


def test_data_array_validator(data_array_validator,
                              numeric_pandas):
    res = data_array_validator.validate_coerce(numeric_pandas)

    # Check type
    assert isinstance(res, np.ndarray)

    # Check dtype
    assert res.dtype == numeric_pandas.dtype

    # Check values
    np.testing.assert_array_equal(res, numeric_pandas)


def test_color_validator_numeric(color_validator,
                                 numeric_pandas):
    res = color_validator.validate_coerce(numeric_pandas)

    # Check type
    assert isinstance(res, np.ndarray)

    # Check dtype
    assert res.dtype == numeric_pandas.dtype

    # Check values
    np.testing.assert_array_equal(res, numeric_pandas)


def test_color_validator_object(color_validator,
                                color_object_pandas):

    res = color_validator.validate_coerce(color_object_pandas)

    # Check type
    assert isinstance(res, np.ndarray)

    # Check dtype
    assert res.dtype == 'object'

    # Check values
    np.testing.assert_array_equal(res, color_object_pandas)


def test_color_validator_categorical(color_validator,
                                     color_categorical_pandas):

    res = color_validator.validate_coerce(color_categorical_pandas)

    # Check type
    assert color_categorical_pandas.dtype == 'category'
    assert isinstance(res, np.ndarray)

    # Check dtype
    assert res.dtype == 'object'

    # Check values
    np.testing.assert_array_equal(res, np.array(color_categorical_pandas))


def test_data_array_validator_dates(data_array_validator,
                                    datetime_pandas,
                                    dates_array):

    res = data_array_validator.validate_coerce(datetime_pandas)

    # Check type
    assert isinstance(res, np.ndarray)

    # Check dtype
    assert res.dtype == 'object'

    # Check values
    np.testing.assert_array_equal(res, dates_array)
