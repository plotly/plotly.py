from __future__ import absolute_import

from unittest import TestCase

from plotly.tools import get_config_defaults, _FILE_CONTENT, CONFIG_FILE


class TestGetConfigDefaults(TestCase):

    def test_config_dict_is_equivalent_copy(self):

        original = _FILE_CONTENT[CONFIG_FILE]
        copy = get_config_defaults()
        self.assertIsNot(copy, original)
        self.assertEqual(copy, original)
