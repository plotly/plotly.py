import warnings
from copy import copy
from json import JSONDecodeError
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
from plotly.files import PLOTLY_DIR
from six import string_types


from atexit import register as exit_register


valid_formats = ('png', 'jpeg', 'webp', 'svg', 'pdf', 'eps')
_format_conversions = {fmt: fmt
                       for fmt in valid_formats}
_format_conversions.update({'jpg': 'jpeg'})


def _validate_coerce_format(fmt):
    assert isinstance(fmt, string_types)
    assert fmt

    fmt = fmt.lower()
    if fmt[0] == '.':
        fmt = fmt[1:]

    assert fmt in _format_conversions
    return _format_conversions[fmt]


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

    def __init__(self):
        self._props = {}
        self.restore_defaults()
        self.reload(warn=False)

    def restore_defaults(self):
        self._props.update({
            'port': None,
            'executable': 'orca',
            'timeout': 120,
            'autostart': True,
            'hostname': 'localhost',
            'default_width': None,
            'default_height': None,
            'default_format': 'png',
            'default_scale': 1
        })

    def update(self, d={}, **kwargs):
        # Combine d and kwargs
        updates = copy(d)
        updates.update(kwargs)

        # Validate keys
        for k in updates:
            if k not in self._props:
                raise ValueError('Invalid property name: {k}'.format(k=k))

        # Apply keys
        for k, v in updates.items():
            setattr(self, k, v)

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

    @property
    def default_width(self):
        return self._props.get('default_width', None)

    @default_width.setter
    def default_width(self, val):
        self._props['default_width'] = val

    @property
    def default_height(self):
        return self._props.get('default_height', None)

    @default_height.setter
    def default_height(self, val):
        self._props['default_height'] = val

    @property
    def default_format(self):
        return self._props.get('default_format', None)

    @default_format.setter
    def default_format(self, val):
        val = _validate_coerce_format(val)
        self._props['default_format'] = val

    @property
    def default_scale(self):
        return self._props.get('default_scale', None)

    @default_scale.setter
    def default_scale(self, val):
        self._props['default_scale'] = val

    @property
    def path(self):
        """
        Path to orca configuration setting file
        """
        return os.path.join(PLOTLY_DIR, ".orca")

    def reload(self, warn=True):
        """
        Reload orca settings from .plotly/.orca, if any.

        This replaces all active sett
        """

        if os.path.exists(self.path):

            # ### Load file into a string ###
            try:
                with open(self.path, 'r') as f:
                    orca_str = f.read()
            except:
                if warn:
                    warnings.warn("""\
Unable to read orca configuration file at {path}""".format(
                        path=self.path
                ))
                return

            # ### Parse as JSON ###
            try:
                orca_props = json.loads(orca_str)
            except JSONDecodeError:
                if warn:
                    warnings.warn("""\
Orca configuration file at {path} is not valid JSON""".format(
                        path=self.path
                    ))
                return

            # ### Update _props ###
            for k, v in orca_props.items():
                # Only keep properties that we understand
                if k in self._props:
                    self._props[k] = v

        elif warn:
            warnings.warn("""\
Orca configuration file at {path} not found""".format(
                path=self.path))

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self._props, f, indent=4)

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


def to_image(fig, format=None, scale=None, width=None, height=None):
    """
    Convert a figure to an image bytes string
    """
    # Make sure orca sever is running
    # -------------------------------
    ensure_orca_server()

    # Handle defaults
    # ---------------
    # Apply configuration defaults to unspecified arguments
    if format is None:
        format = config.default_format

    format = _validate_coerce_format(format)

    if scale is None:
        scale = config.default_scale

    if width is None:
        width = config.default_width

    if height is None:
        height = config.default_height

    # Request image from server
    # -------------------------
    img_data = _request_image_with_retrying(
        figure=fig, format=format, scale=scale, width=width, height=height)

    return img_data


def write_image(fig, file, format=None, scale=None, width=None, height=None):
    """
    Write image to a local file or writable object
    """

    # Check if file is a string
    # -------------------------
    file_is_str = isinstance(file, string_types)

    # Infer format if not specified
    # -----------------------------
    if file_is_str and format is None:
        _, ext = os.path.splitext(file)
        if ext:
            format = _validate_coerce_format(ext)

    # Request image
    # -------------
    # Do this first so we don't create a file if image conversion fails
    img_data = to_image(fig,
                        format=format,
                        scale=scale,
                        width=width,
                        height=height)

    # Open file
    # ---------
    if file_is_str:
        with open(file, 'wb') as f:
            f.write(img_data)
    else:
        file.write(img_data)
