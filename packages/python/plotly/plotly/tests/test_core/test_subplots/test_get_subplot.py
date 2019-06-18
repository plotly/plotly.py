from __future__ import absolute_import

from unittest import TestCase
from plotly.graph_objs import Figure
from plotly import subplots
import plotly.graph_objs as go
from plotly.subplots import SubplotXY, SubplotDomain


class TestGetSubplot(TestCase):
    def test_get_subplot(self):
        # Make Figure with subplot types
        fig = subplots.make_subplots(
            rows=4,
            cols=2,
            specs=[
                [{}, {"secondary_y": True}],
                [{"type": "polar"}, {"type": "ternary"}],
                [{"type": "scene"}, {"type": "geo"}],
                [{"type": "domain", "colspan": 2}, None],
            ],
        )

        fig.add_scatter(y=[2, 1, 3], row=1, col=1)
        fig.add_scatter(y=[2, 1, 3], row=1, col=2)
        fig.add_scatter(y=[1, 3, 2], row=1, col=2, secondary_y=True)
        fig.add_trace(go.Scatterpolar(r=[2, 1, 3], theta=[20, 50, 125]), row=2, col=1)
        fig.add_traces(
            [go.Scatterternary(a=[0.2, 0.1, 0.3], b=[0.4, 0.6, 0.5])],
            rows=[2],
            cols=[2],
        )
        fig.add_scatter3d(
            x=[2, 0, 1], y=[0, 1, 0], z=[0, 1, 2], mode="lines", row=3, col=1
        )
        fig.add_scattergeo(lat=[0, 40], lon=[10, 5], mode="lines", row=3, col=2)
        fig.add_parcats(
            dimensions=[
                {"values": ["A", "A", "B", "A", "B"]},
                {"values": ["a", "a", "a", "b", "b"]},
            ],
            row=4,
            col=1,
        )

        fig.update_traces(uid=None)
        fig.update(layout_height=1200)

        # Check
        expected = Figure(
            {
                "data": [
                    {"type": "scatter", "xaxis": "x", "y": [2, 1, 3], "yaxis": "y"},
                    {"type": "scatter", "xaxis": "x2", "y": [2, 1, 3], "yaxis": "y2"},
                    {"type": "scatter", "xaxis": "x2", "y": [1, 3, 2], "yaxis": "y3"},
                    {
                        "r": [2, 1, 3],
                        "subplot": "polar",
                        "theta": [20, 50, 125],
                        "type": "scatterpolar",
                    },
                    {
                        "a": [0.2, 0.1, 0.3],
                        "b": [0.4, 0.6, 0.5],
                        "subplot": "ternary",
                        "type": "scatterternary",
                    },
                    {
                        "mode": "lines",
                        "scene": "scene",
                        "type": "scatter3d",
                        "x": [2, 0, 1],
                        "y": [0, 1, 0],
                        "z": [0, 1, 2],
                    },
                    {
                        "geo": "geo",
                        "lat": [0, 40],
                        "lon": [10, 5],
                        "mode": "lines",
                        "type": "scattergeo",
                    },
                    {
                        "dimensions": [
                            {"values": ["A", "A", "B", "A", "B"]},
                            {"values": ["a", "a", "a", "b", "b"]},
                        ],
                        "domain": {"x": [0.0, 0.9400000000000001], "y": [0.0, 0.19375]},
                        "type": "parcats",
                    },
                ],
                "layout": {
                    "geo": {
                        "domain": {
                            "x": [0.5700000000000001, 0.9400000000000001],
                            "y": [0.26875, 0.4625],
                        }
                    },
                    "height": 1200,
                    "polar": {"domain": {"x": [0.0, 0.37], "y": [0.5375, 0.73125]}},
                    "scene": {"domain": {"x": [0.0, 0.37], "y": [0.26875, 0.4625]}},
                    "ternary": {
                        "domain": {
                            "x": [0.5700000000000001, 0.9400000000000001],
                            "y": [0.5375, 0.73125],
                        }
                    },
                    "xaxis": {"anchor": "y", "domain": [0.0, 0.37]},
                    "xaxis2": {
                        "anchor": "y2",
                        "domain": [0.5700000000000001, 0.9400000000000001],
                    },
                    "yaxis": {"anchor": "x", "domain": [0.80625, 1.0]},
                    "yaxis2": {"anchor": "x2", "domain": [0.80625, 1.0]},
                    "yaxis3": {"anchor": "x2", "overlaying": "y2", "side": "right"},
                },
            }
        )

        expected.update_traces(uid=None)

        # Make sure we have expected starting figure
        self.assertEqual(fig, expected)

        # (1, 1)
        subplot = fig.get_subplot(1, 1)
        self.assertEqual(
            subplot, SubplotXY(xaxis=fig.layout.xaxis, yaxis=fig.layout.yaxis)
        )

        # (1, 2) Primary
        subplot = fig.get_subplot(1, 2)
        self.assertEqual(
            subplot, SubplotXY(xaxis=fig.layout.xaxis2, yaxis=fig.layout.yaxis2)
        )

        # (1, 2) Primary
        subplot = fig.get_subplot(1, 2, secondary_y=True)
        self.assertEqual(
            subplot, SubplotXY(xaxis=fig.layout.xaxis2, yaxis=fig.layout.yaxis3)
        )

        # (2, 1)
        subplot = fig.get_subplot(2, 1)
        self.assertEqual(subplot, fig.layout.polar)

        # (2, 2)
        subplot = fig.get_subplot(2, 2)
        self.assertEqual(subplot, fig.layout.ternary)

        # (3, 1)
        subplot = fig.get_subplot(3, 1)
        self.assertEqual(subplot, fig.layout.scene)

        # (3, 2)
        subplot = fig.get_subplot(3, 2)
        self.assertEqual(subplot, fig.layout.geo)

        # (4, 1)
        subplot = fig.get_subplot(4, 1)
        domain = fig.data[-1].domain
        self.assertEqual(subplot, SubplotDomain(x=domain.x, y=domain.y))

    def test_get_subplot_out_of_bounds(self):
        fig = subplots.make_subplots(rows=4, cols=2)

        self.assertRaises(ValueError, lambda: fig.get_subplot(0, 1))
        self.assertRaises(ValueError, lambda: fig.get_subplot(5, 1))
        self.assertRaises(ValueError, lambda: fig.get_subplot(1, 0))
        self.assertRaises(ValueError, lambda: fig.get_subplot(1, 3))
