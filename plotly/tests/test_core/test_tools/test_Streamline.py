from unittest import TestCase
from plotly.graph_objs import graph_objs, Scatter, Data, Marker, Line, Trace
from plotly.exceptions import PlotlyError

import plotly.plotly as py
import plotly.tools as tls
import math
from nose.tools import raises


@raises(ValueError)
def test_wrong_arrow_scale():
    data = tls.Streamline(x=[0, 2], y=[0, 2],
                          u=[[-1, -5], [-1, -5]],
                          v=[[1, 1], [-3, -3]],
                          arrow_scale=0)


@raises(ValueError)
def test_wrong_density():
    data = tls.Streamline(x=[0, 2], y=[0, 2],
                          u=[[-1, -5], [-1, -5]],
                          v=[[1, 1], [-3, -3]],
                          density=-1)


@raises(PlotlyError)
def test_uneven_x():
    data = tls.Streamline(x=[0, 2, 7, 9], y=[0, 2, 4, 6],
                          u=[[-1, -5], [-1, -5]],
                          v=[[1, 1], [-3, -3]])


@raises(PlotlyError)
def test_uneven_y():
    data = tls.Streamline(x=[0, 2, 4], y=[0, 2, 6],
                          u=[[-1, -5], [-1, -5]],
                          v=[[1, 1], [-3, -3]])


class TestStreamline(TestCase):

    def test_simple(self):
        self.assertEqual((tls.Streamline(x=[0, 2], y=[0, 2],
                                         u=[[-1, -5], [-1, -5]],
                                         v=[[1, 1], [-3, -3]],
                                         density=2, arrow_scale=.4,
                                         angle=math.pi/6,
                                         line=Line(color='purple',
                                                   width=3))).keys(),
                         (['y', 'x', 'line', 'name', 'mode']))
