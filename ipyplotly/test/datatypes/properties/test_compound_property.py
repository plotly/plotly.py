from unittest import mock
import pytest
from ipyplotly.basedatatypes import BasePlotlyType
from ipyplotly.basevalidators import CompoundValidator


# Fixtures
# --------
@pytest.fixture()
def plotly_obj():

    # ### Setup plotly obj (make fixture eventually) ###
    plotly_obj = BasePlotlyType('plotly_obj')

    # Add validator
    validator = mock.Mock(spec=CompoundValidator,
                          wraps=CompoundValidator('prop1', 'plotly_obj', data_class=mock.Mock, data_docs=''))
    plotly_obj._validators['prop1'] = validator

    # Mock out _send_update
    plotly_obj._send_update = mock.Mock()

    return plotly_obj


# Validation
# ----------
def test_set_invalid_property(plotly_obj):
    with pytest.raises(KeyError) as failure:
        plotly_obj['bogus'] = 'Hello'


def test_get_invalid_property(plotly_obj):
    with pytest.raises(KeyError) as failure:
        p = plotly_obj['bogus']


# Orphan
# ------
@pytest.mark.xfail
def test_set_get_compound_property(plotly_obj):
    # Setup value
    # -----------
    v = mock.Mock()
    d = {'a': 23}
    type(v)._data = mock.PropertyMock(return_value=d)

    # Perform set_prop
    # ----------------
    plotly_obj['prop1'] = v

    # Mutate d
    # --------
    # Just to make sure we copy data on assignment
    d['a'] = 1

    # Object Assertions
    # -----------------
    # ### test get object is a copy ###
    assert plotly_obj['prop1'] is not v

    # ### _send_update sent ###
    plotly_obj._send_update.assert_called_once_with('prop1', {'a': 23})

    # ### _orphan_data configured properly ###
    assert plotly_obj._orphan_data == {'prop1': {'a': 23}}

    # ### _data is mapped to _orphan_data
    assert plotly_obj._props is plotly_obj._orphan_data

    # ### validator called properly ###
    plotly_obj._validators['prop1'].validate_coerce.assert_called_once_with(v)

    # Value Assertions
    # ----------------
    # ### Parent set to plotly_obj
    assert v._parent is plotly_obj

    # ### Orphan data cleared ###
    v._orphan_data.clear.assert_called_once()


# With parent
# -----------
@pytest.mark.xfail
def test_set_get_property_with_parent(plotly_obj, parent):

    # Setup value
    # -----------
    v = mock.Mock()
    d = {'a': 23}
    type(v)._data = mock.PropertyMock(return_value=d)

    # Setup parent
    # ------------
    plotly_obj._parent = parent

    # Perform set_prop
    # ----------------
    plotly_obj['prop1'] = v

    # Parent Assertions
    # -----------------
    parent._get_child_props.assert_called_with(plotly_obj)

    # Object Assertions
    # -----------------
    # ### test get object is a copy ###
    assert plotly_obj['prop1'] is not v

    # ### _send_update sent ###
    plotly_obj._send_update.assert_called_once_with('prop1', d)

    # ### orphan data cleared ###
    assert plotly_obj._orphan_data == {}

    # ### _data bound to parent dict ###
    assert parent._get_child_props(plotly_obj) is plotly_obj._props

    # ### validator called properly ###
    plotly_obj._validators['prop1'].validate_coerce.assert_called_once_with(v)

    # Value Assertions
    # ----------------
    # ### Parent set to plotly_obj
    assert v._parent is plotly_obj

    # ### Orphan data cleared ###
    v._orphan_data.clear.assert_called_once()
