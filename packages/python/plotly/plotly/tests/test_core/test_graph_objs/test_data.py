"""
test_data:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import
from unittest import skip


from plotly.exceptions import (
    PlotlyError,
    PlotlyDictKeyError,
    PlotlyDictValueError,
    PlotlyDataTypeError,
    PlotlyListEntryError,
)
from plotly.graph_objs import Annotations, Data, Figure, Layout


def setup():
    import warnings

    warnings.filterwarnings("ignore")


def test_trivial():
    assert Data() == list()


def test_weird_instantiation():  # Python allows this...
    assert Data({}) == []


def test_default_scatter():
    assert Data([{}]) == list([{}])


def test_dict_instantiation():
    Data([{"type": "scatter"}])


def test_dict_instantiation_key_error():
    assert Data([{"not-a-key": "anything"}]) == [{"not-a-key": "anything"}]


def test_dict_instantiation_key_error_2():
    assert Data([{"marker": "not-a-dict"}]) == [{"marker": "not-a-dict"}]


def test_dict_instantiation_type_error():
    assert Data([{"type": "invalid_type"}]) == [{"type": "invalid_type"}]


def test_dict_instantiation_graph_obj_error_0():
    assert Data([Data()]) == [[]]


def test_dict_instantiation_graph_obj_error_2():
    assert Data([Annotations()]) == [[]]
