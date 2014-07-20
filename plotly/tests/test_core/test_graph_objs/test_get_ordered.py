from __future__ import absolute_import

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from plotly.graph_objs import *

def test_get_ordered():
    fig = Figure(
        data=Data([
            Scatter(
                x=[52698, 43117],
                y=[53, 31],
                mode='markers',
                name='North America',
                text=['United States', 'Canada'],
                marker=Marker(
                    color='rgb(164, 194, 244)',
                    size=12,
                    line=Line(
                        color='white',
                        width=0.5
                    )
                )
            ),
            Scatter(
                x=[39317, 37236, 35650, 30066, 29570, 27159, 23557, 21046, 18007],
                y=[33, 20, 13, 19, 27, 19, 49, 44, 38],
                mode='markers',
                name='Europe',
                text=['Germany', 'Britain', 'France', 'Spain', 'Italy', 'Czech Rep.', 'Greece', 'Poland'],
                marker=Marker(
                    color='rgb(255, 217, 102)',
                    size=12,
                    line=Line(
                        color='white',
                        width=0.5
                    )
                )
            ),
            Scatter(
                x=[42952, 37037, 33106, 17478, 9813, 5253, 4692, 3899],
                y=[23, 42, 54, 89, 14, 99, 93, 70],
                mode='markers',
                name='Asia/Pacific',
                text=['Australia', 'Japan', 'South Korea', 'Malaysia', 'China', 'Indonesia', 'Philippines', 'India'],
                marker=Marker(
                    color='rgb(234, 153, 153)',
                    size=12,
                    line=Line(
                        color='white',
                        width=0.5
                    )
                )
            ),
            Scatter(
                x=[19097, 18601, 15595, 13546, 12026, 7434, 5419],
                y=[43, 47, 56, 80, 86, 93, 80],
                mode='markers',
                name='Latin America',
                text=['Chile', 'Argentina', 'Mexico', 'Venezuela', 'Venezuela', 'El Salvador', 'Bolivia'],
                marker=Marker(
                    color='rgb(142, 124, 195)',
                    size=12,
                    line=Line(
                        color='white',
                        width=0.5
                    )
                )
            )
        ]),
        layout=Layout(
            title='Quarter 1 Growth',
            autosize=False,
            width=500,
            height=500,
            xaxis=XAxis(
                title='GDP per Capita',
                showgrid=False,
                zeroline=False
            ),
            yaxis=YAxis(
                title='Percent',
                showline=False
            ),
            margin=Margin(
                l=65,
                r=50,
                b=65,
                t=90
            )
        )
    )
    ordered_fig = fig.get_ordered()
    comp_fig = OrderedDict([('data', [OrderedDict([('x', [52698, 43117]), ('y', [53, 31]), ('mode', 'markers'), ('name', 'North America'), ('text', ['United States', 'Canada']), ('marker', OrderedDict([('color', 'rgb(164, 194, 244)'), ('size', 12), ('line', OrderedDict([('color', 'white'), ('width', 0.5)]))])), ('type', 'scatter')]), OrderedDict([('x', [39317, 37236, 35650, 30066, 29570, 27159, 23557, 21046, 18007]), ('y', [33, 20, 13, 19, 27, 19, 49, 44, 38]), ('mode', 'markers'), ('name', 'Europe'), ('text', ['Germany', 'Britain', 'France', 'Spain', 'Italy', 'Czech Rep.', 'Greece', 'Poland']), ('marker', OrderedDict([('color', 'rgb(255, 217, 102)'), ('size', 12), ('line', OrderedDict([('color', 'white'), ('width', 0.5)]))])), ('type', 'scatter')]), OrderedDict([('x', [42952, 37037, 33106, 17478, 9813, 5253, 4692, 3899]), ('y', [23, 42, 54, 89, 14, 99, 93, 70]), ('mode', 'markers'), ('name', 'Asia/Pacific'), ('text', ['Australia', 'Japan', 'South Korea', 'Malaysia', 'China', 'Indonesia', 'Philippines', 'India']), ('marker', OrderedDict([('color', 'rgb(234, 153, 153)'), ('size', 12), ('line', OrderedDict([('color', 'white'), ('width', 0.5)]))])), ('type', 'scatter')]), OrderedDict([('x', [19097, 18601, 15595, 13546, 12026, 7434, 5419]), ('y', [43, 47, 56, 80, 86, 93, 80]), ('mode', 'markers'), ('name', 'Latin America'), ('text', ['Chile', 'Argentina', 'Mexico', 'Venezuela', 'Venezuela', 'El Salvador', 'Bolivia']), ('marker', OrderedDict([('color', 'rgb(142, 124, 195)'), ('size', 12), ('line', OrderedDict([('color', 'white'), ('width', 0.5)]))])), ('type', 'scatter')])]), ('layout', OrderedDict([('title', 'Quarter 1 Growth'), ('autosize', False), ('width', 500), ('height', 500), ('xaxis', OrderedDict([('title', 'GDP per Capita'), ('showgrid', False), ('zeroline', False)])), ('yaxis', OrderedDict([('title', 'Percent'), ('showline', False)])), ('margin', OrderedDict([('l', 65), ('r', 50), ('b', 65), ('t', 90)]))]))])
    assert ordered_fig == comp_fig
