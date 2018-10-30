import math
from unittest import TestCase

import datetime
import plotly.figure_factory as ff

from plotly.exceptions import PlotlyError
from plotly.tests.test_optional.optional_utils import NumpyTestUtilsMixin
from plotly.graph_objs import graph_objs


class TestQuiver(TestCase, NumpyTestUtilsMixin):

    def test_unequal_xy_length(self):

        # check: PlotlyError if x and y are not the same length

        kwargs = {'x': [1, 2], 'y': [1], 'u': [1, 2], 'v': [1, 2]}
        self.assertRaises(PlotlyError, ff.create_quiver,
                          **kwargs)

    def test_wrong_scale(self):

        # check: ValueError if scale is <= 0

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'scale': -1}
        self.assertRaises(ValueError, ff.create_quiver,
                          **kwargs)

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'scale': 0}
        self.assertRaises(ValueError, ff.create_quiver,
                          **kwargs)

    def test_wrong_arrow_scale(self):

        # check: ValueError if arrow_scale is <= 0

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'arrow_scale': -1}
        self.assertRaises(ValueError, ff.create_quiver,
                          **kwargs)

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'arrow_scale': 0}
        self.assertRaises(ValueError, ff.create_quiver,
                          **kwargs)

    def test_one_arrow(self):

        # we should be able to create a single arrow using create_quiver

        quiver = ff.create_quiver(x=[1], y=[1],
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
        self.assert_fig_equal(quiver['data'][0],
                              expected_quiver['data'][0])
        self.assert_fig_equal(quiver['layout'],
                              expected_quiver['layout'])

    def test_more_kwargs(self):

        # we should be able to create 2 arrows and change the arrow_scale,
        # angle, and arrow using create_quiver

        quiver = ff.create_quiver(x=[1, 2],
                                  y=[1, 2],
                                  u=[math.cos(1),
                                     math.cos(2)],
                                  v=[math.sin(1),
                                     math.sin(2)],
                                  arrow_scale=.4,
                                  angle=math.pi / 6,
                                  line=graph_objs.scatter.Line(color='purple',
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
        self.assert_fig_equal(quiver['data'][0],
                              expected_quiver['data'][0])
        self.assert_fig_equal(quiver['layout'],
                              expected_quiver['layout'])


class TestFinanceCharts(TestCase, NumpyTestUtilsMixin):

    def test_unequal_ohlc_length(self):

        # check: PlotlyError if open, high, low, close are not the same length
        # for TraceFactory.create_ohlc and TraceFactory.create_candlestick

        kwargs = {'open': [1], 'high': [1, 3],
                  'low': [1, 2], 'close': [1, 2],
                  'direction': ['increasing']}
        self.assertRaises(PlotlyError, ff.create_ohlc, **kwargs)
        self.assertRaises(PlotlyError, ff.create_candlestick,
                          **kwargs)

        kwargs = {'open': [1, 2], 'high': [1, 2, 3],
                  'low': [1, 2], 'close': [1, 2],
                  'direction': ['decreasing']}
        self.assertRaises(PlotlyError, ff.create_ohlc, **kwargs)
        self.assertRaises(PlotlyError, ff.create_candlestick,
                          **kwargs)

        kwargs = {'open': [1, 2], 'high': [2, 3],
                  'low': [0], 'close': [1, 3]}
        self.assertRaises(PlotlyError, ff.create_ohlc, **kwargs)
        self.assertRaises(PlotlyError, ff.create_candlestick,
                          **kwargs)

        kwargs = {'open': [1, 2], 'high': [2, 3],
                  'low': [1, 2], 'close': [1]}
        self.assertRaises(PlotlyError, ff.create_ohlc, **kwargs)
        self.assertRaises(PlotlyError, ff.create_candlestick,
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
                                ff.create_ohlc, **kwargs)
        self.assertRaisesRegexp(PlotlyError,
                                "direction must be defined as "
                                "'increasing', 'decreasing', or 'both'",
                                ff.create_candlestick, **kwargs)

        kwargs = {'open': [1, 2], 'high': [1, 3],
                  'low': [1, 2], 'close': [1, 2],
                  'direction': ['d']}
        self.assertRaisesRegexp(PlotlyError,
                                "direction must be defined as "
                                "'increasing', 'decreasing', or 'both'",
                                ff.create_ohlc, **kwargs)
        self.assertRaisesRegexp(PlotlyError,
                                "direction must be defined as "
                                "'increasing', 'decreasing', or 'both'",
                                ff.create_candlestick, **kwargs)

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
                                ff.create_ohlc,
                                **kwargs)
        self.assertRaisesRegexp(PlotlyError, "Oops! Looks like some of "
                                             "your high values are less "
                                             "the corresponding open, "
                                             "low, or close values. "
                                             "Double check that your data "
                                             "is entered in O-H-L-C order",
                                ff.create_candlestick,
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
                                ff.create_ohlc,
                                **kwargs)
        self.assertRaisesRegexp(PlotlyError,
                                "Oops! Looks like some of "
                                "your low values are greater "
                                "than the corresponding high"
                                ", open, or close values. "
                                "Double check that your data "
                                "is entered in O-H-L-C order",
                                ff.create_candlestick,
                                **kwargs)

    def test_one_ohlc(self):

        # This should create one "increase" (i.e. close > open) ohlc stick

        ohlc = ff.create_ohlc(open=[33.0],
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
                                   'text': ['Open', 'Open', 'High', 'Low',
                                            'Close', 'Close', ''],
                                   'mode': 'lines', 'type': 'scatter',
                                   'x': [-0.2, 0, 0, 0, 0, 0.2, None]},
                                  {'y': [], 'line': {'width': 1,
                                                     'color': '#FF4136'},
                                   'showlegend': False,
                                   'name': 'Decreasing', 'text': (),
                                   'mode': 'lines', 'type': 'scatter',
                                   'x': []}]}

        self.assert_fig_equal(ohlc['data'][0],
                              expected_ohlc['data'][0],
                              ignore=['uid', 'text'])

        self.assert_fig_equal(ohlc['data'][1],
                              expected_ohlc['data'][1],
                              ignore=['uid', 'text'])

        self.assert_fig_equal(ohlc['layout'],
                              expected_ohlc['layout'])

    def test_one_ohlc_increase(self):

        # This should create one "increase" (i.e. close > open) ohlc stick

        ohlc_incr = ff.create_ohlc(open=[33.0],
                                                  high=[33.2],
                                                  low=[32.7],
                                                  close=[33.1],
                                                  direction="increasing")

        expected_ohlc_incr = {'data': [{'line': {'color': '#3D9970',
                                                 'width': 1},
                                        'mode': 'lines',
                                        'name': 'Increasing',
                                        'showlegend': False,
                                        'text': ['Open', 'Open', 'High',
                                                 'Low', 'Close', 'Close', ''],
                                        'type': 'scatter',
                                        'x': [-0.2, 0, 0, 0, 0, 0.2, None],
                                        'y': [33.0, 33.0, 33.2, 32.7, 33.1,
                                              33.1, None]}],
                              'layout': {'hovermode': 'closest',
                                         'xaxis': {'zeroline': False}}}
        self.assert_fig_equal(ohlc_incr['data'][0], expected_ohlc_incr['data'][0])
        self.assert_fig_equal(ohlc_incr['layout'], expected_ohlc_incr['layout'])

    def test_one_ohlc_decrease(self):

        # This should create one "increase" (i.e. close > open) ohlc stick

        ohlc_decr = ff.create_ohlc(open=[33.0],
                                                  high=[33.2],
                                                  low=[30.7],
                                                  close=[31.1],
                                                  direction="decreasing")

        expected_ohlc_decr = {'data': [{'line': {'color': '#FF4136',
                                                 'width': 1},
                                        'mode': 'lines',
                                        'name': 'Decreasing',
                                        'showlegend': False,
                                        'text': ['Open', 'Open', 'High', 'Low',
                                                 'Close', 'Close', ''],
                                        'type': 'scatter',
                                        'x': [-0.2, 0, 0, 0, 0, 0.2, None],
                                        'y': [33.0, 33.0, 33.2, 30.7, 31.1,
                                              31.1, None]}],
                              'layout': {'hovermode': 'closest',
                                         'xaxis': {'zeroline': False}}}

        self.assert_fig_equal(ohlc_decr['data'][0], expected_ohlc_decr['data'][0])
        self.assert_fig_equal(ohlc_decr['layout'], expected_ohlc_decr['layout'])

    # TO-DO: put expected fig in a different file and then call to compare
    def test_one_candlestick(self):

        # This should create one "increase" (i.e. close > open) candlestick

        can_inc = ff.create_candlestick(open=[33.0],
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
                                 'fillcolor': '#ff4136',
                                 'line': {'color': '#ff4136'},
                                 'name': 'Decreasing',
                                 'showlegend': False,
                                 'type': 'box',
                                 'whiskerwidth': 0,
                                 'x': [],
                                 'y': []}],
                       'layout': {}}

        self.assert_fig_equal(can_inc['data'][0],
                              exp_can_inc['data'][0])
        self.assert_fig_equal(can_inc['layout'],
                              exp_can_inc['layout'])

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

        ohlc_d = ff.create_ohlc(open_data, high_data,
                                               low_data, close_data,
                                               dates=x)

        ex_ohlc_d = {'data': [{'line': {'color': '#3D9970', 'width': 1},
                               'mode': 'lines',
                               'name': 'Increasing',
                               'showlegend': False,
                               'text': ['Open',
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
                                        ''],
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
                               'text': ['Open',
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
                                        ''],
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
        self.assert_fig_equal(ohlc_d['data'][0], ex_ohlc_d['data'][0])
        self.assert_fig_equal(ohlc_d['data'][1], ex_ohlc_d['data'][1])
        self.assert_fig_equal(ohlc_d['layout'], ex_ohlc_d['layout'])

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

        candle = ff.create_candlestick(open_data, high_data,
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

        self.assert_fig_equal(candle['data'][0], exp_candle['data'][0])
        self.assert_fig_equal(candle['data'][1], exp_candle['data'][1])
        self.assert_fig_equal(candle['layout'], exp_candle['layout'])


class TestAnnotatedHeatmap(TestCase, NumpyTestUtilsMixin):

    def test_unequal_z_text_size(self):

        # check: PlotlyError if z and text are not the same dimensions

        kwargs = {'z': [[1, 2], [1, 2]], 'annotation_text': [[1, 2, 3], [1]]}
        self.assertRaises(PlotlyError,
                          ff.create_annotated_heatmap,
                          **kwargs)

        kwargs = {'z': [[1], [1]], 'annotation_text': [[1], [1], [1]]}
        self.assertRaises(PlotlyError,
                          ff.create_annotated_heatmap,
                          **kwargs)

    def test_incorrect_x_size(self):

        # check: PlotlyError if x is the wrong size

        kwargs = {'z': [[1, 2], [1, 2]], 'x': ['A']}
        self.assertRaises(PlotlyError,
                          ff.create_annotated_heatmap,
                          **kwargs)

    def test_incorrect_y_size(self):

        # check: PlotlyError if y is the wrong size

        kwargs = {'z': [[1, 2], [1, 2]], 'y': [1, 2, 3]}
        self.assertRaises(PlotlyError,
                          ff.create_annotated_heatmap,
                          **kwargs)

    def test_simple_annotated_heatmap(self):

        # we should be able to create a heatmap with annotated values with a
        # logical text color

        z = [[1, 0, .5], [.25, .75, .45]]
        a_heat = ff.create_annotated_heatmap(z)
        expected_a_heat = {
            'data': [{'colorscale': 'RdBu',
                      'showscale': False,
                      'reversescale': False,
                      'type': 'heatmap',
                      'z': [[1, 0, 0.5], [0.25, 0.75, 0.45]]}],
            'layout': {'annotations': [{'font': {'color': '#000000'},
                                        'showarrow': False,
                                        'text': '1',
                                        'x': 0,
                                        'xref': 'x',
                                        'y': 0,
                                        'yref': 'y'},
                                       {'font': {'color': '#FFFFFF'},
                                        'showarrow': False,
                                        'text': '0',
                                        'x': 1,
                                        'xref': 'x',
                                        'y': 0,
                                        'yref': 'y'},
                                       {'font': {'color': '#FFFFFF'},
                                        'showarrow': False,
                                        'text': '0.5',
                                        'x': 2,
                                        'xref': 'x',
                                        'y': 0,
                                        'yref': 'y'},
                                       {'font': {'color': '#FFFFFF'},
                                        'showarrow': False,
                                        'text': '0.25',
                                        'x': 0,
                                        'xref': 'x',
                                        'y': 1,
                                        'yref': 'y'},
                                       {'font': {'color': '#000000'},
                                        'showarrow': False,
                                        'text': '0.75',
                                        'x': 1,
                                        'xref': 'x',
                                        'y': 1,
                                        'yref': 'y'},
                                       {'font': {'color': '#FFFFFF'},
                                        'showarrow': False,
                                        'text': '0.45',
                                        'x': 2,
                                        'xref': 'x',
                                        'y': 1,
                                        'yref': 'y'}],
                       'xaxis': {'gridcolor': 'rgb(0, 0, 0)',
                                 'showticklabels': False,
                                 'side': 'top',
                                 'ticks': ''},
                       'yaxis': {'showticklabels': False, 'ticks': '',
                                 'ticksuffix': '  '}}}

        self.assert_fig_equal(
            a_heat['data'][0],
            expected_a_heat['data'][0],
        )

        self.assert_fig_equal(a_heat['layout'],
                              expected_a_heat['layout'])

    def test_annotated_heatmap_kwargs(self):

        # we should be able to create an annotated heatmap with x and y axes
        # lables, a defined colorscale, and supplied text.

        z = [[1, 0], [.25, .75], [.45, .5]]
        text = [['first', 'second'], ['third', 'fourth'], ['fifth', 'sixth']]
        a = ff.create_annotated_heatmap(z,
                                        x=['A', 'B'],
                                        y=['One', 'Two', 'Three'],
                                        annotation_text=text,
                                        colorscale=[[0, 'rgb(255,255,255)'],
                                                    [1, '#e6005a']])
        expected_a = {'data': [{'colorscale':
                                    [[0, 'rgb(255,255,255)'], [1, '#e6005a']],
                                'showscale': False,
                                'reversescale': False,
                                'type': 'heatmap',
                                'x': ['A', 'B'],
                                'y': ['One', 'Two', 'Three'],
                                'z': [[1, 0], [0.25, 0.75], [0.45, 0.5]]}],
                      'layout': {'annotations': [{'font': {'color': '#FFFFFF'},
                                                  'showarrow': False,
                                                  'text': 'first',
                                                  'x': 'A',
                                                  'xref': 'x',
                                                  'y': 'One',
                                                  'yref': 'y'},
                                 {'font': {'color': '#000000'},
                                  'showarrow': False,
                                  'text': 'second',
                                  'x': 'B',
                                  'xref': 'x',
                                  'y': 'One',
                                  'yref': 'y'},
                                 {'font': {'color': '#000000'},
                                  'showarrow': False,
                                  'text': 'third',
                                  'x': 'A',
                                  'xref': 'x',
                                  'y': 'Two',
                                  'yref': 'y'},
                                 {'font': {'color': '#FFFFFF'},
                                  'showarrow': False,
                                  'text': 'fourth',
                                  'x': 'B',
                                  'xref': 'x',
                                  'y': 'Two',
                                  'yref': 'y'},
                                 {'font': {'color': '#000000'},
                                  'showarrow': False,
                                  'text': 'fifth',
                                  'x': 'A',
                                  'xref': 'x',
                                  'y': 'Three',
                                  'yref': 'y'},
                                 {'font': {'color': '#000000'},
                                  'showarrow': False,
                                  'text': 'sixth',
                                  'x': 'B',
                                  'xref': 'x',
                                  'y': 'Three',
                                  'yref': 'y'}],
                                 'xaxis': {'dtick': 1,
                                           'gridcolor': 'rgb(0, 0, 0)',
                                           'side': 'top',
                                           'ticks': ''},
                                 'yaxis': {'dtick': 1, 'ticks': '',
                                           'ticksuffix': '  '}}}
        self.assert_fig_equal(
            a['data'][0],
            expected_a['data'][0],
        )

        self.assert_fig_equal(a['layout'],
                              expected_a['layout'])

    def test_annotated_heatmap_reversescale(self):

        # we should be able to create an annotated heatmap with x and y axes
        # lables, a defined colorscale, and supplied text.

        z = [[1, 0], [.25, .75], [.45, .5]]
        text = [['first', 'second'], ['third', 'fourth'], ['fifth', 'sixth']]
        a = ff.create_annotated_heatmap(z,
                                        x=['A', 'B'],
                                        y=['One', 'Two', 'Three'],
                                        annotation_text=text,
                                        reversescale=True,
                                        colorscale=[[0, 'rgb(255,255,255)'],
                                                    [1, '#e6005a']])
        expected_a = {'data': [{'colorscale':
                                    [[0, 'rgb(255,255,255)'], [1, '#e6005a']],
                                'showscale': False,
                                'reversescale': True,
                                'type': 'heatmap',
                                'x': ['A', 'B'],
                                'y': ['One', 'Two', 'Three'],
                                'z': [[1, 0], [0.25, 0.75], [0.45, 0.5]]}],
                      'layout': {'annotations': [
                          {'font': {'color': '#000000'},
                           'showarrow': False,
                           'text': 'first',
                           'x': 'A',
                           'xref': 'x',
                           'y': 'One',
                           'yref': 'y'},
                          {'font': {'color': '#FFFFFF'},
                           'showarrow': False,
                           'text': 'second',
                           'x': 'B',
                           'xref': 'x',
                           'y': 'One',
                           'yref': 'y'},
                          {'font': {'color': '#FFFFFF'},
                           'showarrow': False,
                           'text': 'third',
                           'x': 'A',
                           'xref': 'x',
                           'y': 'Two',
                           'yref': 'y'},
                          {'font': {'color': '#000000'},
                           'showarrow': False,
                           'text': 'fourth',
                           'x': 'B',
                           'xref': 'x',
                           'y': 'Two',
                           'yref': 'y'},
                          {'font': {'color': '#FFFFFF'},
                           'showarrow': False,
                           'text': 'fifth',
                           'x': 'A',
                           'xref': 'x',
                           'y': 'Three',
                           'yref': 'y'},
                          {'font': {'color': '#FFFFFF'},
                           'showarrow': False,
                           'text': 'sixth',
                           'x': 'B',
                           'xref': 'x',
                           'y': 'Three',
                           'yref': 'y'}],
                          'xaxis': {'dtick': 1,
                                    'gridcolor': 'rgb(0, 0, 0)',
                                    'side': 'top',
                                    'ticks': ''},
                          'yaxis': {'dtick': 1, 'ticks': '',
                                    'ticksuffix': '  '}}}
        self.assert_fig_equal(
            a['data'][0],
            expected_a['data'][0],
        )

        self.assert_fig_equal(a['layout'],
                              expected_a['layout'])


class TestTable(TestCase, NumpyTestUtilsMixin):

    def test_fontcolor_input(self):

        # check: ValueError if fontcolor input is incorrect

        kwargs = {'table_text': [['one', 'two'], [1, 2], [1, 2], [1, 2]],
                  'fontcolor': '#000000'}
        self.assertRaises(ValueError,
                          ff.create_table, **kwargs)

        kwargs = {'table_text': [['one', 'two'], [1, 2], [1, 2], [1, 2]],
                  'fontcolor': ['red', 'blue']}
        self.assertRaises(ValueError,
                          ff.create_table, **kwargs)

    def test_simple_table(self):

        # we should be able to create a striped table by suppling a text matrix

        text = [['Country', 'Year', 'Population'], ['US', 2000, 282200000],
                ['Canada', 2000, 27790000], ['US', 1980, 226500000]]
        table = ff.create_table(text)
        expected_table = {'data': [{'colorscale': [[0, '#00083e'],
                                                   [0.5, '#ededee'],
                                                   [1, '#ffffff']],
                                    'hoverinfo': 'none',
                                    'opacity': 0.75,
                                    'showscale': False,
                                    'type': 'heatmap',
                                    'z': [[0, 0, 0], [0.5, 0.5, 0.5],
                                          [1, 1, 1], [0.5, 0.5, 0.5]]}],
                          'layout': {'annotations': [{'align': 'left',
                                                      'font': {'color': '#ffffff'},
                                                      'showarrow': False,
                                                      'text': '<b>Country</b>',
                                                      'x': -0.45,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 0,
                                                      'yref': 'y'},
                                                     {'align': 'left',
                                                      'font': {'color': '#ffffff'},
                                                      'showarrow': False,
                                                      'text': '<b>Year</b>',
                                                      'x': 0.55,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 0,
                                                      'yref': 'y'},
                                                     {'align': 'left',
                                                      'font': {'color': '#ffffff'},
                                                      'showarrow': False,
                                                      'text': '<b>Population</b>',
                                                      'x': 1.55,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 0,
                                                      'yref': 'y'},
                                                     {'align': 'left',
                                                      'font': {'color': '#000000'},
                                                      'showarrow': False,
                                                      'text': 'US',
                                                      'x': -0.45,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 1,
                                                      'yref': 'y'},
                                                     {'align': 'left',
                                                      'font': {'color': '#000000'},
                                                      'showarrow': False,
                                                      'text': '2000',
                                                      'x': 0.55,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 1,
                                                      'yref': 'y'},
                                                     {'align': 'left',
                                                      'font': {'color': '#000000'},
                                                      'showarrow': False,
                                                      'text': '282200000',
                                                      'x': 1.55,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 1,
                                                      'yref': 'y'},
                                                     {'align': 'left',
                                                      'font': {'color': '#000000'},
                                                      'showarrow': False,
                                                      'text': 'Canada',
                                                      'x': -0.45,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 2,
                                                      'yref': 'y'},
                                                     {'align': 'left',
                                                      'font': {'color': '#000000'},
                                                      'showarrow': False,
                                                      'text': '2000',
                                                      'x': 0.55,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 2,
                                                      'yref': 'y'},
                                                     {'align': 'left',
                                                      'font': {'color': '#000000'},
                                                      'showarrow': False,
                                                      'text': '27790000',
                                                      'x': 1.55,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 2,
                                                      'yref': 'y'},
                                                     {'align': 'left',
                                                      'font': {'color': '#000000'},
                                                      'showarrow': False,
                                                      'text': 'US',
                                                      'x': -0.45,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 3,
                                                      'yref': 'y'},
                                                     {'align': 'left',
                                                      'font': {'color': '#000000'},
                                                      'showarrow': False,
                                                      'text': '1980',
                                                      'x': 0.55,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 3,
                                                      'yref': 'y'},
                                                     {'align': 'left',
                                                      'font': {'color': '#000000'},
                                                      'showarrow': False,
                                                      'text': '226500000',
                                                      'x': 1.55,
                                                      'xanchor': 'left',
                                                      'xref': 'x',
                                                      'y': 3,
                                                      'yref': 'y'}],
                                     'height': 170,
                                     'margin': {'b': 0, 'l': 0, 'r': 0, 't': 0},
                                     'xaxis': {'dtick': 1,
                                               'gridwidth': 2,
                                               'showticklabels': False,
                                               'tick0': -0.5,
                                               'ticks': '',
                                               'zeroline': False},
                                     'yaxis': {'autorange': 'reversed',
                                               'dtick': 1,
                                               'gridwidth': 2,
                                               'showticklabels': False,
                                               'tick0': 0.5,
                                               'ticks': '',
                                               'zeroline': False}}}

        self.assert_fig_equal(
            table['data'][0],
            expected_table['data'][0]
        )

        self.assert_fig_equal(
            table['layout'],
            expected_table['layout']
        )

    def test_table_with_index(self):

        # we should be able to create a striped table where the first column
        # matches the coloring of the header

        text = [['Country', 'Year', 'Population'], ['US', 2000, 282200000],
                ['Canada', 2000, 27790000]]
        index_table = ff.create_table(text, index=True, index_title='Title')
        exp_index_table = {'data': [{'colorscale': [[0, '#00083e'], [0.5, '#ededee'], [1, '#ffffff']],
                                     'hoverinfo': 'none',
                                     'opacity': 0.75,
                                     'showscale': False,
                                     'type': 'heatmap',
                                     'z': [[0, 0, 0], [0, 0.5, 0.5], [0, 1, 1]]}],
                           'layout': {'annotations': [{'align': 'left',
                                      'font': {'color': '#ffffff'},
                                      'showarrow': False,
                                      'text': '<b>Country</b>',
                                      'x': -0.45,
                                      'xanchor': 'left',
                                      'xref': 'x',
                                      'y': 0,
                                      'yref': 'y'},
                                     {'align': 'left',
                                      'font': {'color': '#ffffff'},
                                      'showarrow': False,
                                      'text': '<b>Year</b>',
                                      'x': 0.55,
                                      'xanchor': 'left',
                                      'xref': 'x',
                                      'y': 0,
                                      'yref': 'y'},
                                     {'align': 'left',
                                      'font': {'color': '#ffffff'},
                                      'showarrow': False,
                                      'text': '<b>Population</b>',
                                      'x': 1.55,
                                      'xanchor': 'left',
                                      'xref': 'x',
                                      'y': 0,
                                      'yref': 'y'},
                                     {'align': 'left',
                                      'font': {'color': '#ffffff'},
                                      'showarrow': False,
                                      'text': '<b>US</b>',
                                      'x': -0.45,
                                      'xanchor': 'left',
                                      'xref': 'x',
                                      'y': 1,
                                      'yref': 'y'},
                                     {'align': 'left',
                                      'font': {'color': '#000000'},
                                      'showarrow': False,
                                      'text': '2000',
                                      'x': 0.55,
                                      'xanchor': 'left',
                                      'xref': 'x',
                                      'y': 1,
                                      'yref': 'y'},
                                     {'align': 'left',
                                      'font': {'color': '#000000'},
                                      'showarrow': False,
                                      'text': '282200000',
                                      'x': 1.55,
                                      'xanchor': 'left',
                                      'xref': 'x',
                                      'y': 1,
                                      'yref': 'y'},
                                     {'align': 'left',
                                      'font': {'color': '#ffffff'},
                                      'showarrow': False,
                                      'text': '<b>Canada</b>',
                                      'x': -0.45,
                                      'xanchor': 'left',
                                      'xref': 'x',
                                      'y': 2,
                                      'yref': 'y'},
                                     {'align': 'left',
                                      'font': {'color': '#000000'},
                                      'showarrow': False,
                                      'text': '2000',
                                      'x': 0.55,
                                      'xanchor': 'left',
                                      'xref': 'x',
                                      'y': 2,
                                      'yref': 'y'},
                                     {'align': 'left',
                                      'font': {'color': '#000000'},
                                      'showarrow': False,
                                      'text': '27790000',
                                      'x': 1.55,
                                      'xanchor': 'left',
                                      'xref': 'x',
                                      'y': 2,
                                      'yref': 'y'}],
                                      'height': 140,
                                      'margin': {'b': 0, 'l': 0, 'r': 0, 't': 0},
                                      'xaxis': {'dtick': 1,
                                                'gridwidth': 2,
                                                'showticklabels': False,
                                                'tick0': -0.5,
                                                'ticks': '',
                                                'zeroline': False},
                                      'yaxis': {'autorange': 'reversed',
                                                'dtick': 1,
                                                'gridwidth': 2,
                                                'showticklabels': False,
                                                'tick0': 0.5,
                                                'ticks': '',
                                                'zeroline': False}}}

        self.assert_fig_equal(
            index_table['data'][0],
            exp_index_table['data'][0]
        )

        self.assert_fig_equal(
            index_table['layout'],
            exp_index_table['layout']
        )


class TestGantt(TestCase):

    def test_validate_gantt(self):

        # validate the basic gantt inputs

        df = [{'Task': 'Job A',
               'Start': '2009-02-01',
               'Finish': '2009-08-30',
               'Complete': 'a'}]

        pattern2 = ('In order to use an indexing column and assign colors to '
                    'the values of the index, you must choose an actual '
                    'column name in the dataframe or key if a list of '
                    'dictionaries is being used.')

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                ff.create_gantt,
                                df, index_col='foo')

        df = 'foo'

        pattern3 = ('You must input either a dataframe or a list of '
                    'dictionaries.')

        self.assertRaisesRegexp(PlotlyError, pattern3,
                                ff.create_gantt, df)

        df = []

        pattern4 = ('Your list is empty. It must contain at least one '
                    'dictionary.')

        self.assertRaisesRegexp(PlotlyError, pattern4,
                                ff.create_gantt, df)

        df = ['foo']

        pattern5 = ('Your list must only include dictionaries.')

        self.assertRaisesRegexp(PlotlyError, pattern5,
                                ff.create_gantt, df)

    def test_gantt_index(self):

        # validate the index used for gantt

        df = [{'Task': 'Job A',
               'Start': '2009-02-01',
               'Finish': '2009-08-30',
               'Complete': 50}]

        pattern = ('In order to use an indexing column and assign colors to '
                   'the values of the index, you must choose an actual '
                   'column name in the dataframe or key if a list of '
                   'dictionaries is being used.')

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_gantt,
                                df, index_col='foo')

        df = [{'Task': 'Job A', 'Start': '2009-02-01',
               'Finish': '2009-08-30', 'Complete': 'a'},
              {'Task': 'Job A', 'Start': '2009-02-01',
               'Finish': '2009-08-30', 'Complete': 50}]

        pattern2 = ('Error in indexing column. Make sure all entries of each '
                    'column are all numbers or all strings.')

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                ff.create_gantt,
                                df, index_col='Complete')

    def test_gantt_validate_colors(self):

        # validate the gantt colors variable

        df = [{'Task': 'Job A', 'Start': '2009-02-01',
               'Finish': '2009-08-30', 'Complete': 75, 'Resource': 'A'},
              {'Task': 'Job B', 'Start': '2009-02-01',
               'Finish': '2009-08-30', 'Complete': 50, 'Resource': 'B'}]

        pattern = ('Whoops! The elements in your rgb colors tuples cannot '
                   'exceed 255.0.')

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_gantt, df,
                                index_col='Complete', colors='rgb(300,1,1)')

        self.assertRaises(PlotlyError, ff.create_gantt,
                          df, index_col='Complete', colors='foo')

        pattern2 = ('Whoops! The elements in your colors tuples cannot '
                    'exceed 1.0.')

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                ff.create_gantt, df,
                                index_col='Complete', colors=(2, 1, 1))

        # verify that if colors is a dictionary, its keys span all the
        # values in the index column
        colors_dict = {75: 'rgb(1, 2, 3)'}

        pattern3 = ('If you are using colors as a dictionary, all of its '
                    'keys must be all the values in the index column.')

        self.assertRaisesRegexp(PlotlyError, pattern3,
                                ff.create_gantt, df,
                                index_col='Complete', colors=colors_dict)

        # check: index is set if colors is a dictionary
        colors_dict_good = {50: 'rgb(1, 2, 3)', 75: 'rgb(5, 10, 15)'}

        pattern4 = ('Error. You have set colors to a dictionary but have not '
                    'picked an index. An index is required if you are '
                    'assigning colors to particular values in a dictioanry.')

        self.assertRaisesRegexp(PlotlyError, pattern4,
                                ff.create_gantt, df,
                                colors=colors_dict_good)

        # check: number of colors is equal to or greater than number of
        # unique index string values
        pattern5 = ("Error. The number of colors in 'colors' must be no less "
                    "than the number of unique index values in your group "
                    "column.")

        self.assertRaisesRegexp(PlotlyError, pattern5,
                                ff.create_gantt, df,
                                index_col='Resource',
                                colors=['#ffffff'])

        # check: if index is numeric, colors has at least 2 colors in it
        pattern6 = ("You must use at least 2 colors in 'colors' if you "
                    "are using a colorscale. However only the first two "
                    "colors given will be used for the lower and upper "
                    "bounds on the colormap.")

        self.assertRaisesRegexp(PlotlyError, pattern6,
                                ff.create_gantt, df,
                                index_col='Complete',
                                colors=['#ffffff'])

    def test_gannt_groups_and_descriptions(self):

        # check if grouped gantt chart matches with expected output

        df = [
            dict(Task='Task A', Description='Task A - 1', Start='2008-10-05',
                 Finish='2009-04-15', IndexCol='TA'),
            dict(Task="Task B", Description='Task B - 1', Start='2008-12-06',
                 Finish='2009-03-15', IndexCol='TB'),
            dict(Task="Task C", Description='Task C - 1', Start='2008-09-07',
                 Finish='2009-03-15', IndexCol='TC'),
            dict(Task="Task C", Description='Task C - 2', Start='2009-05-08',
                 Finish='2009-04-15', IndexCol='TC'),
            dict(Task="Task A", Description='Task A - 2', Start='2009-04-20',
                 Finish='2009-05-30', IndexCol='TA')
        ]

        test_gantt_chart = ff.create_gantt(
            df, colors=dict(TA='rgb(220, 0, 0)', TB='rgb(170, 14, 200)',
            TC=(1, 0.9, 0.16)), show_colorbar=True, index_col='IndexCol',
            group_tasks=True
        )

        exp_gantt_chart = {
            'data': [{'marker': {'color': 'white'},
               'name': '',
               'showlegend': False,
               'text': 'Task A - 1',
               'x': ['2008-10-05', '2009-04-15'],
               'y': [2, 2]},
              {'marker': {'color': 'white'},
               'name': '',
               'showlegend': False,
               'text': 'Task B - 1',
               'x': ['2008-12-06', '2009-03-15'],
               'y': [1, 1]},
              {'marker': {'color': 'white'},
               'name': '',
               'showlegend': False,
               'text': 'Task C - 1',
               'x': ['2008-09-07', '2009-03-15'],
               'y': [0, 0]},
              {'marker': {'color': 'white'},
               'name': '',
               'showlegend': False,
               'text': 'Task C - 2',
               'x': ['2009-05-08', '2009-04-15'],
               'y': [0, 0]},
              {'marker': {'color': 'white'},
               'name': '',
               'showlegend': False,
               'text': 'Task A - 2',
               'x': ['2009-04-20', '2009-05-30'],
               'y': [2, 2]},
              {'hoverinfo': 'none',
               'marker': {'color': 'rgb(220, 0, 0)', 'size': 1},
               'name': 'TA',
               'showlegend': True,
               'x': ['2009-04-20', '2009-04-20'],
               'y': [0, 0]},
              {'hoverinfo': 'none',
               'marker': {'color': 'rgb(170, 14, 200)', 'size': 1},
               'name': 'TB',
               'showlegend': True,
               'x': ['2009-04-20', '2009-04-20'],
               'y': [1, 1]},
              {'hoverinfo': 'none',
               'marker': {'color': 'rgb(255, 230, 41)', 'size': 1},
               'name': 'TC',
               'showlegend': True,
               'x': ['2009-04-20', '2009-04-20'],
               'y': [2, 2]}],
            'layout': {'height': 600,
                'hovermode': 'closest',
                'shapes': [{'fillcolor': 'rgb(220, 0, 0)',
                            'line': {'width': 0},
                            'opacity': 1,
                            'type': 'rect',
                            'x0': '2008-10-05',
                            'x1': '2009-04-15',
                            'xref': 'x',
                            'y0': 1.8,
                            'y1': 2.2,
                            'yref': 'y'},
                           {'fillcolor': 'rgb(170, 14, 200)',
                            'line': {'width': 0},
                            'opacity': 1,
                            'type': 'rect',
                            'x0': '2008-12-06',
                            'x1': '2009-03-15',
                            'xref': 'x',
                            'y0': 0.8,
                            'y1': 1.2,
                            'yref': 'y'},
                           {'fillcolor': 'rgb(255, 230, 41)',
                            'line': {'width': 0},
                            'opacity': 1,
                            'type': 'rect',
                            'x0': '2008-09-07',
                            'x1': '2009-03-15',
                            'xref': 'x',
                            'y0': -0.2,
                            'y1': 0.2,
                            'yref': 'y'},
                           {'fillcolor': 'rgb(255, 230, 41)',
                            'line': {'width': 0},
                            'opacity': 1,
                            'type': 'rect',
                            'x0': '2009-05-08',
                            'x1': '2009-04-15',
                            'xref': 'x',
                            'y0': -0.2,
                            'y1': 0.2,
                            'yref': 'y'},
                           {'fillcolor': 'rgb(220, 0, 0)',
                            'line': {'width': 0},
                            'opacity': 1,
                            'type': 'rect',
                            'x0': '2009-04-20',
                            'x1': '2009-05-30',
                            'xref': 'x',
                            'y0': 1.8,
                            'y1': 2.2,
                            'yref': 'y'}],
                'showlegend': True,
                'title': 'Gantt Chart',
                'width': 900,
                'xaxis': {'rangeselector': {'buttons': [{'count': 7,
                                                         'label': '1w',
                                                         'step': 'day',
                                                         'stepmode': 'backward'},
                                                        {'count': 1,
                                                         'label': '1m',
                                                         'step': 'month',
                                                         'stepmode': 'backward'},
                                                        {'count': 6,
                                                         'label': '6m',
                                                         'step': 'month',
                                                         'stepmode': 'backward'},
                                                        {'count': 1,
                                                         'label': 'YTD',
                                                         'step': 'year',
                                                         'stepmode': 'todate'},
                                                        {'count': 1,
                                                         'label': '1y',
                                                         'step': 'year',
                                                         'stepmode': 'backward'},
                                                        {'step': 'all'}]},
                          'showgrid': False,
                          'type': 'date',
                          'zeroline': False},
                'yaxis': {'autorange': False,
                          'range': [-1, 4],
                          'showgrid': False,
                          'ticktext': ['Task C', 'Task B', 'Task A'],
                          'tickvals': [0, 1, 2],
                          'zeroline': False}}
        }

        self.assertEqual(test_gantt_chart['data'][0],
                         exp_gantt_chart['data'][0])

        self.assertEqual(test_gantt_chart['data'][1],
                         exp_gantt_chart['data'][1])

        self.assertEqual(test_gantt_chart['data'][2],
                         exp_gantt_chart['data'][2])

        self.assertEqual(test_gantt_chart['data'][3],
                         exp_gantt_chart['data'][3])

        self.assertEqual(test_gantt_chart['data'][4],
                         exp_gantt_chart['data'][4])

        self.assertEqual(test_gantt_chart['layout'],
                         exp_gantt_chart['layout'])

    def test_gantt_all_args(self):

        # check if gantt chart matches with expected output

        df = [{'Task': 'Run',
               'Start': '2010-01-01',
               'Finish': '2011-02-02',
               'Complete': 0},
              {'Task': 'Fast',
               'Start': '2011-01-01',
               'Finish': '2012-06-05',
               'Complete': 25}]

        test_gantt_chart = ff.create_gantt(
            df, colors='Blues', index_col='Complete', reverse_colors=True,
            title='Title', bar_width=0.5, showgrid_x=True, showgrid_y=True,
            height=500, width=500
        )

        exp_gantt_chart = {
            'data': [{'marker': {'color': 'white'},
                      'name': '',
                      'x': ['2010-01-01', '2011-02-02'],
                      'y': [0, 0]},
                     {'marker': {'color': 'white'},
                      'name': '',
                      'x': ['2011-01-01', '2012-06-05'],
                      'y': [1, 1]}],
            'layout': {'height': 500,
                       'hovermode': 'closest',
                       'shapes': [{'fillcolor': 'rgb(220.0, 220.0, 220.0)',
                                   'line': {'width': 0},
                                   'opacity': 1,
                                   'type': 'rect',
                                   'x0': '2010-01-01',
                                   'x1': '2011-02-02',
                                   'xref': 'x',
                                   'y0': -0.5,
                                   'y1': 0.5,
                                   'yref': 'y'},
                                  {'fillcolor': 'rgb(166.25, 167.5, 208.0)',
                                   'line': {'width': 0},
                                   'opacity': 1,
                                   'type': 'rect',
                                   'x0': '2011-01-01',
                                   'x1': '2012-06-05',
                                   'xref': 'x',
                                   'y0': 0.5,
                                   'y1': 1.5,
                                   'yref': 'y'}],
                       'showlegend': False,
                       'title': 'Title',
                       'width': 500,
                       'xaxis': {'rangeselector': {'buttons': [
                           {'count': 7,
                            'label': '1w',
                            'step': 'day',
                            'stepmode': 'backward'},
                           {'count': 1,
                            'label': '1m',
                            'step': 'month',
                            'stepmode': 'backward'},
                           {'count': 6,
                            'label': '6m',
                            'step': 'month',
                            'stepmode': 'backward'},
                           {'count': 1,
                            'label': 'YTD',
                            'step': 'year',
                            'stepmode': 'todate'},
                           {'count': 1,
                            'label': '1y',
                            'step': 'year',
                            'stepmode': 'backward'},
                           {'step': 'all'}
                           ]},
                           'showgrid': True,
                           'type': 'date',
                           'zeroline': False},
                       'yaxis': {'autorange': False,
                                 'range': [-1, 3],
                                 'showgrid': True,
                                 'ticktext': ['Run', 'Fast'],
                                 'tickvals': [0, 1],
                                 'zeroline': False}}
        }

        self.assertEqual(test_gantt_chart['data'][0],
                         exp_gantt_chart['data'][0])

        self.assertEqual(test_gantt_chart['data'][1],
                         exp_gantt_chart['data'][1])

        self.assertEqual(test_gantt_chart['layout'],
                         exp_gantt_chart['layout'])


