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


class TestAddTracesRowsColsDataTypes(TestCase):
    def test_add_traces_with_iterable(self):
        import plotly.express as px

        df = px.data.tips()
        fig = px.scatter(df, x="total_bill", y="tip", color="day")
        from plotly.subplots import make_subplots

        fig2 = make_subplots(1, 2)
        fig2.add_traces(fig.data, rows=[1,] * len(fig.data), cols=[1,] * len(fig.data))

        expected_data_length = 4

        self.assertEqual(expected_data_length, len(fig2.data))

    def test_add_traces_with_integers(self):
        import plotly.express as px

        df = px.data.tips()
        fig = px.scatter(df, x="total_bill", y="tip", color="day")
        from plotly.subplots import make_subplots

        fig2 = make_subplots(1, 2)
        fig2.add_traces(fig.data, rows=1, cols=2)

        expected_data_length = 4

        self.assertEqual(expected_data_length, len(fig2.data))
