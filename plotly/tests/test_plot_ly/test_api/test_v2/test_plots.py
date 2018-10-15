from __future__ import absolute_import

from plotly.api.v2 import plots
from plotly.tests.test_plot_ly.test_api import PlotlyApiTestCase


class PlotsTest(PlotlyApiTestCase):

    def setUp(self):
        super(PlotsTest, self).setUp()

        # Mock the actual api call, we don't want to do network tests here.
        self.request_mock = self.mock('plotly.api.v2.utils.requests.request')
        self.request_mock.return_value = self.get_response()

        # Mock the validation function since we can test that elsewhere.
        self.mock('plotly.api.v2.utils.validate_response')

    def test_create(self):
        filename = 'a plot'
        plots.create({'filename': filename})
        assert self.request_mock.call_count == 1
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(url, '{}/v2/plots'.format(self.plotly_api_domain))
        self.assertEqual(
            kwargs['data'], '{{"filename": "{}"}}'.format(filename)
        )

    def test_retrieve(self):
        plots.retrieve('hodor:88')
        assert self.request_mock.call_count == 1
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'get')
        self.assertEqual(
            url, '{}/v2/plots/hodor:88'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], {})

    def test_retrieve_share_key(self):
        plots.retrieve('hodor:88', share_key='foobar')
        assert self.request_mock.call_count == 1
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'get')
        self.assertEqual(
            url, '{}/v2/plots/hodor:88'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], {'share_key': 'foobar'})

    def test_update(self):
        new_filename = '..zzZ ..zzZ'
        plots.update('hodor:88', body={'filename': new_filename})
        assert self.request_mock.call_count == 1
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'put')
        self.assertEqual(
            url, '{}/v2/plots/hodor:88'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['data'],
                         '{{"filename": "{}"}}'.format(new_filename))

    def test_trash(self):
        plots.trash('hodor:88')
        assert self.request_mock.call_count == 1
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(
            url, '{}/v2/plots/hodor:88/trash'.format(self.plotly_api_domain)
        )

    def test_restore(self):
        plots.restore('hodor:88')
        assert self.request_mock.call_count == 1
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'post')
        self.assertEqual(
            url, '{}/v2/plots/hodor:88/restore'.format(self.plotly_api_domain)
        )

    def test_permanent_delete(self):
        plots.permanent_delete('hodor:88')
        assert self.request_mock.call_count == 1
        args, kwargs = self.request_mock.call_args
        method, url = args
        self.assertEqual(method, 'delete')
        self.assertEqual(
            url,
            '{}/v2/plots/hodor:88/permanent_delete'
            .format(self.plotly_api_domain)
        )

    def test_lookup(self):

        # requests does urlencode, so don't worry about the `' '` character!

        path = '/mah plot'
        parent = 43
        user = 'someone'
        exists = True
        plots.lookup(path=path, parent=parent, user=user, exists=exists)
        assert self.request_mock.call_count == 1
        args, kwargs = self.request_mock.call_args
        method, url = args
        expected_params = {'path': path, 'parent': parent, 'exists': 'true',
                           'user': user}
        self.assertEqual(method, 'get')
        self.assertEqual(
            url, '{}/v2/plots/lookup'.format(self.plotly_api_domain)
        )
        self.assertEqual(kwargs['params'], expected_params)
