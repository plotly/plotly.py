"""
test_annotations:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import
from unittest import skip

from nose.tools import raises

from plotly.exceptions import (PlotlyError, PlotlyDictKeyError,
                               PlotlyDictValueError, PlotlyListEntryError)
from plotly.graph_objs import Annotation, Annotations, Data, Figure, Layout


def setup():
    import warnings
    warnings.filterwarnings('ignore')


def test_trivial():
    assert Annotations() == list()


def test_weird_instantiation():  # Python allows this, but nonsensical for us.
    assert Annotations({}) == list()


def test_dict_instantiation():
    Annotations([{'text': 'annotation text'}])


def test_dict_instantiation_key_error():
    assert Annotations([{'not-a-key': 'anything'}]) == [{'not-a-key': 'anything'}]


def test_dict_instantiation_key_error_2():
    assert Annotations([{'font': 'not-a-dict'}]) == [{'font': 'not-a-dict'}]


def test_dict_instantiation_graph_obj_error_0():
    assert Annotations([Data()]) == [[]]


def test_dict_instantiation_graph_obj_error_2():
    assert Annotations([Annotations()]) == [[]]

