import plotly
from plotly.graph_objs import *
import plotly.tools as tls
from nose.tools import raises

def test_get_single_plot():
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
    assert tls.get_subplots() == expected

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
                domain=[0.0, 0.425],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.575, 1.0],
                anchor='x2'
            )
        )
    )
    assert tls.get_subplots(2) == expected


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

    assert tls.get_subplots(1, 2) == expected

def test_a_lot():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.05714285714285713],
                anchor='y1'
            ),
            xaxis10=XAxis(
                domain=[0.3142857142857143, 0.3714285714285714],
                anchor='y10'
            ),
            xaxis11=XAxis(
                domain=[0.4714285714285714, 0.5285714285714286],
                anchor='y11'
            ),
            xaxis12=XAxis(
                domain=[0.6285714285714286, 0.6857142857142857],
                anchor='y12'
            ),
            xaxis13=XAxis(
                domain=[0.7857142857142857, 0.8428571428571429],
                anchor='y13'
            ),
            xaxis14=XAxis(
                domain=[0.9428571428571428, 1.0],
                anchor='y14'
            ),
            xaxis15=XAxis(
                domain=[0.0, 0.05714285714285713],
                anchor='y15'
            ),
            xaxis16=XAxis(
                domain=[0.15714285714285714, 0.21428571428571427],
                anchor='y16'
            ),
            xaxis17=XAxis(
                domain=[0.3142857142857143, 0.3714285714285714],
                anchor='y17'
            ),
            xaxis18=XAxis(
                domain=[0.4714285714285714, 0.5285714285714286],
                anchor='y18'
            ),
            xaxis19=XAxis(
                domain=[0.6285714285714286, 0.6857142857142857],
                anchor='y19'
            ),
            xaxis2=XAxis(
                domain=[0.15714285714285714, 0.21428571428571427],
                anchor='y2'
            ),
            xaxis20=XAxis(
                domain=[0.7857142857142857, 0.8428571428571429],
                anchor='y20'
            ),
            xaxis21=XAxis(
                domain=[0.9428571428571428, 1.0],
                anchor='y21'
            ),
            xaxis22=XAxis(
                domain=[0.0, 0.05714285714285713],
                anchor='y22'
            ),
            xaxis23=XAxis(
                domain=[0.15714285714285714, 0.21428571428571427],
                anchor='y23'
            ),
            xaxis24=XAxis(
                domain=[0.3142857142857143, 0.3714285714285714],
                anchor='y24'
            ),
            xaxis25=XAxis(
                domain=[0.4714285714285714, 0.5285714285714286],
                anchor='y25'
            ),
            xaxis26=XAxis(
                domain=[0.6285714285714286, 0.6857142857142857],
                anchor='y26'
            ),
            xaxis27=XAxis(
                domain=[0.7857142857142857, 0.8428571428571429],
                anchor='y27'
            ),
            xaxis28=XAxis(
                domain=[0.9428571428571428, 1.0],
                anchor='y28'
            ),
            xaxis3=XAxis(
                domain=[0.3142857142857143, 0.3714285714285714],
                anchor='y3'
            ),
            xaxis4=XAxis(
                domain=[0.4714285714285714, 0.5285714285714286],
                anchor='y4'
            ),
            xaxis5=XAxis(
                domain=[0.6285714285714286, 0.6857142857142857],
                anchor='y5'
            ),
            xaxis6=XAxis(
                domain=[0.7857142857142857, 0.8428571428571429],
                anchor='y6'
            ),
            xaxis7=XAxis(
                domain=[0.9428571428571428, 1.0],
                anchor='y7'
            ),
            xaxis8=XAxis(
                domain=[0.0, 0.05714285714285713],
                anchor='y8'
            ),
            xaxis9=XAxis(
                domain=[0.15714285714285714, 0.21428571428571427],
                anchor='y9'
            ),
            yaxis1=YAxis(
                domain=[0.0, 0.1375],
                anchor='x1'
            ),
            yaxis10=YAxis(
                domain=[0.2875, 0.425],
                anchor='x10'
            ),
            yaxis11=YAxis(
                domain=[0.2875, 0.425],
                anchor='x11'
            ),
            yaxis12=YAxis(
                domain=[0.2875, 0.425],
                anchor='x12'
            ),
            yaxis13=YAxis(
                domain=[0.2875, 0.425],
                anchor='x13'
            ),
            yaxis14=YAxis(
                domain=[0.2875, 0.425],
                anchor='x14'
            ),
            yaxis15=YAxis(
                domain=[0.575, 0.7124999999999999],
                anchor='x15'
            ),
            yaxis16=YAxis(
                domain=[0.575, 0.7124999999999999],
                anchor='x16'
            ),
            yaxis17=YAxis(
                domain=[0.575, 0.7124999999999999],
                anchor='x17'
            ),
            yaxis18=YAxis(
                domain=[0.575, 0.7124999999999999],
                anchor='x18'
            ),
            yaxis19=YAxis(
                domain=[0.575, 0.7124999999999999],
                anchor='x19'
            ),
            yaxis2=YAxis(
                domain=[0.0, 0.1375],
                anchor='x2'
            ),
            yaxis20=YAxis(
                domain=[0.575, 0.7124999999999999],
                anchor='x20'
            ),
            yaxis21=YAxis(
                domain=[0.575, 0.7124999999999999],
                anchor='x21'
            ),
            yaxis22=YAxis(
                domain=[0.8624999999999999, 1.0],
                anchor='x22'
            ),
            yaxis23=YAxis(
                domain=[0.8624999999999999, 1.0],
                anchor='x23'
            ),
            yaxis24=YAxis(
                domain=[0.8624999999999999, 1.0],
                anchor='x24'
            ),
            yaxis25=YAxis(
                domain=[0.8624999999999999, 1.0],
                anchor='x25'
            ),
            yaxis26=YAxis(
                domain=[0.8624999999999999, 1.0],
                anchor='x26'
            ),
            yaxis27=YAxis(
                domain=[0.8624999999999999, 1.0],
                anchor='x27'
            ),
            yaxis28=YAxis(
                domain=[0.8624999999999999, 1.0],
                anchor='x28'
            ),
            yaxis3=YAxis(
                domain=[0.0, 0.1375],
                anchor='x3'
            ),
            yaxis4=YAxis(
                domain=[0.0, 0.1375],
                anchor='x4'
            ),
            yaxis5=YAxis(
                domain=[0.0, 0.1375],
                anchor='x5'
            ),
            yaxis6=YAxis(
                domain=[0.0, 0.1375],
                anchor='x6'
            ),
            yaxis7=YAxis(
                domain=[0.0, 0.1375],
                anchor='x7'
            ),
            yaxis8=YAxis(
                domain=[0.2875, 0.425],
                anchor='x8'
            ),
            yaxis9=YAxis(
                domain=[0.2875, 0.425],
                anchor='x9'
            )
        )
    )

    fig = tls.get_subplots(4, 7,
                            horizontal_spacing=0.1,
                            vertical_spacing=0.15)

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
                domain=[0.0, 0.45],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.0, 0.45],
                anchor='x2'
            ),
            yaxis3=YAxis(
                domain=[0.0, 0.45],
                anchor='x3'
            ),
            yaxis4=YAxis(
                domain=[0.55, 1.0],
                anchor='x4'
            ),
            yaxis5=YAxis(
                domain=[0.55, 1.0],
                anchor='x5'
            ),
            yaxis6=YAxis(
                domain=[0.55, 1.0],
                anchor='x6'
            )
        )
    )

    fig = tls.get_subplots(2, 3,
                           horizontal_spacing=.05,
                           vertical_spacing=.1)

    assert fig == expected

