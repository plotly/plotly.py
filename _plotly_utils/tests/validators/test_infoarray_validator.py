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


@pytest.fixture()
def validator_any3_free():
    return InfoArrayValidator('prop', 'parent', items=[
        {'valType': 'any'},
        {'valType': 'any'},
        {'valType': 'any'}], free_length=True)


@pytest.fixture()
def validator_number2_2d():
    return InfoArrayValidator('prop', 'parent', items=[
        {'valType': 'number', 'min': 0, 'max': 1},
        {'valType': 'number', 'min': 0, 'max': 1}],
                              free_length=True,
                              dimensions=2)


@pytest.fixture()
def validator_number2_12d():
    return InfoArrayValidator('prop', 'parent', items=[
        {'valType': 'number', 'min': 0, 'max': 1},
        {'valType': 'number', 'min': 0, 'max': 1}],
                              free_length=True,
                              dimensions='1-2')


@pytest.fixture()
def validator_number_free_1d():
    return InfoArrayValidator('prop', 'parent',
                              items={'valType': 'number',
                                     'min': 0, 'max': 1},
                              free_length=True,
                              dimensions=1)


@pytest.fixture()
def validator_number_free_2d():
    return InfoArrayValidator('prop', 'parent',
                              items={'valType': 'number',
                                     'min': 0, 'max': 1},
                              free_length=True,
                              dimensions=2)


# Any2 Tests
# ----------
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    [1, 'A'], ('hello', 'world!'), [1, set()], [-1, 1]
])
def test_validator_acceptance_any2(val, validator_any2):
    coerce_val = validator_any2.validate_coerce(val)
    assert coerce_val == list(val)
    assert validator_any2.present(coerce_val) == tuple(val)


def test_validator_acceptance_any2_none(validator_any2):
    coerce_val = validator_any2.validate_coerce(None)
    assert coerce_val is None
    assert validator_any2.present(coerce_val) is None


# ### Rejection by type ###
@pytest.mark.parametrize('val', [
    'Not a list', 123, set(), {}
])
def test_validator_rejection_any2_type(val, validator_any2):
    with pytest.raises(ValueError) as validation_failure:
        validator_any2.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by length ###
@pytest.mark.parametrize('val', [
    [0, 1, 'A'], ('hello', 'world', '!'), [None, {}, []], [-1, 1, 9]
])
def test_validator_rejection_any2_length(val, validator_any2):
    with pytest.raises(ValueError) as validation_failure:
        validator_any2.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# Number3 Tests
# -------------
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    [1, 0, 0.5], (0.1, 0.4, 0.99), [1, 1, 0]
])
def test_validator_acceptance_number3(val, validator_number3):
    coerce_val = validator_number3.validate_coerce(val)
    assert coerce_val == list(val)
    assert validator_number3.present(coerce_val) == tuple(val)


# ### Rejection by length ###
@pytest.mark.parametrize('val', [
    [1, 0], (0.1, 0.4, 0.99, 0.4), [1]
])
def test_validator_rejection_number3_length(val, validator_number3):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by element type ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([1, 0, '0.5'], 2),
    ((0.1, set(), 0.99), 1),
    ([[], '2', {}], 0)
])
def test_validator_rejection_number3_element_type(val, first_invalid_ind, validator_number3):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by element value ###
#     Elements must be in [0, 1]
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([1, 0, 1.5], 2),
    ((0.1, -0.4, 0.99), 1),
    ([-1, 1, 0], 0)
])
def test_validator_rejection_number3_element_value(val, first_invalid_ind, validator_number3):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3.validate_coerce(val)

    assert ('in the interval [0, 1]' in str(validation_failure.value))


# Number3 Tests (free_length=True)
# --------------------------------
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    [1, 0, 0.5],
    (0.1, 0.99),
    np.array([0.1, 0.99]),
    [0], []
])
def test_validator_acceptance_number3_free(val, validator_number3_free):
    coerce_val = validator_number3_free.validate_coerce(val)
    assert coerce_val == list(val)
    assert validator_number3_free.present(coerce_val) == tuple(val)


