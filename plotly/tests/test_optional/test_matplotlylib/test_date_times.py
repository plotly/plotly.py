from __future__ import absolute_import
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import date2num
import plotly.tools as tls
from unittest import TestCase

from plotly.tests.test_optional.optional_utils import compare_dict, run_fig


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

        print date_strings
        print pfig['data'][0]['x']
        # we use the same format here, so we expect equality here
        self.assertEqual(
            fig.axes[0].lines[0].get_xydata()[0][0], 7.33776000e+05
        )
        self.assertEqual(pfig['data'][0]['x'], date_strings)
