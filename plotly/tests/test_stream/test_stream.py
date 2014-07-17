"""
test_get_figure:
=================

A module intended for use with Nose.

"""
import time
from nose.tools import raises
from ... graph_objs import *
from ... plotly import plotly as py
from ... import exceptions

un = 'pythonapi'
ak = 'ubpiol2cve'
tk = 'vaia8trjjb'
fi = 461
py.sign_in(un, ak)

run_tests = False


def test_initialize_stream_plot():
    if run_tests:
        stream = Stream(token=tk, maxpoints=50)
        res = py.plot([Scatter(x=[], y=[], mode='markers', stream=stream)],
                      auto_open=False,
                      filename='stream-test')
        assert res == 'https://plot.ly/~PythonAPI/461'
        time.sleep(5)


def test_stream_single_points():
    if run_tests:
        stream = Stream(token=tk, maxpoints=50)
        res = py.plot([Scatter(x=[], y=[], mode='markers', stream=stream)],
                      auto_open=False,
                      filename='stream-test')
        time.sleep(5)
        my_stream = py.Stream(tk)
        my_stream.open()
        my_stream.write(Scatter(x=1, y=10))
        time.sleep(1)
        my_stream.close()
        fig = py.get_figure(un, fi)
        print(fig.to_string())
        assert fig['data'][0]['x'] == 1
        assert fig['data'][0]['y'] == 10


def test_stream_multiple_points():
    if run_tests:
        stream = Stream(token=tk, maxpoints=50)
        res = py.plot([Scatter(x=[], y=[], mode='markers', stream=stream)],
                      auto_open=False,
                      filename='stream-test')
        time.sleep(5)
        my_stream = py.Stream(tk)
        my_stream.open()
        my_stream.write(Scatter(x=[1, 2, 3, 4], y=[2, 1, 2, 5]))
        time.sleep(1)
        my_stream.close()
        fig = py.get_figure(un, fi)
        print(fig.to_string())
        assert fig['data'][0]['x'] == [1, 2, 3, 4]
        assert fig['data'][0]['y'] == [2, 1, 2, 5]


def test_stream_layout():
    if run_tests:
        stream = Stream(token=tk, maxpoints=50)
        res = py.plot([Scatter(x=[], y=[], mode='markers', stream=stream)],
                      auto_open=False,
                      filename='stream-test')
        time.sleep(5)
        title_0 = "some title i picked first"
        title_1 = "this other title i picked second"
        my_stream = py.Stream(tk)
        my_stream.open()
        my_stream.write(Scatter(x=1, y=10), layout=Layout(title=title_0))
        time.sleep(1)
        my_stream.close()
        fig = py.get_figure(un, fi)
        print(fig.to_string())
        assert fig['layout']['title'] == title_0
        my_stream.open()
        my_stream.write(Scatter(x=1, y=10), layout=Layout(title=title_1))
        time.sleep(1)
        my_stream.close()
        fig = py.get_figure(un, fi)
        print(fig.to_string())
        assert fig['layout']['title'] == title_1


@raises(exceptions.PlotlyError)
def test_stream_validate_data():
    if run_tests:
        my_stream = py.Stream(tk)
        my_stream.open()
        my_stream.write(dict(x=1, y=10, z=[1]))  # assumes scatter...
        time.sleep(1)
        my_stream.close()
    else:
        raise exceptions.PlotlyError()


@raises(exceptions.PlotlyError)
def test_stream_validate_layout():
    if run_tests:
        my_stream = py.Stream(tk)
        my_stream.open()
        my_stream.write(Scatter(x=1, y=10), layout=Layout(legend=True))
        time.sleep(1)
        my_stream.close()
    else:
        raise exceptions.PlotlyError()