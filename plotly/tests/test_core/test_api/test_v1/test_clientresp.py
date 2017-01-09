from __future__ import absolute_import

from plotly import version
from plotly.api.v1 import clientresp
from plotly.tests.test_core.test_api import PlotlyApiTestCase


class Duck(object):
    def to_plotly_json(self):
        return 'what else floats?'


class ClientrespTest(PlotlyApiTestCase):

    def setUp(self):
        super(ClientrespTest, self).setUp()

        # Mock the actual api call, we don't want to do network tests here.
        self.request_mock = self.mock('plotly.api.v1.utils.requests.request')
        self.request_mock.return_value = self.get_response(b'{}', 200)

        # Mock the validation function since we can test that elsewhere.
        self.mock('plotly.api.v1.utils.validate_response')

    def test_data_only(self):
        data = [{'y': [3, 5], 'name': Duck()}]
        clientresp(data)
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(url, '{}/clientresp'.format(self.plotly_domain))
        expected_data = ({
            'origin': 'plot',
            'args': '[{"name": "what else floats?", "y": [3, 5]}]',
            'platform': 'python', 'version': version.__version__, 'key': 'bar',
            'kwargs': '{}', 'un': 'foo'
        })
        self.assertEqual(kwargs['data'], expected_data)
        self.assertTrue(kwargs['verify'])
        self.assertEqual(kwargs['headers'], {})

    def test_data_and_kwargs(self):
        data = [{'y': [3, 5], 'name': Duck()}]
        clientresp_kwargs = {'layout': {'title': 'mah plot'}, 'filename': 'ok'}
        clientresp(data, **clientresp_kwargs)
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(url, '{}/clientresp'.format(self.plotly_domain))
        expected_data = ({
            'origin': 'plot',
            'args': '[{"name": "what else floats?", "y": [3, 5]}]',
            'platform': 'python', 'version': version.__version__, 'key': 'bar',
            'kwargs': '{"filename": "ok", "layout": {"title": "mah plot"}}',
            'un': 'foo'
        })
        self.assertEqual(kwargs['data'], expected_data)
        self.assertTrue(kwargs['verify'])
        self.assertEqual(kwargs['headers'], {})
