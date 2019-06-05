"""
test_scatter:
=================

A module intended for use with Nose.

"""
from __future__ import absolute_import

from nose.tools import raises
from plotly.graph_objs import Scatter
from plotly.exceptions import PlotlyError


def test_trivial():
    print(Scatter())
    assert Scatter().to_plotly_json() == dict(type='scatter')

# @raises(PlotlyError)  # TODO: decide if this SHOULD raise error...
# def test_instantiation_error():
#     print(PlotlyDict(anything='something'))


# TODO: decide if this should raise error

#def test_validate():
#    Scatter().validate()

# @raises(PlotlyError)
# def test_validate_error():
#     scatter = Scatter()
#     scatter['invalid'] = 'something'
#     scatter.validate()
