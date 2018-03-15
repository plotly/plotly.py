from unittest import mock
import pytest


@pytest.fixture(scope="module")
def parent():
    parent_obj = mock.Mock()
    parent_props = {'plotly_obj': {}}
    parent_prop_defaults = {'plotly_obj': {}}
    parent_obj._get_child_props.return_value = parent_props['plotly_obj']
    parent_obj._get_child_prop_defaults.return_value = parent_prop_defaults['plotly_obj']
    parent_obj._in_batch_mode = False
    return parent_obj
