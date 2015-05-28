import plotly
from plotly.graph_objs import *
import plotly.tools as tls
from nose.tools import raises
import numpy as np


@raises(Exception)
def unequal_xy_length():
    data = tls.Quiver(x=[1, 2], y=[1], u=[1, 2], v=[1, 2])


@raises(Exception)
def unequal_uv_length():
    data = tls.Quiver(x=[1, 2], y=[1, 3], u=[1], v=[1, 2])


@raises(Exception)
def test_wrong_kwarg():
    data = tls.Quiver(stuff='not gonna work')


def test_one_arrow():
    nan = np.nan
    trace1 = Scatter(
            x=[0., 1., nan],
            y=[0., 1., nan],
            mode='lines',
            name='Barb',
            line=Line(color='rgb(114, 132, 314)', width=1)
            )
    trace2 = Scatter(
            x=np.array([0.82069826, 1., 0.61548617, nan]),
            y=np.array([0.61548617,  1.,  0.82069826, nan]),
            mode='lines',
            name='Arrow',
            line=Line(color='rgb(114, 132, 314)', width=1)
            )
    expected = Data([trace1, trace2])
    assert tls.Quiver(x=[0], y=[0], u=[1], v=[1], scale=1) == expected
