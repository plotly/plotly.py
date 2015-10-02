import math
from unittest import TestCase

import datetime
from nose.tools import raises
import plotly.tools as tls
from plotly.exceptions import PlotlyError
from plotly.graph_objs import graph_objs


class TestQuiver(TestCase):

    def test_unequal_xy_length(self):

        # check: PlotlyError if x and y are not the same length

        kwargs = {'x': [1, 2], 'y': [1], 'u': [1, 2], 'v': [1, 2]}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_quiver,
                          **kwargs)

    def test_wrong_scale(self):

        # check: ValueError if scale is <= 0

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'scale': -1}
        self.assertRaises(ValueError, tls.FigureFactory.create_quiver,
                          **kwargs)

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'scale': 0}
        self.assertRaises(ValueError, tls.FigureFactory.create_quiver,
                          **kwargs)

    def test_wrong_arrow_scale(self):

        # check: ValueError if arrow_scale is <= 0

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'arrow_scale': -1}
        self.assertRaises(ValueError, tls.FigureFactory.create_quiver,
                          **kwargs)

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'arrow_scale': 0}
        self.assertRaises(ValueError, tls.FigureFactory.create_quiver,
                          **kwargs)

    def test_one_arrow(self):

        # we should be able to create a single arrow using create_quiver

        quiver = tls.FigureFactory.create_quiver(x=[1], y=[1],
                                                 u=[1], v=[1],
                                                 scale=1)
        expected_quiver = {
            'data': [{'mode': 'lines',
                      'type': u'scatter',
                      'x': [1, 2, None, 1.820698256761928, 2,
                            1.615486170766527, None],
                      'y': [1, 2, None, 1.615486170766527, 2,
                            1.820698256761928, None]}],
            'layout': {'hovermode': 'closest'}}
        self.assertEqual(quiver, expected_quiver)

    def test_more_kwargs(self):

        # we should be able to create 2 arrows and change the arrow_scale,
        # angle, and arrow using create_quiver

        quiver = tls.FigureFactory.create_quiver(x=[1, 2],
                                                 y=[1, 2],
                                                 u=[math.cos(1),
                                                    math.cos(2)],
                                                 v=[math.sin(1),
                                                    math.sin(2)],
                                                 arrow_scale=.4,
                                                 angle=math.pi / 6,
                                                 line=graph_objs.Line(color='purple',
                                                                      width=3))
        expected_quiver = {'data': [{'line': {'color': 'purple', 'width': 3},
                                     'mode': 'lines',
                                     'type': u'scatter',
                                     'x': [1,
                                           1.0540302305868139,
                                           None,
                                           2,
                                           1.9583853163452858,
                                           None,
                                           1.052143029378767,
                                           1.0540302305868139,
                                           1.0184841899864512,
                                           None,
                                           1.9909870141679737,
                                           1.9583853163452858,
                                           1.9546151170949464,
                                           None],
                                     'y': [1,
                                           1.0841470984807897,
                                           None,
                                           2,
                                           2.0909297426825684,
                                           None,
                                           1.044191642387781,
                                           1.0841470984807897,
                                           1.0658037346225067,
                                           None,
                                           2.0677536925644366,
                                           2.0909297426825684,
                                           2.051107819102551,
                                           None]}],
                           'layout': {'hovermode': 'closest'}}
        self.assertEqual(quiver, expected_quiver)


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

        ohlc = tls.FigureFactory.create_ohlc(open=[33.0],
                                             high=[33.2],
                                             low=[32.7],
                                             close=[33.1])

        expected_ohlc = {'layout': {'hovermode': 'closest',
                                    'xaxis': {'zeroline': False}},
                         'data': [{'y': [33.0, 33.0, 33.2, 32.7,
                                         33.1, 33.1, None],
                                   'line': {'width': 1,
                                            'color': '#3D9970'},
                                   'showlegend': False,
                                   'name': 'Increasing',
                                   'text': ('Open', 'Open', 'High', 'Low',
                                            'Close', 'Close', ''),
                                   'mode': 'lines', 'type': 'scatter',
                                   'x': [-0.2, 0, 0, 0, 0, 0.2, None]},
                                  {'y': [], 'line': {'width': 1,
                                                     'color': '#FF4136'},
                                   'showlegend': False,
                                   'name': 'Decreasing', 'text': (),
                                   'mode': 'lines', 'type': 'scatter',
                                   'x': []}]}

        self.assertEqual(ohlc, expected_ohlc)

    def test_one_ohlc_increase(self):

        # This should create one "increase" (i.e. close > open) ohlc stick

        ohlc_incr = tls.FigureFactory.create_ohlc(open=[33.0],
                                                  high=[33.2],
                                                  low=[32.7],
                                                  close=[33.1],
                                                  direction="increasing")

        expected_ohlc_incr = {'data': [{'line': {'color': '#3D9970',
                                                 'width': 1},
                                        'mode': 'lines',
                                        'name': 'Increasing',
                                        'showlegend': False,
                                        'text': ('Open', 'Open', 'High',
                                                 'Low', 'Close', 'Close', ''),
                                        'type': 'scatter',
                                        'x': [-0.2, 0, 0, 0, 0, 0.2, None],
                                        'y': [33.0, 33.0, 33.2, 32.7, 33.1,
                                              33.1, None]}],
                              'layout': {'hovermode': 'closest',
                                         'xaxis': {'zeroline': False}}}
        self.assertEqual(ohlc_incr, expected_ohlc_incr)

    def test_one_ohlc_decrease(self):

        # This should create one "increase" (i.e. close > open) ohlc stick

        ohlc_decr = tls.FigureFactory.create_ohlc(open=[33.0],
                                                  high=[33.2],
                                                  low=[30.7],
                                                  close=[31.1],
                                                  direction="decreasing")

        expected_ohlc_decr = {'data': [{'line': {'color': '#FF4136',
                                                 'width': 1},
                                        'mode': 'lines',
                                        'name': 'Decreasing',
                                        'showlegend': False,
                                        'text': ('Open', 'Open', 'High', 'Low',
                                                 'Close', 'Close', ''),
                                        'type': 'scatter',
                                        'x': [-0.2, 0, 0, 0, 0, 0.2, None],
                                        'y': [33.0, 33.0, 33.2, 30.7, 31.1,
                                              31.1, None]}],
                              'layout': {'hovermode': 'closest',
                                         'xaxis': {'zeroline': False}}}
        self.assertEqual(ohlc_decr, expected_ohlc_decr)

    # TO-DO: put expected fig in a different file and then call to compare
    def test_one_candlestick(self):

        # This should create one "increase" (i.e. close > open) candlestick

        can_inc = tls.FigureFactory.create_candlestick(open=[33.0],
                                                       high=[33.2],
                                                       low=[32.7],
                                                       close=[33.1])

        exp_can_inc = {'data': [{'boxpoints': False,
                                 'fillcolor': '#3D9970',
                                 'line': {'color': '#3D9970'},
                                 'name': 'Increasing',
                                 'showlegend': False,
                                 'type': 'box',
                                 'whiskerwidth': 0,
                                 'x': [0, 0, 0, 0, 0, 0],
                                 'y': [32.7, 33.0, 33.1, 33.1, 33.1, 33.2]},
                                {'boxpoints': False,
                                 'fillcolor': '#FF4136',
                                 'line': {'color': '#FF4136'},
                                 'name': 'Decreasing',
                                 'showlegend': False,
                                 'type': 'box',
                                 'whiskerwidth': 0,
                                 'x': [],
                                 'y': []}],
                       'layout': {}}

        self.assertEqual(can_inc, exp_can_inc)

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

        ohlc_d = tls.FigureFactory.create_ohlc(open_data, high_data,
                                               low_data, close_data,
                                               dates=x)

        ex_ohlc_d = {'data': [{'line': {'color': '#3D9970', 'width': 1},
                               'mode': 'lines',
                               'name': 'Increasing',
                               'showlegend': False,
                               'text': ('Open',
                                        'Open',
                                        'High',
                                        'Low',
                                        'Close',
                                        'Close',
                                        '',
                                        'Open',
                                        'Open',
                                        'High',
                                        'Low',
                                        'Close',
                                        'Close',
                                        '',
                                        'Open',
                                        'Open',
                                        'High',
                                        'Low',
                                        'Close',
                                        'Close',
                                        '',
                                        'Open',
                                        'Open',
                                        'High',
                                        'Low',
                                        'Close',
                                        'Close',
                                        ''),
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
                                     None],
                               'y': [33.01,
                                     33.01,
                                     34.2,
                                     31.7,
                                     34.1,
                                     34.1,
                                     None,
                                     32.06,
                                     32.06,
                                     34.25,
                                     31.62,
                                     33.18,
                                     33.18,
                                     None,
                                     33.05,
                                     33.05,
                                     33.25,
                                     32.75,
                                     33.1,
                                     33.1,
                                     None,
                                     33.5,
                                     33.5,
                                     34.62,
                                     32.87,
                                     33.7,
                                     33.7,
                                     None]},
                              {'line': {'color': '#FF4136', 'width': 1},
                               'mode': 'lines',
                               'name': 'Decreasing',
                               'showlegend': False,
                               'text': ('Open',
                                        'Open',
                                        'High',
                                        'Low',
                                        'Close',
                                        'Close',
                                        '',
                                        'Open',
                                        'Open',
                                        'High',
                                        'Low',
                                        'Close',
                                        'Close',
                                        '',
                                        'Open',
                                        'Open',
                                        'High',
                                        'Low',
                                        'Close',
                                        'Close',
                                        '',
                                        'Open',
                                        'Open',
                                        'High',
                                        'Low',
                                        'Close',
                                        'Close',
                                        ''),
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
                                     None],
                               'y': [33.31,
                                     33.31,
                                     34.37,
                                     30.75,
                                     31.93,
                                     31.93,
                                     None,
                                     33.5,
                                     33.5,
                                     33.62,
                                     32.87,
                                     33.37,
                                     33.37,
                                     None,
                                     34.12,
                                     34.12,
                                     35.18,
                                     30.81,
                                     31.18,
                                     31.18,
                                     None,
                                     33.31,
                                     33.31,
                                     35.37,
                                     32.75,
                                     32.93,
                                     32.93,
                                     None]}],
                     'layout': {'hovermode': 'closest',
                                'xaxis': {'zeroline': False}}}
        self.assertEqual(ohlc_d, ex_ohlc_d)

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
        exp_candle = {'data': [{'boxpoints': False,
                                'fillcolor': '#3D9970',
                                'line': {'color': '#3D9970'},
                                'name': 'Increasing',
                                'showlegend': False,
                                'type': 'box',
                                'whiskerwidth': 0,
                                'x': [datetime.datetime(2013, 3, 4, 0, 0),
                                      datetime.datetime(2013, 3, 4, 0, 0),
                                      datetime.datetime(2013, 3, 4, 0, 0),
                                      datetime.datetime(2013, 3, 4, 0, 0),
                                      datetime.datetime(2013, 3, 4, 0, 0),
                                      datetime.datetime(2013, 3, 4, 0, 0),
                                      datetime.datetime(2013, 12, 4, 0, 0),
                                      datetime.datetime(2013, 12, 4, 0, 0),
                                      datetime.datetime(2013, 12, 4, 0, 0),
                                      datetime.datetime(2013, 12, 4, 0, 0),
                                      datetime.datetime(2013, 12, 4, 0, 0),
                                      datetime.datetime(2013, 12, 4, 0, 0),
                                      datetime.datetime(2014, 6, 6, 0, 0),
                                      datetime.datetime(2014, 6, 6, 0, 0),
                                      datetime.datetime(2014, 6, 6, 0, 0),
                                      datetime.datetime(2014, 6, 6, 0, 0),
                                      datetime.datetime(2014, 6, 6, 0, 0),
                                      datetime.datetime(2014, 6, 6, 0, 0),
                                      datetime.datetime(2014, 12, 5, 0, 0),
                                      datetime.datetime(2014, 12, 5, 0, 0),
                                      datetime.datetime(2014, 12, 5, 0, 0),
                                      datetime.datetime(2014, 12, 5, 0, 0),
                                      datetime.datetime(2014, 12, 5, 0, 0),
                                      datetime.datetime(2014, 12, 5, 0, 0)],
                               'y': [31.7,
                                     33.01,
                                     34.1,
                                     34.1,
                                     34.1,
                                     34.2,
                                     31.62,
                                     32.06,
                                     33.18,
                                     33.18,
                                     33.18,
                                     34.25,
                                     32.75,
                                     33.05,
                                     33.1,
                                     33.1,
                                     33.1,
                                     33.25,
                                     32.87,
                                     33.5,
                                     33.7,
                                     33.7,
                                     33.7,
                                     34.62]},
                               {'boxpoints': False,
                                'fillcolor': '#FF4136',
                                'line': {'color': '#FF4136'},
                                'name': 'Decreasing',
                                'showlegend': False,
                                'type': 'box',
                                'whiskerwidth': 0,
                                'x': [datetime.datetime(2013, 6, 5, 0, 0),
                                      datetime.datetime(2013, 6, 5, 0, 0),
                                      datetime.datetime(2013, 6, 5, 0, 0),
                                      datetime.datetime(2013, 6, 5, 0, 0),
                                      datetime.datetime(2013, 6, 5, 0, 0),
                                      datetime.datetime(2013, 6, 5, 0, 0),
                                      datetime.datetime(2013, 9, 6, 0, 0),
                                      datetime.datetime(2013, 9, 6, 0, 0),
                                      datetime.datetime(2013, 9, 6, 0, 0),
                                      datetime.datetime(2013, 9, 6, 0, 0),
                                      datetime.datetime(2013, 9, 6, 0, 0),
                                      datetime.datetime(2013, 9, 6, 0, 0),
                                      datetime.datetime(2014, 3, 5, 0, 0),
                                      datetime.datetime(2014, 3, 5, 0, 0),
                                      datetime.datetime(2014, 3, 5, 0, 0),
                                      datetime.datetime(2014, 3, 5, 0, 0),
                                      datetime.datetime(2014, 3, 5, 0, 0),
                                      datetime.datetime(2014, 3, 5, 0, 0),
                                      datetime.datetime(2014, 9, 4, 0, 0),
                                      datetime.datetime(2014, 9, 4, 0, 0),
                                      datetime.datetime(2014, 9, 4, 0, 0),
                                      datetime.datetime(2014, 9, 4, 0, 0),
                                      datetime.datetime(2014, 9, 4, 0, 0),
                                      datetime.datetime(2014, 9, 4, 0, 0)],
                                'y': [30.75,
                                      33.31,
                                      31.93,
                                      31.93,
                                      31.93,
                                      34.37,
                                      32.87,
                                      33.5,
                                      33.37,
                                      33.37,
                                      33.37,
                                      33.62,
                                      30.81,
                                      34.12,
                                      31.18,
                                      31.18,
                                      31.18,
                                      35.18,
                                      32.75,
                                      33.31,
                                      32.93,
                                      32.93,
                                      32.93,
                                      35.37]}],
                      'layout': {}}

        self.assertEqual(candle, exp_candle)


# class TestDistplot(TestCase):

#     def test_scipy_import_error(self):

#         # make sure Import Error is raised when _scipy_imported = False

#         hist_data = [[1.1, 1.1, 2.5, 3.0, 3.5,
#                       3.5, 4.1, 4.4, 4.5, 4.5,
#                       5.0, 5.0, 5.2, 5.5, 5.5,
#                       5.5, 5.5, 5.5, 6.1, 7.0]]

#         group_labels = ['distplot example']

#         self.assertRaisesRegexp(ImportError,
#                                 "FigureFactory.create_distplot requires scipy",
#                                 tls.FigureFactory.create_distplot,
#                                 hist_data, group_labels)

