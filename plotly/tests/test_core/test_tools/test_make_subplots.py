from __future__ import absolute_import

from unittest import TestCase

from plotly.graph_objs import (Annotation, Annotations, Data, Figure, Font,
                               Layout, layout, Scene, XAxis, YAxis)
import plotly.tools as tls


class TestMakeSubplots(TestCase):

    def test_non_integer_rows(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2.1)

    def test_less_than_zero_rows(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=-2)

    def test_non_integer_cols(self):
        with self.assertRaises(Exception):
            tls.make_subplots(cols=2/3)

    def test_less_than_zero_cols(self):
        with self.assertRaises(Exception):
            tls.make_subplots(cols=-10)

    def test_wrong_kwarg(self):
        with self.assertRaises(Exception):
            tls.make_subplots(stuff='no gonna work')

    def test_start_cell_wrong_values(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, cols=2, start_cell='not gonna work')

    def test_specs_wrong_type(self):
        with self.assertRaises(Exception):
            tls.make_subplots(specs="not going to work")

    def test_specs_wrong_inner_type(self):
        with self.assertRaises(Exception):
            tls.make_subplots(specs=[{}])

    def test_specs_wrong_item_type(self):
        with self.assertRaises(Exception):
            tls.make_subplots(specs=[[('not', 'going to work')]])

    def test_specs_wrong_item_key(self):
        with self.assertRaises(Exception):
            tls.make_subplots(specs=[{'not': "going to work"}])

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
            tls.make_subplots(cols=3, specs=[[{}, None, {'colspan': 2}]])

    def test_specs_rowspan_too_big(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=3, specs=[[{}], [None], [{'rowspan': 2}]])

    def test_insets_wrong_type(self):
        with self.assertRaises(Exception):
            tls.make_subplots(insets="not going to work")

    def test_insets_wrong_item(self):
        with self.assertRaises(Exception):
            tls.make_subplots(insets=[{'not': "going to work"}])

    def test_insets_wrong_cell_row(self):
        with self.assertRaises(Exception):
            tls.make_subplots(insets=([{'cell': (0, 1)}]))

    def test_insets_wrong_cell_col(self):
        with self.assertRaises(Exception):
            tls.make_subplots(insets=([{'cell': (1, 0)}]))

    def test_column_width_not_list(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, cols=2, column_width='not gonna work')

    def test_column_width_not_list_of_correct_numbers(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, cols=2, column_width=[0])

    def test_row_width_not_list(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, cols=2, row_width='not gonna work')

    def test_row_width_not_list_of_correct_numbers(self):
        with self.assertRaises(Exception):
            tls.make_subplots(rows=2, cols=2, row_width=[1])

    def test_single_plot(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 1.0],
                    anchor='x'
                )
            )
        )
        self.assertEqual(tls.make_subplots().to_plotly_json(),
                         expected.to_plotly_json())

    def test_two_row(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y2'
                ),
                yaxis1=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x2'
                )
            )
        )
        self.assertEqual(tls.make_subplots(rows=2).to_plotly_json(), expected.to_plotly_json())

    def test_two_row_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=layout.XAxis(
                    domain=[0.0, 1.0],
                    anchor='y'
                ),
                xaxis2=layout.XAxis(
                    domain=[0.0, 1.0],
                    anchor='y2'
                ),
                yaxis1=layout.YAxis(
                    domain=[0.0, 0.425],
                    anchor='x'
                ),
                yaxis2=layout.YAxis(
                    domain=[0.575, 1.0],
                    anchor='x2'
                ),
            )
        )
        fig = tls.make_subplots(rows=2, start_cell='bottom-left')
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_two_column(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y2'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 1.0],
                    anchor='x2'
                )
            )
        )
        self.assertEqual(tls.make_subplots(cols=2).to_plotly_json(), expected.to_plotly_json())

    def test_a_lot(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.1183673469387755],
                    anchor='y'
                ),
                xaxis10=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836],
                    anchor='y10'
                ),
                xaxis11=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877],
                    anchor='y11'
                ),
                xaxis12=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918],
                    anchor='y12'
                ),
                xaxis13=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959],
                    anchor='y13'
                ),
                xaxis14=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999],
                    anchor='y14'
                ),
                xaxis15=XAxis(
                    domain=[0.0, 0.1183673469387755],
                    anchor='y15'
                ),
                xaxis16=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955],
                    anchor='y16'
                ),
                xaxis17=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836],
                    anchor='y17'
                ),
                xaxis18=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877],
                    anchor='y18'
                ),
                xaxis19=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918],
                    anchor='y19'
                ),
                xaxis2=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955],
                    anchor='y2'
                ),
                xaxis20=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959],
                    anchor='y20'
                ),
                xaxis21=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999],
                    anchor='y21'
                ),
                xaxis22=XAxis(
                    domain=[0.0, 0.1183673469387755],
                    anchor='y22'
                ),
                xaxis23=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955],
                    anchor='y23'
                ),
                xaxis24=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836],
                    anchor='y24'
                ),
                xaxis25=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877],
                    anchor='y25'
                ),
                xaxis26=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918],
                    anchor='y26'
                ),
                xaxis27=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959],
                    anchor='y27'
                ),
                xaxis28=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999],
                    anchor='y28'
                ),
                xaxis3=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877],
                    anchor='y4'
                ),
                xaxis5=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918],
                    anchor='y5'
                ),
                xaxis6=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959],
                    anchor='y6'
                ),
                xaxis7=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999],
                    anchor='y7'
                ),
                xaxis8=XAxis(
                    domain=[0.0, 0.1183673469387755],
                    anchor='y8'
                ),
                xaxis9=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955],
                    anchor='y9'
                ),
                yaxis1=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x'
                ),
                yaxis10=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x10'
                ),
                yaxis11=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x11'
                ),
                yaxis12=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x12'
                ),
                yaxis13=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x13'
                ),
                yaxis14=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x14'
                ),
                yaxis15=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x15'
                ),
                yaxis16=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x16'
                ),
                yaxis17=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x17'
                ),
                yaxis18=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x18'
                ),
                yaxis19=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x19'
                ),
                yaxis2=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x2'
                ),
                yaxis20=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x20'
                ),
                yaxis21=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x21'
                ),
                yaxis22=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x22'
                ),
                yaxis23=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x23'
                ),
                yaxis24=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x24'
                ),
                yaxis25=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x25'
                ),
                yaxis26=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x26'
                ),
                yaxis27=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x27'
                ),
                yaxis28=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x28'
                ),
                yaxis3=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x4'
                ),
                yaxis5=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x5'
                ),
                yaxis6=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x6'
                ),
                yaxis7=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x7'
                ),
                yaxis8=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x8'
                ),
                yaxis9=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x9'
                )
            )
        )
        fig = tls.make_subplots(rows=4, cols=7)
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_a_lot_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.1183673469387755],
                    anchor='y'
                ),
                xaxis10=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836],
                    anchor='y10'
                ),
                xaxis11=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877],
                    anchor='y11'
                ),
                xaxis12=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918],
                    anchor='y12'
                ),
                xaxis13=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959],
                    anchor='y13'
                ),
                xaxis14=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999],
                    anchor='y14'
                ),
                xaxis15=XAxis(
                    domain=[0.0, 0.1183673469387755],
                    anchor='y15'
                ),
                xaxis16=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955],
                    anchor='y16'
                ),
                xaxis17=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836],
                    anchor='y17'
                ),
                xaxis18=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877],
                    anchor='y18'
                ),
                xaxis19=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918],
                    anchor='y19'
                ),
                xaxis2=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955],
                    anchor='y2'
                ),
                xaxis20=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959],
                    anchor='y20'
                ),
                xaxis21=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999],
                    anchor='y21'
                ),
                xaxis22=XAxis(
                    domain=[0.0, 0.1183673469387755],
                    anchor='y22'
                ),
                xaxis23=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955],
                    anchor='y23'
                ),
                xaxis24=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836],
                    anchor='y24'
                ),
                xaxis25=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877],
                    anchor='y25'
                ),
                xaxis26=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918],
                    anchor='y26'
                ),
                xaxis27=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959],
                    anchor='y27'
                ),
                xaxis28=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999],
                    anchor='y28'
                ),
                xaxis3=XAxis(
                    domain=[0.29387755102040813, 0.4122448979591836],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.4408163265306122, 0.5591836734693877],
                    anchor='y4'
                ),
                xaxis5=XAxis(
                    domain=[0.5877551020408163, 0.7061224489795918],
                    anchor='y5'
                ),
                xaxis6=XAxis(
                    domain=[0.7346938775510204, 0.8530612244897959],
                    anchor='y6'
                ),
                xaxis7=XAxis(
                    domain=[0.8816326530612244, 0.9999999999999999],
                    anchor='y7'
                ),
                xaxis8=XAxis(
                    domain=[0.0, 0.1183673469387755],
                    anchor='y8'
                ),
                xaxis9=XAxis(
                    domain=[0.14693877551020407, 0.26530612244897955],
                    anchor='y9'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x'
                ),
                yaxis10=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x10'
                ),
                yaxis11=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x11'
                ),
                yaxis12=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x12'
                ),
                yaxis13=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x13'
                ),
                yaxis14=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x14'
                ),
                yaxis15=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x15'
                ),
                yaxis16=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x16'
                ),
                yaxis17=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x17'
                ),
                yaxis18=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x18'
                ),
                yaxis19=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x19'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x2'
                ),
                yaxis20=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x20'
                ),
                yaxis21=YAxis(
                    domain=[0.5375, 0.73125],
                    anchor='x21'
                ),
                yaxis22=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x22'
                ),
                yaxis23=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x23'
                ),
                yaxis24=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x24'
                ),
                yaxis25=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x25'
                ),
                yaxis26=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x26'
                ),
                yaxis27=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x27'
                ),
                yaxis28=YAxis(
                    domain=[0.80625, 1.0],
                    anchor='x28'
                ),
                yaxis3=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x4'
                ),
                yaxis5=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x5'
                ),
                yaxis6=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x6'
                ),
                yaxis7=YAxis(
                    domain=[0.0, 0.19375],
                    anchor='x7'
                ),
                yaxis8=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x8'
                ),
                yaxis9=YAxis(
                    domain=[0.26875, 0.4625],
                    anchor='x9'
                )
            )
        )
        fig = tls.make_subplots(rows=4, cols=7, start_cell='bottom-left')
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_spacing(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.3],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.35, 0.6499999999999999],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.7, 1.0],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.0, 0.3],
                    anchor='y4'
                ),
                xaxis5=XAxis(
                    domain=[0.35, 0.6499999999999999],
                    anchor='y5'
                ),
                xaxis6=XAxis(
                    domain=[0.7, 1.0],
                    anchor='y6'
                ),
                yaxis1=YAxis(
                    domain=[0.55, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.55, 1.0],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.55, 1.0],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.0, 0.45],
                    anchor='x4'
                ),
                yaxis5=YAxis(
                    domain=[0.0, 0.45],
                    anchor='x5'
                ),
                yaxis6=YAxis(
                    domain=[0.0, 0.45],
                    anchor='x6'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=3,
                                horizontal_spacing=.05,
                                vertical_spacing=.1)
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y4'
                ),
                yaxis1=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x4'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=3,
                                specs=[[{}, None, None],
                                       [{}, {}, {}]])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y4'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x4'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=3,
                                specs=[[{}, None, None],
                                       [{}, {}, {}]],
                                start_cell='bottom-left')
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_colspan(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y4'
                ),
                xaxis5=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y5'
                ),
                yaxis1=YAxis(
                    domain=[0.7333333333333333, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.0, 0.26666666666666666],
                    anchor='x4'
                ),
                yaxis5=YAxis(
                    domain=[0.0, 0.26666666666666666],
                    anchor='x5'
                )
            )
        )
        fig = tls.make_subplots(rows=3, cols=2,
                                specs=[[{'colspan': 2}, None],
                                       [{}, {}],
                                       [{}, {}]])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_rowspan(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y4'
                ),
                xaxis5=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y5'
                ),
                xaxis6=XAxis(
                    domain=[0.35555555555555557, 1.0],
                    anchor='y6'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.7333333333333333, 1.0],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.7333333333333333, 1.0],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333],
                    anchor='x4'
                ),
                yaxis5=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333],
                    anchor='x5'
                ),
                yaxis6=YAxis(
                    domain=[0.0, 0.26666666666666666],
                    anchor='x6'
                )
            )
        )
        fig = tls.make_subplots(rows=3, cols=3,
                                specs=[[{'rowspan': 3}, {}, {}],
                                       [None, {}, {}], [None, {'colspan': 2}, None]])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_rowspan2(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.0, 0.6444444444444445],
                    anchor='y4'
                ),
                xaxis5=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y5'
                ),
                yaxis1=YAxis(
                    domain=[0.7333333333333333, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.7333333333333333, 1.0],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.36666666666666664, 1.0],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333],
                    anchor='x4'
                ),
                yaxis5=YAxis(
                    domain=[0.0, 0.26666666666666666],
                    anchor='x5'
                )
            )
        )
        fig = tls.make_subplots(rows=3, cols=3, specs=[[{}, {}, {'rowspan': 2}],
                                [{'colspan': 2}, None, None],
                                [{'colspan': 3}, None, None]])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_colspan_rowpan(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.6444444444444445],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y4'
                ),
                xaxis5=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y5'
                ),
                xaxis6=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y6'
                ),
                yaxis1=YAxis(
                    domain=[0.36666666666666664, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.7333333333333333, 1.0],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.0, 0.26666666666666666],
                    anchor='x4'
                ),
                yaxis5=YAxis(
                    domain=[0.0, 0.26666666666666666],
                    anchor='x5'
                ),
                yaxis6=YAxis(
                    domain=[0.0, 0.26666666666666666],
                    anchor='x6'
                )
            )
        )
        fig = tls.make_subplots(rows=3, cols=3,
                                specs=[[{'colspan': 2, 'rowspan': 2}, None, {}],
                                       [None, None, {}], [{}, {}, {}]])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_colspan_rowpan_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.6444444444444445],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y4'
                ),
                xaxis5=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y5'
                ),
                xaxis6=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y6'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 0.6333333333333333],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.26666666666666666],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.7333333333333333, 1.0],
                    anchor='x4'
                ),
                yaxis5=YAxis(
                    domain=[0.7333333333333333, 1.0],
                    anchor='x5'
                ),
                yaxis6=YAxis(
                    domain=[0.7333333333333333, 1.0],
                    anchor='x6'
                )
            )
        )
        fig = tls.make_subplots(rows=3, cols=3,
                                specs=[[{'colspan': 2, 'rowspan': 2}, None, {}],
                                       [None, None, {}], [{}, {}, {}]],
                                start_cell='bottom-left')
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_is_3d(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                scene=Scene(
                    domain={'y': [0.575, 1.0], 'x': [0.0, 0.45]}
                ),
                scene2=Scene(
                    domain={'y': [0.0, 0.425], 'x': [0.0, 0.45]}
                ),
                xaxis1=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y2'
                ),
                yaxis1=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x2'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=2, specs=[[{'is_3d': True}, {}],
                                                       [{'is_3d': True}, {}]])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_padding(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.1, 0.5],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.5, 1.0],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.0, 0.5],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.5, 0.9],
                    anchor='y4'
                ),
                yaxis1=YAxis(
                    domain=[0.5, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.7, 1.0],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.0, 0.3],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.0, 0.5],
                    anchor='x4'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=2, horizontal_spacing=0,
                                vertical_spacing=0,
                                specs=[[{'l': 0.1}, {'b': 0.2}],
                                       [{'t': 0.2}, {'r': 0.1}]])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_specs_padding_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.1, 0.5],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.5, 1.0],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.0, 0.5],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.5, 0.9],
                    anchor='y4'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 0.5],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.2, 0.5],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.5, 0.8],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.5, 1.0],
                    anchor='x4'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=2,
                                horizontal_spacing=0, vertical_spacing=0,
                                specs=[[{'l': 0.1}, {'b': 0.2}],
                                       [{'t': 0.2}, {'r': 0.1}]],
                                start_cell='bottom-left')
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_xaxes(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y4'
                ),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y5'
                ),
                xaxis3=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y6'
                ),
                yaxis1=YAxis(
                    domain=[0.575, 1.0],
                    anchor='free',
                    position=0.0
                ),
                yaxis2=YAxis(
                    domain=[0.575, 1.0],
                    anchor='free',
                    position=0.35555555555555557
                ),
                yaxis3=YAxis(
                    domain=[0.575, 1.0],
                    anchor='free',
                    position=0.7111111111111111
                ),
                yaxis4=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x'
                ),
                yaxis5=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x2'
                ),
                yaxis6=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x3'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=3, shared_xaxes=True)
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_xaxes_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y3'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.575, 1.0],
                    anchor='free',
                    position=0.0
                ),
                yaxis5=YAxis(
                    domain=[0.575, 1.0],
                    anchor='free',
                    position=0.35555555555555557
                ),
                yaxis6=YAxis(
                    domain=[0.575, 1.0],
                    anchor='free',
                    position=0.7111111111111111
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=3,
                                shared_xaxes=True, start_cell='bottom-left')
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_yaxes(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y'
                ),
                xaxis10=XAxis(
                    domain=[0.55, 1.0],
                    anchor='free',
                    position=0.0
                ),
                xaxis2=XAxis(
                    domain=[0.55, 1.0],
                    anchor='free',
                    position=0.848
                ),
                xaxis3=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y2'
                ),
                xaxis4=XAxis(
                    domain=[0.55, 1.0],
                    anchor='free',
                    position=0.6359999999999999
                ),
                xaxis5=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y3'
                ),
                xaxis6=XAxis(
                    domain=[0.55, 1.0],
                    anchor='free',
                    position=0.424
                ),
                xaxis7=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y4'
                ),
                xaxis8=XAxis(
                    domain=[0.55, 1.0],
                    anchor='free',
                    position=0.212
                ),
                xaxis9=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y5'
                ),
                yaxis1=YAxis(
                    domain=[0.848, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.6359999999999999, 0.7879999999999999],
                    anchor='x3'
                ),
                yaxis3=YAxis(
                    domain=[0.424, 0.576],
                    anchor='x5'
                ),
                yaxis4=YAxis(
                    domain=[0.212, 0.364],
                    anchor='x7'
                ),
                yaxis5=YAxis(
                    domain=[0.0, 0.152],
                    anchor='x9'
                )
            )
        )
        fig = tls.make_subplots(rows=5, cols=2, shared_yaxes=True)
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_xaxes_yaxes(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y3'
                ),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='free',
                    position=0.0
                ),
                xaxis3=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='free',
                    position=0.0
                ),
                yaxis1=YAxis(
                    domain=[0.7333333333333333, 1.0],
                    anchor='free',
                    position=0.0
                ),
                yaxis2=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333],
                    anchor='free',
                    position=0.0
                ),
                yaxis3=YAxis(
                    domain=[0.0, 0.26666666666666666],
                    anchor='x'
                )
            )
        )
        fig = tls.make_subplots(rows=3, cols=3,
                                shared_xaxes=True, shared_yaxes=True)
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_xaxes_yaxes_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='free',
                    position=0.0
                ),
                xaxis3=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='free',
                    position=0.0
                ),
                yaxis1=YAxis(
                    domain=[0.0, 0.26666666666666666],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.36666666666666664, 0.6333333333333333],
                    anchor='free',
                    position=0.0
                ),
                yaxis3=YAxis(
                    domain=[0.7333333333333333, 1.0],
                    anchor='free',
                    position=0.0
                )
            )
        )
        fig = tls.make_subplots(rows=3, cols=3,
                                shared_xaxes=True, shared_yaxes=True,
                                start_cell='bottom-left')
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_axes_list(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.55, 1.0],
                    anchor='free',
                    position=0.575
                ),
                xaxis3=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y3'
                ),
                yaxis1=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.425],
                    anchor='free',
                    position=0.0
                ),
                yaxis3=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x3'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=2, shared_xaxes=[(1, 1), (2, 1)],
                                shared_yaxes=[(1, 1), (1, 2)])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_axes_list_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.55, 1.0],
                    anchor='free',
                    position=0.0
                ),
                xaxis3=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y3'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.575, 1.0],
                    anchor='free',
                    position=0.0
                ),
                yaxis3=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x3'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=2, shared_xaxes=[(1, 1), (2, 1)],
                                shared_yaxes=[(1, 1), (1, 2)],
                                start_cell='bottom-left')
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_axes_list_of_lists(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y5'
                ),
                yaxis1=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.0, 0.425],
                    anchor='free',
                    position=0.0
                ),
                yaxis5=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x4'
                ),
                yaxis6=YAxis(
                    domain=[0.0, 0.425],
                    anchor='free',
                    position=0.7111111111111111
                )
            )
        )
        fig = tls.make_subplots(
            rows=2, cols=3, shared_xaxes=[[(1, 1), (2, 1)], [(1, 3), (2, 3)]]
        )
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_shared_axes_list_of_lists_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y5'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.575, 1.0],
                    anchor='free',
                    position=0.0
                ),
                yaxis5=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x4'
                ),
                yaxis6=YAxis(
                    domain=[0.575, 1.0],
                    anchor='free',
                    position=0.7111111111111111
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=3, shared_xaxes=[[(1, 1), (2, 1)],
                                                              [(1, 3), (2, 3)]],
                                start_cell='bottom-left')
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_insets(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y4'
                ),
                xaxis5=XAxis(
                    domain=[0.865, 0.955],
                    anchor='y5'
                ),
                yaxis1=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x4'
                ),
                yaxis5=YAxis(
                    domain=[0.085, 0.2975],
                    anchor='x5'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=2,
                                insets=[{'cell': (2, 2), 'l': 0.7, 'w': 0.2,
                                         'b': 0.2, 'h': 0.5}])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_insets_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y4'
                ),
                xaxis5=XAxis(
                    domain=[0.865, 0.955],
                    anchor='y5'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x4'
                ),
                yaxis5=YAxis(
                    domain=[0.6599999999999999, 0.8724999999999999],
                    anchor='x5'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=2,
                                insets=[{'cell': (2, 2), 'l': 0.7, 'w': 0.2,
                                         'b': 0.2, 'h': 0.5}],
                                start_cell='bottom-left')
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_insets_multiple(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.8, 1.0],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.8, 1.0],
                    anchor='y4'
                ),
                yaxis1=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x4'
                )
            )
        )
        fig = tls.make_subplots(rows=2, insets=[{'cell': (1, 1), 'l': 0.8},
                                                {'cell': (2, 1), 'l': 0.8}])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_insets_multiple_bottom_left(self):
        expected = Figure(
            data=Data(),
            layout=Layout(
                xaxis1=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.8, 1.0],
                    anchor='y3'
                ),
                xaxis4=XAxis(
                    domain=[0.8, 1.0],
                    anchor='y4'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.0, 0.425],
                    anchor='x3'
                ),
                yaxis4=YAxis(
                    domain=[0.575, 1.0],
                    anchor='x4'
                )
            )
        )
        fig = tls.make_subplots(rows=2,
                                insets=[{'cell': (1, 1), 'l': 0.8},
                                        {'cell': (2, 1), 'l': 0.8}],
                                start_cell='bottom-left')
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_2x1(self):
        # make a title for each subplot when the layout is 2 rows and 1 column
        expected = Figure(
            data=Data(),
            layout=Layout(
                annotations=Annotations([
                    Annotation(
                        x=0.5,
                        y=1.0,
                        xref='paper',
                        yref='paper',
                        text='Title 1',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    ),
                    Annotation(
                        x=0.5,
                        y=0.375,
                        xref='paper',
                        yref='paper',
                        text='Title 2',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    )
                ]),
                xaxis1=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y2'
                ),
                yaxis1=YAxis(
                    domain=[0.625, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.375],
                    anchor='x2'
                )
            )
        )
        fig = tls.make_subplots(rows=2, subplot_titles=('Title 1', 'Title 2'))
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_1x3(self):
        # make a title for each subplot when the layout is 1 row and 3 columns
        expected = Figure(
            data=Data(),
            layout=Layout(
                annotations=Annotations([
                    Annotation(
                        x=0.14444444444444446,
                        y=1.0,
                        xref='paper',
                        yref='paper',
                        text='Title 1',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    ),
                    Annotation(
                        x=0.5,
                        y=1.0,
                        xref='paper',
                        yref='paper',
                        text='Title 2',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    ),
                    Annotation(
                        x=0.8555555555555556,
                        y=1.0,
                        xref='paper',
                        yref='paper',
                        text='Title 3',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    )
                ]),
                xaxis1=XAxis(
                    domain=[0.0, 0.2888888888888889],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.35555555555555557, 0.6444444444444445],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.7111111111111111, 1.0],
                    anchor='y3'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.0, 1.0],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.0, 1.0],
                    anchor='x3'
                )
            )
        )
        fig = tls.make_subplots(cols=3,
                                subplot_titles=('Title 1', 'Title 2', 'Title 3'))
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_shared_axes(self):
        # make a title for each subplot when the layout is 1 row and 3 columns
        expected = Figure(
            data=Data(),
            layout=Layout(
                annotations=Annotations([
                    Annotation(
                        x=0.225,
                        y=1.0,
                        xref='paper',
                        yref='paper',
                        text='Title 1',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    ),
                    Annotation(
                        x=0.775,
                        y=1.0,
                        xref='paper',
                        yref='paper',
                        text='Title 2',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    ),
                    Annotation(
                        x=0.225,
                        y=0.375,
                        xref='paper',
                        yref='paper',
                        text='Title 3',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    ),
                    Annotation(
                        x=0.775,
                        y=0.375,
                        xref='paper',
                        yref='paper',
                        text='Title 4',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    )
                ]),
                xaxis1=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y2'
                ),
                xaxis2=XAxis(
                    domain=[0.55, 1.0],
                    anchor='free',
                    position=0.0
                ),
                yaxis1=YAxis(
                    domain=[0.625, 1.0],
                    anchor='free',
                    position=0.0
                ),
                yaxis2=YAxis(
                    domain=[0.0, 0.375],
                    anchor='x'
                )
            )
        )

        fig = tls.make_subplots(rows=2, cols=2,
                                subplot_titles=('Title 1', 'Title 2',
                                                'Title 3', 'Title 4'),
                                shared_xaxes=True, shared_yaxes=True)
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_irregular_layout(self):
        # make a title for each subplot when the layout is irregular:
        expected = Figure(
            data=Data(),
            layout=Layout(
                annotations=Annotations([
                    Annotation(
                        x=0.225,
                        y=1.0,
                        xref='paper',
                        yref='paper',
                        text='Title 1',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    ),
                    Annotation(
                        x=0.775,
                        y=1.0,
                        xref='paper',
                        yref='paper',
                        text='Title 2',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    ),
                    Annotation(
                        x=0.5,
                        y=0.375,
                        xref='paper',
                        yref='paper',
                        text='Title 3',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    )
                ]),
                xaxis1=XAxis(
                    domain=[0.0, 0.45],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.55, 1.0],
                    anchor='y2'
                ),
                xaxis3=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y3'
                ),
                yaxis1=YAxis(
                    domain=[0.625, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.625, 1.0],
                    anchor='x2'
                ),
                yaxis3=YAxis(
                    domain=[0.0, 0.375],
                    anchor='x3'
                )
            )
        )
        fig = tls.make_subplots(rows=2, cols=2,
                                subplot_titles=('Title 1', 'Title 2', 'Title 3'),
                                specs=[[{}, {}], [{'colspan': 2}, None]])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_subplot_titles_insets(self):
        # This should make a title for the inset plot
        # and no title for the main plot.
        expected = Figure(
            data=Data(),
            layout=Layout(
                annotations=Annotations([
                    Annotation(
                        x=0.85,
                        y=1.0,
                        xref='paper',
                        yref='paper',
                        text='Inset',
                        showarrow=False,
                        font=Font(size=16),
                        xanchor='center',
                        yanchor='bottom'
                    )
                ]),
                xaxis1=XAxis(
                    domain=[0.0, 1.0],
                    anchor='y'
                ),
                xaxis2=XAxis(
                    domain=[0.7, 1.0],
                    anchor='y2'
                ),
                yaxis1=YAxis(
                    domain=[0.0, 1.0],
                    anchor='x'
                ),
                yaxis2=YAxis(
                    domain=[0.3, 1.0],
                    anchor='x2'
                )
            )
        )
        fig = tls.make_subplots(insets=[{'cell': (1, 1), 'l': 0.7, 'b': 0.3}],
                                subplot_titles=("", 'Inset'))
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
        fig = tls.make_subplots(100, 1,
                                vertical_spacing=v_space,
                                specs=[[{'is_3d': True}] for _ in range(100)])

    def test_row_width_and_column_width(self):

        expected = Figure({
            'data': [],
            'layout': {'annotations': [{'font': {'size': 16},
                                        'showarrow': False,
                                        'text': 'Title 1',
                                        'x': 0.405,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 1.0,
                                        'yanchor': 'bottom',
                                        'yref': 'paper'},
                                       {'font': {'size': 16},
                                        'showarrow': False,
                                        'text': 'Title 2',
                                        'x': 0.9550000000000001,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 1.0,
                                        'yanchor': 'bottom',
                                        'yref': 'paper'},
                                       {'font': {'size': 16},
                                        'showarrow': False,
                                        'text': 'Title 3',
                                        'x': 0.405,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 0.1875,
                                        'yanchor': 'bottom',
                                        'yref': 'paper'},
                                       {'font': {'size': 16},
                                        'showarrow': False,
                                        'text': 'Title 4',
                                        'x': 0.9550000000000001,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 0.1875,
                                        'yanchor': 'bottom',
                                        'yref': 'paper'}],
                       'xaxis': {'anchor': 'y', 'domain': [0.0, 0.81]},
                       'xaxis2': {'anchor': 'y2', 'domain': [0.91, 1.0]},
                       'xaxis3': {'anchor': 'y3', 'domain': [0.0, 0.81]},
                       'xaxis4': {'anchor': 'y4', 'domain': [0.91, 1.0]},
                       'yaxis': {'anchor': 'x', 'domain': [0.4375, 1.0]},
                       'yaxis2': {'anchor': 'x2', 'domain': [0.4375, 1.0]},
                       'yaxis3': {'anchor': 'x3', 'domain': [0.0, 0.1875]},
                       'yaxis4': {'anchor': 'x4', 'domain': [0.0, 0.1875]}}
        })
        fig = tls.make_subplots(rows=2, cols=2,
                                subplot_titles=('Title 1', 'Title 2', 'Title 3', 'Title 4'),
                                row_width=[1, 3], column_width=[9, 1])
        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    def test_row_width_and_shared_yaxes(self):

        expected = Figure({
            'data': [],
            'layout': {'annotations': [{'font': {'size': 16},
                                        'showarrow': False,
                                        'text': 'Title 1',
                                        'x': 0.225,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 1.0,
                                        'yanchor': 'bottom',
                                        'yref': 'paper'},
                                       {'font': {'size': 16},
                                        'showarrow': False,
                                        'text': 'Title 2',
                                        'x': 0.775,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 1.0,
                                        'yanchor': 'bottom',
                                        'yref': 'paper'},
                                       {'font': {'size': 16},
                                        'showarrow': False,
                                        'text': 'Title 3',
                                        'x': 0.225,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 0.1875,
                                        'yanchor': 'bottom',
                                        'yref': 'paper'},
                                       {'font': {'size': 16},
                                        'showarrow': False,
                                        'text': 'Title 4',
                                        'x': 0.775,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 0.1875,
                                        'yanchor': 'bottom',
                                        'yref': 'paper'}],
                       'xaxis': {'anchor': 'y', 'domain': [0.0, 0.45]},
                       'xaxis2': {'anchor': 'free', 'domain': [0.55, 1.0], 'position': 0.4375},
                       'xaxis3': {'anchor': 'y2', 'domain': [0.0, 0.45]},
                       'xaxis4': {'anchor': 'free', 'domain': [0.55, 1.0], 'position': 0.0},
                       'yaxis': {'anchor': 'x', 'domain': [0.4375, 1.0]},
                       'yaxis2': {'anchor': 'x3', 'domain': [0.0, 0.1875]}}
        })

        fig = tls.make_subplots(rows=2, cols=2, row_width=[1, 3], shared_yaxes=True,
                                subplot_titles=('Title 1', 'Title 2', 'Title 3', 'Title 4'))

        self.assertEqual(fig.to_plotly_json(), expected.to_plotly_json())

    # def test_row_width_and_shared_yaxes(self):