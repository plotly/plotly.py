import pytest
from _plotly_utils.basevalidators import InfoArrayValidator, type_str
import numpy as np


# Fixtures
# --------
@pytest.fixture()
def validator_any2():
    return InfoArrayValidator('prop', 'parent', items=[{'valType': 'any'}, {'valType': 'any'}])


@pytest.fixture()
def validator_number3():
    return InfoArrayValidator('prop', 'parent', items=[
        {'valType': 'number', 'min': 0, 'max': 1},
        {'valType': 'number', 'min': 0, 'max': 1},
        {'valType': 'number', 'min': 0, 'max': 1}])


@pytest.fixture()
def validator_number3_free():
    return InfoArrayValidator('prop', 'parent', items=[
        {'valType': 'number', 'min': 0, 'max': 1},
        {'valType': 'number', 'min': 0, 'max': 1},
        {'valType': 'number', 'min': 0, 'max': 1}], free_length=True)


# Any2 Tests
# ----------
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    [1, 'A'], ('hello', 'world!'), [1, ()], [-1, 1]
])
def test_validator_acceptance_any2(val, validator_any2: InfoArrayValidator):
    coerce_val = validator_any2.validate_coerce(val)
    assert coerce_val == list(val)
    assert validator_any2.present(coerce_val) == tuple(val)


# ### Rejection by type ###
@pytest.mark.parametrize('val', [
    'Not a list', 123, set(), {}
])
def test_validator_rejection_any2_type(val, validator_any2: InfoArrayValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_any2.validate_coerce(val)

    assert 'must be a list or tuple.' in str(validation_failure.value)


# ### Rejection by length ###
@pytest.mark.parametrize('val', [
    [0, 1, 'A'], ('hello', 'world', '!'), [None, {}, []], [-1, 1, 9]
])
def test_validator_rejection_any2_length(val, validator_any2: InfoArrayValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_any2.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# Number3 Tests
# -------------
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    [1, 0, 0.5], (0.1, 0.4, 0.99), [1, 1, 0]
])
def test_validator_acceptance_number3(val, validator_number3: InfoArrayValidator):
    coerce_val = validator_number3.validate_coerce(val)
    assert coerce_val == list(val)
    assert validator_number3.present(coerce_val) == tuple(val)


# ### Rejection by length ###
@pytest.mark.parametrize('val', [
    [1, 0], (0.1, 0.4, 0.99, 0.4), [1]
])
def test_validator_rejection_number3_length(val, validator_number3: InfoArrayValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3.validate_coerce(val)

    assert 'must be a list or tuple of length 3.' in str(validation_failure.value)


# ### Rejection by element type ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([1, 0, '0.5'], 2),
    ((0.1, set(), 0.99), 1),
    ([[], '2', {}], 0)
])
def test_validator_rejection_number3_length(val, first_invalid_ind, validator_number3: InfoArrayValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3.validate_coerce(val)

    assert 'The prop[%d] property of parent must be a number.' % first_invalid_ind in str(validation_failure.value)


# ### Rejection by element value ###
#     Elements must be in [0, 1]
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([1, 0, 1.5], 2),
    ((0.1, -0.4, 0.99), 1),
    ([-1, 1, 0], 0)
])
def test_validator_rejection_number3_length(val, first_invalid_ind, validator_number3: InfoArrayValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3.validate_coerce(val)

    assert ('The prop[%d] property of parent must be in the range [0, 1]' % first_invalid_ind
            in str(validation_failure.value))


# Number3 Tests (free_length=True)
# --------------------------------
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    [1, 0, 0.5],
    (0.1, 0.99),
    np.array([0.1, 0.99]),
    [0], []
])
def test_validator_acceptance_number3_free(val, validator_number3_free: InfoArrayValidator):
    coerce_val = validator_number3_free.validate_coerce(val)
    assert coerce_val == list(val)
    assert validator_number3_free.present(coerce_val) == tuple(val)


# ### Rejection by type ###
@pytest.mark.parametrize('val', [
    'Not a list', 123, set(), {}
])
def test_validator_rejection_any2_type(val, validator_number3_free: InfoArrayValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3_free.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by length ###
@pytest.mark.parametrize('val', [
    (0.1, 0.4, 0.99, 0.4), [1, 0, 0, 0, 0, 0, 0]
])
def test_validator_rejection_number3_free_length(val, validator_number3_free: InfoArrayValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3_free.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by element type ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([1, 0, '0.5'], 2),
    ((0.1, set()), 1),
    ([[]], 0)
])
def test_validator_rejection_number3_length(val, first_invalid_ind, validator_number3_free: InfoArrayValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3_free.validate_coerce(val)

    assert ("Invalid value of type {typ} received for the 'prop[{first_invalid_ind}]' property of parent"
            .format(typ= type_str(val[first_invalid_ind]),
                    first_invalid_ind=first_invalid_ind)) in str(validation_failure.value)
