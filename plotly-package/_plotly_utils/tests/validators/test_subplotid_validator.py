import pytest
from _plotly_utils.basevalidators import SubplotidValidator
import numpy as np


# Fixtures
# --------
@pytest.fixture()
def validator():
    return SubplotidValidator('prop', 'parent', dflt='geo')


# Tests
# -----
# ### Acceptance ###
@pytest.mark.parametrize('val', ['geo'] + ['geo%d' % i for i in range(2, 10)])
def test_acceptance(val, validator):
    assert validator.validate_coerce(val) == val


# ### Rejection by type ###
@pytest.mark.parametrize('val', [
    23, [], {}, set(), np.inf, np.nan
])
def test_rejection_type(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)


# ### Rejection by value ###
@pytest.mark.parametrize('val', [
    '',  # Cannot be empty
    'bogus',  # Must begin with 'geo'
    'geo0',  # If followed by a number the number must be > 1
])
def test_rejection_value(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)
