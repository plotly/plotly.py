import pytest
from ipyplotly.basevalidators import CompoundValidator


# Build test class
# ----------------
class CompoundType:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
        self._props = {'a': a, 'b': b, 'c': c}


# Fixtures
# --------
@pytest.fixture()
def validator():
    return CompoundValidator('prop', 'parent', data_class=CompoundType, data_docs='')


# Tests
# -----
def test_acceptance(validator: CompoundValidator):
    val = CompoundType(a=1, c=[3])
    res = validator.validate_coerce(val)

    assert isinstance(res, CompoundType)
    assert res.a == 1
    assert res.b is None
    assert res.c == [3]


def test_acceptance_none(validator: CompoundValidator):
    val = None
    res = validator.validate_coerce(val)

    assert isinstance(res, CompoundType)
    assert res.a is None
    assert res.b is None
    assert res.c is None


def test_acceptance_dict(validator: CompoundValidator):
    val = dict(a=1, b='two')
    res = validator.validate_coerce(val)

    assert isinstance(res, CompoundType)
    assert res.a == 1
    assert res.b == 'two'
    assert res.c is None


def test_rejection_type(validator: CompoundValidator):
    val = 37

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


def test_rejection_value(validator: CompoundValidator):
    val = dict(a=1, b='two', bogus=99)

    with pytest.raises(TypeError) as validation_failure:
        validator.validate_coerce(val)

    assert "got an unexpected keyword argument 'bogus'" in str(validation_failure.value)
