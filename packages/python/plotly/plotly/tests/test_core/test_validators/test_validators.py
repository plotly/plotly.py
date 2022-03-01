
from __future__ import absolute_import

from unittest import TestCase
import plotly.graph_objs as go


class TestValidators(TestCase):
    def test_layout_shape_line_dash_validator(self):
        # regression from issue #3375
        go.layout.shape.Line(color='black', width=2, dash='5px,3px,3px,2px')
