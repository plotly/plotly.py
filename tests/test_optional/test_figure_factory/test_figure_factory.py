from plotly import optional_imports
from plotly.graph_objs import graph_objs as go
from plotly.exceptions import PlotlyError

import plotly.figure_factory as ff
from ...test_optional.optional_utils import NumpyTestUtilsMixin
from ...test_optional.test_utils.test_utils import np_inf

import numpy as np
from ...utils import TestCaseNoTemplate
from scipy.spatial import Delaunay
import pandas as pd

shapely = optional_imports.get_module("shapely")
shapefile = optional_imports.get_module("shapefile")
gp = optional_imports.get_module("geopandas")
sk_measure = optional_imports.get_module("skimage")


class TestStreamline(TestCaseNoTemplate):
    def test_wrong_arrow_scale(self):
        # check for ValueError if arrow_scale is <= 0

        kwargs = {
            "x": [0, 2],
            "y": [0, 2],
            "u": [[-1, -5], [-1, -5]],
            "v": [[1, 1], [-3, -3]],
            "arrow_scale": 0,
        }
        self.assertRaises(ValueError, ff.create_streamline, **kwargs)

    def test_wrong_density(self):
        # check for ValueError if density is <= 0

        kwargs = {
            "x": [0, 2],
            "y": [0, 2],
            "u": [[-1, -5], [-1, -5]],
            "v": [[1, 1], [-3, -3]],
            "density": 0,
        }
        self.assertRaises(ValueError, ff.create_streamline, **kwargs)

    def test_uneven_x(self):
        # check for PlotlyError if x is not evenly spaced

        kwargs = {
            "x": [0, 2, 7, 9],
            "y": [0, 2, 4, 6],
            "u": [[-1, -5], [-1, -5]],
            "v": [[1, 1], [-3, -3]],
        }
        self.assertRaises(PlotlyError, ff.create_streamline, **kwargs)

    def test_uneven_y(self):
        # check for PlotlyError if y is not evenly spaced

        kwargs = {
            "x": [0, 2, 4, 6],
            "y": [1.5, 2, 3, 3.5],
            "u": [[-1, -5], [-1, -5]],
            "v": [[1, 1], [-3, -3]],
        }
        self.assertRaises(PlotlyError, ff.create_streamline, **kwargs)

    def test_unequal_length_xy(self):
        # check for PlotlyError if u and v are not the same length

        kwargs = {
            "x": [0, 2, 4, 6],
            "y": [1.5, 2, 3.5],
            "u": [[-1, -5], [-1, -5]],
            "v": [[1, 1], [-3, -3]],
        }
        self.assertRaises(PlotlyError, ff.create_streamline, **kwargs)

    def test_unequal_length_uv(self):
        # check for PlotlyError if u and v are not the same length

        kwargs = {
            "x": [0, 2, 4, 6],
            "y": [1.5, 2, 3, 3.5],
            "u": [[-1, -5], [-1, -5], [-1, -5]],
            "v": [[1, 1], [-3, -3]],
        }
        self.assertRaises(PlotlyError, ff.create_streamline, **kwargs)

    def test_simple_streamline(self):
        # Need np to check streamline data,
        # this checks that the first 101 x and y values from streamline are
        # what we expect for a simple streamline where:
        # x = np.linspace(-1, 1, 3)
        # y = np.linspace(-1, 1, 3)
        # Y, X = np.meshgrid(x, y)
        # u = X**2
        # v = Y**2
        # u = u.T #transpose
        # v = v.T #transpose

        strln = ff.create_streamline(
            x=[-1.0, 0.0, 1.0],
            y=[-1.0, 0.0, 1.0],
            u=[[1.0, 0.0, 1.0], [1.0, 0.0, 1.0], [1.0, 0.0, 1.0]],
            v=[[1.0, 1.0, 1.0], [0.0, 0.0, 0.0], [1.0, 1.0, 1.0]],
        )
        expected_strln_0_100 = {
            "y": [
                -1.0,
                -0.9788791845863757,
                -0.9579399744939614,
                -0.9371777642073374,
                -0.9165881396413338,
                -0.8961668671832106,
                -0.8759098835283448,
                -0.8558132862403048,
                -0.835873324973195,
                -0.8160863933003534,
                -0.7964490210989816,
                -0.7769578674451656,
                -0.7576097139780906,
                -0.7384014586961288,
                -0.7193301101509343,
                -0.7003927820087748,
                -0.681586687951103,
                -0.6629091368888596,
                -0.64435752846723,
                -0.6259293488396024,
                -0.6076221666912738,
                -0.5894336294951057,
                -0.5713614599827976,
                -0.5534034528167977,
                -0.5355574714490806,
                -0.5178214451541254,
                -0.5001933662244311,
                -0.4826712873178177,
                -0.4652533189465894,
                -0.44793762709939944,
                -0.4307224309873414,
                -0.4136060009064273,
                -0.39658665620919065,
                -0.3796627633786812,
                -0.3628327341986042,
                -0.34609502401380254,
                -0.3294481300756896,
                -0.31289058996761565,
                -0.2964209801054992,
                -0.28003791430937197,
                -0.2637400424417804,
                -0.24752604910925968,
                -0.23139465242334434,
                -0.21534460281781365,
                -0.19937468191908325,
                -0.18348370146685278,
                -0.1676705022823033,
                -0.15193395328130999,
                -0.13627295053029143,
                -0.1206864163424669,
                -0.10517329841242584,
                -0.08973256898704507,
                -0.07436322407090357,
                -0.05906428266445696,
                -0.04383478603333624,
                -0.028673797007230273,
                -0.013580399306900914,
                0.0014484211645073852,
                0.01648792568956914,
                0.03159429687713278,
                0.04676843461935776,
                0.062011259175942746,
                0.07732371182540754,
                0.09270675554339824,
                0.10816137570939799,
                0.12368858084331191,
                0.1392894033734846,
                0.1549649004378033,
                0.1707161547196483,
                0.1865442753205595,
                0.20245039867161063,
                0.21843568948560943,
                0.23450134175238246,
                0.25064857977955146,
                0.26687865928136767,
                0.2831928685183458,
                0.29959252949062387,
                0.3160789991881776,
                0.33265367090123643,
                0.3493179755944802,
                0.366073383348855,
                0.3829214048751186,
                0.39986359310352526,
                0.41690154485438513,
                0.4340369025945845,
                0.4512713562855355,
                0.46860664532844054,
                0.4860445606132082,
                0.5035869466778524,
                0.5212357039857456,
                0.5389927913286829,
                0.5568602283643591,
                0.5748400982975623,
                0.5929345507151613,
                0.6111458045858065,
                0.6294761514361948,
                0.6479279587167714,
                0.6665036733708583,
                0.6852058256224467,
                0.704037032999252,
            ],
            "x": [
                -1.0,
                -0.9788791845863756,
                -0.9579399744939614,
                -0.9371777642073374,
                -0.9165881396413338,
                -0.8961668671832106,
                -0.8759098835283448,
                -0.8558132862403048,
                -0.835873324973195,
                -0.8160863933003534,
                -0.7964490210989816,
                -0.7769578674451656,
                -0.7576097139780906,
                -0.7384014586961289,
                -0.7193301101509344,
                -0.7003927820087748,
                -0.6815866879511031,
                -0.6629091368888596,
                -0.6443575284672302,
                -0.6259293488396025,
                -0.6076221666912739,
                -0.5894336294951058,
                -0.5713614599827976,
                -0.5534034528167978,
                -0.5355574714490807,
                -0.5178214451541254,
                -0.5001933662244312,
                -0.4826712873178177,
                -0.4652533189465894,
                -0.44793762709939944,
                -0.4307224309873414,
                -0.4136060009064273,
                -0.39658665620919065,
                -0.3796627633786812,
                -0.3628327341986042,
                -0.34609502401380254,
                -0.3294481300756896,
                -0.31289058996761565,
                -0.2964209801054992,
                -0.28003791430937197,
                -0.2637400424417804,
                -0.24752604910925968,
                -0.23139465242334434,
                -0.21534460281781365,
                -0.19937468191908325,
                -0.18348370146685278,
                -0.1676705022823033,
                -0.15193395328130999,
                -0.13627295053029143,
                -0.1206864163424669,
                -0.10517329841242584,
                -0.08973256898704507,
                -0.07436322407090357,
                -0.05906428266445696,
                -0.04383478603333624,
                -0.028673797007230273,
                -0.013580399306900914,
                0.0014484211645073852,
                0.01648792568956914,
                0.03159429687713278,
                0.04676843461935776,
                0.062011259175942746,
                0.07732371182540754,
                0.09270675554339824,
                0.10816137570939799,
                0.12368858084331191,
                0.1392894033734846,
                0.1549649004378033,
                0.1707161547196483,
                0.1865442753205595,
                0.20245039867161063,
                0.21843568948560943,
                0.23450134175238246,
                0.25064857977955146,
                0.26687865928136767,
                0.2831928685183458,
                0.29959252949062387,
                0.3160789991881776,
                0.33265367090123643,
                0.3493179755944802,
                0.366073383348855,
                0.3829214048751186,
                0.39986359310352526,
                0.41690154485438513,
                0.4340369025945845,
                0.4512713562855355,
                0.46860664532844054,
                0.4860445606132082,
                0.5035869466778524,
                0.5212357039857456,
                0.5389927913286829,
                0.5568602283643591,
                0.5748400982975623,
                0.5929345507151613,
                0.6111458045858065,
                0.6294761514361948,
                0.6479279587167714,
                0.6665036733708583,
                0.6852058256224467,
                0.704037032999252,
            ],
            "type": "scatter",
            "mode": "lines",
        }
        self.assertListEqual(
            list(strln["data"][0]["y"][0:100]), expected_strln_0_100["y"]
        )
        self.assertListEqual(
            list(strln["data"][0]["x"][0:100]), expected_strln_0_100["x"]
        )