# ### Rejection by type ###
@pytest.mark.parametrize('val', [
    'Not a list', 123, set(), {}
])
def test_validator_rejection_number3_free_type(val, validator_number3_free):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3_free.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by length ###
@pytest.mark.parametrize('val', [
    (0.1, 0.4, 0.99, 0.4), [1, 0, 0, 0, 0, 0, 0]
])
def test_validator_rejection_number3_free_length(val, validator_number3_free):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3_free.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by element type ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([1, 0, '0.5'], 2),
    ((0.1, set()), 1),
    ([{}], 0)
])
def test_validator_rejection_number3_free_element_type(val, first_invalid_ind, validator_number3_free):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3_free.validate_coerce(val)

    assert ("Invalid value of type {typ} received for the 'prop[{first_invalid_ind}]' property of parent"
            .format(typ=type_str(val[first_invalid_ind]),
                    first_invalid_ind=first_invalid_ind)) in str(validation_failure.value)


# ### Rejection by element value ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([1, 0, -0.5], 2),
    ((0.1, 2), 1),
    ([99], 0)
])
def test_validator_rejection_number3_free_element_value(val, first_invalid_ind, validator_number3_free):
    with pytest.raises(ValueError) as validation_failure:
        validator_number3_free.validate_coerce(val)

    assert ("Invalid value of type {typ} received for the 'prop[{first_invalid_ind}]' property of parent"
            .format(typ=type_str(val[first_invalid_ind]),
                    first_invalid_ind=first_invalid_ind)) in str(validation_failure.value)


# Any3 Tests (free_length=True)
# --------------------------------
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    [1, 0, 'Hello'],
    (False, 0.99),
    np.array([0.1, 0.99]),
    [0], [],
    [['a', 'list']],
    [['a', 'list'], 0],
    [0, ['a', 'list'], 1],
])
def test_validator_acceptance_any3_free(val, validator_any3_free):
    coerce_val = validator_any3_free.validate_coerce(val)
    assert coerce_val == list(val)

    # Compute expected
    expected = tuple(tuple(el) if isinstance(el, list) else el for el in val)
    assert validator_any3_free.present(coerce_val) == expected


# Number2 2D
# ----------
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    [],
    [[1, 0]],
    [(0.1, 0.99)],
    np.array([[0.1, 0.99]]),
    [np.array([0.1, 0.4]), [0.2, 0], (0.9, 0.5)]
])
def test_validator_acceptance_number2_2d(val, validator_number2_2d):
    coerce_val = validator_number2_2d.validate_coerce(val)
    assert coerce_val == list((list(row) for row in val))
    expected = tuple([tuple(e) for e in val])
    assert validator_number2_2d.present(coerce_val) == expected


# ### Rejection by type ###
@pytest.mark.parametrize('val', [
    'Not a list', 123, set(), {},
])
def test_validator_rejection_number2_2d_type(val, validator_number2_2d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number2_2d.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by element type ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([[1, 0], [0.2, 0.4], 'string'], 2),
    ([[0.1, 0.7], set()], 1),
    (['bogus'], 0)
])
def test_validator_rejection_number2_2d_element_type(val, first_invalid_ind, validator_number2_2d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number2_2d.validate_coerce(val)

    assert ("Invalid value of type {typ} received for the 'prop[{first_invalid_ind}]' property of parent"
            .format(typ=type_str(val[first_invalid_ind]),
                    first_invalid_ind=first_invalid_ind)) in str(validation_failure.value)


# ### Rejection by element length ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([[1, 0], [0.2, 0.4], [0.2]], 2),
    ([[0.1, 0.7], [0, .1, .4]], 1),
    ([[]], 0)
])
def test_validator_rejection_number2_2d_element_length(val, first_invalid_ind, validator_number2_2d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number2_2d.validate_coerce(val)

    assert ("Invalid value of type {typ} received for the 'prop[{first_invalid_ind}]' property of parent"
            .format(typ=type_str(val[first_invalid_ind]),
                    first_invalid_ind=first_invalid_ind)) in str(validation_failure.value)


# ### Rejection by element value ###
@pytest.mark.parametrize('val,invalid_inds', [
    ([[1, 0], [0.2, 0.4], [0.2, 1.2]], [2, 1]),
    ([[0.1, 0.7], [-2, .1]], [1, 0]),
    ([[99, 0.3]], [0, 0])
])
def test_validator_rejection_number2_2d_element_value(val, invalid_inds, validator_number2_2d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number2_2d.validate_coerce(val)

    invalid_val = val[invalid_inds[0]][invalid_inds[1]]
    invalid_name = 'prop[{}][{}]'.format(*invalid_inds)
    assert ("Invalid value of type {typ} received for the '{invalid_name}' property of parent"
            .format(typ=type_str(invalid_val),
                    invalid_name=invalid_name)) in str(validation_failure.value)


# Number2 '1-2'
# -------------
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    [],
    [1, 0],
    (0.1, 0.99),
    np.array([0.1, 0.99])
])
def test_validator_acceptance_number2_12d_1d(val, validator_number2_12d):
    coerce_val = validator_number2_12d.validate_coerce(val)
    assert coerce_val == list(val)
    expected = tuple(val)
    assert validator_number2_12d.present(coerce_val) == expected


