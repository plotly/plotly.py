from nose.tools import raises
from nose import with_setup
from nose.plugins.attrib import attr

from datetime import datetime as dt
import numpy as np
import json
import pandas as pd
from pandas.util.testing import assert_series_equal

from plotly import utils
from plotly.grid_objs import Column
from plotly.graph_objs import Scatter, Scatter3d, Figure, Data

## JSON encoding
numeric_list = [1, 2, 3]
np_list = np.array([1, 2, 3, np.NaN, np.NAN, np.Inf, dt(2014, 1, 5)])
mixed_list = [1, 'A', dt(2014, 1, 5), dt(2014, 1, 5, 1, 1, 1),
              dt(2014, 1, 5, 1, 1, 1, 1)]

df = pd.DataFrame(columns=['col 1'],
                  data=[1, 2, 3, dt(2014, 1, 5), pd.NaT, np.NaN, np.Inf])

rng = pd.date_range('1/1/2011', periods=2, freq='H')
ts = pd.Series([1.5, 2.5], index=rng)


def test_column_json_encoding():
    columns = [
        Column(numeric_list, 'col 1'),
        Column(mixed_list, 'col 2'),
        Column(np_list, 'col 3')
    ]
    json_columns = json.dumps(
        columns, cls=utils._plotlyJSONEncoder, sort_keys=True
    )
    assert('[{"data": [1, 2, 3], "name": "col 1"}, '
           '{"data": [1, "A", "2014-01-05", '
           '"2014-01-05 01:01:01", '
           '"2014-01-05 01:01:01.000001"], '
           '"name": "col 2"}, '
           '{"data": [1, 2, 3, NaN, NaN, Infinity, '
           '"2014-01-05"], "name": "col 3"}]' == json_columns)


def test_figure_json_encoding():
    df = pd.DataFrame(columns=['col 1'], data=[1, 2, 3])
    s1 = Scatter3d(x=numeric_list, y=np_list, z=mixed_list)
    s2 = Scatter(x=df['col 1'])
    data = Data([s1, s2])
    figure = Figure(data=data)

    js1 = json.dumps(s1, cls=utils._plotlyJSONEncoder, sort_keys=True)
    js2 = json.dumps(s2, cls=utils._plotlyJSONEncoder, sort_keys=True)

    assert(js1 == '{"type": "scatter3d", "x": [1, 2, 3], '
                  '"y": [1, 2, 3, NaN, NaN, Infinity, "2014-01-05"], '
                  '"z": [1, "A", "2014-01-05", '
                  '"2014-01-05 01:01:01", "2014-01-05 01:01:01.000001"]}')
    assert(js2 == '{"type": "scatter", "x": [1, 2, 3]}')

    # Test JSON encoding works
    json.dumps(data, cls=utils._plotlyJSONEncoder, sort_keys=True)
    json.dumps(figure, cls=utils._plotlyJSONEncoder, sort_keys=True)

    # Test data wasn't mutated
    assert(bool(np.asarray(np_list ==
                np.array([1, 2, 3, np.NaN,
                          np.NAN, np.Inf, dt(2014, 1, 5)])).all()))
    assert(set(data[0]['z']) ==
           set([1, 'A', dt(2014, 1, 5), dt(2014, 1, 5, 1, 1, 1),
                dt(2014, 1, 5, 1, 1, 1, 1)]))


def test_pandas_json_encoding():
    j1 = json.dumps(df['col 1'], cls=utils._plotlyJSONEncoder)
    assert(j1 == '[1, 2, 3, "2014-01-05", null, NaN, Infinity]')

    # Test that data wasn't mutated
    assert_series_equal(df['col 1'],
                        pd.Series([1, 2, 3, dt(2014, 1, 5),
                                   pd.NaT, np.NaN, np.Inf]))

    j2 = json.dumps(df.index, cls=utils._plotlyJSONEncoder)
    assert(j2 == '[0, 1, 2, 3, 4, 5, 6]')

    nat = [pd.NaT]
    j3 = json.dumps(nat, cls=utils._plotlyJSONEncoder)
    assert(j3 == '[null]')
    assert(nat[0] is pd.NaT)

    j4 = json.dumps(rng, cls=utils._plotlyJSONEncoder)
    assert(j4 == '["2011-01-01", "2011-01-01 01:00:00"]')

    j5 = json.dumps(ts, cls=utils._plotlyJSONEncoder)
    assert(j5 == '[1.5, 2.5]')
    assert_series_equal(ts, pd.Series([1.5, 2.5], index=rng))

    j6 = json.dumps(ts.index, cls=utils._plotlyJSONEncoder)
    assert(j6 == '["2011-01-01", "2011-01-01 01:00:00"]')
