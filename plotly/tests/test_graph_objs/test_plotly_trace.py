"""
test_trace:
===========

A module intended for use with Nose.

"""
from nose.tools import raises
from ...graph_objs import PlotlyTrace
from ...exceptions import PlotlyError


def test_trivial():
    assert PlotlyTrace() == dict()


# @raises(PlotlyError)  # TODO: decide if this SHOULD raise error...
# def test_instantiation_error():
#     print Trace(anything='something')


def test_validate():
    PlotlyTrace().validate()


@raises(PlotlyError)
def test_validate_error():
    trace = PlotlyTrace()
    trace['invalid'] = 'something'
    trace.validate()
