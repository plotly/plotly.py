# Array not ok
# ------------
import pytest
from pytest import approx
from ipyplotly.basevalidators import IntegerValidator
import numpy as np


# ### Fixtures ###
@pytest.fixture()
def validator():
    return IntegerValidator('prop', 'parent')


@pytest.fixture
def validator_min_max():
    return IntegerValidator('prop', 'parent', min=-1, max=2)


@pytest.fixture
def validator_min():
    return IntegerValidator('prop', 'parent', min=-1)


@pytest.fixture
def validator_max():
    return IntegerValidator('prop', 'parent', max=2)


@pytest.fixture
def validator_aok(request):
    return IntegerValidator('prop', 'parent', min=-2, max=10, array_ok=True)


# ### Acceptance ###
@pytest.mark.parametrize('val',
                         [1, -19, 0, -1234])
def test_acceptance(val, validator: IntegerValidator):
    assert validator.validate_coerce(val) == val


# ### Coercion ###
@pytest.mark.parametrize('val,expected',
                         [(1.0, 1), (-19.1, -19), (0.001, 0), (1234.9, 1234)])
def test_coercion(val, expected, validator: IntegerValidator):
    assert validator.validate_coerce(val) == expected


# ### Rejection by value ###
@pytest.mark.parametrize('val',
                         ['hello', (), [], [1, 2, 3], set(), '34', np.nan, np.inf, -np.inf])
def test_rejection_by_value(val, validator: IntegerValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### With min/max ###
#  min == -1 and max == 2
@pytest.mark.parametrize('val',
                         [0, 1, -1, 2])
def test_acceptance_min_max(val, validator_min_max: IntegerValidator):
    assert validator_min_max.validate_coerce(val) == approx(val)


@pytest.mark.parametrize('val',
                         [-1.01, -10, 2.1, 3, np.iinfo(np.int).max, np.iinfo(np.int).min])
def test_rejection_min_max(val, validator_min_max: IntegerValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_min_max.validate_coerce(val)

    assert 'in the interval [-1, 2]' in str(validation_failure.value)


# ### With min only ###
#  min == -1
@pytest.mark.parametrize('val',
                         [-1, 0, 1, 23, 99999])
def test_acceptance_min(val, validator_min: IntegerValidator):
    assert validator_min.validate_coerce(val) == approx(val)


@pytest.mark.parametrize('val',
                         [-2, -123, np.iinfo(np.int).min])
def test_rejection_min(val, validator_min: IntegerValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_min.validate_coerce(val)

    assert 'in the interval [-1, 2147483647]' in str(validation_failure.value)


# ### With max only ###
#  max == 2
@pytest.mark.parametrize('val',
                         [1, 2, -10, -999999, np.iinfo(np.int32).min])
def test_acceptance_max(val, validator_max: IntegerValidator):
    assert validator_max.validate_coerce(val) == approx(val)


@pytest.mark.parametrize('val',
                         [3, 10, np.iinfo(np.int32).max])
def test_rejection_max(val, validator_max: IntegerValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_max.validate_coerce(val)

    assert 'in the interval [-2147483648, 2]' in str(validation_failure.value)


# Array ok
# --------
# min=-2 and max=10
# ### Acceptance ###
@pytest.mark.parametrize('val',
                         [-2, 1, 0, 1, 10])
def test_acceptance_aok_scalars(val, validator_aok: IntegerValidator):
    assert validator_aok.validate_coerce(val) == val


@pytest.mark.parametrize('val',
                         [[1, 0], [1], [-2, 1, 8], np.array([3, 2, -1, 5])])
def test_acceptance_aok_list(val, validator_aok: IntegerValidator):
    assert np.array_equal(validator_aok.validate_coerce(val), val)


# ### Coerce ###
#     Coerced to general consistent numeric type
@pytest.mark.parametrize('val,expected',
                         [([1.0, 0], [1, 0]),
                          (np.array([1.1, -1]), [1, -1]),
                          ([-1.9, 0, 5.1], [-1, 0, 5]),
                          (np.array([1, 0], dtype=np.int64), [1, 0])])
def test_coercion_aok_list(val, expected, validator_aok: IntegerValidator):
    v = validator_aok.validate_coerce(val)
    assert v.dtype == np.int32
    assert np.array_equal(v, np.array(expected, dtype=np.int32))


# ### Rejection ###
#
@pytest.mark.parametrize('val',
                         [['a', 4], [[], 3, 4]])
def test_integer_validator_rejection_aok(val, validator_aok: IntegerValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by element ###
@pytest.mark.parametrize('val',
                         [[-1, 11], [1.5, -3], [0, np.iinfo(np.int32).max], [0, np.iinfo(np.int32).min]])
def test_rejection_aok_min_max(val, validator_aok: IntegerValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert 'in the interval [-2, 10]' in str(validation_failure.value)
