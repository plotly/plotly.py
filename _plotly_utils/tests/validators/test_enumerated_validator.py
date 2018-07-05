import pytest
import numpy as np
import pandas as pd
from _plotly_utils.basevalidators import EnumeratedValidator


# Fixtures
# --------
@pytest.fixture()
def validator():
    values = ['first', 'second', 'third', 4]
    return EnumeratedValidator('prop', 'parent', values, array_ok=False)


@pytest.fixture()
def validator_re():
    values = ['foo', '/bar(\d)+/', 'baz']
    return EnumeratedValidator('prop', 'parent', values, array_ok=False)


@pytest.fixture()
def validator_aok():
    values = ['first', 'second', 'third', 4]
    return EnumeratedValidator('prop', 'parent', values, array_ok=True)


@pytest.fixture()
def validator_aok_re():
    values = ['foo', '/bar(\d)+/', 'baz']
    return EnumeratedValidator('prop', 'parent', values, array_ok=True)


# Array not ok
# ------------
# ### Acceptance ###
@pytest.mark.parametrize('val',
                         ['first', 'second', 'third', 4])
def test_acceptance(val, validator):
    # Values should be accepted and returned unchanged
    assert validator.validate_coerce(val) == val


# ### Value Rejection ###
@pytest.mark.parametrize('val',
                         [True, 0, 1, 23, np.inf, set(),
                          ['first', 'second'], [True], ['third', 4], [4]])
def test_rejection_by_value(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# Array not ok, regular expression
# --------------------------------
@pytest.mark.parametrize('val',
                         ['foo', 'bar0', 'bar1', 'bar234'])
def test_acceptance(val, validator_re):
    # Values should be accepted and returned unchanged
    assert validator_re.validate_coerce(val) == val


# ### Value Rejection ###
@pytest.mark.parametrize('val',
                         [12, set(), 'bar', 'BAR0', 'FOO'])
def test_rejection_by_value(val, validator_re):
    with pytest.raises(ValueError) as validation_failure:
        validator_re.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# Array ok
# --------
# ### Acceptance ###
@pytest.mark.parametrize('val',
                         ['first', 'second', 'third', 4,
                          [], ['first', 4], [4], ['third', 'first'],
                          ['first', 'second', 'third', 4]])
def test_acceptance_aok(val, validator_aok):
    # Values should be accepted and returned unchanged
    coerce_val = validator_aok.validate_coerce(val)
    if isinstance(val, (list, np.ndarray)):
        assert np.array_equal(coerce_val, np.array(val, dtype=coerce_val.dtype))
    else:
        assert coerce_val == val


# ### Rejection by value ###
@pytest.mark.parametrize('val',
                         [True, 0, 1, 23, np.inf, set()])
def test_rejection_by_value_aok(val, validator_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Reject by elements ###
@pytest.mark.parametrize('val',
                         [[True], [0], [1, 23], [np.inf, set()],
                          ['ffirstt', 'second', 'third']])
def test_rejection_by_element_aok(val, validator_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert 'Invalid element(s)' in str(validation_failure.value)


# Array ok, regular expression
# ----------------------------
# ### Acceptance ###
@pytest.mark.parametrize('val',
                         ['foo', 'bar12', 'bar21',
                          [], ['bar12'], ('foo', 'bar012', 'baz'),
                          np.array([]),
                          np.array(['bar12']),
                          np.array(['foo', 'bar012', 'baz'])])
def test_acceptance_aok(val, validator_aok_re):
    # Values should be accepted and returned unchanged
    coerce_val = validator_aok_re.validate_coerce(val)
    if isinstance(val, (np.ndarray, pd.Series)):
        assert np.array_equal(coerce_val, np.array(val, dtype=coerce_val.dtype))
    elif isinstance(val, (list, tuple)):
        assert validator_aok_re.present(coerce_val) == tuple(val)
    else:
        assert validator_aok_re.present(coerce_val) == val


# ### Reject by elements ###
@pytest.mark.parametrize('val',
                         [['bar', 'bar0'], ['foo', 123]])
def test_rejection_by_element_aok(val, validator_aok_re):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok_re.validate_coerce(val)

    assert 'Invalid element(s)' in str(validation_failure.value)
