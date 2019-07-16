from __future__ import absolute_import

from chart_studio.tests.utils import PlotlyTestCase

from chart_studio import session
from chart_studio.session import update_session_plot_options, SHARING_OPTIONS
from _plotly_utils.exceptions import PlotlyError


class TestSession(PlotlyTestCase):
    def setUp(self):
        super(TestSession, self).setUp()
        session._session["plot_options"].clear()

    def test_update_session_plot_options_invalid_sharing_argument(self):

        # Return PlotlyError when sharing arguement is not
        # 'public', 'private' or 'secret'

        kwargs = {"sharing": "priva"}
        self.assertRaises(PlotlyError, update_session_plot_options, **kwargs)

    def test_update_session_plot_options_valid_sharing_argument(self):

        # _session['plot_options'] should contain sharing key after
        # update_session_plot_options is called by correct arguments
        # 'public, 'private' or 'secret'
        from chart_studio.session import _session

        for key in SHARING_OPTIONS:
            kwargs = {"sharing": key}
            update_session_plot_options(**kwargs)

            self.assertEqual(_session["plot_options"], kwargs)
