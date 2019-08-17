import numpy as np

from unittest import TestCase

import plotly.tools as tls


class TestMakeSubplots(TestCase):
    def test_subplot_titles_numpy_array(self):
        # Pass numpy array
        expected = tls.make_subplots(
            insets=[{"cell": (1, 1), "l": 0.7, "b": 0.3}], subplot_titles=("", "Inset")
        )
        fig = tls.make_subplots(
            insets=[{"cell": (1, 1), "l": 0.7, "b": 0.3}],
            subplot_titles=np.array(["", "Inset"]),
        )
        self.assertEqual(fig, expected)
