from __future__ import absolute_import

from requests.compat import json as _json

from plotly.api.v2 import images
from plotly.tests.test_core.test_api import PlotlyApiTestCase


class ImagesTest(PlotlyApiTestCase):

    def setUp(self):
        super(ImagesTest, self).setUp()

        # Mock the actual api call, we don't want to do network tests here.
        self.request_mock = self.mock('plotly.api.v2.utils.requests.request')
        self.request_mock.return_value = self.get_response()

        # Mock the validation function since we can test that elsewhere.
        self.mock('plotly.api.v2.utils.validate_response')

    def test_create(self):

        body = {
            "figure": {
                "data": [{"y": [10, 10, 2, 20]}],
                "layout": {"width": 700}
            },
            "width": 1000,
            "height": 500,
            "format": "png",
            "scale": 4,
            "encoded": False
        }

        images.create(body)
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(url, '{}/v2/images'.format(self.plotly_api_domain))
        self.assertEqual(kwargs['data'], _json.dumps(body, sort_keys=True))
