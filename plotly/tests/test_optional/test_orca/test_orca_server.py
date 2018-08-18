from unittest import TestCase
import plotly.io as pio
import subprocess
import os
from distutils.version import LooseVersion
import requests
import time
import psutil


def ping_pongs(server_url):
    try:
        response = requests.post(server_url + '/ping')
    except requests.exceptions.ConnectionError:
        # Expected
        return False

    return (response.status_code == 200 and
            response.content.decode('utf-8') == 'pong')


class OrcaServerValidationAndManagement(TestCase):
    def setUp(self):
        pio.orca.reset_orca_status()
        pio.orca.config.restore_defaults()

    def test_validate_orca(self):
        self.assertEqual(pio.orca.status.state, 'unvalidated')
        pio.orca.validate_orca_executable()
        self.assertEqual(pio.orca.status.state, 'validated')

    def test_orca_not_found(self):
        pio.orca.config.executable = 'bogus'
        with self.assertRaises(ValueError) as err:
            pio.orca.validate_orca_executable()

        self.assertEqual(pio.orca.status.state, 'unvalidated')
        self.assertIn('could not be found', err.exception.args[0])

    def test_invalid_executable_found(self):
        pio.orca.config.executable = 'cd'
        with self.assertRaises(ValueError) as err:
            pio.orca.validate_orca_executable()

        self.assertEqual(pio.orca.status.state, 'unvalidated')
        self.assertIn('executable that was found at', err.exception.args[0])

    def test_orca_executable_path(self):
        self.assertIsNone(pio.orca.status.executable)
        if os.name == 'nt':  # Windows
            expected = subprocess.check_output(['where', 'orca']
                                               ).decode('utf-8').strip()
        else:  # Linux / OS X
            expected = subprocess.check_output(['which', 'orca']
                                               ).decode('utf-8').strip()

        pio.orca.validate_orca_executable()
        self.assertEqual(pio.orca.status.executable, expected)

    def test_orca_version_number(self):
        self.assertIsNone(pio.orca.status.version)

        expected_min = LooseVersion('1.1.0rc1')
        expected_max = LooseVersion('2.0.0')

        pio.orca.validate_orca_executable()
        version = LooseVersion(pio.orca.status.version)

        self.assertGreaterEqual(expected_min, version)
        self.assertLess(version, expected_max)

    def test_ensure_orca_ping_and_proc(self):
        pio.orca.config.timeout = None

        self.assertIsNone(pio.orca.status.port)
        self.assertIsNone(pio.orca.status.pid)

        pio.orca.ensure_orca_server()

        self.assertIsNotNone(pio.orca.status.port)
        self.assertIsNotNone(pio.orca.status.pid)
        server_port = pio.orca.status.port
        server_pid = pio.orca.status.pid

        # Make sure server has time to start up
        time.sleep(5)

        # Check that server process number is valid
        self.assertTrue(psutil.pid_exists(server_pid))

        # Build server URL
        server_url = 'http://localhost:%s' % server_port

        # ping server
        self.assertTrue(ping_pongs(server_url))

        # shut down server
        pio.orca.shutdown_orca_server()

        # Check that server process number no longer exists
        self.assertFalse(psutil.pid_exists(server_pid))

        # Check that ping is no longer answered
        self.assertFalse(ping_pongs(server_url))

    def test_server_timeout_shutdown(self):

        # Configure server to shutdown after 10 seconds without
        # calls to ensure_orca_server
        pio.orca.config.timeout = 10
        pio.orca.ensure_orca_server()
        server_port = pio.orca.status.port
        server_pid = pio.orca.status.pid

        # Build server URL
        server_url = 'http://localhost:%s' % server_port

        # Check that server process number is valid
        self.assertTrue(psutil.pid_exists(server_pid))

        for i in range(3):
            # Sleep for just under 10 seconds
            time.sleep(8)
            self.assertTrue(ping_pongs(server_url))
            self.assertTrue(psutil.pid_exists(server_pid))
            pio.orca.ensure_orca_server()

        # Sleep just over 10 seconds, server should then auto shutdown
        time.sleep(11)

        # Check that server process number no longer exists
        self.assertFalse(psutil.pid_exists(server_pid))

        # Check that ping is no longer answered
        self.assertFalse(ping_pongs(server_url))
