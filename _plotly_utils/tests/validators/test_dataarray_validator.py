import pytest
from _plotly_utils.basevalidators import DataArrayValidator
import numpy as np
import pandas as pd

# Fixtures
# --------
@pytest.fixture()
def validator():
    return DataArrayValidator('prop', 'parent')


# Tests
# -----
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    [], [1], [''], (), ('Hello, ',  'world!'), ['A', 1, 'B', 0, 'C']
])
def test_validator_acceptance_simple(val, validator):
    coerce_val = validator.validate_coerce(val)
    assert isinstance(coerce_val, list)
    assert validator.present(coerce_val) == tuple(val)


@pytest.mark.parametrize('val', [
    np.array([2, 3, 4]), pd.Series(['a', 'b', 'c']), np.array([[1, 2, 3], [4, 5, 6]])
])
def test_validator_acceptance_homogeneous(val, validator):
    coerce_val = validator.validate_coerce(val)
    assert isinstance(coerce_val, np.ndarray)
    assert np.array_equal(validator.present(coerce_val), val)


# ### Rejection ###
@pytest.mark.parametrize('val', [
    'Hello', 23, set(), {}
])
def test_rejection(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'Invalid value' in str(validation_failure.value)
