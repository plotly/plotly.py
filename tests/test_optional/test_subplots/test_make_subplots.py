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
        fig2.add_traces(
            fig.data,
            rows=[
                1,
            ]
            * len(fig.data),
            cols=[
                1,
            ]
            * len(fig.data),
        )

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

class TestSharedAxisOnMakeColumn(TestCase): 
    """
        Regression test for #5427: traces should reference the primary axis
        when shared_xaxes=True, so spike lines and hover sync work correctly.
    """
    
    def test_xaxes_shared_columns_mode_single_column(self):
        """
            When 'columns' mode for shared_xaxis, all of the traces in the same column should reference the same x-axis
        """

        from plotly.subplots import make_subplots
        from plotly.graph_objects import Figure, Scatter, XAxis

        fig : Figure = make_subplots(rows=3, cols=1, shared_xaxes='columns')

        trace_1 : Scatter = Scatter(x=[1, 2, 3], y=[1, 2, 3])
        trace_2 : Scatter = Scatter(x=[1, 2, 3], y=[4, 5, 6])
        trace_3 : Scatter = Scatter(x=[1, 2, 3], y=[7, 8, 9])

        fig.add_trace(trace_1, row=1, col=1)
        fig.add_trace(trace_2, row=2, col=1)
        fig.add_trace(trace_3, row=3, col=1)
        

        # The x-axis of all of the figures should be the same
        trace_1_xaxis : XAxis = fig.data[0].xaxis
        trace_2_xaxis : XAxis = fig.data[1].xaxis
        trace_3_xaxis : XAxis = fig.data[2].xaxis

        self.assertEqual(trace_1_xaxis, trace_2_xaxis, "Shared x-axis column don't match: Figure 1 and Figure 2 have different x-axes")
        self.assertEqual(trace_1_xaxis, trace_3_xaxis, "Shared x-axis column don't match: Figure 1 and Figure 3 have different x-axes")
        self.assertEqual(trace_2_xaxis, trace_3_xaxis, "Shared x-axis column don't match: Figure 2 and Figure 3 have different x-axes")

    def test_xaxes_shared_columns_mode_multiple_columns(self): 
        """
            When 'columns' mode for shared_xaxis, different columns should have different references
        """
        from plotly.subplots import make_subplots
        from plotly.graph_objects import Figure, Scatter, XAxis

        fig : Figure = make_subplots(rows=2, cols=2, shared_xaxes='columns')

        trace_1 : Scatter = Scatter(x=[1, 2, 3], y=[1, 2, 3])
        trace_2 : Scatter = Scatter(x=[1, 2, 3], y=[4, 5, 6])
        trace_3 : Scatter = Scatter(x=[1, 2, 3], y=[7, 8, 9])
        trace_4 : Scatter = Scatter(x=[1, 2, 3], y=[10, 11, 12])

        fig.add_trace(trace_1, row=1, col=1)
        fig.add_trace(trace_2, row=2, col=1)
        fig.add_trace(trace_3, row=1, col=2)
        fig.add_trace(trace_4, row=2, col=2)

        fig.update_xaxes()
        fig.update_layout()

        # The x-axis of figures that are in the same column should be the same, and different if they are in different columns
        trace_1_xaxis : XAxis = fig.data[0].xaxis
        trace_2_xaxis : XAxis = fig.data[1].xaxis
        trace_3_xaxis : XAxis = fig.data[2].xaxis
        trace_4_xaxis : XAxis = fig.data[3].xaxis

        self.assertEqual(trace_1_xaxis, trace_2_xaxis, "Shared x-axis column don't match: Figure 1 and Figure 2 have different x-axes")
        self.assertEqual(trace_3_xaxis, trace_4_xaxis, "Shared x-axis column don't match: Figure 3 and Figure 4 have different x-axes")
        self.assertNotEqual(trace_1_xaxis, trace_3_xaxis, "Different x-axis column match: Figure 1 and Figure 3 have the same x-axes")
        self.assertNotEqual(trace_2_xaxis, trace_4_xaxis, "Different x-axis column match: Figure 2 and Figure 4 have the same x-axes")

    def test_xaxes_shared_rows_mode_single_row(self):
        """
            When 'rows' mode for shared_xaxis, all of the traces in the same row should reference the same x-axis
        """

        from plotly.subplots import make_subplots
        from plotly.graph_objects import Figure, Scatter, XAxis

        fig : Figure = make_subplots(rows=1, cols=3, shared_xaxes='rows')

        trace_1 : Scatter = Scatter(x=[1, 2, 3], y=[1, 2, 3])
        trace_2 : Scatter = Scatter(x=[1, 2, 3], y=[4, 5, 6])
        trace_3 : Scatter = Scatter(x=[1, 2, 3], y=[7, 8, 9])

        fig.add_trace(trace_1, row=1, col=1)
        fig.add_trace(trace_2, row=1, col=2)
        fig.add_trace(trace_3, row=1, col=3)

        fig.update_xaxes()
        fig.update_layout()

        # The x-axis of all of the figures should be the same
        trace_1_xaxis : XAxis = fig.data[0].xaxis
        trace_2_xaxis : XAxis = fig.data[1].xaxis
        trace_3_xaxis : XAxis = fig.data[2].xaxis

        self.assertEqual(trace_1_xaxis, trace_2_xaxis, "Shared x-axis row don't match: Figure 1 and Figure 2 have different x-axes")
        self.assertEqual(trace_1_xaxis, trace_3_xaxis, "Shared x-axis row don't match: Figure 1 and Figure 3 have different x-axes")
        self.assertEqual(trace_2_xaxis, trace_3_xaxis, "Shared x-axis row don't match: Figure 2 and Figure 3 have different x-axes")

    def test_xaxes_shared_rows_mode_multiple_rows(self): 
        """
            When 'rows' mode for shared_xaxis, different rows should have different references
        """
        from plotly.subplots import make_subplots
        from plotly.graph_objects import Figure, Scatter, XAxis

        fig : Figure = make_subplots(rows=2, cols=2, shared_xaxes='rows')

        trace_1 : Scatter = Scatter(x=[1, 2, 3], y=[1, 2, 3])
        trace_2 : Scatter = Scatter(x=[1, 2, 3], y=[4, 5, 6])
        trace_3 : Scatter = Scatter(x=[1, 2, 3], y=[7, 8, 9])
        trace_4 : Scatter = Scatter(x=[1, 2, 3], y=[10, 11, 12])

        fig.add_trace(trace_1, row=1, col=1)
        fig.add_trace(trace_2, row=1, col=2)
        fig.add_trace(trace_3, row=2, col=1)
        fig.add_trace(trace_4, row=2, col=2)

        fig.update_xaxes()
        fig.update_layout()

        # The x-axis of figures in the same row should be the same, and different if they are in different rows
        trace_1_xaxis : XAxis = fig.data[0].xaxis
        trace_2_xaxis : XAxis = fig.data[1].xaxis
        trace_3_xaxis : XAxis = fig.data[2].xaxis
        trace_4_xaxis : XAxis = fig.data[3].xaxis

        self.assertEqual(trace_1_xaxis, trace_2_xaxis, "Shared x-axis row don't match: Figure 1 and Figure 2 have different x-axes")
        self.assertEqual(trace_3_xaxis, trace_4_xaxis, "Shared x-axis row don't match: Figure 3 and Figure 4 have different x-axes")
        self.assertNotEqual(trace_1_xaxis, trace_3_xaxis, "Different x-axis row match: Figure 1 and Figure 3 have the same x-axes")
        self.assertNotEqual(trace_2_xaxis, trace_4_xaxis, "Different x-axis row match: Figure 2 and Figure 4 have the same x-axes")

    def test_xaxes_shared_all_mode(self): 
        """
            When 'all' mode for shared_xaxis, all rows share the same x-axes
        """
        from plotly.subplots import make_subplots
        from plotly.graph_objects import Figure, Scatter, XAxis

        fig : Figure = make_subplots(rows=2, cols=2, shared_xaxes='all')

        trace_1 : Scatter = Scatter(x=[1, 2, 3], y=[1, 2, 3])
        trace_2 : Scatter = Scatter(x=[1, 2, 3], y=[4, 5, 6])
        trace_3 : Scatter = Scatter(x=[1, 2, 3], y=[7, 8, 9])
        trace_4 : Scatter = Scatter(x=[1, 2, 3], y=[10, 11, 12])

        fig.add_trace(trace_1, row=1, col=1)
        fig.add_trace(trace_2, row=1, col=2)
        fig.add_trace(trace_3, row=2, col=1)
        fig.add_trace(trace_4, row=2, col=2)

        fig.update_xaxes()
        fig.update_layout()

        # The x-axis of all the figures should be the same
        trace_1_xaxis : XAxis = fig.data[0].xaxis
        trace_2_xaxis : XAxis = fig.data[1].xaxis
        trace_3_xaxis : XAxis = fig.data[2].xaxis
        trace_4_xaxis : XAxis = fig.data[3].xaxis

        self.assertEqual(trace_1_xaxis, trace_2_xaxis, "Shared x-axis all don't match: Figure 1 and Figure 2 have different x-axes")
        self.assertEqual(trace_3_xaxis, trace_4_xaxis, "Shared x-axis all don't match: Figure 3 and Figure 4 have different x-axes")
        self.assertEqual(trace_1_xaxis, trace_3_xaxis, "Shared x-axis all don't match: Figure 1 and Figure 3 have the same x-axes")
        self.assertEqual(trace_2_xaxis, trace_4_xaxis, "Shared x-axis all don't match: Figure 2 and Figure 4 have the same x-axes")

    def test_xaxes_not_shared_mode(self):
        """
            When not shared, all plots have different x-axes
        """
        from plotly.subplots import make_subplots
        from plotly.graph_objects import Figure, Scatter, XAxis

        fig : Figure = make_subplots(rows=2, cols=2, shared_xaxes=False)

        trace_1 : Scatter = Scatter(x=[1, 2, 3], y=[1, 2, 3])
        trace_2 : Scatter = Scatter(x=[1, 2, 3], y=[4, 5, 6])
        trace_3 : Scatter = Scatter(x=[1, 2, 3], y=[7, 8, 9])
        trace_4 : Scatter = Scatter(x=[1, 2, 3], y=[10, 11, 12])

        fig.add_trace(trace_1, row=1, col=1)
        fig.add_trace(trace_2, row=1, col=2)
        fig.add_trace(trace_3, row=2, col=1)
        fig.add_trace(trace_4, row=2, col=2)

        
        fig.update_xaxes()
        fig.update_layout()

        # The x-axis of all of the figures should be different
        trace_1_xaxis : XAxis = fig.data[0].xaxis
        trace_2_xaxis : XAxis = fig.data[1].xaxis
        trace_3_xaxis : XAxis = fig.data[2].xaxis
        trace_4_xaxis : XAxis = fig.data[3].xaxis

        self.assertNotEqual(trace_1_xaxis, trace_2_xaxis, "Different x-axis match: Figure 1 and Figure 2 have the same x-axes")
        self.assertNotEqual(trace_1_xaxis, trace_3_xaxis, "Different x-axis match: Figure 1 and Figure 3 have the same x-axes")
        self.assertNotEqual(trace_1_xaxis, trace_4_xaxis, "Different x-axis match: Figure 1 and Figure 4 have the same x-axes")
        self.assertNotEqual(trace_2_xaxis, trace_3_xaxis, "Different x-axis match: Figure 2 and Figure 3 have the same x-axes")
        self.assertNotEqual(trace_2_xaxis, trace_4_xaxis, "Different x-axis match: Figure 2 and Figure 4 have the same x-axes")
        self.assertNotEqual(trace_3_xaxis, trace_4_xaxis, "Different x-axis match: Figure 3 and Figure 4 have the same x-axes")