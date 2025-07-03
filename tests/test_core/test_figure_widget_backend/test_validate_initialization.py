from unittest import TestCase
import plotly.graph_objs as go

try:
    go.FigureWidget()
    figure_widget_available = True
except ImportError:
    figure_widget_available = False


class TestInitialization(TestCase):
    if figure_widget_available:

        def test_widget_layout_present_on_init(self):
            fig = go.FigureWidget(data=go.Scatter(x=[1, 2], y=[1, 2]))
            assert fig._widget_layout != {}

        def test_widget_data_present_on_init(self):
            fig = go.FigureWidget(data=go.Bar(x=[1, 2], y=[1, 2]))
            assert fig._widget_data != []