@raises(Exception)
def test_non_integer_rows():
   fig = tls.get_subplots(rows=2.1)

@raises(Exception)
def test_non_integer_columns():
   fig = tls.get_subplots(columns=2/3)

@raises(Exception)
def test_wrong_kwarg():
   fig = tls.get_subplots(stuff='no gonna work')

def test_default_spacing():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.16799999999999998],
                anchor='y1'
            ),
            xaxis10=XAxis(
                domain=[0.832, 1.0],
                anchor='y10'
            ),
            xaxis11=XAxis(
                domain=[0.0, 0.16799999999999998],
                anchor='y11'
            ),
            xaxis12=XAxis(
                domain=[0.208, 0.376],
                anchor='y12'
            ),
            xaxis13=XAxis(
                domain=[0.416, 0.584],
                anchor='y13'
            ),
            xaxis14=XAxis(
                domain=[0.624, 0.792],
                anchor='y14'
            ),
            xaxis15=XAxis(
                domain=[0.832, 1.0],
                anchor='y15'
            ),
            xaxis16=XAxis(
                domain=[0.0, 0.16799999999999998],
                anchor='y16'
            ),
            xaxis17=XAxis(
                domain=[0.208, 0.376],
                anchor='y17'
            ),
            xaxis18=XAxis(
                domain=[0.416, 0.584],
                anchor='y18'
            ),
            xaxis19=XAxis(
                domain=[0.624, 0.792],
                anchor='y19'
            ),
            xaxis2=XAxis(
                domain=[0.208, 0.376],
                anchor='y2'
            ),
            xaxis20=XAxis(
                domain=[0.832, 1.0],
                anchor='y20'
            ),
            xaxis21=XAxis(
                domain=[0.0, 0.16799999999999998],
                anchor='y21'
            ),
            xaxis22=XAxis(
                domain=[0.208, 0.376],
                anchor='y22'
            ),
            xaxis23=XAxis(
                domain=[0.416, 0.584],
                anchor='y23'
            ),
            xaxis24=XAxis(
                domain=[0.624, 0.792],
                anchor='y24'
            ),
            xaxis25=XAxis(
                domain=[0.832, 1.0],
                anchor='y25'
            ),
            xaxis26=XAxis(
                domain=[0.0, 0.16799999999999998],
                anchor='y26'
            ),
            xaxis27=XAxis(
                domain=[0.208, 0.376],
                anchor='y27'
            ),
            xaxis28=XAxis(
                domain=[0.416, 0.584],
                anchor='y28'
            ),
            xaxis29=XAxis(
                domain=[0.624, 0.792],
                anchor='y29'
            ),
            xaxis3=XAxis(
                domain=[0.416, 0.584],
                anchor='y3'
            ),
            xaxis30=XAxis(
                domain=[0.832, 1.0],
                anchor='y30'
            ),
            xaxis4=XAxis(
                domain=[0.624, 0.792],
                anchor='y4'
            ),
            xaxis5=XAxis(
                domain=[0.832, 1.0],
                anchor='y5'
            ),
            xaxis6=XAxis(
                domain=[0.0, 0.16799999999999998],
                anchor='y6'
            ),
            xaxis7=XAxis(
                domain=[0.208, 0.376],
                anchor='y7'
            ),
            xaxis8=XAxis(
                domain=[0.416, 0.584],
                anchor='y8'
            ),
            xaxis9=XAxis(
                domain=[0.624, 0.792],
                anchor='y9'
            ),
            yaxis1=YAxis(
                domain=[0.0, 0.125],
                anchor='x1'
            ),
            yaxis10=YAxis(
                domain=[0.175, 0.3],
                anchor='x10'
            ),
            yaxis11=YAxis(
                domain=[0.35, 0.475],
                anchor='x11'
            ),
            yaxis12=YAxis(
                domain=[0.35, 0.475],
                anchor='x12'
            ),
            yaxis13=YAxis(
                domain=[0.35, 0.475],
                anchor='x13'
            ),
            yaxis14=YAxis(
                domain=[0.35, 0.475],
                anchor='x14'
            ),
            yaxis15=YAxis(
                domain=[0.35, 0.475],
                anchor='x15'
            ),
            yaxis16=YAxis(
                domain=[0.5249999999999999, 0.6499999999999999],
                anchor='x16'
            ),
            yaxis17=YAxis(
                domain=[0.5249999999999999, 0.6499999999999999],
                anchor='x17'
            ),
            yaxis18=YAxis(
                domain=[0.5249999999999999, 0.6499999999999999],
                anchor='x18'
            ),
            yaxis19=YAxis(
                domain=[0.5249999999999999, 0.6499999999999999],
                anchor='x19'
            ),
            yaxis2=YAxis(
                domain=[0.0, 0.125],
                anchor='x2'
            ),
            yaxis20=YAxis(
                domain=[0.5249999999999999, 0.6499999999999999],
                anchor='x20'
            ),
            yaxis21=YAxis(
                domain=[0.7, 0.825],
                anchor='x21'
            ),
            yaxis22=YAxis(
                domain=[0.7, 0.825],
                anchor='x22'
            ),
            yaxis23=YAxis(
                domain=[0.7, 0.825],
                anchor='x23'
            ),
            yaxis24=YAxis(
                domain=[0.7, 0.825],
                anchor='x24'
            ),
            yaxis25=YAxis(
                domain=[0.7, 0.825],
                anchor='x25'
            ),
            yaxis26=YAxis(
                domain=[0.875, 1.0],
                anchor='x26'
            ),
            yaxis27=YAxis(
                domain=[0.875, 1.0],
                anchor='x27'
            ),
            yaxis28=YAxis(
                domain=[0.875, 1.0],
                anchor='x28'
            ),
            yaxis29=YAxis(
                domain=[0.875, 1.0],
                anchor='x29'
            ),
            yaxis3=YAxis(
                domain=[0.0, 0.125],
                anchor='x3'
            ),
            yaxis30=YAxis(
                domain=[0.875, 1.0],
                anchor='x30'
            ),
            yaxis4=YAxis(
                domain=[0.0, 0.125],
                anchor='x4'
            ),
            yaxis5=YAxis(
                domain=[0.0, 0.125],
                anchor='x5'
            ),
            yaxis6=YAxis(
                domain=[0.175, 0.3],
                anchor='x6'
            ),
            yaxis7=YAxis(
                domain=[0.175, 0.3],
                anchor='x7'
            ),
            yaxis8=YAxis(
                domain=[0.175, 0.3],
                anchor='x8'
            ),
            yaxis9=YAxis(
                domain=[0.175, 0.3],
                anchor='x9'
            )
        )
    )

    fig = tls.get_subplots(rows=6, columns=5)

    assert fig == expected

