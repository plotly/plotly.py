import pytest
from ipyplotly.basevalidators import DataArrayValidator
import numpy as np


# Fixtures
# --------
@pytest.fixture()
def validator():
    return DataArrayValidator('prop', 'parent')


# Tests
# -----
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    [], [1], np.array([2, 3, 4]), [''], (), ('Hello, ',  'world!')
])
def test_validator_acceptance(val, validator: DataArrayValidator):
    coerce_val = validator.validate_coerce(val)
    assert isinstance(coerce_val, np.ndarray)
    assert np.array_equal(coerce_val, val)


# ### Rejection ###
@pytest.mark.parametrize('val', [
    'Hello', 23, set(), {},
])
def test_rejection(val, validator: DataArrayValidator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)
