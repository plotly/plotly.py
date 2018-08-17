from __future__ import absolute_import

from requests.compat import json as _json
from requests.exceptions import ConnectionError

from plotly import version
from plotly.api.utils import to_native_utf8_string
from plotly.api.v2 import utils
from plotly.exceptions import PlotlyRequestError
from plotly.session import sign_in
from plotly.tests.test_plot_ly.test_api import PlotlyApiTestCase


class MakeParamsTest(PlotlyApiTestCase):

    def test_make_params(self):
        params = utils.make_params(foo='FOO', bar=None)
        self.assertEqual(params, {'foo': 'FOO'})

    def test_make_params_empty(self):
        params = utils.make_params(foo=None, bar=None)
        self.assertEqual(params, {})


class BuildUrlTest(PlotlyApiTestCase):

    def test_build_url(self):
        url = utils.build_url('cats')
        self.assertEqual(url, '{}/v2/cats'.format(self.plotly_api_domain))

    def test_build_url_id(self):
        url = utils.build_url('cats', id='MsKitty')
        self.assertEqual(
            url, '{}/v2/cats/MsKitty'.format(self.plotly_api_domain)
        )

    def test_build_url_route(self):
        url = utils.build_url('cats', route='about')
        self.assertEqual(
            url, '{}/v2/cats/about'.format(self.plotly_api_domain)
        )

    def test_build_url_id_route(self):
        url = utils.build_url('cats', id='MsKitty', route='de-claw')
        self.assertEqual(
            url, '{}/v2/cats/MsKitty/de-claw'.format(self.plotly_api_domain)
        )


class ValidateResponseTest(PlotlyApiTestCase):

    def test_validate_ok(self):
        try:
            utils.validate_response(self.get_response())
        except PlotlyRequestError:
            self.fail('Expected this to pass!')

    def test_validate_not_ok(self):
        bad_status_codes = (400, 404, 500)
        for bad_status_code in bad_status_codes:
            response = self.get_response(status_code=bad_status_code)
            self.assertRaises(PlotlyRequestError, utils.validate_response,
                              response)

    def test_validate_no_content(self):

        # We shouldn't flake if the response has no content.

        response = self.get_response(content=b'', status_code=400)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, u'No Content')
            self.assertEqual(e.status_code, 400)
            self.assertEqual(e.content.decode('utf-8'), u'')
        else:
            self.fail('Expected this to raise!')

    def test_validate_non_json_content(self):
        response = self.get_response(content=b'foobar', status_code=400)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, 'foobar')
            self.assertEqual(e.status_code, 400)
            self.assertEqual(e.content, b'foobar')
        else:
            self.fail('Expected this to raise!')

    def test_validate_json_content_array(self):
        content = self.to_bytes(_json.dumps([1, 2, 3]))
        response = self.get_response(content=content, status_code=400)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, to_native_utf8_string(content))
            self.assertEqual(e.status_code, 400)
            self.assertEqual(e.content, content)
        else:
            self.fail('Expected this to raise!')

    def test_validate_json_content_dict_no_errors(self):
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

    def test_validate_json_content_dict_one_error_bad(self):
        content = self.to_bytes(_json.dumps({'errors': [{}]}))
        response = self.get_response(content=content, status_code=400)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, to_native_utf8_string(content))
            self.assertEqual(e.status_code, 400)
            self.assertEqual(e.content, content)
        else:
            self.fail('Expected this to raise!')

        content = self.to_bytes(_json.dumps({'errors': [{'message': ''}]}))
        response = self.get_response(content=content, status_code=400)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, to_native_utf8_string(content))
            self.assertEqual(e.status_code, 400)
            self.assertEqual(e.content, content)
        else:
            self.fail('Expected this to raise!')

    def test_validate_json_content_dict_one_error_ok(self):
        content = self.to_bytes(_json.dumps(
            {'errors': [{'message': 'not ok!'}]}))
        response = self.get_response(content=content, status_code=400)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, 'not ok!')
            self.assertEqual(e.status_code, 400)
            self.assertEqual(e.content, content)
        else:
            self.fail('Expected this to raise!')

    def test_validate_json_content_dict_multiple_errors(self):
        content = self.to_bytes(_json.dumps({'errors': [
            {'message': 'not ok!'}, {'message': 'bad job...'}
        ]}))
        response = self.get_response(content=content, status_code=400)
        try:
            utils.validate_response(response)
        except PlotlyRequestError as e:
            self.assertEqual(e.message, 'not ok!\nbad job...')
            self.assertEqual(e.status_code, 400)
            self.assertEqual(e.content, content)
        else:
            self.fail('Expected this to raise!')


