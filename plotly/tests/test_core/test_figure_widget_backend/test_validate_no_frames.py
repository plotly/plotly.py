from unittest import TestCase
import plotly.graph_objs as go
from nose.tools import raises


class TestNoFrames(TestCase):
    if 'FigureWidget' in go.__dict__.keys():
        @raises(ValueError)
        def test_no_frames_in_constructor_kwarg(self):
            go.FigureWidget(frames=[{}])

        def test_emtpy_frames_ok_as_constructor_kwarg(self):
            go.FigureWidget(frames=[])

        @raises(ValueError)
        def test_no_frames_in_constructor_dict(self):
            go.FigureWidget({'frames': [{}]})

        def test_emtpy_frames_ok_as_constructor_dict_key(self):
            go.FigureWidget({'frames': []})

        @raises(ValueError)
        def test_no_frames_assignment(self):
            fig = go.FigureWidget()
            fig.frames = [{}]

        def test_emtpy_frames_assignment_ok(self):
            fig = go.FigureWidget()
            fig.frames = []
