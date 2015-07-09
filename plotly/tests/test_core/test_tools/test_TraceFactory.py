from unittest import TestCase
from plotly.graph_objs import graph_objs, Line
from plotly.exceptions import PlotlyError

import plotly.tools as tls
import math
from nose.tools import raises


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

    def test_wrong_arrow_scale(self):

        # check: ValueError if arrow_scale is <= 0

        kwargs = {'x': [1, 2], 'y': [1, 2],
                  'u': [1, 2], 'v': [1, 2],
                  'arrow_scale': -1}
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


class TestStreamline(TestCase):

    # create_streamline has numpy dependency-
    # additional streamline tests in test_optional

    def test_wrong_arrow_scale(self):

        # check for ValueError if arrow_scale is <= 0

        kwargs = {'x': [0, 2], 'y': [0, 2],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]],
                  'arrow_scale': 0}
        self.assertRaises(ValueError, tls.TraceFactory.create_streamline,
                          **kwargs)

    def test_wrong_density(self):

        # check for ValueError if density is <= 0

        kwargs = {'x': [0, 2], 'y': [0, 2],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]],
                  'density': 0}
        self.assertRaises(ValueError, tls.TraceFactory.create_streamline,
                          **kwargs)

    def test_uneven_x(self):

        # check for PlotlyError if x is not evenly spaced

        kwargs = {'x': [0, 2, 7, 9], 'y': [0, 2, 4, 6],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, tls.TraceFactory.create_streamline,
                          **kwargs)

    def test_uneven_y(self):

        # check for PlotlyError if y is not evenly spaced

        kwargs = {'x': [0, 2, 4, 6], 'y': [1.5, 2, 3, 3.5],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, tls.TraceFactory.create_streamline,
                          **kwargs)

    def test_unequal_shape_u(self):

        # check for PlotlyError if u and v are not the same length

        kwargs = {'x': [0, 2, 4, 6], 'y': [1.5, 2, 3, 3.5],
                  'u': [[-1, -5], [-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, tls.TraceFactory.create_streamline,
                          **kwargs)