class Test2D_Density(TestCase, NumpyTestUtilsMixin):

    def test_validate_2D_density(self):

        # validate that x and y contain only numbers
        x = [1, 2]
        y = ['a', 2]

        pattern = ("All elements of your 'x' and 'y' lists must be numbers.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_2d_density, x, y)

        # validate that x and y are the same length
        x2 = [1]
        y2 = [1, 2]

        pattern2 = ("Both lists 'x' and 'y' must be the same length.")

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                ff.create_2d_density, x2, y2)

    def test_2D_density_all_args(self):

        # check if 2D_density data matches with expected output
        x = [1, 2]
        y = [2, 4]

        colorscale = ['#7A4579', '#D56073', 'rgb(236,158,105)',
                      (1, 1, 0.2), (0.98, 0.98, 0.98)]

        test_2D_density_chart = ff.create_2d_density(
            x, y, colorscale=colorscale, hist_color='rgb(255,237,222)',
            point_size=3, height=800, width=800)

        exp_2D_density_chart = {
            'data': [{'marker': {'color': 'rgb(0, 0, 128)',
                      'opacity': 0.4,
                      'size': 3},
                      'mode': 'markers',
                      'name': 'points',
                      'type': 'scatter',
                      'x': [1, 2],
                      'y': [2, 4]},
                     {'colorscale': [[0.0, 'rgb(122, 69, 121)'],
                                     [0.25, 'rgb(213, 96, 115)'],
                                     [0.5, 'rgb(236, 158, 105)'],
                                     [0.75, 'rgb(255, 255, 51)'],
                                     [1.0, 'rgb(250, 250, 250)']],
                      'name': 'density',
                      'ncontours': 20,
                      'reversescale': True,
                      'showscale': False,
                      'type': 'histogram2dcontour',
                      'x': [1, 2],
                      'y': [2, 4]},
                     {'marker': {'color': 'rgb(255, 237, 222)'},
                      'name': 'x density',
                      'type': 'histogram',
                      'x': [1, 2],
                      'yaxis': 'y2'},
                     {'marker': {'color': 'rgb(255, 237, 222)'},
                      'name': 'y density',
                      'type': 'histogram',
                      'xaxis': 'x2',
                      'y': [2, 4]}],
            'layout': {'autosize': False,
                       'bargap': 0,
                       'height': 800,
                       'hovermode': 'closest',
                       'margin': {'t': 50},
                       'showlegend': False,
                       'title': '2D Density Plot',
                       'width': 800,
                       'xaxis': {'domain': [0, 0.85],
                                 'showgrid': False,
                                 'zeroline': False},
                       'xaxis2': {'domain': [0.85, 1],
                                  'showgrid': False,
                                  'zeroline': False},
                       'yaxis': {'domain': [0, 0.85],
                                 'showgrid': False,
                                 'zeroline': False},
                       'yaxis2': {'domain': [0.85, 1],
                                  'showgrid': False,
                                  'zeroline': False}}
        }

        self.assert_fig_equal(test_2D_density_chart['data'][0],
                              exp_2D_density_chart['data'][0])

        self.assert_fig_equal(test_2D_density_chart['data'][1],
                              exp_2D_density_chart['data'][1])

        self.assert_fig_equal(test_2D_density_chart['data'][2],
                              exp_2D_density_chart['data'][2])

        self.assert_fig_equal(test_2D_density_chart['data'][3],
                              exp_2D_density_chart['data'][3])

        self.assert_fig_equal(test_2D_density_chart['layout'],
                              exp_2D_density_chart['layout'])
