from unittest import TestCase
import numpy as np
from plotly.tests.test_optional.optional_utils import NumpyTestUtilsMixin
import plotly.graph_objs as go

class TestSkippedBase64Keys(NumpyTestUtilsMixin, TestCase):
    def test_np_geojson(self):
        choropleth_coordinates = np.array([[
            # Use the min / max of both coordinates to make a simple square
            [-87.359296, 35.00118],
            [-87.359296, 30.247195],
            [-85.004212, 30.247195],
            [-85.004212, 35.00118],
        ]])

        data = [{
            "type": "choropleth",
            "name": "choropleth + RAW",
            "locations": ["AL"],
            "featureidkey": "properties.id",
            "z": np.array([10]),
            "showscale": False,
            "geojson": {
                "type": "Feature",
                "properties": {
                    "id": "AL"
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": choropleth_coordinates
                }
            }
        }]

        fig = go.Figure(data=data)
        exp_data = {
            'featureidkey': 'properties.id',
            'geojson': {
                'geometry': {
                    'coordinates': [[
                        [-87.359296, 35.00118],
                        [-87.359296, 30.247195],
                        [-85.004212, 30.247195],
                        [-85.004212, 35.00118],
                    ]],
                    'type': 'Polygon'
                },
                'properties': {
                    'id': 'AL'
                },
                'type': 'Feature'
            },
            'locations': ['AL'],
            'name': 'choropleth + RAW',
            'showscale': False,
            'type': 'choropleth',
            'z': {
                'bdata': 'Cg==',
                'dtype': 'i1'
            }
        }
        fig.show()

        self.assert_fig_equal(fig.data[0], exp_data)