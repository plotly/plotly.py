import pytest
from ipyplotly.basevalidators import AnyValidator
import numpy as np


# Fixtures
# --------
@pytest.fixture()
def validator():
    return AnyValidator('prop', 'parent')


@pytest.fixture()
def validator_aok():
    return AnyValidator('prop', 'parent', array_ok=True)

# Tests
# -----
# ### Acceptance ###
@pytest.mark.parametrize('val', [
    set(), 'Hello', 123, np.inf, np.nan, {}
])
def test_acceptance(val, validator: AnyValidator):
    assert validator.validate_coerce(val) is val


# ### Acceptance of arrays ###
@pytest.mark.parametrize('val', [
    [], np.array([]), ['Hello', 'World'], [np.pi, np.e, {}]
])
def test_acceptance_array(val, validator_aok: AnyValidator):
    coerce_val = validator_aok.validate_coerce(val)
    assert isinstance(coerce_val, np.ndarray)
    assert coerce_val.dtype == 'object'
    assert np.array_equal(coerce_val, val)
