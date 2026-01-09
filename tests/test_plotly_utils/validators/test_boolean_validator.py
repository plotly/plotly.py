import pytest
from _plotly_utils.basevalidators import BooleanValidator
from ...test_optional.test_utils.test_utils import np_nan


# Boolean Validator


# Fixtures
@pytest.fixture(params=[True, False])
def validator(request):
    return BooleanValidator("prop", "parent", dflt=request.param)


@pytest.fixture(params=[True, False])
def validator_aok(request):
    return BooleanValidator("prop", "parent", dflt=request.param, array_ok=True)


# Array not ok (default)


# Acceptance
@pytest.mark.parametrize("val", [True, False])
def test_acceptance(val, validator):
    assert val == validator.validate_coerce(val)


# Rejection
@pytest.mark.parametrize("val", [1.0, 0.0, "True", "False", [], 0, np_nan()])
def test_rejection(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


# Array ok


# Acceptance
@pytest.mark.parametrize("val", [(True, False), [True, False]])
def test_acceptance_aok(val, validator_aok):
    v = validator_aok.validate_coerce(val)
    if isinstance(val, list):
        assert val == v
    else:
        assert val == tuple(v)


# Rejection
@pytest.mark.parametrize(
    "val", [(True, "Planet Express"), ["Hubert Farnsworth", False]]
)
def test_rejection_aok(val, validator_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert "Invalid elements" in str(validation_failure.value)
