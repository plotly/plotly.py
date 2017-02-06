from __future__ import absolute_import

from plotly.api.v2 import users
from plotly.tests.test_core.test_api import PlotlyApiTestCase


class UsersTest(PlotlyApiTestCase):

    def setUp(self):
        super(UsersTest, self).setUp()

        # Mock the actual api call, we don't want to do network tests here.
        self.request_mock = self.mock('plotly.api.v2.utils.requests.request')
        self.request_mock.return_value = self.get_response()

        # Mock the validation function since we can test that elsewhere.
        self.mock('plotly.api.v2.utils.validate_response')

    def test_current(self):
        users.current()
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'get')
        self.assertEqual(
            url, '{}/v2/users/current'.format(self.plotly_api_domain)
        )
        self.assertNotIn('params', kwargs)
