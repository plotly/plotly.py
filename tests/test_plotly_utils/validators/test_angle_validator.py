import pytest

# from ..basevalidators import AngleValidator
from _plotly_utils.basevalidators import AngleValidator
import numpy as np


# Fixtures
# --------
@pytest.fixture
def validator(request):
    return AngleValidator("prop", "parent")


@pytest.fixture
def validator_aok(request):
    return AngleValidator("prop", "parent", array_ok=True)


# Tests
# -----
# ### Test acceptance ###
@pytest.mark.parametrize("val", [0] + list(np.linspace(-180, 179.99)))
def test_acceptance(val, validator):
    assert validator.validate_coerce(val) == val


# ### Test coercion above 180 ###
@pytest.mark.parametrize(
    "val,expected",
    [(180, -180), (181, -179), (-180.25, 179.75), (540, -180), (-541, 179)],
)
def test_coercion(val, expected, validator):
    assert validator.validate_coerce(val) == expected


# ### Test rejection ###
@pytest.mark.parametrize("val", ["hello", (), [], [1, 2, 3], set(), "34"])
def test_rejection(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


# ### Test acceptance ###
@pytest.mark.parametrize("val", [[0, 179, -179]])
def test_aok_acceptance(val, validator_aok):
    assert validator_aok.validate_coerce(val) == val
    assert validator_aok.validate_coerce(tuple(val)) == val
    assert np.array_equal(validator_aok.validate_coerce(np.array(val)), np.array(val))


# ### Test coercion above 180 ###
@pytest.mark.parametrize(
    "val,expected",
    [(180, -180), (181, -179), (-180.25, 179.75), (540, -180), (-541, 179)],
)
def test_aok_coercion(val, expected, validator_aok):
    assert validator_aok.validate_coerce([val]) == [expected]
    assert np.array_equal(
        validator_aok.validate_coerce(np.array([val])), np.array([expected])
    )


# ### Test rejection ###
@pytest.mark.parametrize("val", [["hello"], [()], [[]], [set()], ["34"]])
def test_aok_rejection(val, validator_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)