@raises(Exception)
def test_subplot_specs_wrong_type():
    fig = tls.get_subplots(specs="not going to work")

@raises(Exception)
def test_subplot_specs_wrong_item():
    fig = tls.get_subplots(specs=[{'not': "going to work"}])

def test_subplot_specs():
    expected =  Figure(
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

    fig = tls.get_subplots(rows=2, columns=3, specs=[[{}], [{}, {}, {}]])

    assert fig == expected

def test_subplot_specs_colspan():
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
                domain=[0.0, 0.26666666666666666],
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
                domain=[0.7333333333333333, 1.0],
                anchor='x4'
            ),
            yaxis5=YAxis(
                domain=[0.7333333333333333, 1.0],
                anchor='x5'
            )
        )
    )

    fig = tls.get_subplots(rows=3, columns=2,
                            specs=[[{'colspan':2}],
                                   [{}, {}],
                                   [{}, {}]])
    assert fig == expected

def test_subplot_specs_rowspan():
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
                domain=[0.0, 0.26666666666666666],
                anchor='x2'
            ),
            yaxis3=YAxis(
                domain=[0.0, 0.26666666666666666],
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
                domain=[0.7333333333333333, 1.0],
                anchor='x6'
            )
        )
    )

    fig = tls.get_subplots(rows=3, columns=3,
            specs=[[{'rowspan': 3}, {}, {}],
                   [{'is_empty': True}, {}, {}],
                   [{'is_empty': True}, {'colspan': 2}]])

    assert fig == expected

