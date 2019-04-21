from __future__ import absolute_import
from unittest import TestCase
import inspect

import plotly.graph_objs as go
from plotly.subplots import make_subplots
from _plotly_future_ import _future_flags


class TestSelectTraces(TestCase):

    def setUp(self):
        _future_flags.add('v4_subplots')
        fig = make_subplots(
            rows=3,
            cols=2,
            specs=[[{}, {'type': 'scene'}],
                   [{}, {'type': 'polar'}],
                   [{'type': 'domain', 'colspan': 2}, None]]
        ).update(layout={'height': 800})

        # data[0], (1, 1)
        fig.add_scatter(
            mode='markers',
            y=[2, 3, 1],
            name='A',
            marker={'color': 'green', 'size': 10},
            row=1, col=1)

        # data[1], (1, 1)
        fig.add_bar(y=[2, 3, 1], row=1, col=1, name='B')

        # data[2], (2, 1)
        fig.add_scatter(
            mode='lines',
            y=[1, 2, 0],
            line={'color': 'purple'},
            name='C',
            row=2,
            col=1,
        )

        # data[3], (2, 1)
        fig.add_heatmap(
            z=[[2, 3, 1], [2, 1, 3], [3, 2, 1]],
            row=2,
            col=1,
            name='D',
        )

        # data[4], (1, 2)
        fig.add_scatter3d(
            x=[0, 0, 0],
            y=[0, 0, 0],
            z=[0, 1, 2],
            mode='markers',
            marker={'color': 'green', 'size': 10},
            name='E',
            row=1,
            col=2
        )

        # data[5], (1, 2)
        fig.add_scatter3d(
            x=[0, 0, -1],
            y=[-1, 0, 0],
            z=[0, 1, 2],
            mode='lines',
            line={'color': 'purple', 'width': 4},
            name='F',
            row=1,
            col=2
        )

        # data[6], (2, 2)
        fig.add_scatterpolar(
            mode='markers',
            r=[0, 3, 2],
            theta=[0, 20, 87],
            marker={'color': 'green', 'size': 8},
            name='G',
            row=2,
            col=2
        )

        # data[7], (2, 2)
        fig.add_scatterpolar(
            mode='lines',
            r=[0, 3, 2],
            theta=[20, 87, 111],
            name='H',
            row=2,
            col=2
        )

        # data[8], (3, 1)
        fig.add_parcoords(
            dimensions=[{'values': [1, 2, 3, 2, 1]},
                        {'values': [3, 2, 1, 3, 2, 1]}],
            line={'color': 'purple'},
            name='I',
            row=3,
            col=1
        )

        self.fig = fig
        self.fig_no_grid = go.Figure(self.fig)
        del self.fig_no_grid.__dict__['_grid_ref']
        del self.fig_no_grid.__dict__['_grid_str']

    def tearDown(self):
        _future_flags.remove('v4_subplots')

    def assert_select_traces(self, expected_inds, selector=None, row=None, col=None, test_no_grid=False):
        trace_generator = self.fig.select_traces(
            selector=selector, row=row, col=col)
        self.assertTrue(inspect.isgenerator(trace_generator))

        trace_list = list(trace_generator)
        self.assertEqual(trace_list, [self.fig.data[i] for i in expected_inds])

        if test_no_grid:
            trace_generator = self.fig_no_grid.select_traces(
                selector=selector, row=row, col=col)
            trace_list = list(trace_generator)
            self.assertEqual(trace_list, [self.fig_no_grid.data[i] for i in expected_inds])

    def test_select_by_type(self):
        self.assert_select_traces(
            [0, 2], selector={'type': 'scatter'}, test_no_grid=True)
        self.assert_select_traces(
            [1], selector={'type': 'bar'}, test_no_grid=True)
        self.assert_select_traces(
            [3], selector={'type': 'heatmap'}, test_no_grid=True)
        self.assert_select_traces(
            [4, 5], selector={'type': 'scatter3d'}, test_no_grid=True)
        self.assert_select_traces(
            [6, 7], selector={'type': 'scatterpolar'}, test_no_grid=True)
        self.assert_select_traces(
            [8], selector={'type': 'parcoords'}, test_no_grid=True)
        self.assert_select_traces(
            [], selector={'type': 'pie'}, test_no_grid=True)

    def test_select_by_grid(self):
        self.assert_select_traces([0, 1], row=1, col=1)
        self.assert_select_traces([2, 3], row=2, col=1)
        self.assert_select_traces([4, 5], row=1, col=2)
        self.assert_select_traces([6, 7], row=2, col=2)
        self.assert_select_traces([8], row=3, col=1)

    def test_select_by_property_across_trace_types(self):
        self.assert_select_traces(
            [0, 4, 6], selector={'mode': 'markers'}, test_no_grid=True)
        self.assert_select_traces(
            [2, 5, 7], selector={'mode': 'lines'}, test_no_grid=True)
        self.assert_select_traces(
            [0, 4],
            selector={'marker': {'color': 'green', 'size': 10}},
            test_no_grid=True)

        # Several traces have 'marker.color' == 'green', but they all have
        # additional marker properties so there should be no exact match.
        self.assert_select_traces(
            [], selector={'marker': {'color': 'green'}}, test_no_grid=True)
        self.assert_select_traces(
            [0, 4, 6], selector={'marker.color': 'green'}, test_no_grid=True)
        self.assert_select_traces(
            [2, 5, 8], selector={'line.color': 'purple'}, test_no_grid=True)

    def test_select_property_and_grid(self):
        # (1, 1)
        self.assert_select_traces(
            [0], selector={'mode': 'markers'}, row=1, col=1)
        self.assert_select_traces(
            [1], selector={'type': 'bar'}, row=1, col=1)

        # (2, 1)
        self.assert_select_traces(
            [2], selector={'mode': 'lines'}, row=2, col=1)

        # (1, 2)
        self.assert_select_traces(
            [4], selector={'marker.color': 'green'}, row=1, col=2)

        # Valid row/col and valid selector but the intersection is empty
        self.assert_select_traces(
            [], selector={'type': 'markers'}, row=3, col=1)
