"""
test_get_figure:
=================

A module intended for use with Nose.

"""
from __future__ import absolute_import

import time

from nose.plugins.attrib import attr
from nose.tools import raises, eq_

import plotly.plotly as py
from plotly.graph_objs import (Layout, Scatter, Stream)
from plotly import exceptions

un = 'PythonAPI'
ak = 'ubpiol2cve'
tk = 'vaia8trjjb'
config = {'plotly_domain': 'https://plot.ly',
          'plotly_streaming_domain': 'stream.plot.ly',
          'plotly_api_domain': 'https://api.plot.ly'}


def setUp():
    py.sign_in(un, ak, **config)


@attr('slow')
def test_initialize_stream_plot():
    py.sign_in(un, ak)
    stream = Stream(token=tk, maxpoints=50)
    url = py.plot([Scatter(x=[], y=[], mode='markers', stream=stream)],
                  auto_open=False,
                  world_readable=True,
                  filename='stream-test')
    assert url == 'https://plot.ly/~PythonAPI/461'
    time.sleep(.5)


@attr('slow')
def test_stream_single_points():
    py.sign_in(un, ak)
    stream = Stream(token=tk, maxpoints=50)
    res = py.plot([Scatter(x=[], y=[], mode='markers', stream=stream)],
                  auto_open=False,
                  world_readable=True,
                  filename='stream-test')
    time.sleep(.5)
    my_stream = py.Stream(tk)
    my_stream.open()
    my_stream.write(Scatter(x=1, y=10))
    time.sleep(.5)
    my_stream.close()


@attr('slow')
def test_stream_multiple_points():
    py.sign_in(un, ak)
    stream = Stream(token=tk, maxpoints=50)
    url = py.plot([Scatter(x=[], y=[], mode='markers', stream=stream)],
                  auto_open=False,
                  world_readable=True,
                  filename='stream-test')
    time.sleep(.5)
    my_stream = py.Stream(tk)
    my_stream.open()
    my_stream.write(Scatter(x=[1, 2, 3, 4], y=[2, 1, 2, 5]))
    time.sleep(.5)
    my_stream.close()


@attr('slow')
def test_stream_layout():
    py.sign_in(un, ak)
    stream = Stream(token=tk, maxpoints=50)
    url = py.plot([Scatter(x=[], y=[], mode='markers', stream=stream)],
                  auto_open=False,
                  world_readable=True,
                  filename='stream-test')
    time.sleep(.5)
    title_0 = "some title i picked first"
    title_1 = "this other title i picked second"
    my_stream = py.Stream(tk)
    my_stream.open()
    my_stream.write(Scatter(x=1, y=10), layout=Layout(title=title_0))
    time.sleep(.5)
    my_stream.close()
    my_stream.open()
    my_stream.write(Scatter(x=1, y=10), layout=Layout(title=title_1))
    my_stream.close()


@attr('slow')
@raises(exceptions.PlotlyError)
def test_stream_validate_data():
    py.sign_in(un, ak)
    my_stream = py.Stream(tk)
    my_stream.open()
    my_stream.write(dict(x=1, y=10, z=[1]))  # assumes scatter...
    my_stream.close()


@attr('slow')
@raises(exceptions.PlotlyError)
def test_stream_validate_layout():
    py.sign_in(un, ak)
    my_stream = py.Stream(tk)
    my_stream.open()
    my_stream.write(Scatter(x=1, y=10), layout=Layout(legend=True))
    my_stream.close()


@attr('slow')
def test_stream_unstreamable():

    # even though `name` isn't streamable, we don't validate it --> should pass

    py.sign_in(un, ak)
    my_stream = py.Stream(tk)
    my_stream.open()
    my_stream.write(Scatter(x=1, y=10, name='nope'))
    my_stream.close()


def test_stream_no_scheme():

    # If no scheme is used in the plotly_streaming_domain, port 80
    # should be used for streaming and ssl_enabled should be False

    py.sign_in(un, ak, **{'plotly_streaming_domain': 'stream.plot.ly'})
    my_stream = py.Stream(tk)
    expected_streaming_specs = {
        'server': 'stream.plot.ly',
        'port': 80,
        'ssl_enabled': False,
        'headers': {
            'Host': 'stream.plot.ly',
            'plotly-streamtoken': tk
        }
    }
    actual_streaming_specs = my_stream.get_streaming_specs()
    eq_(expected_streaming_specs, actual_streaming_specs)


def test_stream_http():

    # If the http scheme is used in the plotly_streaming_domain, port 80
    # should be used for streaming and ssl_enabled should be False

    py.sign_in(un, ak, **{'plotly_streaming_domain': 'http://stream.plot.ly'})
    my_stream = py.Stream(tk)
    expected_streaming_specs = {
        'server': 'stream.plot.ly',
        'port': 80,
        'ssl_enabled': False,
        'headers': {
            'Host': 'stream.plot.ly',
            'plotly-streamtoken': tk
        }
    }
    actual_streaming_specs = my_stream.get_streaming_specs()
    eq_(expected_streaming_specs, actual_streaming_specs)


def test_stream_https():

    # If the https scheme is used in the plotly_streaming_domain, port 443
    # should be used for streaming and ssl_enabled should be True

    py.sign_in(un, ak, **{'plotly_streaming_domain': 'https://stream.plot.ly'})
    my_stream = py.Stream(tk)
    expected_streaming_specs = {
        'server': 'stream.plot.ly',
        'port': 443,
        'ssl_enabled': True,
        'headers': {
            'Host': 'stream.plot.ly',
            'plotly-streamtoken': tk
        }
    }
    actual_streaming_specs = my_stream.get_streaming_specs()
    eq_(expected_streaming_specs, actual_streaming_specs)
