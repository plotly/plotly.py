import unittest
import os
import errno
import time
import ssl

from nose.tools import assert_raises

# from chunked_requests import
from chunked_requests.chunked_requests import Stream


class Test(unittest.TestCase):
    def setUp(self):
        pass
        # stream = Stream('127.0.0.1', port=8080)

    def test_successful_write(self):
        ''' Test that data was successfully
        written to the server.
        '''

        _remove_file('request.txt')

        stream = Stream('127.0.0.1',
                        port=8080,
                        url='/successful_write')

        body = 'request-body'*10
        stream.write(body)
        time.sleep(1)
        with open('request.txt', 'r') as f:
            body_from_file = f.read()

        assert(body_from_file == body)

        _remove_file('request.txt')

    def test_reconnect_on_408_timeout(self):
        ''' Test that `reconnect_on` indeed
        reconnects on a `408` timeout response
        from the server after 5 seconds and
        continues to write data. Test that
        all of the data was transmitted, even
        with a broken connection and re-connect.
        '''

        _remove_file('request.txt')

        stream = Stream('127.0.0.1',
                        port=8080,
                        url='/5s_timeout')

        for i in range(8):
            stream.write(str(i),
                         reconnect_on=('', 200, 408))
            time.sleep(1)

        with open('request.txt', 'r') as f:
            body_from_file = f.read()

        body_sent = ''.join([str(i) for i in range(8)])
        assert(body_from_file == body_sent)
        _remove_file('request.txt')

    def test_failure_on_408_timeout(self):
        ''' Test that an error is thrown when
        the server returns a 408 timeout and
        we choose not to reconnect.
        '''

        with assert_raises(Exception) as cm:
            stream = Stream('127.0.0.1',
                            port=8080,
                            url='/5s_timeout')

            for i in range(8):
                stream.write(str(i),
                             reconnect_on=('', 200))
                time.sleep(1)

        ex = cm.exception
        assert(ex.message == "Server responded "
                             "with status code: 408\n"
                             "and message: "
                             "timeout on active data.")

    def test_huge_request_on_latent_server(self):
        _remove_file('request.txt')

        stream = Stream('127.0.0.1',
                        port=9008)
        body = 'x' * (5000 * 1000)
        stream.write(body)

        # Proxy servers delays the response for 10 seconds
        # Writing 5 mill chars takes a bit, so wait a few
        # extra secs before comparing
        time.sleep(13)
        with open('request.txt', 'r') as f:
            body_from_file = f.read()

        assert(body_from_file == body)

        _remove_file('request.txt')

    def test__get_proxy_config(self):

        stream = Stream('127.0.0.1', port=8080)

        # http_proxy is not set
        # --> proxy_server and proxy_port should not be set
        proxy_server, proxy_port = stream._get_proxy_config()
        self.assertIsNone(proxy_server)
        self.assertIsNone(proxy_port)

        # set proxy env. variable
        os.environ['http_proxy'] = 'http://test:123'

        # http_proxy is set
        # --> proxy_server and proxy_port should be set
        proxy_server, proxy_port = stream._get_proxy_config()
        self.assertEqual(proxy_server, 'test')
        self.assertEqual(proxy_port, 123)

        # no_proxy is set but url is not in no_proxy
        # --> proxy_server and proxy_port should be set
        os.environ['no_proxy'] = 'some_url, other_url'
        proxy_server, proxy_port = stream._get_proxy_config()
        self.assertEqual(proxy_server, 'test')
        self.assertEqual(proxy_port, 123)

        # http_proxy and no_proxy are set and url is in no_proxy
        # --> proxy_server and proxy_port should not be set
        os.environ['no_proxy'] = 'some_url, {}, other_url'.format(
            stream._server
        )
        proxy_server, proxy_port = stream._get_proxy_config()
        self.assertIsNone(proxy_server)
        self.assertIsNone(proxy_port)

        # unset env variables
        os.environ.pop('http_proxy')
        os.environ.pop('no_proxy')

    def test__get_proxy_config_with_ssl(self):

        stream = Stream('127.0.0.1', port=8080)

        # we actually still have an http connection here, but we're faking https
        # to test the expected proxy behaviour
        stream._ssl_enabled = True

        # https_proxy is not set
        # --> proxy_server and proxy_port should not be set
        proxy_server, proxy_port = stream._get_proxy_config()
        self.assertIsNone(proxy_server)
        self.assertIsNone(proxy_port)

        # set proxy env. variable
        os.environ['https_proxy'] = 'https://test:123'

        # https_proxy is set
        # --> proxy_server and proxy_port should be set
        proxy_server, proxy_port = stream._get_proxy_config()
        self.assertEqual(proxy_server, 'test')
        self.assertEqual(proxy_port, 123)

    def test__get_ssl_context(self):

        stream = Stream('127.0.0.1', port=8080)

        # we actually still have an http connection here, but we're faking https
        # to test the expected proxy behaviour
        stream._ssl_enabled = True

        # if ssl verification is enabled (default), context=None expected
        context = stream._get_ssl_context()
        self.assertIsNone(context)

        # if ssl verification is disabled, SSLContext expected
        stream._ssl_verification_enabled = False
        context = stream._get_ssl_context()
        self.assertIsInstance(context, ssl.SSLContext)


def _remove_file(filename):
    try:
        os.remove(filename)
    except OSError as e:
         # errno.ENOENT = no such file or directory
        if e.errno != errno.ENOENT:
            raise e


if __name__ == '__main__':
    unittest.main()
