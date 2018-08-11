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

def which(cmd):
    import shutil
    # TODO: this doesn't exist on Python 2.7 :-(
    return shutil.which(cmd)

class OrcaConfig(object):
    """
    Contains user defined configuration for orca

    These should eventually be loaded from somewhere in the ~/.plotly
    directory.
    """
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


class OrcaStatus(object):
    """
    Class to store information about the current status of the orca server.

    This class is intended to be updated only by the _orca module, and
    viewed by the user
    """
    _props = {
        'state': 'unvalidated', # or 'validated' or 'running'
        'executable': None,
        'version': None,
        'pid': None,
        'port': None
    }

    @property
    def state(self):
        """
        A string representing the state of the orca server process

        One of:
          - unvalidated: The orca executable has not yet been searched for or
            tested for validity
          - verified: The orca executable has been located and tested for
            validity, but is not running
          - running: The orca server process is currently running

        """
        return self._props['state']

    @property
    def executable(self):
        """
        If the `state` is 'validated' or 'running', this property contains the
        full path to the orca executable.  This path can be specified
        explicitly by setting the `executable` property of the
        `plotly.io.orca.config` object.
        """
        return self._props['executable']

    @property
    def version(self):
        """
        The version of the verified orca executable, if any. This property
        will be None if the `state` is 'unvalidated'
        """
        return self._props['version']


    @property
    def pid(self):
        """
        The process id of the orca server process, if any. This property
        will be None if the `state` is not 'running'
        """
        return self._props['pid']


    @property
    def port(self):
        """
        The port number that the orca server process is listening to, if any.
        This property will be None if the `state` is not 'running'
        """
        return self._props['port']

    def __repr__(self):
        return """\
    orca status
    -----------
""" + pformat(self._props, width=40)


status = OrcaStatus()
del OrcaStatus


def validate_orca_executable():
    if status.state != 'unvalidated':
        # Nothing more to do
        return

    # Try to find an executable named orca
    # ------------------------------------
    executable = which(config.executable)
    if executable is None:
        raise ValueError("""
The orca executable could not be found on the system path.

If you havne't installed orca...

If you have already installed orca, make sure the orca executable is on your
system path. Or specify the orca path explicitly in the executable property
of the plotly.io.orca.config configuration object.""")

    # Run executable with --help and see if it's our orca
    # ---------------------------------------------------
    invalid_executable_msg = "Invalid orca executable at..."
    try:
        help_result = subprocess.check_output([executable, '--help'])
    except subprocess.CalledProcessError:
        raise ValueError(invalid_executable_msg)

    if not help_result:
        raise ValueError(invalid_executable_msg)

    if 'plotly' not in help_result.decode('utf-8').lower():
        raise ValueError(invalid_executable_msg)

    # Get orca version
    # ----------------
    try:
        orca_version = subprocess.check_output([executable, '--version'])
    except subprocess.CalledProcessError:
        raise ValueError("version failed")

    if not orca_version:
        raise ValueError("No version reported")
    else:
        orca_version = orca_version.decode()

    # Check version >= 1.1.0 so we have --graph-only support.
    status._props['executable'] = executable
    status._props['version'] = orca_version.strip()
    status._props['state'] = 'validated'


def reset_orca_status():
    shutdown_orca_server()
    status._props['executable'] = None
    status._props['version'] = None
    status._props['state'] = 'unvalidated'


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

                    child_status = __orca_state['proc'].wait()

                    __orca_state['proc'] = None
                    __orca_state['shutdown_timer'].cancel()
                    __orca_state['shutdown_timer'] = None
                    __orca_state['port'] = None

                    # Update status
                    status._props['state'] = 'validated'
                    status._props['pid'] = None
                    status._props['port'] = None
                except:
                    pass


# Launch or get server
def ensure_orca_server():
    if status.state == 'unvalidated':
        validate_orca_executable()

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

            # Update status
            status._props['state'] = 'running'
            status._props['pid'] = __orca_state['proc'].pid
            status._props['port'] = __orca_state['port']

        t = threading.Timer(config.timeout, shutdown_orca_server)
        t.start()
        __orca_state['shutdown_timer'] = t


@retrying.retry(wait_random_min=5, wait_random_max=10, stop_max_delay=10000)
def _request_image_with_retrying(**kwargs):
    server_url = 'http://{hostname}:{port}'.format(
        hostname=config.hostname, port=__orca_state['port'])

    request_params = {k: v for k, v, in kwargs.items() if v is not None}
    json_str = json.dumps(request_params, cls=plotly.utils.PlotlyJSONEncoder)
    r = requests.post(server_url + '/', data=json_str)
    return r.content


def to_image(fig, format='png', scale=1.0, width=None, height=None):
    """
    Convert a figure to an image bytes string
    """
    ensure_orca_server()
    return _request_image_with_retrying(
        figure=fig, format=format, scale=scale, width=width, height=height)
