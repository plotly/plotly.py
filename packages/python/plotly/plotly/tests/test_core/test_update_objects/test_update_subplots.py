from __future__ import absolute_import

import copy
from unittest import TestCase

import plotly.graph_objs as go
from plotly.graph_objs import Figure
from plotly.subplots import make_subplots


class TestSelectForEachUpdateSubplots(TestCase):
    def setUp(self):
        fig = make_subplots(
            rows=3,
            cols=3,
            specs=[
                [{}, {"type": "scene"}, {}],
                [{"secondary_y": True}, {"type": "polar"}, {"type": "polar"}],
                [{"type": "xy", "colspan": 2}, None, {"type": "ternary"}],
            ],
        ).update(layout={"height": 800})

        fig.layout.xaxis.title.text = "A"
        fig.layout.xaxis2.title.text = "A"
        fig.layout.xaxis3.title.text = "B"
        fig.layout.xaxis4.title.text = "B"

        fig.layout.yaxis.title.text = "A"
        fig.layout.yaxis2.title.text = "B"
        fig.layout.yaxis3.title.text = "A"
        fig.layout.yaxis4.title.text = "B"

        fig.layout.polar.angularaxis.rotation = 45
        fig.layout.polar2.angularaxis.rotation = 45
        fig.layout.polar.radialaxis.title.text = "A"
        fig.layout.polar2.radialaxis.title.text = "B"

        fig.layout.scene.xaxis.title.text = "A"
        fig.layout.scene.yaxis.title.text = "B"

        fig.layout.ternary.aaxis.title.text = "A"

        self.fig = fig
        self.fig_no_grid = go.Figure(self.fig.to_dict())

    def assert_select_subplots(
        self,
        subplot_type,
        subplots_name,
        expected_nums,
        selector=None,
        row=None,
        col=None,
        secondary_y=None,
        test_no_grid=False,
    ):

        select_fn = getattr(Figure, "select_" + subplots_name)
        for_each_fn = getattr(Figure, "for_each_" + subplot_type)

        if secondary_y is not None:
            sec_y_args = dict(secondary_y=secondary_y)
        else:
            sec_y_args = {}

        def check_select(fig):
            # Check select_*
            subplots = list(
                select_fn(fig, selector=selector, row=row, col=col, **sec_y_args)
            )
            expected_keys = [
                subplot_type + (str(cnt) if cnt > 1 else "") for cnt in expected_nums
            ]

            self.assertEqual(len(subplots), len(expected_keys))
            self.assertTrue(
                all(v1 is fig.layout[k] for v1, k in zip(subplots, expected_keys))
            )

            # Check for_each_*
            subplots = []
            res = for_each_fn(
                fig,
                lambda obj: subplots.append(obj),
                selector=selector,
                row=row,
                col=col,
                **sec_y_args
            )

            self.assertIs(res, fig)

            self.assertEqual(len(subplots), len(expected_keys))
            self.assertTrue(
                all(v1 is fig.layout[k] for v1, k in zip(subplots, expected_keys))
            )

        check_select(self.fig)
        if test_no_grid:
            check_select(self.fig_no_grid)

    def test_select_by_type(self):
        self.assert_select_subplots("xaxis", "xaxes", [1, 2, 3, 4], test_no_grid=True)

        self.assert_select_subplots(
            "yaxis", "yaxes", [1, 2, 3, 4, 5], test_no_grid=True
        )

        self.assert_select_subplots("scene", "scenes", [1], test_no_grid=True)

        self.assert_select_subplots("polar", "polars", [1, 2], test_no_grid=True)

        self.assert_select_subplots("ternary", "ternaries", [1], test_no_grid=True)

        # No 'geo' or 'mapbox' subplots initialized, but the first subplot
        # object is always present
        self.assert_select_subplots("geo", "geos", [1], test_no_grid=True)

        self.assert_select_subplots("mapbox", "mapboxes", [1], test_no_grid=True)

    def test_select_by_type_and_grid(self):
        self.assert_select_subplots("xaxis", "xaxes", [1, 2], row=1)

        self.assert_select_subplots("xaxis", "xaxes", [1, 3, 4], col=1)

        self.assert_select_subplots("xaxis", "xaxes", [2], col=3)

        self.assert_select_subplots("xaxis", "xaxes", [4], row=3, col=1)

        self.assert_select_subplots("xaxis", "xaxes", [], row=2, col=2)

    def test_select_by_secondary_y(self):
        self.assert_select_subplots("yaxis", "yaxes", [4], secondary_y=True)

        self.assert_select_subplots("yaxis", "yaxes", [1, 2, 3, 5], secondary_y=False)

        self.assert_select_subplots("yaxis", "yaxes", [4], col=1, secondary_y=True)

        self.assert_select_subplots("yaxis", "yaxes", [], col=3, secondary_y=True)

    def test_select_by_type_and_selector(self):
        # xaxis
        self.assert_select_subplots(
            "xaxis", "xaxes", [1, 2], selector={"title.text": "A"}, test_no_grid=True
        )

        self.assert_select_subplots(
            "xaxis", "xaxes", [3, 4], selector={"title.text": "B"}, test_no_grid=True
        )

        self.assert_select_subplots(
            "xaxis", "xaxes", [], selector={"title.text": "C"}, test_no_grid=True
        )

        self.assert_select_subplots(
            "xaxis", "xaxes", [4], selector=-1, test_no_grid=True
        )

        # yaxis
        self.assert_select_subplots(
            "yaxis", "yaxes", [1, 3], selector={"title.text": "A"}, test_no_grid=True
        )

        self.assert_select_subplots(
            "yaxis", "yaxes", [2, 4], selector={"title.text": "B"}, test_no_grid=True
        )

        self.assert_select_subplots(
            "yaxis", "yaxes", [], selector={"title.text": "C"}, test_no_grid=True
        )

        self.assert_select_subplots(
            "yaxis", "yaxes", [5], selector=-1, test_no_grid=True
        )

        self.assert_select_subplots(
            "yaxis", "yaxes", [2], selector=1, test_no_grid=True
        )

        # scene
        self.assert_select_subplots(
            "scene",
            "scenes",
            [1],
            selector={"xaxis.title.text": "A"},
            test_no_grid=True,
        )

        self.assert_select_subplots(
            "scene",
            "scenes",
            [1],
            selector={"xaxis.title.text": "A", "yaxis.title.text": "B"},
            test_no_grid=True,
        )

        self.assert_select_subplots(
            "scene",
            "scenes",
            [],
            selector={"xaxis.title.text": "A", "yaxis.title.text": "C"},
            test_no_grid=True,
        )

        self.assert_select_subplots(
            "scene", "scenes", [1], selector=0, test_no_grid=True
        )

        # polar
        self.assert_select_subplots(
            "polar",
            "polars",
            [1, 2],
            selector={"angularaxis.rotation": 45},
            test_no_grid=True,
        )

        self.assert_select_subplots(
            "polar",
            "polars",
            [2],
            selector={"angularaxis.rotation": 45, "radialaxis_title_text": "B"},
            test_no_grid=True,
        )

        self.assert_select_subplots(
            "polar",
            "polars",
            [],
            selector={"angularaxis.rotation": 45, "radialaxis_title_text": "C"},
            test_no_grid=True,
        )

        self.assert_select_subplots(
            "polar", "polars", [2], selector=-1, test_no_grid=True
        )

        # ternary
        self.assert_select_subplots(
            "ternary",
            "ternaries",
            [1],
            selector={"aaxis.title.text": "A"},
            test_no_grid=True,
        )

        self.assert_select_subplots(
            "ternary",
            "ternaries",
            [],
            selector={"aaxis.title.text": "C"},
            test_no_grid=True,
        )

        self.assert_select_subplots(
            "ternary",
            "ternaries",
            [],
            selector={"aaxis.bogus.text": "A"},
            test_no_grid=True,
        )

        self.assert_select_subplots(
            "ternary", "ternaries", [1], selector=-1, test_no_grid=True
        )

        # No 'geo' or 'mapbox' subplots initialized, but the first subplot
        # object is always present
        self.assert_select_subplots(
            "geo", "geos", [], selector={"bgcolor": "blue"}, test_no_grid=True
        )

        self.assert_select_subplots(
            "geo", "geos", [], selector={"bogus": "blue"}, test_no_grid=True
        )

        self.assert_select_subplots(
            "mapbox", "mapboxes", [], selector={"pitch": 45}, test_no_grid=True
        )

    def test_select_by_type_and_grid_and_selector(self):
        # xaxis
        self.assert_select_subplots(
            "xaxis", "xaxes", [1, 2], row=1, selector={"title.text": "A"}
        )

        self.assert_select_subplots(
            "xaxis", "xaxes", [1], col=1, selector={"title.text": "A"}
        )

        self.assert_select_subplots(
            "xaxis", "xaxes", [], col=2, selector={"title.text": "A"}
        )

        self.assert_select_subplots(
            "xaxis", "xaxes", [3, 4], col=1, selector={"title.text": "B"}
        )

        self.assert_select_subplots("xaxis", "xaxes", [4], col=1, selector=-1)

        self.assert_select_subplots(
            "xaxis", "xaxes", [3], row=2, selector={"title.text": "B"}
        )

        self.assert_select_subplots(
            "xaxis", "xaxes", [4], row=3, col=1, selector={"title.text": "B"}
        )

        # yaxis
        self.assert_select_subplots(
            "yaxis", "yaxes", [1, 3], col=1, selector={"title.text": "A"}
        )

        self.assert_select_subplots("yaxis", "yaxes", [5], col=1, selector=-1)

        self.assert_select_subplots("yaxis", "yaxes", [1], col=1, selector=0)

        self.assert_select_subplots(
            "yaxis", "yaxes", [4], col=1, selector={"title.text": "B"}
        )

        # polar
        self.assert_select_subplots(
            "polar", "polars", [1, 2], row=2, selector={"angularaxis.rotation": 45}
        )

        self.assert_select_subplots("polar", "polars", [2], row=2, selector=-1)

        self.assert_select_subplots(
            "polar", "polars", [1], col=2, selector={"angularaxis.rotation": 45}
        )

        self.assert_select_subplots(
            "polar", "polars", [2], row=2, col=3, selector={"angularaxis.rotation": 45}
        )

        self.assert_select_subplots(
            "polar", "polars", [], row=2, col=3, selector={"angularaxis.rotation": 0}
        )

    def assert_update_subplots(
        self,
        subplot_type,
        subplots_name,
        expected_nums,
        patch=None,
        selector=None,
        row=None,
        col=None,
        secondary_y=None,
        test_no_grid=False,
        **kwargs
    ):

        update_fn = getattr(Figure, "update_" + subplots_name)

        if secondary_y is not None:
            secy_kwargs = dict(secondary_y=secondary_y)
        else:
            secy_kwargs = {}

        def check_update(fig):

            # Copy input figure so that we don't modify it
            fig_orig = fig
            fig = copy.deepcopy(fig)

            # perform update_*
            update_res = update_fn(
                fig,
                patch,
                selector=selector,
                row=row,
                col=col,
                **dict(kwargs, **secy_kwargs)
            )

            self.assertIs(update_res, fig)

            # Build expected layout keys
            expected_keys = [
                subplot_type + (str(cnt) if cnt > 1 else "") for cnt in expected_nums
            ]

            # Iterate over all layout keys
            for k in fig.layout:
                orig_obj = copy.deepcopy(fig_orig.layout[k])
                new_obj = fig.layout[k]
                if k in expected_keys:
                    # Make sure sure there is an initial difference
                    self.assertNotEqual(orig_obj, new_obj)
                    orig_obj.update(patch, **kwargs)

                self.assertEqual(new_obj, orig_obj)

        check_update(self.fig)
        if test_no_grid:
            check_update(self.fig_no_grid)

    def test_update_by_type(self):
        self.assert_update_subplots(
            "xaxis",
            "xaxes",
            [1, 2, 3, 4],
            {"title.font.family": "Rockwell"},
            test_no_grid=True,
        )

        self.assert_update_subplots(
            "yaxis", "yaxes", [1, 2, 3, 4, 5], {"range": [5, 10]}, test_no_grid=True
        )

        self.assert_update_subplots(
            "scene", "scenes", [1], {"zaxis.title.text": "Z-AXIS"}, test_no_grid=True
        )

        self.assert_update_subplots(
            "polar", "polars", [1, 2], {"angularaxis.rotation": 15}, test_no_grid=True
        )

        self.assert_update_subplots(
            "ternary",
            "ternaries",
            [1],
            {"aaxis.title.font.family": "Rockwell"},
            test_no_grid=True,
        )

        # No 'geo' or 'mapbox' subplots initialized, but the first subplot
        # object is always present
        self.assert_update_subplots(
            "geo", "geos", [1], {"bgcolor": "purple"}, test_no_grid=True
        )

        self.assert_update_subplots(
            "mapbox", "mapboxes", [1], {"pitch": 99}, test_no_grid=True
        )

    def test_update_by_type_and_grid(self):
        self.assert_update_subplots(
            "xaxis", "xaxes", [1, 3, 4], {"title.font.family": "Rockwell"}, col=1
        )

        self.assert_update_subplots(
            "xaxis", "xaxes", [1, 2], {"title.font.family": "Rockwell"}, row=1
        )

        self.assert_update_subplots(
            "xaxis", "xaxes", [1], {"title.font.family": "Rockwell"}, row=1, col=1
        )

        self.assert_update_subplots(
            "polar", "polars", [1, 2], {"angularaxis.rotation": 15}, row=2
        )

        self.assert_update_subplots(
            "polar", "polars", [1], {"angularaxis.rotation": 15}, col=2
        )

        self.assert_update_subplots(
            "polar", "polars", [2], {"angularaxis.rotation": 15}, row=2, col=3
        )

    def test_update_by_secondary_y(self):
        self.assert_update_subplots(
            "yaxis", "yaxes", [4], {"range": [5, 10]}, secondary_y=True
        )

        self.assert_update_subplots(
            "yaxis", "yaxes", [1, 2, 3, 5], {"range": [5, 10]}, secondary_y=False
        )

    def test_update_by_type_and_grid_and_selector(self):
        # xaxis
        self.assert_update_subplots(
            "xaxis",
            "xaxes",
            [1, 2],
            {"title.font.family": "Rockwell"},
            row=1,
            selector={"title.text": "A"},
        )

        self.assert_update_subplots(
            "xaxis",
            "xaxes",
            [1],
            {"title.font.family": "Rockwell"},
            col=1,
            selector={"title.text": "A"},
        )

        self.assert_update_subplots(
            "xaxis",
            "xaxes",
            [],
            {"title.font.family": "Rockwell"},
            col=2,
            selector={"title.text": "A"},
        )

        self.assert_update_subplots(
            "xaxis",
            "xaxes",
            [3, 4],
            {"title.font.family": "Rockwell"},
            col=1,
            selector={"title.text": "B"},
        )

        self.assert_update_subplots(
            "xaxis",
            "xaxes",
            [3],
            {"title.font.family": "Rockwell"},
            row=2,
            selector={"title.text": "B"},
        )

        self.assert_update_subplots(
            "xaxis",
            "xaxes",
            [4],
            {"title.font.family": "Rockwell"},
            row=3,
            col=1,
            selector={"title.text": "B"},
        )

        # yaxis
        self.assert_update_subplots(
            "yaxis",
            "yaxes",
            [1, 3],
            {"title.font.family": "Rockwell"},
            col=1,
            selector={"title.text": "A"},
        )

        self.assert_update_subplots(
            "yaxis",
            "yaxes",
            [4],
            {"title.font.family": "Rockwell"},
            col=1,
            selector={"title.text": "B"},
        )

        # polar
        self.assert_update_subplots(
            "polar",
            "polars",
            [1, 2],
            {"radialaxis.title.font.family": "Rockwell"},
            row=2,
            selector={"angularaxis.rotation": 45},
        )

        self.assert_update_subplots(
            "polar",
            "polars",
            [1],
            {"radialaxis.title.font.family": "Rockwell"},
            col=2,
            selector={"angularaxis.rotation": 45},
        )

        self.assert_update_subplots(
            "polar",
            "polars",
            [2],
            {"radialaxis.title.font.family": "Rockwell"},
            row=2,
            col=3,
            selector={"angularaxis.rotation": 45},
        )

        self.assert_update_subplots(
            "polar",
            "polars",
            [],
            {"radialaxis.title.font.family": "Rockwell"},
            row=2,
            col=3,
            selector={"angularaxis.rotation": 0},
        )

        # kwargs
        self.assert_update_subplots(
            "xaxis",
            "xaxes",
            [1, 2],
            title_font_family="Courier",
            title_font_color="yellow",
            row=1,
            selector={"title.text": "A"},
        )

    def test_update_subplot_overwrite(self):
        fig = go.Figure(layout_xaxis_title_text="Axis title")
        fig.update_xaxes(overwrite=True, title={"font": {"family": "Courier"}})

        self.assertEqual(
            fig.layout.xaxis.to_plotly_json(),
            {"title": {"font": {"family": "Courier"}}},
        )
