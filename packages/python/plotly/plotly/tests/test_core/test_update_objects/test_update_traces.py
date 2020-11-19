from __future__ import absolute_import
from unittest import TestCase
import inspect
import copy
import pytest

import plotly.graph_objs as go
from plotly.subplots import make_subplots
from functools import reduce


class TestSelectForEachUpdateTraces(TestCase):
    def setUp(self):
        fig = make_subplots(
            rows=3,
            cols=2,
            specs=[
                [{}, {"type": "scene"}],
                [{"secondary_y": True}, {"type": "polar"}],
                [{"type": "domain", "colspan": 2}, None],
            ],
        ).update(layout={"height": 800})

        # data[0], (1, 1)
        fig.add_scatter(
            mode="markers",
            y=[2, 3, 1],
            name="A",
            marker={"color": "green", "size": 10},
            row=1,
            col=1,
        )

        # data[1], (1, 1)
        fig.add_bar(y=[2, 3, 1], row=1, col=1, name="B")

        # data[2], (2, 1)
        fig.add_scatter(
            mode="lines", y=[1, 2, 0], line={"color": "purple"}, name="C", row=2, col=1
        )

        # data[3], (2, 1)
        fig.add_heatmap(z=[[2, 3, 1], [2, 1, 3], [3, 2, 1]], row=2, col=1, name="D")

        # data[4], (1, 2)
        fig.add_scatter3d(
            x=[0, 0, 0],
            y=[0, 0, 0],
            z=[0, 1, 2],
            mode="markers",
            marker={"color": "green", "size": 10},
            name="E",
            row=1,
            col=2,
        )

        # data[5], (1, 2)
        fig.add_scatter3d(
            x=[0, 0, -1],
            y=[-1, 0, 0],
            z=[0, 1, 2],
            mode="lines",
            line={"color": "purple", "width": 4},
            name="F",
            row=1,
            col=2,
        )

        # data[6], (2, 2)
        fig.add_scatterpolar(
            mode="markers",
            r=[0, 3, 2],
            theta=[0, 20, 87],
            marker={"color": "green", "size": 8},
            name="G",
            row=2,
            col=2,
        )

        # data[7], (2, 2)
        fig.add_scatterpolar(
            mode="lines", r=[0, 3, 2], theta=[20, 87, 111], name="H", row=2, col=2
        )

        # data[8], (3, 1)
        fig.add_parcoords(
            dimensions=[{"values": [1, 2, 3, 2, 1]}, {"values": [3, 2, 1, 3, 2, 1]}],
            line={"color": "purple"},
            name="I",
            row=3,
            col=1,
        )

        # data[9], (2, 1) with secondary_y
        fig.add_scatter(
            mode="lines",
            y=[1, 2, 0],
            line={"color": "purple"},
            name="C",
            row=2,
            col=1,
            secondary_y=True,
        )

        self.fig = fig
        self.fig_no_grid = go.Figure(self.fig.to_dict())

    # select_traces and for_each_trace
    # --------------------------------
    def assert_select_traces(
        self,
        expected_inds,
        selector=None,
        row=None,
        col=None,
        secondary_y=None,
        test_no_grid=False,
    ):

        # Select traces on figure initialized with make_subplots
        trace_generator = self.fig.select_traces(
            selector=selector, row=row, col=col, secondary_y=secondary_y
        )
        self.assertTrue(inspect.isgenerator(trace_generator))

        trace_list = list(trace_generator)
        self.assertEqual(trace_list, [self.fig.data[i] for i in expected_inds])

        # Select traces on figure not containing subplot info
        if test_no_grid:
            trace_generator = self.fig_no_grid.select_traces(
                selector=selector, row=row, col=col, secondary_y=secondary_y
            )
            trace_list = list(trace_generator)
            self.assertEqual(
                trace_list, [self.fig_no_grid.data[i] for i in expected_inds]
            )

        # Test for each trace
        trace_list = []
        for_each_res = self.fig.for_each_trace(
            lambda t: trace_list.append(t),
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        )
        self.assertIs(for_each_res, self.fig)

        self.assertEqual(trace_list, [self.fig.data[i] for i in expected_inds])

    def test_select_by_type(self):
        self.assert_select_traces(
            [0, 2, 9], selector={"type": "scatter"}, test_no_grid=True
        )
        self.assert_select_traces([1], selector={"type": "bar"}, test_no_grid=True)
        self.assert_select_traces([3], selector={"type": "heatmap"}, test_no_grid=True)
        self.assert_select_traces(
            [4, 5], selector={"type": "scatter3d"}, test_no_grid=True
        )
        self.assert_select_traces(
            [6, 7], selector={"type": "scatterpolar"}, test_no_grid=True
        )
        self.assert_select_traces(
            [8], selector={"type": "parcoords"}, test_no_grid=True
        )
        self.assert_select_traces([], selector={"type": "pie"}, test_no_grid=True)

    def test_select_by_grid(self):
        # Row and column
        self.assert_select_traces([0, 1], row=1, col=1)
        self.assert_select_traces([2, 3, 9], row=2, col=1)
        self.assert_select_traces([4, 5], row=1, col=2)
        self.assert_select_traces([6, 7], row=2, col=2)
        self.assert_select_traces([8], row=3, col=1)

        # Row only
        self.assert_select_traces([0, 1, 4, 5], row=1)
        self.assert_select_traces([2, 3, 6, 7, 9], row=2)
        self.assert_select_traces([8], row=3)

        # Col only
        self.assert_select_traces([0, 1, 2, 3, 8, 9], col=1)
        self.assert_select_traces([4, 5, 6, 7], col=2)

    def test_select_by_secondary_y(self):
        self.assert_select_traces([2, 3, 9], row=2, col=1)
        self.assert_select_traces([2, 3], row=2, col=1, secondary_y=False)
        self.assert_select_traces([9], row=2, col=1, secondary_y=True)

    def test_select_by_property_across_trace_types(self):
        self.assert_select_traces(
            [0, 4, 6], selector={"mode": "markers"}, test_no_grid=True
        )
        self.assert_select_traces(
            [2, 5, 7, 9], selector={"mode": "lines"}, test_no_grid=True
        )
        self.assert_select_traces(
            [0, 4],
            selector={"marker": {"color": "green", "size": 10}},
            test_no_grid=True,
        )

        # Several traces have 'marker.color' == 'green', but they all have
        # additional marker properties so there should be no exact match.
        self.assert_select_traces(
            [], selector={"marker": {"color": "green"}}, test_no_grid=True
        )
        self.assert_select_traces(
            [0, 4, 6], selector={"marker.color": "green"}, test_no_grid=True
        )
        self.assert_select_traces(
            [2, 5, 8, 9], selector={"line.color": "purple"}, test_no_grid=True
        )

    def test_select_property_and_grid(self):
        # (1, 1)
        self.assert_select_traces([0], selector={"mode": "markers"}, row=1, col=1)
        self.assert_select_traces([1], selector={"type": "bar"}, row=1, col=1)

        # (2, 1)
        self.assert_select_traces([2, 9], selector={"mode": "lines"}, row=2, col=1)

        # (1, 2)
        self.assert_select_traces([4], selector={"marker.color": "green"}, row=1, col=2)

        # Valid row/col and valid selector but the intersection is empty
        self.assert_select_traces([], selector={"type": "markers"}, row=3, col=1)

    def test_select_with_function(self):
        def _check_trace_key(k, v):
            def f(t):
                try:
                    return t[k] == v
                except LookupError:
                    return False

            return f

        # (1, 1)
        self.assert_select_traces(
            [0], selector=_check_trace_key("mode", "markers"), row=1, col=1
        )
        self.assert_select_traces(
            [1], selector=_check_trace_key("type", "bar"), row=1, col=1
        )

        # (2, 1)
        self.assert_select_traces(
            [2, 9], selector=_check_trace_key("mode", "lines"), row=2, col=1
        )

        # (1, 2)
        self.assert_select_traces(
            [4], selector=_check_trace_key("marker.color", "green"), row=1, col=2
        )

        # Valid row/col and valid selector but the intersection is empty
        self.assert_select_traces(
            [], selector=_check_trace_key("type", "markers"), row=3, col=1
        )

    def test_select_traces_type_error(self):
        with self.assertRaises(TypeError):
            self.assert_select_traces([0], selector=123.456, row=1, col=1)

    def test_for_each_trace_lowercase_names(self):
        # Names are all uppercase to start
        original_names = [t.name for t in self.fig.data]
        self.assertTrue([str.isupper(n) for n in original_names])

        # Lower case names
        result_fig = self.fig.for_each_trace(lambda t: t.update(name=t.name.lower()))

        # Check chaning
        self.assertIs(result_fig, self.fig)

        # Check that names were altered
        self.assertTrue(
            all([t.name == n.lower() for t, n in zip(result_fig.data, original_names)])
        )

    # test update_traces
    # ------------------
    def assert_update_traces(
        self,
        expected_inds,
        patch=None,
        selector=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs
    ):
        # Save off original figure
        fig_orig = copy.deepcopy(self.fig)
        for trace1, trace2 in zip(fig_orig.data, self.fig.data):
            trace1.uid = trace2.uid

        # Perform update
        update_res = self.fig.update_traces(
            patch,
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
            **kwargs
        )

        # Check chaining support
        self.assertIs(update_res, self.fig)

        # Check resulting traces
        for i, (t_orig, t) in enumerate(zip(fig_orig.data, self.fig.data)):
            if i in expected_inds:
                # Check that traces are initially equal
                self.assertNotEqual(t_orig, t)

                # Check that traces are equal after update
                t_orig.update(patch, **kwargs)

            # Check that traces are equal
            self.assertEqual(t_orig, t)

    def test_update_traces_by_type(self):
        self.assert_update_traces(
            [0, 2, 9], {"visible": "legendonly"}, selector={"type": "scatter"}
        )

        self.assert_update_traces(
            [0, 2, 9], selector={"type": "scatter"}, visible=False
        )

        self.assert_update_traces(
            [1], {"visible": "legendonly"}, selector={"type": "bar"}
        )

        self.assert_update_traces(
            [3], {"colorscale": "Viridis"}, selector={"type": "heatmap"}
        )

        # Nest dictionaries
        self.assert_update_traces(
            [4, 5],
            {"marker": {"line": {"color": "yellow"}}},
            selector={"type": "scatter3d"},
        )

        # dot syntax
        self.assert_update_traces(
            [4, 5], {"marker.line.color": "cyan"}, selector={"type": "scatter3d"}
        )

        # underscore syntax
        self.assert_update_traces(
            [4, 5], dict(marker_line_color="pink"), selector={"type": "scatter3d"}
        )

        # underscore syntax with kwarg
        self.assert_update_traces(
            [4, 5], selector={"type": "scatter3d"}, marker_line_color="red"
        )

        self.assert_update_traces(
            [6, 7], {"line": {"dash": "dot"}}, selector={"type": "scatterpolar"}
        )

        # Nested dictionaries
        self.assert_update_traces(
            [8],
            {"dimensions": {1: {"label": "Dimension 1"}}},
            selector={"type": "parcoords"},
        )

        # Dot syntax
        self.assert_update_traces(
            [8], {"dimensions[1].label": "Dimension A"}, selector={"type": "parcoords"}
        )

        # underscore syntax
        # Dot syntax
        self.assert_update_traces(
            [8], dict(dimensions_1_label="Dimension X"), selector={"type": "parcoords"}
        )

        self.assert_update_traces(
            [], {"hoverinfo": "label+percent"}, selector={"type": "pie"}
        )

    def test_update_traces_by_grid_and_selector(self):
        self.assert_update_traces(
            [4, 6], {"marker.size": 5}, selector={"marker.color": "green"}, col=2
        )

        self.assert_update_traces(
            [0, 4], {"marker.size": 6}, selector={"marker.color": "green"}, row=1
        )

        self.assert_update_traces(
            [6], {"marker.size": 6}, selector={"marker.color": "green"}, row=2, col=2
        )

        self.assert_update_traces([9], {"marker.size": 6}, col=1, secondary_y=True)

    def test_update_traces_overwrite(self):
        fig = go.Figure(
            data=[go.Scatter(marker_line_color="red"), go.Bar(marker_line_color="red")]
        )

        fig.update_traces(overwrite=True, marker={"line": {"width": 10}})

        self.assertEqual(
            fig.to_plotly_json()["data"],
            [
                {"type": "scatter", "marker": {"line": {"width": 10}}},
                {"type": "bar", "marker": {"line": {"width": 10}}},
            ],
        )