def test_subplot_specs_rowspan2():
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
                domain=[0.0, 0.26666666666666666],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.0, 0.26666666666666666],
                anchor='x2'
            ),
            yaxis3=YAxis(
                domain=[0.0, 0.6333333333333333],
                anchor='x3'
            ),
            yaxis4=YAxis(
                domain=[0.36666666666666664, 0.6333333333333333],
                anchor='x4'
            ),
            yaxis5=YAxis(
                domain=[0.7333333333333333, 1.0],
                anchor='x5'
            )
        )
    )

    fig = tls.get_subplots(rows=3, columns=3,
                           specs=[[{}, {}, {'rowspan': 2}],
                                  [{'colspan': 2}],
                                  [{'colspan': 3}]])

    assert fig == expected

def test_subplot_specs_is_3d():
    expected = Figure(
        data=Data(),
        layout=Layout(
            scene1=Scene(
                domain={'y': [0.0, 0.425], 'x': [0.0, 0.45]}
            ),
            scene2=Scene(
                domain={'y': [0.575, 1.0], 'x': [0.0, 0.45]}
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
                domain=[0.0, 0.425],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.575, 1.0],
                anchor='x2'
            )
        )
    )

    fig = tls.get_subplots(rows=2, columns=2,
                           specs=[[{'is_3d': True}, {}],
                                   [{'is_3d': True}, {}]])

    assert fig == expected

