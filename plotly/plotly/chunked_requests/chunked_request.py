import time
import httplib
import StringIO


class Stream:
    def __init__(self, server, port=80, headers={}):
        ''' Initialize a stream object and an HTTP Connection
        with chunked Transfer-Encoding to server:port with optional headers.
        '''
        self.maxtries = 5
        self._tries = 0
        self._delay = 1
        self._closed = False
        self._server = server
        self._port = port
        self._headers = headers
        self._connect()

    def write(self, data, reconnect=True):
        ''' Send `data` to the server in chunk-encoded form.
        If `reconnect` is `True`, check the connection to the server before
        writing, and reconnect if disconnected.
        '''

        if not self._isconnected():
            if reconnect:
                self._reconnect()
            else:
                raise Exception("Socket is closed, "
                                "cannot write to a closed socket.")
        try:
            msg = data
            msglen = format(len(msg), 'x')  # msg length in hex
            # Send the message in chunk-encoded form
            self._conn.send('{msglen}\r\n{msg}\r\n'
                            .format(msglen=msglen, msg=msg))
        except httplib.socket.error as e:
            if reconnect:
                self._reconnect()
                self.write(data)
            else:
                raise e

    def _connect(self):
        ''' Initialize an HTTP connection with chunked Transfer-Encoding
        to server:port with optional headers.
        '''
        server = self._server
        port = self._port
        headers = self._headers
        self._conn = httplib.HTTPConnection(server, port)

        self._conn.putrequest('POST', '/')
        self._conn.putheader('Transfer-Encoding', 'chunked')
        for header in headers:
            self._conn.putheader(header, headers[header])
        self._conn.endheaders()

        # Set blocking to False prevents recv
        # from blocking while waiting for a response.
        self._conn.sock.setblocking(False)

        self._reset_retries()

    def close(self):
        ''' Close the connection to server.

        If available, return a httplib.HTTPResponse object.

        Closing the connection involves sending the
        Transfer-Encoding terminating bytes.
        '''
        self._reset_retries()
        self._closed = True

        # Chunked-encoded posts are terminated with '0\r\n\r\n'
        # For some reason, either Python or node.js seems to
        # require an extra \r\n.
        try:
            self._conn.send('\r\n0\r\n\r\n')
        except httplib.socket.error:
            # In case the socket has already been closed
            return ''

        # Wait for a response
        self._conn.sock.setblocking(True)
        # Parse the response
        response = ''
        while True:
            try:
                bytes = self._conn.sock.recv(1)
            except httplib.socket.error:
                # For error 54: Connection reset by peer
                # (and perhaps others)
                return ''
            if bytes == '':
                break
            else:
                response += bytes
        # Set recv to be non-blocking again
        self._conn.sock.setblocking(False)

        # Convert the response string to a httplib.HTTPResponse
        # object with a bit of a hack
        if response != '':
            # Taken from
            # http://pythonwise.blogspot.ca/2010/02/parse-http-response.html
            try:
                response = httplib.HTTPResponse(_FakeSocket(response))
                response.begin()
            except:
                # Bad headers ... etc.
                # Whatever. the important part is that we closed
                # the socket.
                response = ''
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
            self._bytes = self._conn.sock.recv(1)
            return False
        except httplib.socket.error as e:
            # Check if recv failed because there was nothing to receive,
            # this is the "Resource temporarily unavailable" error
            if e.errno == 35:
                # The server hasn't yet returned a response, so assume that
                # the connection is still open.
                return True
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
            except httplib.socket.error as e:
                # Attempt to reconnect if the connection was refused
                if e.errno == 61:
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


class _FakeSocket(StringIO.StringIO):
    # Used to construct a httplib.HTTPResponse object
    # from a string.
    # Thx to: http://pythonwise.blogspot.ca/2010/02/parse-http-response.html
    def makefile(self, *args, **kwargs):
        return self
