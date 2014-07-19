from __future__ import absolute_import

from plotly.graph_objs import *


def test_get_data():
    fig = Figure(
        data=Data([
            Scatter(
                x=[52698, 43117],
                y=[53, 31],
                mode=u'markers',
                name=u'North America',
                text=[u'United States', u'Canada'],
                marker=Marker(
                    color=u'rgb(164, 194, 244)',
                    size=12,
                    line=Line(
                        color=u'white',
                        width=0.5
                    )
                )
            ),
            Scatter(
                x=[39317, 37236, 35650, 30066, 29570, 27159, 23557, 21046, 18007],
                y=[33, 20, 13, 19, 27, 19, 49, 44, 38],
                mode=u'markers',
                name=u'Europe',
                text=[u'Germany', u'Britain', u'France', u'Spain', u'Italy', u'Czech Rep.', u'Greece', u'Poland'],
                marker=Marker(
                    color=u'rgb(255, 217, 102)',
                    size=12,
                    line=Line(
                        color=u'white',
                        width=0.5
                    )
                )
            ),
            Scatter(
                x=[42952, 37037, 33106, 17478, 9813, 5253, 4692, 3899],
                y=[23, 42, 54, 89, 14, 99, 93, 70],
                mode=u'markers',
                name=u'Asia/Pacific',
                text=[u'Australia', u'Japan', u'South Korea', u'Malaysia', u'China', u'Indonesia', u'Philippines', u'India'],
                marker=Marker(
                    color=u'rgb(234, 153, 153)',
                    size=12,
                    line=Line(
                        color=u'white',
                        width=0.5
                    )
                )
            ),
            Scatter(
                x=[19097, 18601, 15595, 13546, 12026, 7434, 5419],
                y=[43, 47, 56, 80, 86, 93, 80],
                mode=u'markers',
                name=u'Latin America',
                text=[u'Chile', u'Argentina', u'Mexico', u'Venezuela', u'Venezuela', u'El Salvador', u'Bolivia'],
                marker=Marker(
                    color=u'rgb(142, 124, 195)',
                    size=12,
                    line=Line(
                        color=u'white',
                        width=0.5
                    )
                )
            )
        ]),
        layout=Layout(
            title=u'Quarter 1 Growth',
            autosize=False,
            width=500,
            height=500,
            xaxis=XAxis(
                title=u'GDP per Capita',
                showgrid=False,
                zeroline=False
            ),
            yaxis=YAxis(
                title=u'Percent',
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
    data = fig.get_data()
    comp_data = [{'name': u'North America',
      'text': [u'United States', u'Canada'],
      'x': [52698, 43117],
      'y': [53, 31]},
     {'name': u'Europe',
      'text': [u'Germany',
       u'Britain',
       u'France',
       u'Spain',
       u'Italy',
       u'Czech Rep.',
       u'Greece',
       u'Poland'],
      'x': [39317, 37236, 35650, 30066, 29570, 27159, 23557, 21046, 18007],
      'y': [33, 20, 13, 19, 27, 19, 49, 44, 38]},
     {'name': u'Asia/Pacific',
      'text': [u'Australia',
       u'Japan',
       u'South Korea',
       u'Malaysia',
       u'China',
       u'Indonesia',
       u'Philippines',
       u'India'],
      'x': [42952, 37037, 33106, 17478, 9813, 5253, 4692, 3899],
      'y': [23, 42, 54, 89, 14, 99, 93, 70]},
     {'name': u'Latin America',
      'text': [u'Chile',
       u'Argentina',
       u'Mexico',
       u'Venezuela',
       u'Venezuela',
       u'El Salvador',
       u'Bolivia'],
      'x': [19097, 18601, 15595, 13546, 12026, 7434, 5419],
      'y': [43, 47, 56, 80, 86, 93, 80]}]
    assert data == comp_data
