import math
from unittest import TestCase

import datetime
from nose.tools import raises

import plotly.tools as tls
from plotly.exceptions import PlotlyError
from plotly.graph_objs import graph_objs


class TestFinanceCharts(TestCase):

    def test_unequal_ohlc_length(self):

        # check: PlotlyError if open, high, low, close are not the same length
        # for TraceFactory.create_ohlc and TraceFactory.create_candlestick

        kwargs = {'open': [1], 'high': [1, 3],
                  'low': [1, 2], 'close': [1, 2],
                  'direction': ['increasing']}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_ohlc, **kwargs)
        self.assertRaises(PlotlyError, tls.FigureFactory.create_candlestick,
                          **kwargs)

        kwargs = {'open': [1, 2], 'high': [1, 2, 3],
                  'low': [1, 2], 'close': [1, 2],
                  'direction': ['decreasing']}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_ohlc, **kwargs)
        self.assertRaises(PlotlyError, tls.FigureFactory.create_candlestick,
                          **kwargs)

        kwargs = {'open': [1, 2], 'high': [2, 3],
                  'low': [0], 'close': [1, 3]}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_ohlc, **kwargs)
        self.assertRaises(PlotlyError, tls.FigureFactory.create_candlestick,
                          **kwargs)

        kwargs = {'open': [1, 2], 'high': [2, 3],
                  'low': [1, 2], 'close': [1]}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_ohlc, **kwargs)
        self.assertRaises(PlotlyError, tls.FigureFactory.create_candlestick,
                          **kwargs)

    def test_direction_arg(self):

        # check: PlotlyError if direction is not defined as "increasing" or
        # "decreasing" for TraceFactory.create_ohlc and
        # TraceFactory.create_candlestick

        kwargs = {'open': [1, 4], 'high': [1, 5],
                  'low': [1, 2], 'close': [1, 2],
                  'direction': ['inc']}
        self.assertRaisesRegexp(PlotlyError,
                                "direction must be defined as "
                                "'increasing', 'decreasing', or 'both'",
                                tls.FigureFactory.create_ohlc, **kwargs)
        self.assertRaisesRegexp(PlotlyError,
                                "direction must be defined as "
                                "'increasing', 'decreasing', or 'both'",
                                tls.FigureFactory.create_candlestick, **kwargs)

        kwargs = {'open': [1, 2], 'high': [1, 3],
                  'low': [1, 2], 'close': [1, 2],
                  'direction': ['d']}
        self.assertRaisesRegexp(PlotlyError,
                                "direction must be defined as "
                                "'increasing', 'decreasing', or 'both'",
                                tls.FigureFactory.create_ohlc, **kwargs)
        self.assertRaisesRegexp(PlotlyError,
                                "direction must be defined as "
                                "'increasing', 'decreasing', or 'both'",
                                tls.FigureFactory.create_candlestick, **kwargs)

    def test_high_highest_value(self):

        # check: PlotlyError if the "high" value is less than the corresponding
        # open, low, or close value because if the "high" value is not the
        # highest (or equal) then the data may have been entered incorrectly.

        kwargs = {'open': [2, 3], 'high': [4, 2],
                  'low': [1, 1], 'close': [1, 2]}
        self.assertRaisesRegexp(PlotlyError, "Oops! Looks like some of "
                                             "your high values are less "
                                             "the corresponding open, "
                                             "low, or close values. "
                                             "Double check that your data "
                                             "is entered in O-H-L-C order",
                                tls.FigureFactory.create_ohlc,
                                **kwargs)
        self.assertRaisesRegexp(PlotlyError, "Oops! Looks like some of "
                                             "your high values are less "
                                             "the corresponding open, "
                                             "low, or close values. "
                                             "Double check that your data "
                                             "is entered in O-H-L-C order",
                                tls.FigureFactory.create_candlestick,
                                **kwargs)

    def test_low_lowest_value(self):

        # check: PlotlyError if the "low" value is greater than the
        # corresponding open, high, or close value because if the "low" value
        # is not the lowest (or equal) then the data may have been entered
        # incorrectly.

        # create_ohlc_increase
        kwargs = {'open': [2, 3], 'high': [4, 6],
                  'low': [3, 1], 'close': [1, 2]}
        self.assertRaisesRegexp(PlotlyError,
                                "Oops! Looks like some of "
                                "your low values are greater "
                                "than the corresponding high"
                                ", open, or close values. "
                                "Double check that your data "
                                "is entered in O-H-L-C order",
                                tls.FigureFactory.create_ohlc,
                                **kwargs)
        self.assertRaisesRegexp(PlotlyError,
                                "Oops! Looks like some of "
                                "your low values are greater "
                                "than the corresponding high"
                                ", open, or close values. "
                                "Double check that your data "
                                "is entered in O-H-L-C order",
                                tls.FigureFactory.create_candlestick,
                                **kwargs)

    def test_one_ohlc(self):

        # This should create one "increase" (i.e. close > open) ohlc stick

        ohlc_incr = tls.FigureFactory.create_ohlc(open=[33.0],
                                                  high=[33.2],
                                                  low=[32.7],
                                                  close=[33.1])

        expected_ohlc_incr = {'layout': {'hovermode': 'closest',
                                         'xaxis': {'zeroline': False}},
                              'data': [{'y': [33.0, 33.0, 33.2, 32.7,
                                              33.1, 33.1, None],
                                        'line': {'color': '#3D9970'},
                                        'showlegend': False,
                                        'name': 'Increasing',
                                        'text': ('Open', 'Open', 'High', 'Low',
                                                 'Close', 'Close', ''),
                                        'mode': 'lines',
                                        'type': 'scatter',
                                        'x': [-0.2, 0, 0, 0, 0, 0.2, None]},
                                       {'y': [],
                                        'line': {'color': '#FF4136'},
                                        'showlegend': False,
                                        'name': 'Decreasing',
                                        'text': (),
                                        'mode': 'lines',
                                        'type': 'scatter', 'x': []}
                                       ]}

        self.assertEqual(ohlc_incr, expected_ohlc_incr)

    def test_one_ohlc_increase(self):

        # This should create one "increase" (i.e. close > open) ohlc stick

        ohlc_incr = tls.FigureFactory.create_ohlc(open=[33.0],
                                                  high=[33.2],
                                                  low=[32.7],
                                                  close=[33.1],
                                                  direction="increasing")

        expected_ohlc_incr = {'layout': {'hovermode': 'closest',
                                         'xaxis': {'zeroline': False}},
                              'data': [{'y': [33.0, 33.0, 33.2, 32.7,
                                              33.1, 33.1, None],
                                        'line': {'color': '#3D9970'},
                                        'showlegend': False,
                                        'name': 'Increasing',
                                        'text': ('Open', 'Open', 'High', 'Low',
                                                 'Close', 'Close', ''),
                                        'mode': 'lines',
                                        'type': 'scatter',
                                        'x': [-0.2, 0, 0, 0, 0, 0.2, None]
                                        }]
                              }
        self.assertEqual(ohlc_incr, expected_ohlc_incr)

    def test_one_ohlc_decrease(self):

        # This should create one "increase" (i.e. close > open) ohlc stick

        ohlc_decr = tls.FigureFactory.create_ohlc(open=[33.0],
                                                  high=[33.2],
                                                  low=[30.7],
                                                  close=[31.1],
                                                  direction="decreasing")

        expected_ohlc_decr = {'layout': {'hovermode': 'closest',
                                         'xaxis': {'zeroline': False}},
                              'data': [{'y': [33.0, 33.0, 33.2, 30.7,
                                              31.1, 31.1, None],
                                        'line': {'color': '#FF4136'},
                                        'showlegend': False,
                                        'name': 'Decreasing',
                                        'text': ('Open', 'Open', 'High', 'Low',
                                                 'Close', 'Close', ''),
                                        'mode': 'lines',
                                        'type': 'scatter',
                                        'x': [-0.2, 0, 0, 0, 0, 0.2, None]
                                        }]
                              }
        self.assertEqual(ohlc_decr, expected_ohlc_decr)

    def test_one_candlestick(self):

        # This should create one "increase" (i.e. close > open) candlestick

        can_inc = tls.FigureFactory.create_candlestick(open=[33.0],
                                                       high=[33.2],
                                                       low=[32.7],
                                                       close=[33.1])

        expected_can_inc = {'layout': {'barmode': 'stack',
                                       'yaxis': {'range': [32.650000000000006,
                                                           33.25]}},
                            'data': [{'y': [33.0],
                                      'hoverinfo': 'none',
                                      'marker': {'color': 'rgba(0, 0, 0, 0)'},
                                      'showlegend': False,
                                      'type': 'bar',
                                      'x': [0],
                                      'legendgroup': 'Increasing'},
                                     {'y': [0.10000000000000142],
                                      'line': {'color': '#3D9970'},
                                      'hoverinfo': 'none',
                                      'marker': {'color': '#3D9970'},
                                      'showlegend': False,
                                      'legendgroup': 'Increasing',
                                      'name': 'Increasing',
                                      'type': 'bar', 'x': [0]},
                                     {'y': [32.7, 33.0, 33.1, 33.2, None],
                                      'line': {'color': '#3D9970'},
                                      'marker': {'color': '#3D9970'},
                                      'showlegend': False,
                                      'legendgroup': 'Increasing',
                                      'name': 'Increasing',
                                      'text': ('Low', 'Open', 'Close',
                                               'High', ''),
                                      'mode': 'lines',
                                      'type': 'scatter',
                                      'x': [0, 0, 0, 0, None]},
                                     {'y': [],
                                      'hoverinfo': 'none',
                                      'marker': {'color': 'rgba(0, 0, 0, 0)'},
                                      'showlegend': False, 'type': 'bar',
                                      'x': [],
                                      'legendgroup': 'Decreasing'},
                                     {'y': [],
                                      'line': {'color': '#FF4136'},
                                      'hoverinfo': 'none',
                                      'marker': {'color': '#FF4136'},
                                      'showlegend': False,
                                      'legendgroup': 'Decreasing',
                                      'name': 'Decreasing',
                                      'type': 'bar', 'x': []},
                                     {'y': [],
                                      'line': {'color': '#FF4136'},
                                      'marker': {'color': '#FF4136'},
                                      'showlegend': False,
                                      'legendgroup': 'Decreasing',
                                      'name': 'Decreasing',
                                      'text': (),
                                      'mode': 'lines',
                                      'type': 'scatter',
                                      'x': []}]}

        self.assertEqual(can_inc, expected_can_inc)

    def test_datetime_ohlc(self):

        # Check expected outcome for ohlc chart with datetime xaxis

        high_data = [34.20, 34.37, 33.62, 34.25, 35.18, 33.25, 35.37, 34.62]
        low_data = [31.70, 30.75, 32.87, 31.62, 30.81, 32.75, 32.75, 32.87]
        close_data = [34.10, 31.93, 33.37, 33.18, 31.18, 33.10, 32.93, 33.70]
        open_data = [33.01, 33.31, 33.50, 32.06, 34.12, 33.05, 33.31, 33.50]

        x = [datetime.datetime(year=2013, month=3, day=4),
             datetime.datetime(year=2013, month=6, day=5),
             datetime.datetime(year=2013, month=9, day=6),
             datetime.datetime(year=2013, month=12, day=4),
             datetime.datetime(year=2014, month=3, day=5),
             datetime.datetime(year=2014, month=6, day=6),
             datetime.datetime(year=2014, month=9, day=4),
             datetime.datetime(year=2014, month=12, day=5)]

        ohlc = tls.FigureFactory.create_ohlc(open_data, high_data,
                                             low_data, close_data,
                                             dates=x)

        exp_ohlc = {'layout': {'hovermode': 'closest',
                               'xaxis': {'zeroline': False}},
                    'data': [{'y': [33.01, 33.01, 34.2, 31.7, 34.1, 34.1, None,
                                    32.06, 32.06, 34.25, 31.62, 33.18, 33.18,
                                    None, 33.05, 33.05, 33.25, 32.75, 33.1,
                                    33.1, None, 33.5, 33.5, 34.62, 32.87, 33.7,
                                    33.7, None],
                              'line': {'color': '#3D9970'},
                              'showlegend': False, 'name': 'Increasing',
                              'text': ('Open', 'Open', 'High', 'Low', 'Close',
                                       'Close', '', 'Open', 'Open', 'High',
                                       'Low', 'Close', 'Close', '', 'Open',
                                       'Open', 'High', 'Low', 'Close', 'Close',
                                       '', 'Open', 'Open', 'High', 'Low',
                                       'Close', 'Close', ''), 'mode': 'lines',
                              'type': 'scatter',
                              'x': [datetime.datetime(2013, 2, 14, 4, 48),
                                    datetime.datetime(2013, 3, 4, 0, 0),
                                    datetime.datetime(2013, 3, 4, 0, 0),
                                    datetime.datetime(2013, 3, 4, 0, 0),
                                    datetime.datetime(2013, 3, 4, 0, 0),
                                    datetime.datetime(2013, 3, 21, 19, 12),
                                    None,
                                    datetime.datetime(2013, 11, 16, 4, 48),
                                    datetime.datetime(2013, 12, 4, 0, 0),
                                    datetime.datetime(2013, 12, 4, 0, 0),
                                    datetime.datetime(2013, 12, 4, 0, 0),
                                    datetime.datetime(2013, 12, 4, 0, 0),
                                    datetime.datetime(2013, 12, 21, 19, 12),
                                    None,
                                    datetime.datetime(2014, 5, 19, 4, 48),
                                    datetime.datetime(2014, 6, 6, 0, 0),
                                    datetime.datetime(2014, 6, 6, 0, 0),
                                    datetime.datetime(2014, 6, 6, 0, 0),
                                    datetime.datetime(2014, 6, 6, 0, 0),
                                    datetime.datetime(2014, 6, 23, 19, 12),
                                    None,
                                    datetime.datetime(2014, 11, 17, 4, 48),
                                    datetime.datetime(2014, 12, 5, 0, 0),
                                    datetime.datetime(2014, 12, 5, 0, 0),
                                    datetime.datetime(2014, 12, 5, 0, 0),
                                    datetime.datetime(2014, 12, 5, 0, 0),
                                    datetime.datetime(2014, 12, 22, 19, 12),
                                    None]},
                             {'y': [33.31, 33.31, 34.37, 30.75, 31.93, 31.93,
                                    None, 33.5, 33.5, 33.62, 32.87, 33.37,
                                    33.37, None, 34.12, 34.12, 35.18, 30.81,
                                    31.18, 31.18, None, 33.31, 33.31, 35.37,
                                    32.75, 32.93, 32.93, None],
                              'line': {'color': '#FF4136'},
                              'showlegend': False, 'name': 'Decreasing',
                              'text': ('Open', 'Open', 'High', 'Low', 'Close',
                                       'Close', '', 'Open', 'Open', 'High',
                                       'Low', 'Close', 'Close', '', 'Open',
                                       'Open', 'High', 'Low', 'Close', 'Close',
                                       '', 'Open', 'Open', 'High', 'Low',
                                       'Close', 'Close', ''), 'mode': 'lines',
                              'type': 'scatter',
                              'x': [datetime.datetime(2013, 5, 18, 4, 48),
                                    datetime.datetime(2013, 6, 5, 0, 0),
                                    datetime.datetime(2013, 6, 5, 0, 0),
                                    datetime.datetime(2013, 6, 5, 0, 0),
                                    datetime.datetime(2013, 6, 5, 0, 0),
                                    datetime.datetime(2013, 6, 22, 19, 12),
                                    None,
                                    datetime.datetime(2013, 8, 19, 4, 48),
                                    datetime.datetime(2013, 9, 6, 0, 0),
                                    datetime.datetime(2013, 9, 6, 0, 0),
                                    datetime.datetime(2013, 9, 6, 0, 0),
                                    datetime.datetime(2013, 9, 6, 0, 0),
                                    datetime.datetime(2013, 9, 23, 19, 12),
                                    None,
                                    datetime.datetime(2014, 2, 15, 4, 48),
                                    datetime.datetime(2014, 3, 5, 0, 0),
                                    datetime.datetime(2014, 3, 5, 0, 0),
                                    datetime.datetime(2014, 3, 5, 0, 0),
                                    datetime.datetime(2014, 3, 5, 0, 0),
                                    datetime.datetime(2014, 3, 22, 19, 12),
                                    None,
                                    datetime.datetime(2014, 8, 17, 4, 48),
                                    datetime.datetime(2014, 9, 4, 0, 0),
                                    datetime.datetime(2014, 9, 4, 0, 0),
                                    datetime.datetime(2014, 9, 4, 0, 0),
                                    datetime.datetime(2014, 9, 4, 0, 0),
                                    datetime.datetime(2014, 9, 21, 19, 12),
                                    None]}]}
        self.assertEqual(ohlc, exp_ohlc)

    def test_datetime_candlestick(self):

        # Check expected outcome for candlestick chart with datetime xaxis

        high_data = [34.20, 34.37, 33.62, 34.25, 35.18, 33.25, 35.37, 34.62]
        low_data = [31.70, 30.75, 32.87, 31.62, 30.81, 32.75, 32.75, 32.87]
        close_data = [34.10, 31.93, 33.37, 33.18, 31.18, 33.10, 32.93, 33.70]
        open_data = [33.01, 33.31, 33.50, 32.06, 34.12, 33.05, 33.31, 33.50]

        x = [datetime.datetime(year=2013, month=3, day=4),
             datetime.datetime(year=2013, month=6, day=5),
             datetime.datetime(year=2013, month=9, day=6),
             datetime.datetime(year=2013, month=12, day=4),
             datetime.datetime(year=2014, month=3, day=5),
             datetime.datetime(year=2014, month=6, day=6),
             datetime.datetime(year=2014, month=9, day=4),
             datetime.datetime(year=2014, month=12, day=5)]

        candle = tls.FigureFactory.create_candlestick(open_data, high_data,
                                                      low_data, close_data,
                                                      dates=x)

        exp_can = {'layout': {'barmode': 'stack',
                              'yaxis': {'range': [30.288,
                                                  35.831999999999994]}},
                   'data': [{'y': [33.01, 32.06, 33.05, 33.5],
                             'hoverinfo': 'none',
                             'marker': {'color': 'rgba(0, 0, 0, 0)'},
                             'showlegend': False,
                             'type': 'bar',
                             'x': [datetime.datetime(2013, 3, 4, 0, 0),
                                   datetime.datetime(2013, 12, 4, 0, 0),
                                   datetime.datetime(2014, 6, 6, 0, 0),
                                   datetime.datetime(2014, 12, 5, 0, 0)],
                             'legendgroup': 'Increasing'},
                            {'y': [1.0900000000000034, 1.1199999999999974,
                                   0.05000000000000426, 0.20000000000000284],
                             'line': {'color': '#3D9970'},
                             'hoverinfo': 'none',
                             'marker': {'color': '#3D9970'},
                             'showlegend': False,
                             'legendgroup': 'Increasing',
                             'name': 'Increasing',
                             'type': 'bar',
                             'x': [datetime.datetime(2013, 3, 4, 0, 0),
                                   datetime.datetime(2013, 12, 4, 0, 0),
                                   datetime.datetime(2014, 6, 6, 0, 0),
                                   datetime.datetime(2014, 12, 5, 0, 0)]},
                            {'y': [31.7, 33.01, 34.1, 34.2, None, 31.62, 32.06,
                                   33.18, 34.25, None, 32.75, 33.05, 33.1,
                                   33.25, None, 32.87, 33.5, 33.7, 34.62,
                                   None],
                             'line': {'color': '#3D9970'},
                             'marker': {'color': '#3D9970'},
                             'showlegend': False,
                             'legendgroup': 'Increasing',
                             'name': 'Increasing',
                             'text': ('Low', 'Open', 'Close', 'High', '',
                                      'Low', 'Open', 'Close', 'High', '',
                                      'Low', 'Open', 'Close', 'High', '',
                                      'Low', 'Open', 'Close', 'High', ''),
                             'mode': 'lines', 'type': 'scatter',
                             'x': [datetime.datetime(2013, 3, 4, 0, 0),
                                   datetime.datetime(2013, 3, 4, 0, 0),
                                   datetime.datetime(2013, 3, 4, 0, 0),
                                   datetime.datetime(2013, 3, 4, 0, 0), None,
                                   datetime.datetime(2013, 12, 4, 0, 0),
                                   datetime.datetime(2013, 12, 4, 0, 0),
                                   datetime.datetime(2013, 12, 4, 0, 0),
                                   datetime.datetime(2013, 12, 4, 0, 0),
                                   None, datetime.datetime(2014, 6, 6, 0, 0),
                                   datetime.datetime(2014, 6, 6, 0, 0),
                                   datetime.datetime(2014, 6, 6, 0, 0),
                                   datetime.datetime(2014, 6, 6, 0, 0), None,
                                   datetime.datetime(2014, 12, 5, 0, 0),
                                   datetime.datetime(2014, 12, 5, 0, 0),
                                   datetime.datetime(2014, 12, 5, 0, 0),
                                   datetime.datetime(2014, 12, 5, 0, 0),
                                   None]},
                            {'y': [31.93, 33.37, 31.18, 32.93],
                             'hoverinfo': 'none',
                             'marker': {'color': 'rgba(0, 0, 0, 0)'},
                             'showlegend': False, 'type': 'bar',
                             'x': [datetime.datetime(2013, 6, 5, 0, 0),
                                   datetime.datetime(2013, 9, 6, 0, 0),
                                   datetime.datetime(2014, 3, 5, 0, 0),
                                   datetime.datetime(2014, 9, 4, 0, 0)],
                             'legendgroup': 'Decreasing'},
                            {'y': [1.3800000000000026, 0.13000000000000256,
                                   2.9399999999999977, 0.38000000000000256],
                             'line': {'color': '#FF4136'},
                             'hoverinfo': 'none',
                             'marker': {'color': '#FF4136'},
                             'showlegend': False, 'legendgroup': 'Decreasing',
                             'name': 'Decreasing', 'type': 'bar',
                             'x': [datetime.datetime(2013, 6, 5, 0, 0),
                                   datetime.datetime(2013, 9, 6, 0, 0),
                                   datetime.datetime(2014, 3, 5, 0, 0),
                                   datetime.datetime(2014, 9, 4, 0, 0)]},
                            {'y': [30.75, 31.93, 33.31, 34.37, None, 32.87,
                                   33.37, 33.5, 33.62, None, 30.81, 31.18,
                                   34.12, 35.18, None, 32.75, 32.93, 33.31,
                                   35.37, None],
                             'line': {'color': '#FF4136'},
                             'marker': {'color': '#FF4136'},
                             'showlegend': False, 'legendgroup': 'Decreasing',
                             'name': 'Decreasing',
                             'text': ('Low', 'Close', 'Open', 'High', '',
                                      'Low', 'Close', 'Open', 'High', '',
                                      'Low', 'Close', 'Open', 'High', '',
                                      'Low', 'Close', 'Open', 'High', ''),
                             'mode': 'lines', 'type': 'scatter',
                             'x': [datetime.datetime(2013, 6, 5, 0, 0),
                                   datetime.datetime(2013, 6, 5, 0, 0),
                                   datetime.datetime(2013, 6, 5, 0, 0),
                                   datetime.datetime(2013, 6, 5, 0, 0), None,
                                   datetime.datetime(2013, 9, 6, 0, 0),
                                   datetime.datetime(2013, 9, 6, 0, 0),
                                   datetime.datetime(2013, 9, 6, 0, 0),
                                   datetime.datetime(2013, 9, 6, 0, 0), None,
                                   datetime.datetime(2014, 3, 5, 0, 0),
                                   datetime.datetime(2014, 3, 5, 0, 0),
                                   datetime.datetime(2014, 3, 5, 0, 0),
                                   datetime.datetime(2014, 3, 5, 0, 0), None,
                                   datetime.datetime(2014, 9, 4, 0, 0),
                                   datetime.datetime(2014, 9, 4, 0, 0),
                                   datetime.datetime(2014, 9, 4, 0, 0),
                                   datetime.datetime(2014, 9, 4, 0, 0),
                                   None]}]}
        self.assertEqual(candle, exp_can)

