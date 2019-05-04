from __future__ import absolute_import
from unittest import TestCase
import inspect
import copy

import plotly.graph_objs as go
from plotly.subplots import make_subplots
from _plotly_future_ import _future_flags


class TestSelectForEachUpdateTraces(TestCase):

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
        self.fig_no_grid = go.Figure(self.fig.to_dict())

    def tearDown(self):
        _future_flags.remove('v4_subplots')

    # select_traces and for_each_trace
    # --------------------------------
    def assert_select_traces(self, expected_inds, selector=None, row=None, col=None, test_no_grid=False):
        # Select traces on figure initialized with make_subplots
        trace_generator = self.fig.select_traces(
            selector=selector, row=row, col=col)
        self.assertTrue(inspect.isgenerator(trace_generator))

        trace_list = list(trace_generator)
        self.assertEqual(trace_list, [self.fig.data[i] for i in expected_inds])

        # Select traces on figure not containing subplot info
        if test_no_grid:
            trace_generator = self.fig_no_grid.select_traces(
                selector=selector, row=row, col=col)
            trace_list = list(trace_generator)
            self.assertEqual(trace_list, [self.fig_no_grid.data[i] for i in expected_inds])

        # Test for each trace
        trace_list = []
        for_each_res = self.fig.for_each_trace(
            lambda t: trace_list.append(t),
            selector=selector,
            row=row,
            col=col,
        )
        self.assertIs(for_each_res, self.fig)

        self.assertEqual(
            trace_list, [self.fig.data[i] for i in expected_inds])

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
        # Row and column
        self.assert_select_traces([0, 1], row=1, col=1)
        self.assert_select_traces([2, 3], row=2, col=1)
        self.assert_select_traces([4, 5], row=1, col=2)
        self.assert_select_traces([6, 7], row=2, col=2)
        self.assert_select_traces([8], row=3, col=1)

        # Row only
        self.assert_select_traces([0, 1, 4, 5], row=1)
        self.assert_select_traces([2, 3, 6, 7], row=2)
        self.assert_select_traces([8], row=3)

        # Col only
        self.assert_select_traces([0, 1, 2, 3, 8], col=1)
        self.assert_select_traces([4, 5, 6, 7], col=2)

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

    def test_for_each_trace_lowercase_names(self):
        # Names are all uppercase to start
        original_names = [t.name for t in self.fig.data]
        self.assertTrue([str.isupper(n) for n in original_names])

        # Lower case names
        result_fig = self.fig.for_each_trace(
            lambda t: t.update(name=t.name.lower())
        )

        # Check chaning
        self.assertIs(result_fig, self.fig)

        # Check that names were altered
        self.assertTrue(
            all([t.name == n.lower()
                 for t, n in zip(result_fig.data, original_names)]))

    # test update_traces
    # ------------------
    def assert_update_traces(
            self, patch, expected_inds, selector=None, row=None, col=None
    ):
        # Save off original figure
        fig_orig = copy.deepcopy(self.fig)
        for trace1, trace2 in zip(fig_orig.data, self.fig.data):
            trace1.uid = trace2.uid

        # Perform update
        update_res = self.fig.update_traces(
            patch, selector=selector, row=row, col=col
        )

        # Check chaining support
        self.assertIs(update_res, self.fig)

        # Check resulting traces
        for i, (t_orig, t) in enumerate(zip(fig_orig.data, self.fig.data)):
            if i in expected_inds:
                # Check that traces are initially equal
                self.assertNotEqual(t_orig, t)

                # Check that traces are equal after update
                t_orig.update(patch)

            # Check that traces are equal
            self.assertEqual(t_orig, t)

    def test_update_traces_by_type(self):
        self.assert_update_traces(
            {'visible': 'legendonly'},
            [0, 2],
            selector={'type': 'scatter'}
        )

        self.assert_update_traces(
            {'visible': 'legendonly'},
            [1],
            selector={'type': 'bar'},
        )

        self.assert_update_traces(
            {'colorscale': 'Viridis'},
            [3],
            selector={'type': 'heatmap'}
        )

        # Nest dictionaries
        self.assert_update_traces(
            {'marker': {'line': {'color': 'yellow'}}},
            [4, 5],
            selector={'type': 'scatter3d'}
        )

        # dot syntax
        self.assert_update_traces(
            {'marker.line.color': 'cyan'},
            [4, 5],
            selector={'type': 'scatter3d'}
        )

        # underscore syntax
        self.assert_update_traces(
            dict(marker_line_color='pink'),
            [4, 5],
            selector={'type': 'scatter3d'}
        )

        self.assert_update_traces(
            {'line': {'dash': 'dot'}},
            [6, 7],
            selector={'type': 'scatterpolar'}
        )

        # Nested dictionaries
        self.assert_update_traces(
            {'dimensions': {1: {'label': 'Dimension 1'}}},
            [8],
            selector={'type': 'parcoords'}
        )

        # Dot syntax
        self.assert_update_traces(
            {'dimensions[1].label': 'Dimension A'},
            [8],
            selector={'type': 'parcoords'}
        )

        # underscore syntax
        # Dot syntax
        self.assert_update_traces(
            dict(dimensions_1_label='Dimension X'),
            [8],
            selector={'type': 'parcoords'}
        )

        self.assert_update_traces(
            {'hoverinfo': 'label+percent'},
            [], selector={'type': 'pie'}
        )

    def test_update_traces_by_grid_and_selector(self):
        self.assert_update_traces(
            {'marker.size': 5},
            [4, 6],
            selector={'marker.color': 'green'},
            col=2
        )

        self.assert_update_traces(
            {'marker.size': 6},
            [0, 4],
            selector={'marker.color': 'green'},
            row=1
        )

        self.assert_update_traces(
            {'marker.size': 6},
            [6],
            selector={'marker.color': 'green'},
            row=2, col=2
        )
