"""
test_plotly_dict:
=================

A module intended for use with Nose.

"""
from __future__ import absolute_import

from nose.tools import raises

from plotly.exceptions import PlotlyError
from plotly.graph_objs.graph_objs import PlotlyDict, PlotlyList


@raises(PlotlyError)
def test_instantiate_plotly_dict():
    PlotlyDict()


@raises(PlotlyError)
def test_instantiate_plotly_list():
    PlotlyList()
