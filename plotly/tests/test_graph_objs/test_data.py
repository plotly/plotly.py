"""
test_data:
==========

A module intended for use with Nose.

"""
from nose.tools import raises
from ...graph_objs.graph_objs import *
from ...exceptions import PlotlyError


def setup():
    import warnings
    warnings.filterwarnings('ignore')


def test_trivial():
    assert Data() == list()


def test_weird_instantiation():  # TODO: ok?
    assert Data({}) == list({})


def test_default_scatter():
    assert Data([{}]) == list([{'type': 'scatter'}])


def test_dict_instantiation():
    Data([{'type': 'scatter'}])


@raises(PlotlyError)
def test_dict_instantiation_key_error():
    print Data([{'not-a-key': 'anything'}])


@raises(PlotlyError)
def test_dict_instantiation_type_error():
    Data([{'type': 'invalid_type'}])


@raises(PlotlyError)
def test_dict_instantiation_graph_obj_error():
    Data([Data()])


def test_validate():
    data = Data()
    data.validate()
    data += [{'type': 'scatter'}]
    data.validate()
    data += [{},{},{}]
    data.validate()


@raises(PlotlyError)
def test_validate_error():
    data = Data()
    data.append({'not-a-key': 'anything'})
    data.validate()

