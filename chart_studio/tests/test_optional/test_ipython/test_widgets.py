"""
Module for testing IPython widgets

"""
from __future__ import absolute_import

from unittest import TestCase

from chart_studio.widgets import GraphWidget

class TestWidgets(TestCase):

    def test_instantiate_graph_widget(self):
        widget = GraphWidget
