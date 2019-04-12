from __future__ import absolute_import

from unittest import TestCase

from requests import Response
from requests.compat import json as _json
from requests.exceptions import ConnectionError

from plotly.api.utils import to_native_utf8_string
from plotly.api.v1 import utils
from plotly.exceptions import PlotlyError, PlotlyRequestError
from plotly.session import sign_in
from plotly.tests.test_plot_ly.test_api import PlotlyApiTestCase
from plotly.tests.utils import PlotlyTestCase

import sys

# import from mock, MagicMock
if sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from unittest.mock import MagicMock, patch
else:
    from mock import patch, MagicMock


class ValidateResponseTest(PlotlyApiTestCase):

    def test_validate_ok(self):
        try:
            utils.validate_response(self.get_response(content=b'{}'))
        except PlotlyRequestError:
            self.fail('Expected this to pass!')

    def test_validate_not_ok(self):
        bad_status_codes = (400, 404, 500)
        for bad_status_code in bad_status_codes:
            response = self.get_response(content=b'{}',
                                         status_code=bad_status_code)
            self.assertRaises(PlotlyRequestError, utils.validate_response,
                              response)

    def test_validate_no_content(self):

        # We shouldn't flake if the response has no content.

        response = self.get_response(content=b'', status_code=200)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, 'No Content')
            self.assertEqual(e.status_code, 200)
            self.assertEqual(e.content, b'')
        else:
            self.fail('Expected this to raise!')

    def test_validate_non_json_content(self):
        response = self.get_response(content=b'foobar', status_code=200)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, 'foobar')
            self.assertEqual(e.status_code, 200)
            self.assertEqual(e.content, b'foobar')
        else:
            self.fail('Expected this to raise!')

    def test_validate_json_content_array(self):
        content = self.to_bytes(_json.dumps([1, 2, 3]))
        response = self.get_response(content=content, status_code=200)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, to_native_utf8_string(content))
            self.assertEqual(e.status_code, 200)
            self.assertEqual(e.content, content)
        else:
            self.fail('Expected this to raise!')

    def test_validate_json_content_dict_no_error(self):
        content = self.to_bytes(_json.dumps({'foo': 'bar'}))
        response = self.get_response(content=content, status_code=400)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, to_native_utf8_string(content))
            self.assertEqual(e.status_code, 400)
            self.assertEqual(e.content, content)
        else:
            self.fail('Expected this to raise!')

    def test_validate_json_content_dict_error_empty(self):
        content = self.to_bytes(_json.dumps({'error': ''}))
        response = self.get_response(content=content, status_code=200)
        try:
            utils.validate_response(response)
        except PlotlyRequestError:
            self.fail('Expected this not to raise!')

    def test_validate_json_content_dict_one_error_ok(self):
        content = self.to_bytes(_json.dumps({'error': 'not ok!'}))
        response = self.get_response(content=content, status_code=200)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, 'not ok!')
            self.assertEqual(e.status_code, 200)
            self.assertEqual(e.content, content)
        else:
            self.fail('Expected this to raise!')


class GetHeadersTest(PlotlyTestCase):

    def setUp(self):
        super(GetHeadersTest, self).setUp()
        self.domain = 'https://foo.bar'
        self.username = 'hodor'
        self.api_key = 'secret'
        sign_in(self.username, self.api_key, proxy_username='kleen-kanteen',
                proxy_password='hydrated', plotly_proxy_authorization=False)

    def test_normal_auth(self):
        headers = utils.get_headers()
        expected_headers = {}
        self.assertEqual(headers, expected_headers)

    def test_proxy_auth(self):
        sign_in(self.username, self.api_key, plotly_proxy_authorization=True)
        headers = utils.get_headers()
        expected_headers = {
            'authorization': 'Basic a2xlZW4ta2FudGVlbjpoeWRyYXRlZA=='
        }
        self.assertEqual(headers, expected_headers)


class RequestTest(PlotlyTestCase):

    def setUp(self):
        super(RequestTest, self).setUp()
        self.domain = 'https://foo.bar'
        self.username = 'hodor'
        self.api_key = 'secret'
        sign_in(self.username, self.api_key, proxy_username='kleen-kanteen',
                proxy_password='hydrated', plotly_proxy_authorization=False)

        # Mock the actual api call, we don't want to do network tests here.
        patcher = patch('plotly.api.v1.utils.requests.request')
        self.request_mock = patcher.start()
        self.addCleanup(patcher.stop)
        self.request_mock.return_value = MagicMock(Response)

        # Mock the validation function since we test that elsewhere.
        patcher = patch('plotly.api.v1.utils.validate_response')
        self.validate_response_mock = patcher.start()
        self.addCleanup(patcher.stop)

        self.method = 'get'
        self.url = 'https://foo.bar.does.not.exist.anywhere'

    def test_request_with_json(self):

        # You can pass along non-native objects in the `json` kwarg for a
        # requests.request, however, V1 packs up json objects a little
        # differently, so we don't allow such requests.

        self.assertRaises(PlotlyError, utils.request, self.method,
                          self.url, json={})

    def test_request_with_ConnectionError(self):

        # requests can flake out and not return a response object, we want to
        # make sure we remain consistent with our errors.

        self.request_mock.side_effect = ConnectionError()
        self.assertRaises(PlotlyRequestError, utils.request, self.method,
                          self.url)

    def test_request_validate_response(self):

        # Finally, we check details elsewhere, but make sure we do validate.

        utils.request(self.method, self.url)
        assert self.validate_response_mock.call_count == 1
