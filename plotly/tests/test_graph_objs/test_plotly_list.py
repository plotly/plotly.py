"""
test_plotly_list:
=================

A module intended for use with Nose.

"""
from __future__ import absolute_import

from nose.tools import raises
from plotly.graph_objs.graph_objs import PlotlyList, PlotlyDict
from plotly.exceptions import PlotlyError


def test_trivial():
    assert PlotlyList() == list()


@raises(PlotlyError)
def test_weird_instantiation():
    print(PlotlyList({}))


@raises(PlotlyError)
def test_instantiation_error():
    print(PlotlyList([{}]))


def test_blank_trace_instantiation():
    assert PlotlyList([PlotlyDict(), PlotlyDict()]) == list([dict(), dict()])


def test_validate():
    PlotlyList().validate()


@raises(PlotlyError)
def test_validate_error():
    pl = PlotlyList()
    pl.append({})
    pl.validate()