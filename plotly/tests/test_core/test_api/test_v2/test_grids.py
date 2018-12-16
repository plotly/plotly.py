from __future__ import absolute_import

from requests.compat import json as _json

from plotly.api.v2 import grids
from plotly.tests.test_core.test_api import PlotlyApiTestCase


class GridsTest(PlotlyApiTestCase):

    def setUp(self):
        super(GridsTest, self).setUp()

        # Mock the actual api call, we don't want to do network tests here.
        self.request_mock = self.mock('plotly.api.v2.utils.requests.request')
        self.request_mock.return_value = self.get_response()

        # Mock the validation function since we can test that elsewhere.
        self.mock('plotly.api.v2.utils.validate_response')

    def test_create(self):
        filename = 'a grid'
        grids.create({'filename': filename})
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(url, '{}/v2/grids'.format(self.plotly_api_domain))
        self.assertEqual(
            kwargs['data'], '{{"filename": "{}"}}'.format(filename)
        )

    def test_retrieve(self):
        grids.retrieve('hodor:88')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'get')
        self.assertEqual(
            url, '{}/v2/grids/hodor:88'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], {})

    def test_retrieve_share_key(self):
        grids.retrieve('hodor:88', share_key='foobar')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'get')
        self.assertEqual(
            url, '{}/v2/grids/hodor:88'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], {'share_key': 'foobar'})

    def test_update(self):
        new_filename = '..zzZ ..zzZ'
        grids.update('hodor:88', body={'filename': new_filename})
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'put')
        self.assertEqual(
            url, '{}/v2/grids/hodor:88'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['data'],
                         '{{"filename": "{}"}}'.format(new_filename))

    def test_trash(self):
        grids.trash('hodor:88')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(
            url, '{}/v2/grids/hodor:88/trash'.format(self.plotly_api_domain)
        )

    def test_restore(self):
        grids.restore('hodor:88')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(
            url, '{}/v2/grids/hodor:88/restore'.format(self.plotly_api_domain)
        )

    def test_permanent_delete(self):
        grids.permanent_delete('hodor:88')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'delete')
        self.assertEqual(
            url,
            '{}/v2/grids/hodor:88/permanent_delete'
            .format(self.plotly_api_domain)
        )

    def test_lookup(self):

        # requests does urlencode, so don't worry about the `' '` character!

        path = '/mah grid'
        parent = 43
        user = 'someone'
        exists = True
        grids.lookup(path=path, parent=parent, user=user, exists=exists)
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        expected_params = {'path': path, 'parent': parent, 'exists': 'true',
                           'user': user}
        self.assertEqual(method, 'get')
        self.assertEqual(
            url, '{}/v2/grids/lookup'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], expected_params)

    def test_col_create(self):
        cols = [
            {'name': 'foo', 'data': [1, 2, 3]},
            {'name': 'bar', 'data': ['b', 'a', 'r']},
        ]
        body = {'cols': _json.dumps(cols, sort_keys=True)}
        grids.col_create('hodor:88', body)
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(
            url, '{}/v2/grids/hodor:88/col'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['data'], _json.dumps(body, sort_keys=True))

    def test_col_retrieve(self):
        grids.col_retrieve('hodor:88', 'aaaaaa,bbbbbb')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'get')
        self.assertEqual(
            url, '{}/v2/grids/hodor:88/col'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], {'uid': 'aaaaaa,bbbbbb'})

    def test_col_update(self):
        cols = [
            {'name': 'foo', 'data': [1, 2, 3]},
            {'name': 'bar', 'data': ['b', 'a', 'r']},
        ]
        body = {'cols': _json.dumps(cols, sort_keys=True)}
        grids.col_update('hodor:88', 'aaaaaa,bbbbbb', body)
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'put')
        self.assertEqual(
            url, '{}/v2/grids/hodor:88/col'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], {'uid': 'aaaaaa,bbbbbb'})
        self.assertEqual(kwargs['data'], _json.dumps(body, sort_keys=True))

    def test_col_delete(self):
        grids.col_delete('hodor:88', 'aaaaaa,bbbbbb')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'delete')
        self.assertEqual(
            url, '{}/v2/grids/hodor:88/col'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], {'uid': 'aaaaaa,bbbbbb'})

    def test_row(self):
        body = {'rows': [[1, 'A'], [2, 'B']]}
        grids.row('hodor:88', body)
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(
            url, '{}/v2/grids/hodor:88/row'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['data'], _json.dumps(body, sort_keys=True))
