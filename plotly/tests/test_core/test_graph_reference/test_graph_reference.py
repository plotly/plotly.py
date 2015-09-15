"""
A module to test functionality related to *using* the graph reference.

"""
from __future__ import absolute_import

from unittest import TestCase

from plotly.graph_reference import string_to_class_name


class TestStringToClass(TestCase):

    def test_capitalize_first_letter(self):
        strings = ['a', 'bee', 'see', 'dilla']
        class_names = ['A', 'Bee', 'See', 'Dilla']
        for string, class_name in zip(strings, class_names):
            self.assertEqual(string_to_class_name(string), class_name)

    def test_capitalize_after_underscore(self):
        strings = ['any_thing', 'cat_paws']
        class_names = ['AnyThing', 'CatPaws']
        for string, class_name in zip(strings, class_names):
            self.assertEqual(string_to_class_name(string), class_name)
