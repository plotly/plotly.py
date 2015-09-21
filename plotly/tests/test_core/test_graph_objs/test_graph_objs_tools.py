from __future__ import absolute_import

from unittest import TestCase

from plotly import graph_reference as gr
from plotly.graph_objs import graph_objs_tools as got


class TestGetHelp(TestCase):

    def test_get_help_does_not_raise(self):

        msg = None
        try:
            for object_name in gr.OBJECTS:
                msg = object_name
                got.get_help(object_name)

            for object_name in gr.ARRAYS:
                msg = object_name
                got.get_help(object_name)

            for object_name in gr.OBJECTS:
                attributes = gr.get_valid_attributes(object_name)
                for attribute in attributes:
                    msg = (object_name, attribute)
                    got.get_help(object_name, attribute=attribute)
                fake_attribute = 'fake attribute'
                msg = (object_name, fake_attribute)
                got.get_help(object_name, attribute=fake_attribute)
        except:
            self.fail(msg=msg)