class TestDendrogram(NumpyTestUtilsMixin, TestCaseNoTemplate):
    def test_default_dendrogram(self):
        X = np.array([[1, 2, 3, 4], [1, 1, 3, 4], [1, 2, 1, 4], [1, 2, 3, 1]])
        dendro = ff.create_dendrogram(X=X)

        expected_dendro = go.Figure(
            data=[
                go.Scatter(
                    x=np.array([25.0, 25.0, 35.0, 35.0]),
                    y=np.array([0.0, 1.0, 1.0, 0.0]),
                    marker=go.scatter.Marker(color="rgb(61,153,112)"),
                    mode="lines",
                    xaxis="x",
                    yaxis="y",
                    hoverinfo="text",
                    text=None,
                ),
                go.Scatter(
                    x=np.array([15.0, 15.0, 30.0, 30.0]),
                    y=np.array([0.0, 2.23606798, 2.23606798, 1.0]),
                    marker=go.scatter.Marker(color="rgb(61,153,112)"),
                    mode="lines",
                    xaxis="x",
                    yaxis="y",
                    hoverinfo="text",
                    text=None,
                ),
                go.Scatter(
                    x=np.array([5.0, 5.0, 22.5, 22.5]),
                    y=np.array([0.0, 3.60555128, 3.60555128, 2.23606798]),
                    marker=go.scatter.Marker(color="rgb(0,116,217)"),
                    mode="lines",
                    xaxis="x",
                    yaxis="y",
                    hoverinfo="text",
                    text=None,
                ),
            ],
            layout=go.Layout(
                autosize=False,
                height=np_inf(),
                hovermode="closest",
                showlegend=False,
                width=np_inf(),
                xaxis=go.layout.XAxis(
                    mirror="allticks",
                    rangemode="tozero",
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    tickmode="array",
                    ticks="outside",
                    ticktext=np.array(["3", "2", "0", "1"]),
                    tickvals=[5.0, 15.0, 25.0, 35.0],
                    type="linear",
                    zeroline=False,
                ),
                yaxis=go.layout.YAxis(
                    mirror="allticks",
                    rangemode="tozero",
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    ticks="outside",
                    type="linear",
                    zeroline=False,
                ),
            ),
        )

        self.assertEqual(len(dendro["data"]), 3)

        # this is actually a bit clearer when debugging tests.
        self.assert_fig_equal(dendro["data"][0], expected_dendro["data"][0])
        self.assert_fig_equal(dendro["data"][1], expected_dendro["data"][1])
        self.assert_fig_equal(dendro["data"][2], expected_dendro["data"][2])

        self.assert_fig_equal(dendro["layout"], expected_dendro["layout"])

    def test_dendrogram_random_matrix(self):
        # create a random uncorrelated matrix
        X = np.random.rand(5, 5)

        # variable 2 is correlated with all the other variables
        X[2, :] = sum(X, 0)

        names = ["Jack", "Oxana", "John", "Chelsea", "Mark"]
        dendro = ff.create_dendrogram(X, labels=names)

        expected_dendro = go.Figure(
            data=[
                go.Scatter(
                    marker=go.scatter.Marker(color="rgb(61,153,112)"),
                    mode="lines",
                    xaxis="x",
                    yaxis="y",
                    hoverinfo="text",
                    text=None,
                ),
                go.Scatter(
                    marker=go.scatter.Marker(color="rgb(61,153,112)"),
                    mode="lines",
                    xaxis="x",
                    yaxis="y",
                    hoverinfo="text",
                    text=None,
                ),
                go.Scatter(
                    marker=go.scatter.Marker(color="rgb(61,153,112)"),
                    mode="lines",
                    xaxis="x",
                    yaxis="y",
                    hoverinfo="text",
                    text=None,
                ),
                go.Scatter(
                    marker=go.scatter.Marker(color="rgb(0,116,217)"),
                    mode="lines",
                    xaxis="x",
                    yaxis="y",
                    hoverinfo="text",
                    text=None,
                ),
            ],
            layout=go.Layout(
                autosize=False,
                height=np_inf(),
                hovermode="closest",
                showlegend=False,
                width=np_inf(),
                xaxis=go.layout.XAxis(
                    mirror="allticks",
                    rangemode="tozero",
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    tickmode="array",
                    ticks="outside",
                    tickvals=[5.0, 15.0, 25.0, 35.0, 45.0],
                    type="linear",
                    zeroline=False,
                ),
                yaxis=go.layout.YAxis(
                    mirror="allticks",
                    rangemode="tozero",
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    ticks="outside",
                    type="linear",
                    zeroline=False,
                ),
            ),
        )

        self.assertEqual(len(dendro["data"]), 4)

        # it's random, so we can only check that the values aren't equal
        y_vals = [
            dendro["data"][0].to_plotly_json().pop("y"),
            dendro["data"][1].to_plotly_json().pop("y"),
            dendro["data"][2].to_plotly_json().pop("y"),
            dendro["data"][3].to_plotly_json().pop("y"),
        ]
        for i in range(len(y_vals)):
            for j in range(len(y_vals)):
                if i != j:
                    self.assertFalse(np.allclose(y_vals[i], y_vals[j]))

        x_vals = [
            dendro["data"][0].to_plotly_json().pop("x"),
            dendro["data"][1].to_plotly_json().pop("x"),
            dendro["data"][2].to_plotly_json().pop("x"),
            dendro["data"][3].to_plotly_json().pop("x"),
        ]
        for i in range(len(x_vals)):
            for j in range(len(x_vals)):
                if i != j:
                    self.assertFalse(np.allclose(x_vals[i], x_vals[j]))

        # we also need to check the ticktext manually
        xaxis_ticktext = dendro["layout"].to_plotly_json()["xaxis"].pop("ticktext")
        self.assertEqual(xaxis_ticktext[0], "John")

        # this is actually a bit clearer when debugging tests.
        self.assert_fig_equal(
            dendro["data"][0], expected_dendro["data"][0], ignore=["uid", "x", "y"]
        )
        self.assert_fig_equal(
            dendro["data"][1], expected_dendro["data"][1], ignore=["uid", "x", "y"]
        )
        self.assert_fig_equal(
            dendro["data"][2], expected_dendro["data"][2], ignore=["uid", "x", "y"]
        )
        self.assert_fig_equal(
            dendro["data"][3], expected_dendro["data"][3], ignore=["uid", "x", "y"]
        )

        # layout except xaxis
        self.assert_fig_equal(
            dendro["layout"], expected_dendro["layout"], ignore=["xaxis"]
        )

        # xaxis
        self.assert_fig_equal(
            dendro["layout"]["xaxis"],
            expected_dendro["layout"]["xaxis"],
            ignore=["ticktext"],
        )

    def test_dendrogram_orientation(self):
        X = np.random.rand(5, 5)

        dendro_left = ff.create_dendrogram(X, orientation="left")
        self.assertEqual(len(dendro_left["layout"]["yaxis"]["ticktext"]), 5)
        tickvals_left = np.array(dendro_left["layout"]["yaxis"]["tickvals"])
        self.assertTrue((tickvals_left <= 0).all())

        dendro_right = ff.create_dendrogram(X, orientation="right")
        tickvals_right = np.array(dendro_right["layout"]["yaxis"]["tickvals"])
        self.assertTrue((tickvals_right >= 0).all())

        dendro_bottom = ff.create_dendrogram(X, orientation="bottom")
        self.assertEqual(len(dendro_bottom["layout"]["xaxis"]["ticktext"]), 5)
        tickvals_bottom = np.array(dendro_bottom["layout"]["xaxis"]["tickvals"])
        self.assertTrue((tickvals_bottom >= 0).all())

        dendro_top = ff.create_dendrogram(X, orientation="top")
        tickvals_top = np.array(dendro_top["layout"]["xaxis"]["tickvals"])
        self.assertTrue((tickvals_top <= 0).all())

    def test_dendrogram_colorscale(self):
        X = np.array([[1, 2, 3, 4], [1, 1, 3, 4], [1, 2, 1, 4], [1, 2, 3, 1]])
        greyscale = [
            "rgb(0,0,0)",  # black
            "rgb(05,105,105)",  # dim grey
            "rgb(128,128,128)",  # grey
            "rgb(169,169,169)",  # dark grey
            "rgb(192,192,192)",  # silver
            "rgb(211,211,211)",  # light grey
            "rgb(220,220,220)",  # gainsboro
            "rgb(245,245,245)",  # white smoke
        ]

        dendro = ff.create_dendrogram(X, colorscale=greyscale)

        expected_dendro = go.Figure(
            data=[
                go.Scatter(
                    x=np.array([25.0, 25.0, 35.0, 35.0]),
                    y=np.array([0.0, 1.0, 1.0, 0.0]),
                    marker=go.scatter.Marker(color="rgb(128,128,128)"),
                    mode="lines",
                    xaxis="x",
                    yaxis="y",
                    hoverinfo="text",
                    text=None,
                ),
                go.Scatter(
                    x=np.array([15.0, 15.0, 30.0, 30.0]),
                    y=np.array([0.0, 2.23606798, 2.23606798, 1.0]),
                    marker=go.scatter.Marker(color="rgb(128,128,128)"),
                    mode="lines",
                    xaxis="x",
                    yaxis="y",
                    hoverinfo="text",
                    text=None,
                ),
                go.Scatter(
                    x=np.array([5.0, 5.0, 22.5, 22.5]),
                    y=np.array([0.0, 3.60555128, 3.60555128, 2.23606798]),
                    marker=go.scatter.Marker(color="rgb(0,0,0)"),
                    mode="lines",
                    xaxis="x",
                    yaxis="y",
                    hoverinfo="text",
                    text=None,
                ),
            ],
            layout=go.Layout(
                autosize=False,
                height=np_inf(),
                hovermode="closest",
                showlegend=False,
                width=np_inf(),
                xaxis=go.layout.XAxis(
                    mirror="allticks",
                    rangemode="tozero",
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    tickmode="array",
                    ticks="outside",
                    ticktext=np.array(["3", "2", "0", "1"]),
                    tickvals=[5.0, 15.0, 25.0, 35.0],
                    type="linear",
                    zeroline=False,
                ),
                yaxis=go.layout.YAxis(
                    mirror="allticks",
                    rangemode="tozero",
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    ticks="outside",
                    type="linear",
                    zeroline=False,
                ),
            ),
        )

        self.assertEqual(len(dendro["data"]), 3)

        # this is actually a bit clearer when debugging tests.
        self.assert_fig_equal(dendro["data"][0], expected_dendro["data"][0])
        self.assert_fig_equal(dendro["data"][1], expected_dendro["data"][1])
        self.assert_fig_equal(dendro["data"][2], expected_dendro["data"][2])

    def test_dendrogram_ticklabels(self):
        X = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 3, 5, 6], [1, 4, 2, 3]])
        dendro = ff.create_dendrogram(X=X)

        self.assertEqual(len(dendro.layout.xaxis.ticktext), 4)
        self.assertEqual(len(dendro.layout.xaxis.tickvals), 4)


