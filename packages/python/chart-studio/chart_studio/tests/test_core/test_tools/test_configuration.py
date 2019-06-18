from __future__ import absolute_import

from unittest import TestCase

from chart_studio.files import CONFIG_FILE, FILE_CONTENT
from chart_studio.tools import get_config_defaults


class TestGetConfigDefaults(TestCase):
    def test_config_dict_is_equivalent_copy(self):

        original = FILE_CONTENT[CONFIG_FILE]
        copy = get_config_defaults()
        self.assertIsNot(copy, original)
        self.assertEqual(copy, original)
