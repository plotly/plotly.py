from __future__ import absolute_import

import datetime
import random
from unittest import TestCase

import pandas as pd
from nose.plugins.attrib import attr

import plotly.tools as tls
from plotly import optional_imports

matplotlylib = optional_imports.get_module('plotly.matplotlylib')

if matplotlylib:
    import matplotlib

    # Force matplotlib to not use any Xwindows backend.
    matplotlib.use('Agg')
    from matplotlib.dates import date2num
    import matplotlib.pyplot as plt


@attr('matplotlib')
class TestDateTimes(TestCase):

    def test_normal_mpl_dates(self):
        datetime_format = '%Y-%m-%d %H:%M:%S'
        y = [1, 2, 3, 4]
        date_strings = ['2010-01-04 00:00:00',
                        '2010-01-04 10:00:00',
                        '2010-01-04 23:00:59',
                        '2010-01-05 00:00:00']

        # 1. create datetimes from the strings
        dates = [datetime.datetime.strptime(date_string, datetime_format)
                 for date_string in date_strings]

        # 2. create the mpl_dates from these datetimes
        mpl_dates = date2num(dates)

        # make a figure in mpl
        fig, ax = plt.subplots()
        ax.plot_date(mpl_dates, y)

        # convert this figure to plotly's graph_objs
        pfig = tls.mpl_to_plotly(fig)

        print(date_strings)
        print(pfig['data'][0]['x'])
        # we use the same format here, so we expect equality here
        self.assertEqual(
            fig.axes[0].lines[0].get_xydata()[0][0], 7.33776000e+05
        )
        self.assertEqual(tuple(pfig['data'][0]['x']), tuple(date_strings))

    def test_pandas_time_series_date_formatter(self):
        ndays = 3
        x = pd.date_range('1/1/2001', periods=ndays, freq='D')
        y = [random.randint(0, 10) for i in range(ndays)]
        s = pd.DataFrame(y, columns=['a'])

        s['Date'] = x
        s.plot(x='Date')

        fig = plt.gcf()
        pfig = tls.mpl_to_plotly(fig)

        expected_x = ('2001-01-01 00:00:00',
                      '2001-01-02 00:00:00',
                      '2001-01-03 00:00:00')
        expected_x0 = 11323.0  # this is floating point days since epoch

        x0 = fig.axes[0].lines[0].get_xydata()[0][0]
        self.assertEqual(x0, expected_x0)
        self.assertEqual(pfig['data'][0]['x'], expected_x)
