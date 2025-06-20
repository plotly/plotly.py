from unittest import TestCase
from plotly.optional_imports import get_module


class OptionalImportsTest(TestCase):
    def test_get_module_exists(self):
        import math

        module = get_module("math")
        self.assertIsNotNone(module)
        self.assertEqual(math, module)

    def test_get_module_exists_submodule(self):
        import requests.sessions

        module = get_module("requests.sessions")
        self.assertIsNotNone(module)
        self.assertEqual(requests.sessions, module)

    def test_get_module_does_not_exist(self):
        module = get_module("hoopla")
        self.assertIsNone(module)

    def test_get_module_import_exception(self):
        # Get module that raises an exception on import
        module_str = "tests.test_core.test_optional_imports.exploding_module"

        with self.assertLogs("_plotly_utils.optional_imports", level="ERROR") as cm:
            module = get_module(module_str)

        # No exception should be raised and None should be returned
        self.assertIsNone(module)

        # Check logging level and log message
        expected_start = (
            "ERROR:_plotly_utils.optional_imports:"
            "Error importing optional module " + module_str
        )
        self.assertEqual(cm.output[0][: len(expected_start)], expected_start)

        # Check that exception message is included after log message
        expected_end = "Boom!"
        self.assertEqual(cm.output[0][-len(expected_end) :], expected_end)
