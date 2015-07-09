from __future__ import absolute_import

from nose.tools import raises

from plotly.graph_objs import (Annotation, Annotations, Data, Figure, Font,
                               Layout, Scene, XAxis, YAxis)
import plotly.tools as tls


@raises(Exception)
def test_non_integer_rows():
    tls.make_subplots(rows=2.1)


@raises(Exception)
def test_less_than_zero_rows():
    tls.make_subplots(rows=-2)


@raises(Exception)
def test_non_integer_cols():
    tls.make_subplots(cols=2/3)


@raises(Exception)
def test_less_than_zero_cols():
    tls.make_subplots(cols=-10)


@raises(Exception)
def test_wrong_kwarg():
    tls.make_subplots(stuff='no gonna work')


@raises(Exception)
def test_non_integer_rows():
    tls.make_subplots(rows=2.1)


@raises(Exception)
def test_non_integer_cols():
    tls.make_subplots(cols=2/3)


@raises(Exception)
def test_wrong_kwarg():
    tls.make_subplots(stuff='no gonna work')


@raises(Exception)
def test_start_cell_wrong_values():
    tls.make_subplots(rows=2, cols=2, start_cell='not gonna work')


@raises(Exception)
def test_specs_wrong_type():
    tls.make_subplots(specs="not going to work")


@raises(Exception)
def test_specs_wrong_inner_type():
    tls.make_subplots(specs=[{}])


@raises(Exception)
def test_specs_wrong_item_type():
    tls.make_subplots(specs=[[('not', 'going to work')]])


@raises(Exception)
def test_specs_wrong_item_key():
    tls.make_subplots(specs=[{'not': "going to work"}])


@raises(Exception)
def test_specs_underspecified():
    tls.make_subplots(rows=2, specs=[{}])
    tls.make_subplots(rows=2, cols=2, specs=[[{}, {}], [{}]])


@raises(Exception)
def test_specs_overspecified():
    tls.make_subplots(rows=2, specs=[[{}], [{}], [{}]])
    tls.make_subplots(cols=2, specs=[{}, {}, {}])


@raises(Exception)
def test_specs_colspan_too_big():
    tls.make_subplots(cols=3, specs=[[{}, None, {'colspan': 2}]])


@raises(Exception)
def test_specs_rowspan_too_big():
    tls.make_subplots(rows=3, specs=[[{}], [None], [{'rowspan': 2}]])


@raises(Exception)
def test_insets_wrong_type():
    tls.make_subplots(insets="not going to work")


@raises(Exception)
def test_insets_wrong_item():
    tls.make_subplots(insets=[{'not': "going to work"}])


@raises(Exception)
def test_insets_wrong_cell_row():
    tls.make_subplots(insets=([{'cell': (0, 1)}]))


@raises(Exception)
def test_insets_wrong_cell_col():
    tls.make_subplots(insets=([{'cell': (1, 0)}]))


def test_single_plot():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 1.0],
                anchor='y1'
            ),
            yaxis1=YAxis(
                domain=[0.0, 1.0],
                anchor='x1'
            )
        )
    )
    assert tls.make_subplots() == expected


def test_two_row():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 1.0],
                anchor='y1'
            ),
            xaxis2=XAxis(
                domain=[0.0, 1.0],
                anchor='y2'
            ),
            yaxis1=YAxis(
                domain=[0.575, 1.0],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.0, 0.425],
                anchor='x2'
            )
        )
    )
    assert tls.make_subplots(rows=2) == expected


def test_two_row_bottom_left():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 1.0],
                anchor='y1'
            ),
            xaxis2=XAxis(
                domain=[0.0, 1.0],
                anchor='y2'
            ),
            yaxis1=YAxis(
                domain=[0.0, 0.425],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.575, 1.0],
                anchor='x2'
            )
        )
    )

    fig = tls.make_subplots(rows=2, start_cell='bottom-left')
    assert fig == expected


def test_two_column():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.45],
                anchor='y1'
            ),
            xaxis2=XAxis(
                domain=[0.55, 1.0],
                anchor='y2'
            ),
            yaxis1=YAxis(
                domain=[0.0, 1.0],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.0, 1.0],
                anchor='x2'
            )
        )
    )
    assert tls.make_subplots(cols=2) == expected


