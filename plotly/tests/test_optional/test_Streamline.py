import plotly
from plotly.graph_objs import graph_objs, Scatter, Data, Marker, Line
import plotly.tools as tls
from nose.tools import raises
import numpy as np


@raises(Exception)
def test_even_x_spacing():
    data = tls.Streamline(x=[1, 2, 2.2], y=[1, 2, 3],
                          u=np.matrix('1 2 3; 1 2 3; 1 2 3'),
                          v=np.matrix('1 2 3; 1 2 3; 1 2 3'))


@raises(Exception)
def test_even_y_spacing():
    data = tls.Streamline(x=[1, 2, 3], y=[1, 2.5, 3],
                          u=np.matrix('1 2 3; 1 2 3; 1 2 3'),
                          v=np.matrix('1 2 3; 1 2 3; 1 2 3'))


@raises(Exception)
def test_uv_dimmensions():
    data = tls.Streamline(x=[1, 2, 3], y=[1, 2, 3],
                          u=np.matrix('1 2 3; 1 2 3; 1 2 3'),
                          v=np.matrix('1 2 3; 1 2 3'))


@raises(Exception)
def test_wrong_kwarg():
    data = tls.Streamline(x=[1, 2, 3], y=[1, 2, 3],
                          u=np.matrix('1 2 3; 1 2 3; 1 2 3'),
                          v=np.matrix('1 2 3; 1 2 3; 1 2 3'),
                          nope="not gonna work")


@raises(Exception)
def test_wrong_density():
    data = tls.Streamline(x=[1, 2, 3], y=[1, 2, 3],
                          u=np.matrix('1 2 3; 1 2 3; 1 2 3'),
                          v=np.matrix('1 2 3; 1 2 3; 1 2 3'),
                          density=0)


def test_simple_streamline():
    trace1 = Scatter(
            x=[0., 1., nan],
            y=[0., 1., nan],
            mode='lines',
            name='Barb',
            line=Line(color='rgb(114, 132, 314)', width=1)
            )
    trace2 = Scatter(
            x=[0.82069826, 1., 0.61548617, nan],
            y=[0.61548617,  1.,  0.82069826, nan],
            mode='lines',
            name='Arrow',
            line=Line(color='rgb(114, 132, 314)', width=1)
            )
    expected = Data([trace1, trace2])

    data = tls.Streamline(x=[1, 2, 3], y=[1, 2, 3],
                          u=np.matrix('1 2 3; 1 2 3; 1 2 3'),
                          v=np.matrix('1 2 3; 1 2 3; 1 2 3'),
                          density=0)

    np.testing.assert_almost_equal(data[0]['y'], expected[0]['y'])
    np.testing.assert_almost_equal(data[0]['x'], expected[0]['x'])
    np.testing.assert_almost_equal(data[1]['y'], expected[1]['y'])
    np.testing.assert_almost_equal(data[1]['x'], expected[1]['x'])
    assert data[0].keys() == expected[0].keys()


def test_complicated_streamline():
