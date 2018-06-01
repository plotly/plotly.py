"""
Module to test plotly.utils with optional dependencies.

"""
from __future__ import absolute_import

import datetime
import math
import decimal
from datetime import datetime as dt
from unittest import TestCase

import numpy as np
import pandas as pd
import pytz
from nose.plugins.attrib import attr
from pandas.util.testing import assert_series_equal
from requests.compat import json as _json

from plotly import optional_imports, utils
from plotly.graph_objs import Scatter, Scatter3d, Figure, Data
from plotly.grid_objs import Column

matplotlylib = optional_imports.get_module('plotly.matplotlylib')

if matplotlylib:
    import matplotlib.pyplot as plt
    from plotly.matplotlylib import Exporter, PlotlyRenderer


class TestJSONEncoder(TestCase):

    def test_encode_as_plotly(self):

        # should *fail* when object doesn't have `to_plotly_json` attribute
        objs_without_attr = [
            1, 'one', set(['a', 'set']), {'a': 'dict'}, ['a', 'list']
        ]
        for obj in objs_without_attr:
            self.assertRaises(utils.NotEncodable,
                              utils.PlotlyJSONEncoder.encode_as_plotly, obj)

        # should return without exception when obj has `to_plotly_josn` attr
        expected_res = 'wedidit'

        class ObjWithAttr(object):

            def to_plotly_json(self):
                return expected_res

        res = utils.PlotlyJSONEncoder.encode_as_plotly(ObjWithAttr())
        self.assertEqual(res, expected_res)

    def test_encode_as_list(self):

        # should *fail* when object doesn't have `tolist` method
        objs_without_attr = [
            1, 'one', set(['a', 'set']), {'a': 'dict'}, ['a', 'list']
        ]
        for obj in objs_without_attr:
            self.assertRaises(utils.NotEncodable,
                              utils.PlotlyJSONEncoder.encode_as_list, obj)

        # should return without exception when obj has `tolist` attr
        expected_res = ['some', 'list']

        class ObjWithAttr(object):

            def tolist(self):
                return expected_res

        res = utils.PlotlyJSONEncoder.encode_as_list(ObjWithAttr())
        self.assertEqual(res, expected_res)

    def test_encode_as_pandas(self):

        # should *fail* on things that are not specific pandas objects
        not_pandas = ['giraffe', 6, float('nan'), ['a', 'list']]
        for obj in not_pandas:
            self.assertRaises(utils.NotEncodable,
                              utils.PlotlyJSONEncoder.encode_as_pandas, obj)

        # should succeed when we've got specific pandas thingies
        res = utils.PlotlyJSONEncoder.encode_as_pandas(pd.NaT)
        self.assertTrue(res is None)

    def test_encode_as_numpy(self):

        # should *fail* on non-numpy-y things
        not_numpy = ['hippo', 8, float('nan'), {'a': 'dict'}]
        for obj in not_numpy:
            self.assertRaises(utils.NotEncodable,
                              utils.PlotlyJSONEncoder.encode_as_numpy, obj)

        # should succeed with numpy-y-thingies
        res = utils.PlotlyJSONEncoder.encode_as_numpy(np.ma.core.masked)
        self.assertTrue(math.isnan(res))

    def test_encode_valid_datetime(self):

        # should *fail* without 'utcoffset' and 'isoformat' and '__sub__' attrs
        #non_datetimes = [datetime.date(2013, 10, 1), 'noon', 56, '00:00:00']
        non_datetimes = [datetime.date(2013, 10, 1)]
        for obj in non_datetimes:
            self.assertRaises(utils.NotEncodable,
                              utils.PlotlyJSONEncoder.encode_as_datetime, obj)

    def test_encode_as_datetime(self):
        # should succeed with 'utcoffset', 'isoformat' and '__sub__' attrs
        res = utils.PlotlyJSONEncoder.encode_as_datetime(
            datetime.datetime(2013, 10, 1)
        )
        self.assertEqual(res, '2013-10-01')

    def test_encode_as_datetime_with_microsecond(self):
        # should not include extraneous microsecond info if DNE
        res = utils.PlotlyJSONEncoder.encode_as_datetime(
            datetime.datetime(2013, 10, 1, microsecond=0)
        )
        self.assertEqual(res, '2013-10-01')

        # should include microsecond info if present
        res = utils.PlotlyJSONEncoder.encode_as_datetime(
            datetime.datetime(2013, 10, 1, microsecond=10)
        )
        self.assertEqual(res, '2013-10-01 00:00:00.000010')

    def test_encode_as_datetime_with_localized_tz(self):
        # should convert tzinfo to utc. Note that in october, we're in EDT!
        # therefore the 4 hour difference is correct.
        naive_datetime = datetime.datetime(2013, 10, 1)
        aware_datetime = pytz.timezone('US/Eastern').localize(naive_datetime)

        res = utils.PlotlyJSONEncoder.encode_as_datetime(aware_datetime)
        self.assertEqual(res, '2013-10-01 04:00:00')

    def test_encode_as_date(self):

        # should *fail* without 'utcoffset' and 'isoformat' and '__sub__' attrs
        non_datetimes = ['noon', 56, '00:00:00']
        for obj in non_datetimes:
            self.assertRaises(utils.NotEncodable,
                              utils.PlotlyJSONEncoder.encode_as_date, obj)

        # should work with a date
        a_date = datetime.date(2013, 10, 1)
        res = utils.PlotlyJSONEncoder.encode_as_date(a_date)
        self.assertEqual(res, '2013-10-01')

        # should also work with a date time without a utc offset!
        res = utils.PlotlyJSONEncoder.encode_as_date(
            datetime.datetime(2013, 10, 1, microsecond=10)
        )
        self.assertEqual(res, '2013-10-01 00:00:00.000010')

    def test_encode_as_decimal(self):

        # should work with decimal values
        res = utils.PlotlyJSONEncoder.encode_as_decimal(decimal.Decimal(1.023452))

        self.assertAlmostEqual(res, 1.023452)  # Checks upto 7 decimal places
        self.assertIsInstance(res, float)

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
    json_columns = _json.dumps(
        columns, cls=utils.PlotlyJSONEncoder, sort_keys=True
    )
    assert('[{"data": [1, 2, 3], "name": "col 1"}, '
           '{"data": [1, "A", "2014-01-05", '
           '"2014-01-05 01:01:01", '
           '"2014-01-05 01:01:01.000001"], '
           '"name": "col 2"}, '
           '{"data": [1, 2, 3, null, null, null, '
           '"2014-01-05"], "name": "col 3"}]' == json_columns)


