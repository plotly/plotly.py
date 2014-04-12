"""
test_scatter:
=================

A module intended for use with Nose.

"""
from nose.tools import raises
from ...graph_objs import Scatter
from ...exceptions import PlotlyError


def test_trivial():
    print Scatter()
    assert Scatter() == dict(type='scatter')


# @raises(PlotlyError)  # TODO: decide if this SHOULD raise error...
# def test_instantiation_error():
#     print PlotlyDict(anything='something')


def test_validate():
    Scatter().validate()


@raises(PlotlyError)
def test_validate_error():
    scatter = Scatter()
    scatter['invalid']='something'
    scatter.validate()