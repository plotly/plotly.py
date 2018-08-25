from unittest import TestCase
import plotly.io as pio
import subprocess
import os
from distutils.version import LooseVersion
import requests
import time
import psutil
import pytest


# Fixtures
# --------
@pytest.fixture()
def setup():
    # Reset orca state
    pio.orca.reset_status()
    pio.orca.config.restore_defaults()


# Run setup before every test function in this file
pytestmark = pytest.mark.usefixtures("setup")


# Utilities
# ---------
def ping_pongs(server_url):
    try:
        response = requests.post(server_url + '/ping')
    except requests.exceptions.ConnectionError:
        # Expected
        return False

    return (response.status_code == 200 and
            response.content.decode('utf-8') == 'pong')


def test_validate_orca():
    assert pio.orca.status.state == 'unvalidated'
    pio.orca.validate_executable()
    assert pio.orca.status.state == 'validated'


def test_orca_not_found():
    pio.orca.config.executable = 'bogus'
    with pytest.raises(ValueError) as err:
        pio.orca.validate_executable()
    assert pio.orca.status.state == 'unvalidated'
    assert 'could not be found' in str(err.value)


def test_invalid_executable_found():
    pio.orca.config.executable = 'python'
    with pytest.raises(ValueError) as err:
        pio.orca.validate_executable()

    assert pio.orca.status.state == 'unvalidated'
    assert 'executable that was found at' in str(err.value)


def test_orca_executable_path():
    assert pio.orca.status.executable is None
    if os.name == 'nt':  # Windows
        expected = subprocess.check_output(['where', 'orca']
                                           ).decode('utf-8').strip()
    else:  # Linux / OS X
        expected = subprocess.check_output(['which', 'orca']
                                           ).decode('utf-8').strip()

    pio.orca.validate_executable()
    assert pio.orca.status.executable == expected


def test_orca_version_number():
    assert pio.orca.status.version is None

    expected_min = LooseVersion('1.1.0')
    expected_max = LooseVersion('2.0.0')

    pio.orca.validate_executable()
    version = LooseVersion(pio.orca.status.version)

    assert expected_min <= version
    assert version < expected_max


def test_ensure_orca_ping_and_proc():
    pio.orca.config.timeout = None

    assert pio.orca.status.port is None
    assert pio.orca.status.pid is None

    pio.orca.ensure_server()

    assert pio.orca.status.port is not None
    assert pio.orca.status.pid is not None
    server_port = pio.orca.status.port
    server_pid = pio.orca.status.pid

    # Make sure server has time to start up
    time.sleep(10)

    # Check that server process number is valid
    assert psutil.pid_exists(server_pid)

    # Build server URL
    server_url = 'http://localhost:%s' % server_port

    # ping server
    assert ping_pongs(server_url)

    # shut down server
    pio.orca.shutdown_server()

    # Check that server process number no longer exists
    assert not psutil.pid_exists(server_pid)

    # Check that ping is no longer answered
    assert not ping_pongs(server_url)


def test_server_timeout_shutdown():

    # Configure server to shutdown after 10 seconds without
    # calls to ensure_orca_server
    pio.orca.config.timeout = 10
    pio.orca.ensure_server()
    server_port = pio.orca.status.port
    server_pid = pio.orca.status.pid

    # Build server URL
    server_url = 'http://localhost:%s' % server_port

    # Check that server process number is valid
    assert psutil.pid_exists(server_pid)

    for i in range(3):
        # Sleep for just under 10 seconds
        time.sleep(8)
        assert ping_pongs(server_url)
        assert psutil.pid_exists(server_pid)
        pio.orca.ensure_server()

    # Sleep just over 10 seconds, server should then auto shutdown
    time.sleep(11)

    # Check that server process number no longer exists
    assert not psutil.pid_exists(server_pid)

    # Check that ping is no longer answered
    assert not ping_pongs(server_url)
