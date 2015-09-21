"""
test_data:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import
from unittest import skip

from nose.tools import raises

from plotly.exceptions import (PlotlyError, PlotlyDictKeyError,
                               PlotlyDictValueError, PlotlyDataTypeError,
                               PlotlyListEntryError)
from plotly.graph_objs import Annotations, Data, Figure, Layout


def setup():
    import warnings
    warnings.filterwarnings('ignore')


def test_trivial():
    assert Data() == list()


@raises(PlotlyError)
def test_weird_instantiation():  # Python allows this...
    print(Data({}))


def test_default_scatter():
    assert Data([{}]) == list([{'type': 'scatter'}])


def test_dict_instantiation():
    Data([{'type': 'scatter'}])


@raises(PlotlyDictKeyError)
def test_dict_instantiation_key_error():
    print(Data([{'not-a-key': 'anything'}]))


@raises(PlotlyDictValueError)
def test_dict_instantiation_key_error():
    print(Data([{'marker': 'not-a-dict'}]))


@raises(PlotlyDataTypeError)
def test_dict_instantiation_type_error():
    Data([{'type': 'invalid_type'}])


@raises(PlotlyListEntryError)
def test_dict_instantiation_graph_obj_error_0():
    Data([Data()])


@raises(PlotlyListEntryError)
def test_dict_instantiation_graph_obj_error_2():
    Data([Annotations()])


def test_validate():
    data = Data()
    data.validate()
    data += [{'type': 'scatter'}]
    data.validate()
    data += [{}, {}, {}]
    data.validate()


@raises(PlotlyDictKeyError)
def test_validate_error():
    data = Data()
    data.append({'not-a-key': 'anything'})
    data.validate()
