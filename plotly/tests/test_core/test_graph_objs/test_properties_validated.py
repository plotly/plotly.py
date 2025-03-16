from unittest import TestCase
import plotly.graph_objs as go
import pytest


class TestPropertyValidation(TestCase):
    def setUp(self):
        # Construct initial scatter object
        self.scatter = go.Scatter()
        self.scatter.name = "Scatter 1"

    def test_validators_work_attr(self):
        """
        Note: all of the individual validators are tested in
        `_plotly_utils/tests/validators`. Here we're just making sure that
        datatypes make use of validators
        """
        with pytest.raises(ValueError):
            self.scatter.name = [1, 2, 3]

    def test_validators_work_item(self):
        """
        Note: all of the individual validators are tested in
        `_plotly_utils/tests/validators`. Here we're just making sure that
        datatypes make use of validators
        """
        with pytest.raises(ValueError):
            self.scatter["name"] = [1, 2, 3]

    def test_invalid_attr_assignment(self):
        with pytest.raises(ValueError):
            self.scatter.bogus = 87

    def test_invalid_item_assignment(self):
        with pytest.raises(ValueError):
            self.scatter["bogus"] = 87

    def test_invalid_dot_assignment(self):
        with pytest.raises(ValueError):
            self.scatter["marker.bogus"] = 87

    def test_invalid_tuple_assignment(self):
        with pytest.raises(ValueError):
            self.scatter[("marker", "bogus")] = 87

    def test_invalid_constructor_kwarg(self):
        with pytest.raises(ValueError):
            go.Scatter(bogus=87)


class TestPropertyPresentation(TestCase):
    def setUp(self):
        # Construct initial scatter object
        self.scatter = go.Scatter()
        self.scatter.name = "Scatter 1"

        self.layout = go.Layout()

    def test_present_dataarray(self):
        self.assertIsNone(self.scatter.x)

        # Assign list
        self.scatter.x = [1, 2, 3, 4]

        # Stored as list
        self.assertEqual(self.scatter.to_plotly_json()["x"], [1, 2, 3, 4])

        # Returned as tuple
        self.assertEqual(self.scatter.x, (1, 2, 3, 4))

    def test_present_compound_array(self):
        self.assertEqual(self.layout.images, ())

        # Assign compound list
        self.layout.images = [
            go.layout.Image(layer="above"),
            go.layout.Image(layer="below"),
        ]

        # Stored as list of dicts
        self.assertEqual(
            self.layout.to_plotly_json()["images"],
            [{"layer": "above"}, {"layer": "below"}],
        )

        # Presented as compound tuple
        self.assertEqual(
            self.layout.images,
            (go.layout.Image(layer="above"), go.layout.Image(layer="below")),
        )

    def test_present_colorscale(self):
        self.assertIsNone(self.scatter.marker.colorscale)

        # Assign list of tuples
        self.scatter.marker.colorscale = [(0, "red"), (1, "green")]

        # Stored as list of lists
        self.assertEqual(
            self.scatter.to_plotly_json()["marker"]["colorscale"],
            [[0, "red"], [1, "green"]],
        )

        # Presented as tuple of tuples
        self.assertEqual(self.scatter.marker.colorscale, ((0, "red"), (1, "green")))

        # Test colorscale and reversed version
        self.scatter.marker.colorscale = "viridis"
        colorscale = self.scatter.to_plotly_json()["marker"]["colorscale"]
        colorscale = [col[1] for col in colorscale]
        self.scatter.marker.colorscale = "viridis_r"
        colorscale_r = self.scatter.to_plotly_json()["marker"]["colorscale"]
        colorscale_r = [col[1] for col in colorscale_r]
        self.assertEqual(colorscale[::-1], colorscale_r)


class TestPropertyIterContains(TestCase):
    def setUp(self):
        # Construct initial scatter object
        self.parcoords = go.Parcoords()
        self.parcoords.name = "Scatter 1"

    def test_contains(self):

        # Primitive property
        self.assertTrue("name" in self.parcoords)

        # Compound property
        self.assertTrue("line" in self.parcoords)

        # Literal
        self.assertTrue("type" in self.parcoords)

        # Compound array property
        self.assertTrue("dimensions" in self.parcoords)

        # Bogus
        self.assertFalse("bogus" in self.parcoords)

    def test_iter(self):
        parcoords_list = list(self.parcoords)

        # Primitive property
        self.assertTrue("name" in parcoords_list)

        # Compound property
        self.assertTrue("line" in parcoords_list)

        # Literal
        self.assertTrue("type" in parcoords_list)

        # Compound array property
        self.assertTrue("dimensions" in parcoords_list)

        # Bogus
        self.assertFalse("bogus" in parcoords_list)
