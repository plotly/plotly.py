import pytest
from pytest import approx

from _plotly_utils.basevalidators import NumberValidator
import numpy as np
import pandas as pd

# Fixtures
# --------
@pytest.fixture
def validator(request):
    return NumberValidator('prop', 'parent')


@pytest.fixture
def validator_min_max(request):
    return NumberValidator('prop', 'parent', min=-1.0, max=2.0)


@pytest.fixture
def validator_min(request):
    return NumberValidator('prop', 'parent', min=-1.0)


@pytest.fixture
def validator_max(request):
    return NumberValidator('prop', 'parent', max=2.0)


@pytest.fixture
def validator_aok():
    return NumberValidator('prop', 'parent', min=-1, max=1.5, array_ok=True)


# Array not ok
# ------------
# ### Acceptance ###
@pytest.mark.parametrize('val',
                         [1.0, 0.0, 1, -1234.5678, 54321, np.pi, np.nan, np.inf, -np.inf])
def test_acceptance(val, validator):
    assert validator.validate_coerce(val) == approx(val, nan_ok=True)


# ### Rejection by value ###
@pytest.mark.parametrize('val',
                         ['hello', (), [], [1, 2, 3], set(), '34'])
def test_rejection_by_value(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### With min/max ###
@pytest.mark.parametrize('val',
                         [0, 0.0, -0.5, 1, 1.0, 2, 2.0, np.pi/2.0])
def test_acceptance_min_max(val, validator_min_max):
    assert validator_min_max.validate_coerce(val) == approx(val)


@pytest.mark.parametrize('val',
                         [-1.01, -10, 2.1, 234, -np.inf, np.nan, np.inf])
def test_rejection_min_max(val, validator_min_max):
    with pytest.raises(ValueError) as validation_failure:
        validator_min_max.validate_coerce(val)

    assert 'in the interval [-1.0, 2.0]' in str(validation_failure.value)


# ### With min only ###
@pytest.mark.parametrize('val',
                         [0, 0.0, -0.5, 99999, np.inf])
def test_acceptance_min(val, validator_min):
    assert validator_min.validate_coerce(val) == approx(val)


@pytest.mark.parametrize('val',
                         [-1.01, -np.inf, np.nan])
def test_rejection_min(val, validator_min):
    with pytest.raises(ValueError) as validation_failure:
        validator_min.validate_coerce(val)

    assert 'in the interval [-1.0, inf]' in str(validation_failure.value)


# ### With max only ###
@pytest.mark.parametrize('val',
                         [0, 0.0, -np.inf, -123456, np.pi/2])
def test_acceptance_max(val, validator_max):
    assert validator_max.validate_coerce(val) == approx(val)


@pytest.mark.parametrize('val',
                         [2.01, np.inf, np.nan])
def test_rejection_max(val, validator_max):
    with pytest.raises(ValueError) as validation_failure:
        validator_max.validate_coerce(val)

    assert 'in the interval [-inf, 2.0]' in str(validation_failure.value)


# Array ok
# --------
# ### Acceptance ###
@pytest.mark.parametrize('val',
                         [1.0, 0.0, 1, 0.4])
def test_acceptance_aok_scalars(val, validator_aok):
    assert validator_aok.validate_coerce(val) == val


@pytest.mark.parametrize('val',
                         [[1.0, 0.0], [1], [-0.1234, .41, -1.0]])
def test_acceptance_aok_list(val, validator_aok):
    assert np.array_equal(validator_aok.validate_coerce(val), np.array(val, dtype='float'))


# ### Coerce ###
#     Coerced to general consistent numeric type
@pytest.mark.parametrize('val,expected',
                         [([1.0, 0], (1.0, 0)),
                          (np.array([1, -1]), np.array([1, -1])),
                          (pd.Series([1, -1]), np.array([1, -1])),
                          (pd.Index([1, -1]), np.array([1, -1])),
                          ((-0.1234, 0, -1), (-0.1234, 0.0, -1.0))])
def test_coercion_aok_list(val, expected, validator_aok):
    v = validator_aok.validate_coerce(val)
    if isinstance(val, (np.ndarray, pd.Series, pd.Index)):
        assert np.array_equal(v, expected)
    else:
        assert isinstance(v, list)
        assert validator_aok.present(v) == tuple(val)


# ### Rejection ###
#
@pytest.mark.parametrize('val',
                         [['a', 4]])
def test_rejection_aok(val, validator_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert 'Invalid element(s)' in str(validation_failure.value)


# ### Rejection by element ###
@pytest.mark.parametrize('val',
                         [[-1.6, 0.0], [1, 1.5, 2], [-0.1234, .41, np.nan],
                          [0, np.inf], [0, -np.inf]])
def test_rejection_aok_min_max(val, validator_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert 'Invalid element(s)' in str(validation_failure.value)
    assert 'in the interval [-1, 1.5]' in str(validation_failure.value)
