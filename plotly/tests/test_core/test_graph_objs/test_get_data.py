from __future__ import absolute_import

from unittest import TestCase

from plotly.graph_objs import (Data, Figure, Layout, Line, Margin, Marker,
                               Scatter, XAxis, YAxis)


class TestGetData(TestCase):

    fig = None

    def setUp(self):
        super(TestGetData, self).setUp()
        self.fig = Figure(
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
                    text=['Australia', 'Japan', 'South Korea', 'Malaysia',
                          'China', 'Indonesia', 'Philippines', 'India'],
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
                    text=['Chile', 'Argentina', 'Mexico', 'Venezuela',
                          'Venezuela', 'El Salvador', 'Bolivia'],
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

    def test_get_data(self):
        data = self.fig.get_data()
        comp_data = [
            {
                'name': 'North America',
                'text': ['United States', 'Canada'],
                'x': [52698, 43117],
                'y': [53, 31]
            },
            {
                'name': 'Europe',
                'text': ['Germany', 'Britain', 'France', 'Spain', 'Italy',
                         'Czech Rep.', 'Greece', 'Poland'],
                'x': [39317, 37236, 35650, 30066, 29570, 27159, 23557, 21046,
                      18007],
                'y': [33, 20, 13, 19, 27, 19, 49, 44, 38]
            },
            {
                'name': 'Asia/Pacific',
                'text': ['Australia', 'Japan', 'South Korea', 'Malaysia',
                         'China', 'Indonesia', 'Philippines', 'India'],
                'x': [42952, 37037, 33106, 17478, 9813, 5253, 4692, 3899],
                'y': [23, 42, 54, 89, 14, 99, 93, 70]},
            {
                'name': 'Latin America',
                'text': ['Chile', 'Argentina', 'Mexico', 'Venezuela',
                         'Venezuela', 'El Salvador', 'Bolivia'],
                'x': [19097, 18601, 15595, 13546, 12026, 7434, 5419],
                'y': [43, 47, 56, 80, 86, 93, 80]
            }
        ]
        self.assertEqual(data, comp_data)

    def test_get_data_flatten(self):

        # this is similar to above, except nested objects are flattened

        flat_data = self.fig.get_data(flatten=True)
        comp_data = {
            'Europe.x': [39317, 37236, 35650, 30066, 29570, 27159, 23557,
                         21046, 18007],
            'Europe.y': [33, 20, 13, 19, 27, 19, 49, 44, 38],
            'Asia/Pacific.x': [42952, 37037, 33106, 17478, 9813, 5253, 4692,
                               3899],
            'Latin America.text': ['Chile', 'Argentina', 'Mexico', 'Venezuela',
                                   'Venezuela', 'El Salvador', 'Bolivia'],
            'North America.x': [52698, 43117],
            'Asia/Pacific.y': [23, 42, 54, 89, 14, 99, 93, 70],
            'Asia/Pacific.text': ['Australia', 'Japan', 'South Korea',
                                  'Malaysia', 'China', 'Indonesia',
                                  'Philippines', 'India'],
            'North America.y': [53, 31],
            'North America.text': ['United States', 'Canada'],
            'Europe.text': ['Germany', 'Britain', 'France', 'Spain', 'Italy',
                            'Czech Rep.', 'Greece', 'Poland'],
            'Latin America.x': [19097, 18601, 15595, 13546, 12026, 7434, 5419],
            'Latin America.y': [43, 47, 56, 80, 86, 93, 80]
        }
        self.assertEqual(flat_data, comp_data)

    # TODO test for Data, Scatter, etc..

    def test_flatten_repeated_trace_names(self):
        dl = Data([Scatter(name='thesame', x=[1, 2, 3]) for _ in range(3)])
        data = dl.get_data(flatten=True)
        comp_data = {
            'thesame.x': [1, 2, 3],
            'thesame_1.x': [1, 2, 3],
            'thesame_2.x': [1, 2, 3]
        }
        self.assertEqual(data, comp_data)