def test_figure_json_encoding():
    df = pd.DataFrame(columns=['col 1'], data=[1, 2, 3])
    s1 = Scatter3d(x=numeric_list, y=np_list, z=mixed_list)
    s2 = Scatter(x=df['col 1'])
    data = Data([s1, s2])
    figure = Figure(data=data)

    js1 = _json.dumps(s1, cls=utils.PlotlyJSONEncoder, sort_keys=True)
    js2 = _json.dumps(s2, cls=utils.PlotlyJSONEncoder, sort_keys=True)

    assert(js1 == '{"type": "scatter3d", "x": [1, 2, 3], '
                  '"y": [1, 2, 3, null, null, null, "2014-01-05"], '
                  '"z": [1, "A", "2014-01-05", '
                  '"2014-01-05 01:01:01", "2014-01-05 01:01:01.000001"]}')
    assert(js2 == '{"type": "scatter", "x": [1, 2, 3]}')

    # Test JSON encoding works
    _json.dumps(data, cls=utils.PlotlyJSONEncoder, sort_keys=True)
    _json.dumps(figure, cls=utils.PlotlyJSONEncoder, sort_keys=True)

    # Test data wasn't mutated
    np_array = np.array(
        [1, 2, 3, np.NaN, np.NAN, np.Inf, dt(2014, 1, 5)]
    )
    for k in range(len(np_array)):
        if k in [3, 4]:
            # check NaN
            assert np.isnan(np_list[k]) and np.isnan(np_array[k])
        else:
            # non-NaN
            assert np_list[k] == np_array[k]

    assert(set(data[0]['z']) ==
           set([1, 'A', dt(2014, 1, 5), dt(2014, 1, 5, 1, 1, 1),
                dt(2014, 1, 5, 1, 1, 1, 1)]))


