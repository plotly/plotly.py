from unittest import TestCase
import plotly.graph_objs as go
from plotly.tests.test_optional.optional_utils import NumpyTestUtilsMixin


class TestAssignmentPrimitive(NumpyTestUtilsMixin, TestCase):

    def setUp(self):
        self.scatter = go.Scatter()
        self.assert_fig_equal(self.scatter, {'type': 'scatter'})

    def test_toplevel(self):
        self.scatter.fillcolor = 'green'
        self.assert_fig_equal(self.scatter,
                              {'type': 'scatter',
                               'fillcolor': 'green'})

    def test_nested(self):
        self.scatter.marker.colorbar.titlefont.family = 'courier'
        self.assert_fig_equal(
            self.scatter,
            {'type': 'scatter',
             'marker': {'colorbar': {'titlefont': {'family': 'courier'}}}})


class TestAssignmentCompound(NumpyTestUtilsMixin, TestCase):
    def setUp(self):
        self.scatter = go.Scatter()
        self.assert_fig_equal(self.scatter,
                              {'type': 'scatter'})

    def test_toplevel_obj(self):

        self.scatter.marker = go.scatter.Marker(
            color='yellow', size=10)

        self.assert_fig_equal(self.scatter,
                              {'type': 'scatter',
                               'marker': {'color': 'yellow',
                                          'size': 10}})

    def test_toplevel_dict(self):
        self.scatter.marker = dict(
            color='yellow', size=10)

        self.assert_fig_equal(self.scatter,
                              {'type': 'scatter',
                               'marker': {'color': 'yellow',
                                          'size': 10}})

    def test_nested_obj(self):
        self.scatter.marker.colorbar = go.scatter.marker.ColorBar(
            bgcolor='yellow', thickness=5)

        self.assert_fig_equal(self.scatter,
                              {'type': 'scatter',
                               'marker': {'colorbar': {
                                   'bgcolor': 'yellow',
                                   'thickness': 5}}})

    def test_nested_dict(self):
        self.scatter.marker.colorbar = dict(
            bgcolor='yellow', thickness=5)

        self.assert_fig_equal(self.scatter,
                              {'type': 'scatter',
                               'marker': {'colorbar': {
                                   'bgcolor': 'yellow',
                                   'thickness': 5}}})

# TODO
#  - Test property/item access
#  - Test item assignment
#  - Test contains (in)
#
#  - Test assign array (Use parcats.dimensions
#  - Test assign None
#  - Test validators (simple, compound, array)
