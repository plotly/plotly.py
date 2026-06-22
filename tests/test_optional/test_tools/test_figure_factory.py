import math

import plotly.figure_factory as ff

from plotly.exceptions import PlotlyError
from ...test_optional.optional_utils import NumpyTestUtilsMixin
from plotly.graph_objs import graph_objs
from ...utils import TestCaseNoTemplate


class TestQuiver(TestCaseNoTemplate, NumpyTestUtilsMixin):
    def test_unequal_xy_length(self):
        # check: PlotlyError if x and y are not the same length

        kwargs = {"x": [1, 2], "y": [1], "u": [1, 2], "v": [1, 2]}
        self.assertRaises(PlotlyError, ff.create_quiver, **kwargs)

    def test_wrong_scale(self):
        # check: ValueError if scale is <= 0

        kwargs = {"x": [1, 2], "y": [1, 2], "u": [1, 2], "v": [1, 2], "scale": -1}
        self.assertRaises(ValueError, ff.create_quiver, **kwargs)

        kwargs = {"x": [1, 2], "y": [1, 2], "u": [1, 2], "v": [1, 2], "scale": 0}
        self.assertRaises(ValueError, ff.create_quiver, **kwargs)

    def test_wrong_arrow_scale(self):
        # check: ValueError if arrow_scale is <= 0

        kwargs = {"x": [1, 2], "y": [1, 2], "u": [1, 2], "v": [1, 2], "arrow_scale": -1}
        self.assertRaises(ValueError, ff.create_quiver, **kwargs)

        kwargs = {"x": [1, 2], "y": [1, 2], "u": [1, 2], "v": [1, 2], "arrow_scale": 0}
        self.assertRaises(ValueError, ff.create_quiver, **kwargs)

    def test_one_arrow(self):
        # we should be able to create a single arrow using create_quiver

        quiver = ff.create_quiver(x=[1], y=[1], u=[1], v=[1], scale=1)
        expected_quiver = {
            "data": [
                {
                    "mode": "lines",
                    "type": "scatter",
                    "x": [1, 2, None, 1.820698256761928, 2, 1.615486170766527, None],
                    "y": [1, 2, None, 1.615486170766527, 2, 1.820698256761928, None],
                }
            ],
            "layout": {"hovermode": "closest"},
        }
        self.assert_fig_equal(quiver["data"][0], expected_quiver["data"][0])
        self.assert_fig_equal(quiver["layout"], expected_quiver["layout"])

    def test_more_kwargs(self):
        # we should be able to create 2 arrows and change the arrow_scale,
        # angle, and arrow using create_quiver

        quiver = ff.create_quiver(
            x=[1, 2],
            y=[1, 2],
            u=[math.cos(1), math.cos(2)],
            v=[math.sin(1), math.sin(2)],
            arrow_scale=0.4,
            angle=math.pi / 6,
            line=graph_objs.scatter.Line(color="purple", width=3),
        )
        expected_quiver = {
            "data": [
                {
                    "line": {"color": "purple", "width": 3},
                    "mode": "lines",
                    "type": "scatter",
                    "x": [
                        1,
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
                        None,
                    ],
                    "y": [
                        1,
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
                        None,
                    ],
                }
            ],
            "layout": {"hovermode": "closest"},
        }
        self.assert_fig_equal(quiver["data"][0], expected_quiver["data"][0])
        self.assert_fig_equal(quiver["layout"], expected_quiver["layout"])


