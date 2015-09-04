from __future__ import absolute_import

from nose.tools import raises

from plotly.graph_objs import (Data, Figure, Layout, Scatter, Scatter3d, Scene,
                               XAxis, YAxis)
import plotly.tools as tls


@raises(Exception)
def test_print_grid_before_make_subplots():
    fig = Figure()
    fig.print_grid()


@raises(Exception)
def test_append_trace_before_make_subplots():
    trace = Scatter(x=[1, 2, 3], y=[2, 3, 4])
    fig = Figure()
    fig.append_trace(trace, 2, 2)


@raises(Exception)
def test_append_trace_row_out_of_range():
    trace = Scatter(x=[1, 2, 3], y=[2, 3, 4])
    fig = tls.make_subplots(rows=2, cols=3)
    fig.append_trace(trace, 10, 2)


@raises(Exception)
def test_append_trace_col_out_of_range():
    trace = Scatter(x=[1, 2, 3], y=[2, 3, 4])
    fig = tls.make_subplots(rows=2, cols=3)
    fig.append_trace(trace, 2, 0)


def test_append_scatter():
    expected = Figure(
        data=Data([
            Scatter(
                x=[1, 2, 3],
                y=[2, 3, 4],
                xaxis='x5',
                yaxis='y5'
            )
        ]),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.2888888888888889],
                anchor='y1'
            ),
            xaxis2=XAxis(
                domain=[0.35555555555555557, 0.6444444444444445],
                anchor='y2'
            ),
            xaxis3=XAxis(
                domain=[0.7111111111111111, 1.0],
                anchor='y3'
            ),
            xaxis4=XAxis(
                domain=[0.0, 0.2888888888888889],
                anchor='y4'
            ),
            xaxis5=XAxis(
                domain=[0.35555555555555557, 0.6444444444444445],
                anchor='y5'
            ),
            xaxis6=XAxis(
                domain=[0.7111111111111111, 1.0],
                anchor='y6'
            ),
            yaxis1=YAxis(
                domain=[0.575, 1.0],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.575, 1.0],
                anchor='x2'
            ),
            yaxis3=YAxis(
                domain=[0.575, 1.0],
                anchor='x3'
            ),
            yaxis4=YAxis(
                domain=[0.0, 0.425],
                anchor='x4'
            ),
            yaxis5=YAxis(
                domain=[0.0, 0.425],
                anchor='x5'
            ),
            yaxis6=YAxis(
                domain=[0.0, 0.425],
                anchor='x6'
            )
        )
    )

    trace = Scatter(x=[1, 2, 3], y=[2, 3, 4])
    fig = tls.make_subplots(rows=2, cols=3)
    fig.append_trace(trace, 2, 2)
    assert fig == expected


@raises(Exception)
def test_append_scatter_after_deleting_xaxis():
    trace = Scatter(x=[1, 2, 3], y=[2, 3, 4])
    fig = tls.make_subplots(rows=2, cols=3)
    fig['layout'].pop('xaxis5', None)
    fig.append_trace(trace, 2, 2)


@raises(Exception)
def test_append_scatter_after_deleting_yaxis():
    trace = Scatter(x=[1, 2, 3], y=[2, 3, 4])
    fig = tls.make_subplots(rows=2, cols=3)
    fig['layout'].pop('yaxis5', None)
    fig.append_trace(trace, 2, 2)


def test_append_scatter3d():
    expected = Figure(
        data=Data([
            Scatter3d(
                x=[1, 2, 3],
                y=[2, 3, 4],
                z=[1, 2, 3],
                scene='scene1'
            ),
            Scatter3d(
                x=[1, 2, 3],
                y=[2, 3, 4],
                z=[1, 2, 3],
                scene='scene2'
            )
        ]),
        layout=Layout(
            scene1=Scene(
                domain={'y': [0.575, 1.0], 'x': [0.0, 1.0]}
            ),
            scene2=Scene(
                domain={'y': [0.0, 0.425], 'x': [0.0, 1.0]}
            )
        )
    )

    fig = tls.make_subplots(rows=2, cols=1,
                            specs=[[{'is_3d': True}],
                                   [{'is_3d': True}]])
    trace = Scatter3d(x=[1, 2, 3], y=[2, 3, 4], z=[1, 2, 3])
    fig.append_trace(trace, 1, 1)
    fig.append_trace(trace, 2, 1)
    assert fig == expected


@raises(Exception)
def test_append_scatter3d_after_deleting_scene():
    fig = tls.make_subplots(rows=2, cols=1,
                            specs=[[{'is_3d': True}],
                                   [{'is_3d': True}]])
    trace = Scatter3d(x=[1, 2, 3], y=[2, 3, 4], z=[1, 2, 3])
    fig['layout'].pop('scene1', None)
    fig.append_trace(trace, 1, 1)