@pytest.mark.parametrize('val', [
    [],
    [[1, 0]],
    [(0.1, 0.99)],
    np.array([[0.1, 0.99]]),
    [np.array([0.1, 0.4]), [0.2, 0], (0.9, 0.5)]
])
def test_validator_acceptance_number2_12d_2d(val, validator_number2_12d):
    coerce_val = validator_number2_12d.validate_coerce(val)
    assert coerce_val == list((list(row) for row in val))
    expected = tuple([tuple(e) for e in val])
    assert validator_number2_12d.present(coerce_val) == expected


# ### Rejection by type / length###
@pytest.mark.parametrize('val', [
    'Not a list', 123, set(), {}, [0.1, 0.3, 0.2]
])
def test_validator_rejection_number2_12d_type(val, validator_number2_12d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number2_12d.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by element type 2D ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([[1, 0], [0.2, 0.4], 'string'], 2),
    ([[0.1, 0.7], set()], 1),
    (['bogus'], 0)
])
def test_validator_rejection_number2_12d_element_type(val, first_invalid_ind, validator_number2_12d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number2_12d.validate_coerce(val)

    assert ("Invalid value of type {typ} received for the 'prop[{first_invalid_ind}]' property of parent"
            .format(typ=type_str(val[first_invalid_ind]),
                    first_invalid_ind=first_invalid_ind)) in str(validation_failure.value)


# ### Rejection by element length ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([[1, 0], [0.2, 0.4], [0.2]], 2),
    ([[0.1, 0.7], [0, .1, .4]], 1),
    ([[]], 0)
])
def test_validator_rejection_number2_12d_element_length(val, first_invalid_ind, validator_number2_12d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number2_12d.validate_coerce(val)

    assert ("Invalid value of type {typ} received for the 'prop[{first_invalid_ind}]' property of parent"
            .format(typ=type_str(val[first_invalid_ind]),
                    first_invalid_ind=first_invalid_ind)) in str(validation_failure.value)


# ### Rejection by element value ###
@pytest.mark.parametrize('val,invalid_inds', [
    ([[1, 0], [0.2, 0.4], [0.2, 1.2]], [2, 1]),
    ([[0.1, 0.7], [-2, .1]], [1, 0]),
    ([[99, 0.3]], [0, 0]),
    ([0.1, 1.2], [1]),
    ([-0.1, 0.99], [0]),
])
def test_validator_rejection_number2_12d_element_value(val, invalid_inds, validator_number2_12d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number2_12d.validate_coerce(val)

    if len(invalid_inds) > 1:
        invalid_val = val[invalid_inds[0]][invalid_inds[1]]
        invalid_name = 'prop[{}][{}]'.format(*invalid_inds)
    else:
        invalid_val = val[invalid_inds[0]]
        invalid_name = 'prop[{}]'.format(*invalid_inds)

    assert ("Invalid value of type {typ} received for the '{invalid_name}' property of parent"
            .format(typ=type_str(invalid_val),
                    invalid_name=invalid_name)) in str(validation_failure.value)


# Number free 1D
# --------------
@pytest.mark.parametrize('val', [
    [],
    [1, 0],
    (0.1, 0.99, 0.4),
    np.array([0.1, 0.4, 0.5, 0.1, 0.6, 0.99])
])
def test_validator_acceptance_number_free_1d(val, validator_number_free_1d):
    coerce_val = validator_number_free_1d.validate_coerce(val)
    assert coerce_val == list(val)
    expected = tuple(val)
    assert validator_number_free_1d.present(coerce_val) == expected


# ### Rejection by type ###
@pytest.mark.parametrize('val', [
    'Not a list', 123, set(), {},
])
def test_validator_rejection_number_free_1d_type(val, validator_number_free_1d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number_free_1d.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by element type ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([1, 0, 0.3, 0.5, '0.5', 0.2], 4),
    ((0.1, set()), 1),
    ([{}], 0)
])
def test_validator_rejection_number_free_1d_element_type(val, first_invalid_ind, validator_number_free_1d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number_free_1d.validate_coerce(val)

    assert ("Invalid value of type {typ} received for the 'prop[{first_invalid_ind}]' property of parent"
            .format(typ=type_str(val[first_invalid_ind]),
                    first_invalid_ind=first_invalid_ind)) in str(validation_failure.value)


# ### Rejection by element value ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([1, 0, 0.3, 0.999, -0.5], 4),
    ((0.1, 2, 0.8), 1),
    ([99, 0.3], 0)
])
def test_validator_rejection_number_free_1d_element_value(val, first_invalid_ind, validator_number_free_1d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number_free_1d.validate_coerce(val)

    assert ("Invalid value of type {typ} received for the 'prop[{first_invalid_ind}]' property of parent"
            .format(typ=type_str(val[first_invalid_ind]),
                    first_invalid_ind=first_invalid_ind)) in str(validation_failure.value)


# Number free 2D
# --------------
@pytest.mark.parametrize('val', [
    [],
    [[1, 0]],
    [(0.1, 0.99)],
    np.array([[0.1, 0.99]]),
    [np.array([0.1, 0.4]), [0.2, 0], (0.9, 0.5)]
])
def test_validator_acceptance_number_free_2d(val, validator_number_free_2d):
    coerce_val = validator_number_free_2d.validate_coerce(val)
    assert coerce_val == list((list(row) for row in val))
    expected = tuple([tuple(e) for e in val])
    assert validator_number_free_2d.present(coerce_val) == expected


# ### Rejection by type ###
@pytest.mark.parametrize('val', [
    'Not a list', 123, set(), {},
])
def test_validator_rejection_number_free_2d_type(val, validator_number_free_2d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number_free_2d.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by element type ###
@pytest.mark.parametrize('val,first_invalid_ind', [
    ([[1, 0], [0.2, 0.4], 'string'], 2),
    ([[0.1, 0.7], set()], 1),
    (['bogus'], 0)
])
def test_validator_rejection_number_free_2d_element_type(val, first_invalid_ind, validator_number_free_2d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number_free_2d.validate_coerce(val)

    assert ("Invalid value of type {typ} received for the 'prop[{first_invalid_ind}]' property of parent"
            .format(typ=type_str(val[first_invalid_ind]),
                    first_invalid_ind=first_invalid_ind)) in str(validation_failure.value)


# ### Rejection by element value ###
@pytest.mark.parametrize('val,invalid_inds', [
    ([[1, 0], [0.2, 0.4], [0.2, 1.2]], [2, 1]),
    ([[0.1, 0.7], [-2, .1]], [1, 0]),
    ([[99, 0.3]], [0, 0])
])
def test_validator_rejection_number_free_2d_element_value(val, invalid_inds, validator_number_free_2d):
    with pytest.raises(ValueError) as validation_failure:
        validator_number_free_2d.validate_coerce(val)

    invalid_val = val[invalid_inds[0]][invalid_inds[1]]
    invalid_name = 'prop[{}][{}]'.format(*invalid_inds)
    assert ("Invalid value of type {typ} received for the '{invalid_name}' property of parent"
            .format(typ=type_str(invalid_val),
                    invalid_name=invalid_name)) in str(validation_failure.value)