def test_subplot_specs_padding():
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

    fig = tls.get_subplots(rows=2, columns=2,
                           horizontal_spacing=0, vertical_spacing=0,
                           specs=[[{'l': 0.1}, {'b': 0.2}],
                                  [{'t': 0.2}, {'r': 0.1}]])

    assert fig == expected

def test_subplot_shared_xaxes():
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
                anchor='free'
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

    fig = tls.get_subplots(rows=2, columns=3, shared_xaxes=True)

    assert fig == expected

def test_subplot_shared_yaxes():
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
                position=0.848
            ),
            xaxis2=XAxis(
                domain=[0.55, 1.0],
                anchor='free'
            ),
            xaxis3=XAxis(
                domain=[0.0, 0.45],
                anchor='y2'
            ),
            xaxis4=XAxis(
                domain=[0.55, 1.0],
                anchor='free',
                position=0.212
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
                position=0.636
            ),
            xaxis9=XAxis(
                domain=[0.0, 0.45],
                anchor='y5'
            ),
            yaxis1=YAxis(
                domain=[0.0, 0.152],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.212, 0.364],
                anchor='x2'
            ),
            yaxis3=YAxis(
                domain=[0.424, 0.576],
                anchor='x3'
            ),
            yaxis4=YAxis(
                domain=[0.636, 0.788],
                anchor='x4'
            ),
            yaxis5=YAxis(
                domain=[0.848, 1.0],
                anchor='x5'
            )
        )
    )

    fig = tls.get_subplots(rows=5, columns=2, shared_yaxes=True)

    assert fig == expected

def test_subplot_shared_xaxes_yaxes():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.2888888888888889],
                anchor='y1'
            ),
            xaxis2=XAxis(
                domain=[0.35555555555555557, 0.6444444444444445],
                anchor='free'
            ),
            xaxis3=XAxis(
                domain=[0.7111111111111111, 1.0],
                anchor='free'
            ),
            yaxis1=YAxis(
                domain=[0.0, 0.26666666666666666],
                anchor='x1'
            ),
            yaxis2=YAxis(
                domain=[0.36666666666666664, 0.6333333333333333],
                anchor='free'
            ),
            yaxis3=YAxis(
                domain=[0.7333333333333333, 1.0],
                anchor='free'
            )
        )
    )
    fig = tls.get_subplots(rows=3, columns=3,
                           shared_xaxes=True, shared_yaxes=True)

    assert fig == expected

def test_subplot_shared_axes_list():
    expected = Figure(
        data=Data(),
        layout=Layout(
            xaxis1=XAxis(
                domain=[0.0, 0.45],
                anchor='y1'
            ),
            xaxis2=XAxis(
                domain=[0.55, 1.0],
                anchor='free'
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
                anchor='free'
            ),
            yaxis3=YAxis(
                domain=[0.575, 1.0],
                anchor='x3'
            )
        )
    )

    fig = tls.get_subplots(rows=2, columns=2,
                           shared_xaxes=[(0,0), (1,0)],
                           shared_yaxes=[(0,0), (0,1)])

    assert fig == expected


def test_subplot_shared_axes_list_of_lists():
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
                anchor='free'
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

    fig = tls.get_subplots(rows=2, columns=3,
                           shared_xaxes=[[(0,0), (1,0)],
                                         [(0,2), (1,2)]])

    assert fig == expected

@raises(Exception)
def test_subplot_insets_wrong_type():
    fig = tls.get_subplots(insets="not going to work")

@raises(Exception)
def test_subplot_insets_wrong_item():
    fig = tls.get_subplots(insets=[{'not': "going to work"}])

def test_subplot_insets():
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

    fig = tls.get_subplots(rows=2, columns=2,
                           insets=[{'cell': (1,1),
                                    'l': 0.7, 'w': 0.2,
                                    'b': 0.2, 'h': 0.5}])

    assert fig == expected

def test_subplot_insets_multiple():
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

    fig = tls.get_subplots(rows=2,
                           insets=[{'cell': (0,0), 'l':0.8},
                                   {'cell': (1,0), 'l':0.8}])
