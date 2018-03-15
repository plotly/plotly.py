import pytest
from ipyplotly.basevalidators import BaseTracesValidator


# Build test classes
# ------------------
class Scatter:
    def __init__(self, a=None, b=None, c=None, uid=None):
        self.type = 'scatter'
        self.a = a
        self.b = b
        self.c = c
        self.uid = uid


class Bar:
    def __init__(self, a=None, b=None, c=None, uid=None):
        self.type = 'bar'
        self.a = a
        self.b = b
        self.c = c
        self.uid = uid


class Box:
    def __init__(self, a=None, b=None, c=None, uid=None):
        self.type = 'bar'
        self.a = a
        self.b = b
        self.c = c
        self.uid = uid


# Fixtures
# --------
@pytest.fixture()
def validator():
    return BaseTracesValidator(class_map={'scatter': Scatter, 'bar': Bar, 'box': Box})


# Tests
# -----
def test_acceptance(validator: BaseTracesValidator):
    val = [Scatter(a=1, c=[3]), Box(b='two')]
    res = validator.validate_coerce(val)

    assert isinstance(res, tuple)
    assert isinstance(res[0], Scatter)
    assert res[0].a == 1
    assert res[0].b is None
    assert res[0].c == [3]
    assert res[0].uid is not None

    assert isinstance(res[1], Box)
    assert res[1].a is None
    assert res[1].b == 'two'
    assert res[1].c is None
    assert res[1].uid is not None

    # Make sure UIDs are actually unique
    assert res[0].uid != res[1].uid


def test_acceptance_dict(validator: BaseTracesValidator):
    val = (dict(type='scatter', a=1, c=[3]), dict(type='box', b='two'))
    res = validator.validate_coerce(val)

    assert isinstance(res, tuple)
    assert isinstance(res[0], Scatter)
    assert res[0].a == 1
    assert res[0].b is None
    assert res[0].c == [3]
    assert res[0].uid is not None

    assert isinstance(res[1], Box)
    assert res[1].a is None
    assert res[1].b == 'two'
    assert res[1].c is None
    assert res[1].uid is not None

    # Make sure UIDs are actually unique
    assert res[0].uid != res[1].uid


def test_default_is_scatter(validator: BaseTracesValidator):
    val = [dict(a=1, c=[3])]
    res = validator.validate_coerce(val)

    assert isinstance(res, tuple)
    assert isinstance(res[0], Scatter)
    assert res[0].a == 1
    assert res[0].b is None
    assert res[0].c == [3]
    assert res[0].uid is not None


def test_uid_preserved(validator: BaseTracesValidator):
    uid1 = 'qwerty'
    uid2 = 'asdf'
    val = (dict(type='scatter', a=1, c=[3], uid=uid1), dict(type='box', b='two', uid=uid2))
    res = validator.validate_coerce(val)

    assert isinstance(res, tuple)
    assert isinstance(res[0], Scatter)
    assert res[0].a == 1
    assert res[0].b is None
    assert res[0].c == [3]
    assert res[0].uid == uid1

    assert isinstance(res[1], Box)
    assert res[1].a is None
    assert res[1].b == 'two'
    assert res[1].c is None
    assert res[1].uid == uid2


def test_rejection_type(validator: BaseTracesValidator):
    val = 37

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


def test_rejection_element_type(validator: BaseTracesValidator):
    val = [42]

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


def test_rejection_element_attr(validator: BaseTracesValidator):
    val = [dict(type='scatter', bogus=99)]

    with pytest.raises(TypeError) as validation_failure:
        validator.validate_coerce(val)

    assert "got an unexpected keyword argument 'bogus'" in str(validation_failure.value)


def test_rejection_element_tracetype(validator: BaseTracesValidator):
    val = [dict(type='bogus', a=4)]

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)
