import pytest
from _plotly_utils.basevalidators import BaseDataValidator
from plotly.graph_objs import Scatter, Bar, Box

# Fixtures
# --------
@pytest.fixture()
def validator():
    return BaseDataValidator(class_strs_map={'scatter': 'Scatter',
                                        'bar': 'Bar',
                                        'box': 'Box'},
                             plotly_name='prop',
                             parent_name='parent')


# Tests
# -----
def test_acceptance(validator: BaseDataValidator):
    val = [Scatter(mode='lines'), Box(fillcolor='yellow')]
    res = validator.validate_coerce(val)
    res_present = validator.present(res)

    assert isinstance(res, list)
    assert isinstance(res_present, tuple)

    assert isinstance(res_present[0], Scatter)
    assert res_present[0].type == 'scatter'
    assert res_present[0].mode == 'lines'

    assert isinstance(res_present[1], Box)
    assert res_present[1].type == 'box'
    assert res_present[1].fillcolor == 'yellow'

    # Make sure UIDs are actually unique
    assert res_present[0].uid != res_present[1].uid


def test_acceptance_dict(validator: BaseDataValidator):
    val = (dict(type='scatter', mode='lines'),
           dict(type='box', fillcolor='yellow'))
    res = validator.validate_coerce(val)
    res_present = validator.present(res)

    assert isinstance(res, list)
    assert isinstance(res_present, tuple)
    assert isinstance(res_present[0], Scatter)
    assert res_present[0].type == 'scatter'
    assert res_present[0].mode == 'lines'

    assert isinstance(res_present[1], Box)
    assert res_present[1].type == 'box'
    assert res_present[1].fillcolor == 'yellow'

    # Make sure UIDs are actually unique
    assert res_present[0].uid != res_present[1].uid


def test_default_is_scatter(validator: BaseDataValidator):
    val = [dict(mode='lines')]
    res = validator.validate_coerce(val)
    res_present = validator.present(res)

    assert isinstance(res, list)
    assert isinstance(res_present, tuple)
    assert isinstance(res_present[0], Scatter)
    assert res_present[0].type == 'scatter'
    assert res_present[0].mode == 'lines'


def test_rejection_type(validator: BaseDataValidator):
    val = 37

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid value" in str(validation_failure.value)


def test_rejection_element_type(validator: BaseDataValidator):
    val = [42]

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)


def test_rejection_element_attr(validator: BaseDataValidator):
    val = [dict(type='scatter', bogus=99)]

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert ("Invalid property specified for object of type " +
            "plotly.graph_objs.Scatter: 'bogus'" in
            str(validation_failure.value))


def test_rejection_element_tracetype(validator: BaseDataValidator):
    val = [dict(type='bogus', a=4)]

    with pytest.raises(ValueError) as validation_failure:
        validator.validate_coerce(val)

    assert "Invalid element(s)" in str(validation_failure.value)
