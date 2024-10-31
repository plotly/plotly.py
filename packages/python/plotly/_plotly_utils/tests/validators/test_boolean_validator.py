import pytest
from _plotly_utils.basevalidators import BooleanValidator
from plotly.tests.test_optional.test_utils.test_utils import np_nan

# Boolean Validator
# =================
# ### Fixtures ###
@pytest.fixture(params=[True, False])
def validator(request):
    return BooleanValidator("prop", "parent", dflt=request.param)


# ### Acceptance ###
@pytest.mark.parametrize("val", [True, False])
def test_acceptance(val, validator):
    assert val == validator.validate_coerce(val)


# ### Rejection ###
@pytest.mark.parametrize("val", [1.0, 0.0, "True", "False", [], 0, np_nan()])
def test_rejection(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)
