from nose.tools import raises
from nose import with_setup
from nose.plugins.attrib import attr

from datetime import datetime as dt
import numpy as np
import json
import pandas as pd

from plotly import utils
from plotly.grid_objs import Column
from plotly.graph_objs import Scatter, Scatter3d, Figure, Data

## JSON encoding
numeric_list = [1, 2, 3]
np_list = np.array([1, 2, 3])
mixed_list = [1, 'A', dt(2014, 1, 5)]
pd = pd.DataFrame(columns=['col 1'], data=[1, 2, 3])


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
    s1 = Scatter3d(x=numeric_list, y=np_list, z=mixed_list)
    s2 = Scatter(x=pd['col 1'])
    data = Data([s1, s2])
    figure = Figure(data=data)

    js1 = json.dumps(s1, cls=utils._plotlyJSONEncoder)
    js2 = json.dumps(s2, cls=utils._plotlyJSONEncoder)
    assert(js1 == '{"y": [1, 2, 3], "x": [1, 2, 3], "z": '
                  '[1, "A", "2014-01-05"], "type": "scatter3d"}')
    assert(js2 == '{"x": [1, 2, 3], "type": "scatter"}')
    json.dumps(data, cls=utils._plotlyJSONEncoder)
    json.dumps(figure, cls=utils._plotlyJSONEncoder)
