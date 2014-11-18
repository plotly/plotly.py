"""
test_plotly_dict:
=================

A module intended for use with Nose.

"""
from __future__ import absolute_import

from nose.tools import raises
from plotly.graph_objs.graph_objs import PlotlyDict
from plotly.exceptions import PlotlyError


def test_trivial():
    assert PlotlyDict() == dict()


# @raises(PlotlyError)  # TODO: decide if this SHOULD raise error...
# def test_instantiation_error():
#     print(PlotlyDict(anything='something'))


def test_validate():
    PlotlyDict().validate()


@raises(PlotlyError)
def test_validate_error():
    pd = PlotlyDict()
    pd['invalid']='something'
    pd.validate()