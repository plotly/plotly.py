import math
from unittest import TestCase

from nose.tools import raises

import plotly.tools as tls
from plotly.exceptions import PlotlyError
from plotly.graph_objs import Data, Line, graph_objs


class TestQuiver(TestCase):

    def test_unequal_xy_length(self):

        # check: PlotlyError if x and y are not the same length

        kwargs = {'x': [1, 2], 'y': [1], 'u': [1, 2], 'v': [1, 2]}
        self.assertRaises(PlotlyError, tls.TraceFactory.create_quiver,
                          **kwargs)

    def test_wrong_scale(self):

        # check: ValueError if scale is <= 0

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'scale': -1}
        self.assertRaises(ValueError, tls.TraceFactory.create_quiver,
                          **kwargs)

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'scale': 0}
        self.assertRaises(ValueError, tls.TraceFactory.create_quiver,
                          **kwargs)

    def test_wrong_arrow_scale(self):

        # check: ValueError if arrow_scale is <= 0

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'arrow_scale': -1}
        self.assertRaises(ValueError, tls.TraceFactory.create_quiver,
                          **kwargs)

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'arrow_scale': 0}
        self.assertRaises(ValueError, tls.TraceFactory.create_quiver,
                          **kwargs)

    def test_one_arrow(self):

        # we should be able to create a single arrow using create_quiver

        quiver = tls.TraceFactory.create_quiver(x=[1], y=[1],
                                                u=[1], v=[1],
                                                scale=1)
        expected_quiver = {
            'y': [1, 2, None, 1.615486170766527, 2, 1.820698256761928, None],
            'x': [1, 2, None, 1.820698256761928, 2, 1.615486170766527, None],
            'type': 'scatter',
            'mode': 'lines'
        }
        self.assertEqual(quiver, expected_quiver)

    def test_more_kwargs(self):

        # we should be able to create 2 arrows and change the arrow_scale,
        # angle, and arrow using create_quiver

        quiver = tls.TraceFactory.create_quiver(x=[1, 2],
                                                y=[1, 2],
                                                u=[math.cos(1),
                                                   math.cos(2)],
                                                v=[math.sin(1),
                                                   math.sin(2)],
                                                arrow_scale=.4,
                                                angle=math.pi / 6,
                                                line=Line(color='purple',
                                                          width=3))
        expected_quiver = {
            'y': [1, 1.0841470984807897,
                  None, 2,
                  2.0909297426825684, None,
                  1.044191642387781, 1.0841470984807897,
                  1.0658037346225067, None,
                  2.0677536925644366, 2.0909297426825684,
                  2.051107819102551, None],
            'x': [1, 1.0540302305868139,
                  None, 2,
                  1.9583853163452858, None,
                  1.052143029378767, 1.0540302305868139,
                  1.0184841899864512, None,
                  1.9909870141679737, 1.9583853163452858,
                  1.9546151170949464, None],
            'line': {'color': 'purple',
                     'width': 3},
            'type': 'scatter',
            'mode': 'lines', }
        self.assertEqual(quiver, expected_quiver)


