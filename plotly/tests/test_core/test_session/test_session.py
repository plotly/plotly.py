from __future__ import absolute_import

from unittest import TestCase

from plotly.session import update_session_plot_options
from plotly.exceptions import PlotlyError


class TestSession(TestCase):

    def test_update_session_plot_options_sharing(self):

        # Return PlotlyError when sharing arguement is not
        # 'public', 'private' or 'secret'

        kwargs = {'sharing': 'priva'}
        self.assertRaises(PlotlyError, update_session_plot_options, **kwargs)
