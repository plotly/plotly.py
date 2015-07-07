from __future__ import absolute_import

from plotly.graph_objs import (Data, Figure, Layout, Line, Margin, Marker,
                               Scatter, XAxis, YAxis)
from plotly.tests.utils import compare_dict


def test_strip_style():
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
                x=[39317, 37236, 35650, 30066, 29570, 27159, 23557, 21046,
                   18007],
                y=[33, 20, 13, 19, 27, 19, 49, 44, 38],
                mode='markers',
                name='Europe',
                text=['Germany', 'Britain', 'France', 'Spain', 'Italy',
                      'Czech Rep.', 'Greece', 'Poland'],
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
                text=['Australia', 'Japan', 'South Korea', 'Malaysia', 'China',
                      'Indonesia', 'Philippines', 'India'],
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
                text=['Chile', 'Argentina', 'Mexico', 'Venezuela', 'Venezuela',
                      'El Salvador', 'Bolivia'],
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
    print(fig)
    print('\n\n')
    fig.strip_style()
    print(fig)
    print('\n\n')
    comp_fig = Figure(
        data=Data([
            Scatter(
                x=[52698, 43117],
                y=[53, 31],
                mode='markers',
                name='North America',
                text=['United States', 'Canada'],
                marker=Marker(
                    line=Line()
                )
            ),
            Scatter(
                x=[39317, 37236, 35650, 30066, 29570, 27159, 23557, 21046,
                   18007],
                y=[33, 20, 13, 19, 27, 19, 49, 44, 38],
                mode='markers',
                name='Europe',
                text=['Germany', 'Britain', 'France', 'Spain', 'Italy',
                      'Czech Rep.', 'Greece', 'Poland'],
                marker=Marker(
                    line=Line()
                )
            ),
            Scatter(
                x=[42952, 37037, 33106, 17478, 9813, 5253, 4692, 3899],
                y=[23, 42, 54, 89, 14, 99, 93, 70],
                mode='markers',
                name='Asia/Pacific',
                text=['Australia', 'Japan', 'South Korea', 'Malaysia', 'China',
                      'Indonesia', 'Philippines', 'India'],
                marker=Marker(
                    line=Line()
                )
            ),
            Scatter(
                x=[19097, 18601, 15595, 13546, 12026, 7434, 5419],
                y=[43, 47, 56, 80, 86, 93, 80],
                mode='markers',
                name='Latin America',
                text=['Chile', 'Argentina', 'Mexico', 'Venezuela', 'Venezuela',
                      'El Salvador', 'Bolivia'],
                marker=Marker(
                    line=Line()
                )
            )
        ]),
        layout=Layout(
            title='Quarter 1 Growth',
            width=500,
            height=500,
            xaxis=XAxis(
                title='GDP per Capita'
            ),
            yaxis=YAxis(
                title='Percent'
            ),
            margin=Margin(
                l=65,
                r=50,
                b=65,
                t=90
            )
        )
    )
    equivalent, msg = compare_dict(fig, comp_fig)
    print(msg)
    assert equivalent