def test_datetime_json_encoding():
    j1 = _json.dumps(dt_list, cls=utils.PlotlyJSONEncoder)
    assert(j1 == '["2014-01-05", '
                 '"2014-01-05 01:01:01", '
                 '"2014-01-05 01:01:01.000001"]')
    j2 = _json.dumps({"x": dt_list}, cls=utils.PlotlyJSONEncoder)
    assert(j2 == '{"x": ["2014-01-05", '
                 '"2014-01-05 01:01:01", '
                 '"2014-01-05 01:01:01.000001"]}')


def test_pandas_json_encoding():
    j1 = _json.dumps(df['col 1'], cls=utils.PlotlyJSONEncoder)
    print(j1)
    print('\n')
    assert(j1 == '[1, 2, 3, "2014-01-05", null, null, null]')

    # Test that data wasn't mutated
    assert_series_equal(df['col 1'],
                        pd.Series([1, 2, 3, dt(2014, 1, 5),
                                   pd.NaT, np.NaN, np.Inf], name='col 1'))

    j2 = _json.dumps(df.index, cls=utils.PlotlyJSONEncoder)
    assert(j2 == '[0, 1, 2, 3, 4, 5, 6]')

    nat = [pd.NaT]
    j3 = _json.dumps(nat, cls=utils.PlotlyJSONEncoder)
    assert(j3 == '[null]')
    assert(nat[0] is pd.NaT)

    j4 = _json.dumps(rng, cls=utils.PlotlyJSONEncoder)
    assert(j4 == '["2011-01-01", "2011-01-01 01:00:00"]')

    j5 = _json.dumps(ts, cls=utils.PlotlyJSONEncoder)
    assert(j5 == '[1.5, 2.5]')
    assert_series_equal(ts, pd.Series([1.5, 2.5], index=rng))

    j6 = _json.dumps(ts.index, cls=utils.PlotlyJSONEncoder)
    assert(j6 == '["2011-01-01", "2011-01-01 01:00:00"]')


def test_numpy_masked_json_encoding():
    l = [1, 2, np.ma.core.masked]
    j1 = _json.dumps(l, cls=utils.PlotlyJSONEncoder)
    print(j1)
    assert(j1 == '[1, 2, null]')


if matplotlylib:
    @attr('matplotlib')
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

        plotopts = {'x': 'esN'}
        fig, ax = plt.subplots(1, 1)
        df.plot(ax=ax, **plotopts)

        renderer = PlotlyRenderer()
        Exporter(renderer).run(fig)

        _json.dumps(renderer.plotly_fig, cls=utils.PlotlyJSONEncoder)

        jy = _json.dumps(renderer.plotly_fig['data'][1]['y'],
                         cls=utils.PlotlyJSONEncoder)
        print(jy)
        array = _json.loads(jy)
        assert(array == [-398.11793027, -398.11792966, -398.11786308, None])


def test_numpy_dates():
    a = np.arange(np.datetime64('2011-07-11'), np.datetime64('2011-07-18'))
    j1 = _json.dumps(a, cls=utils.PlotlyJSONEncoder)
    assert(j1 == '["2011-07-11", "2011-07-12", "2011-07-13", '
                 '"2011-07-14", "2011-07-15", "2011-07-16", '
                 '"2011-07-17"]')


def test_datetime_dot_date():
    a = [datetime.date(2014, 1, 1), datetime.date(2014, 1, 2)]
    j1 = _json.dumps(a, cls=utils.PlotlyJSONEncoder)
    assert(j1 == '["2014-01-01", "2014-01-02"]')
