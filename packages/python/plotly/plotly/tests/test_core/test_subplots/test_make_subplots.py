from __future__ import absolute_import

from unittest import TestCase
import pytest
from plotly.graph_objs import (
    Annotation,
    Annotations,
    Data,
    Figure,
    Font,
    Layout,
    layout,
    Scene,
    XAxis,
    YAxis,
)
import plotly.tools as tls
from plotly import subplots


class TestMakeSubplots(TestCase):
    """
    Test plotly.tools.make_subplots in v4_subplots mode

    In version 4, change this to test plotly.subplots.make_subplots directly
    """

    def test_non_integer_rows(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2.1)

    def test_less_than_zero_rows(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=-2)

    def test_non_integer_cols(self):
        with self.assertRaises(Exception):
            tls.make_subplots(cols=2 / 3)

    def test_less_than_zero_cols(self):
        with self.assertRaises(Exception):
            tls.make_subplots(cols=-10)

    def test_wrong_kwarg(self):
        with self.assertRaises(Exception):
            tls.make_subplots(stuff="no gonna work")

    def test_start_cell_wrong_values(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, cols=2, start_cell="not gonna work")

    def test_specs_wrong_type(self):
        with self.assertRaises(Exception):
            tls.make_subplots(specs="not going to work")

    def test_specs_wrong_inner_type(self):
        with self.assertRaises(Exception):
            tls.make_subplots(specs=[{}])

    def test_specs_wrong_item_type(self):
        with self.assertRaises(Exception):
            tls.make_subplots(specs=[[("not", "going to work")]])

    def test_specs_wrong_item_key(self):
        with self.assertRaises(Exception):
            tls.make_subplots(specs=[{"not": "going to work"}])

    def test_specs_underspecified(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, specs=[{}])
            tls.make_subplots(rows=2, cols=2, specs=[[{}, {}], [{}]])

    def test_specs_overspecified(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, specs=[[{}], [{}], [{}]])
            tls.make_subplots(cols=2, specs=[{}, {}, {}])

    def test_specs_colspan_too_big(self):
        with self.assertRaises(Exception):
            tls.make_subplots(cols=3, specs=[[{}, None, {"colspan": 2}]])

    def test_specs_rowspan_too_big(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=3, specs=[[{}], [None], [{"rowspan": 2}]])

    def test_insets_wrong_type(self):
        with self.assertRaises(Exception):
            tls.make_subplots(insets="not going to work")

    def test_insets_wrong_item(self):
        with self.assertRaises(Exception):
            tls.make_subplots(insets=[{"not": "going to work"}])

    def test_insets_wrong_cell_row(self):
        with self.assertRaises(Exception):
            tls.make_subplots(insets=([{"cell": (0, 1)}]))

    def test_insets_wrong_cell_col(self):
        with self.assertRaises(Exception):
            tls.make_subplots(insets=([{"cell": (1, 0)}]))

    def test_column_width_not_list(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, cols=2, column_widths="not gonna work")

    def test_column_width_not_list_of_correct_numbers(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, cols=2, column_widths=[0])

    def test_row_width_not_list(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, cols=2, row_heights="not gonna work")

    def test_row_width_not_list_of_correct_numbers(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, cols=2, row_heights=[1])

    def test_single_plot(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 1.0], anchor="y"),
                yaxis1=YAxis(domain=[0.0, 1.0], anchor="x"),
            ),
        )
        self.assertEqual(
            tls.make_subplots().to_plotly_json(), expected.to_plotly_json()
        )

    def test_two_row(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 1.0], anchor="y"),
                xaxis2=XAxis(domain=[0.0, 1.0], anchor="y2"),
                yaxis1=YAxis(domain=[0.575, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.0, 0.425], anchor="x2"),
            ),
        )
        self.assertEqual(
            tls.make_subplots(rows=2).to_plotly_json(), expected.to_plotly_json()
        )

    def test_two_row_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=layout.XAxis(domain=[0.0, 1.0], anchor="y"),
                xaxis2=layout.XAxis(domain=[0.0, 1.0], anchor="y2"),
                yaxis1=layout.YAxis(domain=[0.0, 0.425], anchor="x"),
                yaxis2=layout.YAxis(domain=[0.575, 1.0], anchor="x2"),
            ),
        )
        fig = tls.make_subplots(rows=2, start_cell="bottom-left")
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_two_column(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.45], anchor="y"),
                xaxis2=XAxis(domain=[0.55, 1.0], anchor="y2"),
                yaxis1=YAxis(domain=[0.0, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.0, 1.0], anchor="x2"),
            ),
        )
        self.assertEqual(
            tls.make_subplots(cols=2).to_plotly_json(), expected.to_plotly_json()
        )

    def test_a_lot(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.1183673469387755], anchor="y"),
                xaxis10=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836], anchor="y10"
                ),
                xaxis11=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877], anchor="y11"
                ),
                xaxis12=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918], anchor="y12"
                ),
                xaxis13=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959], anchor="y13"
                ),
                xaxis14=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999], anchor="y14"
                ),
                xaxis15=XAxis(domain=[0.0, 0.1183673469387755], anchor="y15"),
                xaxis16=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955], anchor="y16"
                ),
                xaxis17=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836], anchor="y17"
                ),
                xaxis18=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877], anchor="y18"
                ),
                xaxis19=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918], anchor="y19"
                ),
                xaxis2=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955], anchor="y2"
                ),
                xaxis20=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959], anchor="y20"
                ),
                xaxis21=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999], anchor="y21"
                ),
                xaxis22=XAxis(domain=[0.0, 0.1183673469387755], anchor="y22"),
                xaxis23=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955], anchor="y23"
                ),
                xaxis24=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836], anchor="y24"
                ),
                xaxis25=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877], anchor="y25"
                ),
                xaxis26=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918], anchor="y26"
                ),
                xaxis27=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959], anchor="y27"
                ),
                xaxis28=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999], anchor="y28"
                ),
                xaxis3=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836], anchor="y3"
                ),
                xaxis4=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877], anchor="y4"
                ),
                xaxis5=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918], anchor="y5"
                ),
                xaxis6=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959], anchor="y6"
                ),
                xaxis7=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999], anchor="y7"
                ),
                xaxis8=XAxis(domain=[0.0, 0.1183673469387755], anchor="y8"),
                xaxis9=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955], anchor="y9"
                ),
                yaxis1=YAxis(domain=[0.80625, 1.0], anchor="x"),
                yaxis10=YAxis(domain=[0.5375, 0.73125], anchor="x10"),
                yaxis11=YAxis(domain=[0.5375, 0.73125], anchor="x11"),
                yaxis12=YAxis(domain=[0.5375, 0.73125], anchor="x12"),
                yaxis13=YAxis(domain=[0.5375, 0.73125], anchor="x13"),
                yaxis14=YAxis(domain=[0.5375, 0.73125], anchor="x14"),
                yaxis15=YAxis(domain=[0.26875, 0.4625], anchor="x15"),
                yaxis16=YAxis(domain=[0.26875, 0.4625], anchor="x16"),
                yaxis17=YAxis(domain=[0.26875, 0.4625], anchor="x17"),
                yaxis18=YAxis(domain=[0.26875, 0.4625], anchor="x18"),
                yaxis19=YAxis(domain=[0.26875, 0.4625], anchor="x19"),
                yaxis2=YAxis(domain=[0.80625, 1.0], anchor="x2"),
                yaxis20=YAxis(domain=[0.26875, 0.4625], anchor="x20"),
                yaxis21=YAxis(domain=[0.26875, 0.4625], anchor="x21"),
                yaxis22=YAxis(domain=[0.0, 0.19375], anchor="x22"),
                yaxis23=YAxis(domain=[0.0, 0.19375], anchor="x23"),
                yaxis24=YAxis(domain=[0.0, 0.19375], anchor="x24"),
                yaxis25=YAxis(domain=[0.0, 0.19375], anchor="x25"),
                yaxis26=YAxis(domain=[0.0, 0.19375], anchor="x26"),
                yaxis27=YAxis(domain=[0.0, 0.19375], anchor="x27"),
                yaxis28=YAxis(domain=[0.0, 0.19375], anchor="x28"),
                yaxis3=YAxis(domain=[0.80625, 1.0], anchor="x3"),
                yaxis4=YAxis(domain=[0.80625, 1.0], anchor="x4"),
                yaxis5=YAxis(domain=[0.80625, 1.0], anchor="x5"),
                yaxis6=YAxis(domain=[0.80625, 1.0], anchor="x6"),
                yaxis7=YAxis(domain=[0.80625, 1.0], anchor="x7"),
                yaxis8=YAxis(domain=[0.5375, 0.73125], anchor="x8"),
                yaxis9=YAxis(domain=[0.5375, 0.73125], anchor="x9"),
            ),
        )
        fig = tls.make_subplots(rows=4, cols=7)
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_a_lot_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.1183673469387755], anchor="y"),
                xaxis10=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836], anchor="y10"
                ),
                xaxis11=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877], anchor="y11"
                ),
                xaxis12=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918], anchor="y12"
                ),
                xaxis13=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959], anchor="y13"
                ),
                xaxis14=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999], anchor="y14"
                ),
                xaxis15=XAxis(domain=[0.0, 0.1183673469387755], anchor="y15"),
                xaxis16=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955], anchor="y16"
                ),
                xaxis17=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836], anchor="y17"
                ),
                xaxis18=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877], anchor="y18"
                ),
                xaxis19=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918], anchor="y19"
                ),
                xaxis2=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955], anchor="y2"
                ),
                xaxis20=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959], anchor="y20"
                ),
                xaxis21=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999], anchor="y21"
                ),
                xaxis22=XAxis(domain=[0.0, 0.1183673469387755], anchor="y22"),
                xaxis23=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955], anchor="y23"
                ),
                xaxis24=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836], anchor="y24"
                ),
                xaxis25=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877], anchor="y25"
                ),
                xaxis26=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918], anchor="y26"
                ),
                xaxis27=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959], anchor="y27"
                ),
                xaxis28=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999], anchor="y28"
                ),
                xaxis3=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836], anchor="y3"
                ),
                xaxis4=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877], anchor="y4"
                ),
                xaxis5=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918], anchor="y5"
                ),
                xaxis6=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959], anchor="y6"
                ),
                xaxis7=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999], anchor="y7"
                ),
                xaxis8=XAxis(domain=[0.0, 0.1183673469387755], anchor="y8"),
                xaxis9=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955], anchor="y9"
                ),
                yaxis1=YAxis(domain=[0.0, 0.19375], anchor="x"),
                yaxis10=YAxis(domain=[0.26875, 0.4625], anchor="x10"),
                yaxis11=YAxis(domain=[0.26875, 0.4625], anchor="x11"),
                yaxis12=YAxis(domain=[0.26875, 0.4625], anchor="x12"),
                yaxis13=YAxis(domain=[0.26875, 0.4625], anchor="x13"),
                yaxis14=YAxis(domain=[0.26875, 0.4625], anchor="x14"),
                yaxis15=YAxis(domain=[0.5375, 0.73125], anchor="x15"),
                yaxis16=YAxis(domain=[0.5375, 0.73125], anchor="x16"),
                yaxis17=YAxis(domain=[0.5375, 0.73125], anchor="x17"),
                yaxis18=YAxis(domain=[0.5375, 0.73125], anchor="x18"),
                yaxis19=YAxis(domain=[0.5375, 0.73125], anchor="x19"),
                yaxis2=YAxis(domain=[0.0, 0.19375], anchor="x2"),
                yaxis20=YAxis(domain=[0.5375, 0.73125], anchor="x20"),
                yaxis21=YAxis(domain=[0.5375, 0.73125], anchor="x21"),
                yaxis22=YAxis(domain=[0.80625, 1.0], anchor="x22"),
                yaxis23=YAxis(domain=[0.80625, 1.0], anchor="x23"),
                yaxis24=YAxis(domain=[0.80625, 1.0], anchor="x24"),
                yaxis25=YAxis(domain=[0.80625, 1.0], anchor="x25"),
                yaxis26=YAxis(domain=[0.80625, 1.0], anchor="x26"),
                yaxis27=YAxis(domain=[0.80625, 1.0], anchor="x27"),
                yaxis28=YAxis(domain=[0.80625, 1.0], anchor="x28"),
                yaxis3=YAxis(domain=[0.0, 0.19375], anchor="x3"),
                yaxis4=YAxis(domain=[0.0, 0.19375], anchor="x4"),
                yaxis5=YAxis(domain=[0.0, 0.19375], anchor="x5"),
                yaxis6=YAxis(domain=[0.0, 0.19375], anchor="x6"),
                yaxis7=YAxis(domain=[0.0, 0.19375], anchor="x7"),
                yaxis8=YAxis(domain=[0.26875, 0.4625], anchor="x8"),
                yaxis9=YAxis(domain=[0.26875, 0.4625], anchor="x9"),
            ),
        )
        fig = tls.make_subplots(rows=4, cols=7, start_cell="bottom-left")
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_spacing(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.3], anchor="y"),
                xaxis2=XAxis(domain=[0.35, 0.6499999999999999], anchor="y2"),
                xaxis3=XAxis(domain=[0.7, 1.0], anchor="y3"),
                xaxis4=XAxis(domain=[0.0, 0.3], anchor="y4"),
                xaxis5=XAxis(domain=[0.35, 0.6499999999999999], anchor="y5"),
                xaxis6=XAxis(domain=[0.7, 1.0], anchor="y6"),
                yaxis1=YAxis(domain=[0.55, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.55, 1.0], anchor="x2"),
                yaxis3=YAxis(domain=[0.55, 1.0], anchor="x3"),
                yaxis4=YAxis(domain=[0.0, 0.45], anchor="x4"),
                yaxis5=YAxis(domain=[0.0, 0.45], anchor="x5"),
                yaxis6=YAxis(domain=[0.0, 0.45], anchor="x6"),
            ),
        )
        fig = tls.make_subplots(
            rows=2, cols=3, horizontal_spacing=0.05, vertical_spacing=0.1
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.2888888888888889], anchor="y"),
                xaxis2=XAxis(domain=[0.0, 0.2888888888888889], anchor="y2"),
                xaxis3=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445], anchor="y3"
                ),
                xaxis4=XAxis(domain=[0.7111111111111111, 1.0], anchor="y4"),
                yaxis1=YAxis(domain=[0.575, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.0, 0.425], anchor="x2"),
                yaxis3=YAxis(domain=[0.0, 0.425], anchor="x3"),
                yaxis4=YAxis(domain=[0.0, 0.425], anchor="x4"),
            ),
        )
        fig = tls.make_subplots(rows=2, cols=3, specs=[[{}, None, None], [{}, {}, {}]])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.2888888888888889], anchor="y"),
                xaxis2=XAxis(domain=[0.0, 0.2888888888888889], anchor="y2"),
                xaxis3=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445], anchor="y3"
                ),
                xaxis4=XAxis(domain=[0.7111111111111111, 1.0], anchor="y4"),
                yaxis1=YAxis(domain=[0.0, 0.425], anchor="x"),
                yaxis2=YAxis(domain=[0.575, 1.0], anchor="x2"),
                yaxis3=YAxis(domain=[0.575, 1.0], anchor="x3"),
                yaxis4=YAxis(domain=[0.575, 1.0], anchor="x4"),
            ),
        )
        fig = tls.make_subplots(
            rows=2,
            cols=3,
            specs=[[{}, None, None], [{}, {}, {}]],
            start_cell="bottom-left",
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_colspan(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 1.0], anchor="y"),
                xaxis2=XAxis(domain=[0.0, 0.45], anchor="y2"),
                xaxis3=XAxis(domain=[0.55, 1.0], anchor="y3"),
                xaxis4=XAxis(domain=[0.0, 0.45], anchor="y4"),
                xaxis5=XAxis(domain=[0.55, 1.0], anchor="y5"),
                yaxis1=YAxis(domain=[0.7333333333333333, 1.0], anchor="x"),
                yaxis2=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333], anchor="x2"
                ),
                yaxis3=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333], anchor="x3"
                ),
                yaxis4=YAxis(domain=[0.0, 0.26666666666666666], anchor="x4"),
                yaxis5=YAxis(domain=[0.0, 0.26666666666666666], anchor="x5"),
            ),
        )
        fig = tls.make_subplots(
            rows=3, cols=2, specs=[[{"colspan": 2}, None], [{}, {}], [{}, {}]]
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_rowspan(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.2888888888888889], anchor="y"),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445], anchor="y2"
                ),
                xaxis3=XAxis(domain=[0.7111111111111111, 1.0], anchor="y3"),
                xaxis4=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445], anchor="y4"
                ),
                xaxis5=XAxis(domain=[0.7111111111111111, 1.0], anchor="y5"),
                xaxis6=XAxis(domain=[0.35555555555555557, 1.0], anchor="y6"),
                yaxis1=YAxis(domain=[0.0, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.7333333333333333, 1.0], anchor="x2"),
                yaxis3=YAxis(domain=[0.7333333333333333, 1.0], anchor="x3"),
                yaxis4=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333], anchor="x4"
                ),
                yaxis5=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333], anchor="x5"
                ),
                yaxis6=YAxis(domain=[0.0, 0.26666666666666666], anchor="x6"),
            ),
        )
        fig = tls.make_subplots(
            rows=3,
            cols=3,
            specs=[
                [{"rowspan": 3}, {}, {}],
                [None, {}, {}],
                [None, {"colspan": 2}, None],
            ],
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_rowspan2(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.2888888888888889], anchor="y"),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445], anchor="y2"
                ),
                xaxis3=XAxis(domain=[0.7111111111111111, 1.0], anchor="y3"),
                xaxis4=XAxis(domain=[0.0, 0.6444444444444445], anchor="y4"),
                xaxis5=XAxis(domain=[0.0, 1.0], anchor="y5"),
                yaxis1=YAxis(domain=[0.7333333333333333, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.7333333333333333, 1.0], anchor="x2"),
                yaxis3=YAxis(domain=[0.36666666666666664, 1.0], anchor="x3"),
                yaxis4=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333], anchor="x4"
                ),
                yaxis5=YAxis(domain=[0.0, 0.26666666666666666], anchor="x5"),
            ),
        )
        fig = tls.make_subplots(
            rows=3,
            cols=3,
            specs=[
                [{}, {}, {"rowspan": 2}],
                [{"colspan": 2}, None, None],
                [{"colspan": 3}, None, None],
            ],
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_colspan_rowpan(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.6444444444444445], anchor="y"),
                xaxis2=XAxis(domain=[0.7111111111111111, 1.0], anchor="y2"),
                xaxis3=XAxis(domain=[0.7111111111111111, 1.0], anchor="y3"),
                xaxis4=XAxis(domain=[0.0, 0.2888888888888889], anchor="y4"),
                xaxis5=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445], anchor="y5"
                ),
                xaxis6=XAxis(domain=[0.7111111111111111, 1.0], anchor="y6"),
                yaxis1=YAxis(domain=[0.36666666666666664, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.7333333333333333, 1.0], anchor="x2"),
                yaxis3=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333], anchor="x3"
                ),
                yaxis4=YAxis(domain=[0.0, 0.26666666666666666], anchor="x4"),
                yaxis5=YAxis(domain=[0.0, 0.26666666666666666], anchor="x5"),
                yaxis6=YAxis(domain=[0.0, 0.26666666666666666], anchor="x6"),
            ),
        )
        fig = tls.make_subplots(
            rows=3,
            cols=3,
            specs=[
                [{"colspan": 2, "rowspan": 2}, None, {}],
                [None, None, {}],
                [{}, {}, {}],
            ],
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_colspan_rowpan_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.6444444444444445], anchor="y"),
                xaxis2=XAxis(domain=[0.7111111111111111, 1.0], anchor="y2"),
                xaxis3=XAxis(domain=[0.7111111111111111, 1.0], anchor="y3"),
                xaxis4=XAxis(domain=[0.0, 0.2888888888888889], anchor="y4"),
                xaxis5=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445], anchor="y5"
                ),
                xaxis6=XAxis(domain=[0.7111111111111111, 1.0], anchor="y6"),
                yaxis1=YAxis(domain=[0.0, 0.6333333333333333], anchor="x"),
                yaxis2=YAxis(domain=[0.0, 0.26666666666666666], anchor="x2"),
                yaxis3=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333], anchor="x3"
                ),
                yaxis4=YAxis(domain=[0.7333333333333333, 1.0], anchor="x4"),
                yaxis5=YAxis(domain=[0.7333333333333333, 1.0], anchor="x5"),
                yaxis6=YAxis(domain=[0.7333333333333333, 1.0], anchor="x6"),
            ),
        )
        fig = tls.make_subplots(
            rows=3,
            cols=3,
            specs=[
                [{"colspan": 2, "rowspan": 2}, None, {}],
                [None, None, {}],
                [{}, {}, {}],
            ],
            start_cell="bottom-left",
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_is_3d(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                scene=Scene(domain={"y": [0.575, 1.0], "x": [0.0, 0.45]}),
                scene2=Scene(domain={"y": [0.0, 0.425], "x": [0.0, 0.45]}),
                xaxis1=XAxis(domain=[0.55, 1.0], anchor="y"),
                xaxis2=XAxis(domain=[0.55, 1.0], anchor="y2"),
                yaxis1=YAxis(domain=[0.575, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.0, 0.425], anchor="x2"),
            ),
        )
        fig = tls.make_subplots(
            rows=2, cols=2, specs=[[{"is_3d": True}, {}], [{"is_3d": True}, {}]]
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_padding(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.1, 0.5], anchor="y"),
                xaxis2=XAxis(domain=[0.5, 1.0], anchor="y2"),
                xaxis3=XAxis(domain=[0.0, 0.5], anchor="y3"),
                xaxis4=XAxis(domain=[0.5, 0.9], anchor="y4"),
                yaxis1=YAxis(domain=[0.5, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.7, 1.0], anchor="x2"),
                yaxis3=YAxis(domain=[0.0, 0.3], anchor="x3"),
                yaxis4=YAxis(domain=[0.0, 0.5], anchor="x4"),
            ),
        )
        fig = tls.make_subplots(
            rows=2,
            cols=2,
            horizontal_spacing=0,
            vertical_spacing=0,
            specs=[[{"l": 0.1}, {"b": 0.2}], [{"t": 0.2}, {"r": 0.1}]],
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_padding_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.1, 0.5], anchor="y"),
                xaxis2=XAxis(domain=[0.5, 1.0], anchor="y2"),
                xaxis3=XAxis(domain=[0.0, 0.5], anchor="y3"),
                xaxis4=XAxis(domain=[0.5, 0.9], anchor="y4"),
                yaxis1=YAxis(domain=[0.0, 0.5], anchor="x"),
                yaxis2=YAxis(domain=[0.2, 0.5], anchor="x2"),
                yaxis3=YAxis(domain=[0.5, 0.8], anchor="x3"),
                yaxis4=YAxis(domain=[0.5, 1.0], anchor="x4"),
            ),
        )
        fig = tls.make_subplots(
            rows=2,
            cols=2,
            horizontal_spacing=0,
            vertical_spacing=0,
            specs=[[{"l": 0.1}, {"b": 0.2}], [{"t": 0.2}, {"r": 0.1}]],
            start_cell="bottom-left",
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_xaxes(self):
        expected = Figure(
            data=Data(),
            layout={
                "xaxis": {
                    "anchor": "y",
                    "domain": [0.0, 0.2888888888888889],
                    "matches": "x4",
                    "showticklabels": False,
                },
                "xaxis2": {
                    "anchor": "y2",
                    "domain": [0.35555555555555557, 0.6444444444444445],
                    "matches": "x5",
                    "showticklabels": False,
                },
                "xaxis3": {
                    "anchor": "y3",
                    "domain": [0.7111111111111111, 1.0],
                    "matches": "x6",
                    "showticklabels": False,
                },
                "xaxis4": {"anchor": "y4", "domain": [0.0, 0.2888888888888889]},
                "xaxis5": {
                    "anchor": "y5",
                    "domain": [0.35555555555555557, 0.6444444444444445],
                },
                "xaxis6": {"anchor": "y6", "domain": [0.7111111111111111, 1.0]},
                "yaxis": {"anchor": "x", "domain": [0.575, 1.0]},
                "yaxis2": {"anchor": "x2", "domain": [0.575, 1.0]},
                "yaxis3": {"anchor": "x3", "domain": [0.575, 1.0]},
                "yaxis4": {"anchor": "x4", "domain": [0.0, 0.425]},
                "yaxis5": {"anchor": "x5", "domain": [0.0, 0.425]},
                "yaxis6": {"anchor": "x6", "domain": [0.0, 0.425]},
            },
        )

        fig = tls.make_subplots(rows=2, cols=3, shared_xaxes=True)
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_xaxes_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout={
                "xaxis": {"anchor": "y", "domain": [0.0, 0.2888888888888889]},
                "xaxis2": {
                    "anchor": "y2",
                    "domain": [0.35555555555555557, 0.6444444444444445],
                },
                "xaxis3": {"anchor": "y3", "domain": [0.7111111111111111, 1.0]},
                "xaxis4": {
                    "anchor": "y4",
                    "domain": [0.0, 0.2888888888888889],
                    "matches": "x",
                    "showticklabels": False,
                },
                "xaxis5": {
                    "anchor": "y5",
                    "domain": [0.35555555555555557, 0.6444444444444445],
                    "matches": "x2",
                    "showticklabels": False,
                },
                "xaxis6": {
                    "anchor": "y6",
                    "domain": [0.7111111111111111, 1.0],
                    "matches": "x3",
                    "showticklabels": False,
                },
                "yaxis": {"anchor": "x", "domain": [0.0, 0.425]},
                "yaxis2": {"anchor": "x2", "domain": [0.0, 0.425]},
                "yaxis3": {"anchor": "x3", "domain": [0.0, 0.425]},
                "yaxis4": {"anchor": "x4", "domain": [0.575, 1.0]},
                "yaxis5": {"anchor": "x5", "domain": [0.575, 1.0]},
                "yaxis6": {"anchor": "x6", "domain": [0.575, 1.0]},
            },
        )
        fig = tls.make_subplots(
            rows=2, cols=3, shared_xaxes=True, start_cell="bottom-left"
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_yaxes(self):
        expected = Figure(
            data=Data(),
            layout={
                "xaxis": {"anchor": "y", "domain": [0.0, 0.45]},
                "xaxis10": {"anchor": "y10", "domain": [0.55, 1.0]},
                "xaxis2": {"anchor": "y2", "domain": [0.55, 1.0]},
                "xaxis3": {"anchor": "y3", "domain": [0.0, 0.45]},
                "xaxis4": {"anchor": "y4", "domain": [0.55, 1.0]},
                "xaxis5": {"anchor": "y5", "domain": [0.0, 0.45]},
                "xaxis6": {"anchor": "y6", "domain": [0.55, 1.0]},
                "xaxis7": {"anchor": "y7", "domain": [0.0, 0.45]},
                "xaxis8": {"anchor": "y8", "domain": [0.55, 1.0]},
                "xaxis9": {"anchor": "y9", "domain": [0.0, 0.45]},
                "yaxis": {"anchor": "x", "domain": [0.848, 1.0]},
                "yaxis10": {
                    "anchor": "x10",
                    "domain": [0.0, 0.152],
                    "matches": "y9",
                    "showticklabels": False,
                },
                "yaxis2": {
                    "anchor": "x2",
                    "domain": [0.848, 1.0],
                    "matches": "y",
                    "showticklabels": False,
                },
                "yaxis3": {
                    "anchor": "x3",
                    "domain": [0.6359999999999999, 0.7879999999999999],
                },
                "yaxis4": {
                    "anchor": "x4",
                    "domain": [0.6359999999999999, 0.7879999999999999],
                    "matches": "y3",
                    "showticklabels": False,
                },
                "yaxis5": {"anchor": "x5", "domain": [0.424, 0.576]},
                "yaxis6": {
                    "anchor": "x6",
                    "domain": [0.424, 0.576],
                    "matches": "y5",
                    "showticklabels": False,
                },
                "yaxis7": {"anchor": "x7", "domain": [0.212, 0.364]},
                "yaxis8": {
                    "anchor": "x8",
                    "domain": [0.212, 0.364],
                    "matches": "y7",
                    "showticklabels": False,
                },
                "yaxis9": {"anchor": "x9", "domain": [0.0, 0.152]},
            },
        )
        fig = tls.make_subplots(rows=5, cols=2, shared_yaxes=True)
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_xaxes_yaxes(self):
        expected = Figure(
            data=Data(),
            layout={
                "xaxis": {
                    "anchor": "y",
                    "domain": [0.0, 0.2888888888888889],
                    "matches": "x7",
                    "showticklabels": False,
                },
                "xaxis2": {
                    "anchor": "y2",
                    "domain": [0.35555555555555557, 0.6444444444444445],
                    "matches": "x8",
                    "showticklabels": False,
                },
                "xaxis3": {
                    "anchor": "y3",
                    "domain": [0.7111111111111111, 1.0],
                    "matches": "x9",
                    "showticklabels": False,
                },
                "xaxis4": {
                    "anchor": "y4",
                    "domain": [0.0, 0.2888888888888889],
                    "matches": "x7",
                    "showticklabels": False,
                },
                "xaxis5": {
                    "anchor": "y5",
                    "domain": [0.35555555555555557, 0.6444444444444445],
                    "matches": "x8",
                    "showticklabels": False,
                },
                "xaxis6": {
                    "anchor": "y6",
                    "domain": [0.7111111111111111, 1.0],
                    "matches": "x9",
                    "showticklabels": False,
                },
                "xaxis7": {"anchor": "y7", "domain": [0.0, 0.2888888888888889]},
                "xaxis8": {
                    "anchor": "y8",
                    "domain": [0.35555555555555557, 0.6444444444444445],
                },
                "xaxis9": {"anchor": "y9", "domain": [0.7111111111111111, 1.0]},
                "yaxis": {"anchor": "x", "domain": [0.7333333333333333, 1.0]},
                "yaxis2": {
                    "anchor": "x2",
                    "domain": [0.7333333333333333, 1.0],
                    "matches": "y",
                    "showticklabels": False,
                },
                "yaxis3": {
                    "anchor": "x3",
                    "domain": [0.7333333333333333, 1.0],
                    "matches": "y",
                    "showticklabels": False,
                },
                "yaxis4": {
                    "anchor": "x4",
                    "domain": [0.36666666666666664, 0.6333333333333333],
                },
                "yaxis5": {
                    "anchor": "x5",
                    "domain": [0.36666666666666664, 0.6333333333333333],
                    "matches": "y4",
                    "showticklabels": False,
                },
                "yaxis6": {
                    "anchor": "x6",
                    "domain": [0.36666666666666664, 0.6333333333333333],
                    "matches": "y4",
                    "showticklabels": False,
                },
                "yaxis7": {"anchor": "x7", "domain": [0.0, 0.26666666666666666]},
                "yaxis8": {
                    "anchor": "x8",
                    "domain": [0.0, 0.26666666666666666],
                    "matches": "y7",
                    "showticklabels": False,
                },
                "yaxis9": {
                    "anchor": "x9",
                    "domain": [0.0, 0.26666666666666666],
                    "matches": "y7",
                    "showticklabels": False,
                },
            },
        )
        fig = tls.make_subplots(rows=3, cols=3, shared_xaxes=True, shared_yaxes=True)
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_xaxes_yaxes_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout={
                "xaxis": {"anchor": "y", "domain": [0.0, 0.2888888888888889]},
                "xaxis2": {
                    "anchor": "y2",
                    "domain": [0.35555555555555557, 0.6444444444444445],
                },
                "xaxis3": {"anchor": "y3", "domain": [0.7111111111111111, 1.0]},
                "xaxis4": {
                    "anchor": "y4",
                    "domain": [0.0, 0.2888888888888889],
                    "matches": "x",
                    "showticklabels": False,
                },
                "xaxis5": {
                    "anchor": "y5",
                    "domain": [0.35555555555555557, 0.6444444444444445],
                    "matches": "x2",
                    "showticklabels": False,
                },
                "xaxis6": {
                    "anchor": "y6",
                    "domain": [0.7111111111111111, 1.0],
                    "matches": "x3",
                    "showticklabels": False,
                },
                "xaxis7": {
                    "anchor": "y7",
                    "domain": [0.0, 0.2888888888888889],
                    "matches": "x",
                    "showticklabels": False,
                },
                "xaxis8": {
                    "anchor": "y8",
                    "domain": [0.35555555555555557, 0.6444444444444445],
                    "matches": "x2",
                    "showticklabels": False,
                },
                "xaxis9": {
                    "anchor": "y9",
                    "domain": [0.7111111111111111, 1.0],
                    "matches": "x3",
                    "showticklabels": False,
                },
                "yaxis": {"anchor": "x", "domain": [0.0, 0.26666666666666666]},
                "yaxis2": {
                    "anchor": "x2",
                    "domain": [0.0, 0.26666666666666666],
                    "matches": "y",
                    "showticklabels": False,
                },
                "yaxis3": {
                    "anchor": "x3",
                    "domain": [0.0, 0.26666666666666666],
                    "matches": "y",
                    "showticklabels": False,
                },
                "yaxis4": {
                    "anchor": "x4",
                    "domain": [0.36666666666666664, 0.6333333333333333],
                },
                "yaxis5": {
                    "anchor": "x5",
                    "domain": [0.36666666666666664, 0.6333333333333333],
                    "matches": "y4",
                    "showticklabels": False,
                },
                "yaxis6": {
                    "anchor": "x6",
                    "domain": [0.36666666666666664, 0.6333333333333333],
                    "matches": "y4",
                    "showticklabels": False,
                },
                "yaxis7": {"anchor": "x7", "domain": [0.7333333333333333, 1.0]},
                "yaxis8": {
                    "anchor": "x8",
                    "domain": [0.7333333333333333, 1.0],
                    "matches": "y7",
                    "showticklabels": False,
                },
                "yaxis9": {
                    "anchor": "x9",
                    "domain": [0.7333333333333333, 1.0],
                    "matches": "y7",
                    "showticklabels": False,
                },
            },
        )
        fig = tls.make_subplots(
            rows=3,
            cols=3,
            shared_xaxes=True,
            shared_yaxes=True,
            start_cell="bottom-left",
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_insets(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.45], anchor="y"),
                xaxis2=XAxis(domain=[0.55, 1.0], anchor="y2"),
                xaxis3=XAxis(domain=[0.0, 0.45], anchor="y3"),
                xaxis4=XAxis(domain=[0.55, 1.0], anchor="y4"),
                xaxis5=XAxis(domain=[0.865, 0.955], anchor="y5"),
                yaxis1=YAxis(domain=[0.575, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.575, 1.0], anchor="x2"),
                yaxis3=YAxis(domain=[0.0, 0.425], anchor="x3"),
                yaxis4=YAxis(domain=[0.0, 0.425], anchor="x4"),
                yaxis5=YAxis(domain=[0.085, 0.2975], anchor="x5"),
            ),
        )
        fig = tls.make_subplots(
            rows=2,
            cols=2,
            insets=[{"cell": (2, 2), "l": 0.7, "w": 0.2, "b": 0.2, "h": 0.5}],
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_insets_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 0.45], anchor="y"),
                xaxis2=XAxis(domain=[0.55, 1.0], anchor="y2"),
                xaxis3=XAxis(domain=[0.0, 0.45], anchor="y3"),
                xaxis4=XAxis(domain=[0.55, 1.0], anchor="y4"),
                xaxis5=XAxis(domain=[0.865, 0.955], anchor="y5"),
                yaxis1=YAxis(domain=[0.0, 0.425], anchor="x"),
                yaxis2=YAxis(domain=[0.0, 0.425], anchor="x2"),
                yaxis3=YAxis(domain=[0.575, 1.0], anchor="x3"),
                yaxis4=YAxis(domain=[0.575, 1.0], anchor="x4"),
                yaxis5=YAxis(
                    domain=[0.6599999999999999, 0.8724999999999999], anchor="x5"
                ),
            ),
        )
        fig = tls.make_subplots(
            rows=2,
            cols=2,
            insets=[{"cell": (2, 2), "l": 0.7, "w": 0.2, "b": 0.2, "h": 0.5}],
            start_cell="bottom-left",
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_insets_multiple(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 1.0], anchor="y"),
                xaxis2=XAxis(domain=[0.0, 1.0], anchor="y2"),
                xaxis3=XAxis(domain=[0.8, 1.0], anchor="y3"),
                xaxis4=XAxis(domain=[0.8, 1.0], anchor="y4"),
                yaxis1=YAxis(domain=[0.575, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.0, 0.425], anchor="x2"),
                yaxis3=YAxis(domain=[0.575, 1.0], anchor="x3"),
                yaxis4=YAxis(domain=[0.0, 0.425], anchor="x4"),
            ),
        )
        fig = tls.make_subplots(
            rows=2, insets=[{"cell": (1, 1), "l": 0.8}, {"cell": (2, 1), "l": 0.8}]
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_insets_multiple_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(domain=[0.0, 1.0], anchor="y"),
                xaxis2=XAxis(domain=[0.0, 1.0], anchor="y2"),
                xaxis3=XAxis(domain=[0.8, 1.0], anchor="y3"),
                xaxis4=XAxis(domain=[0.8, 1.0], anchor="y4"),
                yaxis1=YAxis(domain=[0.0, 0.425], anchor="x"),
                yaxis2=YAxis(domain=[0.575, 1.0], anchor="x2"),
                yaxis3=YAxis(domain=[0.0, 0.425], anchor="x3"),
                yaxis4=YAxis(domain=[0.575, 1.0], anchor="x4"),
            ),
        )
        fig = tls.make_subplots(
            rows=2,
            insets=[{"cell": (1, 1), "l": 0.8}, {"cell": (2, 1), "l": 0.8}],
            start_cell="bottom-left",
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_2x1(self):
        # make a title for each subplot when the layout is 2 rows and 1 column
        expected = Figure(
            data=Data(),
            layout=Layout(
                annotations=Annotations(
                    [
                        Annotation(
                            x=0.5,
                            y=1.0,
                            xref="paper",
                            yref="paper",
                            text="Title 1",
                            showarrow=False,
                            font=Font(size=16),
                            xanchor="center",
                            yanchor="bottom",
                        ),
                        Annotation(
                            x=0.5,
                            y=0.375,
                            xref="paper",
                            yref="paper",
                            text="Title 2",
                            showarrow=False,
                            font=Font(size=16),
                            xanchor="center",
                            yanchor="bottom",
                        ),
                    ]
                ),
                xaxis1=XAxis(domain=[0.0, 1.0], anchor="y"),
                xaxis2=XAxis(domain=[0.0, 1.0], anchor="y2"),
                yaxis1=YAxis(domain=[0.625, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.0, 0.375], anchor="x2"),
            ),
        )
        fig = tls.make_subplots(rows=2, subplot_titles=("Title 1", "Title 2"))
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_1x3(self):
        # make a title for each subplot when the layout is 1 row and 3 columns
        expected = Figure(
            data=Data(),
            layout=Layout(
                annotations=Annotations(
                    [
                        Annotation(
                            x=0.14444444444444446,
                            y=1.0,
                            xref="paper",
                            yref="paper",
                            text="Title 1",
                            showarrow=False,
                            font=Font(size=16),
                            xanchor="center",
                            yanchor="bottom",
                        ),
                        Annotation(
                            x=0.5,
                            y=1.0,
                            xref="paper",
                            yref="paper",
                            text="Title 2",
                            showarrow=False,
                            font=Font(size=16),
                            xanchor="center",
                            yanchor="bottom",
                        ),
                        Annotation(
                            x=0.8555555555555556,
                            y=1.0,
                            xref="paper",
                            yref="paper",
                            text="Title 3",
                            showarrow=False,
                            font=Font(size=16),
                            xanchor="center",
                            yanchor="bottom",
                        ),
                    ]
                ),
                xaxis1=XAxis(domain=[0.0, 0.2888888888888889], anchor="y"),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445], anchor="y2"
                ),
                xaxis3=XAxis(domain=[0.7111111111111111, 1.0], anchor="y3"),
                yaxis1=YAxis(domain=[0.0, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.0, 1.0], anchor="x2"),
                yaxis3=YAxis(domain=[0.0, 1.0], anchor="x3"),
            ),
        )
        fig = tls.make_subplots(
            cols=3, subplot_titles=("Title 1", "Title 2", "Title 3")
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_shared_axes(self):
        # make a title for each subplot when the layout is 1 row and 3 columns
        expected = Figure(
            data=Data(),
            layout={
                "annotations": [
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 1",
                        "x": 0.225,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 1.0,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 2",
                        "x": 0.775,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 1.0,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 3",
                        "x": 0.225,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 0.375,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 4",
                        "x": 0.775,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 0.375,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                ],
                "xaxis": {
                    "anchor": "y",
                    "domain": [0.0, 0.45],
                    "matches": "x3",
                    "showticklabels": False,
                },
                "xaxis2": {
                    "anchor": "y2",
                    "domain": [0.55, 1.0],
                    "matches": "x4",
                    "showticklabels": False,
                },
                "xaxis3": {"anchor": "y3", "domain": [0.0, 0.45]},
                "xaxis4": {"anchor": "y4", "domain": [0.55, 1.0]},
                "yaxis": {"anchor": "x", "domain": [0.625, 1.0]},
                "yaxis2": {
                    "anchor": "x2",
                    "domain": [0.625, 1.0],
                    "matches": "y",
                    "showticklabels": False,
                },
                "yaxis3": {"anchor": "x3", "domain": [0.0, 0.375]},
                "yaxis4": {
                    "anchor": "x4",
                    "domain": [0.0, 0.375],
                    "matches": "y3",
                    "showticklabels": False,
                },
            },
        )

        fig = tls.make_subplots(
            rows=2,
            cols=2,
            subplot_titles=("Title 1", "Title 2", "Title 3", "Title 4"),
            shared_xaxes=True,
            shared_yaxes=True,
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_shared_axes_all(self):
        # make a title for each subplot when the layout is 1 row and 3 columns
        expected = Figure(
            data=Data(),
            layout={
                "annotations": [
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 1",
                        "x": 0.225,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 1.0,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 2",
                        "x": 0.775,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 1.0,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 3",
                        "x": 0.225,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 0.375,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 4",
                        "x": 0.775,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 0.375,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                ],
                "xaxis": {
                    "anchor": "y",
                    "domain": [0.0, 0.45],
                    "matches": "x3",
                    "showticklabels": False,
                },
                "xaxis2": {
                    "anchor": "y2",
                    "domain": [0.55, 1.0],
                    "matches": "x3",
                    "showticklabels": False,
                },
                "xaxis3": {"anchor": "y3", "domain": [0.0, 0.45]},
                "xaxis4": {"anchor": "y4", "domain": [0.55, 1.0], "matches": "x3"},
                "yaxis": {"anchor": "x", "domain": [0.625, 1.0], "matches": "y3"},
                "yaxis2": {
                    "anchor": "x2",
                    "domain": [0.625, 1.0],
                    "matches": "y3",
                    "showticklabels": False,
                },
                "yaxis3": {"anchor": "x3", "domain": [0.0, 0.375]},
                "yaxis4": {
                    "anchor": "x4",
                    "domain": [0.0, 0.375],
                    "matches": "y3",
                    "showticklabels": False,
                },
            },
        )

        fig = tls.make_subplots(
            rows=2,
            cols=2,
            subplot_titles=("Title 1", "Title 2", "Title 3", "Title 4"),
            shared_xaxes="all",
            shared_yaxes="all",
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_shared_axes_rows_columns(self):
        # make a title for each subplot when the layout is 1 row and 3 columns
        expected = Figure(
            data=Data(),
            layout={
                "annotations": [
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 1",
                        "x": 0.225,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 1.0,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 2",
                        "x": 0.775,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 1.0,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 3",
                        "x": 0.225,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 0.375,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                    {
                        "font": {"size": 16},
                        "showarrow": False,
                        "text": "Title 4",
                        "x": 0.775,
                        "xanchor": "center",
                        "xref": "paper",
                        "y": 0.375,
                        "yanchor": "bottom",
                        "yref": "paper",
                    },
                ],
                "xaxis": {"anchor": "y", "domain": [0.0, 0.45]},
                "xaxis2": {"anchor": "y2", "domain": [0.55, 1.0], "matches": "x"},
                "xaxis3": {"anchor": "y3", "domain": [0.0, 0.45]},
                "xaxis4": {"anchor": "y4", "domain": [0.55, 1.0], "matches": "x3"},
                "yaxis": {"anchor": "x", "domain": [0.625, 1.0], "matches": "y3"},
                "yaxis2": {"anchor": "x2", "domain": [0.625, 1.0], "matches": "y4"},
                "yaxis3": {"anchor": "x3", "domain": [0.0, 0.375]},
                "yaxis4": {"anchor": "x4", "domain": [0.0, 0.375]},
            },
        )

        fig = tls.make_subplots(
            rows=2,
            cols=2,
            subplot_titles=("Title 1", "Title 2", "Title 3", "Title 4"),
            shared_xaxes="rows",
            shared_yaxes="columns",
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_irregular_layout(self):
        # make a title for each subplot when the layout is irregular:
        expected = Figure(
            data=Data(),
            layout=Layout(
                annotations=Annotations(
                    [
                        Annotation(
                            x=0.225,
                            y=1.0,
                            xref="paper",
                            yref="paper",
                            text="Title 1",
                            showarrow=False,
                            font=Font(size=16),
                            xanchor="center",
                            yanchor="bottom",
                        ),
                        Annotation(
                            x=0.775,
                            y=1.0,
                            xref="paper",
                            yref="paper",
                            text="Title 2",
                            showarrow=False,
                            font=Font(size=16),
                            xanchor="center",
                            yanchor="bottom",
                        ),
                        Annotation(
                            x=0.5,
                            y=0.375,
                            xref="paper",
                            yref="paper",
                            text="Title 3",
                            showarrow=False,
                            font=Font(size=16),
                            xanchor="center",
                            yanchor="bottom",
                        ),
                    ]
                ),
                xaxis1=XAxis(domain=[0.0, 0.45], anchor="y"),
                xaxis2=XAxis(domain=[0.55, 1.0], anchor="y2"),
                xaxis3=XAxis(domain=[0.0, 1.0], anchor="y3"),
                yaxis1=YAxis(domain=[0.625, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.625, 1.0], anchor="x2"),
                yaxis3=YAxis(domain=[0.0, 0.375], anchor="x3"),
            ),
        )
        fig = tls.make_subplots(
            rows=2,
            cols=2,
            subplot_titles=("Title 1", "Title 2", "Title 3"),
            specs=[[{}, {}], [{"colspan": 2}, None]],
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_insets(self):
        # This should make a title for the inset plot
        # and no title for the main plot.
        expected = Figure(
            data=Data(),
            layout=Layout(
                annotations=Annotations(
                    [
                        Annotation(
                            x=0.85,
                            y=1.0,
                            xref="paper",
                            yref="paper",
                            text="Inset",
                            showarrow=False,
                            font=Font(size=16),
                            xanchor="center",
                            yanchor="bottom",
                        )
                    ]
                ),
                xaxis1=XAxis(domain=[0.0, 1.0], anchor="y"),
                xaxis2=XAxis(domain=[0.7, 1.0], anchor="y2"),
                yaxis1=YAxis(domain=[0.0, 1.0], anchor="x"),
                yaxis2=YAxis(domain=[0.3, 1.0], anchor="x2"),
            ),
        )
        fig = tls.make_subplots(
            insets=[{"cell": (1, 1), "l": 0.7, "b": 0.3}], subplot_titles=("", "Inset")
        )
        self.assertEqual(fig, expected)

    def test_subplot_titles_array(self):
        # Pass python array
        expected = tls.make_subplots(
            insets=[{"cell": (1, 1), "l": 0.7, "b": 0.3}], subplot_titles=("", "Inset")
        )
        fig = tls.make_subplots(
            insets=[{"cell": (1, 1), "l": 0.7, "b": 0.3}], subplot_titles=["", "Inset"]
        )
        self.assertEqual(fig, expected)

    def test_subplot_titles_empty(self):
        # Pass empty array
        expected = tls.make_subplots(insets=[{"cell": (1, 1), "l": 0.7, "b": 0.3}])
        fig = tls.make_subplots(
            insets=[{"cell": (1, 1), "l": 0.7, "b": 0.3}], subplot_titles=[]
        )
        self.assertEqual(fig, expected)

    def test_large_columns_no_errors(self):
        """
        Test that creating subplots with a large number of columns, and
        zero vertical spacing doesn't result in domain values that are out
        of range.

        Here is the error that was reported in GH1031

        ValueError:
            Invalid value of type 'builtins.float' received for the
            'domain[1]' property of layout.yaxis
                Received value: 1.0000000000000007

            The 'domain[1]' property is a number and may be specified as:
              - An int or float in the interval [0, 1]

        """
        v_space = 0.0

        # 2D
        fig = tls.make_subplots(100, 1, vertical_spacing=v_space)

        # 3D
        fig = tls.make_subplots(
            100,
            1,
            vertical_spacing=v_space,
            specs=[[{"is_3d": True}] for _ in range(100)],
        )

    def test_row_width_and_column_width(self):

        expected = Figure(
            {
                "data": [],
                "layout": {
                    "annotations": [
                        {
                            "font": {"size": 16},
                            "showarrow": False,
                            "text": "Title 1",
                            "x": 0.405,
                            "xanchor": "center",
                            "xref": "paper",
                            "y": 1.0,
                            "yanchor": "bottom",
                            "yref": "paper",
                        },
                        {
                            "font": {"size": 16},
                            "showarrow": False,
                            "text": "Title 2",
                            "x": 0.9550000000000001,
                            "xanchor": "center",
                            "xref": "paper",
                            "y": 1.0,
                            "yanchor": "bottom",
                            "yref": "paper",
                        },
                        {
                            "font": {"size": 16},
                            "showarrow": False,
                            "text": "Title 3",
                            "x": 0.405,
                            "xanchor": "center",
                            "xref": "paper",
                            "y": 0.1875,
                            "yanchor": "bottom",
                            "yref": "paper",
                        },
                        {
                            "font": {"size": 16},
                            "showarrow": False,
                            "text": "Title 4",
                            "x": 0.9550000000000001,
                            "xanchor": "center",
                            "xref": "paper",
                            "y": 0.1875,
                            "yanchor": "bottom",
                            "yref": "paper",
                        },
                    ],
                    "xaxis": {"anchor": "y", "domain": [0.0, 0.81]},
                    "xaxis2": {"anchor": "y2", "domain": [0.91, 1.0]},
                    "xaxis3": {"anchor": "y3", "domain": [0.0, 0.81]},
                    "xaxis4": {"anchor": "y4", "domain": [0.91, 1.0]},
                    "yaxis": {"anchor": "x", "domain": [0.4375, 1.0]},
                    "yaxis2": {"anchor": "x2", "domain": [0.4375, 1.0]},
                    "yaxis3": {"anchor": "x3", "domain": [0.0, 0.1875]},
                    "yaxis4": {"anchor": "x4", "domain": [0.0, 0.1875]},
                },
            }
        )
        fig = tls.make_subplots(
            rows=2,
            cols=2,
            subplot_titles=("Title 1", "Title 2", "Title 3", "Title 4"),
            row_heights=[3, 1],
            column_widths=[9, 1],
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

        # Check backward compatible using kwargs
        # named 'row_width', and 'column_width'
        #
        # Note that we manually reverse the order of the list passed to
        # `row_width` because the legacy argument is always applied from
        # bottom to top, whereas the new row_heights argument follows the
        # direction specified by start_cell
        fig = tls.make_subplots(
            rows=2,
            cols=2,
            subplot_titles=("Title 1", "Title 2", "Title 3", "Title 4"),
            row_width=[1, 3],
            column_width=[9, 1],
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_row_width_and_shared_yaxes(self):

        expected = Figure(
            {
                "data": [],
                "layout": {
                    "annotations": [
                        {
                            "font": {"size": 16},
                            "showarrow": False,
                            "text": "Title 1",
                            "x": 0.225,
                            "xanchor": "center",
                            "xref": "paper",
                            "y": 1.0,
                            "yanchor": "bottom",
                            "yref": "paper",
                        },
                        {
                            "font": {"size": 16},
                            "showarrow": False,
                            "text": "Title 2",
                            "x": 0.775,
                            "xanchor": "center",
                            "xref": "paper",
                            "y": 1.0,
                            "yanchor": "bottom",
                            "yref": "paper",
                        },
                        {
                            "font": {"size": 16},
                            "showarrow": False,
                            "text": "Title 3",
                            "x": 0.225,
                            "xanchor": "center",
                            "xref": "paper",
                            "y": 0.1875,
                            "yanchor": "bottom",
                            "yref": "paper",
                        },
                        {
                            "font": {"size": 16},
                            "showarrow": False,
                            "text": "Title 4",
                            "x": 0.775,
                            "xanchor": "center",
                            "xref": "paper",
                            "y": 0.1875,
                            "yanchor": "bottom",
                            "yref": "paper",
                        },
                    ],
                    "xaxis": {"anchor": "y", "domain": [0.0, 0.45]},
                    "xaxis2": {"anchor": "y2", "domain": [0.55, 1.0]},
                    "xaxis3": {"anchor": "y3", "domain": [0.0, 0.45]},
                    "xaxis4": {"anchor": "y4", "domain": [0.55, 1.0]},
                    "yaxis": {"anchor": "x", "domain": [0.4375, 1.0]},
                    "yaxis2": {
                        "anchor": "x2",
                        "domain": [0.4375, 1.0],
                        "matches": "y",
                        "showticklabels": False,
                    },
                    "yaxis3": {"anchor": "x3", "domain": [0.0, 0.1875]},
                    "yaxis4": {
                        "anchor": "x4",
                        "domain": [0.0, 0.1875],
                        "matches": "y3",
                        "showticklabels": False,
                    },
                },
            }
        )

        fig = tls.make_subplots(
            rows=2,
            cols=2,
            row_heights=[3, 1],
            shared_yaxes=True,
            subplot_titles=("Title 1", "Title 2", "Title 3", "Title 4"),
        )

        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_secondary_y(self):
        fig = subplots.make_subplots(rows=1, cols=1, specs=[[{"secondary_y": True}]])

        expected = Figure(
            {
                "data": [],
                "layout": {
                    "xaxis": {"anchor": "y", "domain": [0.0, 0.94]},
                    "yaxis": {"anchor": "x", "domain": [0.0, 1.0]},
                    "yaxis2": {"anchor": "x", "overlaying": "y", "side": "right"},
                },
            }
        )

        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_secondary_y_traces(self):
        fig = subplots.make_subplots(rows=1, cols=1, specs=[[{"secondary_y": True}]])

        fig.add_scatter(y=[1, 3, 2], name="First", row=1, col=1)
        fig.add_scatter(y=[2, 1, 3], name="second", row=1, col=1, secondary_y=True)
        fig.update_traces(uid=None)

        expected = Figure(
            {
                "data": [
                    {
                        "name": "First",
                        "type": "scatter",
                        "y": [1, 3, 2],
                        "xaxis": "x",
                        "yaxis": "y",
                    },
                    {
                        "name": "second",
                        "type": "scatter",
                        "y": [2, 1, 3],
                        "xaxis": "x",
                        "yaxis": "y2",
                    },
                ],
                "layout": {
                    "xaxis": {"anchor": "y", "domain": [0.0, 0.94]},
                    "yaxis": {"anchor": "x", "domain": [0.0, 1.0]},
                    "yaxis2": {"anchor": "x", "overlaying": "y", "side": "right"},
                },
            }
        )
        expected.update_traces(uid=None)

        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_secondary_y_subplots(self):
        fig = subplots.make_subplots(
            rows=2,
            cols=2,
            specs=[
                [{"secondary_y": True}, {"secondary_y": True}],
                [{"secondary_y": True}, {"secondary_y": True}],
            ],
        )

        fig.add_scatter(y=[1, 3, 2], name="First", row=1, col=1)
        fig.add_scatter(y=[2, 1, 3], name="Second", row=1, col=1, secondary_y=True)

        fig.add_scatter(y=[4, 3, 2], name="Third", row=1, col=2)
        fig.add_scatter(y=[8, 1, 3], name="Forth", row=1, col=2, secondary_y=True)

        fig.add_scatter(y=[0, 2, 4], name="Fifth", row=2, col=1)
        fig.add_scatter(y=[2, 1, 3], name="Sixth", row=2, col=1, secondary_y=True)

        fig.add_scatter(y=[2, 4, 0], name="Fifth", row=2, col=2)
        fig.add_scatter(y=[2, 3, 6], name="Sixth", row=2, col=2, secondary_y=True)

        fig.update_traces(uid=None)

        expected = Figure(
            {
                "data": [
                    {
                        "name": "First",
                        "type": "scatter",
                        "xaxis": "x",
                        "y": [1, 3, 2],
                        "yaxis": "y",
                    },
                    {
                        "name": "Second",
                        "type": "scatter",
                        "xaxis": "x",
                        "y": [2, 1, 3],
                        "yaxis": "y2",
                    },
                    {
                        "name": "Third",
                        "type": "scatter",
                        "xaxis": "x2",
                        "y": [4, 3, 2],
                        "yaxis": "y3",
                    },
                    {
                        "name": "Forth",
                        "type": "scatter",
                        "xaxis": "x2",
                        "y": [8, 1, 3],
                        "yaxis": "y4",
                    },
                    {
                        "name": "Fifth",
                        "type": "scatter",
                        "xaxis": "x3",
                        "y": [0, 2, 4],
                        "yaxis": "y5",
                    },
                    {
                        "name": "Sixth",
                        "type": "scatter",
                        "xaxis": "x3",
                        "y": [2, 1, 3],
                        "yaxis": "y6",
                    },
                    {
                        "name": "Fifth",
                        "type": "scatter",
                        "xaxis": "x4",
                        "y": [2, 4, 0],
                        "yaxis": "y7",
                    },
                    {
                        "name": "Sixth",
                        "type": "scatter",
                        "xaxis": "x4",
                        "y": [2, 3, 6],
                        "yaxis": "y8",
                    },
                ],
                "layout": {
                    "xaxis": {"anchor": "y", "domain": [0.0, 0.37]},
                    "xaxis2": {
                        "anchor": "y3",
                        "domain": [0.5700000000000001, 0.9400000000000001],
                    },
                    "xaxis3": {"anchor": "y5", "domain": [0.0, 0.37]},
                    "xaxis4": {
                        "anchor": "y7",
                        "domain": [0.5700000000000001, 0.9400000000000001],
                    },
                    "yaxis": {"anchor": "x", "domain": [0.575, 1.0]},
                    "yaxis2": {"anchor": "x", "overlaying": "y", "side": "right"},
                    "yaxis3": {"anchor": "x2", "domain": [0.575, 1.0]},
                    "yaxis4": {"anchor": "x2", "overlaying": "y3", "side": "right"},
                    "yaxis5": {"anchor": "x3", "domain": [0.0, 0.425]},
                    "yaxis6": {"anchor": "x3", "overlaying": "y5", "side": "right"},
                    "yaxis7": {"anchor": "x4", "domain": [0.0, 0.425]},
                    "yaxis8": {"anchor": "x4", "overlaying": "y7", "side": "right"},
                },
            }
        )

        expected.update_traces(uid=None)

        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_if_passed_figure(self):
        # assert it returns the same figure it was passed
        fig = Figure()
        figsp = subplots.make_subplots(2, 2, figure=fig)
        assert id(fig) == id(figsp)
        # assert the layout is the same when it returns its own figure
        fig2sp = subplots.make_subplots(2, 2)
        assert id(fig2sp) != id(figsp)
        assert fig2sp.layout == figsp.layout


def test_make_subplots_spacing_error():
    # check exception describing maximum value for horizontal_spacing or
    # vertical_spacing is raised when spacing exceeds that value
    for match in [
        (
            "^%s spacing cannot be greater than \(1 / \(%s - 1\)\) = %f."
            % ("Vertical", "rows", 1.0 / 50.0)
        ).replace(".", "\."),
        "The resulting plot would have 51 rows \(rows=51\)\.$",
    ]:
        with pytest.raises(
            ValueError, match=match,
        ):
            fig = subplots.make_subplots(51, 1, vertical_spacing=0.0201)
    for match in [
        (
            "^%s spacing cannot be greater than \(1 / \(%s - 1\)\) = %f."
            % ("Horizontal", "cols", 1.0 / 50.0)
        ).replace(".", "\."),
        "The resulting plot would have 51 columns \(cols=51\)\.$",
    ]:
        with pytest.raises(
            ValueError, match=match,
        ):
            fig = subplots.make_subplots(1, 51, horizontal_spacing=0.0201)
    # Check it's not raised when it's not beyond the maximum
    try:
        fig = subplots.make_subplots(51, 1, vertical_spacing=0.0200)
    except ValueError:
        # This shouldn't happen so we assert False to force failure
        assert False
    try:
        fig = subplots.make_subplots(1, 51, horizontal_spacing=0.0200)
    except ValueError:
        # This shouldn't happen so we assert False to force failure
        assert False
    # make sure any value between 0 and 1 works for horizontal_spacing if cols is 1
    try:
        fig = subplots.make_subplots(1, 1, horizontal_spacing=0)
    except ValueError:
        # This shouldn't happen so we assert False to force failure
        assert False
    try:
        fig = subplots.make_subplots(1, 1, horizontal_spacing=1)
    except ValueError:
        # This shouldn't happen so we assert False to force failure
        assert False
    # make sure any value between 0 and 1 works for horizontal_spacing if cols is 1
    try:
        fig = subplots.make_subplots(1, 1, horizontal_spacing=0)
    except ValueError:
        # This shouldn't happen so we assert False to force failure
        assert False
    # make sure any value between 0 and 1 works for horizontal_spacing if cols is 1
    try:
        fig = subplots.make_subplots(1, 1, horizontal_spacing=1)
    except ValueError:
        # This shouldn't happen so we assert False to force failure
        assert False
    with pytest.raises(
        ValueError, match="^Horizontal spacing must be between 0 and 1\.$"
    ):
        fig = subplots.make_subplots(1, 1, horizontal_spacing=-0.01)
    with pytest.raises(
        ValueError, match="^Horizontal spacing must be between 0 and 1\.$"
    ):
        fig = subplots.make_subplots(1, 1, horizontal_spacing=1.01)
    with pytest.raises(
        ValueError, match="^Vertical spacing must be between 0 and 1\.$"
    ):
        fig = subplots.make_subplots(1, 1, vertical_spacing=-0.01)
    with pytest.raises(
        ValueError, match="^Vertical spacing must be between 0 and 1\.$"
    ):
        fig = subplots.make_subplots(1, 1, vertical_spacing=1.01)
