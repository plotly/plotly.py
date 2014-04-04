"""
test_trace:
===========

A module intended for use with Nose.

"""
from nose.tools import raises
from ...graph_objs import Trace
from ...exceptions import PlotlyError


def test_trivial():
    assert Trace() == dict()


# @raises(PlotlyError)  # TODO: decide if this SHOULD raise error...
# def test_instantiation_error():
#     print Trace(anything='something')


def test_validate():
    Trace().validate()


@raises(PlotlyError)
def test_validate_error():
    trace = Trace()
    trace['invalid'] = 'something'
    trace.validate()