class TestOHLC(TestCase):

    def test_unequal_ohlc_length(self):

        # check: PlotlyError if open, high, low, close are not the same length
        # for TraceFactory.ohlc_increase and TraceFactory.ohlc_decrease

        kwargs = {'open': [1], 'high': [1, 3], 'low': [1, 2], 'close': [1, 2]}
        self.assertRaises(PlotlyError, tls.TraceFactory.create_ohlc_increase,
                          **kwargs)

        kwargs = {'open': [1, 2], 'high': [1, 2, 3], 'low': [1, 2],
                  'close': [1, 2]}
        self.assertRaises(PlotlyError, tls.TraceFactory.create_ohlc_increase,
                          **kwargs)

        kwargs = {'open': [1], 'high': [1, 3], 'low': [1, 2], 'close': [2]}
        self.assertRaises(PlotlyError, tls.TraceFactory.create_ohlc_decrease,
                          **kwargs)

        kwargs = {'open': [1, 2], 'high': [1, 2],
                  'low': [1, 2, .5], 'close': [1, 2]}
        self.assertRaises(PlotlyError, tls.TraceFactory.create_ohlc_decrease,
                          **kwargs)

    def test_high_highest_value(self):

        # check: PlotlyError if the "high" value is less than the corresponding
        # open, low, or close value because if the "high" value is not the
        # highest (or equal) then the data may have been entered incorrectly.

        # create_ohlc_increase
        kwargs = {'open': [2, 3], 'high': [4, 2],
                  'low': [1, 1], 'close': [1, 2]}
        self.assertRaisesRegexp(PlotlyError, "Oops! Looks like some of "
                                             "your high values are less "
                                             "the corresponding open, "
                                             "low, or close values. "
                                             "Double check that your data "
                                             "is entered in O-H-L-C order",
                                tls.TraceFactory.create_ohlc_increase,
                                **kwargs)

        # create_ohlc_decrease
        kwargs = {'open': [2, 3], 'high': [4, 3],
                  'low': [1, 1], 'close': [1, 6]}
        self.assertRaisesRegexp(PlotlyError,
                                "Oops! Looks like some of "
                                "your high values are less "
                                "the corresponding open, "
                                "low, or close values. "
                                "Double check that your data "
                                "is entered in O-H-L-C order",
                                tls.TraceFactory.create_ohlc_decrease,
                                **kwargs)

    def test_low_lowest_value(self):

        # check: PlotlyError if the "low" value is greater than the
        # corresponding open, high, or close value because if the "low" value
        # is not the lowest (or equal) then the data may have been entered
        # incorrectly

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
                                tls.TraceFactory.create_ohlc_increase,
                                **kwargs)

        # create_ohlc_decrease
        kwargs = {'open': [2, 3], 'high': [4, 6],
                  'low': [1, 5], 'close': [1, 6]}
        self.assertRaisesRegexp(PlotlyError,
                                "Oops! Looks like some of "
                                "your low values are greater "
                                "than the corresponding high"
                                ", open, or close values. "
                                "Double check that your data "
                                "is entered in O-H-L-C order",
                                tls.TraceFactory.create_ohlc_decrease,
                                **kwargs)

    def test_one_ohlc_increase(self):

        # This should create one "increase" (i.e. close > open) ohlc stick

        ohlc_incr = tls.TraceFactory.create_ohlc_increase(open=[33.0],
                                                          high=[33.2],
                                                          low=[32.7],
                                                          close=[33.1])

        expected_ohlc_incr = {
            'mode': 'lines',
            'y': [33.0, 33.0, 33.2, 32.7, 33.1, 33.1, None],
            'line': {'color': 'rgb(44, 160, 44)'},
            'x': [0.8, 1, 1, 1, 1, 1.2, None],
            'name': 'Increasing',
            'type': 'scatter',
            'text': ('Open', 'Open', 'High', 'Low', 'Close', 'Close', '')}
        self.assertEqual(ohlc_incr, expected_ohlc_incr)

    def test_ohlc_increase_with_kwargs(self):

        # This should create one "increase" (i.e. close > open) ohlc stick
        # and change the name to "POSITIVE!!"

        ohlc_incr = tls.TraceFactory.create_ohlc_increase(open=[1.5],
                                                          high=[30],
                                                          low=[1],
                                                          close=[25],
                                                          name="POSITIVE!!")

        expected_ohlc_incr = {
            'text': ('Open', 'Open', 'High', 'Low', 'Close', 'Close', ''),
            'type': 'scatter',
            'name': 'POSITIVE!!',
            'x': [0.8, 1, 1, 1, 1, 1.2, None],
            'y': [1.5, 1.5, 30, 1, 25, 25, None],
            'mode': 'lines',
            'line': {'color': 'rgb(44, 160, 44)'}}

        self.assertEqual(ohlc_incr, expected_ohlc_incr)

    def test_one_ohlc_decrease(self):

        # This should create one "decrease" (i.e. close < open) ohlc stick

        ohlc_decr = tls.TraceFactory.create_ohlc_decrease(open=[33.3],
                                                          high=[33.3],
                                                          low=[32.7],
                                                          close=[32.9])

        expected_ohlc_decr = {
            'mode': 'lines',
            'y': [33.3, 33.3, 33.3, 32.7, 32.9, 32.9, None],
            'line': {'color': 'rgb(214, 39, 40)'},
            'x': [0.8, 1, 1, 1, 1, 1.2, None],
            'name': 'Decreasing',
            'type': 'scatter',
            'text': ('Open', 'Open', 'High', 'Low', 'Close', 'Close', '')}
        self.assertEqual(ohlc_decr, expected_ohlc_decr)

    def test_ohlc_decrease_with_kwargs(self):

        # This should create one "decrease" (i.e. close < open) ohlc stick
        # and change the line width to 4

        ohlc_decr = tls.TraceFactory.create_ohlc_decrease(open=[15], high=[30],
                                                          low=[1], close=[5],
                                                          line=Line(
                                                              color='rgb(214, 39, 40)',
                                                              width=4))

        expected_ohlc_decr = {
            'text': ('Open', 'Open', 'High', 'Low', 'Close', 'Close', ''),
            'type': 'scatter',
            'name': 'Decreasing',
            'x': [0.8, 1, 1, 1, 1, 1.2, None],
            'y': [15, 15, 30, 1, 5, 5, None],
            'mode': 'lines',
            'line': {'color': 'rgb(214, 39, 40)', 'width': 4}}

        self.assertEqual(ohlc_decr, expected_ohlc_decr)

    def test_ohlc_increase_and_decrease(self):

        # This should add multiple increasing and decreasing sticks
        # and check that what we expect (i.e. the data and default kwargs)
        # is resulting from data=Data([ohlc_increasing, ohlc_decreasing])

        o = [3.3, 4, 9.3, 8.9, 4.9, 9, 2.9, 5]
        h = [7, 6.4, 10, 10, 10, 14.6, 12, 7]
        l = [3, 2, 7, 3, 2, 2, 1.1, 2.3]
        c = [3.3, 6.3, 10, 9, 9.2, 3, 2.9, 6.1]

        ohlc_incr = tls.TraceFactory.create_ohlc_increase(o, h, l, c)
        ohlc_decr = tls.TraceFactory.create_ohlc_decrease(o, h, l, c)
        ohlc_data = Data([ohlc_incr, ohlc_decr])

        expected_ohlc_data = [{
            'text': ('Open', 'Open', 'High', 'Low', 'Close', 'Close', '',
                     'Open', 'Open', 'High', 'Low', 'Close', 'Close', '',
                     'Open', 'Open', 'High', 'Low', 'Close', 'Close', '',
                     'Open', 'Open', 'High', 'Low', 'Close', 'Close', '',
                     'Open', 'Open', 'High', 'Low', 'Close', 'Close', ''),
            'type': 'scatter',
            'name': 'Increasing',
            'x': [1.8, 2, 2, 2, 2, 2.2, None, 2.8, 3, 3, 3, 3, 3.2, None,
                  3.8, 4, 4, 4, 4, 4.2, None, 4.8, 5, 5, 5, 5, 5.2, None,
                  7.8, 8, 8, 8, 8, 8.2, None],
            'y': [4, 4, 6.4, 2, 6.3, 6.3, None, 9.3, 9.3, 10, 7, 10, 10, None,
                  8.9, 8.9, 10, 3, 9, 9, None, 4.9, 4.9, 10, 2, 9.2, 9.2, None,
                  5, 5, 7, 2.3, 6.1, 6.1, None],
            'mode': 'lines',
            'line': {'color': 'rgb(44, 160, 44)'}},
            {'text': ('Open', 'Open', 'High', 'Low', 'Close', 'Close', '',
                      'Open', 'Open', 'High', 'Low', 'Close', 'Close', '',
                      'Open', 'Open', 'High', 'Low', 'Close', 'Close', ''),
             'type': 'scatter', 'name': 'Decreasing',
             'x': [0.8, 1, 1, 1, 1, 1.2, None, 5.8, 6, 6, 6, 6, 6.2, None,
                   6.8, 7, 7, 7, 7, 7.2, None],
             'y': [3.3, 3.3, 7, 3, 3.3, 3.3, None, 9, 9, 14.6, 2, 3, 3, None,
                   2.9, 2.9, 12, 1.1, 2.9, 2.9, None],
             'mode': 'lines',
             'line': {'color': 'rgb(214, 39, 40)'}}]

        self.assertEqual(ohlc_data, expected_ohlc_data)

