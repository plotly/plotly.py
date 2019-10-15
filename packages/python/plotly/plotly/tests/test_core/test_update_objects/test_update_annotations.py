from __future__ import absolute_import

import types
from unittest import TestCase

import plotly.graph_objs as go
from plotly.subplots import make_subplots


class TestSelectForEachUpdateAnnotations(TestCase):
    def setUp(self):
        self.fig = make_subplots(
            rows=2, cols=2, specs=[[{}, {"secondary_y": True}], [{}, {"type": "polar"}]]
        )

    def assert_selected(
        self, prop, inds, selector=None, row=None, col=None, secondary_y=None
    ):
        # ## Test select_*
        # Get select_ method
        prefix = "layout_" if prop == "images" else ""
        fn = getattr(self.fig, "select_" + prefix + prop)

        # Perform selection
        res = fn(selector=selector, row=row, col=col, secondary_y=secondary_y)
        self.assertIsInstance(res, types.GeneratorType)
        objs = list(res)

        # Check length of selected objects
        self.assertEqual(len(objs), len(inds))

        # Check individual annotations
        for i, obj in zip(inds, objs):
            self.assertEqual(self.fig.layout[prop][i], obj)

        # ## Test for_each_*
        objs = []
        fn = getattr(self.fig, "for_each_" + prefix + prop[:-1])
        fn(
            lambda v: objs.append(v),
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        )
        self.assertEqual(len(objs), len(inds))
        for i, obj in zip(inds, objs):
            self.assertEqual(self.fig.layout[prop][i], obj)

    def assert_update(
        self, prop, inds, patch, selector=None, row=None, col=None, secondary_y=None
    ):
        # Copy figure and perform update
        prefix = "layout_" if prop == "images" else ""
        fig_orig = go.Figure(self.fig)
        fig = go.Figure(self.fig)
        fn = getattr(fig, "update_" + prefix + prop)
        fn(patch, selector=selector, row=row, col=col, secondary_y=secondary_y)

        # Get original up updated object lis
        objs_orig = fig_orig.layout[prop]
        objs = fig.layout[prop]

        for i, (obj, obj_orig) in enumerate(zip(objs, objs_orig)):
            if i in inds:
                # Check that object changed from original
                self.assertNotEqual(obj, obj_orig)

                # Apply update to original and check that they match now
                obj_orig.update(patch)
                self.assertEqual(obj, obj_orig)
            else:
                # Check object unchanged
                self.assertEqual(obj, obj_orig)

    def test_add_annotation_no_grid(self):
        # Paper annotation
        fig = go.Figure()
        fig.add_annotation(text="A")
        annot = fig.layout.annotations[-1]
        self.assertEqual(annot.text, "A")
        self.assertEqual(annot.xref, "paper")
        self.assertEqual(annot.yref, "paper")

        # Not valid to add annotation by row/col
        with self.assertRaisesRegexp(Exception, "make_subplots"):
            fig.add_annotation(text="B", row=1, col=1)

    def test_add_annotations(self):
        # Paper annotation
        self.fig.add_annotation(text="A")
        annot = self.fig.layout.annotations[-1]
        self.assertEqual(annot.text, "A")
        self.assertEqual(annot.xref, "paper")
        self.assertEqual(annot.yref, "paper")

        # (1, 1) annotation
        self.fig.add_annotation(text="B", row=1, col=1)
        annot = self.fig.layout.annotations[-1]
        self.assertEqual(annot.text, "B")
        self.assertEqual(annot.xref, "x")
        self.assertEqual(annot.yref, "y")

        # (1, 2) annotation, primary y-axis
        self.fig.add_annotation(text="C1", row=1, col=2)
        annot = self.fig.layout.annotations[-1]
        self.assertEqual(annot.text, "C1")
        self.assertEqual(annot.xref, "x2")
        self.assertEqual(annot.yref, "y2")

        # (1, 2) annotation, secondary y-axis
        self.fig.add_annotation(text="C2", row=1, col=2, secondary_y=True)
        annot = self.fig.layout.annotations[-1]
        self.assertEqual(annot.text, "C2")
        self.assertEqual(annot.xref, "x2")
        self.assertEqual(annot.yref, "y3")

        # (2, 1) annotation
        self.fig.add_annotation(text="D", row=2, col=1)
        annot = self.fig.layout.annotations[-1]
        self.assertEqual(annot.text, "D")
        self.assertEqual(annot.xref, "x3")
        self.assertEqual(annot.yref, "y4")

        # Try to add to (2, 2), which not a valid
        with self.assertRaisesRegexp(ValueError, "of type polar"):
            self.fig.add_annotation(text="D", row=2, col=2)

    def test_select_annotations_no_grid(self):
        (
            self.fig.add_annotation(text="A1", arrowcolor="red")
            .add_annotation(text="A2", arrowcolor="blue")
            .add_annotation(text="A3", arrowcolor="blue")
        )
        self.assert_selected("annotations", [0, 1, 2])
        self.assert_selected("annotations", [0], selector=dict(arrowcolor="red"))
        self.assert_selected("annotations", [1, 2], selector=dict(arrowcolor="blue"))

    def test_select_annotations(self):
        (
            self.fig.add_annotation(text="A1", arrowcolor="red")
            .add_annotation(text="A2", arrowcolor="blue")
            .add_annotation(text="B", arrowcolor="red", row=1, col=1)
            .add_annotation(text="C1", row=1, col=2)
            .add_annotation(text="C2", row=1, col=2, secondary_y=True)
            .add_annotation(text="D", arrowcolor="blue", row=2, col=1)
        )

        # Test selections
        self.assert_selected("annotations", [0, 1, 2, 3, 4, 5])
        self.assert_selected("annotations", [0, 2], selector=dict(arrowcolor="red"))
        self.assert_selected("annotations", [2, 3, 4], row=1)
        self.assert_selected("annotations", [2], selector=dict(arrowcolor="red"), row=1)
        self.assert_selected("annotations", [0, 1], row="paper", col="paper")
        self.assert_selected("annotations", [4], secondary_y=True)

    def test_select_shapes(self):
        (
            self.fig.add_shape(opacity=0.1, fillcolor="red")
            .add_shape(opacity=0.2, fillcolor="blue")
            .add_shape(opacity=0.3, fillcolor="red", row=1, col=1)
            .add_shape(opacity=0.4, row=1, col=2)
            .add_shape(opacity=0.5, row=1, col=2, secondary_y=True)
            .add_shape(opacity=0.6, fillcolor="blue", row=2, col=1)
        )

        # Test selections
        self.assert_selected("shapes", [0, 1, 2, 3, 4, 5])
        self.assert_selected("shapes", [0, 2], selector=dict(fillcolor="red"))
        self.assert_selected("shapes", [2, 3, 4], row=1)
        self.assert_selected("shapes", [2], selector=dict(fillcolor="red"), row=1)
        self.assert_selected("shapes", [0, 1], row="paper", col="paper")
        self.assert_selected("shapes", [4], secondary_y=True)

    def test_select_images(self):
        (
            self.fig.add_layout_image(opacity=0.1, source="red")
            .add_layout_image(opacity=0.2, source="blue")
            .add_layout_image(opacity=0.3, source="red", row=1, col=1)
            .add_layout_image(opacity=0.4, row=1, col=2)
            .add_layout_image(opacity=0.5, row=1, col=2, secondary_y=True)
            .add_layout_image(opacity=0.6, source="blue", row=2, col=1)
        )

        # Test selections
        self.assert_selected("images", [0, 1, 2, 3, 4, 5])
        self.assert_selected("images", [0, 2], selector=dict(source="red"))
        self.assert_selected("images", [2, 3, 4], row=1)
        self.assert_selected("images", [2], selector=dict(source="red"), row=1)
        self.assert_selected("images", [0, 1], row="paper", col="paper")
        self.assert_selected("images", [4], secondary_y=True)

    def test_update_annotations(self):
        (
            self.fig.add_annotation(text="A1", arrowcolor="red")
            .add_annotation(text="A2", arrowcolor="blue")
            .add_annotation(text="B", arrowcolor="red", row=1, col=1)
            .add_annotation(text="C1", row=1, col=2)
            .add_annotation(text="C2", row=1, col=2, secondary_y=True)
            .add_annotation(text="D", arrowcolor="blue", row=2, col=1)
        )

        self.assert_update(
            "annotations", [0, 1, 2, 3, 4, 5], patch=dict(showarrow=False)
        )
        self.assert_update(
            "annotations",
            [1, 5],
            patch=dict(showarrow=False),
            selector=dict(arrowcolor="blue"),
        )
        self.assert_update("annotations", [2, 3, 4], patch=dict(showarrow=False), row=1)
        self.assert_update("annotations", [2, 5], patch=dict(showarrow=False), col=1)
        self.assert_update(
            "annotations", [4], patch=dict(showarrow=False), secondary_y=True
        )

    def test_update_shapes(self):
        (
            self.fig.add_shape(opacity=0.1, fillcolor="red")
            .add_shape(opacity=0.2, fillcolor="blue")
            .add_shape(opacity=0.3, fillcolor="red", row=1, col=1)
            .add_shape(opacity=0.4, row=1, col=2)
            .add_shape(opacity=0.5, row=1, col=2, secondary_y=True)
            .add_shape(opacity=0.6, fillcolor="blue", row=2, col=1)
        )

        self.assert_update("shapes", [0, 1, 2, 3, 4, 5], patch=dict(opacity=0))
        self.assert_update(
            "shapes", [1, 5], patch=dict(opacity=0), selector=dict(fillcolor="blue")
        )
        self.assert_update("shapes", [2, 3, 4], patch=dict(opacity=0), row=1)
        self.assert_update("shapes", [2, 5], patch=dict(opacity=0), col=1)
        self.assert_update("shapes", [4], patch=dict(opacity=0), secondary_y=True)

    def test_update_images(self):
        (
            self.fig.add_layout_image(opacity=0.1, source="red")
            .add_layout_image(opacity=0.2, source="blue")
            .add_layout_image(opacity=0.3, source="red", row=1, col=1)
            .add_layout_image(opacity=0.4, row=1, col=2)
            .add_layout_image(opacity=0.5, row=1, col=2, secondary_y=True)
            .add_layout_image(opacity=0.6, source="blue", row=2, col=1)
        )

        self.assert_update("images", [0, 1, 2, 3, 4, 5], patch=dict(opacity=0))
        self.assert_update(
            "images", [1, 5], patch=dict(opacity=0), selector=dict(source="blue")
        )
        self.assert_update("images", [2, 3, 4], patch=dict(opacity=0), row=1)
        self.assert_update("images", [2, 5], patch=dict(opacity=0), col=1)
        self.assert_update("images", [4], patch=dict(opacity=0), secondary_y=True)
