from unittest import TestCase
import numpy as np
from plotly.tests.test_optional.optional_utils import NumpyTestUtilsMixin
import plotly.graph_objs as go
import plotly.io as pio

pio.renderers.default = 'iframe'

class TestSkippedBase64Keys(NumpyTestUtilsMixin, TestCase):
    def test_np_geojson(self):
        normal_coordinates = [[  
            [-87, 35],  
            [-87, 30],  
            [-85, 30],  
            [-85, 35],  
        ]]  

        numpy_coordinates = np.array(normal_coordinates)  

        data = [{  
            "type": "choropleth",  
            "locations": ["AL"],  
            "featureidkey": "properties.id",  
            "z": np.array([10]),  
            "geojson": {  
                "type": "Feature",  
                "properties": {  
                    "id": "AL"  
                },  
                "geometry": {  
                    "type": "Polygon",  
                    "coordinates": numpy_coordinates  
                }  
            }  
        }]  

        fig = go.Figure(data=data)  
        fig.show()  

        assert (fig["data"][0]["geojson"]["geometry"]["coordinates"] == normal_coordinates).all()
