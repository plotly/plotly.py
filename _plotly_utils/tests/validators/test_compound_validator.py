import pytest
from _plotly_utils.basevalidators import CompoundValidator
from plotly.graph_objs.scatter import Marker


# Fixtures
# --------
@pytest.fixture()
def validator():
    return CompoundValidator('prop', 'scatter',
                             data_class_str='Marker',
                             data_docs='')


# Tests
# -----
def test_acceptance(validator: CompoundValidator):
    val = Marker(color='green', size=10)
    res = validator.validate_coerce(val)

    assert isinstance(res, Marker)
    assert res.color == 'green'
    assert res.size == 10


def test_acceptance_none(validator: CompoundValidator):
    val = None
    res = validator.validate_coerce(val)

    assert isinstance(res, Marker)
    assert res.color is None
    assert res.size is None


def test_acceptance_dict(validator: CompoundValidator):
    val = dict(color='green', size=10)
    res = validator.validate_coerce(val)

    assert isinstance(res, Marker)
    assert res.color == 'green'
    assert res.size == 10


def test_rejection_type(validator: CompoundValidator):
    val = 37

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


def test_rejection_value(validator: CompoundValidator):
    val = dict(color='green', size=10, bogus=99)

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert ("Invalid property specified for object of type "
            "plotly.graph_objs.scatter.Marker: 'bogus'" in
            str(validation_failure.value))
