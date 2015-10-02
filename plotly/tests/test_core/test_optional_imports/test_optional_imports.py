from __future__ import absolute_import

from unittest import TestCase

from plotly.optional_imports import get_module


class OptionalImportsTest(TestCase):

    def test_get_module_exists(self):
        import math
        module = get_module('math')
        self.assertIsNotNone(module)
        self.assertEqual(math, module)

    def test_get_module_exists_submodule(self):
        import requests.sessions
        module = get_module('requests.sessions')
        self.assertIsNotNone(module)
        self.assertEqual(requests.sessions, module)

    def test_get_module_does_not_exist(self):
        module = get_module('hoopla')
        self.assertIsNone(module)
