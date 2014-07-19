import plotly
from plotly.graph_objs import *
import plotly.tools as tls

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
    assert tls.get_subplots(4, 7) == expected

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

    assert expected == tls.get_subplots(2, 3, .05, .1)
