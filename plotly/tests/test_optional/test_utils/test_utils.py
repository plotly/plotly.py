from nose.tools import raises
from nose import with_setup
from nose.plugins.attrib import attr

from datetime import datetime as dt
import numpy as np
import json

from plotly import utils
from plotly.grid_objs import Column
from plotly.graph_objs import Scatter3d, Figure, Data

## JSON encoding
numeric_list = [1, 2, 3]
np_list = np.array([1, 2, 3])
mixed_list = [1, 'A', dt(2014, 1, 5)]


def test_column_json_encoding():
    columns = [
        Column(numeric_list, 'col 1'),
        Column(mixed_list, 'col 2'),
        Column(np_list, 'col 3')
    ]
    json_columns = json.dumps(columns, cls=utils._plotlyJSONEncoder)
    assert('[{"data": [1, 2, 3], "name": "col 1"}, '
           '{"data": [1, "A", "2014-01-05"], "name": "col 2"}, '
           '{"data": [1, 2, 3], "name": "col 3"}]' == json_columns)


def test_figure_json_encoding():
    s = Scatter3d(x=numeric_list, y=np_list, z=mixed_list)
    data = Data([s])
    figure = Figure(data=data)

    json.dumps(s, cls=utils._plotlyJSONEncoder)
    json.dumps(data, cls=utils._plotlyJSONEncoder)
    json.dumps(figure, cls=utils._plotlyJSONEncoder)
