from unittest import TestCase
import plotly.graph_objs as go
import pytest

try:
    go.FigureWidget()
    figure_widget_available = True
except ImportError:
    figure_widget_available = False


class TestNoFrames(TestCase):
    if figure_widget_available:

        def test_no_frames_in_constructor_kwarg(self):
            with pytest.raises(ValueError):
                go.FigureWidget(frames=[{}])

        def test_emtpy_frames_ok_as_constructor_kwarg(self):
            go.FigureWidget(frames=[])

        def test_no_frames_in_constructor_dict(self):
            with pytest.raises(ValueError):
                go.FigureWidget({"frames": [{}]})

        def test_emtpy_frames_ok_as_constructor_dict_key(self):
            go.FigureWidget({"frames": []})

        def test_no_frames_assignment(self):
            fig = go.FigureWidget()
            with pytest.raises(ValueError):
                fig.frames = [{}]

        def test_emtpy_frames_assignment_ok(self):
            fig = go.FigureWidget()
            fig.frames = []
