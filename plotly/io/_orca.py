from pprint import pformat
import requests
import subprocess
import socket
import json
import os
import threading
import signal
import retrying
import atexit

import plotly

def _find_open_port():
    """
    Use socket module to find an open port
    """
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', 0))
        _, port = s.getsockname()

    return port

class OrcaConfig(object):
    _props = {
        'port': None,
        'hostname': 'localhost',
        'executable': 'orca',
        'autostart': True,
        'timeout': 120
    }

    @property
    def port(self):
        return self._props.get('port', None)

    @port.setter
    def port(self, val):
        if isinstance(val, int):
            val = str(val)
        # Must be integer or string that contains an integer
        self._props['port'] = val

    @property
    def hostname(self):
        return self._props.get('hostname', None)

    @hostname.setter
    def hostname(self, val):
        self._props['hostname'] = val

    @property
    def executable(self):
        return self._props.get('executable', None)

    @executable.setter
    def executable(self, val):
        self._props['executable'] = val

    @property
    def autostart(self):
        return self._props.get('autostart', None)

    @autostart.setter
    def autostart(self, val):
        # - Must be string
        # - Hostname must be localhost
        self._props['autostart'] = val

    @property
    def timeout(self):
        return self._props.get('timeout', None)

    @timeout.setter
    def timeout(self, val):
        # - Must be number
        self._props['timeout'] = val

    def __repr__(self):
        return """\
orca configuration
------------------
""" + pformat(self._props, width=40)


config = OrcaConfig()
del OrcaConfig

# Initialze process control
__orca_lock = threading.Lock()
__orca_state = {'proc': None,
                'shutdown_timer': None}


@atexit.register
def shutdown_orca_server():
    if __orca_state['proc'] is not None:
        with __orca_lock:
            if __orca_state['proc'] is not None:
                try:
                    if os.name == 'nt':
                        __orca_state['proc'].send_signal(
                            signal.CTRL_BREAK_EVENT)  # Windows
                    else:
                        __orca_state['proc'].terminate()  # Unix

                    __orca_state['proc'] = None
                    __orca_state['shutdown_timer'].cancel()
                    __orca_state['shutdown_timer'] = None
                    __orca_state['port'] = None
                except:
                    pass


# Launch or get server
def ensure_orca_server():
    with __orca_lock:
        if __orca_state['shutdown_timer'] is not None:
            __orca_state['shutdown_timer'].cancel()

        if config.autostart and __orca_state['proc'] is None:
            if config.port is None:
                __orca_state['port'] = str(_find_open_port())
            else:
                __orca_state['port'] = config.port

            if os.name == 'nt':
                creationflags = subprocess.CREATE_NEW_PROCESS_GROUP
            else:
                creationflags = 0

            __orca_state['proc'] = subprocess.Popen(
                [config.executable, 'serve', '-p', __orca_state['port'],
                 '--graph-only'],
                creationflags=creationflags)

        t = threading.Timer(config.timeout, shutdown_orca_server)
        t.start()
        __orca_state['shutdown_timer'] = t


@retrying.retry(wait_random_min=5, wait_random_max=10, stop_max_delay=10000)
def _request_image_with_retrying(fig):
    server_url = 'http://{hostname}:{port}'.format(
        hostname=config.hostname, port=__orca_state['port'])
    json_str = json.dumps({'figure': fig}, cls=plotly.utils.PlotlyJSONEncoder)
    r = requests.post(server_url + '/', data=json_str)
    return r.content


def to_image(fig):
    """
    Convert a figure to an image bytes string
    """
    ensure_orca_server()
    return _request_image_with_retrying(fig)