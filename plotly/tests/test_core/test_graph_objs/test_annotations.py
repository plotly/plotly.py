"""
test_annotations:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import

from nose.tools import raises
from plotly.graph_objs import *
from plotly.exceptions import (PlotlyError,
                               PlotlyDictKeyError,
                               PlotlyDictValueError,
                               PlotlyDataTypeError,
                               PlotlyListEntryError)


def setup():
    import warnings
    warnings.filterwarnings('ignore')


def test_trivial():
    assert Annotations() == list()


@raises(PlotlyError)
def test_weird_instantiation():  # Python allows this, but nonsensical for us.
    print(Annotations({}))


def test_dict_instantiation():
    Annotations([{'text': 'annotation text'}])


@raises(PlotlyDictKeyError)
def test_dict_instantiation_key_error():
    print(Annotations([{'not-a-key': 'anything'}]))


@raises(PlotlyDictValueError)
def test_dict_instantiation_key_error():
    print(Annotations([{'font': 'not-a-dict'}]))


@raises(PlotlyListEntryError)
def test_dict_instantiation_graph_obj_error_0():
    Annotations([Data()])


@raises(PlotlyListEntryError)
def test_dict_instantiation_graph_obj_error_1():
    Annotations([Figure()])


@raises(PlotlyListEntryError)
def test_dict_instantiation_graph_obj_error_2():
    Annotations([Annotations()])


@raises(PlotlyListEntryError)
def test_dict_instantiation_graph_obj_error_3():
    Annotations([Layout()])


def test_validate():
    annotations = Annotations()
    annotations.validate()
    annotations += [{'text': 'some text'}]
    annotations.validate()
    annotations += [{},{},{}]
    annotations.validate()


@raises(PlotlyDictKeyError)
def test_validate_error():
    annotations = Annotations()
    annotations.append({'not-a-key': 'anything'})
    annotations.validate()

