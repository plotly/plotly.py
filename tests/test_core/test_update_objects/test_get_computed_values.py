from unittest.mock import MagicMock
import importlib.metadata

# Mock importlib.metadata.version BEFORE importing plotly to avoid PackageNotFoundError
if not hasattr(importlib.metadata.version, "assert_called"):
    importlib.metadata.version = MagicMock(return_value="6.7.0")

from unittest import TestCase
import plotly.graph_objects as go


class TestGetComputedValues(TestCase):
    def test_get_computed_axis_ranges_basic(self):
        # Create a simple figure
        fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[10, 20, 30]))

        # Mock full_figure_for_development to return a dict with computed ranges
        mock_full_fig = {
            "layout": {
                "xaxis": {"range": [0.8, 3.2], "type": "linear"},
                "yaxis": {"range": [8.0, 32.0], "type": "linear"},
                "template": {},
            }
        }
        fig.full_figure_for_development = MagicMock(return_value=mock_full_fig)

        # Call get_computed_values
        computed = fig.get_computed_values(include=["axis_ranges"])

        # Verify results
        expected = {"axis_ranges": {"xaxis": [0.8, 3.2], "yaxis": [8.0, 32.0]}}
        self.assertEqual(computed, expected)
        fig.full_figure_for_development.assert_called_once_with(
            warn=False, as_dict=True
        )

    def test_get_computed_axis_ranges_multi_axis(self):
        # Create a figure with multiple axes
        fig = go.Figure()

        # Mock full_figure_for_development (returning tuples to test conversion)
        mock_full_fig = {
            "layout": {
                "xaxis": {"range": (0, 1)},
                "yaxis": {"range": (0, 10)},
                "xaxis2": {"range": (0, 100)},
                "yaxis2": {"range": (50, 60)},
            }
        }
        fig.full_figure_for_development = MagicMock(return_value=mock_full_fig)

        computed = fig.get_computed_values(include=["axis_ranges"])

        # Ranges should be converted to lists
        expected = {
            "axis_ranges": {
                "xaxis": [0, 1],
                "yaxis": [0, 10],
                "xaxis2": [0, 100],
                "yaxis2": [50, 60],
            }
        }
        self.assertEqual(computed, expected)
        # Verify result values are indeed lists
        for val in computed["axis_ranges"].values():
            self.assertIsInstance(val, list)

    def test_empty_include(self):
        fig = go.Figure()
        fig.full_figure_for_development = MagicMock()

        # Should return empty dict early without calling full_figure
        computed = fig.get_computed_values(include=[])

        self.assertEqual(computed, {})
        fig.full_figure_for_development.assert_not_called()

    def test_invalid_include_parameter(self):
        fig = go.Figure()

        # Test non-list/tuple input
        with self.assertRaisesRegex(ValueError, "must be a list or tuple of strings"):
            fig.get_computed_values(include="axis_ranges")

        # Test unsupported key and deterministic error message
        with self.assertRaisesRegex(
            ValueError,
            r"Unsupported key 'invalid'.*Supported keys are: \['axis_ranges', 'axis_types'\]",
        ):
            fig.get_computed_values(include=["invalid"])

    def test_safe_extraction_handling(self):
        # Test that non-dict or missing 'range' values are skipped
        fig = go.Figure()
        mock_full_fig = {
            "layout": {
                "xaxis": "not-a-dict",
                "yaxis": {"no-range": True},
                "xaxis2": {"range": [1, 2]},
            }
        }
        fig.full_figure_for_development = MagicMock(return_value=mock_full_fig)

        computed = fig.get_computed_values(include=["axis_ranges"])

        expected = {"axis_ranges": {"xaxis2": [1, 2]}}
        self.assertEqual(computed, expected)

    def test_get_computed_axis_types(self):
        # Verify standalone extraction of axis types
        fig = go.Figure()
        mock_full_fig = {
            "layout": {
                "xaxis": {"range": [0, 10], "type": "linear"},
                "yaxis": {"range": [0, 100], "type": "log"},
                "xaxis2": {"type": "date"},
            }
        }
        fig.full_figure_for_development = MagicMock(return_value=mock_full_fig)

        computed = fig.get_computed_values(include=["axis_types"])

        expected = {"axis_types": {"xaxis": "linear", "yaxis": "log", "xaxis2": "date"}}
        self.assertEqual(computed, expected)
        # axis_ranges should not be present when not requested
        self.assertNotIn("axis_ranges", computed)

    def test_get_computed_values_combined(self):
        # Verify that requesting multiple keys returns all of them correctly
        fig = go.Figure()
        mock_full_fig = {
            "layout": {
                "xaxis": {"range": [0, 1], "type": "linear"},
                "yaxis": {"range": [0, 10], "type": "log"},
                # axis with no range — should appear in axis_types but not axis_ranges
                "xaxis2": {"type": "date"},
            }
        }
        fig.full_figure_for_development = MagicMock(return_value=mock_full_fig)

        computed = fig.get_computed_values(include=["axis_ranges", "axis_types"])

        self.assertEqual(
            computed["axis_ranges"],
            {"xaxis": [0, 1], "yaxis": [0, 10]},
        )
        self.assertEqual(
            computed["axis_types"],
            {"xaxis": "linear", "yaxis": "log", "xaxis2": "date"},
        )
        # Verify single call to the rendering engine despite two keys
        fig.full_figure_for_development.assert_called_once()
