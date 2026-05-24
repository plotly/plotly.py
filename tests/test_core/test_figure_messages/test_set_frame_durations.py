from unittest import TestCase

import plotly.graph_objs as go
from plotly.io import to_html

from unittest.mock import MagicMock

try:
    go.FigureWidget()
    figure_widget_available = True
except ImportError:
    figure_widget_available = False


class TestSetFrameDurations(TestCase):
    def _make_figure(self, n=3):
        return go.Figure(
            data=[go.Scatter(y=[1, 2, 3])],
            frames=[go.Frame(name=str(i)) for i in range(n)],
        )

    # --- set_frame_durations: valid inputs ---

    def test_scalar_sets_all_frames(self):
        fig = self._make_figure(3)
        fig.set_frame_durations(500)
        for frame in fig._frame_objs:
            self.assertEqual(frame._props["duration"], 500)

    def test_list_sets_individual_durations(self):
        fig = self._make_figure(3)
        fig.set_frame_durations([100, 200, 300])
        durations = [f._props["duration"] for f in fig._frame_objs]
        self.assertEqual(durations, [100, 200, 300])

    def test_returns_self(self):
        fig = self._make_figure(2)
        result = fig.set_frame_durations(100)
        self.assertIs(result, fig)

    def test_zero_duration_is_valid(self):
        fig = self._make_figure(2)
        fig.set_frame_durations(0)
        for frame in fig._frame_objs:
            self.assertEqual(frame._props["duration"], 0)

    def test_float_duration_is_valid(self):
        fig = self._make_figure(2)
        fig.set_frame_durations([100.5, 200.0])
        durations = [f._props["duration"] for f in fig._frame_objs]
        self.assertEqual(durations, [100.5, 200.0])

    # --- set_frame_durations: invalid inputs ---

    def test_no_frames_raises(self):
        fig = go.Figure(data=[go.Scatter(y=[1, 2, 3])])
        with self.assertRaises(ValueError):
            fig.set_frame_durations(100)

    def test_wrong_length_raises(self):
        fig = self._make_figure(3)
        with self.assertRaises(ValueError):
            fig.set_frame_durations([100, 200])

    def test_negative_duration_raises(self):
        fig = self._make_figure(2)
        with self.assertRaises(ValueError):
            fig.set_frame_durations([100, -1])

    def test_invalid_type_raises(self):
        fig = self._make_figure(2)
        with self.assertRaises(ValueError):
            fig.set_frame_durations("fast")

    def test_list_with_invalid_element_raises(self):
        fig = self._make_figure(2)
        with self.assertRaises(ValueError):
            fig.set_frame_durations([100, "slow"])

    # --- serialization ---

    def test_duration_appears_in_to_dict(self):
        fig = self._make_figure(3)
        fig.set_frame_durations([100, 200, 300])
        d = fig.to_dict()
        durations = [f["duration"] for f in d["frames"]]
        self.assertEqual(durations, [100, 200, 300])

    def test_scalar_duration_appears_in_to_dict(self):
        fig = self._make_figure(2)
        fig.set_frame_durations(500)
        d = fig.to_dict()
        durations = [f["duration"] for f in d["frames"]]
        self.assertEqual(durations, [500, 500])


class TestAnimateFrames(TestCase):
    if figure_widget_available:

        def _make_widget(self):
            fig = go.FigureWidget(data=[go.Scatter(y=[1, 2, 3])])
            fig._send_animate_msg = MagicMock()
            return fig

        def test_animate_frames_calls_batch_animate_per_frame(self):
            fig = self._make_widget()
            frames_data = [{"y": [1, 2, 3]}, {"y": [4, 5, 6]}, {"y": [7, 8, 9]}]
            durations = [100, 200, 300]
            fig.animate_frames(frames_data, durations)
            self.assertEqual(fig._send_animate_msg.call_count, 3)

        def test_animate_frames_duration_controls_frame_and_transition(self):
            fig = self._make_widget()
            fig.animate_frames([{"y": [1, 2, 3]}], [200])
            opts = fig._send_animate_msg.call_args.kwargs["animation_opts"]
            self.assertEqual(opts["frame"]["duration"], 200)
            self.assertEqual(opts["transition"]["duration"], 200)

        def test_animate_frames_length_mismatch_raises(self):
            fig = self._make_widget()
            with self.assertRaises(ValueError):
                fig.animate_frames([{"y": [1, 2]}], [100, 200])

        def test_animate_frames_negative_duration_raises(self):
            fig = self._make_widget()
            with self.assertRaises(ValueError):
                fig.animate_frames([{"y": [1, 2]}], [-100])

        def test_animate_frames_invalid_duration_type_raises(self):
            fig = self._make_widget()
            with self.assertRaises(ValueError):
                fig.animate_frames([{"y": [1, 2]}], ["fast"])

        def test_animate_frames_invalid_frames_data_type_raises(self):
            fig = self._make_widget()
            with self.assertRaises(ValueError):
                fig.animate_frames("not a list", [100])


class TestToHtmlPerFrameDurations(TestCase):
    def _make_figure_with_durations(self, durations):
        n = len(durations)
        fig = go.Figure(
            data=[go.Scatter(y=[1, 2, 3])],
            frames=[go.Frame(data=[go.Scatter(y=[i])], name=str(i)) for i in range(n)],
        )
        fig.set_frame_durations(durations)
        return fig

    def test_per_frame_html_contains_custom_js_loop(self):
        fig = self._make_figure_with_durations([200, 2000])
        html = to_html(fig, auto_play=True)
        self.assertIn("playNext", html)
        self.assertIn("frameNames", html)
        self.assertIn("durations", html)

    def test_per_frame_html_contains_correct_durations(self):
        fig = self._make_figure_with_durations([100, 5000, 300])
        html = to_html(fig, auto_play=True)
        self.assertIn("[100, 5000, 300]", html)

    def test_per_frame_html_contains_frame_names(self):
        fig = self._make_figure_with_durations([200, 400])
        html = to_html(fig, auto_play=True)
        self.assertIn('["0", "1"]', html)

    def test_no_per_frame_durations_uses_global_animate(self):
        fig = go.Figure(
            data=[go.Scatter(y=[1, 2, 3])],
            frames=[go.Frame(data=[go.Scatter(y=[i])]) for i in range(2)],
        )
        html = to_html(fig, auto_play=True)
        self.assertNotIn("playNext", html)
        self.assertIn("Plotly.animate", html)