class GetHeadersTest(PlotlyApiTestCase):

    def test_normal_auth(self):
        headers = utils.get_headers()
        expected_headers = {
            'plotly-client-platform': 'python {}'.format(version.stable_semver()),
            'authorization': 'Basic Zm9vOmJhcg==',
            'content-type': 'application/json'
        }
        self.assertEqual(headers, expected_headers)

    def test_proxy_auth(self):
        sign_in(self.username, self.api_key, plotly_proxy_authorization=True)
        headers = utils.get_headers()
        expected_headers = {
            'plotly-client-platform': 'python {}'.format(version.stable_semver()),
            'authorization': 'Basic Y25ldDpob29wbGE=',
            'plotly-authorization': 'Basic Zm9vOmJhcg==',
            'content-type': 'application/json'
        }
        self.assertEqual(headers, expected_headers)


class RequestTest(PlotlyApiTestCase):

    def setUp(self):
        super(RequestTest, self).setUp()

        # Mock the actual api call, we don't want to do network tests here.
        self.request_mock = self.mock('plotly.api.v2.utils.requests.request')
        self.request_mock.return_value = self.get_response()

        # Mock the validation function since we can test that elsewhere.
        self.validate_response_mock = self.mock(
            'plotly.api.v2.utils.validate_response')

        self.method = 'get'
        self.url = 'https://foo.bar.does.not.exist.anywhere'

    def test_request_with_params(self):

        # urlencode transforms `True` --> `'True'`, which isn't super helpful,
        # Our backend accepts the JS `true`, so we want `True` --> `'true'`.

        params = {'foo': True, 'bar': 'True', 'baz': False, 'zap': 0}
        utils.request(self.method, self.url, params=params)
        args, kwargs = self.request_mock.call_args
        method, url = args
        expected_params = {'foo': 'true', 'bar': 'True', 'baz': 'false',
                           'zap': 0}
        self.assertEqual(method, self.method)
        self.assertEqual(url, self.url)
        self.assertEqual(kwargs['params'], expected_params)

    def test_request_with_non_native_objects(self):

        # We always send along json, but it may contain non-native objects like
        # a pandas array or a Column reference. Make sure that's handled in one
        # central place.

        class Duck(object):
            def to_plotly_json(self):
                return 'what else floats?'

        utils.request(self.method, self.url, json={'foo': [Duck(), Duck()]})
        args, kwargs = self.request_mock.call_args
        method, url = args
        expected_data = '{"foo": ["what else floats?", "what else floats?"]}'
        self.assertEqual(method, self.method)
        self.assertEqual(url, self.url)
        self.assertEqual(kwargs['data'], expected_data)
        self.assertNotIn('json', kwargs)

    def test_request_with_ConnectionError(self):

        # requests can flake out and not return a response object, we want to
        # make sure we remain consistent with our errors.

        self.request_mock.side_effect = ConnectionError()
        self.assertRaises(PlotlyRequestError, utils.request, self.method,
                          self.url)

    def test_request_validate_response(self):

        # Finally, we check details elsewhere, but make sure we do validate.

        utils.request(self.method, self.url)
        assert self.request_mock.call_count == 1
