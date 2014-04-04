"""
test_data:
==========

A module intended for use with Nose.

"""
from nose.tools import raises
from ...graph_objs import *
from ...exceptions import PlotlyError


def test_trivial():
    assert Data() == list()


def test_weird_instantiation():
    assert Data({}) == list({})


@raises(PlotlyError)
def test_instantiation_error():
    print Data([{}])


def test_blank_trace_instantiation():
    assert Data([Trace(), Trace()]) == list([dict(), dict()])


def test_dict_instantiation():
    Data([{'type': 'scatter'}])


@raises(PlotlyError)
def test_dict_instantiation_error():
    Data([{}])


@raises(PlotlyError)
def test_dict_instantiation_type_error():
    Data([{'type': 'invalid_type'}])


def test_validate():
    Data().validate()


@raises(PlotlyError)
def test_validate_error():
    data = Data()
    data.append({})
    data.validate()