class TestTrisurf(NumpyTestUtilsMixin, TestCaseNoTemplate):
    def test_vmin_and_vmax(self):
        # check if vmin is greater than or equal to vmax
        u = np.linspace(0, 2, 2)
        v = np.linspace(0, 2, 2)
        u, v = np.meshgrid(u, v)
        u = u.flatten()
        v = v.flatten()

        x = u
        y = v
        z = u * v

        points2D = np.vstack([u, v]).T
        tri = Delaunay(points2D)
        simplices = tri.simplices

        pattern = (
            "Incorrect relation between vmin and vmax. The vmin value cannot "
            "be bigger than or equal to the value of vmax."
        )

        self.assertRaisesRegex(
            PlotlyError, pattern, ff.create_trisurf, x, y, z, simplices
        )

    def test_valid_colormap(self):
        # create data for trisurf plot
        u = np.linspace(-np.pi, np.pi, 3)
        v = np.linspace(-np.pi, np.pi, 3)
        u, v = np.meshgrid(u, v)
        u = u.flatten()
        v = v.flatten()

        x = u
        y = u * np.cos(v)
        z = u * np.sin(v)

        points2D = np.vstack([u, v]).T
        tri = Delaunay(points2D)
        simplices = tri.simplices

        # check that a valid plotly colorscale string is entered

        pattern = (
            "If your colors variable is a string, it must be a Plotly scale, "
            "an rgb color or a hex color."
        )

        self.assertRaisesRegex(
            PlotlyError, pattern, ff.create_trisurf, x, y, z, simplices, colormap="foo"
        )

        # check: if colormap is a list of rgb color strings, make sure the
        # entries of each color are no greater than 255.0

        pattern2 = "Whoops! The elements in your rgb colors tuples cannot exceed 255.0."

        self.assertRaisesRegex(
            PlotlyError,
            pattern2,
            ff.create_trisurf,
            x,
            y,
            z,
            simplices,
            colormap=["rgb(4, 5, 600)"],
        )

        # check: if colormap is a list of tuple colors, make sure the entries
        # of each tuple are no greater than 1.0

        pattern3 = "Whoops! The elements in your colors tuples cannot exceed 1.0."

        self.assertRaisesRegex(
            PlotlyError,
            pattern3,
            ff.create_trisurf,
            x,
            y,
            z,
            simplices,
            colormap=[(0.8, 1.0, 1.2)],
        )

    def test_trisurf_all_args(self):
        # check if trisurf plot matches with expected output
        u = np.linspace(-1, 1, 3)
        v = np.linspace(-1, 1, 3)
        u, v = np.meshgrid(u, v)
        u = u.flatten()
        v = v.flatten()

        x = u
        y = v
        z = u * v

        points2D = np.vstack([u, v]).T
        tri = Delaunay(points2D)
        simplices = tri.simplices

        test_trisurf_plot = ff.create_trisurf(x, y, z, simplices)

        exp_trisurf_plot = {
            "data": [
                {
                    "facecolor": [
                        "rgb(143, 123, 97)",
                        "rgb(255, 127, 14)",
                        "rgb(143, 123, 97)",
                        "rgb(31, 119, 180)",
                        "rgb(143, 123, 97)",
                        "rgb(31, 119, 180)",
                        "rgb(143, 123, 97)",
                        "rgb(255, 127, 14)",
                    ],
                    "i": [3, 1, 1, 5, 7, 3, 5, 7],
                    "j": [1, 3, 5, 1, 3, 7, 7, 5],
                    "k": [4, 0, 4, 2, 4, 6, 4, 8],
                    "name": "",
                    "type": "mesh3d",
                    "x": [-1.0, 0.0, 1.0, -1.0, 0.0, 1.0, -1.0, 0.0, 1.0],
                    "y": [-1.0, -1.0, -1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                    "z": [1.0, -0.0, -1.0, -0.0, 0.0, 0.0, -1.0, 0.0, 1.0],
                },
                {
                    "line": {"color": "rgb(50, 50, 50)", "width": 1.5},
                    "mode": "lines",
                    "showlegend": False,
                    "type": "scatter3d",
                    "x": [
                        -1.0,
                        0.0,
                        0.0,
                        -1.0,
                        None,
                        0.0,
                        -1.0,
                        -1.0,
                        0.0,
                        None,
                        0.0,
                        1.0,
                        0.0,
                        0.0,
                        None,
                        1.0,
                        0.0,
                        1.0,
                        1.0,
                        None,
                        0.0,
                        -1.0,
                        0.0,
                        0.0,
                        None,
                        -1.0,
                        0.0,
                        -1.0,
                        -1.0,
                        None,
                        1.0,
                        0.0,
                        0.0,
                        1.0,
                        None,
                        0.0,
                        1.0,
                        1.0,
                        0.0,
                        None,
                    ],
                    "y": [
                        0.0,
                        -1.0,
                        0.0,
                        0.0,
                        None,
                        -1.0,
                        0.0,
                        -1.0,
                        -1.0,
                        None,
                        -1.0,
                        0.0,
                        0.0,
                        -1.0,
                        None,
                        0.0,
                        -1.0,
                        -1.0,
                        0.0,
                        None,
                        1.0,
                        0.0,
                        0.0,
                        1.0,
                        None,
                        0.0,
                        1.0,
                        1.0,
                        0.0,
                        None,
                        0.0,
                        1.0,
                        0.0,
                        0.0,
                        None,
                        1.0,
                        0.0,
                        1.0,
                        1.0,
                        None,
                    ],
                    "z": [
                        -0.0,
                        -0.0,
                        0.0,
                        -0.0,
                        None,
                        -0.0,
                        -0.0,
                        1.0,
                        -0.0,
                        None,
                        -0.0,
                        0.0,
                        0.0,
                        -0.0,
                        None,
                        0.0,
                        -0.0,
                        -1.0,
                        0.0,
                        None,
                        0.0,
                        -0.0,
                        0.0,
                        0.0,
                        None,
                        -0.0,
                        0.0,
                        -1.0,
                        -0.0,
                        None,
                        0.0,
                        0.0,
                        0.0,
                        0.0,
                        None,
                        0.0,
                        0.0,
                        1.0,
                        0.0,
                        None,
                    ],
                },
                {
                    "hoverinfo": "none",
                    "marker": {
                        "color": [-0.33333333333333331, 0.33333333333333331],
                        "colorscale": [
                            [0.0, "rgb(31, 119, 180)"],
                            [1.0, "rgb(255, 127, 14)"],
                        ],
                        "showscale": True,
                        "size": 0.1,
                    },
                    "mode": "markers",
                    "showlegend": False,
                    "type": "scatter3d",
                    "x": [-1.0],
                    "y": [-1.0],
                    "z": [1.0],
                },
            ],
            "layout": {
                "height": 800,
                "scene": {
                    "aspectratio": {"x": 1, "y": 1, "z": 1},
                    "xaxis": {
                        "backgroundcolor": "rgb(230, 230, 230)",
                        "gridcolor": "rgb(255, 255, 255)",
                        "showbackground": True,
                        "zerolinecolor": "rgb(255, 255, 255)",
                    },
                    "yaxis": {
                        "backgroundcolor": "rgb(230, 230, 230)",
                        "gridcolor": "rgb(255, 255, 255)",
                        "showbackground": True,
                        "zerolinecolor": "rgb(255, 255, 255)",
                    },
                    "zaxis": {
                        "backgroundcolor": "rgb(230, 230, 230)",
                        "gridcolor": "rgb(255, 255, 255)",
                        "showbackground": True,
                        "zerolinecolor": "rgb(255, 255, 255)",
                    },
                },
                "title": {"text": "Trisurf Plot"},
                "width": 800,
            },
        }

        self.assert_fig_equal(test_trisurf_plot["data"][0], exp_trisurf_plot["data"][0])

        self.assert_fig_equal(test_trisurf_plot["data"][1], exp_trisurf_plot["data"][1])

        self.assert_fig_equal(test_trisurf_plot["data"][2], exp_trisurf_plot["data"][2])

        self.assert_fig_equal(test_trisurf_plot["layout"], exp_trisurf_plot["layout"])

        # Test passing custom colors
        colors_raw = np.random.randn(simplices.shape[0])
        colors_str = [
            "rgb(%s, %s, %s)" % (i, j, k)
            for i, j, k in np.random.randn(simplices.shape[0], 3)
        ]

        # Color == strings should be kept the same
        test_colors_plot = ff.create_trisurf(x, y, z, simplices, color_func=colors_str)
        self.assertListEqual(
            list(test_colors_plot["data"][0]["facecolor"]), list(colors_str)
        )
        # Colors must match length of simplices
        colors_bad = colors_str[:-1]
        self.assertRaises(
            ValueError, ff.create_trisurf, x, y, z, simplices, color_func=colors_bad
        )
        # Check converting custom colors to strings
        test_colors_plot = ff.create_trisurf(x, y, z, simplices, color_func=colors_raw)
        self.assertTrue(isinstance(test_colors_plot["data"][0]["facecolor"][0], str))


class TestQuiver(TestCaseNoTemplate):
    def test_scaleratio_param(self):
        x, y = np.meshgrid(np.arange(0.5, 3.5, 0.5), np.arange(0.5, 4.5, 0.5))
        u = x
        v = y
        angle = np.arctan(v / u)
        norm = 0.25
        u = norm * np.cos(angle)
        v = norm * np.sin(angle)
        fig = ff.create_quiver(x, y, u, v, scale=1, scaleratio=0.5)

        exp_fig_head = [
            (
                0.5,
                0.5883883476483185,
                None,
                1.0,
                1.1118033988749896,
                None,
                1.5,
                1.6185854122563141,
                None,
                2.0,
            ),
            (
                0.5,
                0.6767766952966369,
                None,
                0.5,
                0.6118033988749895,
                None,
                0.5,
                0.5790569415042095,
                None,
                0.5,
            ),
        ]

        fig_head = [fig["data"][0]["x"][:10], fig["data"][0]["y"][:10]]

        self.assertEqual(fig_head, exp_fig_head)


class TestTernarycontour(NumpyTestUtilsMixin, TestCaseNoTemplate):
    def test_wrong_coordinates(self):
        a, b = np.mgrid[0:1:20j, 0:1:20j]
        a = a.ravel()
        b = b.ravel()
        z = a * b
        with self.assertRaises(
            ValueError, msg="Barycentric coordinates should be positive."
        ):
            _ = ff.create_ternary_contour(np.stack((a, b)), z)
        mask = a + b <= 1.0
        a = a[mask]
        b = b[mask]
        with self.assertRaises(ValueError):
            _ = ff.create_ternary_contour(np.stack((a, b, a, b)), z)
        with self.assertRaises(ValueError, msg="different number of values and points"):
            _ = ff.create_ternary_contour(
                np.stack((a, b, 1 - a - b)), np.concatenate((z, [1]))
            )
        # Different sums for different points
        c = a
        with self.assertRaises(ValueError):
            _ = ff.create_ternary_contour(np.stack((a, b, c)), z)
        # Sum of coordinates is different from one but is equal
        # for all points.
        with self.assertRaises(ValueError):
            _ = ff.create_ternary_contour(np.stack((a, b, 2 - a - b)), z)

    def test_simple_ternary_contour(self):
        a, b = np.mgrid[0:1:20j, 0:1:20j]
        mask = a + b < 1.0
        a = a[mask].ravel()
        b = b[mask].ravel()
        c = 1 - a - b
        z = a * b * c
        fig = ff.create_ternary_contour(np.stack((a, b, c)), z)
        fig2 = ff.create_ternary_contour(np.stack((a, b)), z)
        np.testing.assert_array_almost_equal(
            fig2["data"][0]["a"], fig["data"][0]["a"], decimal=3
        )

    def test_colorscale(self):
        a, b = np.mgrid[0:1:20j, 0:1:20j]
        mask = a + b < 1.0
        a = a[mask].ravel()
        b = b[mask].ravel()
        c = 1 - a - b
        z = a * b * c
        z /= z.max()
        fig = ff.create_ternary_contour(np.stack((a, b, c)), z, showscale=True)
        fig2 = ff.create_ternary_contour(
            np.stack((a, b, c)), z, showscale=True, showmarkers=True
        )
        assert isinstance(fig.data[-1]["marker"]["colorscale"], tuple)
        assert isinstance(fig2.data[-1]["marker"]["colorscale"], tuple)
        assert fig.data[-1]["marker"]["cmax"] == 1
        assert fig2.data[-1]["marker"]["cmax"] == 1

    def check_pole_labels(self):
        a, b = np.mgrid[0:1:20j, 0:1:20j]
        mask = a + b < 1.0
        a = a[mask].ravel()
        b = b[mask].ravel()
        c = 1 - a - b
        z = a * b * c
        pole_labels = ["A", "B", "C"]
        fig = ff.create_ternary_contour(np.stack((a, b, c)), z, pole_labels=pole_labels)
        assert fig.layout.ternary.aaxis.title.text == pole_labels[0]
        assert fig.data[-1].hovertemplate[0] == pole_labels[0]

    def test_optional_arguments(self):
        a, b = np.mgrid[0:1:20j, 0:1:20j]
        mask = a + b <= 1.0
        a = a[mask].ravel()
        b = b[mask].ravel()
        c = 1 - a - b
        z = a * b * c
        ncontours = 7
        args = [
            dict(showmarkers=False, showscale=False),
            dict(showmarkers=True, showscale=False),
            dict(showmarkers=False, showscale=True),
            dict(showmarkers=True, showscale=True),
        ]

        for arg_set in args:
            fig = ff.create_ternary_contour(
                np.stack((a, b, c)),
                z,
                interp_mode="cartesian",
                ncontours=ncontours,
                **arg_set,
            )
            # This test does not work for ilr interpolation
            print(len(fig.data))
            assert len(fig.data) == ncontours + 2 + arg_set["showscale"]


class TestHexbinMap(NumpyTestUtilsMixin, TestCaseNoTemplate):
    def compare_list_values(self, list1, list2, decimal=7):
        assert len(list1) == len(list2), "Lists are not of the same length."
        for i in range(len(list1)):
            if isinstance(list1[i], list):
                self.compare_list_values(list1[i], list2[i], decimal=decimal)
            elif isinstance(list1[i], dict):
                self.compare_dict_values(list1[i], list2[i], decimal=decimal)
            elif isinstance(list1[i], float):
                np.testing.assert_almost_equal(list1[i], list2[i], decimal=decimal)
            else:
                assert list1[i] == list2[i], (
                    f"Values at index {i} are not equal: {list1[i]} != {list2[i]}"
                )

    def compare_dict_values(self, dict1, dict2, decimal=7):
        for k, v in dict1.items():
            if isinstance(v, dict):
                self.compare_dict_values(v, dict2[k], decimal=decimal)
            elif isinstance(v, list):
                self.compare_list_values(v, dict2[k], decimal=decimal)
            elif isinstance(v, float):
                np.testing.assert_almost_equal(v, dict2[k], decimal=decimal)
            else:
                assert v == dict2[k], (
                    f"Values for key {k} are not equal: {v} != {dict2[k]}"
                )

    def test_aggregation(self):
        lat = [0, 1, 1, 2, 4, 5, 1, 2, 4, 5, 2, 3, 2, 1, 5, 3, 5]
        lon = [1, 2, 3, 3, 0, 4, 5, 0, 5, 3, 1, 5, 4, 0, 1, 2, 5]
        color = np.ones(len(lat))

        fig1 = ff.create_hexbin_map(lat=lat, lon=lon, nx_hexagon=1)

        actual_geojson = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "id": "-8.726646259971648e-11,-0.031886255679892235",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [-5e-09, -4.7083909316316985],
                                [2.4999999999999996, -3.268549270944215],
                                [2.4999999999999996, -0.38356933397072673],
                                [-5e-09, 1.0597430482129082],
                                [-2.50000001, -0.38356933397072673],
                                [-2.50000001, -3.268549270944215],
                                [-5e-09, -4.7083909316316985],
                            ]
                        ],
                    },
                },
                {
                    "type": "Feature",
                    "id": "-8.726646259971648e-11,0.1192636916419258",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [-5e-09, 3.9434377827164666],
                                [2.4999999999999996, 5.381998306154031],
                                [2.4999999999999996, 8.248045720432454],
                                [-5e-09, 9.673766164509932],
                                [-2.50000001, 8.248045720432454],
                                [-2.50000001, 5.381998306154031],
                                [-5e-09, 3.9434377827164666],
                            ]
                        ],
                    },
                },
                {
                    "type": "Feature",
                    "id": "0.08726646268698293,-0.031886255679892235",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [5.0000000049999995, -4.7083909316316985],
                                [7.500000009999999, -3.268549270944215],
                                [7.500000009999999, -0.38356933397072673],
                                [5.0000000049999995, 1.0597430482129082],
                                [2.5, -0.38356933397072673],
                                [2.5, -3.268549270944215],
                                [5.0000000049999995, -4.7083909316316985],
                            ]
                        ],
                    },
                },
                {
                    "type": "Feature",
                    "id": "0.08726646268698293,0.1192636916419258",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [5.0000000049999995, 3.9434377827164666],
                                [7.500000009999999, 5.381998306154031],
                                [7.500000009999999, 8.248045720432454],
                                [5.0000000049999995, 9.673766164509932],
                                [2.5, 8.248045720432454],
                                [2.5, 5.381998306154031],
                                [5.0000000049999995, 3.9434377827164666],
                            ]
                        ],
                    },
                },
                {
                    "type": "Feature",
                    "id": "0.04363323129985823,0.04368871798101678",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [2.4999999999999996, -0.38356933397072673],
                                [5.0000000049999995, 1.0597430482129082],
                                [5.0000000049999995, 3.9434377827164666],
                                [2.4999999999999996, 5.381998306154031],
                                [-5.0000001310894304e-09, 3.9434377827164666],
                                [-5.0000001310894304e-09, 1.0597430482129082],
                                [2.4999999999999996, -0.38356933397072673],
                            ]
                        ],
                    },
                },
            ],
        }

        actual_agg = [2.0, 2.0, 1.0, 3.0, 9.0]

        self.compare_dict_values(fig1.data[0].geojson, actual_geojson)
        assert np.array_equal(fig1.data[0].z, actual_agg)

        fig2 = ff.create_hexbin_map(
            lat=lat,
            lon=lon,
            nx_hexagon=1,
            color=color,
            agg_func=np.mean,
        )

        assert np.array_equal(fig2.data[0].z, np.ones(5))

        fig3 = ff.create_hexbin_map(
            lat=np.random.randn(1000),
            lon=np.random.randn(1000),
            nx_hexagon=20,
        )

        assert fig3.data[0].z.sum() == 1000

    def test_build_dataframe(self):
        np.random.seed(0)
        N = 10000
        nx_hexagon = 20
        n_frames = 3

        lat = np.random.randn(N)
        lon = np.random.randn(N)
        color = np.ones(N)
        frame = np.random.randint(0, n_frames, N)
        df = pd.DataFrame(  # TODO: Test other constructors?
            np.c_[lat, lon, color, frame],
            columns=["Latitude", "Longitude", "Metric", "Frame"],
        )

        fig1 = ff.create_hexbin_map(lat=lat, lon=lon, nx_hexagon=nx_hexagon)
        fig2 = ff.create_hexbin_map(
            data_frame=df, lat="Latitude", lon="Longitude", nx_hexagon=nx_hexagon
        )

        assert isinstance(fig1, go.Figure)
        assert len(fig1.data) == 1
        self.assert_dict_equal(
            fig1.to_plotly_json()["data"][0], fig2.to_plotly_json()["data"][0]
        )

        fig3 = ff.create_hexbin_map(
            lat=lat,
            lon=lon,
            nx_hexagon=nx_hexagon,
            color=color,
            agg_func=np.sum,
            min_count=0,
        )
        fig4 = ff.create_hexbin_map(
            lat=lat,
            lon=lon,
            nx_hexagon=nx_hexagon,
            color=color,
            agg_func=np.sum,
        )
        fig5 = ff.create_hexbin_map(
            data_frame=df,
            lat="Latitude",
            lon="Longitude",
            nx_hexagon=nx_hexagon,
            color="Metric",
            agg_func=np.sum,
        )

        self.assert_dict_equal(
            fig1.to_plotly_json()["data"][0], fig3.to_plotly_json()["data"][0]
        )
        self.assert_dict_equal(
            fig4.to_plotly_json()["data"][0], fig5.to_plotly_json()["data"][0]
        )

        fig6 = ff.create_hexbin_map(
            data_frame=df,
            lat="Latitude",
            lon="Longitude",
            nx_hexagon=nx_hexagon,
            color="Metric",
            agg_func=np.sum,
            animation_frame="Frame",
        )

        fig7 = ff.create_hexbin_map(
            lat=lat,
            lon=lon,
            nx_hexagon=nx_hexagon,
            color=color,
            agg_func=np.sum,
            animation_frame=frame,
        )

        assert len(fig6.frames) == n_frames
        assert len(fig7.frames) == n_frames
        assert fig6.data[0].geojson == fig1.data[0].geojson
