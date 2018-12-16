from __future__ import absolute_import

from mock import patch
from requests import Response

from plotly.session import sign_in
from plotly.tests.utils import PlotlyTestCase


class PlotlyApiTestCase(PlotlyTestCase):

    def mock(self, path_string):
        patcher = patch(path_string)
        new_mock = patcher.start()
        self.addCleanup(patcher.stop)
        return new_mock

    def setUp(self):

        super(PlotlyApiTestCase, self).setUp()

        self.username = 'foo'
        self.api_key = 'bar'

        self.proxy_username = 'cnet'
        self.proxy_password = 'hoopla'
        self.stream_ids = ['heyThere']

        self.plotly_api_domain = 'https://api.do.not.exist'
        self.plotly_domain = 'https://who.am.i'
        self.plotly_proxy_authorization = False
        self.plotly_streaming_domain = 'stream.does.not.exist'
        self.plotly_ssl_verification = True

        sign_in(
            username=self.username,
            api_key=self.api_key,
            proxy_username=self.proxy_username,
            proxy_password=self.proxy_password,
            stream_ids = self.stream_ids,
            plotly_domain=self.plotly_domain,
            plotly_api_domain=self.plotly_api_domain,
            plotly_streaming_domain=self.plotly_streaming_domain,
            plotly_proxy_authorization=self.plotly_proxy_authorization,
            plotly_ssl_verification=self.plotly_ssl_verification
        )

    def to_bytes(self, string):
        try:
            return string.encode('utf-8')
        except AttributeError:
            return string

    def get_response(self, content=b'', status_code=200):
        response = Response()
        response.status_code = status_code
        response._content = content
        response.encoding = 'utf-8'
        return response
