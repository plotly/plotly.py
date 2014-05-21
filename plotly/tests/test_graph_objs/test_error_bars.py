"""
test_error_bars:
================

A module intended for use with Nose.

"""
from nose.tools import raises
from ...graph_objs.graph_objs import *
from ...exceptions import (PlotlyDictKeyError, PlotlyDictValueError,
                           PlotlyDataTypeError, PlotlyListEntryError)

def test_instantiate_error_x():
    ErrorX()
    ErrorX(value=0.1, type='percent', color='red')


def test_instantiate_error_y():
    ErrorY()
    ErrorY(value=0.1, type='percent', color='red')


@raises(PlotlyDictKeyError)
def test_key_error():
    ErrorX(value=0.1, typ='percent', color='red')