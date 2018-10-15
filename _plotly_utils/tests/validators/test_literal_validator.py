import pytest
from _plotly_utils.basevalidators import LiteralValidator
import numpy as np


# Fixtures
# --------
@pytest.fixture()
def validator():
    return LiteralValidator('prop', 'parent', 'scatter')


# Tests
# -----
# ### Acceptance ###
@pytest.mark.parametrize('val', ['scatter'])
def test_acceptance(val, validator):
    assert validator.validate_coerce(val) is val


# ### Test rejection ###
@pytest.mark.parametrize('val',
                         ['hello', (), [], [1, 2, 3], set(), '34'])
def test_rejection(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert 'read-only' in str(validation_failure.value)
