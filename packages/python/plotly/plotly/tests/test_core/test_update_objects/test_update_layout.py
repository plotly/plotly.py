from unittest import TestCase
import plotly.graph_objects as go


class TestUpdateLayout(TestCase):
    def test_update_layout_kwargs(self):
        # Create initial figure
        fig = go.Figure()
        fig.layout.title.font.size = 10

        # Grab copy of original figure
        orig_fig = go.Figure(fig)

        fig.update_layout(title_font_family="Courier New")
        orig_fig.layout.update(title_font_family="Courier New")
        self.assertEqual(fig, orig_fig)

    def test_update_layout_dict(self):
        # Create initial figure
        fig = go.Figure()
        fig.layout.title.font.size = 10

        # Grab copy of original figure
        orig_fig = go.Figure(fig)

        fig.update_layout(dict(title=dict(font=dict(family="Courier New"))))
        orig_fig.layout.update(title_font_family="Courier New")
        self.assertEqual(fig, orig_fig)
