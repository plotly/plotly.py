from chart_studio.api.v2 import users
from chart_studio.tests.test_plot_ly.test_api import PlotlyApiTestCase


class UsersTest(PlotlyApiTestCase):
    def setUp(self):
        super(UsersTest, self).setUp()

        # Mock the actual api call, we don't want to do network tests here.
        self.request_mock = self.mock("chart_studio.api.v2.utils.requests.request")
        self.request_mock.return_value = self.get_response()

        # Mock the validation function since we can test that elsewhere.
        self.mock("chart_studio.api.v2.utils.validate_response")

    def test_current(self):
        users.current()
        assert self.request_mock.call_count == 1
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, "get")
        self.assertEqual(url, "{}/v2/users/current".format(self.plotly_api_domain))
        self.assertNotIn("params", kwargs)