class TestTable(TestCaseNoTemplate, NumpyTestUtilsMixin):
    def test_fontcolor_input(self):
        # check: ValueError if fontcolor input is incorrect

        kwargs = {
            "table_text": [["one", "two"], [1, 2], [1, 2], [1, 2]],
            "fontcolor": "#000000",
        }
        self.assertRaises(ValueError, ff.create_table, **kwargs)

        kwargs = {
            "table_text": [["one", "two"], [1, 2], [1, 2], [1, 2]],
            "fontcolor": ["red", "blue"],
        }
        self.assertRaises(ValueError, ff.create_table, **kwargs)

    def test_simple_table(self):
        # we should be able to create a striped table by supplying a text matrix

        text = [
            ["Country", "Year", "Population"],
            ["US", 2000, 282200000],
            ["Canada", 2000, 27790000],
            ["US", 1980, 226500000],
        ]
        table = ff.create_table(text)
        expected_table = {
            "data": [
                {
                    "colorscale": [[0, "#00083e"], [0.5, "#ededee"], [1, "#ffffff"]],
                    "hoverinfo": "none",
                    "opacity": 0.75,
                    "showscale": False,
                    "type": "heatmap",
                    "z": [[0, 0, 0], [0.5, 0.5, 0.5], [1, 1, 1], [0.5, 0.5, 0.5]],
                }
            ],
            "layout": {
                "annotations": [
                    {
                        "align": "left",
                        "font": {"color": "#ffffff"},
                        "showarrow": False,
                        "text": "<b>Country</b>",
                        "x": -0.45,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 0,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#ffffff"},
                        "showarrow": False,
                        "text": "<b>Year</b>",
                        "x": 0.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 0,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#ffffff"},
                        "showarrow": False,
                        "text": "<b>Population</b>",
                        "x": 1.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 0,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "US",
                        "x": -0.45,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 1,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "2000",
                        "x": 0.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 1,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "282200000",
                        "x": 1.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 1,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "Canada",
                        "x": -0.45,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 2,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "2000",
                        "x": 0.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 2,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "27790000",
                        "x": 1.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 2,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "US",
                        "x": -0.45,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 3,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "1980",
                        "x": 0.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 3,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "226500000",
                        "x": 1.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 3,
                        "yref": "y",
                    },
                ],
                "height": 170,
                "margin": {"b": 0, "l": 0, "r": 0, "t": 0},
                "xaxis": {
                    "dtick": 1,
                    "gridwidth": 2,
                    "showticklabels": False,
                    "tick0": -0.5,
                    "ticks": "",
                    "zeroline": False,
                },
                "yaxis": {
                    "autorange": "reversed",
                    "dtick": 1,
                    "gridwidth": 2,
                    "showticklabels": False,
                    "tick0": 0.5,
                    "ticks": "",
                    "zeroline": False,
                },
            },
        }

        self.assert_fig_equal(table["data"][0], expected_table["data"][0])

        self.assert_fig_equal(table["layout"], expected_table["layout"])

    def test_table_with_index(self):
        # we should be able to create a striped table where the first column
        # matches the coloring of the header

        text = [
            ["Country", "Year", "Population"],
            ["US", 2000, 282200000],
            ["Canada", 2000, 27790000],
        ]
        index_table = ff.create_table(text, index=True, index_title="Title")
        exp_index_table = {
            "data": [
                {
                    "colorscale": [[0, "#00083e"], [0.5, "#ededee"], [1, "#ffffff"]],
                    "hoverinfo": "none",
                    "opacity": 0.75,
                    "showscale": False,
                    "type": "heatmap",
                    "z": [[0, 0, 0], [0, 0.5, 0.5], [0, 1, 1]],
                }
            ],
            "layout": {
                "annotations": [
                    {
                        "align": "left",
                        "font": {"color": "#ffffff"},
                        "showarrow": False,
                        "text": "<b>Country</b>",
                        "x": -0.45,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 0,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#ffffff"},
                        "showarrow": False,
                        "text": "<b>Year</b>",
                        "x": 0.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 0,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#ffffff"},
                        "showarrow": False,
                        "text": "<b>Population</b>",
                        "x": 1.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 0,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#ffffff"},
                        "showarrow": False,
                        "text": "<b>US</b>",
                        "x": -0.45,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 1,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "2000",
                        "x": 0.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 1,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "282200000",
                        "x": 1.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 1,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#ffffff"},
                        "showarrow": False,
                        "text": "<b>Canada</b>",
                        "x": -0.45,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 2,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "2000",
                        "x": 0.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 2,
                        "yref": "y",
                    },
                    {
                        "align": "left",
                        "font": {"color": "#000000"},
                        "showarrow": False,
                        "text": "27790000",
                        "x": 1.55,
                        "xanchor": "left",
                        "xref": "x",
                        "y": 2,
                        "yref": "y",
                    },
                ],
                "height": 140,
                "margin": {"b": 0, "l": 0, "r": 0, "t": 0},
                "xaxis": {
                    "dtick": 1,
                    "gridwidth": 2,
                    "showticklabels": False,
                    "tick0": -0.5,
                    "ticks": "",
                    "zeroline": False,
                },
                "yaxis": {
                    "autorange": "reversed",
                    "dtick": 1,
                    "gridwidth": 2,
                    "showticklabels": False,
                    "tick0": 0.5,
                    "ticks": "",
                    "zeroline": False,
                },
            },
        }

        self.assert_fig_equal(index_table["data"][0], exp_index_table["data"][0])

        self.assert_fig_equal(index_table["layout"], exp_index_table["layout"])
