from nose.tools import raises
from nose import with_setup
from nose.plugins.attrib import attr

from datetime import datetime as dt
import datetime
import numpy as np
import json
import pandas as pd
from pandas.util.testing import assert_series_equal
import matplotlib.pyplot as plt

from plotly import utils
from plotly.grid_objs import Column
from plotly.graph_objs import Scatter, Scatter3d, Figure, Data
from plotly.matplotlylib import Exporter, PlotlyRenderer
from plotly.plotly import plot

## JSON encoding
numeric_list = [1, 2, 3]
np_list = np.array([1, 2, 3, np.NaN, np.NAN, np.Inf, dt(2014, 1, 5)])
mixed_list = [1, 'A', dt(2014, 1, 5), dt(2014, 1, 5, 1, 1, 1),
              dt(2014, 1, 5, 1, 1, 1, 1)]
dt_list = [dt(2014, 1, 5), dt(2014, 1, 5, 1, 1, 1),
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


def test_datetime_json_encoding():
    j1 = json.dumps(dt_list, cls=utils._plotlyJSONEncoder)
    assert(j1 == '["2014-01-05", '
                 '"2014-01-05 01:01:01", '
                 '"2014-01-05 01:01:01.000001"]')
    j2 = json.dumps({"x": dt_list}, cls=utils._plotlyJSONEncoder)
    assert(j2 == '{"x": ["2014-01-05", '
                 '"2014-01-05 01:01:01", '
                 '"2014-01-05 01:01:01.000001"]}')


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


def test_numpy_masked_json_encoding():
    l = [1, 2, np.ma.core.masked]
    j1 = json.dumps(l, cls=utils._plotlyJSONEncoder)
    assert(j1 == '[1, 2, NaN]')
    assert(set(l) == set([1, 2, np.ma.core.masked]))


def test_masked_constants_example():
    # example from: https://gist.github.com/tschaume/d123d56bf586276adb98
    data = {
        'esN': [0, 1, 2, 3],
        'ewe_is0': [-398.11901997, -398.11902774,
                    -398.11897111, -398.11882215],
        'ewe_is1': [-398.11793027, -398.11792966, -398.11786308, None],
        'ewe_is2': [-398.11397008, -398.11396421, None, None]
    }
    df = pd.DataFrame.from_dict(data)

    plotopts = {'x': 'esN', 'marker': 'o'}
    fig, ax = plt.subplots(1, 1)
    df.plot(ax=ax, **plotopts)

    renderer = PlotlyRenderer()
    Exporter(renderer).run(fig)

    json.dumps(renderer.plotly_fig, cls=utils._plotlyJSONEncoder)

    jy = json.dumps(renderer.plotly_fig['data'][1]['y'],
                    cls=utils._plotlyJSONEncoder)
    assert(jy == '[-398.11793026999999, -398.11792966000002, '
                 '-398.11786308000001, NaN]')


def test_numpy_dates():
    a = np.arange(np.datetime64('2011-07-11'), np.datetime64('2011-07-18'))
    j1 = json.dumps(a, cls=utils._plotlyJSONEncoder)
    assert(j1 == '["2011-07-11", "2011-07-12", "2011-07-13", '
                 '"2011-07-14", "2011-07-15", "2011-07-16", '
                 '"2011-07-17"]')


def test_datetime_dot_date():
    a = [datetime.date(2014, 1, 1), datetime.date(2014, 1, 2)]
    j1 = json.dumps(a, cls=utils._plotlyJSONEncoder)
    assert(j1 == '["2014-01-01", "2014-01-02"]')
