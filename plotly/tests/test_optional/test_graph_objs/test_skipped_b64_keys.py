import json
from unittest import TestCase
import numpy as np
from plotly.tests.test_optional.optional_utils import NumpyTestUtilsMixin
import plotly.graph_objs as go


class TestShouldNotUseBase64InUnsupportedKeys(NumpyTestUtilsMixin, TestCase):
    def test_np_geojson(self):
        normal_coordinates = [
            [
                [-87, 35],
                [-87, 30],
                [-85, 30],
                [-85, 35],
            ]
        ]

        numpy_coordinates = np.array(normal_coordinates)

        data = [
            {
                "type": "choropleth",
                "locations": ["AL"],
                "featureidkey": "properties.id",
                "z": np.array([10]),
                "geojson": {
                    "type": "Feature",
                    "properties": {"id": "AL"},
                    "geometry": {"type": "Polygon", "coordinates": numpy_coordinates},
                },
            }
        ]

        fig = go.Figure(data=data)

        assert (
            json.loads(fig.to_json())["data"][0]["geojson"]["geometry"]["coordinates"]
            == normal_coordinates
        )

    def test_np_layers(self):
        layout = {
            "mapbox": {
                "layers": [
                    {
                        "sourcetype": "geojson",
                        "type": "line",
                        "line": {"dash": np.array([2.5, 1])},
                        "source": {
                            "type": "FeatureCollection",
                            "features": [
                                {
                                    "type": "Feature",
                                    "geometry": {
                                        "type": "LineString",
                                        "coordinates": np.array(
                                            [[0.25, 52], [0.75, 50]]
                                        ),
                                    },
                                }
                            ],
                        },
                    },
                ],
                "center": {"lon": 0.5, "lat": 51},
            },
        }
        data = [{"type": "scattermapbox"}]

        fig = go.Figure(data=data, layout=layout)

        assert (fig.layout["mapbox"]["layers"][0]["line"]["dash"] == (2.5, 1)).all()

        assert json.loads(fig.to_json())["layout"]["mapbox"]["layers"][0]["source"][
            "features"
        ][0]["geometry"]["coordinates"] == [[0.25, 52], [0.75, 50]]

    def test_np_range(self):
        layout = {"xaxis": {"range": np.array([0, 1])}}

        fig = go.Figure(data=[{"type": "scatter"}], layout=layout)

        assert json.loads(fig.to_json())["layout"]["xaxis"]["range"] == [0, 1]