def test_a_lot():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.1183673469387755],
                anchor='y1'
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
                domain=[0.7346938775510203, 0.8530612244897958],
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
                domain=[0.7346938775510203, 0.8530612244897958],
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
                domain=[0.7346938775510203, 0.8530612244897958],
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
                domain=[0.7346938775510203, 0.8530612244897958],
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
                domain=[0.8062499999999999, 0.9999999999999999],
                anchor='x1'
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
                domain=[0.8062499999999999, 0.9999999999999999],
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
                domain=[0.8062499999999999, 0.9999999999999999],
                anchor='x3'
            ),
            yaxis4=YAxis(
                domain=[0.8062499999999999, 0.9999999999999999],
                anchor='x4'
            ),
            yaxis5=YAxis(
                domain=[0.8062499999999999, 0.9999999999999999],
                anchor='x5'
            ),
            yaxis6=YAxis(
                domain=[0.8062499999999999, 0.9999999999999999],
                anchor='x6'
            ),
            yaxis7=YAxis(
                domain=[0.8062499999999999, 0.9999999999999999],
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
    assert fig == expected


def test_a_lot_bottom_left():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.1183673469387755],
                anchor='y1'
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
                domain=[0.7346938775510203, 0.8530612244897958],
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
                domain=[0.7346938775510203, 0.8530612244897958],
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
                domain=[0.7346938775510203, 0.8530612244897958],
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
                domain=[0.7346938775510203, 0.8530612244897958],
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
                anchor='x1'
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
                domain=[0.8062499999999999, 0.9999999999999999],
                anchor='x22'
            ),
            yaxis23=YAxis(
                domain=[0.8062499999999999, 0.9999999999999999],
                anchor='x23'
            ),
            yaxis24=YAxis(
                domain=[0.8062499999999999, 0.9999999999999999],
                anchor='x24'
            ),
            yaxis25=YAxis(
                domain=[0.8062499999999999, 0.9999999999999999],
                anchor='x25'
            ),
            yaxis26=YAxis(
                domain=[0.8062499999999999, 0.9999999999999999],
                anchor='x26'
            ),
            yaxis27=YAxis(
                domain=[0.8062499999999999, 0.9999999999999999],
                anchor='x27'
            ),
            yaxis28=YAxis(
                domain=[0.8062499999999999, 0.9999999999999999],
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
    assert fig == expected


def test_spacing():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.3],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_specs():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.2888888888888889],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_specs_bottom_left():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.2888888888888889],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_specs_colspan():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 1.0],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_specs_rowspan():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.2888888888888889],
                anchor='y1'
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
                anchor='x1'
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

    fig = tls.make_subplots(rows=3, cols=3, specs=[[{'rowspan': 3}, {}, {}],
                            [None, {}, {}], [None, {'colspan': 2}, None]])
    assert fig == expected


def test_specs_rowspan2():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.2888888888888889],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_specs_colspan_rowpan():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.6444444444444445],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_specs_colspan_rowpan_bottom_left():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.6444444444444445],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_specs_is_3d():
    expected = Figure(
        data=Data(),
        layout=Layout(
            scene1=Scene(
                domain={'y': [0.575, 1.0], 'x': [0.0, 0.45]}
            ),
            scene2=Scene(
                domain={'y': [0.0, 0.425], 'x': [0.0, 0.45]}
            ),
            xaxis1=XAxis(
                domain=[0.55, 1.0],
                anchor='y1'
            ),
            xaxis2=XAxis(
                domain=[0.55, 1.0],
                anchor='y2'
            ),
            yaxis1=YAxis(
                domain=[0.575, 1.0],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.0, 0.425],
                anchor='x2'
            )
        )
    )

    fig = tls.make_subplots(rows=2, cols=2, specs=[[{'is_3d': True}, {}],
                                                   [{'is_3d': True}, {}]])
    assert fig == expected


def test_specs_padding():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.1, 0.5],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_specs_padding_bottom_left():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.1, 0.5],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_shared_xaxes():
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
                anchor='x1'
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
    assert fig == expected


def test_shared_xaxes_bottom_left():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.2888888888888889],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_shared_yaxes():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.45],
                anchor='y1'
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
                position=0.636
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
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.636, 0.788],
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
    assert fig == expected


def test_shared_xaxes_yaxes():
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
                anchor='x1'
            )
        )
    )

    fig = tls.make_subplots(rows=3, cols=3,
                            shared_xaxes=True, shared_yaxes=True)
    assert fig == expected


def test_shared_xaxes_yaxes_bottom_left():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.2888888888888889],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_shared_axes_list():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.45],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_shared_axes_list_bottom_left():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.45],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_shared_axes_list_of_lists():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.2888888888888889],
                anchor='y1'
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
                anchor='x1'
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

    fig = tls.make_subplots(rows=2, cols=3, shared_xaxes=[[(1, 1), (2, 1)],
                                                          [(1, 3), (2, 3)]])
    assert fig == expected


def test_shared_axes_list_of_lists_bottom_left():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.2888888888888889],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_insets():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.45],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_insets_bottom_left():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.45],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_insets_multiple():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 1.0],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_insets_multiple_bottom_left():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 1.0],
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_subplot_titles_2x1():
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
                anchor='y1'
            ),
            xaxis2=XAxis(
                domain=[0.0, 1.0],
                anchor='y2'
            ),
            yaxis1=YAxis(
                domain=[0.625, 1.0],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.0, 0.375],
                anchor='x2'
            )
        )
    )
    fig = tls.make_subplots(rows=2, subplot_titles=('Title 1', 'Title 2'))
    assert fig == expected


def test_subplot_titles_1x3():
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
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_subplot_titles_shared_axes():
    # make a title for each subplot when the layout is 1 row and 3 columns
    expected = Figure(
        data=Data(),
        layout=Layout(
            annotations=Annotations([
                Annotation(
                    x=0.22499999999999998,
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
                    x=0.7749999999999999,
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
                    x=0.22499999999999998,
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
                    x=0.7749999999999999,
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
                anchor='x1'
            )
        )
    )
    fig = tls.make_subplots(rows=2, cols=2,
                            subplot_titles=('Title 1', 'Title 2',
                                            'Title 3', 'Title 4'),
                            shared_xaxes=True, shared_yaxes=True)

    assert fig == expected


def test_subplot_titles_irregular_layout():
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
                anchor='y1'
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
                anchor='x1'
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
    assert fig == expected


def test_subplot_titles_insets():
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
                anchor='y1'
            ),
            xaxis2=XAxis(
                domain=[0.7, 1.0],
                anchor='y2'
            ),
            yaxis1=YAxis(
                domain=[0.0, 1.0],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.3, 1.0],
                anchor='x2'
            )
        )
    )
    fig = tls.make_subplots(insets=[{'cell': (1, 1), 'l': 0.7, 'b': 0.3}],
                            subplot_titles=("", 'Inset'))
    assert fig == expected
