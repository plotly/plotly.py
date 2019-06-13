import time
import six
import os
import ssl

from six.moves import http_client
from six.moves.urllib.parse import urlparse


class Stream:
    def __init__(self, server, port=80, headers={}, url='/', ssl_enabled=False,
                 ssl_verification_enabled=True):
        ''' Initialize a stream object and an HTTP or HTTPS connection
        with chunked Transfer-Encoding to server:port with optional headers.
        '''
        self.maxtries = 5
        self._tries = 0
        self._delay = 1
        self._closed = False
        self._server = server
        self._port = port
        self._headers = headers
        self._url = url
        self._ssl_enabled = ssl_enabled
        self._ssl_verification_enabled = ssl_verification_enabled
        self._connect()

    def write(self, data, reconnect_on=('', 200, )):
        ''' Send `data` to the server in chunk-encoded form.
        Check the connection before writing and reconnect
        if disconnected and if the response status code is in `reconnect_on`.

        The response may either be an HTTPResponse object or an empty string.
        '''

        if not self._isconnected():

            # Attempt to get the response.
            response = self._getresponse()

            # Reconnect depending on the status code.
            if ((response == '' and '' in reconnect_on) or
                (response and isinstance(response, http_client.HTTPResponse) and
                 response.status in reconnect_on)):
                self._reconnect()

            elif response and isinstance(response, http_client.HTTPResponse):
                # If an HTTPResponse was recieved then
                # make the users aware instead of
                # auto-reconnecting in case the
                # server is responding with an important
                # message that might prevent
                # future requests from going through,
                # like Invalid Credentials.
                # This allows the user to determine when
                # to reconnect.
                raise Exception("Server responded with "
                                "status code: {status_code}\n"
                                "and message: {msg}."
                                .format(status_code=response.status,
                                        msg=response.read()))

            elif response == '':
                raise Exception("Attempted to write but socket "
                                "was not connected.")

        try:
            msg = data
            msglen = format(len(msg), 'x')  # msg length in hex
            # Send the message in chunk-encoded form
            self._conn.sock.setblocking(1)
            self._conn.send('{msglen}\r\n{msg}\r\n'
                            .format(msglen=msglen, msg=msg).encode('utf-8'))
            self._conn.sock.setblocking(0)
        except http_client.socket.error:
            self._reconnect()
            self.write(data)

    def _get_proxy_config(self):
        """
        Determine if self._url should be passed through a proxy. If so, return
        the appropriate proxy_server and proxy_port. Assumes https_proxy is used
        when ssl_enabled=True.

        """

        proxy_server = None
        proxy_port = None
        ssl_enabled = self._ssl_enabled

        if ssl_enabled:
            proxy = os.environ.get("https_proxy")
        else:
            proxy = os.environ.get("http_proxy")
        no_proxy = os.environ.get("no_proxy")
        no_proxy_url = no_proxy and self._server in no_proxy

        if proxy and not no_proxy_url:
            p = urlparse(proxy)
            proxy_server = p.hostname
            proxy_port = p.port

        return proxy_server, proxy_port

    def _get_ssl_context(self):
        """
        Return an unverified context if ssl verification is disabled.

        """

        context = None

        if not self._ssl_verification_enabled:
            context = ssl._create_unverified_context()

        return context

    def _connect(self):
        ''' Initialize an HTTP/HTTPS connection with chunked Transfer-Encoding
        to server:port with optional headers.
        '''
        server = self._server
        port = self._port
        headers = self._headers
        ssl_enabled = self._ssl_enabled
        proxy_server, proxy_port = self._get_proxy_config()

        if (proxy_server and proxy_port):
            if ssl_enabled:
                context = self._get_ssl_context()
                self._conn = http_client.HTTPSConnection(
                    proxy_server, proxy_port, context=context
                )
            else:
                self._conn = http_client.HTTPConnection(
                    proxy_server, proxy_port
                )
            self._conn.set_tunnel(server, port)
        else:
            if ssl_enabled:
                context = self._get_ssl_context()
                self._conn = http_client.HTTPSConnection(
                    server, port, context=context
                )
            else:
                self._conn = http_client.HTTPConnection(server, port)

        self._conn.putrequest('POST', self._url)
        self._conn.putheader('Transfer-Encoding', 'chunked')
        for header in headers:
            self._conn.putheader(header, headers[header])
        self._conn.endheaders()

        # Set blocking to False prevents recv
        # from blocking while waiting for a response.
        self._conn.sock.setblocking(False)
        self._bytes = six.b('')
        self._reset_retries()
        time.sleep(0.5)

    def close(self):
        ''' Close the connection to server.

        If available, return a http_client.HTTPResponse object.

        Closing the connection involves sending the
        Transfer-Encoding terminating bytes.
        '''
        self._reset_retries()
        self._closed = True

        # Chunked-encoded posts are terminated with '0\r\n\r\n'
        # For some reason, either Python or node.js seems to
        # require an extra \r\n.
        try:
            self._conn.send('\r\n0\r\n\r\n'.encode('utf-8'))
        except http_client.socket.error:
            # In case the socket has already been closed
            return ''

        return self._getresponse()

    def _getresponse(self):
        ''' Read from recv and return a HTTPResponse object if possible.
        Either
        1 - The client has succesfully closed the connection: Return ''
        2 - The server has already closed the connection: Return the response
            if possible.
        '''
        # Wait for a response
        self._conn.sock.setblocking(True)
        # Parse the response
        response = self._bytes
        while True:
            try:
                _bytes = self._conn.sock.recv(1)
            except http_client.socket.error:
                # For error 54: Connection reset by peer
                # (and perhaps others)
                return six.b('')
            if _bytes == six.b(''):
                break
            else:
                response += _bytes
        # Set recv to be non-blocking again
        self._conn.sock.setblocking(False)

        # Convert the response string to a http_client.HTTPResponse
        # object with a bit of a hack
        if response != six.b(''):
            # Taken from
            # http://pythonwise.blogspot.ca/2010/02/parse-http-response.html
            try:
                response = http_client.HTTPResponse(_FakeSocket(response))
                response.begin()
            except:
                # Bad headers ... etc.
                response = six.b('')
        return response

    def _isconnected(self):
        ''' Return True if the socket is still connected
        to the server, False otherwise.

        This check is done in 3 steps:
        1 - Check if we have closed the connection
        2 - Check if the original socket connection failed
        3 - Check if the server has returned any data. If they have,
            assume that the server closed the response after they sent
            the data, i.e. that the data was the HTTP response.
        '''

        # 1 - check if we've closed the connection.
        if self._closed:
            return False

        # 2 - Check if the original socket connection failed
        # If this failed, then no socket was initialized
        if self._conn.sock is None:
            return False

        try:
            # 3 - Check if the server has returned any data.
            # If they have, then start to store the response
            # in _bytes.
            self._bytes = six.b('')
            self._bytes = self._conn.sock.recv(1)
            return False
        except http_client.socket.error as e:
            # Check why recv failed
            # Windows machines are the error codes
            # that start with 1
            # (http://msdn.microsoft.com/en-ca/library/windows/desktop/ms740668(v=vs.85).aspx)
            if e.errno == 35 or e.errno == 10035:
                # This is the "Resource temporarily unavailable" error
                # which is thrown cuz there was nothing to receive, i.e.
                # the server hasn't returned a response yet.
                # This is a non-fatal error and the operation
                # should be tried again.
                # So, assume that the connection is still open.
                return True
            elif e.errno == 54 or e.errno == 10054:
                # This is the "Connection reset by peer" error
                # which is thrown cuz the server reset the
                # socket, so the connection is closed.
                return False
            elif e.errno == 11:
                # This is the "Resource temporarily unavailable" error
                # which happens because the "operation would have blocked
                # but nonblocking operation was requested".
                # We require non-blocking reading of this socket because
                # we don't want to wait around for a response, we just
                # want to see if a response is currently available. So
                # let's just assume that we're still connected and
                # hopefully recieve some data on the next try.
                return True
            elif isinstance(e, ssl.SSLError):
                if e.errno == 2:
                    # errno 2 occurs when trying to read or write data, but more
                    # data needs to be received on the underlying TCP transport
                    # before the request can be fulfilled.
                    #
                    # Python 2.7.9+ and Python 3.3+ give this its own exception,
                    # SSLWantReadError
                    return True
                raise e
            else:
                # Unknown scenario
                raise e

    def _reconnect(self):
        ''' Connect if disconnected.
        Retry self.maxtries times with delays
        '''
        if not self._isconnected():
            try:
                self._connect()
            except http_client.socket.error as e:
                # Attempt to reconnect if the connection was refused
                if e.errno == 61 or e.errno == 10061:
                    # errno 61 is the "Connection Refused" error
                    time.sleep(self._delay)
                    self._delay += self._delay  # fibonacii delays
                    self._tries += 1
                    if self._tries < self.maxtries:
                        self._reconnect()
                    else:
                        self._reset_retries()
                        raise e
                else:
                    # Unknown scenario
                    raise e

        # Reconnect worked - reset _closed
        self._closed = False

    def _reset_retries(self):
        ''' Reset the connect counters and delays
        '''
        self._tries = 0
        self._delay = 1


class _FakeSocket(six.StringIO):
    # Used to construct a http_client.HTTPResponse object
    # from a string.
    # Thx to: http://pythonwise.blogspot.ca/2010/02/parse-http-response.html
    def makefile(self, *args, **kwargs):
        return self
