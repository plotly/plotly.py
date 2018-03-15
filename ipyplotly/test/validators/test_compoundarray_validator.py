import pytest
from ipyplotly.basevalidators import CompoundArrayValidator


# Build test class
# ----------------
class CompoundType:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c


# Fixtures
# --------
@pytest.fixture()
def validator():
    return CompoundArrayValidator('prop', 'parent', element_class=CompoundType, element_docs='')


# Tests
# -----
def test_acceptance(validator: CompoundArrayValidator):
    val = [CompoundType(a=1, c=[3]), CompoundType(b='two')]
    res = validator.validate_coerce(val)

    assert isinstance(res, tuple)
    assert isinstance(res[0], CompoundType)
    assert res[0].a == 1
    assert res[0].b is None
    assert res[0].c == [3]

    assert isinstance(res[1], CompoundType)
    assert res[1].a is None
    assert res[1].b == 'two'
    assert res[1].c is None


def test_acceptance_empty(validator: CompoundArrayValidator):
    val = [{}]
    res = validator.validate_coerce(val)

    assert isinstance(res, tuple)
    assert isinstance(res[0], CompoundType)
    assert res[0].a is None
    assert res[0].b is None
    assert res[0].c is None


def test_acceptance_dict(validator: CompoundArrayValidator):
    val = [dict(a=1, c=[3]), dict(b='two')]
    res = validator.validate_coerce(val)

    assert isinstance(res, tuple)
    assert isinstance(res[0], CompoundType)
    assert res[0].a == 1
    assert res[0].b is None
    assert res[0].c == [3]

    assert isinstance(res[1], CompoundType)
    assert res[1].a is None
    assert res[1].b == 'two'
    assert res[1].c is None


def test_rejection_type(validator: CompoundArrayValidator):
    val = 37

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


def test_rejection_element(validator: CompoundArrayValidator):
    val = [{'a': 23}, 37]

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


def test_rejection_value(validator: CompoundArrayValidator):
    val = [dict(a=1, b='two', bogus=99)]

    with pytest.raises(TypeError) as validation_failure:
        validator.validate_coerce(val)

    assert "got an unexpected keyword argument 'bogus'" in str(validation_failure.value)