@pytest.fixture
def select_traces_fixture():
    fig = make_subplots(2, 3)
    for n in range(3):
        fig.add_trace(go.Scatter(x=[1, 2], y=[3, n]), row=2, col=3)
    for n, ty in zip(range(3), [go.Scatter, go.Bar, go.Bar]):
        fig.add_trace(ty(x=[1, 2], y=[3, 10 * n]), row=1, col=3)
    return fig


def test_select_traces_integer(select_traces_fixture):
    fig = select_traces_fixture
    # check we can index last trace selected
    tr = list(fig.select_traces(selector=-1))[0]
    assert tr.y[1] == 20
    # check we can index last trace selected in a row and column
    tr = list(fig.select_traces(selector=-1, row=2, col=3))[0]
    assert tr.y[1] == 2
    # check that indexing out of bounds raises IndexError
    with pytest.raises(IndexError):
        tr = list(fig.select_traces(selector=6))[0]


def test_select_traces_string(select_traces_fixture):
    fig = select_traces_fixture
    # check we can select traces by type simply by passing a string to selector
    trs = list(fig.select_traces(selector="bar"))
    assert len(trs) == 2 and reduce(
        lambda last, cur: last
        and (cur[0]["type"] == "bar")
        and (cur[0]["y"][1] == cur[1]),
        zip(trs, [10, 20]),
        True,
    )
    # check we can select traces by type regardless of the subplots they are on
    trs = list(fig.select_traces(selector="scatter"))
    assert len(trs) == 4 and reduce(
        lambda last, cur: last
        and (cur[0]["type"] == "scatter")
        and (cur[0]["y"][1] == cur[1]),
        zip(trs, [0, 1, 2, 0]),
        True,
    )
    # check that we can select traces by type but only on a specific subplot
    trs = list(fig.select_traces(row=2, col=3, selector="scatter"))
    assert len(trs) == 3 and reduce(
        lambda last, cur: last
        and (cur[0]["type"] == "scatter")
        and (cur[0]["y"][1] == cur[1]),
        zip(trs, [0, 1, 2]),
        True,
    )
    # check that if selector matches no trace types then no traces are returned
    trs = list(fig.select_traces(selector="bogus"))
    assert len(trs) == 0
