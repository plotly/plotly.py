from __future__ import absolute_import

from plotly.api.v2 import folders
from plotly.tests.test_core.test_api import PlotlyApiTestCase


class FoldersTest(PlotlyApiTestCase):

    def setUp(self):
        super(FoldersTest, self).setUp()

        # Mock the actual api call, we don't want to do network tests here.
        self.request_mock = self.mock('plotly.api.v2.utils.requests.request')
        self.request_mock.return_value = self.get_response()

        # Mock the validation function since we can test that elsewhere.
        self.mock('plotly.api.v2.utils.validate_response')

    def test_create(self):
        path = '/foo/man/bar/'
        folders.create({'path': path})
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(url, '{}/v2/folders'.format(self.plotly_api_domain))
        self.assertEqual(kwargs['data'], '{{"path": "{}"}}'.format(path))

    def test_retrieve(self):
        folders.retrieve('hodor:88')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'get')
        self.assertEqual(
            url, '{}/v2/folders/hodor:88'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], {})

    def test_retrieve_share_key(self):
        folders.retrieve('hodor:88', share_key='foobar')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'get')
        self.assertEqual(
            url, '{}/v2/folders/hodor:88'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], {'share_key': 'foobar'})

    def test_update(self):
        new_filename = '..zzZ ..zzZ'
        folders.update('hodor:88', body={'filename': new_filename})
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'put')
        self.assertEqual(
            url, '{}/v2/folders/hodor:88'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['data'],
                         '{{"filename": "{}"}}'.format(new_filename))

    def test_trash(self):
        folders.trash('hodor:88')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(
            url, '{}/v2/folders/hodor:88/trash'.format(self.plotly_api_domain)
        )

    def test_restore(self):
        folders.restore('hodor:88')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(
            url, '{}/v2/folders/hodor:88/restore'.format(self.plotly_api_domain)
        )

    def test_permanent_delete(self):
        folders.permanent_delete('hodor:88')
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'delete')
        self.assertEqual(
            url,
            '{}/v2/folders/hodor:88/permanent_delete'
            .format(self.plotly_api_domain)
        )

    def test_lookup(self):

        # requests does urlencode, so don't worry about the `' '` character!

        path = '/mah folder'
        parent = 43
        user = 'someone'
        exists = True
        folders.lookup(path=path, parent=parent, user=user, exists=exists)
        self.request_mock.assert_called_once()
        args, kwargs = self.request_mock.call_args
        method, url = args
        expected_params = {'path': path, 'parent': parent, 'exists': 'true',
                           'user': user}
        self.assertEqual(method, 'get')
        self.assertEqual(
            url, '{}/v2/folders/lookup'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], expected_params)
