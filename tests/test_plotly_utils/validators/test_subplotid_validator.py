import pytest
from _plotly_utils.basevalidators import SubplotidValidator
from ...test_optional.test_utils.test_utils import np_nan, np_inf


# Fixtures


@pytest.fixture()
def validator():
    return SubplotidValidator("prop", "parent", dflt="geo")


@pytest.fixture()
def validator_aok():
    return SubplotidValidator("prop", "parent", dflt="legend", array_ok=True)


# Tests

# Array not ok (default)

# Acceptance


@pytest.mark.parametrize("val", ["geo"] + ["geo%d" % i for i in range(2, 10)])
def test_acceptance(val, validator):
    assert validator.validate_coerce(val) == val


# Coercion from {base}1 to {base}
def test_coerce(validator):
    v = validator.validate_coerce("geo1")
    assert ("geo") == v


# Rejection by type
@pytest.mark.parametrize("val", [23, [], {}, set(), np_inf(), np_nan()])
def test_rejection_type(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


# Rejection by value
@pytest.mark.parametrize(
    "val",
    [
        "",  # Cannot be empty
        "bogus",  # Must begin with 'geo'
        "geo0",  # If followed by a number the number must be > 1
    ],
)
def test_rejection_value(val, validator):
    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


# Array ok

# Acceptance


@pytest.mark.parametrize(
    "val",
    ["legend2", ["legend", "legend2"], ["legend", "legend2"]],
)
def test_acceptance_aok(val, validator_aok):
    v = validator_aok.validate_coerce(val)
    if isinstance(val, tuple):
        assert val == tuple(v)
    else:
        assert val == v


# Coercion from {base}1 to {base}
def test_coerce_aok(validator_aok):
    v = validator_aok.validate_coerce(("legend1", "legend2"))
    assert ("legend", "legend2") == tuple(v)


# Rejection by type
@pytest.mark.parametrize("val", [23, [2, 3], {}, set(), np_inf(), np_nan()])
def test_rejection_type_aok(val, validator_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    failure_msg = str(validation_failure.value)
    assert "Invalid value" in failure_msg or "Invalid elements" in failure_msg


# Rejection by value
@pytest.mark.parametrize(
    "val",
    [
        "",  # Cannot be empty
        "bogus",  # Must begin with 'geo'
        "legend0",  # If followed by a number the number must be > 1,
        ["", "legend"],
        ("bogus", "legend2"),
    ],
)
def test_rejection_value_aok(val, validator_aok):
    with pytest.raises(ValueError) as validation_failure:
        validator_aok.validate_coerce(val)

    failure_msg = str(validation_failure.value)
    assert "Invalid value" in failure_msg or "Invalid elements" in failure_msg
